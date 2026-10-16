import numpy as np

def print_report(scores, subjects, grades):
    print("=" * 50)
    print("HORIZON ACADEMY — EXAM REPORT")
    print("=" * 50)

    student_avg = np.mean(scores, axis=1)
    subject_average = np.mean(scores, axis=0)

    print(f"Total Students : {len(np.sum(scores, axis=1))}")
    print(f"Total Subjects : {len(np.sum(scores, axis=0))}")

    class_avg = np.mean(np.mean(scores, axis=1))
    highest_score = np.max(np.max(scores, axis=1))
    lowest_score = np.min(np.min(scores, axis=1))
    overall_stddev = np.std(np.std(scores, axis=1))
    print("\n\nCLASS OVERVIEW")
    print(f"\tClass Avg : {class_avg:.2f}")
    print(f"\tHighest Score : {highest_score}")
    print(f"\tLowest Score : {lowest_score}")
    print(f"\tOverall Std Dev : {overall_stddev:.2f}")

    AP = student_avg[student_avg >= 90]
    A = student_avg[student_avg >= 75]
    B = student_avg[student_avg >= 60]
    C = student_avg[student_avg >= 50]
    F = student_avg[student_avg < 50]
    print("TOP PERFORMER")
    print(f"\tStudents {np.sum(grades=='A')} Avg : {np.mean(A):.2f} | Grade: A")

    print("WEAKEST STUDENTS")
    print(f"\tStudents {np.sum(grades=='F')} Avg : {np.mean(F):.2f} | Grade: F")

    print(f"\nFAILED STUDENTS (Avg < 50): {len(F)}")

    print("GRADE DISTRIBUTION")
    print(f"\tA+: {len(AP)}")
    print(f"\tA : {len(A)}")
    print(f"\tB : {len(B)}")
    print(f"\tC : {len(C)}")
    print(f"\tF : {len(F)}")

    hardest_subject = np.argmin(subject_average)
    easiest_subject = np.argmax(subject_average)

    print("SUBJECT ANALYSIS")
    print(f"\tHardest : {subjects[hardest_subject]} (Avg {np.mean(scores[:,hardest_subject]):.2f})")
    print(f"\tEasiest : {subjects[easiest_subject]} (Avg {np.mean(scores[:,easiest_subject]):.2f})")
