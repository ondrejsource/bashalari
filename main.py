# BaSHaláři - klientská aplikace Bakalářů napsaná v Pythonu

import os
import requests
import util


folder = os.listdir()
if "prefs" in folder:
    pass
else:
    print("Vítejte v BaSHalářích. Vypadá to, že toto je první spuštění. Zadejte, prosím, své údaje.")
    util.getdetails()

f = open("prefs", "r")

returncode = util.login(f.readline(1), f.readline(2), f.readline(3))