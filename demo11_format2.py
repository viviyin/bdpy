class Course(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Course name=%s" % (self.name)

    def __repr__(self):
        return "中文[name:%s]" % (self.name)


f1 = Course("BDPY")
print(f1)
print("%s,%r" % (f1, f1))
print("{0!s},{0!r},{0!a}".format(f1))
####
# class Course(object):
# ...     def __init__(self, name):
# ...         self.name = name
# ...
# ...     def __str__(self):
# ...         return "Course name=%s" % (self.name)
# ...
# ...     def __repr__(self):
# ...         return "[name:%s]" % (self.name)
# ...
# f1 = Course("BDPY")0
#   File "<input>", line 1
#     f1 = Course("BDPY")0
#                        ^
# SyntaxError: invalid syntax
# f1 = Course("BDPY")
# f1
# [name:BDPY]
#
