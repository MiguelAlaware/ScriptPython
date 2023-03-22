def ack(m, n):
    if m == 0:
        return n + 1
    if n ==0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n-1))


def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1: -1]

def is_palindrome(word):
    length = len(word)
    inv = list()
    cont = list()
    count = 1
    for n in range(length):
        inv.append(word[-count])
        count+=1
    for m in range(length):
        cont.append(word[m])
    print(inv)
    print(cont)   
    if cont == inv:
        return True
    else:
        return False    
    
print(is_palindrome('tenet'))
