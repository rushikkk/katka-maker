from datetime import datetime

affixes_rotation = {
    1:  ('fortified', 'sanguine', 'necrotic', 'beguiling', 'http://bot-static.m-gaming.tk/fort-sang-necr-reap.jpg'),
    2:  ('tyrannical', 'bursting', 'skittish', 'beguiling', 'http://bot-static.m-gaming.tk/tyr-burs-skitt-reap.jpg'),
    3:  ('fortified', 'teeming', 'quaking', 'beguiling', 'http://bot-static.m-gaming.tk/fort-teem-quak-reap.jpg'),
    4:  ('tyrannical', 'raging', 'necrotic', 'beguiling', 'http://bot-static.m-gaming.tk/tyr-rag-necr-reap.jpg'),
    5:  ('fortified', 'bolstering', 'skittish', 'beguiling', 'http://bot-static.m-gaming.tk/fort-bols-skitt-reap.jpg'),
    6:  ('tyrannical', 'teeming', 'volcanic', 'beguiling', 'http://bot-static.m-gaming.tk/tyr-teem-volc-reap.jpg'),
    7:  ('fortified', 'sanguine', 'grievous', 'beguiling', 'http://bot-static.m-gaming.tk/fort-sang-griev-reap.jpg'),
    8:  ('tyrannical', 'bolstering', 'explosive', 'beguiling', 'http://bot-static.m-gaming.tk/tyr-bolst-expl-reap.jpg'),
    9:  ('fortified', 'bursting', 'quaking', 'beguiling', 'http://bot-static.m-gaming.tk/fort-burst-quak-reap.jpg'),
    10: ('tyrannical', 'raging', 'volcanic', 'beguiling', 'http://bot-static.m-gaming.tk/tyr-rag-volc-reap.jpg'),
    11: ('fortified', 'teeming', 'explosive', 'beguiling', 'http://bot-static.m-gaming.tk/fort-teem-expl-reap.jpg'),
    0:  ('tyrannical', 'bolstering', 'grievous', 'beguiling', 'http://bot-static.m-gaming.tk/tyr-bols-griev-reap.jpg')
    }

affixes_ru = {
    'bolstering':   ('Усиливающий', 'Все противники, не являющиеся боссами, в момент гибели издают последний клич, \
                    увеличивая максимальный запас здоровья ближайших союзников и наносимый ими урон \
                    на 20%.'),
    'bursting':     ('Взрывной', 'Все противники, не являющиеся боссами, в момент гибели взрываются, в течение \
                    4 секунд нанося всем игрокам урон в размере 10% от их максимального запаса здоровья. \
                    Этот эффект суммируется.'),
    'explosive':    ('Взрывоопасный', 'В бою противники периодически призывают взрывоопасные сферы, которые \
                    детонируют, если их вовремя не уничтожить.'),
    'fortified':    ('Укрепленный', 'Противники, не являющиеся боссами, имеют на 20% больше здоровья и наносят \
                    на 30% больше урона.'),
    'grievous':     ('Мучительный', 'Если уровень здоровья игрока опускается ниже 90%, он начинает получать \
                    нарастающий периодический урон до тех пор, пока его уровень здоровья не превысит 90%.'),
    'beguiling':    ('Манящий', 'В подземелье присутствуют посланники Азшары.'),
    'necrotic':     ('Некротический', 'Все атаки противника в ближнем бою накладывают на цели суммирующийся эффект \
                    гнили, который наносит периодический урон и уменьшает получаемое исцеление.'),
    'quaking':      ('Сотрясающий', 'Периодически все игроки излучают ударные волны, нанося урон ближайшим союзникам \
                    и прерывая используемые ими способности.'),
    'raging':       ('Разъяренный', 'Противники, не являющиеся боссами, впадают в ярость, когда у них остается менее \
                    30% здоровья, и наносят на 100% больше урона, пока не погибнут.'),
    'sanguine':     ('Кровавый', 'Все противники, не являющиеся боссами, после гибели оставляют за собой лужу крови, \
                    которая лечит их союзников и наносит урон игрокам.'),
    'skittish':     ('Упрямый', 'Противники в значительной степени игнорируют объем угрозы, создаваемой танками.'),
    'teeming':      ('Кишащий', 'В подземелье присутствуют дополнительные противники, не являющиеся боссами.'),
    'tyrannical':   ('Тиранический', 'Противники-боссы имеют на 40% больше здоровья и наносят на 15% больше урона.'),
    'volcanic':     ('Вулканический', 'Под ногами игроков, ведущих бой с противником на дальней дистанции, из-под \
                    земли периодически вырываются струи огня.'),
}

# Старт 10:00 5 сентября 2018 года
start_day = datetime(2019, 7, 3, 10, 00, 00, 00)


def count_week():
    return ((datetime.now() - start_day).days // 7) + 1


def get_affixes(m=0):
    n_affix = (count_week() + m) % 12
    return n_affix
