def right_justify(s):
    print('                                                     ' + 'monty')


def do_twice(f, g):
    f
    g
def print_spam():
    print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(r, t):
    r
    t
    
do_four(do_twice(print_spam(), print_spam()), do_twice(print_spam(), print_spam()))

do_twice(print_spam, print_spam)

do_twice(print_twice('spam'), print_twice('spam'))

def draw_diagram():
    print('+', '- '*4 + '+', '- '*4 + '+' )
    print('|', ' '*8 + '|', ' '*8 + '|')
    print('|', ' '*8 + '|', ' '*8 + '|')
    print('|', ' '*8 + '|', ' '*8 + '|')
    print('|', ' '*8 + '|', ' '*8 + '|')
    print('+', '- '*4 + '+', '- '*4 + '+' )
    print('|', ' '*8 + '|', ' '*8 + '|')
    print('|', ' '*8 + '|', ' '*8 + '|')
    print('|', ' '*8 + '|', ' '*8 + '|')
    print('|', ' '*8 + '|', ' '*8 + '|')
    print('+', '- '*4 + '+', '- '*4 + '+' )
draw_diagram()
