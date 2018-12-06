uur = int(input("Wat uur is het? "))
minuten = int(input("Hoeveel minuten zijn er uit dat uur al gepasseerd? "))
graden_tussen_uur = 30
graden_tussen_minuten = 6
while uur < 0 or uur > 24 or minuten < 0 or minuten > 59:
   uur: int = int(input("Wat uur is het? "))
   minuten = int(input("Hoeveel minuten zijn er uit dat uur al gepasseerd? "))
## grote wijzer berekening
if minuten <= 15:
   graden_grote_wijzer = (15 - minuten) * graden_tussen_minuten
elif minuten > 15 and minuten <= 60:
   graden_grote_wijzer = 90 + ((60 - minuten) * graden_tussen_minuten)
## kleine wijzer berekening
if uur <= 3:
   graden_kleine_wijzer = (3 - uur) * graden_tussen_uur - (minuten * 0.5)
elif uur > 3 and uur < 12:
   graden_kleine_wijzer = 90 + ((12 - uur) * graden_tussen_uur) + (minuten * 0.5)
elif uur <=15 and uur >= 12:
   graden_kleine_wijzer =((3 - (uur - 12)) * graden_tussen_uur) - ( minuten * 0.5)
elif uur > 15:
   graden_kleine_wijzer = 90 + ((12 - (uur - 12)) * graden_tussen_uur) + (minuten * 0.5)
print(float(graden_kleine_wijzer))
print(float(graden_grote_wijzer))