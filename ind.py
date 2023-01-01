#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def Summa(*args):
    first = 0
    second = 0
    summa = 0
    if args:
        for i in args:
            if i > 0:
                first = args.index(i)
                break

        for i in args:
            if i > 0 and args.index(i) > first:
                second = args.index(i)
                break

        for i in args:
            if (args.index(i) > first) and (args.index(i) < second):
                summa += i
        return summa

    else:
        return None

if __name__ == "__main__":
    print(Summa())
    print(Summa(-2, -4, 2, -6, -1, -9, 1, 4, 9, -5))