#to use first input a population number in pop
#then on bottum input desired numbers in print function

import random
birthday_list = []
pop = 35

def bdaygen(population):
    i = population
    while i > 0:
        birthday_list.append(random.randint(1, 365))
        i = i - 1
def samebday():
    k = 0
    birthday_list.sort()
    while k < pop - 1:
        if birthday_list[k] == birthday_list[k+1]:
            return(True)
        else:
            k+=1
def simulate(tries):
    yes = 0
    p = tries
    while p > 0:
        birthday_list.clear()
        bdaygen(pop)
        if samebday() == True:
            yes = yes + 1
            p = p - 1
        else:
            p = p - 1
    u = yes/tries
    o = round(u * 100)
    return (o)

#times is how many times use for averaging
#tries is how many tries used to simulate and get percent
def avg(times, tries):
    a = times
    temp = []
    while a > 0:
        temp.append(simulate(tries))
        a = a - 1
    b = sum(temp) / times
    return(round(b))


print(avg(20, 20))
