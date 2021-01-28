# Python Program to print the largest among three numbers,
# using the if...elif...else ladder to find the largest 
# among the three and display it.

# Taking input as list and then accesing in three integer variables.

numbers = input("Enter three numbers:(Add space to seperate numbers) ").split()

number_1 = int(numbers[0])

number_2 = int(numbers[1])

number_3 = int(numbers[2])

def Largest_Number(number_1, number_2, number_3):
    
    if((number_1 >= number_2) and (number_1 >= number_3)):
        return number_1
    
    elif((number_2 >= number_1) and (number_2 >= number_3)):
        return number_2
    
    else:
        return number_3

print("The Largest Number is: " + str(Largest_Number(number_1, number_2, number_3)))
