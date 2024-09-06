import hid
import os

######
WRITE_BYTES_UNIT = 48
######

progress_percent = 0
error_log = ""

def device_read_and_check_valid():
    global device
    ret = device.read(64)
    if ret[0] == 255:
        error_log = "error: TP78_knob should enter the firmware update mode!!!"
        print(error_log)
        return -1
    return 0

def firmware_download_progress(firmware_path):
    global device
    global progress_percent
    global error_log
    if (os.path.exists(firmware_path) == False):
        error_log = "The firmware is not found!!"
        print(error_log)
        return

    devices = hid.enumerate()
    via_device = 0

    for device in devices:
        if device['vendor_id'] == 0x418 and device['product_id'] == 0x78A1 and device['product_string'] == 'TP78_foc' and device['usage_page'] == 0xFF60:
            via_device = device

    if via_device == 0:
        error_log = "TP78_konb is not found!!"
        print(error_log)
        return

    device = hid.device()
    device.open_path(via_device['path'])

    f = open(firmware_path, 'rb')
    s = f.read()
    addr = 0
    progress_percent = 0
    wlist = [0 for i in range(64)]

    # start to update
    wlist[0] = 0 # report id
    wlist[1] = 0x78
    device.write(wlist)
    if device_read_and_check_valid() != 0:
        return

    while True:
        wlist[0] = 0 # report id
        wlist[1] = 0x79
        wlist[2] = (addr >> 24) & 0xFF
        wlist[3] = (addr >> 16) & 0xFF
        wlist[4] = (addr >> 8) & 0xFF
        wlist[5] = (addr & 0xFF)
        wlist[6] = WRITE_BYTES_UNIT
        for i in range(7, 7 + WRITE_BYTES_UNIT):
            if (addr == len(s)):
                wlist[i] = 0xFF
                wlist[6] -= 1
            else:
                wlist[i] = s[addr]
                addr += 1
        device.write(wlist)
        if device_read_and_check_valid() != 0:
            return
        if progress_percent != int(addr * 100 / len(s)):
            progress_percent = int(addr * 100 / len(s))
            print("update progress: %d/%d bytes (%d%%)" % (addr, len(s), progress_percent))
        if (addr == len(s)):
            break

    # end to update
    wlist[0] = 0
    wlist[1] = 0x7A
    device.write(wlist)
    #device_read_and_check_valid()

    device.close()
    progress_percent = 100
