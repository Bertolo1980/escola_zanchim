import re

import requests
from django.conf import settings


def enviar_whatsapp(telefone, mensagem):
    """Envia mensagem via WhatsApp Cloud API da Meta."""
    if not telefone:
        return None

    telefone_normalizado = re.sub(r'[^0-9]', '', str(telefone))
    if not telefone_normalizado.startswith('55'):
        telefone_normalizado = '55' + telefone_normalizado

    url = f'https://graph.facebook.com/v19.0/{settings.PHONE_NUMBER_ID}/messages'
    headers = {
        'Authorization': f'Bearer {settings.WHATSAPP_TOKEN}',
        'Content-Type': 'application/json',
    }
    payload = {
        'messaging_product': 'whatsapp',
        'to': telefone_normalizado,
        'type': 'text',
        'text': {'body': mensagem},
    }

    response = requests.post(url, headers=headers, json=payload)
    print(f'WhatsApp status_code: {response.status_code}')
    print(f'WhatsApp resposta: {response.text}')

    if response.status_code >= 400:
        response.raise_for_status()

    return response.json()
