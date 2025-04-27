
cold_drinks = ["ქარვა", "კოკა-კოლა", "პეპსი", "ჯუსი", "ტონიკი"]
new_drink = input("დამატეთ ახალი ცივი სასმელი თქვენს მაცივარში: ")


cold_drinks.append(new_drink)


print("თქვენი სასმელების სია: ", cold_drinks)
drink_choice = int(input(f"აირჩიეთ სასმელი (0 - {len(cold_drinks)-1}): "))


chosen_drink = cold_drinks[drink_choice]
print(f"თქვენი არჩევანი: {chosen_drink}")


name = "გიორგი"


print("თქვენი სახელი - სამი სიმბოლო:", name[:3])
