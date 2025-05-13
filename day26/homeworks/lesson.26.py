# მომხმარებლისგან მონაცემების მიღება
start = int(input("შეიყვანეთ საწყისი რიცხვი: "))
end = int(input("შეიყვანეთ საბოლოო რიცხვი: "))

# if-else პირობა – ვამოწმებთ შუალედს
if end < start:
    print("არასწორი შუალედი. მეორე რიცხვი უნდა იყოს მეტი ან ტოლი პირველზე.")
else:
    total = 0
    print("რიცხვები შუალედში:")
    
    for number in range(start, end + 1):
        print(number)
        total += number  # ჯამს ვამატებთ რიცხვს
    
    print("ჯამი:", total)
