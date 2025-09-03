try:
    a = int(input())
    b = int(input())
    result = a / b 
    print(result)
except ZeroDivisionError:
    print("Lỗi! ko thể chia cho 0")
except ValueError:
    print("Sai kiểu dữ liệu")


