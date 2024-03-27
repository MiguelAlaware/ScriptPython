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

def uses_only(word, pattern):
    only = list() 
    for letter in word:
        if letter in pattern: 
            only.append(True)
        else: 
            only.append(False) 
    if False in only:
        return False
    else:
        return True





def uses_all(word, pattern):
     used = list()   
     for letters in pattern:
        if letters in word:
            if letters in used:
                pass
            else:
                used.append(letters)
     return True if ''.join(used) == pattern else False

def is_abcedarian(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i += 1
    return True


def is_consecutive(word):
    i = 0
    if len(word) >= 6: 
        while i < len(word)-1:
            if word[i] == word[i+1]:
                if word[i+2] == word[i+3]:
                    if word[i+4] == word[i+5]:
                            return True
    else:
        return False


def has_palindrome(i, start, len):
    s = str(i)[start:start+len]
    return s[::-1] == s


def check(i):
    return(has_palindrome(i, 2, 4) and 
           has_palindrome(i+1, 1, 5) and
           has_palindrome(i+2, 1, 4) and
           has_palindrome(i+3, 0, 6))

def check_all():
    i = 100000
    while i <= 999999:
        if check(i):
            print(i)
        i = i + 1


        




