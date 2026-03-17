# 1- import the random module
import random

# 2- create subjects

subjects=[
    "Shahrukkhan",
    "virat kohli",
    "Nirmala sitaraman",
    "A Mumbai cat",
    "A Group of monkeys",
    "Prime Minister Modi",
    "Auto rickshaw driver from delhi"
]

actions = [
    "launches",
    "cancels",
    "dance with",
    "eats",
    "declare war on",
    "orders",
    "celebrates"
]

places_or_things=[
    "at red fort",
    "in Mumbai local train",
    "a playes"
    "playes"
    "plate of samosa",
    "inside of parliament",
    "at ganga ghat",
    "during IPL Match",
    "at Indian Gate"
]

## 3 start the headline generation loop
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(places_or_things)
    headline=f"Breaking News: {subject} {action} {place_or_thing}"
    print("\n"+headline)

    user_input=input("\n Do you want another headline ? (yes/no)").strip().lower()
    if user_input == "no":
        break

    #print goodbye message
    print("\n"+headline)
