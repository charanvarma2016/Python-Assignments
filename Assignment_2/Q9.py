# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 15:32:07 2025

@author: saikr
"""
"""9.Number to Words (1–99)
Write a function num_to_words(n) that converts numbers from 1 to 99 into words.
Example: num_to_words(42) → forty two"""


def num_to_words(n):
    if n < 1 or n > 99:
        return "Number out of range (1–99 only)"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    if 1 <= n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    else:
        ten = n // 10
        one = n % 10
        return tens[ten] + (" " + ones[one] if one != 0 else "")


print(num_to_words(99))


