#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 14:08:36 2025

@author: charan
"""

import pandas as pd

# Sample data
data = {
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance', 'IT'],
    'Salary': [50000, 60000, 52000, 58000, 61000, 57000, 62000]
}

df = pd.DataFrame(data)

# Group by Department and calculate average salary
avg_salary = df.groupby('Department')['Salary'].mean()

# Sort descending
avg_salary_sorted = avg_salary.sort_values(ascending=False)

print(avg_salary_sorted)