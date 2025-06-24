#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 14:10:57 2025

@author: charan
"""

import pandas as pd

# Sample data
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'JoiningDate': ['2010-05-10', '2012-09-15', '2008-03-20', '2015-07-01', '2007-11-25']
}

df = pd.DataFrame(data)

# Convert JoiningDate to datetime
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])

# Sort by JoiningDate ascending (oldest date first = longest tenure)
df_sorted = df.sort_values(by='JoiningDate')

# Select top 3 employees with longest tenure
top_3_tenure = df_sorted.head(3)

print(top_3_tenure)