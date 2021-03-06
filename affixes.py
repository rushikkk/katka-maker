from datetime import datetime

STATIC_URL_PREFIX = "https://static.uxoxo.gq/wow/affixes/sl/s1"

affixes_rotation = {
    1:  ('fortified', 'bursting', 'volcanic', 'prideful', f'{STATIC_URL_PREFIX}/week-05.webp'),
    2:  ('tyrannical', 'bolstering', 'storming', 'prideful', f'{STATIC_URL_PREFIX}/tyr-bolst-storm.webp'),
    3:  ('fortified', 'spiteful', 'grievous', 'prideful', f'{STATIC_URL_PREFIX}/fort-spit-griev.webp'),
    4:  ('tyrannical', 'inspiring', 'necrotic', 'prideful', f'{STATIC_URL_PREFIX}/week-08.webp'),
    5:  ('fortified', 'sanguine', 'quaking', 'prideful', f'{STATIC_URL_PREFIX}/week-09.webp'),
    6:  ('tyrannical', 'raging', 'explosive', 'prideful', f'{STATIC_URL_PREFIX}/week-10.webp'),
    7:  ('fortified', 'spiteful', 'volcanic', 'prideful', f'{STATIC_URL_PREFIX}/week-11.webp'),
    8:  ('tyrannical', 'bolstering', 'necrotic', 'prideful', f'{STATIC_URL_PREFIX}/week-12.webp'),
    9:  ('fortified', 'inspiring', 'storming', 'prideful', f'{STATIC_URL_PREFIX}/fort-insp-storm.webp'),
    10: ('tyrannical', 'bursting', 'explosive', 'prideful', f'{STATIC_URL_PREFIX}/tyr-burst-expl.webp'),
    11: ('fortified', 'sanguine', 'grievous', 'prideful', f'{STATIC_URL_PREFIX}/fort-sang-griev.webp'),
    0:  ('tyrannical', 'raging', 'quaking', 'prideful', f'{STATIC_URL_PREFIX}/week-04.webp'),
}

affixes_ru = {
    'unknown':      ('Информация отсутствует', 'Информация о данной неделе аффиксов отсутсвует.'),
    'beguiling':    ('Манящий', 'В подземелье присутствуют посланники Азшары.'),
    'bolstering':   ('Усиливающий', 'Все противники, не являющиеся боссами, в момент гибели издают последний клич, '
                                    'увеличивая максимальный запас здоровья ближайших союзников и наносимый ими урон '
                                    'на 20%.'),
    'bursting':     ('Взрывной', 'Все противники, не являющиеся боссами, в момент гибели взрываются, в течение 4 '
                                 'секунд нанося всем игрокам урон в размере 10% от их максимального запаса здоровья. '
                                 'Этот эффект суммируется.'),
    'explosive':    ('Взрывоопасный', 'В бою противники периодически призывают взрывоопасные сферы, которые '
                                      'детонируют, если их вовремя не уничтожить.'),
    'fortified':    ('Укрепленный', 'Противники, не являющиеся боссами, имеют на 20% больше здоровья и наносят на 30% '
                                    'больше урона.'),
    'grievous':     ('Мучительный', 'Если уровень здоровья игрока опускается ниже 90%, он начинает получать '
                                    'нарастающий периодический урон до тех пор, пока его уровень здоровья не превысит '
                                    '90%.'),
    'inspiring':    ('Воодушевляющий', 'Некоторые не являющиеся боссами противники вдохновляют своим присутствием '
                                       'других врагов.'),
    'necrotic':     ('Некротический', 'Все атаки противника в ближнем бою накладывают на цели суммирующийся эффект '
                                      'гнили, который наносит периодический урон и уменьшает получаемое исцеление.'),
    'prideful':     ('Полный гордыни', 'Побеждая не являющихся боссами противников, игроки переполняются гордыней, '
                                       'пока рядом с ними не появляется воплощение гордыни. Победив воплощение, '
                                       'игроки получают мощное усиление.'),
    'quaking':      ('Сотрясающий', 'Периодически все игроки излучают ударные волны, нанося урон ближайшим союзникам '
                                    'и прерывая используемые ими способности.'),
    'raging':       ('Разъяренный', 'Противники, не являющиеся боссами, впадают в ярость, когда у них остается менее '
                                    '30% здоровья, и наносят на 100% больше урона, пока не погибнут.'),
    'sanguine':     ('Кровавый', 'Все противники, не являющиеся боссами, после гибели оставляют за собой лужу крови, '
                                 'которая лечит их союзников и наносит урон игрокам.'),
    'skittish':     ('Упрямый', 'Противники в значительной степени игнорируют объем угрозы, создаваемой танками.'),
    'spiteful':     ('Злопамятный', 'Бесы восстают из трупов не являющихся боссами противников и преследуют случайных '
                                    'игроков.'),
    'storming':     ('Бушующий', 'Во время боя противники время от времени призывают вихри, наносящие урон.'),
    'teeming':      ('Кишащий', 'В подземелье присутствуют дополнительные противники, не являющиеся боссами.'),
    'tyrannical':   ('Тиранический', 'Противники-боссы имеют на 40% больше здоровья и наносят на 15% больше урона.'),
    'volcanic':     ('Вулканический', 'Под ногами игроков, ведущих бой с противником на дальней дистанции, из-под '
                                      'земли периодически вырываются струи огня.'),
}

# Старт 3 сезона
start_day = datetime(2020, 12, 9, 10, 00, 00, 00)


def count_week():
    return ((datetime.now() - start_day).days // 7) + 1


def get_affixes(m=0):
    n_affix = (count_week() + m) % 12
    return n_affix
