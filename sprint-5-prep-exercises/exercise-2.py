def double(number):
    return number * 3

print(double(10))

# Read the above code and write down what the bug is.
# The bug is the function name, double implies multiplying by 2
# but instead, this function multiplies the number by 3.
# How would you fix it?
# Change "return number * 3" to "return number * 2"