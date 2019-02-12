Captial = {"VietNam":"Hanoi",
"Indonesia":"Jakarta",
"Malaysia":"Kualalumpur",
"Japan":"Tokyo",
"China":"Beijing",
"Korean":"Seoul"}
for key in Captial:
    print(key)
Country = input("Enter your country: ")
if Country in Captial:
    print(Captial[Country])
else: 
    print("The country is not in our list. Please try another")