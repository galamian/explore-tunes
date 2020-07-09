import sys
import numpy as np
import pandas as pd
from progressbar import ProgressBar

from dictionarize import abc_to_dictionary

tuid_from, tuid_to = 1, 1

if len(sys.argv)>1:
	tuid_from = int(sys.argv[1]) if sys.argv[1] else 1
	if len(sys.argv)>2:
		tuid_to = int(sys.argv[2]) if sys.argv[2] else tuid_from	
else:
	print('no tune_ids passed as parameter')

dic_list = []


pbar = ProgressBar()
for tuid in pbar(range(tuid_from, tuid_to)):
    fname = '../data/raw/'+str(tuid)+'.abc'
    dc = abc_to_dictionary(fname)
    if dc:
        dic_list.append(dc)

dataFrame = pd.DataFrame.from_dict(dic_list)

dataFrame = dataFrame.convert_dtypes()

#print(dataFrame)
if len(sys.argv)>3 and sys.argv[3]=='csv':
    dataFrame.to_csv('../data/processed/tunes_'+str(tuid_from)+'_to_'+str(tuid_to)+'.csv')
else:
    dataFrame.to_pickle('../data/processed/tunes_'+str(tuid_from)+'_to_'+str(tuid_to)+'.pkl')