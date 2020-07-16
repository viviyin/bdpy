import PIL

print(f"pillow version={PIL.__version__}")


class MyClass(object):
    pass


inst1 = MyClass()

print(f"MyClass type={type(MyClass)}, inst1 type={type(inst1)}")
print(f"inst1 class is {inst1.__class__}")
print(f"type equal to class?{type(inst1) == inst1.__class__, inst1.__class__.__bases__}")
print(f"compare class with object class?{inst1.__class__ == MyClass}")

