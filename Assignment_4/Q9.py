#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 14:10:19 2025

@author: charan
"""

import pandas as pd

# Sample data
data = {
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance', 'IT'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'PerformanceScore': [85, 90, 85, 88, 90, 88, 85]
}

df = pd.DataFrame(data)

# Step 1: Find max performance score per department
max_scores = df.groupby('Department')['PerformanceScore'].transform('max')

# Step 2: Filter rows where PerformanceScore equals the max score in the department
top_performers = df[df['PerformanceScore'] == max_scores]

print(top_performers)