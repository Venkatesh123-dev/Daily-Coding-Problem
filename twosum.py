#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:45:06 2020

@author: venky

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""


def two_numbers(nums,target):
    output = set()
    for num in nums:
        temp = target - num
        if temp in output:
            return True
        output.add(num)
    return False    


nums = [10, 15, 3, 7] 
target = 13
print(two_numbers(nums,target))