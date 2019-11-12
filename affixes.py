from datetime import datetime

affixes_rotation = {
    1:  ('fortified', 'bolstering', 'grievous', 'beguiling',
         'https://bot-static.m-gaming.tk/fort-bolst-griev-beg.webp'),
    2:  ('tyrannical', 'raging', 'explosive', 'beguiling', 'https://bot-static.m-gaming.tk/tyr-rag-expl-beg.webp'),
    3:  ('fortified', 'sanguine', 'grievous', 'beguiling', 'https://bot-static.m-gaming.tk/forti-sang-griev-beg.webp'),
    4:  ('tyrannical', 'teeming', 'volcanic', 'beguiling', 'https://bot-static.m-gaming.tk/tyr-teem-volc-beg.webp'),
    5:  ('fortified', 'bolstering', 'skittish', 'beguiling', 'https://bot-static.m-gaming.tk/fort-bolst-skit-beg.webp'),
    6:  ('tyrannical', 'bursting', 'necrotic', 'beguiling', 'https://bot-static.m-gaming.tk/tyr-burst-necr-beg.webp'),
    7:  ('fortified', 'sanguine', 'quaking', 'beguiling', 'https://bot-static.m-gaming.tk/fort-sang-quak-beg.webp'),
    8:  ('tyrannical', 'bolstering', 'explosive', 'beguiling', 'https://bot-static.m-gaming.tk/tyr-bolst-expl.webp'),
    9:  ('fortified', 'bursting', 'volcanic', 'beguiling', 'https://bot-static.m-gaming.tk/fort-burst-volc-beg.webp'),
    10: ('tyrannical', 'raging', 'volcanic', 'beguiling', 'https://bot-static.m-gaming.tk/tyr-rag-volc-beg.webp'),
    11: ('fortified', 'teeming', 'quaking', 'beguiling', 'https://bot-static.m-gaming.tk/fort-teem-quak-beg.webp'),
    0:  ('tyrannical', 'raging', 'necrotic', 'beguiling', 'https://bot-static.m-gaming.tk/tyr-rag-necr-beg.webp')
    }

affixes_ru = {
    'unknown':      ('Информация отсутствует', 'Информация о данной неделе аффиксов отсутсвует.'),
    'beguiling':    ('Манящий', 'В подземелье присутствуют посланники Азшары.'),
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

# Старт 3 сезона
start_day = datetime(2019, 7, 10, 10, 00, 00, 00)


def count_week():
    return ((datetime.now() - start_day).days // 7) + 1


def get_affixes(m=0):
    n_affix = (count_week() + m) % 12
    return n_affix
