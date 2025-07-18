# 1. ვქმნით რიცხვების set-ს
numbers = {1, 2, 3, 4, 5}

# 2. ვბეჭდავთ მისი ძირითადი თვისებების მაგალითებს
print("➡️ საწყისი set:", numbers)

# თვისებები:
# - set არ ინახავს დუბლირებულ მნიშვნელობებს
# - ელემენტების განლაგება არ არის გარანტირებული (არ არის მოწესრიგებული)
# - set-ის თითოეული ელემენტი უნიკალურია
# - set შეიცავს ცვლად ტიპის ელემენტებს (მაგ. მთელი რიცხვები, სტრინგები, მაგრამ არა ცვლადი ტიპები, როგორიცაა სიები)

# 3. ვამატებთ 2 ახალ ელემენტს set-ში
numbers.add(6)
numbers.add(7)
print("➕ დამატებული ელემენტები (6 და 7):", numbers)

# 4. ვშლით 2 ელემენტს set-იდან
numbers.remove(1)
numbers.remove(3)
print("➖ წაშლილი ელემენტები (1 და 3):", numbers)

# 5. ვქმნით მეორე set-ს
more_numbers = {4, 5, 6, 8, 9}
print("➡️ მეორე set:", more_numbers)

# 6. ვასრულებთ სამ მოქმედებას ორ set-ს შორის

# UNION – აერთიანებს ორივე set-ის ყველა უნიკალურ ელემენტს
union_set = numbers.union(more_numbers)
print("🔗 Union (გაერთიანება):", union_set)

# INTERSECTION – პოულობს საერთო ელემენტებს
intersection_set = numbers.intersection(more_numbers)
print("🎯 Intersection (გადაკვეთა):", intersection_set)

# DIFFERENCE – აბრუნებს ელემენტებს, რომლებიც მხოლოდ პირველშია და არა მეორეში
difference_set = numbers.difference(more_numbers)
print("🧮 Difference (განსხვავება):", difference_set)
