#def generator(x):
#    for i in range(x):
#        yield i ** 2
#
#number = int(input("Enter the number: "))
#print(generator(number))



#def check(s1, s2):
#    return [x for x in s1 if x not in s2]
#
#
#s1 = 'SPAM'
#s2 = 'SCAM'
#print(check(s1, s2))


def ups(line):
    for sub in line.split(','):
        yield sub.upper()

data = {i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))}
print(data)


