# Ben Chappell - Team 54

# This file is meant to optimize the results of the cost function to find the lowest cost, highest efficiency option

import math
from random import randint
import secondModel as model
import modeling as m
import partsCost as price
import cost

# Parameters include
# pump efficiency, pump perf rating, pump volumetric flow
# pipe dff, pipe diameter, pipe length
# bend loss coeff, internal diameter, number of bends (kinda)
# turbine eff, turb performance raiting, turb volumetric flow
# maybe - drain and fill time.
# keep mass stored in resevoir constant for now

def main():
    minResult = runOptimization(1.07 * (10**9))
    print(minResult[0][0])
    print(minResult[0][1])
    print(minResult[0][2])
    print(minResult[1])

def runOptimization(waterMass):
    DEBUG = 1

    #waterMass = 1.07 * (10 ** 9)
    energyOut = 120 # in MWh

    waterMass = 795215626.875
    # get water volume from water mass
    waterVol = m.calcWaterVolume(waterMass)

    # Since pipe lengths will stay the same dependent on site (or they just have very few permutations)
    # we will define these at the start of the program. 
    pipeLen = 111.993
    bendCount = 2
    kValues = [2, 3]

    # Calculate the required pump and turbine performace ratings
    pumpRatings = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    desiredRating = 0
    for i in range(0, len(pumpRatings)):
        if pumpRatings[i] > pipeLen:
            desiredRating = i
            break

    pumpRating = turbRating = desiredRating

    # All of the parts options, used to determine the actual values to pass into the efficiency modeling.
    # lays down the lists of options for pump
    pumpEffs = [.8, .83, .86, .89, .92]
    pumpRatings = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

    # pipe options
    pipeDFFs = [.05, .04, .02, .01, .005, .002]
    pipeDias = [.1, .25, .5, .75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]

    # pipe bend stuff - mostly chosen based on zone choice.
    pipeLossCoef = [.1,.15,.2,.22,.27,.3]
    intDia = [.1, .25, .5, .75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]

    # turbine stuff
    turbEff = [.83,.86,.89,.92,.94]
    perfDown = [20,30,40,50,60,70,80,90,100,110,120]

    # all other values stores in this randomly generated list
    # [pumpeff, pumpVolFlow, pipeDff, pipeDia/benDia, turbineEff, turbineVolFlow]
    randomValues = randomInitialization(waterVol)
    valueArray = randomValues

    minPumpTurbVolFlow = int(waterVol / (3600 * 12)) + 1

    bestCost = 999999999
    hasConverged = False
    iterationCounter = 0
    # Keeps track of the array producing the minimum cost so far
    bestValueArray = valueArray.copy()

    while not hasConverged:
        # Keeps track of what change was the change that caused the greated change in the cost
        # -1 = no change, 0 - pump efficiency plus, 1 - pump eff minus, 2 - pumpVolFlow plus, 3 - pump vol flow minus, 4 - pipe dff plus, 5 - pipe dff minus
        # 6 - pipe dia plus, 7 - pipe dia minus, 8 - turb eff plus, 9 - turb eff minus, 10 - turb vol flow plus, 11 - turb vol flow minus
        changeTracker = -1
        
        # Test array used to test values so that value array doesn't need to be changed until the end.
        testArray = valueArray.copy()

        # Go through all of the potential changes and record the costs for each of those changes
        testArray[0] = (testArray[0] + 1) % 5
        # Calculate the cost in this situation and compare it to the top Change
        c = getCost(energyOut, pumpEffs, testArray, pipeDFFs, pipeDias, pipeLen, kValues, intDia, bendCount, turbEff, waterMass, pumpRating, turbRating)[0]
        if c < bestCost:
            bestCost = c
            changeTracker = 0
            bestValueArray = testArray.copy()
        testArray = valueArray.copy()
        if DEBUG:
            print(c)

        testArray[0] = (testArray[0] - 1) % 5
        # Calculate the cost in this situation and compare it to top Change
        c = getCost(energyOut, pumpEffs, testArray, pipeDFFs, pipeDias, pipeLen, kValues, intDia, bendCount, turbEff, waterMass, pumpRating, turbRating)[0]
        if c < bestCost:
            bestCost = c
            changeTracker = 1
            bestValueArray = testArray.copy()
        testArray = valueArray.copy()
        if DEBUG:
            print(c)

    
        testArray[1] = ((testArray[1] + 5) % (500 - minPumpTurbVolFlow)) + minPumpTurbVolFlow
        c = getCost(energyOut, pumpEffs, testArray, pipeDFFs, pipeDias, pipeLen, kValues, intDia, bendCount, turbEff, waterMass, pumpRating, turbRating)[0]
        if c < bestCost:
            bestCost = c
            changeTracker = 2
            bestValueArray = testArray.copy()
        testArray = valueArray.copy()
        if DEBUG:
            print(c)

        testArray[1] = ((testArray[1] - 5) % (500 - minPumpTurbVolFlow)) + minPumpTurbVolFlow
        c = getCost(energyOut, pumpEffs, testArray, pipeDFFs, pipeDias, pipeLen, kValues, intDia, bendCount, turbEff, waterMass, pumpRating, turbRating)[0]
        if c < bestCost:
            bestCost = c
            changeTracker = 3
            bestValueArray = testArray.copy()
        testArray = valueArray.copy()
        if DEBUG:
            print(c)

    
        testArray[2] = (testArray[2] + 1) % 6
        c = getCost(energyOut, pumpEffs, testArray, pipeDFFs, pipeDias, pipeLen, kValues, intDia, bendCount, turbEff, waterMass, pumpRating, turbRating)[0]
        if c < bestCost:
            bestCost = c
            changeTracker = 4
            bestValueArray = testArray.copy()
        testArray = valueArray.copy()
        if DEBUG:
            print(c)

        testArray[2] = (testArray[2] - 1) % 6
        c = getCost(energyOut, pumpEffs, testArray, pipeDFFs, pipeDias, pipeLen, kValues, intDia, bendCount, turbEff, waterMass, pumpRating, turbRating)[0]
        if c < bestCost:
            bestCost = c
            changeTracker = 5
            bestValueArray = testArray.copy()
        testArray = valueArray.copy()
        if DEBUG:
            print(c)

    
        testArray[3] = (testArray[3] + 1) % 13
        c = getCost(energyOut, pumpEffs, testArray, pipeDFFs, pipeDias, pipeLen, kValues, intDia, bendCount, turbEff, waterMass, pumpRating, turbRating)[0]
        if c < bestCost:
            bestCost = c
            changeTracker = 6
            bestValueArray = testArray.copy()
        testArray = valueArray.copy()
        if DEBUG:
            print(c)

        testArray[3] = (testArray[3] - 1) % 13
        c = getCost(energyOut, pumpEffs, testArray, pipeDFFs, pipeDias, pipeLen, kValues, intDia, bendCount, turbEff, waterMass, pumpRating, turbRating)[0]
        if c < bestCost:
            bestCost = c
            changeTracker = 7
            bestValueArray = testArray.copy()
        testArray = valueArray.copy()
        if DEBUG:
            print(c)
    
        testArray[4] = (testArray[4] + 1) % 5
        # Calculate the cost in this situation and compare it to the top Change
        c = getCost(energyOut, pumpEffs, testArray, pipeDFFs, pipeDias, pipeLen, kValues, intDia, bendCount, turbEff, waterMass, pumpRating, turbRating)[0]
        if c < bestCost:
            bestCost = c
            changeTracker = 8
            bestValueArray = testArray.copy()
        testArray = valueArray.copy()
        if DEBUG:
            print(c)

        testArray[4] = (testArray[4] - 1) % 5
        # Calculate the cost in this situation and compare it to top Change
        c = getCost(energyOut, pumpEffs, testArray, pipeDFFs, pipeDias, pipeLen, kValues, intDia, bendCount, turbEff, waterMass, pumpRating, turbRating)[0]
        if c < bestCost:
            bestCost = c
            changeTracker = 9
            bestValueArray = testArray.copy()
        testArray = valueArray.copy()
        if DEBUG:
            print(c)
    
        testArray[5] = ((testArray[5] + 5) % (500 - minPumpTurbVolFlow)) + minPumpTurbVolFlow
        c = getCost(energyOut, pumpEffs, testArray, pipeDFFs, pipeDias, pipeLen, kValues, intDia, bendCount, turbEff, waterMass, pumpRating, turbRating)[0]
        if c < bestCost:
            bestCost = c
            changeTracker = 10
            bestValueArray = testArray.copy()
        testArray = valueArray.copy()
        if DEBUG:
            print(c)

        testArray[5] = ((testArray[5] - 5) % (500 - minPumpTurbVolFlow)) + minPumpTurbVolFlow
        c = getCost(energyOut, pumpEffs, testArray, pipeDFFs, pipeDias, pipeLen, kValues, intDia, bendCount, turbEff, waterMass, pumpRating, turbRating)[0]
        if c < bestCost:
            bestCost = c
            changeTracker = 11
            bestValueArray = testArray.copy()
        testArray = valueArray.copy()
        if DEBUG:
            print(c)

        if changeTracker == -1:
            hasConverged = True

        valueArray = bestValueArray.copy()
        iterationCounter += 1

        if DEBUG:
            print(bestCost)
            print(changeTracker)
            print(iterationCounter)
            print("")

        #print (iterationCounter)
    #print(iterationCounter)
    finalResults = getCost(energyOut, pumpEffs, bestValueArray, pipeDFFs, pipeDias, pipeLen, kValues, intDia, bendCount, turbEff, waterMass, pumpRating, turbRating)
    
    if DEBUG:
        print(finalResults[0])
        print(finalResults[1])
        print(finalResults[2])
    
    return [finalResults, bestValueArray]


def getCost(energyOut, pumpEffs, valueArray, pipeDFFs, pipeDias, pipeLen, kValues, intDia, bendCount, turbEff, waterMass, pumpRating, turbRating):
    # Transform kValues into something usable by energyIn
    pipeLossCoef = [.1,.15,.2,.22,.27,.3]
    kVals = []
    for i in range(0, len(kValues)):
        kVals.append(pipeLossCoef[kValues[i]])
    
    # Calculates energy in
    eIn = model.calcEIn(energyOut, pumpEffs[valueArray[0]], valueArray[1], pipeDFFs[valueArray[2]], 
                            pipeDias[valueArray[3]], pipeLen, kVals, intDia[valueArray[3]], bendCount, 
                           turbEff[valueArray[4]], valueArray[5], waterMass)

    # Create the partSelection.txt file for price calculation.
    parts = open("partSelection.txt", 'w')

    # piece together the line for the pump
    pumpLine = "1 " + str(valueArray[0]) + " " + str(pumpRating) + " " + str(valueArray[1]) + "\n"
    parts.write(pumpLine)

    # piece together the line for the pipe
    pipeLine = "2 " + str(valueArray[2]) + " " + str(valueArray[3]) + " " + str(pipeLen) + "\n"
    parts.write(pipeLine)

    # piece together the lines for the bends    
    for i in range(0, bendCount):
        bendline = "3 " + str(kValues[i]) + " " + str(valueArray[3]) + "\n"
        parts.write(bendline)

    # piece together the line for the turbine
    turbLine = "4 " + str(valueArray[4]) + " " + str(turbRating) + " " + str(valueArray[5]) + "\n"
    parts.write(turbLine)
    parts.close()

    # Calculate the price of the parts
    iterationPrice = price.calcParts()

    #print(eIn)
    #print(iterationPrice)
    iterationCost = cost.cost(eIn, iterationPrice)
    #print(iterationCost)
    #print(" ")
    return [iterationCost, eIn, iterationPrice]

def storage():
    # Since we have now found the change that causes the greatest change in the cost, we need to keep it.
    #    if changeTracker == 0:
    #        valueArray[0] = (valueArray[0] + 1) % 5
    #    elif changeTracker == 1:
    #        valueArray[0] = (valueArray[0] - 1) % 5
    #    elif changeTracker == 2:
    #        valueArray[1] = ((valueArray[1] + 1) % (500 - minPumpTurbVolFlow)) + minPumpTurbVolFlow
    #    elif changeTracker == 3:
    #        valueArray[1] = ((valueArray[1] - 1) % (500 - minPumpTurbVolFlow)) + minPumpTurbVolFlow
    #    elif changeTracker == 4:
    #        valueArray[2] = (valueArray[2] + 1) % 6
    #    elif changeTracker == 5:
    #        valueArray[2] = (valueArray[2] - 1) % 6
    #    elif changeTracker == 6:
    #        valueArray[3] = (valueArray[3] + 1) % 13
    #    elif changeTracker == 7:
    #        valueArray[3] = (valueArray[3] - 1) % 13
    #    elif changeTracker == 8:
    #        valueArray[4] = (valueArray[4] + 1) % 5
    #    elif changeTracker == 9:
    #        valueArray[4] = (valueArray[4] - 1) % 5
    #    elif changeTracker == 10:
    #       valueArray[5] = ((valueArray[5] + 1) % (500 - minPumpTurbVolFlow)) + minPumpTurbVolFlow
    ##   elif changeTracker == 11:
    #        valueArray[5] = ((valueArray[5] - 1) % (500 - minPumpTurbVolFlow)) + minPumpTurbVolFlow
    #    elif changeTracker == -1:
    #        hasConverged = True
    pass

def randomInitialization(waterVol):
    minPumpTurbVolFlow = waterVol / (3600 * 12)

    initialized = []

    initialized.append(randint(0, 4)) # random pipe efficiency value
    initialized.append(randint(int(minPumpTurbVolFlow) + 1, 500)) # random pump volumetric flow TODO calculate the minimum value based on the amount of water present
    initialized.append(randint(0, 5)) # random pipe quality
    initialized.append(randint(0, 12)) # random pipe and bend diameter
    initialized.append(randint(0, 4)) # random turb efficiency
    initialized.append(randint(int(minPumpTurbVolFlow) + 1, 500)) # random turbine volumetric flow, same todo as with pump volumetric flow.

    return initialized

    


if __name__ == "__main__":
    main()
