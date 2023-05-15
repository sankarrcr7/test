def divide(*args):
    if len(args) == 0:
        raise ValueError("At least one argument is required.")
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ValueError("Cannot divide by zero.")
        result /= num
    return result
print (int (divide(2000,200)))