#Introduction to Python Requests
#Processing HTTP requests through python
#leveraging HTTPBin.org to test HTTP Request and Response
import requests
x=requests.get('https://httpbin.org/get')
#Print header information similar to running a curl -I Https://httpbin.org/get command
print(x.headers)
#Print only a specific header
print(x.headers['Server'])
#Retrieving HTTP Status Code
if x.status_code == 200:
	print("HTTP Status Code: " + str(x.status_code))
	print("Success!")
elif x.status_code == 404:
	print("HTTP Path not found!")
#Tracking request response timing
print("Time elapsed: " + str(x.elapsed))
#Print the cookies 
print("Cookie Jar Object: " + str(x.cookies))
#Look at returned contents
print(x.content)
#Results in unicode
print(x.text)

#Get request with passed in parameters
x=requests.get("https://httpbin.org/get", params={'id':'1'})
print(x.url)
x=requests.get("https://httpbin.org/get?id=2")
print(x.url)
x=requests.get("https://httpbin.org/get", params={'id':'3'}, headers={'Accept':'application/json'})
print(x.text)
x=requests.get("https://httpbin.org/get", params={'id':'4'},headers={'Accept':'application/json','test_header':'test'})
print(x.text)

#Specifiying other HTTP requests
#Delete Request
x=requests.delete('https://httpbin.org/delete')
print(x.text)
#Post Request
x=requests.post('https://httpbin.org/post', data={'a':'b', 'c':'d','e':'f'})
print(x.text)
#Using file formats within http requests 
files = {'file':open('errors.txt','rb')}
x=requests.post('https://httpbin.org/post', files=files)
print(x.text)

#Requests for basic authentication
x=requests.get('http://httpbin.org/get', auth=('username','password'))
print(x.text)

x=requests.get('http://github.com', allow_redirects=False)
print(x.headers)
#Http Cookies
x=requests.get('http://httpbin.org/cookies',cookies={'a':'b'})
print(x.content)

x=requests.session()
x.cookies.update({'a':'b'})
print(x.get('http://httpbin.org/cookies').text)

#Retrieve  JSON using a request
x=requests.get("https://api.github.com/events")
print(x.json())
#Downloading file from the internet
x=requests.get('https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png')
with open('google.png','wb') as f:
	f.write(x.content)
