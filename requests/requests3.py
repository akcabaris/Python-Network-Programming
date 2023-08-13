import requests

#metasploitable2 ip
url = 'http://10.10.10.21/dvwa/login.php'

data ={'username':'admin','password':'password','Login':'Login'}

try:
	r=requests.post(url, data=data, allow_redirects=True)
	print(r.status_code)
	print(r.text)
except Exc.peption as e:
	print(e)
	raise e