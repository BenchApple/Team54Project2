# Ben Chappell - Team 54

# This file runs optimizations multiple times with varying water mass to see if that makes a difference for wahtever reasons it might

import multipleOptimizations as m
import optimize as o

def main():
    output = open("siteOneChoices.txt", 'w')

    for height in range(10, 41, 5):
        pi = 3.1415926
        h = height / 2
        waterMass = 600 * 600 * h * 1000

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