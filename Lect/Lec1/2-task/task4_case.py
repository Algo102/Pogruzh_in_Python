color = input('Твой любимый цвет?')
match color:
    case 'красный' | 'оранжевый':
        print('Ты любитель яркого')
    case 'зеленый':
        print('Ты не охотник?')
    case 'синий':
        print('Ха, классика')
    case _:
        print('Тебя не понять')