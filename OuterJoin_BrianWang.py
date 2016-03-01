"""
@author: Brian Wang's Answer
"""

import csv

def load_csv(fname):
    with open(fname, mode='r') as infile:
        reader = csv.reader(infile)
        next(reader)
        mydict = dict()
        for row in reader:
            if row[0] not in mydict:
                mydict[row[0]] = [ row[1] ]
            else:
                mydict[row[0]] = mydict[row[0]] + [ row[1] ]
        return mydict

math = load_csv('math.csv')
verb = load_csv('verb.csv')

Outer = []
for key in math.keys():
    for mv in math[key]:
        if key in verb:
            for vv in verb[key]:
                Outer.append([key, mv, vv])
        else:
            Outer.append([key, mv, None])
for key in verb.keys():
    if key not in math:
        for vv in verb[key]:
            Outer.append([key, None, vv])

print Outer
