
# First program for my cs class
# Created on 9/15/2025
# Purpose: to learn
# Editor: Jason

# def main():
#     position = int((input("enter a position ")))
#     numofcars = int((input("enter number of cars ")))
#     total = int((input("enter the amount one car holds ")))

#     if position <= numofcars * total:
#         print("You can ride on aaron the big backy ride")
#     else:
#          print("You cannot ride on aaron the big backy ride")

# main()



# def main():
#     numofdonuts = int((input("enter number of donuts ")))
#     numevents = int((input("enter the number of events ")))
#     current_event = 1
#     while current_event <= numevents and numofdonuts > 0:
#         event_type = input("+ or -?: ")
#         donut_amount = int((input("enter the amount of donuts ")))
#         if event_type == "+":
#             numofdonuts += donut_amount
           
#         elif event_type == "-":
#             numofdonuts -= donut_amount
#         else :
#             print("invalid input")
#             break

# print(f"At the end of our events, you have {numofdonuts} donuts left")

    #     elif event_type != "+" or "-":
    #         print("invalid input")
    #         break
              
        
    # print("you have", numofdonuts, "donuts left")

# def main():
#     factor_count = 0
#     num = int(input("Enter a number: "))
#     print(f"Factors of {num} are:")
#     for i in range(1, num+1):
#         if num % i == 0:
#             factor_count += 1
#             print(i)
#     print(f"{num} has {factor_count} factors.")
#     if factor_count == 2:
#         print(f"{num} is a prime number.")
#     else:
#         print(f"{num} is not a prime number.")

# main()
import math
start = 1
num = int(input("Enter a number:"))

new_stop = int(math.sqrt(num)) + 1

factor_count = 0
while start < new_stop
    if num % start == 0:
        divident = num // start
        if star != divident:
            factor_count += 2
        else:
            factor_count += 1
    start += 1

print(f"{num} has {factor_count} factors.")