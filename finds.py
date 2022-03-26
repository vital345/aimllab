import pandas as pd

hp = []
hn = []
df = pd.read_csv('./enjoysport.csv')

for row in df.values:
  if row[-1] == 'yes':
    hp.append(row[:-1])
  else:
    hn.append(row[:-1])

h = hp[0][:]

for i in range(len(hp)):
  for j in range(len(hp[0])):
    if h[j] != hp[i][j]:
      h[j] = '?'
print('final hypothesis:', h)
