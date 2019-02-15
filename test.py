#"""Check if a number is even or odd"""
#N = int(input('Enter a number !'))
#if N % 2 > 0:
#    print("Weird")
#else:
#    if N >= 2 and N <= 5:
#        print("Not Weird")
#    elif N >= 6 and N <= 20:
#        print("Weird")
#    elif N > 20:
#        print("Not Weird")



#def is_leap(year):
#    leap = False
#    if (year % 4) == 0:
#        if (year % 100) == 0:
#            if (year % 400) == 0:
#                leap = True
#            else:
#                leap = False
#        else:
#            leap = True
#    else:
#        leap = False
#    return leap
#
#year = int(input('Enter a year :'))
#print(is_leap(year))

n = int(input('Enter a number: '))
for i in range(n):
    while i < n:
        print(i)
