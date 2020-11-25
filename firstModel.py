# Ben Chappell - Team 54

# This file contains the final calculations so far using the models created.

import reorganizedModeling as m
import outputCalcs as o

def main():
    #initialEnergy = 200 # placeholder.
    pumpEff = .9
    finalEnergy = 120 # Final value of the energy will always need to be 120 kilowatt hours.
    turbineEff = .92
    M = 100 # mass, placeholder
    pipeFrictionConst = .05
    pipeLength = 75
    diameter = 2
    eOutJoules = m.mwhToJoules(finalEnergy)

    # Parameters for bends in the pipe
    topFittingFactor = .2
    bottomFittingFactor = .15

    fillingTime = 12 # Measured in hours
    drainingTime = 12 # measured in hours

    waterVol = m.calcWaterVolume(M)

    # Calculate the velocities of the water up and down
    veloUp = m.waterVelocity(fillingTime, waterVol, diameter)
    veloDown = m.waterVelocity(drainingTime, waterVol, diameter)

    # Do the calculations based on the placeholder values.
    #pump = m.pumpLoss(initialEnergy, pumpEff)
    turbine = m.turbineLoss(eOutJoules, turbineEff)

    dwUp = m.darcyWeisbach(pipeLength, diameter, veloUp, pipeFrictionConst)
    dwDown = m.darcyWeisbach(pipeLength, diameter, veloDown, pipeFrictionConst)
    lossUp = m.energyLossFromHeadLoss(dwUp, M)
    lossDown = m.energyLossFromHeadLoss(dwDown, M)

    bendHeadLossTop = m.pipeBendHeadLoss(topFittingFactor, veloUp) + m.pipeBendHeadLoss(topFittingFactor, veloDown)
    bendHeadLossBottom = m.pipeBendHeadLoss(bottomFittingFactor, veloUp) + m.pipeBendHeadLoss(bottomFittingFactor, veloDown)
    bendLossTop = m.energyLossFromHeadLoss(bendHeadLossTop, M)
    bendLossBottom = m.energyLossFromHeadLoss(bendHeadLossBottom, M)

    totalEnergyLoss = turbine + lossDown + lossUp + bendLossBottom + bendLossTop

    requiredInputEnergy = o.calcEnergyIn(totalEnergyLoss, eOutJoules, pumpEff)
    requiredInputEnergy = m.joulesToMwh(requiredInputEnergy)
    print(requiredInputEnergy)
    

if __name__ == "__main__":
    main()