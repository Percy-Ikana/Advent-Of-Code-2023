import time
import argparse
import sys
import copy
from os.path import join
import itertools

def findMap(value, key, default):
    for mapping in key:
        if value in range(mapping[1], mapping[1]+mapping[2]):
            return (value+(mapping[0]-mapping[1]), default)
    return (value, default)

def findMapNR(value, key):
    for mapping in key:
        if value in mapping[1]:
            return value+mapping[2]
    return value

def findTotalMapping(value, mapKey, mapdict, fromTo):
    #if where we are asked to map is 
    if mapKey not in mapdict.keys():
        return value
    else:
        mappedVal = findMap(value, mapdict[mapKey],fromTo[mapKey])
        return (findTotalMapping(mappedVal[0], mappedVal[1], mapdict, fromTo))

def findTotalMappingNonRecursive(value, mapdict):
    return findMapNR(findMapNR(findMapNR(findMapNR(findMapNR(findMapNR(findMapNR(value, mapdict["seed"]), mapdict["soil"]),mapdict["fertilizer"]),mapdict["water"]),mapdict["light"]),mapdict["temperature"]),mapdict["humidity"])
              
def partOne(data):
    data = data.split('\n\n')
    seeds = [int(x) for x in data[0].split(':')[1].split()]
    mappings = {}
    fromTo = {}
    for category in data[1:]:
        source, dest = category.split('\n')[0].split(' ')[0].split('-to-')
        fromTo[source] = dest
        ranges = category.split('\n')[1:]
        mappings[source] = []
        for mapRange in ranges:
            destStart, rangeStart, rangeLength = mapRange.split()
            rangeLength = int(rangeLength)
            offset = int(destStart) - int(rangeStart)
            rangeStart = range(int(rangeStart),int(rangeStart)+rangeLength)
            destStart = range(int(destStart), int(destStart)+rangeLength)
            mappings[source].append((destStart, rangeStart, offset))
    
    lastLocations = {}
    for seed in seeds:
        #lastLocations[seed] = findTotalMapping(seed,'seed', mappings, fromTo)
        lastLocations[seed] = findTotalMappingNonRecursive(seed, mappings)
    return min([lastLocations[x] for x in lastLocations.keys()])
    #now we have the values and thier maps, time to start from the top, seeds, and go down


def partTwo(data):
    data = data.split('\n\n')
    seeds = [int(x) for x in data[0].split(':')[1].split()]
    mappings = {}
    fromTo = {}
    for category in data[1:]:
        source, dest = category.split('\n')[0].split(' ')[0].split('-to-')
        fromTo[source] = dest
        ranges = category.split('\n')[1:]
        mappings[source] = []
        for mapRange in ranges:
            destStart, rangeStart, rangeLength = mapRange.split()
            rangeLength = int(rangeLength)
            offset = int(destStart) - int(rangeStart)
            rangeStart = range(int(rangeStart),int(rangeStart)+rangeLength)
            destStart = range(int(destStart), int(destStart)+rangeLength)
            mappings[source].append((destStart, rangeStart, offset))
    
    #we need to calc all the seeds
    seeds = set()
    tupes = [int(x) for x in data[0].split(':')[1].split()]
    tuples = []
    for group in range(0, len(tupes), 2):
        tuples.append(range(tupes[group], tupes[group]+tupes[group+1]))
    lastLocations = sys.maxsize
    print(sum([len(x) for x in tuples]))
    for group in tuples:
        for seed in group:
            #lastLocations = min(findTotalMapping(seed, "soil", mappings, fromTo), lastLocations)
            lastLocations = min(findTotalMappingNonRecursive(seed, mappings), lastLocations)
        print("finished group " + str(tuples.index(group)) + " out of " + str(len(tuples)))
    return lastLocations
    #now we have the values and thier maps, time to start from the top, seeds, and go down

def main(fileName):
    data = []
    with open(fileName, 'r') as file:
        data = file.read()

    start_time = time.time()
    
    print(partOne(data))
    print(partTwo(data))
    
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', help='use the test input or not', 
                        action='store_false', required=False)
    args = parser.parse_args()
    fileName =join(sys.path[0],( "input" if args.test else "TestInput"))

    main(fileName)