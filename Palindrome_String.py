# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#palindrome String
# length = len(s1)-1
# for x in range(len(s1)-1, -1, -1):

s1=input("enter a string")

s2=s1.replace(" ","").lower()

if s2==s2[::-1]:
    print("palindrome")
else:
    print("not palindrome")

