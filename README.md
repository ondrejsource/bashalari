## Tento projekt teď není aktivní!
Snažil jsem se najít Linux distribuci, na které bych se cítil jako doma. Vyzkoušel jsem víc dister, než je zdravé, a po krátkém přesvědčení, že jsem našel perfektní distribuci (Fedora, něco jako openSUSE tumbleweed, ale u RHEL), jsem zjistil, že se mi nelíbí hodně věcí. 

1. **Non-free `dnf` repo není jednoduše dostupné** - mám moc rád open-source, ale možnost používat grafickou kartu na maximum, a tudíž možnost nainstalovat closed-sorce ovladače, by měla být jednoduše dostupná, třeba s varováním. Ubuntu to takhle má, ale Ubuntu má zase své nevýhody.
2. **`dnf` nemá jasné příkazy** - Například co má znamenat `distro-sync`? Ano, `dnf` má `manpage`, kde má být všechno napsané, ale `distro-sync` tam moc dobře popsané není.
3. **Fedora je nacpaná věcmi** - Možná až přecpaná. Zkoušel jsem jen Workstation flavour Fedory, protože žádný jiný by mi nejspíš nevyhovoval. Workstation edice má být nacpaná všemi možnými nástroji, které bych mohl potřebovat; A tak to také bylo. Ale bylo jich až moc. Já si radši nainstaluji potřebné programy sám, než abych strávil hodiny vytrháváním balíčků manuálně.

Tímto nechci říct, že Fedora je špatná. Je to asi to druhé nejlepší distro, které jsem kdy vyzkoušel. Na mé účely a preference se ale nehodí. Z mých zkušeností mám nejradši Arch Linux, na který se teď budu stěhovat zpátky. Raději 5 minut strávím instalací 20 balíčků, než 2 hodiny odinstalací 100 balíčků. Na Archi se cítím jako doma - velká většina uživatelů Arche má velmi podobné názory, jako já, a jsou velice aktivní na fórech. Když už jsem s nějakým problémem naprosto v koncích, většinou to trvá nejvýše 2 hodiny, než někdo odpoví, a já se mohu plácnout do čela, že jsem na to nepřišel sám. Proto se tedy vracím na Arch. Lidé, kteří slyšeli o Archi, a znám je osobně, říkají, že měli s Arch Linuxem spoustu problémů. Já jim říkám, že problém není v systému, ale v lidech samých.

[![Hits](https://hits.sh/github.com/ondrejsource/bashalari.svg?style=plastic&label=Hity&logo=python)](https://hits.sh/github.com/ondrejsource/bashalari/)  
# BaSHaláři - Klientská aplikace pro Bakaláře v Pythonu
Jako student druhého ročníku gymnázia, co nemá rád napjaté 2 minutové čekání na otevření aplikace Bakaláři jen abych zjistil, že hodina, která měla původně začínat za 20 minut
najednou začíná za 5 minut a je na druhé straně budovy jsem se rozhodl napsat toto - rychlého, velice odlehčeného klienta Bakalářů, který se dá používat nezávisle na platformě
a nenačítá a nestahuje data rychlostí mobilní sítě Edge.  
  
Klient je zatím v pre-alpha verzi. Není připravený k použití, není připravený k vykonávání svého účelu a nepodporuje rodiče ani učitele (U učitelů si nejsem jistý, jestli to má smysl
a jestli bych se vůbec dokázal dostat k učitelskému účtu)  
  
## Budoucnost projektu
BaSHaláři mohou jít po dokončení (tedy po implementaci všech potřebných funkcí) dvěma cestami:
* Zůstat jako Pythonový klient
* Zůstat jen jako jádro (nebo knihovna), kvůli navazujícímu projektu s krycím jménem "Light"
