def word_length(file):
    fin = open(file)
    for line in fin:
        if len(line.strip()) > 20:
            print(line)

def has_no_e(file):
    fin = open(file)
    count_e = 0 
    count_all = 0 
    for line in fin:
        count_all+=1 
        if 'e' in line:
            count_e+=1 
    return count_e * 100 / count_all

def avoids(prohibited, word):
    for w in range(0, len(prohibited)):
        if prohibited[w] in word:
            return False
    return True

def avoids_plus(file, avoid):
    fin = open(file)
    for line in fin:
        if avoids(avoid, line):
           print(line) 
        else:
            pass

def uses_only(file, pattern):
    





