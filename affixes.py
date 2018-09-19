from datetime import datetime

affixes_rotation = {
    1:  ('fortified', 'sanguine', 'necrotic', 'infested', 'http://bot-static.m-gaming.tk/fort-sang-necr-inf.jpg'),
    2:  ('tyrannical', 'bursting', 'skittish', 'infested', 'http://bot-static.m-gaming.tk/tyr-burs-skitt-inf.jpg'),
    3:  ('fortified', 'teeming', 'quaking', 'infested', 'http://bot-static.m-gaming.tk/fort-teem-quak-inf.jpg'),
    4:  ('tyrannical', 'raging', 'necrotic', 'infested', 'http://bot-static.m-gaming.tk/tyr-rag-necr-inf.jpg'),
    5:  ('fortified', 'bolstering', 'skittish', 'infested', 'http://bot-static.m-gaming.tk/fort-bols-skitt-inf.jpg'),
    6:  ('tyrannical', 'teeming', 'volcanic', 'infested', 'http://bot-static.m-gaming.tk/tyr-teem-volc-inf.jpg'),
    7:  ('fortified', 'sanguine', 'grievous', 'infested', 'http://bot-static.m-gaming.tk/fort-sang-griev-inf.jpg'),
    8:  ('tyrannical', 'bolstering', 'explosive', 'infested', 'http://bot-static.m-gaming.tk/tyr-bolst-expl-inf.jpg'),
    9:  ('fortified', 'bursting', 'quaking', 'infested', 'http://bot-static.m-gaming.tk/fort-burst-quak-inf.jpg'),
    10: ('tyrannical', 'raging', 'volcanic', 'infested', 'http://bot-static.m-gaming.tk/tyr-rag-volc-inf.jpg'),
    11: ('fortified', 'teeming', 'explosive', 'infested', 'http://bot-static.m-gaming.tk/fort-teem-expl-inf.jpg'),
    0:  ('tyrannical', 'bolstering', 'grievous', 'infested', 'http://bot-static.m-gaming.tk/tyr-bols-griev-inf.jpg')
    }

affixes_ru = {
    'bolstering':   ['Усиливающий', 'Все противники, не являющиеся боссами, в момент гибели издают последний клич, \
                    увеличивая максимальный запас здоровья ближайших союзников и наносимый ими урон \
                    на 20%.'],
    'bursting':     ['Взрывной', 'Все противники, не являющиеся боссами, в момент гибели взрываются, в течение \
                    4 секунд нанося всем игрокам урон в размере 10% от их максимального запаса здоровья. \
                    Этот эффект суммируется.'],
    'explosive':    ['Взрывоопасный', 'В бою противники периодически призывают взрывоопасные сферы, которые \
                    детонируют, если их вовремя не уничтожить.'],
    'fortified':    ['Укрепленный', 'Противники, не являющиеся боссами, имеют на 20% больше здоровья и наносят \
                    на 30% больше урона.'],
    'grievous':     ['Мучительный', 'Если уровень здоровья игрока опускается ниже 90%, он начинает получать \
                    нарастающий периодический урон до тех пор, пока его уровень здоровья не превысит 90%.'],
    'infested':     ['Зараженный', "Некоторые противники, не являющиеся боссами, заражены порождениями Г'ууна."],
    'necrotic':     ['Некротический', 'Все атаки противника в ближнем бою накладывают на цели суммирующийся эффект \
                    гнили, который наносит периодический урон и уменьшает получаемое исцеление.'],
    'quaking':      ['Сотрясающий', 'Периодически все игроки излучают ударные волны, нанося урон ближайшим союзникам \
                    и прерывая используемые ими способности.'],
    'raging':       ['Разъяренный', 'Противники, не являющиеся боссами, впадают в ярость, когда у них остается менее \
                    30% здоровья, и наносят на 100% больше урона, пока не погибнут.'],
    'sanguine':     ['Кровавый', 'Все противники, не являющиеся боссами, после гибели оставляют за собой лужу крови, \
                    которая лечит их союзников и наносит урон игрокам.'],
    'skittish':     ['Упрямый', 'Противники в значительной степени игнорируют объем угрозы, создаваемой танками.'],
    'teeming':      ['Кишащий', 'В подземелье присутствуют дополнительные противники, не являющиеся боссами.'],
    'tyrannical':   ['Тиранический', 'Противники-боссы имеют на 40% больше здоровья и наносят на 15% больше урона.'],
    'volcanic':     ['Вулканический', 'Под ногами игроков, ведущих бой с противником на дальней дистанции, из-под \
                    земли периодически вырываются струи огня.'],
}

# Старт 10:00 5 сентября 2018 года
start_day = datetime(2018, 9, 5, 10, 00, 00, 00)


def count_week():
    return ((datetime.now() - start_day).days // 7) + 1


def get_affixes(m=0):
    n_affix = (count_week() + m) % 12
    return n_affix


print(affixes_rotation[get_affixes(120)])
