# source : https://www.programiz.com/python-programming/generator
# Initialize the list
my_list = ['1', '3', '6', '10']

# square each term using list comprehension
# Output: [1, 9, 36, 100]
a = [str(x) for x in my_list]
r1 = ",".join(a)
print (r1)

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
a = (str(x) for x in my_list)
r2 = ",".join(a)
print (r2)
