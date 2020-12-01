# Ben Chappell - Team 54

# This file runs optimizations multiple times in order to find the best of the local minima

import optimise as o

def main():
    minCost = 999999999
    limit = 10
    minResult = []

    for i in range(0, limit):
        result = o.runOptimization()

        if result[0][0] < minCost:
            print(result[0][0])
            minCost = result[0][0]
            minResult = result.copy()

    print(minCost)
    print(minResult[0][1])
    print(minResult[0][2])
    print(minResult[1])

    # Since pipe lengths will stay the same dependent on site (or they just have very few permutations)
    # we will define these at the start of the program. 
    pipeLen = 75
    bendCount = 2
    kValues = [1,2]

    # Calculate the required pump and turbine performace ratings
    pumpRatings = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    desiredRating = 0
    for i in range(0, len(pumpRatings)):
        if pumpRatings[i] > pipeLen:
            desiredRating = i
            break

    pumpRating = turbRating = desiredRating

    valueArray = minResult[1].copy()

    # Create the partSelection.txt file for price calculation.
    parts = open("bestParts.txt", 'w')

    # All of the parts options, used to determine the actual values to pass into the efficiency modeling.
    # lays down the lists of options for pump
    pumpEffs = [.8, .83, .86, .89, .92]
    pumpRatings = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

    # pipe options
    pipeDFFs = [.05, .04, .02, .01, .005, .002]
    pipeDias = [.1, .25, .5, .75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]

    # pipe bend stuff - mostly chosen based on zone choice.
    pipeLossCoef = [.1,.15,.2,.22,.27,.3]
    intDia = [.1,.25,.5,.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,3]

    # turbine stuff
    turbEff = [.83,.86,.89,.92,.94]
    perfDown = [20,30,40,50,60,70,80,90,100,110,120]

    # piece together the line for the pump
    pumpLine = "1 " + str(pumpEffs[valueArray[0]]) + " " + str(pumpRating) + " " + str(valueArray[1]) + "\n"
    parts.write(pumpLine)

    # piece together the line for the pipe
    pipeLine = "2 " + str(pipeDFFs[valueArray[2]]) + " " + str(pipeDias[valueArray[3]]) + " " + str(pipeLen) + "\n"
    parts.write(pipeLine)

    # piece together the lines for the bends    
    for i in range(0, bendCount):
        bendline = "3 " + str(kValues[i]) + " " + str(intDia[valueArray[3]]) + "\n"
        parts.write(bendline)

    # piece together the line for the turbine
    turbLine = "4 " + str(turbEff[valueArray[4]]) + " " + str(turbRating) + " " + str(valueArray[5]) + "\n"
    parts.write(turbLine)
    parts.close()

if __name__ == "__main__":
    main()