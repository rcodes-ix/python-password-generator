# PyPassword Generator

import random
import json

found = False

def save_json(data, filename = "PyPasswordG.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_json(filename="PyPasswordG.json"):
        try:
            with open(filename, "r")  as f:
                return json.load(f) 
        except FileNotFoundError:
            return { }

def generate():
            app_name = input("For what platform do you want me to generate password?\n").lower()
           
            nr_letters = int(input("How many letters would you like in your password?\n"))
            nr_symbols = int(input(f"How many symbols would you like?\n"))
            nr_numbers = int(input(f"How many numbers would you like?\n"))
                
            l = random.sample(letters, k=nr_letters)
            s = random.sample(symbols, k=nr_symbols)
            n = random.sample(numbers, k=nr_numbers)
                
                
            random_password = l + s + n
                
            random.shuffle(random_password)
                
            result = "".join(random_password)
        
            new_entry = {
                    "platform": app_name,
                    "password": result
            }
            passwords = passG.get("generated_passwords",[])
                
               
            passwords.append(new_entry)   
            passG["generated_passwords"] = passwords
                
           
               
            print(f"Here is your password: {result}") 
                
                   

def show():
        found = False
        
        show = input("Which platform's?\n").lower()
        
        for platform in passG["generated_passwords"]:
            if platform["platform"] == show:
                print("password: ",platform["password"])
                found = True
        if not found:
            print("Not found.")      
                           
passG = load_json()


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")

while True:

    ask = input("""
Do you want to:
   1, Generate
   2, Show
""")
    
    if ask == "1":
        generate()
        save_json(passG)
         
    elif ask == "2":
        show()
   
    if ask not in ["1","2"]:
        print("Error, Type only 1 or 2.")
       
   
    last = input("\nContinue or Exit?\n").lower()
    if last =="continue":
        continue
    elif last == "exit":
        break
    else:
        print("Invalid Input.")
        break
      