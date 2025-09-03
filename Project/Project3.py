# Mini calculator
def calculator():
    math = input("Hãy nhập một biểu thức toán học: ")  
    try:
        math_result = eval(math)
        return math_result
    except:
        return "Lỗi! Bạn đã nhập sai cú pháp"





print(calculator())