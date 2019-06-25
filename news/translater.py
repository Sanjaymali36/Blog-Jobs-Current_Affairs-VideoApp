import json
import requests
def translate_hindi(text):
    key = 'AIzaSyDOW6Nt-1jpzxcEbypSpJ-ObCsZHjYBjPA'
    url = 'https://translation.googleapis.com/language/translate/v2?target=hi&key=' + key + '&q=' + text + ''
    r = requests.get(url)
    if r.status_code == 200:
        trans = r.text
        trans = json.loads(trans)
        trans_dict = trans['data']['translations']
        final_text = trans_dict[0]['translatedText']
        return final_text
    else:
        return r.status_code