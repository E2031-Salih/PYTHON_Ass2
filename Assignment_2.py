age = bool(input("Are you a cigarette addict older than 75 years old? (Yes or No) :").title() == "Yes")
chronic = bool(input("Do you have a severe chronic disease? (Yes or No) :").title() == "Yes")
immune = bool(input("Is your immune system too weak? (Yes or No) :").title() == "Yes")
risk = age or chronic or immune
if risk:
    print("You are in risky group")
else:
    print("You are not in risky group")
