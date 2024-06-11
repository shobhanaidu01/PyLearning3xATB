#1. Explain the difference between the = operator and the == operator in Python.

# In Python, the = operator and the == operator are used for different purposes.

# "="  is Assignment Operator :

# The "=" operator is used for assigning the value on the right-hand side of the operator to the variable on the left-hand side.
#For example:

a = 10
#Here, a is assigned the value 10.

# "==" is Equality Operator :

# The "==" operator is used to check for equality between two operands. It returns True if the values on both sides are equal, otherwise, it returns False.
#For example:

a = 5
b = 5
print(a == b) #Here result is True.

#Here, a and b have the same value, so the expression a == b evaluates to True.

x = 10
y = 12
print(x == y) #Here result is False.


# 2. What does the ** operator do in Python, and how is it used?

# Im Python, the ** operator is used for exponentiation,
# meaning it raises the left operand to the power of the right operand.

# Syntax:

# result = base ** exponent

# Where:
# base is the base number.
# exponent is the power to which the base is raised.

# For example:

result = 2 ** 3
print(result)  # Output: 8

result1 = 6 ** 2
print(result1)  # Output: 36


# 3. What does the ^ operator do in Python, and in what context is it commonly used?

# In Python, the ^ operator is the bitwise XOR operator.
# It performs a bitwise XOR operation on the binary representations of two integers.

# Here's how it works:
#result = operand1 ^ operand2

#Where operand1 and operand2 are integers.

#The bitwise XOR operation returns a 1 in each bit position for which the corresponding bits of either but not both operands are 1s.
# Otherwise, it returns 0.

#For example:
result = 5 ^ 3
print(result)  # Output: 6

#In this example, 5 in binary is 101, and 3 in binary is 011. Performing the XOR operation:
 # 101
# ^ 011
#-----
#  110

#So, the result is 110 in binary, which is 6 in decimal.

#The ^ operator is commonly used in scenarios involving bitwise manipulation, cryptography, and sometimes in algorithms where bitwise operations are required for performance optimization or specific data manipulation.

#It's worth noting that if you want to raise a number to a power in Python, you should use the ** operator, not the ^ operator, as ^ is reserved for bitwise XOR.