# *args --> creates a tuple
# *args collects all positional args into a TUPLE

# def average(*args):
#     avg = sum(args) / len(args)
#     return avg

# print(average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def report(title, *scores):
#     print(f"\n=== {title} ===")
#     for i, s in enumerate(scores, 1):
#         print(f"Student {i} : {s}")
#         print(f" Average: {sum(scores)/len(scores):.1f}\n")

# report("AI Masterclass", 90, 85, 98, 80)


# **kwargs collects keyword args into a DICT

# def model_config(**kwargs):
#     print("Model configuration:")

#     for key, val in kwargs.items():
#         print(f"{key} --> {val}")

# model_config(n_estimators=100, max_depth=5, random_state=42)
# model_config(learning_rate=0.01, epochs=50)


# Lambda syntax: lambda params: expression

# num = float(input("Enter your number: "))

# square = lambda x: x**2
# print(f"Squared :- {square(num)}")

# add = lambda a, b: a + b
# print(add(2,3))


# grade = lambda s: "Pass" if s >= 50 else "Fail"
# print(grade(80))


# normalise = lambda x, mn, mx: (x - mn) / (mx - mn)
# print(normalise(0, 50, 100))

# dataset = [ {"name":"Krish", "marks":88}, {"name":"Shivam", "marks":45}, {"name":"Dhirendra", "marks":72}]

# ranked = sorted(dataset, key= lambda s: s['marks'], reverse=True)
# for s in ranked:
#     print(f"{s['name']}: {s['marks']}")


# map() applies a function to every item. filter() keeps only items where the function returns True. Both use lambdas as their function argument.

scores = [85, 45, 72, 33, 91]

# normalised = list(map(lambda s: s/100, scores))
# print(normalised)

# passed = list(filter(lambda s: s >= 50, scores))
# print(passed)

# result = list(map( lambda s: s/100, filter(lambda s: s>=50, scores) ))
# print(result)


ops = { "double" : lambda x: x * 2, "max" : lambda x: max(0, x), "sigmoid" : lambda x: 1 / (1 + 2.718**(-x)), "threshold" : lambda x: 1 if x > 0.5 else 0 }

for name, fn in ops.items(): 
    print(f"{name}(0.7) = {fn(0.7):.4f}")

