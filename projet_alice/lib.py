def try_me():

    while True:
        x = input('do you have memes for me? yes/no ')
        if x not in ['yes', 'Yes', 'No', 'no']:
            print("Sorry, what are you saying you anoying cow")
            continue
        else:
            break

    if x == 'yes' or x == 'Yes':
        return 'please send it to me'
    if x == 'no' or x == 'No':
        return 'what are you doing here then'
