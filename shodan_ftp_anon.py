import shodan

shodan_api_key = input("enter the shodan api key : ")
try:
    s = shodan.Shodan(shodan_api_key)

    results = s.search("port: 21 Anonymous user logged in")
    print(len(results['matches']))
    for result in results['matches']:
        print(result['ip_str'])
except:
    print("api error")
