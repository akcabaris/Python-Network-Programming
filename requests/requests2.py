import requests

url = "https://github.com/"
headers = {'user-agent' : 'btk-akademi/1.1.1'}

try:
	r= requests.get(url, headers=headers, allow_redirects=True,timeout=0.001)
	print(r.status_code)
	print(r.headers.get('Date'))
	pass
except Exception as e:
	print(e)
	pass