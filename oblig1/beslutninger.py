quest = "Vil du ha brus? "
ans = input(quest).lower()


if ans == "ja":
    print("Her har du en brus!")
elif ans=="nei":
    print("Den er grei")
else: 
    print("Det forstod jeg ikke helt")

