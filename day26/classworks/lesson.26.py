
full_name = "Gio Jashashvili"


result = ""


for i in range(len(full_name)):
    char = full_name[i]

    
    if char == "G" or char == "J":
        count = 0  

       
        for j in range(i + 1, len(full_name)):
            if full_name[j].isupper():
                result += full_name[j].lower()
                count += 1

            if count == 3:  
                break


print("Result:", result)
