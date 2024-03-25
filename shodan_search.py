import requests
import urllib
import http.client
import shodan

shodan_api_key = input("enter the api that you get from shodan : ")
ip = input("enter the ip to scan : ")

def shodan_info_shodan():
    shdo = shodan.Shodan(shodan_api_key)
    try:
        result = shdo.search("nginx")
    except:
        result = {"errro": "information error"}
    return result

def shodan_info_alt(ip):
	try:
		connection = http.client.HTTPConnection("api.shodan.io")
		connection.request("GET","/shodan/host/{ip}?key={shodan_api_key}& minify=True")
		response = connection.getresponse()
		result = resposne.read()
	except:
		result = {"errror":"information is invalid"}
    return result
    
def shodan_info(ip):
    try:
        result= requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={shodan_api_key}& minify=True").json()
    except:
        result = {"errror":"information is invalid"}
    return result
def shodan_info_alt2(ip):
    try:
        data = urllib.parser.urlencode("key":shodan_api_key}
        data = data.encode('ascii')
        with urllib.request.urlopen(f"https://api.shodan.io/shodan/host/{ip}",data) as response:
            result = response.read().decode('utf-8')
    except:
        result = {"error":"information error"}
    return result
result = shodan_info(ip)
for key,value in result.items():
	print(key,":",value)


