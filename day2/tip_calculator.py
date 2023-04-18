# -- day 2 -- #

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

def calculate_tip(total_bill, people_count, percent):
    each_bill = total_bill / people_count
    tip = each_bill * (percent / 100)

    return "{:.2f}".format(round((each_bill + tip), 2))

total_bill = float(input('What was the total bill? $'))
percent = int(input('What percentage tip would you linke to give? 10, 12 or 15? '))
people_count = int(input('How many people to split the bill? '))

result = calculate_tip(total_bill, people_count, percent)
print(f'Each people should pay: ${result}')
