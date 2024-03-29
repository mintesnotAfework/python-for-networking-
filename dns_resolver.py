import dns
import sys
import dns.resolver

while True:
    print("1.name lookup")
    print("2.ip lookup")
    choice = input("Enter the your choice : ")
    try:
        choice = int(choice)
        print("yes")
        if choice <= 2 and choice >= 1:
            break
    except:
        print("Enter your choice correctly(only number is allowed)")
if choice == 1:
    ip = input("Enter the name of the host : ")
    list_type = ['A','AAAA','NS','SOA','MX','TXT']
    number = 1
    while True:
        for i in list_type:
            print(number,".",i)
            number += 1
        choice2 = input("Enter your choice : ")
        try:
            choice2 = int(choice2)
            if 1 <= choice2 <=6:
                break
        except Exception:
            print("enter a number please")
    try:
        result = dns.resolver.resolve(ip,list_type[choice])
        print("The corresponding ip for ",ip ,"is ",result.nameserver)
    except:
        print("An error has occured......")
        print("check your dns configuration")
elif choice == 2:
    hostname = input("enter the domain ip to translate : ")
    result = dns.reversename.to_address(hostname)
    print("the corresponding ip to for",hostname,"is",result)
else:
    print("you have entered the wrong number please try again")
    
print("bye")
sys.exit(1)

