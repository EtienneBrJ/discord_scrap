#!/usr/bin/python3
""" Caisse calculator """
import time


caisse_un = int(input("Total de la caisse BAR 1: "))
caisse_deux = int(input("Total de la caisse BAR 2: "))
caisse_trois = int(input("Total de la caisse BAR 3: "))
caisse_rose = int(input("Total de la caisse BAR ROSE: "))
caisse_snow = int(input("Total de la caisse SNOWMELT: "))

total_caisses = caisse_un + caisse_deux + caisse_trois + caisse_rose + caisse_snow

print("Le montant total des caisses est " + str(total_caisses) + " €")
print()

TPE1_BAR1 = int(input("Total TPE 1 du BAR 1 : "))
TPE2_BAR1 = int(input("Total TPE 2 du BAR 1 : "))
TPE1_BAR2 = int(input("Total TPE 1 du BAR 2 : "))
TPE2_BAR2 = int(input("Total TPE 2 du BAR 2 : "))
TPE1_BAR3 = int(input("Total TPE 1 du BAR 3 : "))
TPE2_BAR3 = int(input("Total TPE 2 du BAR 3 : "))
TPE_ROSE = int(input("Total TPE du BAR ROSE : "))
TPE_SNOW = int(input("Total TPE du BAR SNOW : "))

total_tpe = TPE_SNOW + TPE_ROSE + TPE2_BAR3 + TPE1_BAR3 + TPE2_BAR2 + TPE1_BAR2 + TPE2_BAR1 + TPE1_BAR1

print("Le montant total des caisses est " + str(total_tpe) + " €")
print()

trou = total_tpe - total_caisses
if trou > 0:
    print("Tu as un trou de " + str(trou) + " € ")
    print()
    print("Tu dois donc taper " + str(trou) + " € sur la caisse")
elif trou == 0:
    print("C'est carré")
else:
    print("Trop tapé sur la caisse")