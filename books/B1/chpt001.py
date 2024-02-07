def right_justify(s):
    print(" " * (70 - len(s)) + s)

# right_justify("monty")
def print_twice(bruce):
    print(bruce)
    print(bruce)

def print_spam():
    print("spam")

def do_twice(f,v):
    f(v)
    f(v)

# do_twice(print_twice, "spam")

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

# do_four(print_twice, "spam")

def grid(length):
    print("+" + "-"*length + "+" + "-"*length + "+")
    print("|" + " "*length + "|" + " "*length + "|")
    print("|" + " "*length + "|" + " "*length + "|")
    print("|" + " "*length + "|" + " "*length + "|")
    print("|" + " "*length + "|" + " "*length + "|")
    print("+" + "-"*length + "+" + "-"*length + "+")
    print("|" + " "*length + "|" + " "*length + "|")
    print("|" + " "*length + "|" + " "*length + "|")
    print("|" + " "*length + "|" + " "*length + "|")
    print("|" + " "*length + "|" + " "*length + "|")
    print("+" + "-"*length + "+" + "-"*length + "+")
 
# grid(3)


