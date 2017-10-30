
# lsusb 
# Bus 001 Device 006: ID 1546:01a7 U-Blox AG 
#
#pi@raspberrypi:~/megatron $ dmesg | grep tty
#[    0.000000] Kernel command line: 8250.nr_uarts=1 bcm2708_fb.fbwidth=1824 bcm2708_fb.fbheight=984 bcm2708_fb.fbswap=1 vc_mem.mem_base=0x3dc00000 vc_mem.mem_size=0x3f000000  dwc_otg.lpm_enable=0 console=ttyS0,115200 console=tty1 root=/dev/mmcblk0p7 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles
#[    0.000344] console [tty1] enabled
#[    0.819759] 3f201000.serial: ttyAMA0 at MMIO 0x3f201000 (irq = 87, base_baud = 0) is a PL011 rev2
#[    0.821328] console [ttyS0] disabled
#[    0.821357] 3f215040.serial: ttyS0 at MMIO 0x0 (irq = 220, base_baud = 31250000) is a 16550
#[    0.828000] console [ttyS0] enabled
#[    2.455574] systemd[1]: Expecting device dev-ttyS0.device...
#[ 7276.614777] cdc_acm 1-1.4:1.0: ttyACM0: USB ACM device
#
#~ GLL Geographic Position - Latitude / Longitude
# $--GLL,llll.ll,a,yyyyy.yy,a,hhmmss.ss,A*hh
# 1) Latitude
# 2) N or S (North or South)
# 3) Longitude
# 4) E or W (East or West)
# 5) Time (UTC)
# 6) Status A - Data Valid, V - Data Invalid
# 7) Checksum
# The NMEA 0183 Protocol 9 


import serial

ser = serial.Serial('/dev/ttyACM0')
print(ser.name)

while True:
    line = ser.readline()
    [msg, data] = line.split(',',1)
    if msg == '$GPGLL':
		[lat, latDir, lon, lonDir, time, valid, cksum] = data.split(',', 6)
		if valid == 'A':
			print('Valid data received: ') 
			print('Current latitude ' + lat + ' degrees ' + latDir)
			print('Current longitude ' + lon + ' degrees ' + lonDir)
        
ser.close()
