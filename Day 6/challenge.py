import time
import argparse
import sys
import copy
from os.path import join
from functools import reduce

def partOne(data):
    times = [int(x) for x in data[0].split(':')[1].split()]
    records = [int(x) for x in data[1].split(':')[1].split()]
    
    distances = []
    recordDistances = []
    for race in range(len(times)):
        time = times[race]
        record = records[race]
        raceDistance = [(time-x)*(x) for x in range(time+1)]
        distances.append(raceDistance)
        recordDistances.append([x for x in raceDistance if x > record])
    return(reduce(lambda x, y: x*y, [len(x) for x in recordDistances]))

def partTwo(data):
    time = int(''.join([x for x in data[0].split(':')[1].split()]))
    record = int(''.join([x for x in data[1].split(':')[1].split()]))

    print(record)

    raceDistance = [(time-x)*(x) for x in range(time+1)]
    recordDistances = [x for x in raceDistance if x > record]

    return(len(recordDistances))

def main(fileName):
    data = []
    with open(fileName, 'r') as file:
        data = file.readlines()

    start_time = time.time()
    
    print(partOne(data))
    print(partTwo(data))
    
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', help='use the test input or not', 
                        action='store_false', required=False)
    args = parser.parse_args()
    fileName =join(sys.path[0],( "input" if args.test else "Testinput"))
    main(fileName)