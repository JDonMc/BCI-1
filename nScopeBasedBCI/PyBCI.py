import nScopePy as ns       # import the nScopePy module
import sys
sys.path.append('../')  # add the path to the library to our path

NetworkOutput = ['Please', 'Phone', 'Computer', 'Head_top', 'Up', 'Down', 'Left', 'Right', 'In', 'Out', 'Click',
                 'Search', 'Add', 'Remove', 'Cancel', 'Thanks']

# open a connection to nScope
nScope = ns.nScopeObj()

sampleRate = 4096.0         # Hz
numSamples = 2048           # number of samples per channel
number_of_data_blocks = 40  # number of repeated learnings

# Turn on the appropriate channels (ch1,ch2,ch3,ch4)
nScope.setChannelsOn(1, 0, 0, 0)
nScope.setSampleRateInHz(sampleRate)
nScope.requestData(numSamples)

'''
Note that if sample rate is faster than 16k samples/sec
a 3200 (total) sample limit is enforced.
In this case, the above function will return an invalid request error
'''


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

# initialize data lists
ch1 = []

for i in range(0, len(NetworkOutput), 1):
    for j in range(0, number_of_data_blocks, 1):
        print(NetworkOutput[i])
        record_input = input('Record?')
        if record_input == 'y':
            while nScope.requestHasData():
                # read from channel 1
                voltage = nScope.readData(1)
                ch1.append(voltage)
            write_to_file(NetworkOutput[i], ch1)
            ch1 = []
        else:
            print("That'll do donkey, i: " + str(i) + ", j: " + str(j))
            break


# do something with the returned data
print ch1

