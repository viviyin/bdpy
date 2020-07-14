def foo(a, b):
    return f"[foo]result={a + b}"


def bar(a, b):
    return f"[bar]result={a * b}"


print(f"for demo39, name={__name__}")
if __name__ == '__main__':
    print("validate demo39 from demo39")
    print(foo(3, 4))
    print(bar(5, 6))
