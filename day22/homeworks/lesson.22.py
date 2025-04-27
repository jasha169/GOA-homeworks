
vegetables = ["კომბოსტო", "პომიდორი", "კარტოფილი", "ჩაშუშული ბარდა"]


undesired_vegetables = ["კომბოსტო", "ჩაშუშული ბარდა"]


new_vegetables = ["სტაფილო", "ყაბაყი"]


for i in range(len(vegetables)):
    if vegetables[i] in undesired_vegetables:
        vegetables[i] = new_vegetables.pop(0)


print(vegetables)













