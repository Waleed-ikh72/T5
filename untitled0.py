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

opt1 = df.groupby("Student").mean()
opt1


