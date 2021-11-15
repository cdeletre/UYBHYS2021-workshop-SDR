#!/usr/bin/env python3
# coding: utf-8

from sys import stdin,stdout,argv
from colored import fg, bg, attr
import socket
import json


def get_crc4(s):

    # CRC 4 polynome : x4 + x2 + x1 => b00010011 = 0x13
    CRC4POLY = 0x13
    crc = 0x0

    for ch in s:

        if (crc & 0x8):
            check = "1"
        else:
            check = "0"

        if (check != ch):
                crc = ((crc<<1) ^ CRC4POLY) & 0xf
        else:
                crc = (crc<<1) & 0xf

    return crc


C_FTYPE = fg('light_gray')
C_DTYPE = fg('white')
C_KEYID = fg('light_blue')
C_DATA = fg('light_yellow')
C_CRCOK = fg('light_green')
C_CRCKO = fg('light_red')
C_FILL = fg('dark_gray')
#C_KEY = bg('light_gray') + fg('black')
C_KEY = fg('white')
C_SYNC = fg('white')
C_RESET = attr('reset')

#SYNCTXT = u'🔄'
SYNCTXT = u'SYNC'
KBEMO=u'⌨️'
MOUSEMO=u'🐁'
DWEMO = u'⬇️  '
UPEMO = u'⬆️  '

KID=['001100111000']

FILEMAP_NAME = "./key.map"

UDP_IP_IN = argv[1]
UDP_PORT_IN = int(argv[2])
UDP_BUFFER_IN = 64

rawmod = len(argv)>= 4 and argv[3] == "raw"
verbose = len(argv)>= 5 and argv[4] == "verbose"

sock_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_in.bind((UDP_IP_IN, UDP_PORT_IN))

ftype_len = 5
dtype_len = 0
keyid_len = 12
data_len =  {}
protect_len = 4
data_len['00100'] = [11] # keystroke
data_len['00110'] = [12] # keyboard sync data ?

fmap=open(FILEMAP_NAME,'r')

keymap = json.load(fmap)

reverse_keymap = dict()

for k in keymap.keys():
  reverse_keymap[keymap[k]] = k

end = False

stack = {}

while not end:

  frame = ""

  f_channel = -1
  dtype_len = 0

  ftype = ""
  dtype = ""
  keyid = ""
  devtype = u'❓ '
  data = ""
  protect = ""
  fill = ""
  crc4 = ""

  protect_color = C_CRCKO

  packet,addr = sock_in.recvfrom(UDP_BUFFER_IN)
  message = packet.decode('utf-8')
  f_channel = ord(message[0])
  frame_len = ord(message[1])
  frame = message[2:frame_len+2]

  if frame_len > ftype_len + dtype_len:
    ftype = frame[0:ftype_len]

  if ftype == "00000":
    frame = frame[ftype_len:]
    for i,dt in enumerate(data_len):
      if dt == frame[0:len(dt)]:
        dtype_len = len(dt)
        dtype  = dt
        frame = frame[dtype_len:]
        break

    if dtype_len > 0:

      keyid = frame[0:keyid_len]
      if keyid in KID:
        devtype = KBEMO + u' '
      frame = frame[keyid_len:]
      for i,l in enumerate(data_len[dtype]):
        if l < len(frame):
          data = frame[0:l]
          frame = frame[l:]
          break

      protect = frame[0:protect_len]
      frame = frame[protect_len:]

      fill = frame

      crc4 = format( get_crc4(ftype + dtype + keyid + data), '04b')

  if crc4 == protect:
    protect_color = C_CRCOK

  if dtype == "00100" and crc4 == protect:
    action = ""
    if data[-1] == "1":
      #action = u'\u21d3 '
      action = DWEMO + u'  '
    else:
      #action = u'\u21d1 '
      action = UPEMO + u'  '
    try:
      key = reverse_keymap[data[:-1]]
    except Exception as err:
      key = "unknown" 

    if rawmod:
      stdout.write("[%s] %s%s %s%s %s%s%s %s%s\t%s%s\t%s%s\t%s%s%s\n" % (f_channel,C_FTYPE,ftype,C_DTYPE,dtype,C_KEYID,keyid,devtype,C_DATA,data,protect_color,protect,C_FILL,fill,C_KEY,action+key.strip(),C_RESET))
    else:

      if data[-1] ==  "1" and key not in stack:
        stack[ key ] = 1
        stdout.write(key)
        #stdout.flush()
      elif data[-1] == "0":
        if key in stack:
          stack.pop(key)

  elif dtype == "00110" and crc4 == protect:
    if rawmod:
      stdout.write("[%s] %s%s %s%s %s%s%s %s%s\t%s%s\t%s%s\t%s%s%s\n" % (f_channel,C_FTYPE,ftype,C_DTYPE,dtype,C_KEYID,keyid,devtype,C_DATA,data,protect_color,protect,C_FILL,fill,C_SYNC,SYNCTXT,C_RESET))

  else:
    if rawmod:
      if dtype in data_len:
        stdout.write("[%s] %s%s %s%s %s%s%s %s%s\t%s%s\t%s%s%s\n" % (f_channel,C_FTYPE,ftype,C_DTYPE,dtype,C_KEYID,keyid,devtype,C_DATA,data,protect_color,protect,C_FILL,fill,C_RESET))
      elif verbose:
        stdout.write("[%s] %s (unknown frame)\n" % (f_channel, packet[2:frame_len+2]))

  stdout.flush()
