import random
def guess_number():
    
    print("Đoán số đê!!!")
    while True:
        # Chọn độ khó cho game
        print("\nChọn độ khó: ")
        print("1. Dễ (1-50) trong 10 lượt đoán ")
        print("2. Vừa (1-75) trong 9 lượt đoán")
        print("3. Khó (1-100) trong 5 lượt đoán")
        mode = input("Nhặp 1,2 hoặc 3 để xác định độ khó: ")
        if mode == '1':
            max_attempt = 10
            max_secret = 50
        elif mode == '2':
            max_attempt = 9
            max_secret = 75
        elif mode == '3':
            max_attempt = 5
            max_secret = 100
        else: 
            print("Lựa chọn không hợp lệ")
            continue
        secret = random.randint(1,max_secret)
        attempt = 0
        while attempt <= max_attempt:
            try:
                guess = int(input(f"\nĐoán một số từ 1 đến {max_secret}: , Bạn có {max_attempt} lượt đoán: "))
            except ValueError:
                print("Bạn đã nhập số không hợp lệ !!!")
                continue
            attempt +=1
            if guess < secret:
                print("Quá thấp")
            elif guess > secret:
                print("Quá cao")
            else:
                print(f"Chính xác!!! Bạn đã đoán đúng sau {attempt} lần")
                break 
        else:
            print("Hết giờ!")
            print(f"Số cần đoán là {secret}")
        again = input("\nBạn có muốn chơi lại ko? (y/n): ").lower()
        if again != 'y':
            print("Cảm ơn đã chơi! Chúc bạn may mắn lần sau")
            break


guess_number()

