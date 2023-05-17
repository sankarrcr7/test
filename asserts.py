# assert condition, error_message


x = 9

if x <= 10:
    print("x is not greater than 10")
    assert x > 10, "x should be greater than 10"

print("Assertion passed")


def divide (a,b):
    assert b!=0,"cannot divide by zero"
    result=a/b
    assert result >=0, "result must non-negative"
    return result

result=divide (20,-20)  #"""result must non-negative"""
result=divide(20,0)   #"cannot divide by zero"
result=divide(10,200)
print(result)


