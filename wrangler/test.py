from dictionarize import abc_to_dictionary


ids = [21976, 20922, 44794, 131128]

fnames = ['../data/raw/'+str(t)+'.abc' for t in ids]

for fname in fnames:
    print(abc_to_dictionary(fname))