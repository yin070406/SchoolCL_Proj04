tempature = float(input("The tempature right now? "))

if tempature >= 30:
    print("Can i stay home?")
elif tempature >= 25:
    print("Hot")
elif tempature >= 20:
    print("Not too cold, Not too hot")
elif tempature >= 10:
    print("Kinda Cold")
else: 
    print("JUSY LET ME STAY IN MY BED")

print(f"Tempature: {tempature}")