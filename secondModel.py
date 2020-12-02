# Ben Chappell - Team 54

# Second try at modeling shit.

import outputCalcs as o
import reorganizedModeling as m


def main():
    # Input parameters.
    energyOut = 120
    pumpEff = .92
    pumpVolFlow = 48
    pipeDia = 2.75
    pipeLen = 75
    pipeDff = .02
    resevoirDepth = 10
    resevoirElevation = 50
    bendCount = 2
    kVals = [.15, .2]
    turbEff = .92
    turbVolFlow = 29

    waterMass = 1.07 * (10 ** 9)
    waterVolume = m.calcWaterVolume(waterMass)
    
    fillTime = (waterVolume / pumpVolFlow) / 3600 # calculates the fill time in hours
    
    # Calculate the energy coming out in joules
    eOut = m.mwhToJoules(energyOut)
    #print("eOut: " + str(eOut))

    # Calculate the volume of the water moved
    drainTime = m.drainTimeFromVolumeAndQ(waterVolume, turbVolFlow)
    #print("waterVolume: " + str(waterVolume))
    #print("drainTime: " + str(drainTime))

    # Caculate Water velocities
    veloUp = m.waterVelocity(fillTime, waterMass, pipeDia)
    veloDown = m.waterVelocity(drainTime, waterMass, pipeDia)
    #print("veloUp: " + str(veloUp))
    #print("veloDown: " + str(veloDown))
    #print("cross sectional area: " + str(m.crossSectionalArea(pipeDia)))

    # Energy loss from turbine
    turbineL = m.turbineLoss(eOut, turbEff)

    # Calculate head loss from pipe friction
    dwUp = m.darcyWeisbach(pipeLen, pipeDia, veloUp, pipeDff)
    dwDown = m.darcyWeisbach(pipeLen, pipeDia, veloDown, pipeDff)

    lossUp = m.energyLossFromHeadLoss(dwUp, waterMass)
    lossDown = m.energyLossFromHeadLoss(dwDown, waterMass)

    # Calculate energy loss from bends
    bendHeadLossTotal = 0
    for i in range(0, bendCount):
        bendHeadLossTotal += m.pipeBendHeadLoss(kVals[i], veloUp)
        bendHeadLossTotal += m.pipeBendHeadLoss(kVals[i], veloDown)

    bendLossTotal = m.energyLossFromHeadLoss(bendHeadLossTotal, waterMass)

    # Calculate the total energy loss from everything but the pump.
    totalEnergyLoss = turbineL + lossDown + lossUp + bendLossTotal
    energyLossMwh = m.joulesToMwh(totalEnergyLoss)

    eInJoules = o.calcEnergyIn(totalEnergyLoss, eOut, pumpEff)
    eInMhw = o.calcEnergyIn(energyLossMwh, energyOut, pumpEff)
    eIn = m.joulesToMwh(eInJoules)
    print(eIn)
    eff = o.sysEfficiency(eInMhw, energyOut)
    #print(eff)

    return eIn

def calcEIn(energyOut, pumpEff, pumpVolFlow, pipeDff, pipeDia, pipeLen, kVals, kDia, bendCount, turbEff, turbVolFlow, waterMass):
    waterVolume = m.calcWaterVolume(waterMass)
    
    fillTime = (waterVolume / pumpVolFlow) / 3600 # calculates the fill time in hours
    
    # Calculate the energy coming out in joules
    eOut = m.mwhToJoules(energyOut)
    #print("eOut: " + str(eOut))

    # Calculate the volume of the water moved
    drainTime = m.drainTimeFromVolumeAndQ(waterVolume, turbVolFlow)
    #print("waterVolume: " + str(waterVolume))
    #print("drainTime: " + str(drainTime))

    # Caculate Water velocities
    veloUp = m.waterVelocity(fillTime, waterMass, pipeDia)
    veloDown = m.waterVelocity(drainTime, waterMass, pipeDia)
    #print("veloUp: " + str(veloUp))
    #print("veloDown: " + str(veloDown))
    #print("cross sectional area: " + str(m.crossSectionalArea(pipeDia)))

    # Energy loss from turbine
    turbineL = m.turbineLoss(eOut, turbEff)

    # Calculate head loss from pipe friction
    dwUp = m.darcyWeisbach(pipeLen, pipeDia, veloUp, pipeDff)
    dwDown = m.darcyWeisbach(pipeLen, pipeDia, veloDown, pipeDff)

    lossUp = m.energyLossFromHeadLoss(dwUp, waterMass)
    lossDown = m.energyLossFromHeadLoss(dwDown, waterMass)

    # Calculate energy loss from bends
    bendHeadLossTotal = 0
    for i in range(0, bendCount):
        bendHeadLossTotal += m.pipeBendHeadLoss(kVals[i], veloUp)
        bendHeadLossTotal += m.pipeBendHeadLoss(kVals[i], veloDown)

    bendLossTotal = m.energyLossFromHeadLoss(bendHeadLossTotal, waterMass)

    # Calculate the total energy loss from everything but the pump.
    totalEnergyLoss = turbineL + lossDown + lossUp + bendLossTotal
    energyLossMwh = m.joulesToMwh(totalEnergyLoss)

    eInJoules = o.calcEnergyIn(totalEnergyLoss, eOut, pumpEff)
    eInMhw = o.calcEnergyIn(energyLossMwh, energyOut, pumpEff)
    eIn = m.joulesToMwh(eInJoules)
    #print(eIn)
    eff = o.sysEfficiency(eInMhw, energyOut)
    #print(eff)

    return eIn

if __name__ == "__main__":
    main()