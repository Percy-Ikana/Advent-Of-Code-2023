import time
import argparse
import sys
import copy
from os.path import join
from functools import cmp_to_key

cardValues = { 'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, 
              '6':6, '5':5, '4':4, '3':3, '2':2 }

cardValuespt2 = { 'A':14, 'K':13, 'Q':12, 'J':0, 'T':10, '9':9, '8':8, '7':7, 
              '6':6, '5':5, '4':4, '3':3, '2':2 }

handValues = {'5 of kind':7, 'four of kind':6, 'full house':5, 
              'three of kind':4, 'two pair':3, 'one pair':2, 'high card':1}

def returnHighestValue(handCounts):
    sortedCounts = sorted(handCounts, key=lambda item: item[1],\
                                reverse=True)
    if len(sortedCounts) in [2,3]:
        if cardValues[sortedCounts[0][0]] > cardValues[sortedCounts[1][0]]:
            return sortedCounts[0][0]
        else: return sortedCounts[1][0]
    return sortedCounts[0][0]

def getType(hand):
    counts = (sorted({x:hand.count(x) for x in set(hand)}.items(), \
                         key=lambda item: (item[1],cardValues[item[0]]), \
                            reverse=True))
    high = counts[0][0]
    if len(counts) == 1:
        return ('5 of kind', high)
    if len(counts) == 5:
        return ('high card', high)
    if len(counts) == 4:
        return ('one pair',high)
    if len(counts) == 3:
        if counts[0][1] == 3:
            return ('three of kind',high)
        if counts[0][1] == 2:
            return ('two pair',high)
    if len(counts) == 2:
        if counts[0][1] == 4:
            return ('four of kind',high)
        if counts[0][1] == 3:
            return ('full house',high)
        
def getTypePt2(hand):
    counts = dict(sorted({x:hand.count(x) for x in set(hand)}.items(), \
                         key=lambda item: (item[1],cardValues[item[0]]), \
                            reverse=True))
    joker = 0
    if 'J' in counts.keys() and counts['J'] != 5:
        #we have a joker, more cards are always worth more than pairs, so we just add it to the top card
        joker = counts.pop('J')
    counts = list(counts.items())
    counts[0] = (counts[0][0], counts[0][1] + joker)
    high = list(counts)[0][0]
    if len(counts) == 1:
        return ('5 of kind', high)
    if len(counts) == 5:
        return ('high card', high)
    if len(counts) == 4:
        return ('one pair',high)
    if len(counts) == 3:
        if counts[0][1] == 3:
            return ('three of kind',high)
        if counts[0][1] == 2:
            return ('two pair',high)
    if len(counts) == 2:
        if counts[0][1] == 4:
            return ('four of kind',high)
        if counts[0][1] == 3:
            return ('full house',high)
        
def compHands(hand1,hand2):
    #If the hands dont have the same "rank" of matching, we can compare
    # them using only that
    if hand1[0][0] != hand2[0][0]:
        return handValues[hand1[0][0]] - handValues[hand2[0][0]]
    else:
        #thier ranks match, so we have to return based on the card rules
        for elem in range(len(hand1[2])):
            if hand1[2][elem] != hand2[2][elem]:
                return cardValues[hand1[2][elem]] - cardValues[hand2[2][elem]]
    return 0

def compHandsPt2(hand1,hand2):
    #If the hands dont have the same "rank" of matching, we can compare 
    #them using only that
    if hand1[0][0] != hand2[0][0]:
        return handValues[hand1[0][0]] - handValues[hand2[0][0]]
    else:
        #thier ranks match, so we have to return based on the card rules
        for elem in range(len(hand1[2])):
            if hand1[2][elem] != hand2[2][elem]:
                return cardValuespt2[hand1[2][elem]] - \
                        cardValuespt2[hand2[2][elem]]
    return 0

def partOne(data):
    values = sorted([(getType(line.strip().split()[0]),\
              int(line.strip().split()[1]),line.strip().split()[0]) \
              for line in data], key=cmp_to_key(compHands))
    return(sum([values[x][1]*(x+1) for x in range(len(values))]))

def partTwo(data):
    values = sorted([(getTypePt2(line.strip().split()[0]),\
              int(line.strip().split()[1]),line.strip().split()[0]) \
              for line in data], key=cmp_to_key(compHandsPt2))
    return(sum([values[x][1]*(x+1) for x in range(len(values))]))

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
