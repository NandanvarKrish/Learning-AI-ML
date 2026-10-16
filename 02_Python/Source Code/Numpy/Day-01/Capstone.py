import numpy as np
from report import print_report

np.random.seed(99)

subjects = ['Maths', 'Science', 'English', 'History', 'Computer']

num_students = 50

scores = np.random.randint(30, 101, size=(num_students, 5))
# print(f"Shape: {scores.shape}")

student_totals = np.sum(scores, axis=1)
student_averages = np.mean(scores, axis=1)
subject_average = np.mean(scores, axis=0)

fail_mask = student_averages < 50
failing_students = np.where(fail_mask)[0]

# print(f"Student who failed : {len(failing_students)}")

conditions = [
    student_averages >= 90,
    student_averages >= 75,
    student_averages >= 60, 
    student_averages >= 50
]

choices = ['A+', 'A', 'B', 'C']
grades = np.select(conditions, choices, default='F')

# print(grades)

print('=' * 40)
print('''Subjects | Avg  | High | Low| StdDev|''')
for i in range(len(subjects)):
    print(f"{subjects[i]:8} | {student_averages[i]:3} | {scores[:,i].max():4} | {scores[:,i].min()} | {scores[i].std():.2f} |")
print('=' * 40)

hardest_subject = np.argmin(subject_average)
print(f"Hardest Subject : {subjects[hardest_subject]}")

easiest_subject = np.argmax(subject_average)
print(f"Easiest Subject : {subjects[easiest_subject]}")

above_80_per_subject = np.sum(scores > 80, axis=0)

AP= np.sum(student_averages >= 90, axis=0)
A = np.sum(student_averages >= 75, axis=0)
B = np.sum(student_averages >= 60, axis=0)
C = np.sum(student_averages >= 50, axis=0)
F = np.sum(student_averages < 50, axis=0)
# print(AP)
# print(A)
# print(B)
# print(C)
# print(F)

norm = (scores - np.min(scores)) / (np.max(scores) - np.min(scores))
# print(np.round(norm[:3], 2))

ranked_indices = np.argsort(student_totals)[::-1]
for rank, idx in enumerate(ranked_indices[:5], 1):
    print(f"Rank {rank}: Student {idx+1} — Total: {student_totals[idx]}")

scores_bonused = scores.copy()
mask_low = scores_bonused < 40
scores_bonused[mask_low] += 5
scores_bonused = np.clip(scores_bonused, 0, 100)

print_report(scores, subjects, grades)

