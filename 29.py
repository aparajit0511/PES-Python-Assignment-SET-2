str = "lets test the function";
print("str.capitalize() : ", str.capitalize())

str = "lets Test the function";
print(str.islower())

str = "LETs TEST THE FUNCTIOn";
print(str.isupper())

str = "LETS TEST THE FUNCTION";
print(str.lower())

str = "lets test the function";
print(str.upper())

str = "LETS test THE function";
print(str.swapcase())

str2="Hello"
print(len(str2))

str = "Lets test the function";
print(str.split())
print(str.split('the'))

str = "Lets test the function and the test should be good";
print(str.replace('test','changed'))

str = "Lets test the function and the test should be good";
sub="t"
print("Number of  t are",str.count(sub, 1, 20))

str = "             Lets test the function and the test should be good";
str1 = "000000000Lets test the function and the test should be good000000";
print(str.lstrip(' '))
print(str1.lstrip(‘0’))


str = "Lets test the function and the test should be good               ";
str1 = "000000000Lets test the function and the test should be good000000";
print(str.rstrip(' '))
print(str1.rstrip(‘0’))

str = "  Lets test the function and the test should be good";
print(str.rfind('test', 0, 20))

str = "  1231231Lets test the function";
print(str.isdigit())

str="-"
seq=("This","string","will","be","joined")
print(str.join(seq))