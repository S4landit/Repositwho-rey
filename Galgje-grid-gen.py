WOORD = input("Wat is je woord?")
slang1 = "|"
slang2 = "|"
slang3 = "|"

Lengte = len(WOORD)

for x in range(Lengte):
    slang1 = slang1 + "-|"
    slang2 = slang2 + ".|"
    slang3 = slang3 + str(1 + x) + "|"
    
    
print(slang1)
print(slang2)
print(slang3)