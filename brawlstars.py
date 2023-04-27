#ya boi plays too much brawlstars, so i'm going to practice with the API.

import urllib3

from api_keys import TEST_API_TOKEN

MAL = '%2328RP22UYC'
CAL = '%2320CL0P8C0'

http = urllib3.PoolManager()

headers = {'Authorization': f'Bearer {TEST_API_TOKEN}'}
url = f'https://api.brawlstars.com/v1/players/{MAL}/battlelog'

resp = http.request('GET', url, headers=headers)

print(resp.data)