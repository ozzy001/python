#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator!")
bill = float(input("Enter the bill amount. $"))
tip = float(input("Enter the tip amount: "))
bill_with_tip = tip / 100 * bill + bill
number_of_people = int(input("Enter the number of people in your group: "))
final_amount = round(bill_with_tip / number_of_people, 2)

print(f"Each person should pay: ${final_amount :0.2f}")

# can also be done using the following:
# final_amount = "{:0.2f}".format(round(bill_with_tip / number_of_people, 2))