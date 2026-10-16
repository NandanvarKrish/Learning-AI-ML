# scores = [85, 45, 72, 33, 91]
# normalise_scores = [s/100 for s in scores]
# passed = [s for s in scores if s >= 50]
# print(passed)
# print(normalise_scores)

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
#
# print(f"Matrix: {matrix}")
#
# flat = [x for row in matrix for x in row]
# print(f"Flat: {flat}")

# names = ['krish', 'satyam', 'amar', 'atharv']
# age = [18, 19, 16, 18]
#
# dict_comp = {n:a for n, a in zip(names, age)}
# print(dict_comp)

# adult = {n:a for n, a in zip(names, age) if a >= 18}
# print(adult)

# original = {"a":1, "b":2, "c":3}
# print(original)
#
# inverted = {v:k for k, v in original.items()}
# print(inverted)

# names = ["krish", "shyam", "shivam"]
# scores = [88, 45, 72]
# grades = ["A", "F", "B"]
#
# for name, score, grade in zip(names, scores, grades):
#     print(f"{name}: {score} ({grade})")

# y_true = [1, 0, 1, 1]
# y_pred = [1, 0, 0, 1]
#
# correct = sum(1 for t, p in zip(y_true, y_pred) if t==p)
# print(f"Accuracy: {correct/len(y_true)*100:.2f}%")

# scores = [88, 45, 72]
# for i, score in enumerate(scores, start=1):
#     print(f"Student {i}: {score}")

# for epoch, loss in enumerate([2.1,1.4,0.8,0.3], 1):
#     print(f"Epoch {epoch}: loss={loss}")


# big_list = [x for x in range(1001)]
# big_gen = (x for x in range(1001))
# # print(big_list)
# # print(big_gen)
#
# for i in big_gen:
#     print(i, end="\n")

# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1

# print(countdown(5))

# for i in countdown(5):
#     print(i)

# gen = countdown(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# squares_gen = (n**2 for n in range(5123))
#
# total = sum(squares_gen)
# print(total)

class Sale:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._price = price


    def read_sales(path):
        with open(path) as file:
            for line in file:
                item, amount_str = line.strip().split(",")
                yield Sale(item, float(amount_str))

    def big_sales(sales, threshold=50):
        for sale in sales:
            if sale.price >= threshold:
                yield sale

# s = Sale("Laptop", 1_000_000)

    sales_stream = read_sales("sales_log.csv")
    notable = big_sales(sales_stream, threshold=100)


    import itertools

    for sale in itertools.islice(notable, 3):
        print(f"{sale.item} --> {sale.price}")

    total = sum(sale.price for sale in big_sales(read_sales("sales_log.csv")))

top_items = ["Laptop", "Monitor", "Keyboard", "Mouse", "Gamepad", "Racing Wheel"]
price_lookup = [len(item)*10 for item in top_items]
# print(price_lookup)

for i in range (len(top_items)):
    s = Sale(top_items[i], price_lookup[i])
    print(f"{s.item} --> {s.price}")
