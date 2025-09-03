file_name = input()
try:
    with open(file_name, 'r') as f:
        content = f.read()
        print("Nội dung file: ")
        print(content)
except FileNotFoundError:
    print("file này ko tồn tại")



