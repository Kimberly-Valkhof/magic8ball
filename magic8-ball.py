import random
name = ""
question = "Will i become filthy rich by the end of the year?"
answer = ""
random_number = random.randint(1,11)
#print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
  
elif random_number == 2:
  answer = "It is decidedly so"
  
elif random_number == 3:
  answer = "Without a doubt"
  
elif random_number == 4:
  answer = "Reply hazy, try again"
  
elif random_number == 5:
  answer = "Ask again later"
  
elif random_number == 6:
  answer = "Better not tell you now"
  
elif random_number == 7:
  answer = "My sources say no"
  
elif random_number == 8: 
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Babe think about this one yourself"
elif random_number == 11:
  answer = "I love this for you, yes!"
else:
 answer = "Error!"

if name == "":
  print("Question:", question)
else:
  print(name, "asks:", question)

if question == "":
  print("you have comprimised the fabric of reality")
else:
  print("Magic 8-Ball's answer:", answer)
