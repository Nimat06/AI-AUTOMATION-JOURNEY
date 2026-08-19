
def calculator(num1, num2, operation):
    try:
        if operation == "+":
            return num1 + num2  
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            return num1 / num2
        else: 
            return "invalid operation"
        
    except ZeroDivisionError as E:
        return f"invalid operation: {E}"
    except TypeError as B:
        return f"invalid operation: {B}"


result = calculator(5, 0, "+")
print(result)

result = calculator(10, 0, "/")
print(result)

result = calculator(7, 0, "$")
print(result)
