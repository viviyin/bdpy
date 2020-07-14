def sample_func2(fix1, fix2, **kwargs):
    print(f"var1 = {fix1}, var2={fix2}")
    for k, v in kwargs.items():
        print(f"key={k}, value={v}")


sample_func2("hello", "world")
sample_func2("pass", "1parameter", name="BDPY")
sample_func2("pass", "1parameter", name="BDPY", duration="35hr")
sample_func2("pass", "1parameter", name="BDPY", duration="35hr", location="Taipei")
bdpy_course = {"name": "BDPY", "duration": "35hr", "location": "Taipei"}
sample_func2("pass", "flatten dictionary", **bdpy_course)
