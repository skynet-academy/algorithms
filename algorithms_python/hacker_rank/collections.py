from collections import namedtuple


students = int(input())
Student = namedtuple('Student', ' '.join(input().split()).split(" "))
total = 0

for _ in range(students):
    ID, MARKS, NAME, CLASS = ' '.join(input().split()).split(" ")
    std = Student(ID, MARKS, NAME, CLASS)
    total += int(std.MARKS)
print(total / students)
