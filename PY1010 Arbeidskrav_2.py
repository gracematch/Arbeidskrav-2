# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 16:38:27 2025

@author: grace
"""

# PY1010 ARBEIDSKRAV 2 


# OPPGAVE 1
"""
Du skal her lage et program som skal starter med alder = int(input('Hvilket år er du født? ') ).
Programmet skal så regne ut hvor gammel personen blir nå i løpet av år 2024 og skrive 
svaret til skjerm med passende tekst.
"""
# SVAR Oppgave 1:
alder = int(input('Hvilket år er du født? ') ) 
hvor_gammel = (2024 - alder)
print("I 2024 var du", hvor_gammel, "år gammel")



# OPPGAVE 2 
"""
Det skal arrangeres en klassefest og man antar at hver elev spiser 1/4 pizza. Lag et 
program som tar inn antall elever fra konsollen ved  
antall_elever = int(input('Skriv inn antall elever:' )) 
Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen og skrive 
svaret til skjerm. Merk, man kan ikke kjøpe 4 og en kvart pizza på butikken (man må da kjøpe 
5)
    
Hint1: Gir programmet ditt et fornuftig svar hvis det f.eks er 21 elever i klassen?  
Hint2: Det er ikke vanlig å si/skrive: ‘Det må handles inn 6.0 pizzaer til festen’. Hvordan kan 
sikre at antall pizzaer skrives ut som et heltall (ikke desimaltall)?
"""  
# SVAR Oppgave 2:
antall_elever = int(input('Skriv inn antall elever:' )) 
antall_pizzaer = (antall_elever / 4)
d2h = int(antall_pizzaer)
print("Det må handles inn", d2h, "pizzaer til festen")



# OPPGAVE 3
"""
Lag et program med en funksjon som regner om fra grader til radianer. 
Programmet skal starte med: import numpy as np  
v_grad = float(input('Skriv inn gradtallet:' )) 

Radiantallet til vinkelen regnes så ut ved følgende formel:  v_rad = v_grad*np.pi/180 
Resultatet v_rad skrives til skjerm med passende tekst og verdi.   
Merk: np.pi er en ferdiglaget funksjon som gir verdien 3.1415....
'"""
# SVAR Oppgave 3:
import numpy as np
def G2R(grad):
    rad = grad * np.pi / 180
    return rad
v_grad = float(input('Skriv inn gradtallet: '))
v_rad = G2R(v_grad)
print("Radianverdien er", v_rad)


# OPPGAVE 4
"""
a) Opprett en dictionary som gitt under. Dictionaryen har ulike land som nøkkel (Keys) 
og gir info om hovedstaden i landet og antall innbyggere i mill. i hovedstaden. 

b) Lag et program som ber brukeren skrive inn et land (eksempelvis England). 
Programmet skal på bakgrunn av dette skrive ut følgende setning: 
London er hovedstaden i England og det er 8.982 mill. innbyggere i London  

c) Lag et program som ber brukeren skrive inn info om et nytt land (altså et land som 
ikke allerede finnes i dictionaryen data). Videre skal brukeren oppgi hovedstad og 
antall innbyggere for det «nye» landet. Programmet skal så utvide/oppdatere 
dictionaryen med den nye informasjonen. Dictionaryen data skrives så til skjerm. 
"""

# SVAR Oppgave 4: 

  
# A
data = {
        "Norge": {"hovedstad": "Oslo", "innbyggere": 0.634},
        "England": {"hovedstad": "London", "innbyggere": 8.982},
        "Frankrike": {"hovedstad": "Paris", "innbyggere": 2.161},
        "Italia": {"hovedstad": "Roma", "innbyggere": 0.634}
        }


# B
be_om_land = input("Skriv inn et land: ")

# Bruk en boolsk variabel for å holde styr på om landet finnes
finnes = False

# Sjekk alle keys i dictionaryen
for land in data:
    if land == be_om_land:
        finnes = True
        hovedstad = data[land]["hovedstad"]
        innbyggere = data[land]["innbyggere"]
        break  # Vi fant landet, ingen grunn til å fortsette løkken

# Skriv ut resultatet basert på True / False
if finnes:
   print(f"{hovedstad} er hovedstaden i {be_om_land} og det er {innbyggere} mill. innbyggere i {hovedstad}")
else:
   print("Landet finnes ikke i databasen.")

# C
# Be brukeren skrive inn et nytt land
nytt_land = input("Skriv inn navnet på et nytt land: ")

# Sjekk om landet allerede finnes
if nytt_land in data:
    print(f"{nytt_land} finnes allerede i databasen.")
else:
    # Spør om hovedstad og innbyggere
   ny_hovedstad = input(f"Hva er hovedstaden i {nytt_land}? ")
   ny_innbyggere = float(input(f"Hvor mange millioner innbyggere har {nytt_land}? "))

    # Legg til det nye landet i dictionaryen
    data[nytt_land] = {"hovedstad": ny_hovedstad, "innbyggere": ny_innbyggere}

    print("\nOppdatert data:")
    for land, info in data.items():
       print(f"{land}: Hovedstad = {info['hovedstad']}, Innbyggere = {info['innbyggere']} mill.")


# OPPGAVE 5
"""Lag et program med en funksjon som tar a og b som inn-argumenter og som så 
regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant og en 
halvsirkel, se figuren under.  Med «ytre» omkrets menes samlet lengde av de sorte strekene. 
Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med passende 
tekst."""

#SVAR OPPGAVE 5
import math

def figur(a, b):
    # Areal
    areal_trekant = (a * b) / 2
    radius = b / 2
    areal_halvsirkel = (math.pi * radius**2) / 2
    areal = areal_trekant + areal_halvsirkel

    # Ytre omkrets
    hypotenus = math.sqrt(a**2 + b**2)
    omkrets = a + hypotenus + math.pi * radius  # katet a + hypotenus + halvsirkelbue

    return areal, omkrets

# Input fra bruker
a = float(input("Skriv inn a: "))
b = float(input("Skriv inn b: "))

areal, omkrets = figur(a, b)

print(f"Arealet til figuren er {areal:.3f}")
print(f"Ytre omkrets er {omkrets:.3f}")



# OPPGAVE 6
"""Skriv en kode som plotter funksjonen 𝑓(𝑥) = −𝑥2 − 5, for x på intervallet [-10,10]. 
Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet         
[-10,10]. """

# SVAR OPPGAVE 6
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 200)
y = -x**2 - 5

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot av f(x) = -x^2 - 5")
plt.grid(True)  # Valgfritt: legger til rutenett for bedre oversikt
plt.show()


