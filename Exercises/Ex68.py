while True:
    try:
        num = int(input())
        print(f"You entered: {num}")
        break
    except:
        print("Invalid!!! You must enter integer number")
        continue