import time
import argparse
import sys
import copy
from os.path import join
from functools import lru_cache

#this allows python to remember the result of functions with matching args, it a huge speedup, since it just skips those branches.
@lru_cache(maxsize=10000, typed=False)
def findCombo(row, groups):
    #these two default returns happen if we are "out" of groups to check
    #If we have no "#" in the string we are computing, then we return 1, this is so progress on this branch does not wipe out the other
    #since there could be matches on the other side. Without this is always returns 0
    #we undercount else
    if len(groups) == 0 and row.count("#") == 0:
        return 1
    #if we get here, nothing in the numbers, we return 0, no matches here. we overcount otherwise
    if len(groups) == 0:
        return 0
    
    #get the largest group so we dont overspill the list, and its index.
    largestGroup = max(groups)
    lgi = groups.index(largestGroup)

    count  = 0
    for i in range(len(row)-largestGroup+1):
        #we dont want to consider groups with . in the middle of them
        if row[i:i+largestGroup].count('.') == 0:
            #if the index is 0, so this always happens, or if we arent right after or before a # due to needed seperation
            if i == 0 or row[i-1] != '#':
                if largestGroup+i == len(row) or row[largestGroup+i] !='#':
                    
                    #again, when we split the lists, we are actually "dropping" en element at the split point, becasue we need seperation. (meaining we drop a ? or .)
                    l = findCombo(row[:max(0,i-1)],groups[:lgi])
                    r = findCombo(row[i+largestGroup+1:],groups[lgi+1:])

                    count += l*r
    return count
    
def partOne(data):
    rows = [(row, tuple([int(num) for num in broken.split(',')])) for line in data for row, broken in [line.split()]]
    sum = 0
    for row in rows:
        sum += findCombo(row[0],row[1])    
    return sum 

def partTwo(data):
    rows = [((''.join([row+'?']*5)[:-1]), tuple([int(num) for num in broken.split(',')]*5)) for line in data for row, broken in [line.split()]]
    sum = 0
    for row in rows:
        sum += findCombo(row[0],row[1])    
    return sum 

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
    fileName =join(sys.path[0],( "input" if args.test else "TestInput"))
    main(fileName)