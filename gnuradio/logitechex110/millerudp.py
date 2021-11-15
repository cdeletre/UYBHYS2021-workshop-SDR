#!/usr/bin/env python3
from sys import argv
from sys import stdout
from time import time
from math import ceil
from binascii import hexlify
import socket

UDP_IP_IN = argv[1]
UDP_PORT_IN = int(argv[2])
UDP_BUFFER_IN = 1472

UDP_IP_OUT = argv[3]
UDP_PORT_OUT = int(argv[4])
UDP_BUFFER_OUT = 64

CHAN = int(argv[5])


sock_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_in.bind((UDP_IP_IN, UDP_PORT_IN))

sock_out = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

min_training_lock = 10
min_symbol_dur = 2
max_symbol_delta = 0.2

symbol_ratio_S = 1.0
symbol_ratio_M = 1.5
symbol_ratio_L = 2.0
symbol_ratio_SS = 3.0

preamble_symbols = []
average_dur = 0
shift_SM = 0
shift_ML = 0
shift_LSS = 0
prevb = "\x00"
symbol_dur = 0

stream = []
frame = 0x00
frame_len = 0

start = False
trained = False


#data, addr = sock_in.recvfrom(UDP_BUFFER_IN)	
#t_recv = time()
#data_rcv = UDP_BUFFER_IN>>4

#stdout.write("estimate sps: " + " "*10 )
#stdout.flush()

while True:
        data, addr = sock_in.recvfrom(UDP_BUFFER_IN)	
        #data_rcv += UDP_BUFFER_IN>>4
        #stdout.write("\b"*10 + format( int(data_rcv / (time() - t_recv)),' 10d') )
        #stdout.flush()

        for i,b in enumerate(data):

                switched = (b != prevb)

                if switched:
                        if symbol_dur < min_symbol_dur:
                                # Not good
                                start = False
                                stop = False
                                stream = []
                                frame = 0x00
                                frame_len = 0
                                preamble_symbols = []

                        elif trained and start:

                                if abs(symbol_dur - average_dur * symbol_ratio_S) <= shift_SM:
                                        # short
                                        stream.append(stream[-1])
                                        frame = frame<<1 | frame & 0x01
                                        frame_len += 1
                                        
                                elif symbol_dur >= (average_dur * symbol_ratio_M - shift_SM) and symbol_dur <= (average_dur * symbol_ratio_M + shift_ML):
                                        # medium
                                        if stream[-1] == "0":
                                                stream.append("1")
                                        else:
                                                stream.append("0")
                                                stream.append("0")
                                                

                                        if (frame & 0x01) == 0x00:
                                                frame = frame<< 1 | 0x01
                                                frame_len += 1
                                        else:
                                                frame = frame<< 2
                                                frame_len += 2

                                elif symbol_dur >= (average_dur * symbol_ratio_L - shift_ML) and symbol_dur <= (average_dur * symbol_ratio_L + shift_LSS):
                                        # long
                                        stream.append("0")
                                        stream.append("1")
                                        frame = frame<<2 | 0x01
                                        frame_len += 2
                                elif abs(symbol_dur - average_dur * symbol_ratio_SS) <= shift_LSS:
                                        # stop
                                        message = chr(CHAN) + chr(frame_len) + format(frame,"0%sb" % frame_len) + "\n"+"\x00"*(UDP_BUFFER_OUT - len(stream) - 3)
                                        sock_out.sendto(message.encode('utf-8'), (UDP_IP_OUT, UDP_PORT_OUT))
                                        stream = []
                                        frame = 0x00
                                        frame_len = 0
                                        start = False
                                else:
                                        # need to sync again
                                        message = chr(CHAN) + chr(frame_len) + format(frame,"0%sb" % frame_len) + "\n"+"\x00"*(UDP_BUFFER_OUT - len(stream) - 3)
                                        sock_out.sendto(message.encode('utf-8'), (UDP_IP_OUT, UDP_PORT_OUT))
                                        trained = False
                                        preamble_symbols = []
                                        start = False
                                        frame = 0x00
                                        frame_len = 0
                        elif trained:

                                if abs(symbol_dur - average_dur * symbol_ratio_SS) <= shift_LSS:
                                        start = True
                                        stream = ["0"]
                                        frame = 0x00
                                        frame_len = 1

                        else:
                                # training phase
                                if len(preamble_symbols) > 0:
                                        average_dur = int(sum(preamble_symbols) / len(preamble_symbols))
                                        shift_SM = int(average_dur * (symbol_ratio_M - symbol_ratio_S) / 2.0)
                                        shift_ML = int(average_dur * (symbol_ratio_L - symbol_ratio_M) / 2.0)
                                        shift_LSS = int(average_dur * (symbol_ratio_SS - symbol_ratio_L) / 2.0)


                                        if len(preamble_symbols) >= min_training_lock and abs(symbol_dur - average_dur * symbol_ratio_SS) <= shift_LSS:
                                                # start detected
                                                stream = ["0"]
                                                frame = 0x00
                                                frame_len = 1
                                                trained = True
                                                start = True
                                                #print("average_dur %s shift_SM %s shift_ML %s shift_LSS %s" % (average_dur,shift_SM,shift_ML,shift_LSS))
                                        else:
                                                # may be a new preamble symbol
                                                preamble_symbols.append(symbol_dur)

                                                # remove old preamble symbol if not within delta limit
                                                while (max(preamble_symbols) - min(preamble_symbols))/2.0 > (sum(preamble_symbols) / len(preamble_symbols)) * max_symbol_delta:
                                                        preamble_symbols = preamble_symbols[1:]

                                else:
                                        # this is our first symbol
                                        preamble_symbols.append(symbol_dur)

                        symbol_dur = 1
                else:
                        symbol_dur +=1

                prevb = b


