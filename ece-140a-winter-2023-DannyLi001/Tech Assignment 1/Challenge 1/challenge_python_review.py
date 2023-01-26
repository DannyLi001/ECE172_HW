# -*- coding: utf-8 -*-

import math

'''
The print_squares function only calculate squares from 1 to 10. It initial a number array, 
then using a for loop to print out the square of each.
'''
def print_squares():
    nums = [1,2,3,4,5,6,7,8,9,10]
    for num in nums:
        print(num*num)
        
'''
This fuction is used to calculate the average of a list of numbers.
I iterate the list to check whether all elements are numbers. If not, I will return None
Then I rule out exception of when the array has no element.
In the last case which an array uses extend function. It wont work because the arguement for 
the average function is not a list.
'''
def average(nums):
    sum = 0    
    if not isinstance(nums, list):
        return None
    for num in nums:
        if not isinstance(num,int) and not isinstance(num,float):
            return None
        sum += num
    if len(nums) == 0:
        return 0
    return sum/len(nums)
    
'''
To determine whether a number is prime or not, we only need to check if it can be
whole divided by any number lower than itself. If there's any number can divide it with
0 remainder, then it is not a prime number.
'''
def is_prime(num):
    for i in range(2,num):
        if(num%i) == 0:
            return False
    return True

def prime_100():
    count = 0
    num = 2
    prime_list = []
    while count < 100:
        if is_prime(num) == True:
            prime_list.append(num)
            count += 1
            num += 1
            continue
        num += 1
    return prime_list


'''
I first change all capital to lowercase to avoid counting them differently. Then I iterate letter by letter
and skip when the "letter" is space. When forming dictionary, I check if the dict has already contained the letter.
If yes, then I add one to the letter. If no, I add a new pair into the dict and assign it as 1.
'''
def count_letters(sentence):
    sentence = sentence.lower()
    letterDict = {}
    for letter in sentence:
        if letter.isalpha() == False:
            continue
        if letterDict.get(letter, 0) == 0:
            letterDict[letter] = 1
        else:
            letterDict[letter] += 1;
    return letterDict


'''
Iterating through the list to get each string, then check if the string
has more than 5 letters. If yes, check if it contains vowel.
'''
def filter_strings(strings_list):
    vowel = ['a','e','i','o','u']
    new_list = []
    for string in strings_list:
        if len(string) < 5:
            continue
        for letter in string:
            if letter in vowel:
                new_list.append(string)
                break
    return new_list
            

'''
I first filtered out negative numbers which cannot be palindrome. Then I change 
int to string which makes the task easier. I create a new string which is the 
inverse version of input. By comparing these two data, I can identify whether the
input is a palidrome or not.
'''
def is_palindrome(num):
    if num < 0:
        return "False"
    rev=str(num)[::-1]
    if type(num) == int and num==int(rev) or type(num) == float and num==float(rev):
        return True
    else:
        return False


if __name__ == '__main__':
   print_squares()
    
   print(average([3,4,5,6]))
   print(average([-2.3,45,0.111,11/6]))
   print(average([])) # Returns 0
   print(average([1.0,1.0,-math.inf]))
   print(average([1, 3.14, "h"]))
   print(average("hello?"))
   print(average([1,2,3,4].extend([5]))) # what happens here?
   
   print(prime_100())
   
   print(count_letters("The quick brown fox jumps over the lazy dog."))
   print(count_letters("Web serving with FastAPI!"))

   print(filter_strings(['abcdef','bdbdbdb','abc','aaeeiioo']))
   
   print(is_palindrome(1234567.7654321))
   print(is_palindrome(-0.123))
   