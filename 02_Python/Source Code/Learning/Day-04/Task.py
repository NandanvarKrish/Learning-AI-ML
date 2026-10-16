# PRINT 1 TO 20 NUMBERS

# for i in range(1, 21, 1):
#     print(i)
    
# PRINT EVEN NUMBERS NETWEEN 1 TO 20

# for i in range(1, 21, 2):
#     print(i)


# PRINT PASS/FAIL

# scores = [85, 42, 91, 37, 76, 58, 22, 99]

# for score in scores:
#     if score >= 50:
#         print(f"Your score is {score}. So you're Pass ✅")
#     else:
#         print(f"Your score is {score}. So you're Fail ❌")


# MULTIPLICATION TABLE

# num = int(input("Enter the number: "))

# for i in range(1, 11, 1):
#     print(f"{num} x {i} = {num*i}")


# WHILE LOOP TRAINING SIMULATOR

# loss = 10.0
# epoch = 1

# while loss > 0.1:
#     loss = loss * 0.7
#     print(f"Epoch {epoch}: loss = {loss:.4f}")
#     epoch += 1


# NUM PRINT AND BREAK WHEN NUM == 15

# for i in range(1, 21, 1):
#     print(i)
#     if i == 15:
#         break
#     else:
#         continue

# SKIP ODD NUMBERS

# for i in range(1, 21, 1):
#     if i % 2 !=  0:
#         continue
#     print(i)


# NESTED LOOP 3x3 MULTIPLICATION GRID

# for row in range(1, 4, 1):
#     for col in range (1, 4, 1):
#         print(f"{row} x {col} = {row * col}", end = " ")
#     print()




# Bug Hunt — 4 errors to find and fix

# Bug 1: range includes the stop value? 
for i in range(1, 6):
    print(i) # Expected: 1 2 3 4 5 — what does this actually print?

# Bug 2: infinite loop risk 
count = 0
while count < 5:
    print(count)
    count += 1
# Bug 2: counter never updates → infinite loop!
# Bug 3: break vs continue confused
for n in range(1, 11): 
    if n % 2 == 0: 
        continue
    print(n)

# Bug 3: should SKIP evens not STOP the loop print(n) 
 
# Bug 4: nested loop wrong range 
for row in range(1, 4): 
    for col in range(1, 4):
        print(f"{row}x{col}", end=" ")

# Bug 4: gives rows 0,1,2 — should be 1,2,3 for col in range(3): print(f"{row}x{col}", end=" ")
