import time
import argparse
import sys
import copy
from os.path import join

def partOne(data):
    gamesDict = {}
    reqsDict = {'red':12,'green':13,'blue':14}
    for each in data:
        game, info = each.split(':')
        setDict = {}
        for gameSet in info.split(';'):
            for draw in gameSet.split(','):
                for number, color in [draw.split()]:
                    if color in setDict.keys():
                        if setDict[color] < int(number):
                            setDict[color] = int(number)
                    else:
                       setDict[color] = int(number) 
        #I dont know how to make this not overwrite if a current elem is greater, so... all that fancy for nothing. 
        #gamesDict[game] = {color:number for set in info.split(';') for draw in set.split(',') for number, color in [draw.split()]}
        gamesDict[int(game.split()[1])] = copy.deepcopy(setDict)
    total = 0
    totalPower = 0
    for game in gamesDict.keys():
        possible = True
        power = 1
        for req in reqsDict.keys():
            if req in gamesDict[game].keys():
                power = power * gamesDict[game][req]
                if gamesDict[game][req] > reqsDict[req]:
                    possible=False
        if possible:
            total = total + game
        totalPower = totalPower + power
    return str(total) + '\n' + str(totalPower)

def main(fileName):
    data = []
    with open(fileName, 'r') as file:
        data = file.readlines()

    start_time = time.time()

    print(partOne(data))
    
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', help='use the test input or not', action='store_false', required=False)
    args = parser.parse_args()
    fileName =join(sys.path[0],( "input" if args.test else "Testinput"))
    main(fileName)