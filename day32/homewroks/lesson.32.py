print("Hello, world!")



name = input("შეიყვანე სახელი: ")
print(f"Hello, {name}!")



a = int(input("შეიყვანე პირველი რიცხვი: "))
b = int(input("შეიყვანე მეორე რიცხვი: "))
print("ჯამი:", a + b)


num = int(input("შეიყვანე რიცხვი: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")





age = int(input("შეიყვანე ასაკი: "))
if age < 18:
    print("არასრულწლოვანი")
else:
    print("სრულწლოვანი")





grade = int(input("შეიყვანე ქულა: "))
if grade >= 90:
    print("შესანიშნავი")
elif grade >= 75:
    print("კარგი")
elif grade >= 60:
    print("დამაკმაყოფილებელი")
else:
    print("დაუკმაყოფილებელი")






num = float(input("შეიყვანე რიცხვი: "))
print("შედეგი:", num / 2)




age = int(input("შეიყვანე ასაკი: "))
if age >= 18:
    print("სტუდენტი სრულწლოვანია")
else:
    print("სტუდენტი არასრულწლოვანია")




a = int(input("შეიყვანე პირველი რიცხვი: "))
b = int(input("შეიყვანე მეორე რიცხვი: "))
print("უმცირესი:", min(a, b))







value = input("შეიყვანე True ან False: ")

if value == "True":
    print(True)
else:
    print(False)
