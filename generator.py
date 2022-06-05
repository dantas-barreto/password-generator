import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
  length = int(input("quantidade de caracteres: "))
  random.shuffle(characters)
  password = []
  for i in range(lenght):
    password.append(random.choice(characters))
  random.shuffle(password)
  print("".join(password))
  
generate_random_password()
