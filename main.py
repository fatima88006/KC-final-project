print(f"SignUp whith your email:")

class Username:
    email = "fatima@gmail.com"
    email_password = "08"
    username = "fatima006"
    password = "006"  

    emailInput = input("What is your email\n")
    
    if emailInput == email:
        a=input("Email Password?\n")
        if a == email_password:
            print("SignUp with your username:\n")
        else:
            print("That is wrong password.")
    else:
        print("That is the wrong email.")

    userInput = input("What is your username?\n")

    if userInput == username:
        a=input("Password?\n")
        if a == password:
            print("Welcome!\n")
        else:
            print("That is wrong password.")
    else:
        print("That is the wrong username.")

Clothes = [{
            "taype" : "hoodie",
            "color" : "black,white,gray",
            "season" : "summer,winter" ,
    }, { 
            "taype" : "jacket",
            "color" : "black,white,gray",
            "season" : "summer,winter",
}]

print(Clothes)

print(f"Hi senior you can start order your Hoodie or jacket:")

def shopping(order):
    if order == "hoodie":
        return 0
    elif order == "jacket":
        return 0

def sleeve(season):
    if season == "summer":
        return 0
    elif season == "winter":
        return 0

def top(color):
    if color == "black":
        return 0
    elif color == "white":
        return 0
    elif color == "gray":
        return 0

def pieces(num):
    if num == 1:
        return 0
    elif num == 2:
        return 20
    elif num == 2:
        return 40
    elif num == 3:
        return 60
    elif num == 4:
        return 80
    elif num == 5:
        return 100
    

def shippment(receive):
    if receive == "delivery":
     return 2
    elif receive == "pick up":
     return 0
   

def price():
    order = (input("hoodie or jacket?"))
    material = print(input("Chose the material: \n summer \n winter \n"))
    color = input("Which color do want? \n white \n black \n gray \n")
    writing = input("What do you want to write?" )
    num = int(input("How many pieces do want(1/2/3/4/5)?"))
    receive = (input("delivery or pick up:"))
    paytment = (input("How do you want to pay: \n cash \n kent \n visa \n"))
    
    
    total_cost = shopping(order) + pieces(num) + shippment(receive)
    
    print(f"order: {order}\nnum: {num}\nrecive: {receive}")
    return total_cost

total_price = price()
print(f"totle price is: {total_price} KD")

print(f"Thank you for shopping is our store we hope you enjoy:)")
