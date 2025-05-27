countries = ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]

# ყველა ელემენტი გადაიყვანეთ პატარა ასოებად და დაბეჭდეთ
for country in countries:
    print(country.lower())





countries = ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]

# ყველა ელემენტი გადავიყვანოთ დიდი ასოებად და დავბეჭდოთ
for country in countries:
    print(country.upper())




countries = ["georgia", "aRMENIA", "greeCE"]

for country in countries:
    fixed_country = country.lower().capitalize()
    print(fixed_country)





text = "I visited Georgia, Armenia and Greece"

position = text.find("Armenia")
print("Armenia-ს პოზიციაა:", position)
