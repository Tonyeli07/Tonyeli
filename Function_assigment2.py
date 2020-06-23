
1. Write a function is isDivisibleBy7() to check if a number is divisble by 7
def is_Divisible_By_7(num): 
    if num % 7 == 0: 
        return True 
    else: 
        return False
    
2. Write a function isDivisibleby(num, divisor) to check to check if num is evenly divisble by divisor
def is_Divisible_By(num, divisor): 
    if num % divisor == 0: 
         return True 
    else: 
        return False                                                                                           
is_Divisible_By(7, 16)                                                                    
 False
is_Divisible_By(7, 14)                                                                    
 False
is_Divisible_By(7, 7)
True 

3. Make a function shout(word) that accepts a string and returns the string in Capital letters with an exclamation mark
    def shout(string)
        print(string.upper() + '!')
    shout("shout")
SHOUT!

4. Write a function introduce() which will ask a user for their name and shout it back to them
def introduce(): 
    name = input('please put your name here:') 
    print(name.upper())                                                                                      

def introduce()                                                                          
please put your name here: Tonyeli
 TONYELI

5. Write a function snack_check() that takes a string snack and prints True or False depending on whether the snack is your favorite snack or not.
def snack_check(): 
     favorite_snack = input("Enter snack name:") 
     if favorite_snack == 'brownie': 
         return True 
     else: 
         return False 

6. Write a snack_check() function that takes a string snack and prints an appropriate responds depending on whether the input is your favorite snack or not.
    def snack_check(snack): 
     favorite_snack = "brownie" 
     if snack == favorite_snack: 
         print ("you right") 
     else: 
         print ("try again next time")
     
     snack_check("meat pie")                                                                                             
try again next time

In [11]: snack_check("brownie")                                                                                              
you right   

        
7. Write a function in_grocery_list() to test if an item grocery_item is a string. Print a message warning if it's not
    def grocery_list(grocery_item): 
    strings = (" grocery_item", "sugar", "plantainchips") 
    if grocery_item == strings: 
        print ("That is great") 
    else: 
        print("Not a string")                                                                                                                      

grocery_list("sugar")                                                                                               
Not a string

grocery_list("grocery_list")                                                                                        
Not a string

grocery_list("grocery_item")                                                                                        
Not a string

grocery_list("plantainchips")                                                                                       
Not a string

8. Write a function you_won() that randonly picks a number from your price list 9.42, 5.57, 3.25, 13.40, and 7.50 and prints True or False depending on whether the random number is greater than 10.
def you_won(some_list, 'random num'):
 import random 

help(random.choice)                                                                                                 

In [15]: def you_won(): 
 price_list = [9.42, 5.57, 3.25, 13.40, 7.50] 
if random.choice(price_list) >=10: 
    return True 
else: 
    return False 

you_won()                                                                                                           
Out[17]: True

 you_won()                                                                                                           
 False

9. Write a function that imports datetime and uses it to determine current time The function should print an appropriate message based on the time. 
for example if the time is between 0900 and 1300 H: print "Morning Lecture Time"

def function(datetime, current time, import):

def morning_lecture time
    print(message, time)

def return_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    now_time = now.time()
    if now_time >= time(7, 00) or now_time <= time(11, 59):
        print(current_time, ': Morning Class')
    elif now_time >= time(12, 00) or now_time <= time(22, 00):
        print(current_time, ": Evening Class")
    else:
        print(current_time, ": Why are you are you still in school?!")


10. Write a function called volume which computes and returns the volume of a box when given the width, length and height.
def volume():
    box_size = input('width', 'length','height')
    vol = box_size



    
