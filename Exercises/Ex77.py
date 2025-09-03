try:
    n = int(input("Nhập số lượng phần tử: "))
    list = []
    for i in range(n):
        x = int(input())
        list.append(x)
    a = int(input())
    print(a, list[a])
except ValueError:
    print("Lỗi")
except IndexError:
    print("Lỗi")

    
