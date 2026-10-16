# # Matplotlib is used to draw the chart.
# import matplotlib.pyplot as plt
# # NumPy is used to create and calculate the sample data.
# import numpy as np


# # Create a random number generator with a fixed seed.
# # The fixed seed makes the same random data each time the program runs.
# rng = np.random.default_rng(42)

# # Create 100 x-values, starting at 1 and ending at 100.
# x = np.arange(1, 101)

# # Create y-values using a positive relationship with x.
# # The random noise makes the points look like realistic sample data
# # instead of placing every point exactly on one line.
# y = 2.5 * x + rng.normal(0, 15, size=100)

# # Find the straight line that best matches the data.
# # The line follows this formula: y = slope * x + intercept.
# # A degree of 1 tells polyfit to fit a straight line.
# slope, intercept = np.polyfit(x, y, 1)

# # Calculate the y-value of the trendline for every x-value.
# trendline = slope * x + intercept

# # Draw the 100 sample points as a scatter chart.
# plt.scatter(x, y, color="#40badf", label="Sample data")

# # Draw the fitted trendline on top of the sample points.
# plt.plot(x, trendline, color="#ff3c00", linewidth=2, label=f"Trendline (slope={slope:.2f})", linestyle="--")

# # Add a title, labels, grid, and legend to make the chart easier to read.
# plt.title("100 Sample Data Points with a Positive Trend")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid(True, alpha=0.3)
# plt.legend()

# # Adjust spacing so chart elements do not overlap.
# plt.tight_layout()

# # Display the chart in a window.
# plt.show()


# def add_all(*numbers):
#     total = 0

#     for i in range(len(numbers)):
#         total = total + numbers[i]

#     return total

# # print(f"Total :- {add_all(1,2,3,4)}")

# def show_profile(**details):
#     for key in details:
#         print(f"{key} : {str(details[key])}")
# # show_profile(name="Krish", age=18, city="Surat")

# def describe_product(name, *features, **details):
#     print("Product: " + name)
#     print("Features: " + str(features))
#     print("Details: " + str(details))

# describe_product("Laptop", "fast", "lightweight", price=55000, brand="TechCo")

# square = lambda x : x ** 2
# print(square(2))

# prices = [100, 250, 80, 500]
# doubled = list(map(lambda x : x * 2, prices))
# print(doubled)

# prices = [100, 250, 80, 500]
# expensive = list(filter(lambda x: x > 150, prices))
# print(expensive)


