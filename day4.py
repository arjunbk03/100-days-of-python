#The goal of today is to build a rock, paper and scissors game:

#=============================================================
#Randomisation
import random

# random_number = random.randint(1,100) #creating random integers
# print(random_number)

# random_floating =  random.random()
# print(random_floating)

# random_uniform = random.uniform(1,100)
# print(random_uniform)

# random_num = random.randint(1,10)
# if random_num % 2 == 0:
#     print("Heads")
# else:
#     print("Tails")
#==================================================================

#Lists : Data structure --> storing data could be grouped
#fruits = ["oranges", "apples"]
us_states = ["New York", "Delaware", "New Jersey", "Maryland"]
print(us_states[0])
us_states.append("Arjunland")
print(us_states)
#===============================================================

import random
choices = ["Rock", "Scicors","Paper"]
random_choice = random.random(choices)
