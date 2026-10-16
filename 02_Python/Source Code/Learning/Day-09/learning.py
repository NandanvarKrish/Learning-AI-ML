# import math

# print(math.sqrt(25))
# print(math.pi)
# print(math.ceil(4.2))
# print(math.floor(4.9))
# print(math.log(100, 10))


# import math as m
# print(m.sqrt(144)) 


# from math import sqrt, pi, factorial

# print(sqrt(81))
# print(factorial(5))


# import random
# import datetime
# import os

# print(random.randint(1, 100))
# print(random.choice(["cat", "dog", "bird"]))

# data = [1, 2, 3, 4, 5]
# random.shuffle(data)
# print(data)

# today = datetime.date.today()
# print(today)

# born = datetime.date(2008, 10, 20)
# age = (today - born).days // 365
# print(f"Age: {age} years")

# print(os.getcwd())
# print(os.listdir("."))
# print(os.path.exists("data.csv"))

# from myModule import normalise, get_grade, PI

# scores = [45, 78, 91, 33, 85]

# print(normalise(scores))

# for s in scores:
#     print(f"{s} → {get_grade(s)}")

# print(f"Pi = {PI}")

import random
import math
import os
# Set random seed — reproducible ML experiments
random.seed(42) # same seed = same "random" results # Generate synthetic dataset

dataset = [{ "x": random.uniform(0, 10), "y": random.randint(0, 1) } for _ in range(100)] # Shuffle and split 80/20

random.shuffle(dataset)
split = int(0.8 * len(dataset))
train = dataset[:split]
test = dataset[split:]
print(f"Train: {len(train)}, Test: {len(test)}")
print(f"sqrt(len) = {math.sqrt(len(dataset)):.2f}")

# Check if data folder exists
if not os.path.exists("data"):
    os.makedirs("Trial_9th_day")
    print("Created Trial_9th_day/ folder")

