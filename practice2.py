print("1-sign up""\n2-enter \ sign in ""\n3-exit")
entry=int(input("enter any option :"))
if entry ==1 :
    user_name=input("enter your username:")
    password=input(" enter your password ""\t (plese just enter letter): ")
    address=input("please enter your address:")
    if len(password)!=8 and type(password)==int:
      print("plese enter correct password!") 
elif entry==2:
    user_name2=input("enter your username")
    password2=input("plese enter your password:")
    if len(password2)!=8 and type(password2)==int:
       print("plese enter correct password!")   
elif entry==3:
    print("goodbye......")
else:
    print("plese enter correct option!")