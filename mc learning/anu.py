import http.cookiejar
import urllib.request
import requests
import bs4
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.
                             HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
authentication_url = "https://facebook.com/login.php"
payload = {

    'email':"9891794597",
    'pass':"anu"
}
data = urllib.parse.urlencode(payload).encode('utf-8')
req = urllib.request.Request(authentication_url, data)
resp = urllib.request.urlopen(req)
contents = resp.read()
#print(contents)
url = "https://facebook.com/cbse.abesec.9"
index = 0
z = []
while(index<6):
    data = requests.get(url, cookies=cj)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    print(url)
    for i in soup.find_all('a', href=True):
        if i['href'][0:22] == "/cbse.abesec.9/photos":
            #print("Hello")
            z.append(i['href'])
        if i.text.lower() == "show more":
            url = "https://facebook.com" +i['href']
    index = index + 1

photos = []
num = 0
for url in z:
    url = "https://facebook.com" +url
    data = requests.get(url, cookies=cj)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    for i in soup.find_all('a', href=True):
        if i.text.lower() =="view full size":
            photos.append(i['href'])
            urllib.request.urlretrieve(i['href'], str(num) +'.jpg')
            num = num+1

print(len(photos))
print(photos)
