# Ben Chappell - Team 54

# This file has all of the functions to calculate the final results that we need for the program.

def resevoirArea():
    pass

# Calculates the required energy coming into the system in order to reach the target energy out of 120 kWh
# ELossA is the amount of energy lost in the system from every souce after the pump
# Eout is the required energy out of the system (120 kWh)
# etaP is the efficiency of the pump.
def calcEnergyIn(ELossA, Eout, etaP):
    return (ELossA + Eout) / (1 - etaP)

def sysEfficiency(eIn, eOut):
    return eIn / eOut 

# Calculates the amount of time it takes to fill the resevoir
def timeToFill(pumpFlowVolume, waterVolume):
    return waterVolume / pumpFlowVolume

# Calcualtes the amount of time it takes to empty the resevoir.
def timeToEmpty(turbineFlowVolume, waterVolume):
    return waterVolume / turbineFlowVolume