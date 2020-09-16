#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:17:49 2020

@author: venky
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?



def product_ar(arr):
	new_arr = []
	for i in range(0,len(arr)):
		new_arr.append(multiply_all(arr[0:i], arr[i+1:len(arr)]) )	
	
	return new_arr

def multiply_all(arr1, arr2):
	product = 1
	for item in arr1:
		product *= item		
	for item in arr2:
		product *= item	

	return product

# Some tests 

print(product_ar([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])
print(product_ar([3,2,1]) == [2,3,6])


def productExceptSelf(nums):
        before = [1]*len(nums)
        after = [1]*len(nums)
        product = [0]*len(nums)

        for i in range(1, len(nums)):
            before[i] = before[i-1]*nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            after[i] = after[i+1]*nums[i+1]

        for i in range(0, len(nums)):
            product[i] = before[i]*after[i]

        return product

nums = [1,2,3,4]
print(productExceptSelf(nums))

"""


def productExceptSelf(nums):        
        #scan from left to i
        output = []
        n = len(nums)
        p = 1
        for i in range(n):
            output.append(p)
            p = p * nums[i]
            
        p = 1    
        #scan from right to i
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output

nums = [1, 2, 3, 4, 5]
print(productExceptSelf(nums))












