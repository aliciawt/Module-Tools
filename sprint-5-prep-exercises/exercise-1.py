def half(value):
    return value / 2 

def double(value):
    return value * 2 

def second(value):
    return value[1]

# Predict what double("22") will do.
# Answer: it will return an error since "22" is a string and cannot be multiplied by 2.
# Then run the code and check. Did it do what you expected? Why did it return the value it did?
# Answer: no, it did not return an error. It returned '2222' because in Python,
# multiplying a string by an integer repeats the string that many times.
# String support the * operator and translates it into repetition in Python.