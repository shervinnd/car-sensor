start_massege=input("are you ready for doz (yes/no): ")
if start_massege=="yes":
  menu="\n 1  2  3 \n 4  5  6 \n 7  8  9 "
  print(menu)
  print("\nnow !!")
  name_player1=input("enter first player name : ")
  name_player2=input("enter the seconde player name : ")
  first_input=(input(" enter your num " + name_player1 + " (1...9): "))
  if first_input=="1": 
    print(menu.replace("1","#"))
    second_input=(input("enter your num "+ name_player2 +":"))
    if second_input =="2":
      print(menu.replace("2","*"))
      third_input=input("enter your num " +name_player1+":" )
      if third_input=="3":
       print(menu.replace("3","#"))



elif start_massege=="no":
  print ("good bye!!")
else:
  print("enter right option!")

