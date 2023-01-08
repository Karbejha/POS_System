drinks_list = {"water":1 , "milk":5}
drinks_names = list(drinks_list.keys())
drinks = input(f"Enter your drink : ").lower()
if drinks not in drinks_list:
    print("is not in drinks")
else:
    money=float(input(f"please put the  : {drinks_list[drinks]} $"))
    if money < drinks_list[drinks]:
        print(f"The money is not enough , take your money {money} ")

    elif money > drinks_list[drinks]:
        print(f"you put more money , take the rest {money-drinks_list[drinks]} ")
    else:
        print("enjoy")