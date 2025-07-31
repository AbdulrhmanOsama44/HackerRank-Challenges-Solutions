#!/bin/python3

import math
import os
import random
import re
import sys

def char_counter(word):
    
    word = sorted(word)
    frequency = {}
    
    for i in word:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    
    frequency_sorted = sorted(frequency.items(), key = lambda x: (-x[1], x[0]))
    for j, k in frequency_sorted[ : 3]:
        print(j, k)

if __name__ == '__main__':
    s = input()
    char_counter(s)