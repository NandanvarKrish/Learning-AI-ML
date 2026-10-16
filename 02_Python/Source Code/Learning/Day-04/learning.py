# scores = [85, 42, 91, 37, 76]

# for score in scores:
#     if score >= 50:
#         print(f"{score} --> Pass ✅")
#     else:
#         print(f"{score} --> Fail ❌")

# for i in range(0, 101, 1):
#     print(i)


# for i in range(0, 51, 1):
#     if (i == 5):
#         continue

#     if (i == 48):
#         break

#     print(i)

# for i in range(0, 51, 1):
#     if(i % 2 == 0):
#         continue

#     print(i)


# TRAINING AI MODEL NEURAL NETWORK

# dataset = [10, 20, 30, 40, 50] # 5 data points
# weight = 1.0
# lr = 0.01 # learning rate

# for epoch in range(3): # 3 training epochs
#     for data_point in dataset: # each sample 
#         prediction = weight * data_point
#         error = prediction - 100
#         weight -= lr * error
#         print(f"Epoch {epoch+1}: weight = {weight:.4f}")


# PRINT 1 to 20

# for i in range(0, 21, 1):
#     print(i)


# Looped through a list of 5 test scores and printed Pass/Fail for each

# scores = [50, 10, 99, 100, 33]

# for score in scores:
#     if (score >= 50):
#         print(f"Your score is {score}! You're pass ✅")

#     else:
#         print(f"Your score is {score}! You're fail ❌")


num = int(input("Enter the number: "))

for i in range(1, 11, 1):
    print(f"{num} x {i} = {num*i}")