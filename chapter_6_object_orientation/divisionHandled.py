#!/usr/bin/env python

import sys

def main():
    print("Please input two numbers. The first will be divided by the second", '\n')
    afirst = input('1st number: ')
    asecond = input('2st number: ')
    first = float(afirst)
    second = float(asecond)
    try:
        quotient = first / second
        print('Quotient 1st/2st = ', quotient)
    except ZeroDivisionError as e:
        print(e, ': 2st number must be no zero. Please try again', '\n')
        main()

if __name__ == '__main__':
    main()
