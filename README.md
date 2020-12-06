# Team54Project2

The files used in the final code are varyWaterMass.py, optimize.py, cost.py, secondModel.py, 
reorganizedModeling.py, outputCalcs.py, calcParts.py.

All other .py files were either used for testing or became outdated due to their functions being overwritten in some other file
This approach was decided upon to aid in the modularity of the code, as otherwise we would have had a massive, 
unapproachable, 2000 plus line document, which does not aid or abbett in the process of coding a large project.

Any text files present are utilized for various forms of data storage, and generally they are overwritten as the program
runs multiple times. testing.txt was used mainly for debugging as we had a rather nasty bug in the final week of the project

All files in /textFiles are used for data storage when it comes to calculating the prices of components.

In order to run the program, specify the water mass in the main function of varyWaterMass.py, and specify the pipe length
and bend coefficients in optimize.py, then run varyWaterMass.py