import time
import argparse
import sys
import copy
from os.path import join

def getDifferenceList(data, difs):
    diff = []
    for x in range(1,len(data)):
        diff.append(data[x]-data[x-1])
    difs.append(diff)
    if diff[0] == 0 and len(set(diff)) == 1:
        return 
    getDifferenceList(diff, difs)

def expandList(lists, reverse=False):
    mul = 1
    if reverse:
        for list in lists:
            list.reverse()
            mul = -1

    lists[-1].append(0)
    for list in range(len(lists)-2, -1, -1):
        #we are in, so we now expand each list using the previous element
        lists[list].append(lists[list][-1]+lists[list+1][-1]*mul)
        pass

def partOne(data):
    groups = [[int(y) for y in x.split()] for x in data]
    finalData = []
    for group in groups:
        diffs = [copy.deepcopy(group)]
        getDifferenceList(group, diffs)
        expandList(diffs)
        finalData.append(diffs[0][-1])
    return sum(finalData)

def partTwo(data):
    groups = [[int(y) for y in x.split()] for x in data]
    finalData = []
    for group in groups:
        diffs = [copy.deepcopy(group)]
        getDifferenceList(group, diffs)
        expandList(diffs, True)
        finalData.append(diffs[0][-1])
    return sum(finalData)

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