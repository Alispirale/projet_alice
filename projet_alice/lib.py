def try_me():
    x = input('do you have memes for me? yes/no')
    if x == 'yes' or x == 'Yes':
        return 'please send it to me'
    if x == 'no' or x == 'No':
        return 'what are you doing here then'
    if x not in ['yes','Yes','no','No']:
        'Please entre valid response you anoying cow'
