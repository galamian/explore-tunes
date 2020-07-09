from pathlib import Path


'''function that inputs a filename and returns a dictionary with all found fields in abc description'''
def abc_to_dictionary(fname):
    dic = {}
    try:
        id = Path(fname).stem
        f = open(fname, 'r')
        lines = f.readlines()
        tune = ''
        dic['tune_id']=id
        for line in lines:
            line = line.strip()
            if (len(line)>2) and \
                    (line[1] == ':') and \
                        (line[0] not in ['|', ':', '!', '\"', '\'']) and \
                            (line[2] not in ['|']) and \
                                (not line[0].isdigit()): 
                key, val = line[0], line[2:].strip()
                if key in dic:
                    dic[key] = dic[key] + '; ' + val
                    #if type(dic[key]) is str:
                    #    dic[key] = [dic[key], val]
                    #else:
                    #    dic[key].append(val)
                else:
                    dic[key] = val
            else:
                tune = tune + line.strip()

        
        dic['melody']=tune
    except:
        pass
    
    return dic
    


#print(abc_to_dictionary('../data/raw/1.abc'))