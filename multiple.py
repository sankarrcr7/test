def multiply(*args):
    if len(args) == 0:
        raise ValueError("At least one argument is required.")
    result = 1
    for num in args:
        result *= num
    return result
print(multiply(1,3))