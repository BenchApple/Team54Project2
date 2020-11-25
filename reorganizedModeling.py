# Ben Chappell - Team 54

import numpy as np

global g
g = 9.81

def mwhToJoules(mwh):
    conversionRate = 3.6 * (10 ** 9)

    return mwh * conversionRate

def joulesToMwh(joules):
    result = joules / 3.6

    for i in range(0, 9):
        result /= 10

    return result

def turbineLoss(energyOut, turbineEfficiency):
    return energyOut * ((1 / turbineEfficiency) - 1)

# Uses a form of the darcy-weissbach equation to compute the head loss of energy due to a bend in the pipe
# Fitting factor varies from .1 to 2
# This is the energy loss per bend and per flow direction
def pipeBendHeadLoss(fittingFactor, waterVelocity):
    return fittingFactor * ((waterVelocity ** 2) / (2 * g))

# Calculates the head loss due to pipe friction using the darcy weisbach equation.
def darcyWeisbach(pipeLength, diameter, exitVelocity, frictionFactor):
    return frictionFactor * (pipeLength / diameter) * ((exitVelocity ** 2) / (2 * g))

# Calculates the energy loss due to pipe head loss, regardless of what the head loss was a result of.
# M - The mass of the water going through the pipe.
def energyLossFromHeadLoss(headLoss, M):
    return M * g * headLoss

# Calculates the water volume based on the mass of the volume.
def calcWaterVolume(waterMass):
    waterDensity = 1 # Assume that the waster density is 1 gram / cm^3

    # since volume = mass / density
    return waterMass / waterDensity

# Calculates the cross sectional diameter of a pipe
def crossSectionalArea(diameter):
    return np.pi * ((diameter / 2) ** 2)

# NOTE the distance the water is moved is determined by the length of the pipe it is moving through.
# Calculates the average velocity of the water in the pipe as per the volumetric flow equation.
def waterVelocity(timeElapsed, waterVolume, diameter):
    timeInSec = timeElapsed * 3600
    area = crossSectionalArea(diameter)

    return waterVolume / (area * timeInSec)

def waterVolumeFromFillTimeAndQ(fillTime, pumpQ):
    timeInSec = fillTime * 3600

    volume = pumpQ * timeInSec
    return volume

def drainTimeFromVolumeAndQ(waterVolume, turbineQ):
    timeInSec = waterVolume / turbineQ

    return timeInSec / 3600
