def sample_func1(fix1, fix2, *var3):
    print(f"I got two fix parameters:{fix1},{fix2}")
    print([v for v in var3])


sample_func1("hello", "world")
sample_func1("pass", "something", 500)
sample_func1("pass", "many:", 500, 3.14, 'hi', None)
l1 = ['apple', 'banana', 'citron']
sample_func1("pass", "list:", l1)
sample_func1("pass", " flatten list:", *l1)
t1 = ('apple', 'banana', 'citron')
sample_func1("pass", " flatten tuple:", *t1)
