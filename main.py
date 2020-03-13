import vk_api
from vk_api import bot_longpoll
import assets.View.MainView as mainView
import threading
import json

token = open('./assets/token.cred').readline().replace('\n', '')


views = []
userIds = []

apiViews = []
apiIDs = []

def parseStuff(userId, event):
    print(json.dumps(event['object']))
    if event['object']['from_id'] >= 0:
        for view in views:
            if view.vkID == userId:
                if view.ParseEvent(event['object']) == True:
                    views.remove(view)
                    userIds.remove(view.vkID)
                break    
    else:
        # TODO: parse bots conversation
        pass

def parseAPIReq(userId, event):
    for apiView in apiViews:
        if apiView.vkID == userId:
            if apiView.ParseEvent(event):
                apiViews.remove(apiView)
                apiIDs.remove(userId)
    pass

def main():
    try:
        session = vk_api.VkApi(token= token)
        lps = bot_longpoll.VkBotLongPoll(session, 192912095)
        for event in lps.listen():
            for view in views:
                if view.vkID not in userIds:
                    userIds.append(view.vkID)
            rawEvent = event.raw
            userId = rawEvent['object']['from_id']
            if event.raw['object']['from_id'] >= 0:
                mV = mainView.MainView(session= session, userId= userId, event= rawEvent)
                if mV.vkID not in userIds:
                    views.append(mV)
                    userIds.append(mV.vkID)
                a = threading.Thread(target= parseStuff, kwargs= {'event': rawEvent, "userId": userId})
                a.start()
            else: 
                userId = rawEvent['object']['peer_id']
                # apiV = APIView.APIView(session, userId)
                # if apiV.vkID not in apiIDs:
                #     apiViews.append(apiV)
                #     apiIDs.append(userId)
                # b = threading.Thread(target= parseAPIReq, kwargs= {'userId': userId, 'event': event})
                # b.start()
            pass
    except Exception as e:
        print(str(e))
        main()

main()