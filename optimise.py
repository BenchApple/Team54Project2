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
    waterMass = 1.07 * (10 ** 9)
    energyOut = 120 # in MWh

    # get water volume from water mass
    waterVol = m.calcWaterVolume(waterMass)

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

    # all other values stores in this randomly generated list
    # [pumpeff, pumpVolFlow, pipeDff, pipeDia/benDia, turbineEff, turbineVolFlow]
    randomValues = randomInitialization(waterVol)
    valueArray = randomValues

    # Calculates energy in
    eIn = model.calcEIn(energyOut, pumpEffs[valueArray[0]], valueArray[1], pipeDFFs[valueArray[2]], 
                        pipeDias[valueArray[3]], pipeLen, kValues, intDia[valueArray[3]], bendCount, 
                        turbEff[valueArray[4]], valueArray[5], waterVol)

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

    print(eIn)
    print(iterationPrice)
    iterationCost = cost.cost(eIn, iterationPrice)
    print(iterationCost)



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