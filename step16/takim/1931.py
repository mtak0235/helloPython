#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:32:08 2022

@author: takim
"""
import sys

finishTime = 0
result = 0
times =[]
timesDiff = []

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    times.append(tuple(map(int, sys.stdin.readline().rstrip().split())))
 
times.sort(key = lambda time: [time[1], time[0]])

for time in times:
    if time[0] >= finishTime:
        result+=1
        finishTime = time[1]
        
print(result)