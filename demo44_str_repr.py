from datetime import datetime

now = datetime.now()
print(now)
print(repr(now))
print(str(now))

print([now])
print({now})
print((now,))
print((now))  # not a tuple
print({'key1': now})
print([now, str(now)])
