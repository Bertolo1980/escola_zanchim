import requests
from decouple import config

TOKEN = config('WHATSAPP_TOKEN')
PHONE_NUMBER_ID = config('PHONE_NUMBER_ID')

def enviar_aviso_falta(telefone, nome_aluno, data_falta):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"

    payload = {
        "messaging_product": "whatsapp",
        "to": telefone,
        "type": "template",
        "template": {
            "name": "aviso_falta_aluno",
            "language": {"code": "pt_BR"},
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": nome_aluno},
                        {"type": "text", "text": data_falta}
                    ]
                }
            ]
        }
    }

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()
