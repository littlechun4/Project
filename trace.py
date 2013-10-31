import numpy as np
import pandas as pd
import re

pattern = re.compile('{};')

chars = set('{};')
depth = 0

f = open('./trace.txt', 'r')
f2 = open('./a.txt', 'w')

for line in f:
  for c in line:
    if c == '{':
      depth += 1
      f2.write(str(depth)+'\n') # print depth
    elif c == '}':
      depth -= 1
      f2.write(str(depth)+'\n') # print depth
    elif c == ';':
      f2.write(str(depth)+'\n') # print depth

f.close()
f2.close()

my = np.genfromtxt('./a.txt')
when = pd.date_range(start=pd.datetime(2013,1,1), freq = '2S', periods=len(my))
x = pd.Series(my)
myx = pd.Series(x.values, index=when)
myx.to_csv('./synth.csv')
