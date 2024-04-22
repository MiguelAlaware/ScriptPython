

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


known = {}

def ackermann(m, n):
    if (m, n) in known:
        return known[(m, n)]
 
    elif m == 0:
        res = n + 1 
        known[(m, n)] = res
        return res
  
    elif m > 0 and n == 0:
        res = ackermann(m - 1, 1)
        known[(m, n)] = res 
        return res
   
    elif m > 0 and n > 0:
        res = ackermann(m - 1, ackermann(m, n - 1)) 
        known[(m, n)] = res
        return res


def has_duplicates(l):
    verification = dict()
    for i in l:
        verification[i] = 1
        if verification[i] in verification:
            return True
        else:
            return False

pairs = dict()
def rotate_word(l): 
    for i in l:
        if i == i[::-1]:
            pairs[i] = i[::-1]
    return pairs

