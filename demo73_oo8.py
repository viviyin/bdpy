class Emp:
    gradeLevel = 6

    def startWork(self):
        pass

    def stopWork(self):
        pass


class RD(Emp):
    pass


class PM(Emp):
    pass


class HR(Emp):
    pass


e1 = Emp()
r1 = RD()
p1 = PM()
hr1 = HR()
staffs = [(e1, "Employee"), (r1, "RD Engineer"), (p1, "ProductMarketing"), (hr1, "Human Resource")]
emp_classes = [Emp, RD, PM, HR]

for staff, name in staffs:
    for emp_class in emp_classes:
        isA = isinstance(staff, emp_class)
        msg1 = 'is a' if isA else 'is not a'
        print(name, msg1, emp_class.__name__)
for c1 in emp_classes:
    for c2 in emp_classes:
        isSub = issubclass(c1, c2)
        message = '{} a subclass of'.format('is' if isSub else 'is not')
        print(c1.__name__, message, c2.__name__)

print(Emp.gradeLevel, RD.gradeLevel, PM.gradeLevel)
RD.gradeLevel = 8
print(Emp.gradeLevel, RD.gradeLevel, PM.gradeLevel)
Emp.gradeLevel = 7
print(Emp.gradeLevel, RD.gradeLevel, PM.gradeLevel)
print(e1.gradeLevel, r1.gradeLevel, p1.gradeLevel)
