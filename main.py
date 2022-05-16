import getpass
import os
import requests
import sys


def testlogin(username, password):
    payload = dict(username=username, password=password)

    testrequest = requests.post("https://bakalari.ceskolipska.cz/Login", data=payload)

    return testrequest.status_code


def getlogin():
    print("Zadej své přihlašovací údaje (tvé údaje nejsou ukládány mimo tento počítač a nejsou posílány mimo "
          "Bakaláře:")

    username = getpass.getuser(prompt="Uživatelské jméno: ")
    password = getpass.getpass(prompt="Heslo: ")

    if testlogin(username, password) == 200:
        print("Správné údaje, zapisuji do souboru...")
        writelogin(username, password)
        print("Zápis dokončen.")
    else:
        retry = input("Nesprávné údaje. Zkusit znovu? [y/n]")
        if retry == "y".lower():
            getlogin()
        else:
            sys.exit()


def writelogin(username, password):
    loginfilewrite.write(f"{username}\n{password}")


# >> Zde začíná hlavní kód:
folder = os.listdir()

loginfile = open("loginfile", "r")
loginfilewrite = open("loginfile", "w")

if "loginfile" in folder:
    fileexists = input("Soubor pro přihlašovací údaje byl nalezen. Co s ním chcete dělat? [Přepsat/Vypsat obsah/Nic, "
                       "přihlásit se do Bakalářů]")
    if fileexists.lower() == "v":
        print(f"Vypisuji obsah souboru s přihlašovacími údaji: {loginfile.read()}")
    elif fileexists.lower() == "p":
        print("Přepisuji soubor pro přihlašovací údaje.")
        getlogin()
    elif fileexists.lower() == "n":
        print(f"Přihlášení vrátilo HTTP kód {testlogin(loginfile.readline(1), loginfile.readline(2))}")
else:
    print("Soubor pro přihlašovací údaje nebyl nalezen, vytvářím ho...")
    loginfile.write("<Toto je jen placeholder. Pokud jste ještě nezadával(a) přihlašovací údaje do Bakalářů, "
                    "něco je špatně.>")
    print("Hotovo.")
    getlogin()
