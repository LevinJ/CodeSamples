squares = [1, 4, 9, 16, 25]

# indexing returns the item
# print(squares[1])
# print(squares[-1])
# print(squares[-3])
# 
# # slicing returns a new list
# print(squares[0:2])
# print(squares[-3:-1])
# print squares[:]
# 
# print(squares + [36, 49, 64, 81, 100])


# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# letters[2:5] = ['C', 'D', 'E']
# print(letters)
# print(len(letters))
# a = ['a', 'b', 'c']
# n = [1, 2]
# x = []
# x.append(a)
# x.append(n)
# x.append(n)
# print(x)

a, b = 0, 1
while b < 10:
#   A trailing comma avoids the newline after the output:  
    print'a=', a,
    print 'b=',b
    a, b = b, a+b