# scores = [85, 45, 72, 33, 91, 58]
#
# all_norm = [s/100 for s in scores]
# print("All normalised:", all_norm)
#
# pass_norm = [s/100 for s in scores if s >= 50]
# print("Passing only:", pass_norm)


# scores = [85, 45, 72, 33, 91, 58]
# labels = ["Pass" if s >= 50 else "Fail" for s in scores]
# print(f"Labels: {labels}")
#
# y = [1 if s >= 50 else 0 for s in scores]
# print(f"Binary (y): {y}")
#
# dataset = [{"marks": s, "passed": 1 if s >= 50 else 0} for s in scores]
# print(f"Dataset: {dataset}")

# y_true=[1,0,1,1]
# y_pred = [1, 0, 0, 1]
#
# print(sum(1 for t,p in zip(y_true,y_pred) if t==p))

# names = ["Krish", "Shivam", "Dhiren", "Shubh"]
# scores = [88, 45, 72, 33]
#
# grade_map = {n:s for n, s in zip(names, scores)}
# # print(grade_map)
#
# for name, score in zip(names, scores):
#     status = "✅ Pass" if score >= 50 else "❌ Fail"
#     print(f"{name}: {score} → {status}")


# scores = [85, 45, 72, 33, 91, 58]
#
# for i, score in enumerate(scores, start=1):
#     status = "✅" if score >= 50 else "❌"
#     print(f"Student {i}: {score} {status}")


# losses = [2.1, 1.4, 0.8, 0.4, 0.2]
#
# for epoch, loss in enumerate(losses, 1):
#     print(f"Epoch {epoch}/5 — loss: {loss:.1f}")


# list_version = [x**2 for x in range(1000)]
# print(type(list_version))
# print(f"Length of List: {len(list_version)}")
#
# gen_version = (x**2 for x in range(1000))
# print(type(gen_version))
# # print(len(gen_version))


# def batch_loader(data, batch_size=2):
#     for i in range(0, len(data), batch_size):
#         yield data[i : i + batch_size]
#
# images = ["img1", "img2", "img3", "img4", "img5", "img6"]
#
# for batch_num, batch in enumerate(batch_loader(images), 1):
#     print(f"Batch {batch_num}: {batch}")


names = ["Krish", "Shivam", "Dhiren", "Shubh"]
scores = [88, 45, 72, 33]

full_data = {n: s for n, s in zip(names, scores)}
print("Full data:", full_data)

X = [s/100 for s in scores]
print("Normalised X:", X)

y = [1 if s >= 50 else 0 for s in scores]
print("Labels y:", y)

passing = {n: s for n, s in zip(names, scores) if s >= 50}
print("Passing students:", passing)

print("\n\t\t=== STUDENT REPORT ===")
for i, (name, score, norm, label) in enumerate(zip(names,scores,X,y), 1):
    status = "✅" if label else "❌"
    print(f"{i}. {name:<8} | raw:{score} | norm:{norm:.2f} | y={label} {status}")

print(f"\nTotal: {len(names)} | Passed: {sum(y)} | Accuracy feature ready ✅")
