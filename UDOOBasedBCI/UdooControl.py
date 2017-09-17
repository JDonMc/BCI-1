import serial
import time

# check /dev/ttyS0 or ttyMCC
ser = serial.Serial('/dev/ttyMCC', 115200, timeout=1)
ser.flushOutput()

print('Serial connected')

runCase = 1

NetworkConfig = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
NetworkSize = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
NetworkOutput = ['Please', 'Phone', 'Computer', 'Headtop', 'Up', 'Down', 'Left', 'Right', 'In', 'Out', 'Click', 'Search', 'Add', 'Remove', 'Cancel', 'Thanks']


# ready to be tested
def write_to_file(filename, array):
    actual_file_name = filename + '.txt'
    writefile = open(actual_file_name, 'w+')
    writefile.write('nextLearning')
    writefile.write(str(len(array)))
    writefile.writelines(array)
    writefile.close()


# ready to be tested
def read_from_file(filename, learning):
    actual_file_name = filename + '.txt'
    readfile = open(actual_file_name, 'r')
    lines = readfile.readlines()  # might need to use .split(',')
    count = 0
    array = 0
    for line in range(0, len(lines)):
        if lines[line] == 'nextLearning':
            count += 1
        if count == learning:
            array_length = int(lines[line+1])
            array = lines[line+2:line+2+array_length]
    readfile.close()
    return array


ser.write("ready".encode())
while runCase == 1:
    readOne = ser.read(7)
    if readOne == 'getNetworkConfig':
        ser.write(len(NetworkConfig).encode())
        for i in range(0, len(NetworkConfig)):
            readTwo = ser.read(7)
            if readTwo == i:
                ser.write(NetworkConfig[i].encode())
    if readOne == 'getNetworkSize':
        ser.write(len(NetworkSize).encode())
        for i in range(0, len(NetworkSize)):
            readTwo = ser.read(7)
            if readTwo == i:
                ser.write(NetworkSize[i].encode())
    if readOne == 'getNetworkOutput':
        ser.write(len(NetworkOutput).encode())
        for i in range(0, len(NetworkOutput)):
            readTwo = ser.read(7)
            if readTwo == i:
                ser.write(NetworkOutput[i].encode())
    if readOne == 'learn10times':
        output = ser.read(7)
        for i in range(0, 10):
            readTwo = ser.read(7)
            if readTwo == 'getIthLength':
                IthPart = read_from_file(output, i)
                ser.write(len(IthPart).encode())
                for x in range(0, len(IthPart)):
                    readThree = ser.read(7)
                    if readThree == x:
                        ser.write(IthPart[x].encode())
    if readOne == 'test10times':
        output = ser.read(7)
        for i in range(0, 10):
            readTwo = ser.read(7)
            if readTwo == 'b\'gIL\'':
                IthPart = read_from_file(output, 10+i)
                ser.write(len(IthPart).encode())
                for x in range(0, len(IthPart)):
                    readThree = ser.read(7)
                    if readThree == x:
                        ser.write(IthPart[x].encode())
    if readOne == 'learn10times':
        ser.write('length'.encode())
        length = ser.read(7)  # may need to handshake this
        ser.write('output'.encode())
        output = ser.read(7)
        to_save = []
        for i in range(0, length):
            ser.write(i.encode())
            to_save[i] = ser.read(7)
        write_to_file(output, to_save)
    if readOne == 'Record?':
        ser.write('what'.encode())
        output = ser.read(7)
        print(output)
        record_input = input('Record?')
        if record_input == 'y':
            ser.write(record_input.encode())
        else:
            break

print('Game Over')
