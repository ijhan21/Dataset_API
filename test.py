import requests

url = 'http://127.0.0.1:8000/api/auth'
response = requests.post(url, data = {'username':'admin', 'password':'1'})
print(response.text)

# myToken = response.text
# myToken = myToken.split(':')[-1].replace('}','').replace('"','')
# print(myToken)
myToken = response.json()['token']
header = {'Authorization':'Token '+myToken}
print("header",header)
url = 'http://127.0.0.1:8000/api/dataset_list'
response = requests.get(url,headers=header)
print(response.text)