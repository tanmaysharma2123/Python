# Python Program to check if a year is leap year or not!

year = int(input("Enter you year: "))

def LeapYear(year):
    
    # Leap year is a year exactly divisible by 4 except for century years..!
    if(year%4==0):
        
        # The century year is a leap year only if it is perfectly divisible by 100 and 400 also!
        if(year%100==0 and year%400==0):
            result = str(year) + " is a Leap Year!"
        else:
            result = str(year) + " is not a Leap Year!"
    else:
        result = str(year) + " is not a Leap Year!"
    
    return result

print(LeapYear(year))
