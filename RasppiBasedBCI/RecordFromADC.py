import RPi.GPIO as IO
import time

IO.setwarnings(False)  # do not show any warnings
binary_pins = [4, 17, 27, 22, 5, 6, 13, 19]  # order the following from least to most significant bit
NetworkOutput = ['Please', 'Phone', 'Computer', 'Headtop', 'Up', 'Down', 'Left', 'Right', 'In', 'Out', 'Click',
                 'Search', 'Add', 'Remove', 'Cancel', 'Thanks']
time_per_recording = 2  # time in seconds
time_between_data_points = 0.01  # time in seconds
time_to_wait_for_data_confirmation = 0.001  # time in seconds
repeats_per_output = 40
points_per_set = time_per_recording / time_between_data_points


def setup_pins(pins):
    IO.setmode(IO.BCM)
    b = bytearray[len(pins)]
    for n in range(0, len(pins), 1):
        IO.setup(pins[n], IO.IN)
        b[n] = 0


def write_to_file(filename, array):
    actual_file_name = filename + '.txt'
    writefile = open(actual_file_name, 'w+')
    writefile.write('nextLearning')
    writefile.write(str(len(array)))
    writefile.writelines(array)
    writefile.close()


def read_pins(pins, time_to_wait):
    x = 0
    b = int[len(pins)]
    for n in range(0, len(pins), 1):
        if IO.input(pins[n]):
            time.sleep(time_to_wait)
            if IO.input(pins[n]):
                b[n] = 1
                x += b[n] * (2 ^ n)
                b[n] = 0
    return x


setup_pins(binary_pins)

for x in range(0, len(NetworkOutput), 1):
    for y in range(0, repeats_per_output, 1):
        data_points = int[points_per_set]
        for data_point in range(0, points_per_set, 1):
            data_points[data_point] = read_pins(binary_pins, time_to_wait_for_data_confirmation)
            time.sleep(time_between_data_points)  # wait for 10ms
        write_to_file(NetworkOutput[x], data_points)

