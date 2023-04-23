
# # # Write a function that takes a list of numbers as input and
# # #  returns the product of all the numbers in the list.
def numbers(*numberss):
    product=1
    for y in numberss:
        product *=y
    return product

    
        
       # Write a function that takes a list of strings as input and returns a 
       # new list that contains only the strings with more than 5 characters.

def string(*stringss):
        answer=[]
        for l in stringss:
            if len(l)>5:
                answer.append(l)
        return answer


 # Write a function that takes a string as input 
 # and returns true if the string is a palindrome, false otherwise.

def name(mercy):
    if len(mercy)<1:

        return true

        if mercy[0]==mercy[-1]:

    return name(mercy[1:-1])

    else:
    return false

# #  # Write a function that takes a list of numbers as input and returns a new list that 
# # #  contains the square of each number in the input list.


def square(number):
    squares=1
    
    for i in numbers:
        square*2=num

       return squares

  


# Write a function that takes a number as input and returns
#  true if the number is a prime number, false otherwise.
def number(n):
  if n%2==0:
    return False
  else:
      return True




# Write a function that takes a list of strings as 
# input and returns the string with the most characters.
def str(*string):
    longest=""
    for i in string:
        if len(i)>len(longest):
            longest=i
        return longest




    

            
           
        
      