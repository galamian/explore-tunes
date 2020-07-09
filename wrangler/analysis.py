import numpy as np
import pandas as pd


def get_info(dataframe):
    info = {
        'shape' : df.shape,
    }
    return info


filepath = "../data/processed/tunes_1_to_202030.pkl"

df = pd.read_pickle(filepath)

#df.R = df.R.fillna('None')

#df = df.convert_dtypes()


#rhythms = df.groupby('R').X.agg('count')
print(df.dtypes)

char_of_interest = 'd'
print(df[char_of_interest].unique())
print(df[df[char_of_interest].eq('* * * * HRTu|!mf!       |!sfz!  *** ***!D.S.!; ~.JN    HRTu|~.JN   HRTu|!5!!4!M*   !5! M; |           |*  P  !3!  !4!')])
#
#i = 56010
#print(df.melody[i])
#print(df.tune_id[i])
#print(df.E[i])