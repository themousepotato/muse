#!/usr/bin/python3

import subprocess as s, random, ast

def main():
    with open('/usr/share/muse/quotes.txt', 'r') as f:
        data = f.read().split('\n')
        f.close()

    quote, author = ast.literal_eval(data[random.randint(0,len(data))])

    s.call(['notify-send', quote, author]) # Show quote as notification

if __name__ == '__main__':
    main()
