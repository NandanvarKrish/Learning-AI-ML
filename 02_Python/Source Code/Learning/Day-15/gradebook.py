import csv, json, os, datetime
from student import Student

class GradeBook:
    def __init__(self, filename="students.csv"):
        self.filename = filename
        self.students = self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            return []

        students = []
        with (open(self.filename) as f):
            for row in csv.DictReader(f):
                try:
                    s = Student(row["roll"], row["name"], float(row["marks"]))
                    students.append(s)
                except (ValueError, KeyError) as e:
                    print(f"⚠️ Skipped row: {e}")
            return students

    def _save(self):
        with open(self.filename, "w", newline="") as f:
            fields = ["roll", "name", "marks", "grade", "status"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(s.to_dict() for s in self.students)

    def add(self, roll, name, marks):
        try:
            s = Student(roll, name, marks)
            self.students.append(s)
            self._save()
            print(f"✅ Added {s.name} — Grade: {s.grade}")

        except (ValueError, TypeError) as e:
            print(f"❌ Error: {e}")

    def search(self, name):
        query = name.lower()
        results = [s for s in self.students if query in s.name.lower()]
        return results

    @property
    def stats(self):
        if not self.students:
            return {}

        all_marks = [s.marks for s in self.students]

        return {"total": len(self.students), "average": round(sum(all_marks) / len(all_marks), 2),
                "highest": max(all_marks), "lowest": min(all_marks),
                "passed": sum(1 for s in self.students if s.is_passing),
                "grades": {g: sum(1 for s in self.students if s.grade == g) for g in ["A+", "A", "B", "C", "D", "F"]}}

    def leaderboard(self, top=5):
        return sorted(self.students, key=lambda s: s.marks, reverse=True)[:top]

    def report(self, *args, **kwargs):
        show_stats = kwargs.get("show_stats", True)

        sort_by = kwargs.get("sort_by", "marks")
        print(f"\n{'=' * 44}")
        print(f" GRADE REPORT — {datetime.date.today()}")
        print(f"{'=' * 44}")

        ordered = sorted(self.students, key=lambda s: getattr(s, sort_by, s.marks), reverse=True)

        for rank, s in enumerate(ordered, 1): icon = "✅" if s.is_passing else "❌"

        print(f" {rank:>2}. {s.name:15} {s.marks:>5} {s.grade:>3} {icon}")

        if show_stats:
            st = self.stats
            print(f"\n Average: {st['average']} | Passed: {st['passed']}/{st['total']}")

    def batch_report(self, batch_size=3):
        for i in range(0, len(self.students), batch_size):
            yield self.students[i:i + batch_size]

    def export_json(self):
        data = {"exported": str(datetime.date.today()), "stats": self.stats,
                "students": [s.to_dict() for s in self.students]}

        with open("report.json", "w") as f:
            json.dump(data, f, indent=4)
        print("📄 Exported to report.json")


# print(GradeBook())


