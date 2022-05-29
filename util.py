import requests
import getpass


def getdetails():
    # Získání údajů
    username = input("Uživatelské jméno: ")
    password = getpass.getpass(prompt="Heslo: ")
    bakaurl = input("Adresa školy (včetně protokolu, tedy ve formátu\"https://bakalari.tvojeskola.cz\": ")

    # Zapsání údajů
    f = open("prefs", "w")
    f.write(f'{username}\n{password}\n{bakaurl}')
    f.close()


def login(username, password, bakaurl):
    logindict = dict(username=username, password=password)

    r = requests.post(f"{bakaurl}/login", data=logindict)

    statuscode = r.status_code
    return statuscode
