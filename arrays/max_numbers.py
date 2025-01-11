# Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function

odd_numbers=[]

max_numbers=0
print("Enter the max number for your list")
max_numbers=int(input(max_numbers))
print(max_numbers)

for i in range(1 and max_numbers):
    if(i%2==1):
        odd_numbers.append(i)

print("Your list of odd numbers is ", odd_numbers)