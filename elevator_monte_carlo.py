from collections import defaultdict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
floors = 16
capacity = 10
trials = 10000
np.random.seed(2017)
 
d = defaultdict(int)
 
for i in range(trials):
    d[len(np.unique(np.random.randint(floors, size=capacity)))] += 1
 
print('Trials: {}'.format(trials))
for k, v in d.items():
    print('{}: {}'.format(k, v))
 
df = (pd.DataFrame(list(d.items()), columns=['stops', 'frequency'])
      .set_index('stops')
      .reindex(range(1, floors+1))
      .fillna(0)
      .reset_index())
df.frequency = df.frequency.astype(int)
print('Mean: {:.2f}'.format(
    (df.stops * df.frequency).sum() / df.frequency.sum()))
 
ax = df.plot.bar(x='stops', y='frequency', width=1, legend=False)
ax.tick_params(axis='x', length=0)
plt.xticks(rotation=0)
plt.show()
