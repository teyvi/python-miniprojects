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

# plot random walk
# NumPy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()