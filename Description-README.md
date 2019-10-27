# Same-Birthday-Simulator
Description:

This project is a python written simulator that illustrates the famous birthday problem in statistics.
The birthday problem takes a room of people and determines what the chance is that two people share 
the same birthday. For this project, I neglected leap years and to generate a list of people with different
birthdays I used python's random module. Birthdays are represents as a single number from 1 to 365.

To Use:
1. Enter a number in the "pop" variable @ line 3 (it is set at 35 as default)
  - This number is the number of people in the room or population of project

2. In print function @ line 45 or last line of code enter desire parameters for the avg function
  - The first number is the times parameter which is how many times you want to run the the birthday problem
  - The second number is the tries parameter which is how many tries you want to run the whole simulation to 
    get a percent over different times the birthday problem is run

What the Functions Do:

First function bdaygen(population) is used to create a list of people with different birthdays

Second fuction samebday() returns a True if two people have the same birthday

Third function simulate(tries) returns a precent of how many simulations have 2 people that have the same
  birthday so if we ran 2 simulations and both have 2 people with same birthdays, then function will return 100%

Fourth function avg(times, tries) returns an average percentage over the percents that were calculated in the
  simulate(tries) function 
  
