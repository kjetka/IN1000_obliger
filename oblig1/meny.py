# Hovedretter

hovedretter_dyr = ["kylling", "laks"]
hovedretter_veg = ["linsegryte"]

# Tilbehør - grønnsak
tilbehør_grønnsaker = ["gulrøtter"]
# Tilbehør - saus
tilbehør_saus = ["peppersaus"]

#######################################
# Printe menyen
print("Velkommen!")
print("Her er dagens meny: ")
print(" Hovedretter: ")
print("\t",hovedretter_dyr)
print("\t",hovedretter_veg)


print(" Tilbehør: ")
print("\t Grønnsaker: \n\t\t", tilbehør_grønnsaker)
print("\t saus: \n\t\t", tilbehør_saus)

#########################################
# Oppgave2 - interaksjon kunde
print(" ")
bestilling_hoved = input("Hvilken hovedrett vil du ha? ").lower()
bestilling_tilbehør = input("Hva vil du ha som tilbehør? ").lower()

# bestilling_string
bestilling_string = "Du har valg "+ bestilling_hoved +" med " + bestilling_tilbehør
###########################################
# Oppgave3 - anbefalinger til kunden

#Warning - spis grønnsaker!
if bestilling_tilbehør not in tilbehør_grønnsaker:
    print("Du spiser ikke nok grønnsaker!")

# Vegetar eller kjøtt + grønt
if bestilling_hoved in hovedretter_veg or bestilling_hoved in hovedretter_dyr:

    if bestilling_hoved in hovedretter_veg:
        if  bestilling_tilbehør in tilbehør_grønnsaker:
            print("Du har valgt et vegetarmåltid. Så bra!")
        else:
            print(bestilling_string)

    else: # mao: bestilling er kjøtt
        if  bestilling_tilbehør  in tilbehør_grønnsaker:
            print(bestilling_string)

else: 
    print("Bestillte du en hovedrett fra menyen?")


