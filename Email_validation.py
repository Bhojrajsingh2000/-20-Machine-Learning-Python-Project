k,j,d=0,0,0
while True:
    print("\n================================")
    email=input('Enter Your Email Address : ')
    if len(email)>=6:
        if email[0].isalpha():
            if('@'in email) and (email.count('@')==1):
                if(email[-4]=='.')^(email[-3]=='.'):
                    for i in email:
                        if i==i.isspace():
                            k=1
                        elif i.isalpha():
                            if i==i.upper():
                                j=1
                        elif i.isdigit():
                            continue
                        elif i=="_" or i=="." or i=="@":
                            continue
                        else:
                            d=1
                    if k==1 or j==1 or d==1:
                        print("Email Invalid because have a Space ,upper case character")
                    else:
                        print("Email Valid")
                        print("\n================================================================")
                        break
                else:
                    print("Dot(.) have not contain right portion")
            else:
                print("Email have no @ Symbols")
        else:
            print("Email should not start with alphabet")
    else:
        print("Email have not min 6 characters")