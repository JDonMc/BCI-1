import serial
# import time

# check /dev/ttyS0 or ttyMCC
ser = serial.Serial('/dev/ttyMCC', 115200, timeout=1)
ser.flushOutput()

print('Serial connected')

runCase = 1
NetworkOutput = ['Please', 'Phone', 'Computer', 'Headtop', 'Up', 'Down', 'Left', 'Right', 'In', 'Out', 'Click',
                 'Search', 'Add', 'Remove', 'Cancel', 'Thanks']


def write_to_file(filename, array):
    actual_file_name = filename + '.txt'
    writefile = open(actual_file_name, 'w+')
    writefile.write('nextLearning')
    writefile.write(str(len(array)))
    writefile.writelines(array)
    writefile.close()


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


def convert_and_send_int(int_int):
    # value = list(str(int_int))
    # data = [b"i"]  # means int incoming
    # for char in value:
    #     data.append(char.encode())
    data = str(int_int)
    ser.write(data)


def receive_decode_to_int():
    return ser.readline()[:-2].decode()  # get arduino to println("")

# the question is length of int able to send/receive
convert_and_send_int(runCase)
print("runCase written")
while runCase == 1:
    readOne = receive_decode_to_int()
    print(readOne)
    if readOne == 9999:  # to Transmit LT
        convert_and_send_int(9999)  # to get length
        length = receive_decode_to_int()
        convert_and_send_int(9999)  # to get output location
        output_location = receive_decode_to_int()
        to_save = []
        for i in range(0, length):
            to_save[i] = receive_decode_to_int()
            print(to_save)
        # write_to_file(NetworkOutput[outputlocation], to_save)
    if readOne == 9998:  # to begin Recording said output
        convert_and_send_int(9998)  # to get output location
        output_location = receive_decode_to_int()
        print(NetworkOutput[output_location])
        record_input = input('Rec? (y/other)')
        if record_input == 'y':
            convert_and_send_int(9998)
        else:
            print('Game Over')
            break
