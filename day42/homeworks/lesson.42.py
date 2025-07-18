# ვქმნით ცარიელ set-ს სახელად numbers
numbers = set()

# ვამატებთ ორ ელემენტს set-ში add() მეთოდით
numbers.add(4)
numbers.add(7)

# ვშლით ორ ელემენტს set-იდან remove() მეთოდით
# თუ ელემენტი არ არსებობს, remove() გამოიტანს შეცდომას
numbers.remove(4)
numbers.remove(7)

# ვქმნით მეორე set-ს სახელად even_numbers
even_numbers = {2, 4, 6, 8}

# დავამატოთ თავიდან ელემენტები პირველ set-ში, რადგან წაშალეთ ისინი
numbers.add(2)
numbers.add(6)

# union() — აერთიანებს ორივე set-ის ყველა უნიკალურ ელემენტს
union_set = numbers.union(even_numbers)
print("Union:", union_set)

# intersection() — პოულობს ორივე set-ში საერთო ელემენტებს
intersection_set = numbers.intersection(even_numbers)
print("Intersection:", intersection_set)

# difference() — აბრუნებს იმ ელემენტებს, რომლებიც არიან პირველ set-ში, მაგრამ არა მეორეში
difference_set = numbers.difference(even_numbers)
print("Difference:", difference_set)
