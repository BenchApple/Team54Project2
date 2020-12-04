# Ben Chappell - Team 54

# This file runs optimizations multiple times with varying water mass to see if that makes a difference for wahtever reasons it might

import multipleOptimizations as m
import optimize as o
import matplotlib.pyplot as plt

def main():
    # Input the water mass of the system here
    waterMass = 1.07 * (10 ** 9)

    results = o.runOptimization(waterMass)

    tVals = [i for i in range(1, len(results[2]) + 1)]
    costResults = results[2].copy()

    plt.figure(num=1, figsize=(13,8), dpi=80)
    plt.title("Progression of Optimization over Time", fontsize=15)
    plt.xlabel("Iteration Number", fontsize=13)
    plt.ylabel("Cost Function Output", fontsize=13)
    plt.plot(tVals, costResults, label="Cost Progression", linewidth='2')

    # Format the results of each trial and output them to the text file.
    cost = results[0][0]
    eIn = results[0][1]
    price = results[0][2]

    componentChoices = results[1]
    toWrite = "Water Mass: " + str(waterMass) + "\nCost: " + str(cost) + "\nEnergy In: " + str(eIn) + "\nPrice: " + str(price) + "\nComponents: " + str(componentChoices) + "\n\n"
    print(toWrite)

    plt.show()  

def varyMasses():
    output = open("siteThreeLastOneRaised.txt", 'w')

    for height in range(10, 41, 31):
        pi = 3.1415926
        h = height / 2
        waterMass = 600 * 600 * h * 1000

        waterMass = 735574467.407

        results = o.runOptimization(waterMass)

        # Format the results of each trial and output them to the text file.
        cost = results[0][0]
        eIn = results[0][1]
        price = results[0][2]

        componentChoices = results[1]
        toWrite = "Water Mass: " + str(waterMass) + "\nCost: " + str(cost) + "\nEnergy In: " + str(eIn) + "\nPrice: " + str(price) + "\nComponents: " + str(componentChoices) + "\n\n"
        output.write(toWrite)

    output.close()

if __name__ == "__main__":
    main()