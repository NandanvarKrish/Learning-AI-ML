# LISTS

scores = [85, 92, 78, 85, 91] # Lists are mutable and can store anything

# print(scores[0])
# print(scores[-1])
# print(scores[1:4])

# scores.append(95)

# print(scores)

# scores.remove(78)
# print(scores)

# scores.sort()
# print(scores)

# print(len(scores))
# print(sum(scores))
# print(max(scores))
# print(scores.sort())
# scores.reverse()
# print(scores)


# TUPLES AND SETS

# rgb = (255, 0, 255) # Tuples are immutable can store duplicate values

# print(rgb[0])

# labels = {"Cat", "Dog", "Bird", "Human", "Cat"} # Sets are mutabe but only stores unique values
# print(labels)


# LISTS COMPREHENSION

# print("="*40)
# squares = [x**2 for x in range(1, 11, 1)]
# print(squares)

# scores = [85, 92, 78, 85, 91, 48, 55, 69, 33]

# studentsPassed = [p for p in scores if p >= 50]

# print(studentsPassed)
# print(f"Length of scores is {len(scores)}")
# print(f"Length of studentPassed is {len(studentsPassed)}")
# print(f"Total students failed = {len(scores)-len(studentsPassed)}")
# print("="*40)


# NESTED LISTS

# image = [ [0, 128, 255], [64, 192, 128], [255, 0, 64 ] ]

# nl = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(nl)
# print(nl[0][0])

# normalised = [[p/255 for p in row] for row in image]
# print(normalised[0])

