# excercise 1
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
coin= np.random.randint(1, 7)
print(coin)
# Use randint() again
coin= np.random.randint(1, 7)
print(coin)

# change seed
# Import numpy and set seed
import numpy as np
np.random.seed(124)

# Use randint() to simulate a dice
coin= np.random.randint(1, 7)
print(coin)
# Use randint() again
coin= np.random.randint(1, 7)
print(coin)

# exercise 2
# NumPy is imported, seed is set
np.random.seed(124)
# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <=3 or dice <=5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)


# excersice 3
# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <=3 or dice <=5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)