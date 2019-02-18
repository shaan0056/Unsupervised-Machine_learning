import pandas as pd
import numpy as np
import os
import sklearn.model_selection as ms

for d in ['BASE','RP','PCA','ICA','RF']:
    n = './{}/'.format(d)
    if not os.path.exists(n):
        os.makedirs(n)

OUT = './BASE/'
madX1 = pd.read_csv('madelon_train.txt',header=None,sep=' ')
madX2 = pd.read_csv('madelon_valid.txt',header=None,sep=' ')
madX = pd.concat([madX1,madX2],0).astype(float)
madY1 = pd.read_csv('madelon_trainlabels.txt',header=None,sep=' ')
madY2 = pd.read_csv('madelon_validlabels.txt',header=None,sep=' ')
madY = pd.concat([madY1,madY2],0)
madY.columns = ['Class']

madelon_trgX, madelon_tstX, madelon_trgY, madelon_tstY = ms.train_test_split(madX, madY, test_size=0.3, random_state=0,stratify=madY)

madX = pd.DataFrame(madelon_trgX)
madY = pd.DataFrame(madelon_trgY)
madY.columns = ['Class']

madX2 = pd.DataFrame(madelon_tstX)
madY2 = pd.DataFrame(madelon_tstY)
madY2.columns = ['Class']

mad1 = pd.concat([madX,madY],1)
mad1 = mad1.dropna(axis=1,how='all')
mad1.to_hdf(OUT+'datasets.hdf','madelon',complib='blosc',complevel=9)

mad2 = pd.concat([madX2,madY2],1)
mad2 = mad2.dropna(axis=1,how='all')
mad2.to_hdf(OUT+'datasets.hdf','madelon_test',complib='blosc',complevel=9)



# digits = load_digits(return_X_y=True)
# digitsX,digitsY = digits

letter = pd.read_csv("LetterRecognition.csv",header=None)
letter = letter.iloc[1:]

#
# digits = np.hstack((digitsX, np.atleast_2d(digitsY).T))
# digits = pd.DataFrame(digits)
cols = list(range(letter.shape[1]))
cols[-1] = 'Class'
letter.columns = cols
letter.to_hdf(OUT+'datasets.hdf','letter',complib='blosc',complevel=9)