import datetime

class Student:
    pass_mark = 50

    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name.strip().title()
        self.marks = marks
        self.added = datetime.date.today()

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("marks must be a number")

        if not 0 <= value <= 100:
            raise ValueError("marks must be between 0 and 100")

        self._marks = round(value, 1)

    @property
    def grade(self):
        for threshold, letter in [ (90,"A+"),(80,"A"),(70,"B"), (60,"C"),(50,"D") ]:
            if self._marks >= threshold:
                return letter
            return "F"

    @property
    def is_passing(self):
        return self._marks >= self.pass_mark

    def to_dict(self):
        return {"roll" : self.roll, "name" : self.name, "marks" : self.marks, "grade" : self.grade, "status" : "Pass" if self.is_passing else "Fail"}

    def __repr__(self):
        return f"Student({self.roll}, {self.name}, {self.grade})"


class ScholarStudent(Student):
    scholarship_threshold = 85

    def __init__(self, roll, name, marks, scholarship=False):
        super().__init__(roll, name, marks)
        self.scholarship = scholarship

    @property
    def qualifies_for_scholarship(self):
        return self._marks >= ScholarStudent.scholarship_threshold

    def to_dict(self):

        d = super().to_dict()
        d['scholar'] = self.qualifies_for_scholarship

        return d



