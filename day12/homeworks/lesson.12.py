# ცვლადი 1: შეამოწმებს, არის თუ არა ტემპერატურა 30-ზე მეტი და არ არის ხანმოკლე ღრუბლები
temperature = 32
cloudy = False
result1 = temperature > 30 and not cloudy
print("result1:", result1)  # True, რადგან ტემპერატურა 30-ზე მეტი და არ არის ღრუბლები

# ცვლადი 2: შეამოწმებს, არის თუ არა ასაკი 18 ან მეტი და მოქალაქე
age = 25
citizen = True
result2 = age >= 18 and citizen
print("result2:", result2)  # True, რადგან ასაკი 18-ზე მეტია და მოქალაქეა

# ცვლადი 3: შეამოწმებს, არის თუ არა ტემპერატურა უფრო ნაკლები 0°C ან მეტი 40°C
result3 = temperature < 0 or temperature > 40
print("result3:", result3)  # False, რადგან ტემპერატურა არც 0-ზე ნაკლებია და არც 40-ზე მეტი

# ცვლადი 4: შეამოწმებს, არის თუ არა არდადეგები და ცხელა
vacation = True
hot_weather = True
result4 = vacation or hot_weather
print("result4:", result4)  # True, რადგან არდადეგები ან ცხელა

# ცვლადი 5: შეამოწმებს, არის თუ არა პირი ასაკში 18-დან 65 წლამდე და მუშაობს თუ არა
working = True
age = 45
result5 = 18 <= age <= 65 and working
print("result5:", result5)  # True, რადგან ასაკი 18-65 და მუშაობს
