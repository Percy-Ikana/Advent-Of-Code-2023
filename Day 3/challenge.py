import time
import argparse
import sys
import copy
from os.path import join

def findNumber(gridDict, pos):
    #we have a dict of a grid, and have to build the numbers it contains
    line = list(gridDict[pos[0]].keys())
    splits = [x for x in range(1,len(line)+1) if (x == len(line)) \
              or ((abs(line[x-1]-line[x])) != 1)]
    splits.insert(0,0)
    nums = []
    #we now have where the lines split, so we can build a list of numbers,
    #and the sets of coords they take up
    for split in range(len(splits)):
        if split is not 0:
            numbers = line[splits[split-1]:splits[split]]
            spots = set()
            num = []
            for numPos in numbers:
                num.append(str(gridDict[pos[0]][numPos]))
                spots.add((pos[0],numPos))
            pass
            nums.append((int(''.join(num)), spots))
    for entry in nums:
        if pos in entry[1]:
            if entry[0] == 75:
                pass
            return entry

def getGrid(data):
    gridDict = {}
    symbols = set({})
    for line in range(len(data)): 
        gridDict[line] = {}
        for elem in range(len(data[line])):
            if data[line][elem] is not '.':
                if data[line][elem].isdigit():
                    gridDict[line][elem] = int(data[line][elem])
                elif data[line][elem] != '.' and data[line][elem] != '\n':
                    symbols.add((data[line][elem],(line,elem)))
    return [gridDict, symbols]
    
def partOne(data):
    
    gridDict, symbols = getGrid(data)
    parts = []
    foundcoords = []
    for symbol, coords in symbols:
        #check the grid around the symbols to find a number
        for xoff in range(-1,2):
            x = xoff + coords[0]
            if (x in gridDict.keys()):
                for yoffset in range(-1,2):
                    y = yoffset + coords[1]
                    if y in gridDict[x].keys():
                        #we have a valid position that contains a number
                        value = findNumber(gridDict, (x,y))
                        if value != None and value[1] not in foundcoords:
                            parts.append(value[0])
                            foundcoords.append(value[1])
    return sum(parts)
                        
def partTwo(data):
    gridDict, symbols = getGrid(data)
    
    ratios = []
    for symbol, coords in symbols:
        #check the grid around the symbols to find a number
        parts = []
        foundcoords = []
        if symbol == '*':
            for xoff in range(-1,2):
                x = xoff + coords[0]
                if (x in gridDict.keys()):
                    for yoffset in range(-1,2):
                        y = yoffset + coords[1]
                        if y in gridDict[x].keys():
                            #we have a valid position that contains a number
                            value = findNumber(gridDict, (x,y))
                            if value != None and value[1] not in foundcoords:
                                parts.append(value[0])
                                foundcoords.append(value[1])
            if len(parts) == 2:
                ratios.append(parts[0]*parts[1])
    return sum(ratios)

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