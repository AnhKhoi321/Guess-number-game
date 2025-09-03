try:
    a = input()
    result = eval(a)
    print(result)
except SyntaxError:
    print("Sai cú pháp")
except ZeroDivisionError:
    print("Ko thể chia cho 0")
except Exception as e:
    print(f"Lỗi ko xác định: {e}")
