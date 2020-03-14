import json


mKB = {
    'one_time': True,
    'buttons':
    [
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"mainMenu\":\"История транзакций\"}",
                        "label": "История транзакций"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"mainMenu\":\"Улики\"}",
                        "label": "Улики"
                    },
                "color": "secondary"
            }
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"mainMenu\":\"Завершить\"}",
                        "label": "Завершить"
                    },
                "color": "positive"
            }   
        ]
    ]
}

mainKB = json.dumps(mKB)