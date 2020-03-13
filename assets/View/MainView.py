import random
import base64
from assets.Controller.CItizenController import *


class MainView:
    def __init__(self, session, userId, event):
        self.vkID = userId
        self.session = session
        pass

    def ParseEvent(self, event):
        text = event['text']
        a = text.split(' ')
        if text.split(' ').__len__() == 1 and text.split('\n').__len__() == 1:
            try:
                a = base64.b64decode(text)
                if len(a[len('TransferMoneyTo '):]) > 0:
                    id = int(a[len('TransferMoneyTo '):])
                    m  = 0
                    paylaod = LoadCitizen(id)
                    self.session.method('messages.send', {
                        'message': f'Профиль гражданина\n\n{paylaod}',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000)
                    })                 
        
            except Exception as e:
                self.session.method('messages.send', {
                    'message': f'Неверный формат введенных данных',
                    'peer_id': self.vkID,
                    'random_id': random.randint(1, 10000000000000)
                })                 
            pass
        else:
            self.session.method('messages.send', {
                    'message': f'Неверный формат введенных данных',
                    'peer_id': self.vkID,
                    'random_id': random.randint(1, 10000000000000)
                })  
            return True
        