import os
import sys

DATA_DIR = "中文"
print(f"current working directory:{os.getcwd()}")
os.mkdir(DATA_DIR)
os.chdir(DATA_DIR)
print(f"[II]current working directory:{os.getcwd()}")
os.chdir('..')
os.rmdir(DATA_DIR)
for item in sys.argv:
    print(f"got an argument:{item}")
