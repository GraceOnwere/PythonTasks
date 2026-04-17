
a = 5
b = 10
#wrong expression a = b b = a

#right expression

'''c = a
a = b
b = c

print(a,b)
'''
#The solution is using a temporary variable to store one of the values, making the other variable empty to store the next value

a,b = b,a
print(a,b)
