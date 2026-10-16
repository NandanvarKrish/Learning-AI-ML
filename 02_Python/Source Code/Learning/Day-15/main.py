from gradebook import GradeBook
from student import ScholarStudent

gb = GradeBook()

gb.add("001", "Krish", 92)
gb.add("002", "Deven", 45)
gb.add("003", "Shivam", 78)
gb.add("004", "Arya", 88)
gb.add("005", "Atharv", 150)

scholar = ScholarStudent("006", "Hira Baig", 94)
gb.students.append(scholar)
print(f"Scholarship? {scholar.qualifies_for_scholarship}")

gb.report(show_stats=True, sort_by="marks")
print("\n🏆 TOP 3:")

for i, s in enumerate(gb.leaderboard(3), 1):
    print(f" #{i} {s.name}: {s.marks}")

print("\n🔍 Search 'krish':")
for s in gb.search("krish"):
    print(f" {s}")

print(f"\n📊 Class stats: {gb.stats}")
print("\n📋 Batch report (3 per batch):")

for i, batch in enumerate(gb.batch_report(3), 1):
    print(f" Batch {i}: {[s.name for s in batch]}")


