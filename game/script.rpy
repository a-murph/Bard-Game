# The script of the game goes in this file.
init python:
    ## Class object for setting pronouns and using them in dialogue
    class Pronoun:
        def __init__(self, gender):
            if (gender == "m"):
                self.subj = "he"
                self.obj = "him"
                self.adj = "his"
                self.poss = "his"
                self.reflex = "himself"
                self.contract = "he's"
                self.subjCap = "He"
                self.objCap = "Him"
                self.adjCap = "His"
                self.possCap = "His"
                self.reflexCap = "Himself"
                self.contractCap = "He's"
            if (gender == "f"):
                self.subj = "she"
                self.obj = "her"
                self.adj = "her"
                self.poss = "hers"
                self.reflex = "herself"
                self.contract = "she's"
                self.subjCap = "She"
                self.objCap = "Her"
                self.adjCap = "Her"
                self.possCap = "Hers"
                self.reflexCap = "Herself"
                self.contractCap = "She's"
            if (gender == "x"):
                self.subj = "they"
                self.obj = "them"
                self.adj = "their"
                self.poss = "theirs"
                self.reflex = "themself"
                self.contract = "they're"
                self.subjCap = "They"
                self.objCap = "Them"
                self.adjCap = "Their"
                self.possCap = "Theirs"
                self.reflexCap = "Themself"
                self.contractCap = "They're"

    ## Class object for tracking relationship points with each girl
    class Relationship:
        def __init__(self):
            self.emma = 0
            self.mae = 0
            self.gale = 0
            self.var = 0
            self.chi = 0
            self.kaz = 0
            self.aldo = 0
            self.sil = 0
            self.ala = 1

        def bestGirl(self):
            import random
            girls = {
                "emma": self.emma,
                "mae": self.mae,
                "gale": self.gale,
                "var": self.var,
                "chi": self.chi,
                "kaz": self.kaz,
                "aldo": self.aldo,
                "sil": self.sil,
                "ala": self.ala
            }
            highest = max(girls, key=girls.get)

            tied = []
            for key in girls:
                if girls[key] == girls[highest]:
                    tied.append(key)

            highest = random.choice(tied)

            return highest

    ## Defining additional audio channels
    renpy.music.register_channel("ambience", mixer="ambience", loop=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("bgSound", mixer="ambience", loop=True, tight=True, buffer_queue=True)

    def showMC(location=[], isInjured=False):
        if (legs == "m"):
            if (isInjured):
                renpy.show("mcmlegs injured", at_list=location)
            else:
                renpy.show("mcmlegs", at_list=location)
        if (legs == "f"):
            if (isInjured):
                renpy.show("mcflegs injured", at_list=location)
            else:
                renpy.show("mcflegs", at_list=location)

        if (torso == "m"):
            if (isInjured):
                renpy.show("mcmtorso injured", at_list=location)
            else:
                renpy.show("mcmtorso", at_list=location)
        if (torso == "f"):
            if (isInjured):
                renpy.show("mcftorso injured", at_list=location)
            else:
                renpy.show("mcftorso", at_list=location)

        if (head == "m"):
            if (isInjured):
                renpy.show("mcmhead injured", at_list=location)
            else:
                renpy.show("mcmhead", at_list=location)
        if (head == "f"):
            if (isInjured):
                renpy.show("mcfhead injured", at_list=location)
            else:
                renpy.show("mcfhead", at_list=location)

    def hideMC():
        renpy.hide("mcmhead")
        renpy.hide("mcmtorso")
        renpy.hide("mcmlegs")
        renpy.hide("mcfhead")
        renpy.hide("mcftorso")
        renpy.hide("mcflegs")

# Main Character (Default name: Ashton Moon)
define MCNameless = Character("")
define N = Character("", what_italic=True)
define MC = Character("[firstName] [lastName]")
default firstName = "Ashton"
default lastName = "Moon"
default relationship = Relationship()

# Main party members (TODO: Pick colors for each character)
define Emma = Character("Emmaline Lightheart")
define Fighter = Character("Armored Girl")

define Mae = Character("Mae Faeleigh")
define Mage = Character("Frilly Girl")

define Gale = Character("Gale Farrowthorn")
define Ranger = Character("Slender Girl")

define Var = Character("Varna Northwind")
define Barbarian = Character("Large Woman")

define Chi = Character("Chiyo")

define Kaz = Character("Kaz Freehold")
define KazFirst = Character("Kaz")
define Monk = Character("Laid-Back Girl")

define Aldo = Character("Aldona Fortwright")
define AldoFirst = Character("Aldona")
define Paladin = Character("White-Haired Woman")

define Sil = Character("Silver")

define Ala = Character("Alarice Peigne")
define AlaFirst = Character("Alarice")
define Warlock = Character("Horned Woman")

# Minor characters
define Derk = Character("Derk Longston")
define ShopOwner = Character("Shop Owner")
define StallOwner = Character("Stall Owner")
define Jo = Character("Jo")
define SternMan = Character("Stern Man")
define MLK = Character("Mary Lynn Kearne")
define Innkeep = Character("Middle-Aged Woman")

# Antagonists
define Goon = Character("Golden Scales Goon")

# The game starts here.

label start:
    #TODO: GUI for character customization
    "Which head would you like to use?"
    menu:
        "Masculine":
            python:
                head = "m"
        "Feminine":
            python:
                head = "f"

    "Which torso would you like to use?"
    menu:
        "Masculine":
            python:
                torso = "m"
        "Feminine":
            python:
                torso = "f"

    "Which legs would you like to use?"
    menu:
        "Masculine":
            python:
                legs = "m"
        "Feminine":
            python:
                legs = "f"

    "Which pronouns would you like to use?"
    menu:
        "He/Him":
            python:
                pronoun = Pronoun("m")
        "She/Her":
            python:
                pronoun = Pronoun("f")
        "They/Them":
            python:
                pronoun = Pronoun("x")

    jump chapter1