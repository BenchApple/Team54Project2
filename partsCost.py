# Ben Chappell - Team 54

# This file calculates the cost of the parts from the file partSelection.txt

import partsSelection as p

def calcParts():
    parts = open("partSelection.txt", 'r')
    
    pumpData = open("textFiles\Pumps.txt", 'r')
    pumpData = p.getCostArray(pumpData)
    pipeData = open("textFiles\Pipes.txt", 'r')
    pipeData = p.getCostArray(pipeData)
    bendData = open("textFiles\Bends.txt", 'r')
    bendData = p.getCostArray(bendData)
    turbData = open("textFiles\Turbines.txt", 'r')
    turbData = p.getCostArray(turbData)

    # partSelection.txt is based on a code
    # The first value of a line determines what part type it corresponds to
    # 1 - pump, 2 - pipe, 3 - bend, 4 - turbine
    # For pump, the second value on the line is the efficiency, third is perf rating, fourth is m^3 / second of flow
    # for pipe, second value is darcy friction factor, third is internal diameter, and final is length
    # for bend, second value is pipe loss, third value is internal diameter
    # for turbine, second value is efficiency, third is perf rating, fourth is volumetric flow.
    # Each of these options are the Index that that option is stored in in the actual table for all of the data

    # Keeps track of the total cost
    cost = 0

    for line in parts.readlines():
        curLine = line.rstrip().split()
        
        if int(curLine[0]) == 1:
            # If the first value is 1 then we have pump specifications
            cost += (pumpData[int(curLine[2])][int(curLine[1])]) * float(curLine[3])
        elif int(curLine[0]) == 2:
            # If the first value is 1 then we have pump specifications
            cost += (pipeData[int(curLine[2])][int(curLine[1])]) * float(curLine[3]) 
        elif int(curLine[0]) == 3:
            # If the first value is 1 then we have pump specifications
            cost += (bendData[int(curLine[2])][int(curLine[1])])
        elif int(curLine[0]) == 4:
            # If the first value is 1 then we have pump specifications
            cost += (turbData[int(curLine[2])][int(curLine[1])]) * float(curLine[3])

    print(cost)



if __name__ == "__main__":
    calcParts()