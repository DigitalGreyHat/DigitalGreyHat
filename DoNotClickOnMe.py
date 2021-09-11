import os
import glob

files = glob.glob('MY_LIFE/*') #Just kidding
for f in files:
    os.remove(f)
