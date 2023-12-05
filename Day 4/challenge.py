import time
import argparse
import sys
import copy
from os.path import join

def partOne(data):
    points = []
    for line in data:
        key, ours = line.split(':')[1].split('|')
        key = set(key.split())
        ours = set(ours.split())
        match = key.intersection(ours)
        inital = 0
        if len(match) != 0:
            inital = 1
            for x in match:
                inital = inital*2
        points.append(inital//2)
    return sum(points)
        

def partTwo(data):
    cards = {}
    for line in data:
        game = int(line.split(':')[0].split()[1])
        key, ours = line.split(':')[1].split('|')
        key = set(key.split())
        ours = set(ours.split())
        match = key.intersection(ours)
        cards[game] = [len(match), 1]
    for line in cards:
        for match in range(1,cards[line][0]+1):
            cards[line+match][1] = cards[line+match][1]+1*cards[line][1]
    return sum([cards[x][1] for x in cards])

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