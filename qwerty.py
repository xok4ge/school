class Situation:
    def __init__(self):
        self.description = ''
        self.ways = dict()
        self.name = ''


situations = {}
start = Situation()
start.description = 'Вы просыпаетесь внутри одной из квартир разрушенного многоквартирного дома'
start.ways['Лестница'] = 'Выйти из квартиры'
start.ways['Фатализм'] = 'Ничего не делать и продолжить лежать'
start.name = 'Старт'
situations[start.name] = start


staircase = Situation()
staircase.description = "Вы выходите на лестничную площадку"
staircase.ways['Здесь бутылки принимают?'] = 'Войти в квартиру напротив'
staircase.ways['Икар'] = 'Спуститься вниз и выйти на улицу'
staircase.ways['Сизиф'] = 'Подняться на крышу'
staircase.name = 'Лестница'
situations[staircase.name] = staircase

meet = Situation()
meet.description = 'Как только вы выходите на улицу, на вас тут же нападает разъяренный рейдер с ножом'
meet.ways['Лестница'] = 'Убежать обратно на лестничную площадку'
meet.ways['Рожденный бегать'] = 'Увернуться от атак и убежать'
meet.ways['Mortal Kombat'] = 'Напасть в ответ'
meet.name = 'Икар'
situations[meet.name] = meet

death_fight = Situation()
death_fight.description = '''
Вы уворачиваетесь от удара и начинаете бежать, но вдруг ощущаете, нестерпимую боль в ноге.
Оказывается ножи можно метать, чем и воспользовался противник. Вскоре он подбежит и в порыве ярости проломит вам череп своими берцами.'''
death_fight.name = 'Рожденный бегать'
situations[death_fight.name] = death_fight

fight = Situation()
fight.description = 'Вы выхватываете свой обрез и стреляете по неприятелю. Да, все так просто'
fight.ways['Обыск'] = 'Обыскать труп'
fight.ways['Убежище'] = 'Пойти своей дорогой'
fight.name = 'Mortal Kombat'
situations[fight.name] = fight

flat = Situation()
flat.description = 'Вы входите в квартиру'
flat.ways['Кухня'] = 'Зайти на кухню'
flat.ways['Спальня'] = 'Зайти в спальню'
flat.ways['Лестница'] = 'Вернуться'
flat.name = 'Здесь бутылки принимают?'
situations[flat.name] = flat

kitchen = Situation()
kitchen.description = 'В кухне вы обнаруживаете сломанный самогонный аппарат и бутылку, наполненную по видимому этим самым напитком, а также множество шкафчиков'
kitchen.ways['Дед доест'] = 'Выпить содержимое'
kitchen.ways['Целомудрие'] = 'Обыскать шкафчики'
kitchen.ways['Здесь бутылки принимают?'] = 'Вернуться'
kitchen.name = 'Кухня'
situations[kitchen.name] = kitchen

death_alc = Situation()
death_alc.description = 'Как только вы делаете глоток, ваши синапсы мгновенно сгорают, а из глаз начинает течь кровь. Вскоре вы умираете в страшных муках'
death_alc.name = 'Дед доест'
situations[death_alc.name] = death_alc

search = Situation()
search.description = 'Вы обыскиваете один из шкафчиков и кладете найденные предметы в рюкзак'
search.ways['Кухня'] = 'Остановиться'
search.ways['Целомудрие'] = 'Продолжить'
search.name = 'Целомудрие'
situations[search.name] = search

bedroom = Situation()
bedroom.description = 'Вы входите в спальню. На полу стоит телевизор с DVD-проигрывателем'
bedroom.ways['Гик'] = 'Включить проигрыватель'
bedroom.ways['Здесь бутылки принимают?'] = 'Вернуться'
bedroom.name = 'Спальня'
situations[bedroom.name] = bedroom

death_anime = Situation()
death_anime.description = '''
Как только вы включаете телевизор, комнату наполняет оглушительный крик \'АНННННИИГИЛЯТОРНАЯ ПУШКАААА\'.
Звук был настолько мощный, что ваше тело моментально превращается в прах'''
death_anime.name = 'Гик'
situations[death_anime.name] = death_anime

roof = Situation()
roof.description = '''Вы выбегаете на крышу и задеваете растяжку, из-за которой спотыкаетесь и перелетаете ограждение.
Последние, что вы слышите - это трек ЛСП \'Номера\'.
'''
roof.name = 'Сизиф'
situations[roof.name] = roof

death = Situation()
death.description = 'Вы медленно истекаете кровью и спустя некоторое время умираете. А чего вы еще ожидали?'
death.name = 'Фатализм'
situations[death.name] = death

d1 = Situation()
d1.description = 'Бюджета на сцену не хватило, да и у разраба было другое дз. Здесь ваш путь кончается'
d1.name = 'Обыск'
situations[d1.name] = d1

d2 = Situation()
d2.description = 'Бюджета на сцену не хватило, да и у разраба было другое дз. Здесь ваш путь кончается'
d2.name = 'Убежище'
situations[d2.name] = d2

current_situation = situations['Старт']
while True:
    print(current_situation.description)
    for key, value in current_situation.ways.items():
        print(f'{key}: {value}')
    choice = input()
    current_situation = situations[choice]
    if len(current_situation.ways) == 0:
        break
print(current_situation.description)