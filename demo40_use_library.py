import demo39_demo_library

print("inside demo40")
print(demo39_demo_library.foo(5, 6))
print(demo39_demo_library.bar(7, 8))

import demo39_demo_library as d39

print(d39.foo(9, 10))
print(d39.bar(11, 12))

from demo39_demo_library import foo, bar

print(foo(100, 200), bar(300, 400))

from demo39_demo_library import foo as f
from demo39_demo_library import bar as b

print(f(13, 14), b(15, 16))
