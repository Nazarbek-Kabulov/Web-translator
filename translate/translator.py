import requests


def translate(language1, language2, text):
    url = "https://translate-plus.p.rapidapi.com/translate"
    if text == '':
        text = ' '
    else:
        text = text
    payload = {
        "text": f"{text}",
        "source": f"{language1}",
        "target": f"{language2}"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "af0a9a4d97mshf5d4fc239774059p147199jsnf1c8c0a3a5ea",
        "X-RapidAPI-Host": "translate-plus.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()
