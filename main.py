# 1. Reverse a string

# a. Write code that takes a string as input and returns the string reversed

# b. i.e. “Hello” will be returned as “olleH”

def reverse_str(string):
  return string[::-1]

print(reverse_str('Hello'))

# 2. Capitalize letter

# a. Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”

def cap_first_letter(string):   
  return string.capitalize()

print(cap_first_letter('hello world'))
  

# 3. Compress a string of characters

# a. For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a" "3a5b4c2a3c3b3a3b3a"

def compress_str(string):
  count = 0
  char_in_question =''
  new_string = ''
  for char in string:
    if char_in_question != '' and char_in_question != char:
      new_string += str(count) + char_in_question
      count = 0
    if char == char_in_question:
      count += 1
    else:
      char_in_question = char
      count = 1 
  new_string += str(count) + char_in_question     
  return new_string
     
print(compress_str('aaabbbbbccccaacccbbbaaabbbaaa'))     

# 4. BONUS CHALLENGE: Palindrome

# a. A word, phrase, or sequence that reads the same backward as forward i.e. madam

# b. Write code that takes a user input and checks to see if it is a Palindrome and reports the result

def is_palindrome(string):
  reversed_string = string[::-1]
  if reversed_string == string:
    return 'This is a Palindrome!'
  else:
    return 'This is not a Palindrome!'  

print(is_palindrome('madam'))
print(is_palindrome('bubble'))    


# 1. Happy Numbers a. https://en.wikipedia.org/wiki/Happy_number

# b. A happy number is a number defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1. An example of a happy number is 19

# c. Write a method that determines if a number is happy or sad

def is_happy_num(num):
  nums = str(num)
  newNum = 0
  for num in nums:
    num = int(num)**2
    newNum += num
  if newNum == 1:
    return 'This is a happy number!'
  elif newNum < 10 and newNum != 1:
    return 'This is not a happy number!'
  return is_happy_num(newNum) 

print(is_happy_num(19))

print(is_happy_num(4))

# 2. Prime Numbers

# a. A prime number is a number that is only divisible by one and itself.

# b. Write a method that prints out all prime numbers between 1 and 100

def prime_checker(num):
  is_prime = True
  if(num == 2):
    return is_prime
  else:
    for i in range(2, num):
      if(num % i == 0):
         is_prime = False
  return is_prime

def show_prime_nums_to_100():  
  
  for number in range(2,100):
    if prime_checker(number):
      print(number)

print(show_prime_nums_to_100())


# 3. Fibonacci

# a. A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.

# b. Write a method that does the Fibonacci sequence starting at 1


def is_fibonacci():
   my_list = [1,1]

   for i in range(2,14):
     new_val = my_list[i - 1] + my_list[i - 2]
     my_list.append(new_val)
   return my_list

print(is_fibonacci())

# c. HARDER VERSION: Write a method that does the Fibonacci sequence starting at a number that a user inputs

def is_fibonacci(starting_num):
   my_list = [starting_num,starting_num]

   for i in range(2,14):
     new_val = my_list[i - 1] + my_list[i - 2]
     my_list.append(new_val)
   return my_list

print(is_fibonacci(3))



# Steps of the software development process:
# 1. Based on a given starting point (feature, task, code block, etc.), what is the 
# expected end result?
# 2. What are the written-out steps to go from point A to point B? You need to 
# solve the problem before you begin coding it.
# 3. Implementation (coding it out, researching)
# 4. Test and debug code (run code with breakpoint, unit test, etc.)
# 5. Refactor if necessary. Test again. This continues until functionality is 
# solidified.
# The above steps should be rinse and repeated for every single problem you 
# encounter. Ignoring these steps or straying from them will result in the long way 
# around to solving a problem or even possibly never solving the problem. 
# To be a good problem solver, it is important to be able to break problems down. 
# One way to go about this is to write out the steps it will take to solve the problem. 
# These steps are written down in English in a manner that are easily explainable to 
# someone who may not be technical. The idea is that in order to code something out,
# you first need to have a good understanding of what it is you are attempting to 
# solve. For each of the problems below, write out the steps it will take to go about 
# solving the problem. Then code it out and test!
# You may jump around in these problems. If you get stuck on one problem, begin 
# working on another. If you get stuck on that new problem, go back to working on 
# the previous one. 
# The use cases below are just examples to give you a better idea of what might be 
# passed into the method or what might be outputted from the method. You shouldn’t
# be coding exactly to these examples, but rather, be flexible to handle any data of 
# that data type.
# Whiteboard Challenges
# 1. Given an array of integers, return indices of the two numbers such that they 
# add up to a specific target. You may assume that each input would 
# have exactly one solution, and you may not use the same element twice.
# a. Use Case:
# i. Given numbers in an array: [5, 17, 77, 50] 
# ii. Target: 55


def find_indices(list, target):
  # check each index of possible pairs to see if they add to target number
  for i in range(0,len(list)):
      for j in range(i,len(list)):
        if list[i] + list[j] == target:
          # expected end result is two numbers
          return [i,j]

print(find_indices([2,3,4,22,4,6], 28))


# 2. Given a number, return the reciprocal of the reverse of the original number, 
# as a double. 
# a. Use case: If given 17, return 0.01408 (1/71)

def recip_reverse(num):
  # make string
  num = str(num)
  # reverse string
  num = num[::-1]
  # reciprocal
  num = 1/int(num)
  # format 5 decimal places to right
  num = "{:.5f}".format(num)
  return num

print(recip_reverse(17))

# 3. A briefcase has a four-digit rolling-lock. Each digit is a number from 0-9 that 
# can be rolled either forwards or backwards. Write a method that returns the 
# smallest number of turns it takes to transform the lock from current 
# combination to the target combination. One turn is equivalent to rolling a 
# number forwards or backwards by one. 
# a. Use case: 
# i. Current lock: 3893
# ii. Target lock: 5296

def to_str(char):
  return str(char)

def how_many_turns(current_lock, target_lock):
  # parse to str for iteration
  current_lock = str(current_lock)
  target_lock = str(target_lock)
  # est count var to keep count of distance
  count = 0
  for i in range(0,len(current_lock)):
    # make sure to continue if same
    if current_lock[i] == target_lock[i]:
      continue
    num1 = int(current_lock[i])
    num2 = int(target_lock[i])
    # little math to compensate for index 0-9
    if num1 < num2:
      count += num2 - num1
    else:
      count += (num2 + 10) - num1 
  # return count
  return count 
print(how_many_turns(3893, 5296)) 


# 4. Given a list of integers, return a bool that represents whether or not all 
# integers in the list can form a sequence of incrementing integers
# a. Use case: 
# i. {5, 7, 3, 8, 6}  false (no 4 to complete the sequence)
# ii. {17, 15, 20, 19, 21, 16, 18}  true

def can_sort_by_increments(list_of_nums):
  list_of_nums.sort()
  for i in range(1,len(list_of_nums)):
    num1 = list_of_nums[i - 1]
    num2 = list_of_nums[i]
    if num2 != num1 + 1:
      return False
  return True

print(can_sort_by_increments([5, 7, 3, 8, 6]))


# 5. Create a method that takes an array of positive and negative numbers. 
# Return an array where the first element is the count of the positive numbers 
# and the second element is the sum of negative numbers. 
# a. Use case: [7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]


# 6. Create a method that accepts a string of space separated numbers and 
# returns the highest and lowest number as a string
# a. Use case: “3 9 0 1 4 8 10 2”  “0 10”
# 7. Create a method that accepts a string, check if it’s a valid email address and 
# returns either true or false depending on the valuation. Think about what is 
# necessary to have a valid email address.
# a. Use case:
# i. “mike1@gmail.com”  true
# ii. “gmail.com”  false
# 8. Create a method that takes in a string and replaces each letter with its 
# appropriate position in the alphabet and returns the string
# a. Use case:
# i. “abc”  “1 2 3”
# ii. “coding is fun”  “3 15 4 9 14 7 9 19 6 21 14”