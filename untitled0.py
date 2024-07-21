#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:31:33 2024

@author: Al-Ikhwan
"""


import pandas as pd

df = pd.DataFrame({'Student' : ['A', 'A', 'A', 'B', 'B', 'C'],
                   'Score' : [15., 23., 17., 5., 8., 12.]})
print(df, end='\n\n')

#group = df.groupby(['Studnet'], as_index=False)
opt1 = df.mean("Student",axis=1)
opt2 = df.groupby("Student").mean()
opt3 = df.mean("Score",axis=0)
opt3 = df.mean("Student",axis=0)


print(group.mean())