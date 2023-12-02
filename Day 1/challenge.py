import time
import argparse
import sys
import copy
from os.path import join

def partOne(data):
    cali = []
    for line in data:
        digits = [x for x in line if x.isdigit()]
        cali.append(int(digits[0]+digits[-1]) if len(digits)>0 else 0)
    print(sum(cali))

def partTwo(data):
    listNum = [('one',1),('two',2),('three',3),('four',4),('five',5),('six',6),('seven',7),('eight',8),('nine',9)]
    cali = []
    for line in data:
        earliestNumber = ('',1000)
        latestNumber = ('',-1)
        earldig = ('',1000)
        latedig = ('',-1)
        for string, number in listNum:
            if line.find(string) < earliestNumber[1] and line.find(string) != -1:
                earliestNumber = (number,line.find(string))
            if line.rfind(string) > latestNumber[1] and line.rfind(string) != -1:
                latestNumber = (number,line.rfind(string))
        for dig in range(len(line)):
            if line[dig].isdigit():
                if dig < earldig[1]:
                    earldig = (line[dig], dig)
                if dig > latedig[1]:
                    latedig = (line[dig], dig)
        first = earliestNumber[0] if earliestNumber[1] < earldig[1] else earldig[0]
        last = latestNumber[0] if latestNumber[1] > latedig[1] else latedig[0]
        cali.append(int(str(first)+str(last)))
    print(sum(cali))

def main(fileName):
    data = ''
    with open(fileName, 'r') as file:
        data = file.readlines()
    partOne(data)
    partTwo(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', help='use the test input or not', action='store_false', required=False)
    args = parser.parse_args()
    fileName =join(sys.path[0],( "input" if args.test else "Testinput"))
    
    print(fileName)

    startTime = start_time = time.time()

    main(fileName)
    
    print("--- %s seconds ---" % (time.time() - start_time))

