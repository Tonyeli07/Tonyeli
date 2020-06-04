#1. Make a Shopping List for 5 items that you need at tht grocery stor. Remember to use quotation marks.
#Use the print() so that each of the items of the grocery list displays
print('bread')
print('sugar')
print('salt')
print(tomatoes')
print('salmon')

#2. The groceries ring up as 9.42, 5.57, 3.25, 13.40, and 7.50 respectively. Use python as a handy calculator to add these values. 
9.42 + 5.57 + 3.25 + 13.40 + 7.50

#3. You decide to buy 5 more of the last item. Recalculate your total
9.42 + 5.57 + 3.25 + 13.40 + (7.50 * 5)

#4 Figure out how to get the output of exercise one with only one print statement. If you can, do it with one line of code.
print('bread', 'sugar', 'salt', 'tomatoes', 'salmon')

#5 Write an all_the_snacks function that takes a snack (string) and uses * to print it 100 times. 
Then test your function by using all the items on your shopping list. See what happens when you enter a number into your function. Is the result what you expected?
def all_the_snacks(snack):
    print(snack * 100)

all_the_snacks('bread')
all_the_snacks('sugar')
...

#6 Notice that your all_the_snacks function prints out the results all squished together. Rewrite the all_the_snacks function to take an additional argument spacer.
Use the + sign to combine the spacer and the snack before multiplying. Test your function with different inputs. Use a string for both snacks and the spacer and see what happens.
Both numbers. A string and an integer. Is the result what you expected? 
def all_the_snacks(snack, spacer):
    print((snack + spacer) * 100)

all_the_snacks('bread', '_') 
all_the_snacks('sugar', ',')

#7.Rewrite the all_the_snacks such that it takes a num variable allowing you to customize the number of times that you can print out the snacks.
def all_the_snacks(snack, spacer, num):
    print((snack + spacer) * num)

all_the_snacks('bread', ',', 45)
all_the_snacks('sugar', '_', 95)

#8 Write a grocery_list function which takes an item and returns true or false if the item is on your grocery list.
def grocery_list(item)
    g_list = ('bread', 'rice', 'tomatoes', 'sugar', 'salmon')
    if item in g_list:
        return True
    else:
        return False

#9 Write a price_matcher function that takes no argument but prints a random grocery item and a price from your lsit everytime its run. 
 import random

 def price_matcher():
     grocery_list = ('bread', 'rice', 'tomatoes', 'sugar', 'salmon')
     prices = (9.42, 5.57, 3.25, 13.40, 7.50) 
     print(random.choice(grocery_list) + " ", random.choice(prices))

#10. Rewrite the all_the_snacks function so that the num and spacer have defaults of '100' and ',', using your favorite snack  as input try running your function
 with no additional input.
 def all_the_snacks, spacer-',', num-100):
    print((snack + spacer) * num)

all_the_snacks('brownie')

#11. Try running the all_the_snacks function with your favorite snack and with the spacer '!' and no additional input. How would run it while inputing your favorite snack and 42
as the num while keeping the dfault spacer? Can you use this method to enter spacer and num in reverse order.
all_the_snacks('brownie', spacer-'!')
all_the_snacks('brownie', num-42)
all_the_snacks('brownie', num-36, spacer-'_')

#12. Write an april_swapper function that takes an input to get your favorite color, saved as my_color and neighbors_color. Use a print statement to declare what your swapping
your neighbors favorite colors are. Now add a line that prints the same values but swapping your favorite color for your neighbors. 
def april_fool_swapper ():
    my_color = input("Green:")
    neighbors_color = input("Black:")
    print("Black" + my_color)
    print("Green") + neighbors_color)
    print("Black" + neighbors_color)
    print("Green" + my_color) 
