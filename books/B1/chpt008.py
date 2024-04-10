from random import randint

def nested_sum(l):
    c = 0
    total = 0
    while len(l) > c:
        total += sum(l[c])
        c+=1
    return total

def cumsum(l):
    new = list() 
    c = 0 
    while len(l) > c:
         new.append(sum(l[0:c+1])) 
         c+=1
    return new 

def middle(l):
    del l[0]
    del l[len(l)-1]
    return l

def chop(l):
    l.remove(l[0])
    l.remove(l[len(l)-1]) 

def is_sorted(l):
    ordered_l = sorted(l)
    if l == ordered_l:
        return True
    else:
        return False

def is_anagram(word_1, word_2):
    list_1 = list(word_1) 
    list_2 = list(word_2)
    if sorted(list_1) == sorted(list_2):
        return True
    else:
        return False

def has_duplicates(l):
    verification = list()
    c = 0 
    while len(l) > c:
        if l[c] not in verification:
            verification.append(l[c])
            c+=1 
        else:
            return True
    return False








