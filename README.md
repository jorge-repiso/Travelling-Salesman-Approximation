# Traveling Salesman

This Python project offers an approximation to the travelling salesman problem.

This solution uses a hill-climbing approach, where the salesman starts in a random
city and tries to progressively improve until it is no longer possible.


## General idea of the assignment

Suppose there are a number of "cities", as in shown in Figure 1:

![Figure 1, Cities](https://www.dcs.bbk.ac.uk/~vlad/pub/pop1/proj/Figure1.png)

The distance between any two cities with the coordinates (x1, y1) and (x2,y2) is
 the standard Euclidean distance, that is, 

sqrt((x1-x2)^2 + (y1-y2)^2)

A traveling salesman wishes to visit every city exactly once, 
then return to their starting point. It doesn't matter what city is 
the starting point.

![Figure 2. A circuit](https://www.dcs.bbk.ac.uk/~vlad/pub/pop1/proj/Figure2.png)

However, the salesman also wishes to minimise the total distance that 
must be traveled.
