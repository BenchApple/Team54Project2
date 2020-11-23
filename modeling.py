# Ben Chappell - Team 54

g = 9.81
global g

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
    return energyOut * ((1/turbineEfficiency) - 1)

# Uses a form of the darcy-weissbach equation to compute the head loss of energy due to a bend in the pipe
# Fitting factor varies from .1 to 2
# This is the energy loss per bend and per flow direction
def pipeBendHeadLoss(fittingFactor, waterVelocity):
    return fittingFactor * ((waterVelocity ** 2) / (2 * g))