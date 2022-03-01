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
