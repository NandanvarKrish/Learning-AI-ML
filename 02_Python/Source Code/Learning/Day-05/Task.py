# scores = [72, 88, 45, 91, 63, 77]

# scores.sort()
# print(f"Max score is {max(scores)}")
# print(f"Min score is {min(scores)}")
# print(f"Sum of scores is {sum(scores)}")
# print(f"Length of scores is {len(scores)}")

# print(scores[:3])
# print(scores[:-2])
# print(scores[::2])


# RGB = (255, 128, 0)

# print(RGB[0])

# RGB[0] = 100 # ERROR BCOZ WE CAN'T CHANGE TUPLE VALUES


# labels = ["cat", "dog", "cat", "bird", "dog", "cat"]
# print(f"Labels: {labels}")

# unique = set(labels)
# print(f"Unique: {unique}")


# image = [ [0, 128, 255], [64, 192, 128], [255, 0, 64 ] ]

# nl = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(nl)
# print(nl[0][0])

# normalised = [[p/255 for p in row] for row in image]
# print(normalised[0])


# squares = [x**2 for x in range(1, 11, 1)]
# print(squares)


# image = [[0, 128, 255], [64, 192, 128], [255, 0, 64]]
# image[1][2] = 128
# normalised = [[p/255 for p in row] for row in image]


# preds = []

# for i in range(5):
#     preds.append(i * 0.1)


# preds.remove(0.2)

# print(preds)


scores = [25, 65, 85, 85, 75, 85, 95, 65]

for i in range(0, 8, 1):
    print(f"{i}) Score = {scores[i]}. You're {"pass" if scores[i] >= 50 else "Fail"}")
    # if scores[i] >= 50:
    #     print("Pass")
    # else:
    #     print("Fail")

print(f"Sum: {sum(scores)}")
print(f"Length: {len(scores)}")
print(f"Average: {sum(scores)/len(scores)}")