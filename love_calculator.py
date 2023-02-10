
name1 = str(input("what is your name? "))
name2 = str(input("What is their name?"))

lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

t = lowercase_name1.count("t") + lowercase_name2.count("t")
r = lowercase_name1.count("r") + lowercase_name2.count("r")
u = lowercase_name1.count("u") + lowercase_name2.count("u")
e = lowercase_name1.count("e") + lowercase_name2.count("e")

first_digit = int(t + r + u + e) 

l = lowercase_name1.count("l") + lowercase_name2.count("l")
o = lowercase_name1.count("o") + lowercase_name2.count("o")
v = lowercase_name1.count("v") + lowercase_name2.count("v")
e = lowercase_name1.count("e") + lowercase_name2.count("e")

second_digit = int(l + o + v + e)

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >40) and (score < 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")