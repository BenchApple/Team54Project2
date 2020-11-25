# Ben Chappell - team 54

# This file controls parts selection and cost determination.

def main():
    # lays down the lists of options for pump
    pumpEffs = [.8, .83, .86, .89, .92]
    pumpRatings = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

    # pipe options
    pipeDFFs = [.05, .04, .02, .01, .005, .002]
    pipDias = [.1, .25, .5, .75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]

    # pipe bend stuff - mostly chosen based on zone choice.
    pipeLossCoef = [.1,.15,.2,.22,.27,.3]
    intDia = [.1,.25,.5,.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,3]

    # turbine stuff
    turbEff = [.83,.86,.89,.92,.94]
    perfDown = [20,30,40,50,60,70,80,90,100,110,120]

    pumpData = open("textFiles\Pumps.txt", 'r')
    pumpData = getCostArray(pumpData)
    pipeData = open("textFiles\Pipes.txt", 'r')
    pipeData = getCostArray(pipeData)
    bendData = open("textFiles\Bends.txt", 'r')
    bendData = getCostArray(bendData)
    turbData = open("textFiles\Turbines.txt", 'r')
    turbData = getCostArray(turbData)



    for i in range(0, len(turbEff)):
        for j in range(0, len(perfDown)):
            print(turbData[j][i])




# Eff, rating are indices, not the specific values
#
def getCostArray(data):
    rawData = data.readlines()
    data = [0 for i in range(0, len(rawData))]

    for line in range(0, len(rawData)):
        curLine = rawData[line].rstrip().split()
        for i in range(0, len(curLine)):
            curLine[i] = float(curLine[i])

        data[line] = curLine

    return data


        



if __name__ == "__main__":
    main()