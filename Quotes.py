import requests
import json

def api ():
    category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'WYYdBPA6ThfxN7sK71fj8w==s2q93BYridj6kKz2'})
    if response.status_code == requests.codes.ok:
        quotes = json.loads(response.text)
        for quote in quotes :
           quote_json=quote
        return quote_json
    
    else:
        print("Error:", response.status_code, response.text)



