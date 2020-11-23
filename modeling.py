# Ben Chappell - Team 54

import numpy as np

global g
g = 9.81

# Returns the energy loss from a single pump with a given efficiency and energy in.
def pumpLoss(energyIn, efficiencyConst):
    pumpEnergyLoss = (1 - efficiencyConst) * energyIn

    return pumpEnergyLoss

# returns the mass change due to evaporation on a surface of water.
# use engineeringtoolbox.com
# mass of evaporated water = Theta * A(X_s - X) per hour where Theta = 25 + 19v
# A is the surface area over the water
# X_s is the humidity ration in saturated air
# X is the current humidity ratio
# V is the speed of the air over the water.
def massChangeFromEvaporation(humidity, humidityRatio, airSpeedOverWater, waterSurfaceArea):
    theta = 25 + 19 * airSpeedOverWater

    massLossPerHour = theta * waterSurfaceArea * (humidityRatio - humidity)
    return massLossPerHour

def turbineLoss(energyOut, turbineEfficiency):
    return energyOut * ((1 / turbineEfficiency) - 1)

# Uses a form of the darcy-weissbach equation to compute the head loss of energy due to a bend in the pipe
# Fitting factor varies from .1 to 2
# This is the energy loss per bend and per flow direction
def pipeBendHeadLoss(fittingFactor, waterVelocity):
    return fittingFactor * ((waterVelocity ** 2) / (2 * g))

# Returns the system efficiency of the whole system based on energy in and energy out.
def systemEfficiency(eIn, eOut):
    return eOut / eIn

# Calculates the head loss due to pipe friction using the darcy weisbach equation.
def darcyWeisbach(pipeLength, diameter, exitVelocity, frictionFactor):
    return frictionFactor * (pipeLength / diameter) * ((exitVelocity ** 2) / (2 * g))

# Calculates the energy loss due to pipe head loss, regardless of what the head loss was a result of.
# M - The mass of the water going through the pipe.
def energyLossFromHeadLoss(headLoss, M):
    return M * g * headLoss

# Calculates the cross sectional diameter of a pipe
def crossSectionalArea(diameter):
    return np.pi * ((diameter / 2) ** 2)

# NOTE the distance the water is moved is determined by the length of the pipe it is moving through.
# Calculates the average velocity of the water in the pipe as per the volumetric flow equation.
def waterVelocity(timeElapsed, waterVolume, diameter):
    area = crossSectionalArea(diameter)

    return waterVolume / (area * timeElapsed)

# Calculates the water volume based on the mass of the volume.
def calcWaterVolume(waterMass):
    waterDensity = 1 # Assume that the waster density is 1 gram / cm^3

    # since volume = mass / density
    return waterMass / waterDensity

# Calculates the required energy coming into the system in order to reach the target energy out of 120 kWh
# ELossA is the amount of energy lost in the system from every souce after the pump
# Eout is the required energy out of the system (120 kWh)
# etaP is the efficiency of the pump.
def calcEnergyIn(ELossA, Eout, etaP):
    return (ELossA + Eout) / (1 - etaP)