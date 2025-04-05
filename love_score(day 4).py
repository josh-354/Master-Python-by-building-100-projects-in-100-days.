def calculate_love_score():

    name1=str(input("enter boy"))
    name2=str(input("enter girl"))

    combined_names=name1+name2


    true_count=(
        combined_names.count('t')+
        combined_names.count('r')+
        combined_names.count('u')+
        combined_names.count('e')


    )

    love_count=(
        combined_names.count('l')+
        combined_names.count('o')+
        combined_names.count('v')+
        combined_names.count('e')

        
    )

    love_score = (int(str(true_count))+int(str(love_count)))*2

    print(f"Your love score is {love_score}.")


calculate_love_score()
