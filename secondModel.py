# Ben Chappell - Team 54

# Second try at modeling shit.

import outputCalcs as o
import reorganizedModeling as m


def main():
    # Input parameters.
    energyOut = 120
    pumpEff = .9
    pumpQ = 65
    pipeDia = 2
    pipeLen = 75
    pipeF = .05
    resevoirDepth = 10
    resevoirElevation = 50
    k1 = .15
    k2 = .2
    turbineEff = .92
    turbineQ = 30

    # Our choice
    fillTime = 4.58
    
    # Calculate the energy coming out in joules
    eOut = m.mwhToJoules(energyOut)
    print("eOut: " + str(eOut))

    # Calculate the volume of the water moved
    waterVolume = m.waterVolumeFromFillTimeAndQ(fillTime, pumpQ)
    drainTime = m.drainTimeFromVolumeAndQ(waterVolume, turbineQ)
    print("waterVolume: " + str(waterVolume))
    print("drainTime: " + str(drainTime))

    # Caculate Water velocities
    veloUp = m.waterVelocity(fillTime, waterVolume, pipeDia)
    veloDown = m.waterVelocity(drainTime, waterVolume, pipeDia)
    print("veloUp: " + str(veloUp))
    print("veloDown: " + str(veloDown))
    print("cross sectional area: " + str(m.crossSectionalArea(pipeDia)))

    # Energy loss from turbine
    turbineL = m.turbineLoss(eOut, turbineEff)

    # Calculate head loss from pipe friction
    dwUp = m.darcyWeisbach(pipeLen, pipeDia, veloUp, pipeF)
    dwDown = m.darcyWeisbach(pipeLen, pipeDia, veloDown, pipeF)

    lossUp = m.energyLossFromHeadLoss(dwUp, waterVolume)
    lossDown = m.energyLossFromHeadLoss(dwDown, waterVolume)

    # Calculate energy loss from bends
    bendHeadLossTop = m.pipeBendHeadLoss(k1, veloUp) + m.pipeBendHeadLoss(k1, veloDown)
    bendHeadLossBottom = m.pipeBendHeadLoss(k2, veloUp) + m.pipeBendHeadLoss(k2, veloDown)
    bendLossTop = m.energyLossFromHeadLoss(bendHeadLossTop, waterVolume)
    bendLossBottom = m.energyLossFromHeadLoss(bendHeadLossBottom, waterVolume)


    # Calculate the total energy loss from everything but the pump.
    totalEnergyLoss = turbineL + lossDown + lossUp + bendLossBottom + bendLossTop

    eInJoules = o.calcEnergyIn(totalEnergyLoss, eOut, pumpEff)
    eIn = m.joulesToMwh(eInJoules)
    print(eIn)



if __name__ == "__main__":
    main()