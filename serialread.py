import serial

ser = serial.Serial(
    port='1',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)


print("connected to:" + ser.portstr)

line = []

while True:
    for c in ser.read():
        line.append(c)
        if c == '\n':
            print("Line:" + ''.join(line))
            line = []
            break

ser.close()
