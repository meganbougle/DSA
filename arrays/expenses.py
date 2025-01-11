# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

monthly_expenses = [2200, 2350, 2600, 2130, 2190]

#1
#When the index is =1 (February), we substract the amount spent in February from the amount spent in January
for i in range(len(monthly_expenses)):
    if i==1:
        dollars_spent = monthly_expenses[i]-monthly_expenses[0]
        print("In Feb $",dollars_spent,"was spent extra")

#Second approach for #1
print("In February the amount that was spent extra compared to January was ",monthly_expenses[1]-monthly_expenses[0])
#2 
fQuarter=0
for i in range(3):
   fQuarter+=monthly_expenses[i]

print ("The amount spent in the first Quarter is",fQuarter )

#Second approach for #2
print("The amount spent in the first Quarter of the year is", monthly_expenses[0]+monthly_expenses[1]+monthly_expenses[2])

#3
if 2000 in monthly_expenses:
    i= monthly_expenses.index(2000)
    print(f"Exactly 2000 was spent in month{i+1}")
else:
    print("Exactly 2000 was never spent in any month")

#4
monthly_expenses.append(1980)
print("June's total expenses was",monthly_expenses[5])

#5
april_refund = 200
monthly_expenses[3]=monthly_expenses[3]-april_refund
print("After the refund, April's total expenses is", monthly_expenses[3])