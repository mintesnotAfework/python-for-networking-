import dns
import sys
import dns.resolver

while True:
    print("1.name lookup \n2.ip lookup")
    choice = input("Enter the your choice : ")
    try:
        choice = int(chioce)
        if choice <= 2 and choice >= 1:
            print("yes")
            break
    except:
        print("Enter your choice correctly(only number is allowed)")
if choice == 1:
    ip = input("Enter the ip address of the host : ")
    list_type = ['A','AAAA','NS','SOA','MX','TXT']
    number = 1
    while True:
        for i in list_type:
            print(number,i)
        choice2 = input("Enter your choice : ")
        try:
            choice2 = int(choice2)
            if 1 <= choice2 <=6:
                break
        except Exception:
            print("enter a number please")
    result = dns.reslover.query(ip,list_type[choice])
    print("The corresponding ip for ",ip ,"is ",result)
elif choice == 2:
    hostname = input("enter the domain name to translate : ")
    result = dns.revername.to_address(hostname)
    print("the corresponding ip to for",hostname,"is",result)
else:
    print("you have entered the wrong number please try again")
    
print("bye")
sys.exit(1)

