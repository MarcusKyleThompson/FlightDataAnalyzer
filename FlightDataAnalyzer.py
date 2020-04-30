# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:10:16 2020

@author: Marcus
"""


#FlightDataAnalyzer.py

data = open("flightdata.txt").read().splitlines()


dataTitles = data[0].split('<')

def titles():
    for x in dataTitles:
        if x != '':
           print(x)
           #pass

print(dataTitles[1])

titleDict = {}

for line in data:
    values = line.split()
    height = values[9]
