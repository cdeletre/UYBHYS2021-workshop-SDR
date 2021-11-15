# UYBHYS 2021: SDR workshop quick recap and bonus

![workshop_uybhys_cyril_celetre-](https://github.com/cdeletre/UYBHYS2021-workshop-SDR/raw/main/media/pics/workshop_uybhys_cyril_deletre.jpg)

## Slides

You can get the slides here: [UYBHYS2021-workshop-SDR.pdf](https://github.com/cdeletre/UYBHYS2021-workshop-SDR/raw/main/UYBHYS2021-workshop-SDR.pdf)

## Hardware

During the workshop we've used an RTL-SDR dongle to record the RF. You can get one from [www.passion-radio.fr](https://www.passion-radio.fr/recepteurs-sdr/rtl-sdr-r820t2-248.html) for few bucks.

## In practice

### WBFM receiver

[wbfm.grc](https://github.com/cdeletre/UYBHYS2021-workshop-SDR/tree/main/gnuradio/wbfm/wbfm.grc) is a working graphflow of the WBFM receiver we built together during the workshop. It should work with your own RTL-SDR USB dongle. 

If you don't have an RTL-SDR USB dongle you can use [wbfm.grc](https://github.com/cdeletre/UYBHYS2021-workshop-SDR/tree/main/gnuradio/wbfm/wbfm_simu.grc) which generate a fake WBFM activity from two recorded file `fm1.cs8` and `fm2.cs8`. You may need to update in the graphflow the path of this two files in the two `File source` blocks. Then you need to tune the parameters to hear one of the two channels and don't forget the `Low Pass Filter` **;)**

### logitechex110

[logitechex110\_dual\_simu.grc](https://github.com/cdeletre/UYBHYS2021-workshop-SDR/tree/main/gnuradio/logitechex110/logitechex110_dual_simu.grc) is a working graphflow that demodulates the radio transmissions of a Logitech EX110 keyboard. Then additionnal processing is needed to decode the [Miller encoding](https://en.wikipedia.org/wiki/Modified_frequency_modulation), process the payload and get the keystroke.

You will need to update the path to `gqrx_20180105_132052_27120000_240000_fc_password.raw` in the `File source` block. Then regerate the `.py` file in **GNURadio** (`Run -> Generate` or press `F5`) and follow the instructions:

	Run the following commands in 4 terminals:

	./millerudp.py 127.0.0.1 9000 127.0.0.1 1234 0
	./millerudp.py 127.0.0.1 9001 127.0.0.1 1234 1
	./ex110.py 127.0.0.1 1234 raw
	./logitechex110_dual_simu.py

	NOTE:
	ex110.py may be run without 'raw' option to only show the key pressed
	Launch logitechex110_dual_simu.py instead of logitech110_dual.py for simulation (playing radio record in loop)

You should see in the QT window each step of the demodulation and in the terminal the keystrokes that have been pressed:

	[1] 00000 00100 001100111000⌨️  00010100011  1010  000 ⬇️    M
	[1] 00000 00100 001100111000⌨️  00010100011  1010  000 ⬇️    M
	[1] 00000 00100 001100111000⌨️  00010100010  1001  00  ⬆️    M
	[1] 00000 00100 001100111000⌨️  00010100010  1001  00  ⬆️    M
	[1] 00000 00100 001100111000⌨️  00010110101  0101  000 ⬇️    Y
	[1] 00000 00100 001100111000⌨️  00010110101  0101  000 ⬇️    Y
	[1] 00000 00100 001100111000⌨️  00010110100  0110  000 ⬆️    Y
	[1] 00000 00100 001100111000⌨️  00010110100  0110  000 ⬆️    Y
	[1] 00000 00100 001100111000⌨️  00010001101  0001  000 ⬇️    P
	[1] 00000 00100 001100111000⌨️  00010001101  0001  000 ⬇️    P
	[1] 00000 00100 001100111000⌨️  00010001100  0010  00  ⬆️    P
	[1] 00000 00100 001100111000⌨️  00010001100  0010  00  ⬆️    P
	[1] 00000 00100 001100111000⌨️  00000010101  0001  000 ⬇️    A
	[1] 00000 00100 001100111000⌨️  00000010101  0001  000 ⬇️    A
	[1] 00000 00100 001100111000⌨️  00000010100  0010  00  ⬆️    A
	[1] 00000 00100 001100111000⌨️  00000010100  0010  00  ⬆️    A



## Softwares

### GQRX

[GQRX](https://gqrx.dk/) is an SDR receiver that can be use to analyze the radio spectrum and perform basic demodulation.

### Gnuradio

[GNURadio](https://www.gnuradio.org/) is a complete toolkit to manipulate radio signal with a python script generated from graphflow. It's also a good choice to manipulate offline RawIQ (RF recording).

### Inspectrum

[Inspectrum](https://github.com/miek/inspectrum) is a tool which can be used to make a quick analyze of a radio signals such as: measuring baudrate, decoding and comparing consecutive transmissions.

## IQ files

RF can be recorded in various IQ files formats such as

| Format | File extension | Application |
| :-- | :-- | :-- |
| Complex 32-bit floating point samples | *.cf32, *.cfile  | GNURadio, osmocom_fft, GQRX |
| Complex 16-bit signed integer samples | *.cs16 | BladeRF |
| Complex 8-bit signed integer samples | *.cs8 | HackRF |
| Complex 8-bit unsigned integer samples | *.cu8 | RTL-SDR |
| WAV file 16-bit stereo | *.wav | SDR# |

Conversion between these formats can be done easily with SoX see [howto](https://github.com/cdeletre/pachydermata/blob/master/sdr/iqformats.md).

## SDR related twitter accounts

| account | subjects |
| --- | :-- |
| [@r2x0t](https://twitter.com/r2x0t) | SpaceX Falcon video downlink decoding |
| [@mrn_status](https://twitter.com/mrn_status) | Updates from @nasa's Mars Relay Network, relaying data between Mars landers and Earth. |
| [@SignalCapture](https://twitter.com/SignalCapture) | RF-Hacking Contest |
| [@F5OEOEvariste](https://twitter.com/F5OEOEvariste) | creator of RPiTX, reverse RF protocol, Digital TV and SDR |
| [@rf_hacking](https://twitter.com/rf_hacking) | Various SDR topics |
| [@RadioHacking](https://twitter.com/RadioHacking) | Various SDR topics (spanish) |
| [@windyoona](https://twitter.com/windyoona) | RDS decoder, Capturing PAL video with an SDR, lot of stuffs. Check her site [http://www.windytan.com](https://www.windytan.com) |
| [@FlUxIuS](https://twitter.com/FlUxIuS) | Networks and computer security engineer in #Wireless systems, #SDR, #Mobile, #CarHacking and #IoT [penthertz.com](https://penthertz.com/) |
| [@F4DAV](https://twitter.com/F4DAV) | QO-100 satellite, various SDR projects |
| [@furrtek](https://twitter.com/furrtek) | Various SDR hacking subjects like |
| [@RatZillaS](https://twitter.com/RatZillaS) | PoC with SDR like 4G emergency messages or wireless backup internet in case of disaster |
| [@BadgeWizard](https://twitter.com/BadgeWizard) | Various SDR hack like traffic lights |
| [@michaelossmann](https://twitter.com/michaelossmann) | Designer of HackRF |
| [@csete](https://twitter.com/csete) | Creator of GQRX |