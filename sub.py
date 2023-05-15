def subtract(*args):
    if len(args) == 0:
        raise ValueError("At least one argument is required.")
    result = args[0]
    for num in args[1:]:
        result -= num
    return result
print(subtract(3,4))