def histogram(s):
    d = dict()
    for c in s: 
        d[c] = d.get(c, 0) + 1
    return d

def read_text(file):
    words = dict()
    exec = open(file)   
    for lines in exec:
        if lines in words.keys():
           pass 
        else:
           words[lines.strip()] = 1
    return words

def inverse_dict(d):
    inverse = dict()
    for key, val in d.items():
        inverse.setdefault(val, []).append(key)
    return inverse







