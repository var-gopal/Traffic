# Traffic

## Aim

This checkpoint requires you to code a simple cellular automaton which attempts to model traffic flow. This is an example where the effective theory is not known, so we invent a theory that has the basic properties that we believe are important. By running simulations we can look for emergent phenomena, in this case the onset of congestion (traffic jams).

## The Model

The simulation box is a straight line of $N$ cells (the road) which can each only have two values: $1$ if a car is present on that section of road, $0$ otherwise. The update rules for each iteration are very simple:

If the space in front of a car is empty then it moves forward one cell;
Otherwise it stays where it is.
If we use $c(j)$ to indicate the state of the $jth$ cell, and use a subscript n to represent the iteration, we can write down rules that determine $cn+1(j)$ from values at the previous iteration $cn(j−1)$, $cn(j)$ and $cn(j+1)$.
- if $cn(j)=1$ 
    - if $cn(j+1)=1$
        - then $cn+1(j)=1$
    - else $cn+1(j)=0$
- else if $cn(j)=0$
    - if $cn(j−1)=1$
        - then $cn+1(j)=1$
    - else $cn+1(j)=0$
## Checkpoint task

Write an object-oriented Python program to simulate the movement of cars on a one-dimensional road according to the rules defined above. The road has periodic boundary conditions, i.e. moving forward from the last cell of the road takes you back to the first cell.

Your code should prompt the user for the number of cells $N$ (i.e. the length of the road), the number of iterations (i.e. the number of timesteps) and the car density (i.e. the fraction of cells that have a car on them). It should then initialise the simulation by placing cars in random positions on the road.


### Initialisation, car density and number of cars

One way to place cars randomly on the road is to iterate over all of the cells in the road and determine whether or not to place a car on a cell by generating a random number and comparing it to the car density (this as the same approach that we used in Checkpoint 2 to randomly select undecayed nuclei to decay). Because this is a statistical process, the number of cars on the road, and hence the car density, is likely to vary slightly each time the simulation is run. In addition, depending on the input values of car density and number of cells, it may not be possible to match the input value of the car density exactly as - self-evidently - the number of cars must be an integer. For example, a road of $25$ cells cannot have a car density of $0.5$, as this would mean placing $12.5$ cars on the road!

In this checkpoint, neither of these limitations is problematic, but it does mean that you will need to determine the actual (‘experimental’) total number of cars in your simulation in order to obtain the average speed (see below), rather than calculating this from input value of car density.

 
Your code should update the road for the given number of timesteps. At each timestep, the code should compute and print the average speed of the cars.


### What does ‘average speed’ mean?

In this checkpoint, we are interested in the average speed of the cars in a given timestep (not, for example, the average over many timesteps, or over the whole simulation). In a single timestep, each car will either move forward one cell or will stay where it is. The average speed of the cars in a given timestep is therefore simply the fraction of cars that move in that timestep, i.e:   
$average\ speed=\dfrac{number\ of\ cars\ that\ move}{total\ number\ of\ cars}$.
 
You should find that the average speed of the cars changes over the first few timesteps, but that once the movement of the cars reaches steady state the average speed remains constant, i.e. is the same at each timestep. This is the ‘steady state’ average speed.

At the end of the simulation, your code should graphically represent the positions of the cars on the road as a function of time. This representation does not need to be animated, although you may use animation if you wish.

Finally, you should use your code to determine the steady state average speed for a range of car densities between zero, for a completely empty road, to one, for a completely jammed road. You should then plot or sketch a graph of the steady state average speed against the density of cars. What does this tell you about the onset of congestion (traffic jams)?


### How to determine the steady state average speed?

One simple way to determine the steady state average speed is to run the simulation until it is in equilibrium and then take the average speed for the final timestep. You may find your graphical representation useful for checking whether the simulation has reached equilibrium.

You may use a more sophisticated approach if you wish, but this is not required as part of the checkpoint code.

The number of timesteps needed to reach equilibrium depends on the density of cars and their initial positions on the road. However, the dynamics of traffic cellular automata are very complex (and beyond this course) and in general do not have exact solutions.
### Recording and plotting your results

As noted above, for each car density you should use the average speed in steady state. If you wish, you may modify your code to determine this and/or to record and plot your results (we think using Python is the easiest approach!), but this is not required as part of the checkpoint code. Alternatives include noting your results by hand and then plotting them using Excel, or by hand.