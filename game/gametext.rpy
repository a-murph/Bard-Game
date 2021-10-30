label c1_gametext:
    window show
    MC "When my fingers begin to pluck the strings, something strange happens."
    MC "A blue glow begins to emit from my fingertips, and it envelops my hands. The mandolin pulses with every note I play."
    MC "What is this?"
    Goon "What the hell is this? Is this some kind of - OUGH!"
    #play sound magic_burst
    Mage "What is this? I'm stronger."
    Ranger "And my arrows fly faster!"
    Fighter "What's that music?"
    Mage "Music...?"
    N "She looks over to me, and her face lights up with realization."
    Mage "That's it! Keep playing, bard!"
    MC "O-Okay!"
    N "My playing appears to be making them stronger. Is this some kind of magic?"
    window hide
    pause 1000

label c1_gamefail:
    if (lives == 2):
        window show
        Ranger "Agh!{p=0.5}{nw}"
        MC "I can't mess up that many times in a row. Their lives depend on it!{p=0.5}{nw}"
        Fighter "Keep going!{p=0.5}{nw}"
        window hide
        pause 1000
    elif (lives == 1):
        window show
        Mage "AGH!{p=0.5}{nw}"
        Fighter "EUGH!{p=0.5}{nw}"
        MC "Shit, I did it again and they got hit. If I make a mistake like that again they'll get killed!{p=0.5}{nw}"
        window hide
        pause 1000
    elif (lives <= 0):
        return #TODO: Figure out retry button, and showing the girls losing