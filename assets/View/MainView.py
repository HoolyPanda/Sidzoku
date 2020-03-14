import random
import base64
from assets.Controller.CItizenController import *
from assets.View.keyboards import mainKB


class MainView:
    def __init__(self, session, userId, event):
        self.vkID = userId
        self.session = session
        self.citizenID = None
        pass

    def ParseEvent(self, event):
        text = event['text']
        a = text.split(' ')

        if 'payload' in event.keys():
            a = 0
            payload = json.loads(event['payload'])['mainMenu']
            if self.citizenID:
                if payload == 'История транзакций':
                    transactionsHistory = GetTransactionsHistory(self.citizenID)
                    
                    self.session.method('messages.send', {
                        'message': f'История транзакций: {transactionsHistory}',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': mainKB
                    })  
                    pass
                elif payload == 'Улики':
                    evidences = GetEvidences(self.citizenID)

                    self.session.method('messages.send', {
                        'message': f'{evidences}',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': mainKB
                    })  
                    pass
                elif payload == 'Завершить':
                    return True

        elif text.split(' ').__len__() == 1 and text.split('\n').__len__() == 1:
            try:
                a = base64.b64decode(text)
                if len(a[len('TransferMoneyTo '):]) > 0:
                    id = int(a[len('TransferMoneyTo '):])
                    self.citizenID = id
                    paylaod = LoadCitizen(id)
                    self.session.method('messages.send', {
                        'message': f'Профиль гражданина\n\n{paylaod}',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': mainKB
                    })                 
        
            except Exception as e:
                self.session.method('messages.send', {
                    'message': f'Неверный формат введенных данных',
                    'peer_id': self.vkID,
                    'random_id': random.randint(1, 10000000000000)
                })   
                return True           
            pass
        else:
            self.session.method('messages.send', {
                    'message': f'Неверный формат введенных данных',
                    'peer_id': self.vkID,
                    'random_id': random.randint(1, 10000000000000)
                })  
            return True
        