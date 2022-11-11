import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.reset_input_buffer()
    f = open("/home/rail-communication/rail-communication/file.txt", 'r')

    x = ""
    start = time.time()
    b = 0
    a = f.read(1024).encode('utf-8')

    while a:
        n = ser.write(a)
        a = f.read(1024).encode('utf-8')
        print("Raspberry Pi: sent",n," bytes")
        #x += ser.read(2048).decode('utf-8').rstrip()
        x = ser.read(2048).decode('utf-8').rstrip()
        print(x)
        b += n

    #print(x)
    print("\nSent",b,"bytes in", time.time() - start, "seconds")
