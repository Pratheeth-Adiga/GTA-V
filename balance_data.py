import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load('training_data.npy',allow_pickle=True)

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

lefts = []
rights = []
forwards = []
backwards = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1,0,0,0]:
        lefts.append([img,choice])
    elif choice == [0,1,0,0]:
        forwards.append([img,choice])
    elif choice == [0,0,1,0]:
        rights.append([img,choice])
    elif choice == [0,0,0,1]:
        backwards.append([img,choice])
    else:
        print('no match')


forwards = forwards[:len(lefts)][:len(rights)][:len(backwards)]
lefts = lefts[:len(backwards)]
rights = rights[:len(backwards)]
backwards = backwards[:len(lefts)][:len(rights)]


final_data = forwards + lefts + rights + backwards
shuffle(final_data)

np.save('training_data-1-balanced.npy', final_data)




