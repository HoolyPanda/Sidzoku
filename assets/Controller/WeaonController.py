import json
import os

def LoadWeapon(id: int):
    path = '../Blacksmith/DB/'
    for file in os.listdir(path):
        if str(id) in file:
            a = {}
            weapon = open(f'{path}{file}').read()
            weapon = json.loads(weapon)
            payload = ''
            for param in weapon.keys():
                payload += f'===>{param}: {weapon[param]}\n'
            return payload

