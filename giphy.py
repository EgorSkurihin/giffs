import os
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


adapter = HTTPAdapter(max_retries=Retry(
    total=2,
    backoff_factor=0.25,
	raise_on_status=False,
))
session = requests.Session()
session.mount('http://', adapter)
session.mount('https://', adapter)

giphy_base_url = 'https://api.giphy.com/v1/gifs'
api_key = os.getenv('API_KEY')


def get_gif_url(tag):
	params = {
		'api_key': api_key,
		'tag': tag,
	}
	try:
		response = session.get(
			url=f'{giphy_base_url}/random',
			params=params,
			timeout=(3, 6)
		)
		if response.status_code != 200:
			return ''
	
		return response.json()['data']['images']['original']['url']

	except Exception as e:
		return ''
