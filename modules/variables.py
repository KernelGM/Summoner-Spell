summoner_spells = ['Barrier', 'Cleanse', 'Exhaust', 'Flash',
                   'Ghost',  'Heal', 'Ignite', 'Smite', 'Teleport',
                   'Unleashed Teleport']

cooldowns = {
    'Barrier': 180,
    'Cleanse': 210,
    'Exhaust': 210,
    'Flash': 300,
    'Ghost': 210,
    'Heal': 240,
    'Ignite': 180,
    'Smite': 3,
    'Teleport': 360,
    'Unleashed Teleport': 240,
}

roles = {'TOP': {
    'spell_d': 1,
    'spell_f': 2},
    'JNG': {
    'spell_d': 1,
    'spell_f': 2},
    'MID': {
    'spell_d': 1,
    'spell_f': 2},
    'ADC': {
    'spell_d': 1,
    'spell_f': 2},
    'SUP': {
    'spell_d': 1,
    'spell_f': 2}}


for key, value in roles.items():
    print(key, value)
