def nested_sum(l):
    c = 0
    total = 0
    while len(l) > c:
        total += sum(l[c])
        c+=1
    return total

def cumsum(l):
    c = 0 
    while len(l) > c:
        l[c] = sum(l[0:c+1])
        c+=1 
    return l

t = [1, 2, 3]
print(cumsum(t))

