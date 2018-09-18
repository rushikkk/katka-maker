from datetime import datetime

affixes_rotation = {
    1:  ('fortified', 'sanguine', 'necrotic', 'infested', ''),
    2:  ('tyrannical', 'bursting', 'skittish', 'infested', 'http://bot-static.m-gaming.tk/tyr-burs-skitt-inf.jpg'),
    3:  ('fortified', 'teeming', 'quaking', 'infested', ''),
    4:  ('tyrannical', 'raging', 'necrotic', 'infested', ''),
    5:  ('fortified', 'bolstering', 'skittish', 'infested', ''),
    6:  ('tyrannical', 'teeming', 'volcanic', 'infested', ''),
    7:  ('fortified', 'sanguine', 'grievous', 'infested', ''),
    8:  ('tyrannical', 'bolstering', 'explosive', 'infested', ''),
    9:  ('fortified', 'bursting', 'quaking', 'infested', ''),
    10: ('tyrannical', 'raging', 'volcanic', 'infested', ''),
    11: ('fortified', 'teeming', 'explosive', 'infested', ''),
    0:  ('tyrannical', 'bolstering', 'grievous', 'infested', '')
    }

affixes_ru = {
    'bolstering':   ['усиливающий'],
    'bursting':     ['взрывной'],
    'explosive':    ['взрывоопасный'],
    'fortified':    ['укрепленный'],
    'grievous':     ['мучительный'],
    'infested':     ['зараженный'],
    'necrotic':     ['некротический'],
    'quaking':      ['сотрясающий'],
    'raging':       ['разъяренный'],
    'sanguine':     ['кровавый'],
    'skittish':     ['упрямый'],
    'teeming':      ['кишащий'],
    'tyrannical':   ['тиранический'],
    'volcanic':     ['вулканический'],
}

# Старт 10:00 5 сентября 2018 года
start_day = datetime(2018, 9, 5, 10, 00, 00, 00)


def count_week():
    return ((datetime.now() - start_day).days // 7) + 1


def get_affixes(m=0):
    n_affix = (count_week() + m) % 12
    return n_affix


print(affixes_rotation[get_affixes(120)])
