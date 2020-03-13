import os
import json

# TODO: transactions history button
# TODO: evidences Button

def LoadCitizen(id: int):
    path = '../AnthillPay/DB/'

    translation = {
        'name': 'Имя: ',
        'work': 'Место работы: ',
        'district': 'Родился в: ',
        'eyeColor': 'Глаза: ',
        'hairColor': 'Цвет волос: ',
        'height': 'Рост: ',
        'money': 'Денег на счету: '
    }    
    for f in os.listdir(path):
        if not os.path.isdir(f'{path}{f}'):
            c = json.loads(open(f'{path}{f}', 'r').read())
            if c['id'] == id:
                payload = ''
                for k in translation.keys():
                    line = f'{translation[k]}{c[k]}'
                    payload += f'{line}\n'
                return payload

                