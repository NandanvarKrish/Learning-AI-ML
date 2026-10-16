# def average(*args):
#     avg = sum(args) / len(args)
#     return avg


# print(average(2, 3, 5))


# def model_config(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")

# square = lambda x: x ** 2
# print(square(2))

# maximum = lambda *m: max(m)
# print(maximum(1,2,3,4,5))

# normalise = lambda x, x_min, x_max: (x-x_min) / (x_max-x_min)
# print(normalise(50, 10, 100))

# grade = lambda marks: "pass" if marks >= 50 else print("fail")
# print(grade(80))

# threshold = lambda x: 1 if x > 0.5 else 0
# print(threshold(3))

# dataset = [ {"name":"Krish", "marks":88}, {"name":"Shivam", "marks":45}, {"name":"Dhirendra", "marks":72}]

# ranked = sorted(dataset, key= lambda s: s['marks'], reverse=True)
# for s in ranked:
#     print(f"{s['name']} : {s['marks']}")


# dataset = [ {"name":"Krish", "marks":88}, {"name":"Shivam", "marks":45}, {"name":"Dhirendra", "marks":72}, {"name" : "Ankit", "marks" : 33}]

# normalise = list(map(lambda s: s['marks'] / 100, dataset))
# print(normalise)


# pass_only = list(filter(lambda p: p['marks'] >= 50, dataset))
# print(pass_only)


# normalised_result = list(map(lambda s: s['marks'] / 100, filter(lambda p: p['marks'] >= 50, dataset)))
# print(normalised_result)

# grade_fn = lambda r: "A" if r['marks'] >= 80 else "B" if r['marks'] >= 50 else "F"

dataset = [ {"name":"Krish", "marks":88}, {"name":"Shivam", "marks":45}, {"name":"Dhirendra", "marks":72}, {"name" : "Ankit", "marks" : 33}]

grade_fn = sorted(dataset, key= lambda r: "A" if r['marks'] >= 80 else "B" if r['marks'] >= 50 else "F", reverse=True)

final_grade = list(map(lambda r: r['marks'] / 100, filter(lambda p: p['marks'] >= 50, dataset)))

print(final_grade)

for s in grade_fn:
    print(f"{s['name']} --> {s['marks']}")

# print(list(filter(lambda x: x > 50, [30, 60, 45, 80])))

# print(list(map(lambda x: x**2, range(1,4))))

# def average(*args): return sum(args)/len(args)
# print(average(80, 90, 70))


