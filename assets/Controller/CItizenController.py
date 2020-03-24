import os
import json

def GetTransactionsHistory(id: int):
    path = '../AnthillPay/DB/'

    for f in os.listdir(path):
        if not os.path.isdir(f'{path}{f}'):
            c = json.loads(open(f'{path}{f}', 'r').read())
            if c['id'] == id:
                payload = ''
                for k in c['transactions']:
                    payload += f'\n{k}'
                return payload

def GetEvidences(id: int):
    path = '../AnthillPay/DB/'

    translation = {
        'name': 'Имя: ',
        'work': 'Место работы: ',
        'district': 'Родился в: ',
        'eyes': 'Глаза: ',
        'hair': 'Цвет волос: ',
        'height': 'Рост: ',
        'money': 'Денег на счету: ',
        'id': 'Личный код: '
    } 

    for f in os.listdir(path):
        if not os.path.isdir(f'{path}{f}'):
            c = json.loads(open(f'{path}{f}', 'r').read())
            if c['id'] == id:
                payload = ''
                if len(c['evidences']) > 0:    
                    for evidence in c['evidences']:
                        payload += f'\nНайдена улика\n'
                        for k in evidence.keys():
                            line = f'===>{translation[k]}{evidence[k]}\n'
                            payload += line
                else:
                    payload = "Улик не обнаружено"
                return payload

def LoadCitizen(id: int):
    path = '../AnthillPay/DB/'

    translation = {
        'name': 'Имя: ',
        'work': 'Место работы: ',
        'district': 'Родился в: ',
        'eyeColor': 'Глаза: ',
        'hairColor': 'Цвет волос: ',
        'height': 'Рост: ',
        'money': 'Денег на счету: ',
        "id": 'Личный номер: '
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
                