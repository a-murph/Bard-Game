label chapter1:
    # scene black
    # play sound rock_show
    # pause 10
    
    # scene cg stage
    # pause 8
    # scene cg audience
    # pause 8
    # scene cg guitarist
    # pause 12

    # scene black
    # pause 7

    # stop sound
    play movie "video/intro_scene.webm"
    
    scene cg dorian face
    MCNameless "Where...?"

    # -----------------------------------------------------------------------------------------------------
    label chapter1_scene1:
        scene bg mulberry square
        #play ambience mulberry_square_ambient
        N "I thought that I was in the middle of my band's first performance as the headliner, but then I suddenly opened my eyes to find myself in what appears to be a medieval village."
        MCNameless "Am I... having a mental breakdown?"

        scene cg dorian hands
        N "I look down at my hands, and they still look like the hands I know very well. Still the same fingers that I know how to strum with."
        N "That familiar freckle just above the right index knuckle has never been so assuring."

        scene bg mulberry square
        MCNameless "There's no way this is here, though... maybe I fell on stage and hit my head?"
        N "I walk out into the center of the town square. The busy sounds and chatter of the townspeople going about their day surround me."
        N "The chatting of housewives, the clattering and shouting of large men loading and unloading crates, the clopping of hooves as carriages roll by."
        N "I approach one of the shop stands and peer at the merchandise."
        N "The table is covered in intricately stacked hand-sculpted plates and bowls, carved wooden trinkets, and leatherware with chunky, methodical stitching."
        N "Picking up one of the leather satchels, I turn it around in my hands. It feels just as soft and real as my own skin."
        
        python:
            showMC([left])
        show mc concerned at left
        MCNameless "This is crazy..."

        show stallownerbody at right
        show stallowner annoyed at right
        StallOwner "Can I help you?"

        show mc surprised
        MCNameless "Oh- no, sorry!"
        N "Realizing what a weirdo I must look like, I put down the bag and quickly begin to walk away."

        show stallowner neutral
        StallOwner "Hey! Are you a musician?"
        N "This question catches me slightly off-guard. I turn around."
        MCNameless "How did you know?"
        StallOwner "Well, cause you've got that instrument on your back!"
        MCNameless "What?"
        N "I twist my neck around to no avail, and then stretch my arms up and around my back to feel my hands bump against hard polished wood."
        N "I reach higher and feel the neck of a stringed instrument, and lift it out of its holster and pull it in front of me."

        scene cg dorian mandolin
        N "It's a mandolin."
        N "A finely-carved, teardrop-shaped body with a lovely burnt umber wood. I've seen these online, but never actually in person."
        play sound mandolin_tuning
        N "I wonder how it's tuned..."

        scene bg mulberry square
        python:
            showMC([left])
        show mc neutral at left
        show stallownerbody at right
        show stallowner neutral at right
        MCNameless "Interesting..."
        StallOwner "Well hey, how about this: if you can play me a nice little song, I'll give you a discount on that bag you were admiring earlier?"
        MCNameless "Umm..."
        
        show mc concerned
        N "I look down to the frets and feel intimidated."
        N "I try placing my fingers as best I can in a few relatively familiar chords and then strum."
        play sound discordant_mandolin
        pause 2
        MCNameless "This is nothing like guitar..."

        show stallowner concerned
        StallOwner "Are you sure you're okay?"

        show mc embarrassed
        MCNameless "Yeah... I just might have hit my head earlier."
        StallOwner "Oh..."
        play sound fast_walk_foot_steps_on_rock
        N "Before the old lady could get in another word, I turn and quickly walk away."
        N "God, that was embarrassing."

    # -----------------------------------------------------------------------------------------------------
    label chapter1_scene2:
        scene bg mulberry street #sunset
        play ambience ambience_town_day
        N "I wander through the streets of the town, trying to get my bearings on where exactly I am without drawing too much attention towards myself again."
        N "I've figured out that the name of the town I'm in is Mulberry Town, named for the plethora of mulberry trees in the valley it was settled in, but that's about it."
        python:
            showMC()
        show mc tired
        MCNameless "{i}*sigh*{/i}"
        MCNameless "How do I get out of this place?"
        show mc surprised
        play sound stomach_rumbling_1
        MCNameless "...?!"
        show mc tired
        MCNameless "Oh..."
        python:
            hideMC()
        hide mc
        N "I guess I'm going to have to figure out some way to make money after all.{p}Even in a fever dream, I can't escape it."
        N "I think of all the townsfolk I saw dealing in the square. I don't have nearly enough muscle to be hauling crates as big as those guys."
        N "I also don't have any crafting skills to make wares, and if I had the startup capital to be buying wares to trade, I wouldn't be in this situation."
        N "As my mind goes over the options, it eventually trails to the wooden instrument on my back."
        python:
            showMC()
        show mc tired
        MCNameless "Well, it's been a while since I've had to busk..."
        MCNameless "But I'm sure I can figure out the mandolin faster than I can put on pounds of muscle."
        play sound normal_walk_foot_steps_on_rock
        #TODO: Figure out how to make ongoing street ambience quieter here
        python:
            hideMC()
        hide mc
        N "I pull myself into an alleyway and sit for a while while I play around with my new instrument, figuring out how it translates to the stringed instruments I've played before."
        python:
            showMC()
        show mc neutral
        MCNameless "Oh, I see... it's like the lowest four strings of a guitar - but reversed!"
        python:
            hideMC()
        hide mc
        #play sound mandolin_noodling_1
        N "I spend the evening playing around with the instrument, getting lost in feeling my way around the fretboard, strumming out old tunes that I used to play."
        
        scene bg mulberry street #night
        play ambience ambience_town_night
        #play sound mandolin_noodling_2
        N "I get so lost in playing with the new instrument that I forget completely about my hunger, and eventually doze off sitting in the alleyway with the mandolin resting on my lap."
        
        scene bg mulberry street #day
        play ambience ambience_town_day volume 0.5
        play sound carriage_wheel_bump
        N "I awake to the sound of a carriage bumping loudly against a bump in the road."
        N "I look around to see that it is day, and the town is bustling again."
        python:
            showMC()
        show mc neutral
        MCNameless "Looks like I'm still here..."
        play sound stomach_rumbling_2
        pause 2
        MCNameless "Right! I gotta earn some money!"
        python:
            hideMC()
        hide mc
        N "I exit out onto the street. There are a decent amount of people going by, but not quite as large of a crowd as yesterday."
        #TODO: figure out how to make ongoing street ambience louder here
        N "I set up shop, so to speak, and begin playing what I practiced last night."
        play sound busking
        N "The crowd walking by begins to take note of me as I play on the side of the cobblestone road."
        N "Some look with an expression of mild curiosity, but others look with an expression of concern and alarm and move a bit quicker as they continue on their way."
        python:
            showMC()
        show mc thinking
        MCNameless "That's unusual."
        python:
            hideMC()
        hide mc
        N "I continue to play and get similar reactions from the people going down the road. Nobody approaches, or even places a hand on their coin pouch like they're considering giving money."
        python:
            showMC()
        show mc sad
        MCNameless "Maybe there isn't a concept of street performance in this world."
        play sound shop_door_open_bell
        python:
            hideMC()
        hide mc
        N "A small bell rings as the shop door of the building next to me swings open. A gruff-looking man sticks his head out of the door and frantically looks around before finding me."
        
        python:
            showMC([left])
        show mc scared at left
        show derkbody at right
        show derk angry at right
        play music music_antics
        ShopOwner "Hey! What do you think you're doing, you're driving away all my customers!"
        MCNameless "I'm sorry! Was it that bad?"
        ShopOwner "Well-"
        show derk thinking
        ShopOwner "I mean no, it sounds kind of nice..."
        show derk angry
        ShopOwner "But - Do you have a street merchant license?"
        MCNameless "I need a license?!"
        ShopOwner "Well of course you need a license if you-"
        show derk thinking
        ShopOwner "... you must not be from around here, are you?"
        show mc nervous
        MCNameless "Well, no... I'm a traveler and I was just-"
        play sound stomach_rumbling_1
        MCNameless "..."
        show derk angry
        ShopOwner "..."
        show derk thinking
        ShopOwner "I see."
        show derk neutral
        ShopOwner "Listen. How about you come inside my shop and we can talk?"
        ShopOwner "You're going to get us both in trouble if you keep making a ruckus out here."
        show mc happy
        MCNameless "O-Okay!"

    # -----------------------------------------------------------------------------------------------------
    label chapter1_scene3:
        scene bg mulberry shop
        stop music
        play sound shop_door_open_bell
        queue sound shop_door_close_bell
        pause 2
        play music music_cozy_place
        play ambience ambience_fireplace
        N "I follow the man into his shop as the door bell rings closed behind us. We are in what appears to be a small general store."
        N "I look around at the variety of supplies up on the shelves around the room."
        N "Everything from hefty adventuring rations to little carved knick-knacks. It's like the medieval equivalent of a convenience store."
        python:
            showMC([left])
        show mc neutral at left
        show derkbody at right
        show derk sorry at right
        ShopOwner "Sorry about the gruffness, it's just - if the Golden Scales caught wind of that - I think you would also get in trouble since you were outside my shop, and I don't think they'd take too kindly to someone like you."
        show mc thinking
        MCNameless "Someone like me?"
        show derk neutral
        ShopOwner "Yeah. They don't like outsiders."
        ShopOwner "They tend to keep a pretty tight lid on operations around here - especially when it comes to people making money."
        MCNameless "Is that why no one was giving me any coins?"
        ShopOwner "Likely. Most people around here are selling goods, not begging.{p}No offense."
        N "I did feel a little offended, but I understood his point."
        N "I don't know anything about the culture of this place. I could have easily run into trouble blindly."
        MCNameless "There was another shop owner that said she was interested in trading for some of my music."
        show derk amused
        ShopOwner "She was probably just trying to be nice."
        show mc sad
        MCNameless ""
        ShopOwner ""
        show derk neutral
        ShopOwner "Anyhow, you can stay here for the night to stay out of trouble with the Golden Scales."
        ShopOwner "I'm not a cook, but I can give you some packaged rations."
        show mc happy
        MCNameless "Thank you!"
        show mc thinking
        MCNameless "What's the deal with the Golden Scales, exactly?"

        stop music fadeout 2.0
        N "The shop owner's expression turns even more serious than he had looked before."
        N "His brow furrowing even deeper, he doesn't look like he's glaring at me, but at an enemy that is off in the distance."
        show derk glaring
        ShopOwner "Between you and me, they're a bunch of bastards."
        ShopOwner "They're a gang of thugs that got too full of themselves, and now they think they deserve to rule over the entire country."
        ShopOwner "They've been taking over town after town and lording over them with an iron fist, and this town was one of the most recent additions to their \"kingdom\"."
        show mc solemn
        MCNameless "I see..."
        show derk neutral
        ShopOwner "You'd do your best to get out of here as quickly as you can and get someplace a little safer."
        ShopOwner "As much as I pray that this town will someday be released from their grip, I don't expect that to be any day soon."
        ShopOwner "The only thing is that since they have a tight lock on the place, getting out is a little difficult."
        ShopOwner "They have guards posted and regulating what goes in and out of every gate. I'm honestly surprised you made it in here."
        show mc nervous
        MCNameless "Quite honestly, I'm not really sure how I got in here, either."
        N "The shop owner raises an eyebrow at that statement."
        ShopOwner "You don't know?"
        MCNameless "I mean - I don't really remember anything. It was all kind of black and then I just woke up on the streets."
        show derk solemn
        ShopOwner "What the hell... are they abducting foreigners now?"
        N "Although I'm kind of glad that he went that way with it rather than thinking I was lying, I feel bad for adding further onto his distress."
        ShopOwner "Do you remember your name?"
        N "Considering I'm in a new world and they think I'm a street performer - maybe I should just use my stage name..."
        show mc thinking
        MCNameless "Well, yeah, of course - it's..."
        
        label nameInput:
        python:
            firstName = renpy.input("First name?", default="Dorian")
            lastName = renpy.input("Last name?", default="Blackmore")
            firstName = firstName.strip() or "Dorian"
            lastName = lastName.strip() or "Blackmore"

        show mc serious
        show derk neutral
        MC "[firstName] [lastName]."
        ShopOwner "[firstName] [lastName]?"
        
        if firstName == "Mind" and lastName == "Goblin":
            MC "mind gobblin' deez nuts"
            show derk angry
            ShopOwner "..."
            MC "..."
            ShopOwner "..."
            ShopOwner "Do you wanna try giving me a real answer?"
            menu:
                "Yes":
                    ShopOwner "Good choice. What's your name?"
                    jump nameInput
                "No":
                    ShopOwner "Alright, if you're sure... {w}{size=-10}Kids these days...{/size}"
                    jump afterNameInput
        if firstName == "Derk" and lastName == "Longston":
            show derk thinking
            ShopOwner "Huh... funny thing."
            jump afterNameInput

        show derk thinking
        ShopOwner "Yeah... well, I guess you really aren't from around here."
        N "Was he maybe doubting me after all?"

        label afterNameInput:
        play music music_cozy_place
        show derk neutral
        ShopOwner "My name's Derk Longston."
        show derk neutral
        Derk "As I was saying before, it'll be tough getting you out of here - but I have heard of an underground caravan that's been working to smuggle people out of the town."
        Derk "As rumor has it, you can find them by showing up at nightfall to the alley behind the Westside Inn."
        show mc thinking
        MC "Are you going to leave, as well?"
        show derk amused
        Derk "Are you kidding? I have a shop to run!"
        Derk "Besides that, this is my home town. I'm not going to leave until we drive those bastards out."
        N "I'm not sure if I would stay, myself, but I have to respect the strength of his conviction."
        show derk neutral
        Derk "Anyway, I have to go back to running the shop."
        Derk "You can eat and rest upstairs for the day, but come nightfall you should make your way to the caravan."
        show mc happy
        MC "Thank you so much for all of this. I don't know if there's anything I can do to repay you."
        show derk amused
        Derk "Don't you worry about it. We gotta stick together and help each other in times like these after all!"
        MC "Yeah!"
        N "In times like these... The people of this town must have gone through a lot under the ruling of the Golden Scales."
        N "I only just got here, but I get the feeling that those guys are going to be a lot of trouble."
        N "I make my way upstairs to get out of Derk's way so that he can run his shop."

        scene bg mulberry shop bedroom
        N "I cook up some rations for myself and take a rest in what appears to be a spare bedroom."
        N "I peer out the window and watch the bustling of the street below."
        N "As I watch the crowd, I catch a couple patrols of what appear to be armed guards, wearing what appears at a distance to be gold-colored crests on the shoulders of their armor."
        N "Those must be the Golden Scales."
        N "I squint my eyes to try to get a better look at the crest, but I can't make out the imagery that is etched into it."
        N "Regardless, I feel grateful that a patrol had not come by when I was busking on the streets. Who knows that would have happened if that had been the case."
        N "I imagine the possibilities as I wait for nightfall."
        stop bgSound
        stop music

    # -----------------------------------------------------------------------------------------------------
    label chapter1_scene4:
        scene bg mulberry street #night
        play ambience ambience_town_night
        N "Nightfall rolls in before too long. The crowds on the streets thin out, but don't completely disappear."
        N "Crickets can be heard faintly from the foliage on this cool summer evening, just after the sun had all but completely set."
        N "Derk sees me off before I head on my way."
        show derkbody at right
        show derk smiling at right
        python:
            showMC([left])
        show mc neutral at left
        Derk "Well, that should about do it for supplies. You shouldn't need much else before getting to Strathmore."
        show mc happy
        MC "Thank you again for helping me out."
        Derk "Like I said, not a problem!"
        Derk "By the way, when you get over there - it's a little bit of a bigger city than this one."
        Derk "I have a friend over there who's a blacksmith; Fran Himbleton is her name."
        show derk embarrassed
        Derk "I admit I haven't seen her in a year or two since the town has been on lockdown, but I'm sure her shop is still on Woodrior Road."
        show derk smiling
        Derk "She'd help you out if you needed anything."
        show mc thinking
        MC "Good to know. I'll be sure to drop by."
        show mc happy
        MC "I better get going if I want to make it."
        MC "See you, Derk!"
        Derk "Best of luck, young bard."

        python:
            hideMC()
        hide mc
        hide derkbody
        hide derk
        N "\"Young bard?\" As I head down the street, I think about Derk's send-off."
        N "I guess if you think about it, I am kind of like a bard with this mandolin."
        N "I'm not really much of a poet or a storyteller though."
        N "That's usually the singer's job."
        play sound normal_walk_foot_steps_on_rock
        pause 1
        N "I continue walking down the cobblestone road, boots hitting the ground with a satisfying tap in the mostly-empty town."
        N "I pass by a stall still open selling late-night treats, and a couple walking away arm-in-arm sharing one between themselves."
        python:
            showMC()
        show mc smiling
        MC "That looks so nice..."
        python:
            hideMC()
        hide mc
        N "As I look at the people walking down the street, a flash of maroon in the alleyway catches the corner of my eye."
        N "What looks like... a hooded figure?"
        N "I look quickly, but almost as quickly as I look, they're gone."
        python:
            showMC()
        show mc nervous
        MC "That's right, this is still an unfamiliar town at night. I gotta be careful, unless I want to get robbed."
        python:
            hideMC()
        hide mc
        N "I tuck my hands farther into my pockets and hasten the pace a bit."
        N "I pass by a group of guards standing watch over the activities of the pedestrians, but try my best to not make eye contact and keep walking as if I am trying to get home."
        N "As I approach the meeting site, I make sure to check behind me a couple times as I go."
        N "I don't think anyone is following me."
        python:
            showMC()
        show mc exasperated
        MC "Maybe I'm being a bit too paranoid. It was probably just a homeless person."
        MC "I'm sure they have those here."
        SternMan "Unfortunately, there are a lot of people struggling here, homeless or otherwise."
        show mc scared
        MC "?!"

        python:
            showMC([left])
        show mc scared at left
        show jobody at right
        show jo neutral at right
        N "I turn to see that there is suddenly a stern-looking middle-aged man standing in front of me."
        SternMan "Why are you here?"
        show mc nervous
        MC "I-I was told there was a caravan helping people get out of the town here."
        SternMan "Who told you that?"
        MC "Derk Longston."
        N "The man pauses a moment, seeming to think."
        SternMan "Longston..."
        SternMan "Yeah, that's fine. Come along."
        MC "Who are you?"
        SternMan "I'm the driver."
        SternMan "You're lucky I'm not a Scale, otherwise you would have just ratted out your friend."
        MC "Oh..."
        N "Was there something else I was supposed to say?"
        python:
            hideMC()
        hide mc
        hide jobody
        hide jo
        N "I follow the driver around the corner, where tucked into the alley is a covered horse-drawn wagon filled with crates. There is an assortment of other people waiting."
        N "The driver walks off to speak with someone for a bit, but shortly returns and calls us all over to give an explanation."
        show jobody
        show jo neutral
        SternMan "Greetings everyone, my name is Joren - but you can just call me Jo."
        Jo "Now, we can get you out of this town to the next one over that's not in Scales-controlled land - but it is very important that we have your cooperation."
        N "He almost sounds like a flight attendant when giving us his explanation, but not even trying to hide how tired he is."
        N "Jo opens the back of the carriage and shifts a couple crates to the side to reveal a rectangular seam in the wood below."

        scene bg smuggler carriage night
        show jobody
        show jo neutral
        Jo "This carriage has been outfitted with a false bottom."
        play sound door_open
        pause 1
        Jo "On our way out of the city, in order to keep you hidden, you will be down in there during the inspection at the gate."
        Jo "Once we are a few miles out of town, you can emerge and enjoy the rest of the ride as you normally would."
        Jo "During the inspection though, it is integral that you make not a single sound, because doing so would mean that all of us are dead."
        Jo "Any questions?"
        N "He is so deadpan when saying that. I look around and the rest of the crowd seems a bit nervous, but completely quiet."
        Jo "Alright, with that all out of the way let's start getting loaded."
        Jo "If anyone has to pee, do so {i}before{/i} getting in."
        hide jobody
        hide jo
        N "Everyone gets their belongings together and one-by-one slips into the space underneath the floor of the carriage."
        N "It's dark and cramped, but bearable if it means getting out of this town."
        N "The crates are rearranged to hide the door in the floor, and we set off on our way out of the city."
        play bgSound ambience_wagon_rolling
        pause 3
        N "We get inspected by the guards at the gate, and everything goes well."
        N "They don't seem too concerned about what they believe is a merchant's carriage, and were not interested in being thorough enough to move around the large stacks of crates hiding the door."
        N "Jo's deadpan demeanor works well to fit the role of an everyday cart driver who's just trying to get his shipment delivered."
        stop bgSound
        play ambience ambience_woods_night fadein 2.0
        pause 2
        N "We stay in place under the floor for a couple miles down the road just in case we are stopped, but then Jo pulls off onto the side of the road and rearranges the crates into seating, then opens the door for us to come out."
        play sound moving_crates
        queue sound door_open
        pause 5
        show jobody
        show jo neutral
        Jo "Should no longer be in Scales territory now."
    
    # -----------------------------------------------------------------------------------------------------
    label chapter1_scene5:
        scene bg smuggler carriage night lit
        play bgSound ambience_wagon_rolling
        play music music_calm_night
        N "With everyone settled above the floor sitting on various crates, Jo takes the reigns and we start moving again."
        N "The road is incredibly dark, lit only faintly by the lanterns hanging near the driver's seat on the front."
        N "The inside of the carriage is also lit by lantern light. I look around at the various people sitting on top of crates of varying shapes and sizes."
        N "Most of the people in the crowd being smuggled look like average folk you'd find on the streets."
        N "Dressed in relatively drab clothing, some wearing cloaks - likely to draw less attention to themselves when they were on their way to the meeting spot."
        N "My eye is then caught by a group of three girls sitting across from me."

        scene cg smuggler carriage girls
        pause 2
        N "As they got comfortable in their seats, the girls sitting across from me opened their cloaks up more, looking relieved to be able to relax a bit more."
        N "Their outfits were eye-catching. Certainly not anything you would see an average citizen wearing."
        #TODO: Figure out panning across image at certain intervals
        N "Heavy plate armor and chainmail..." #Focus on Fighter for this line
        N "Colorful fabric edged with delicate lacing..." #Focus on Mage for this line
        N "Tight leather straps hugging their bodies..." #Focus on Ranger for this line
        pause 2 #more panning
        scene cg dorian miring
        pause 2
        scene cg smuggler carriage girls
        pause 2 #more panning, ending on mage tiddies
        play sound carriage_wheel_bump
        N "*KA-THUNK*"
        #TODO: animation and sound of jiggles goes here
        scene cg dorian miring blush
        pause 2
        N "I accidentally find myself staring at the girls for a bit longer than is socially acceptable."

        scene bg smuggler carriage night lit
        show maebody at right
        show mae suspicious at right
        Mage "..."
        python:
            showMC([left])
        show mc embarrassed at left
        MC "!!"
        N "They begin to look back, noticing that I'm staring. I look away quickly, my face feeling red hot."
        hide maebody
        hide mae
        show emmabody at right
        show emma smiling at right
        Fighter ""
        N "But still - for being people on this caravan - they are way more heavily-armed than your average townspeople..."
        hide emmabody
        hide emma
        python:
            hideMC()
        hide mc
        play sound arrow_shoot
        queue sound arrow_hit
        pause 2
        show galebody at right
        show gale scared at right
        Ranger "-!"

        scene black
        stop music
        stop sound
        stop bgSound
        pause 2
        play sound carriage_explosion
        pause 4

        scene bg smuggler carriage night destroyed
        queue sound ears_ringing
        queue sound multiple_horses_getting_closer
        python:
            showMC([], True)
        show mc pained
        MC "Egh..."
        python:
            hideMC()
        hide mc
        N "It seems that the transport didn't go unnoticed after all."
        #queue ambience carriage_attack_ambience
        play music music_skirmish
        N "As I get my bearings, I look to see that the cart is absolutely destroyed."
        N "I doubt many people made it."
        play sound sword_clash_1
        N "I hear the sounds of battle, and look up to see the three that were sitting across from me are fighting off our attackers."

        scene cg carriage combat fighter
        play sound sword_clash_2
        pause 2
        scene cg carriage combat ranger
        play sound arrow_shoot
        queue sound arrow_hit
        pause 2
        scene cg carriage combat mage
        #play sound magic_burst
        pause 2
        
        scene bg smuggler carriage night destroyed
        N "They seem pretty strong, but the attackers they are fighting far outnumber them."
        N "As the assailants swing their weapons, I can see that they are wearing golden crests. They must be the Golden Scales."
        show goonbody at right
        show goon cocky at right
        Goon "You think you can get away with smuggling our citizens, huh?"
        play sound sword_clash_1
        queue sound punch
        queue sound body_hit_ground
        pause 2
        show emmabody injured at left
        show emma hit at left
        Fighter "Augh!"
        hide emmabody
        hide emma
        show galebody injured at left
        show gale angryscared at left
        Ranger "Emmaline!"
        N "I have to do something to help. Things aren't looking good."
        N "I don't have any weapons though, what am I supposed to do?"
        hide galebody
        hide gale
        hide goonbody
        hide goon
        N "I look around frantically for an improvised weapon of some kind, and see my mandolin among the shards of destroyed carriage strewn on the ground."
        N "Maybe... I could distract them?"
        N "What, by playing a song? That's a stupid idea."
        show maebody injured at left
        show mae hit at left
        Mage "Aagh!"
        N "There's no time! Nothing else here works."
        N "I need to get attention off them so they can fight back. Anything else would be suicide."
        hide maebody
        hide mae
        N "Here goes nothing."
        python:
            showMC([], True)
        show mc angry
        MC "HEYYY!"
        python:
            hideMC()
        hide mc

        jump rhythmgame

        #TODO: Figure out rhythm game failstate logic
        
    # -----------------------------------------------------------------------------------------------------
    label chapter1_scene6:
        scene bg forest path 1 night
        play ambience ambience_woods_night
        #play bgSound carriage_burning
        show galebody injured at left
        show gale relieved at left
        stop music
        Ranger "We won."
        show maebody injured at center
        show mae assured at center
        Mage "{i}*sigh*{/i}"
        play music music_happy
        show emmabody injured at right
        show emma excited at right
        Fighter "Ya-hoo! That was crazy!"
        N "The young blonde fighter excitedly bounces up to me, shoving her face close to mine inquisitively."
        Fighter "How'd you do that, huh? That was so cool!"
        hide galebody
        hide gale
        python:
            showMC([left], True)
        show mc happynervous at left
        MC "I, uh... actually have no idea."
        show emma confused
        Fighter "You don't?"
        MC "Yeah, that's the first time that's ever happened to me."
        show mae inquisitive
        Mage "Curious."
        hide maebody
        hide mae
        show galebody injured at center
        show gale relieved at center
        Ranger "Well, whatever you did - we were able to beat them because of it. Thank you."
        show emma happy
        Fighter "Yeah! Thanks!"
        hide emmabody
        hide emma
        show maebody injured at right
        show mae inquisitive at right
        Mage "What's your name?"
        show mc smiling
        MC "[firstName] [lastName]."
        show gale amused
        Ranger "[firstName] [lastName]?"
        hide maebody
        hide mae
        show emmabody injured at right
        show emma happy at right
        Fighter "Oooh! I like that name!"
        hide galebody
        hide gale
        show maebody injured at center
        show mae smiling at center
        Mage "It's a pleasure to make your acquaintance, [firstName]."
        Fighter "My name's Emmaline! Emmaline Lumiere!"
        hide emmabody
        hide emma
        show galebody injured at right
        show gale smiling eyesclosed at right
        Ranger "Gale Ashwood."
        Mage "And I'm Mae Faeleigh."
        MC "Nice to meet all of you."

        stop music fadeout 2.0
        pause 2
        show mae serious
        Mae "On a more serious note, the reason we were on that caravan is because we were gathering intel on the operations of the Golden Scales."
        Mae "We're part of a guild that has been working to push back against their advances."
        python:
            hideMC()
        hide mc
        show galebody injured at left
        show gale serious at left
        show emmabody injured at right
        show emma serious at right
        N "Emmaline and Gale's faces grow a bit more stern as Mae talks, and nod in confirmation of their efforts."
        Mae "The aid you have provided us with today, [firstName], made the difference in whether or not we made it out alive."
        Mae "Regardless of whether or not you yet know what skills you possess, it is clear to me that you have an innate talent for enchantment that would be a great help in fighting against the Golden Scales."
        show emma excited
        Emma "{i}*gasp*{/i} Are you asking [pronoun.obj] to come with?"
        N "Mae nods."
        show mae smiling
        Mae "That is exactly what I'm proposing."
        Gale "I'm not sure, Mae. We did just meet [pronoun.obj]."
        show emma exasperated
        Emma "Awww. Come on, Gale! You saw how much stronger that music made us!"
        show gale happynervous
        Gale "I mean, I guess that is hard to deny."
        Mae "What do you say, [firstName] [lastName]?"
        N "This is a lot to take in right off the bat."
        N "I haven't been in this universe for more than 24 hours, and I've already been a stowaway, blown up, awoken to mysterious magical powers, fought off members of a hostile organization I know next-to-nothing about..."
        N "and now I'm being asked if I want to join a resistance?"
        N "Mae appears to be a sorceress of some kind; it's possible that through her or other people in this guild I could find out what exactly my abilities are, or how I got here in the first place."
        N "It's also pretty clear that the Golden Scales are not great people, and working to stop them would make things a lot better for the people of this world."
        
        hide maebody
        hide mae
        hide galebody
        hide gale
        hide emmabody
        hide emma
        N "I look to the wreckage of the carriage still smoldering from the explosion. All of those people that were in there-"
        #play sound shuffling_sounds
        pause 2
        show jobody damaged at right
        show jo pained at right
        Jo "{i}*wheeze*{/i} Help..."
        python:
            showMC([left], True)
        show mc surprised at left
        MC "He's still alive!"
        show emmabody injured at center
        show emma scared at center
        Emma "Jo!"
        hide emmabody
        hide emma
        python:
            hideMC()
        hide mc
        hide jobody
        hide jo
        N "We all rush over to the wreckage and quickly lift the boards that are pinning Jo down."
        N "He's bloodied, and his clothes are seared, but he doesn't look that badly burned."
        show jobody damaged at right
        show jo pained at right
        Jo "{i}*groan*{/i}"
        N "As we lift the wreckage off his legs, we see a thick shard of wood speared into his left thigh. It's bleeding pretty badly."
        show maebody injured at left
        show mae scared at left
        Mae "Don't pull it out until we can get him to a doctor. Here-"
        N "Mae places her hands onto Jo's leg and they emit a pulsing green light."
        #play sound magical_humming
        pause 2
        N "The pulses move into Jo's leg and he stops groaning."
        N "She stands up and turns to us."
        hide jobody
        hide jo
        show mae nervous
        Mae "I'm not a healer, but that shold be good enough to slow the bleeding until we can get to Strathmore."
        show emmabody injured at right
        show emma scared at right
        Emma "Are there any other survivors?"
        show galebody injured at center
        show gale serious at center
        N "We turn to the carriage, and Gale has already been looking through the wreckage while we were helping Jo."
        N "She looks to us grimly, and shakes her head no."
        show mae serious
        Mae "Let's take some of horses off the Scales we killed and get him into town."
        Emma "Help me out, [firstName]!"
        hide emmabody
        hide emma
        hide galebody
        hide gale
        hide maebody
        hide mae
        N "As Mae and Gale gather some horses for us to ride, I help Emmaline lift Jo and carry him."
        N "We hoist him up onto a horse with Gale, and we all ride through the rest of the night into town, with Mae creating a bright orb in front of us to provide some light."
        play sound multiple_horses_galloping
        pause 2

    # -----------------------------------------------------------------------------------------------------
    label chapter1_scene7:
        scene bg strathmore walls night
        play ambience ambience_town_night
        play sound multiple_horses_galloping
        N "As we ride closer to the city of Strathmore, we break from the edge of the forest and I can see its large walls growing on the horizon."
        N "Even from a distance, I can tell it's a much larger place than Mulberry Town."
        N "As we get closer I can see the gate is open, but there is a small group of guards posted at it. Emmaline begins to shout to them."
        N "The guards look towards us, and at first seem cautious, but as we get closer they seem to recognize Emmaline's shouting and move to open the center of the path for us to race through without stopping."

        scene bg strathmore street night
        N "I follow the lead of the others, who seem to know by heart where the nearest hospital is in town."
        N "We pull up outside of it, and Mae and Emmaline quickly hop off as a nurse runs out, and they help bring Jo inside."
        N "I stand by the entrance, unsure if I should go in or not."
        play music music_calm_night
        show galebody injured at right
        show gale neutral at right
        Gale "Don't worry, now that we've made it here he's in good hands."
        N "I turn to look at Gale, who is standing not too far behind me holding the reigns of all the horses steadily, two in each hand."
        N "The soft lantern light of the city glows warmly against her red hair - but her silver eyes remain cool like the brisk air."
        python:
            showMC([left], True)
        show mc solemn at left
        MC "I was just a bit worried. Emmaline seemed really scared for him."
        Gale "Jo is the uncle of one of our guild members, and besides that he has been really good to all of us."
        Gale "He's done a lot to help people escape from the takeover of the Golden Scales."
        MC "I see..."
        show gale smiling
        Gale "But like I said, don't worry. He's tough as nails. It's going to take a lot more than that to stop him."
        Gale "We've got some of the best healers in the country here in Strathmore."
        show mc thinking
        MC "This city does seem very big, is it the capital?"
        show gale amused
        Gale "You're a traveler and you don't even know the capital of the country you're traveling in?"
        show mc irritated
        MC "I don't think I ever told you I was traveling."
        Gale "I can tell by the name."

        menu:
            "Well, I guess that's fair.":
                jump choice1_a
            "People have all kinds of names!":
                jump choice1_b
            "Gale isn't really that common of a name, either.":
                jump choice1_c
        
        label choice1_a:
            show mc surprised
            MC "Well, I guess that's fair."
            Gale ""
            N "Gale seems to hide a small chuckle at that."
            python:
                relationship.gale += 1
            jump choice1_after
        
        label choice1_b:
            MC "People have all kinds of names!"
            N "Gale seems unconvinced, but relents."
            Gale "Yeah, I guess you're right."
            jump choice1_after

        label choice1_c:
            MC "Gale isn't really that common of a name, either."
            show gale serious
            N "Gale seems a little bothered by my comment."
            Gale "I disagree, but nonetheless-"
            python:
                relationship.gale -= 1
            jump choice1_after
            
        label choice1_after:
            show gale curious
            Gale "Have you given any more thought to Mae's offer?"
            N "Just as I open my mouth to give her an answer, Mae and Emmaline emerge from the hospital."
            python:
                hideMC()
            hide mc
            show maebody at left
            show mae assured at left
            show emmabody at center
            show emma smiling at center
            Mae "Looks like he's going to be fine."
            show gale smiling
            N "I look to Emmaline and she looks tired but is also smiling in relief. Gale looks content in knowing that she was right."
            Gale "See? Just like I told you."
            show mae inquisitive
            Mae "Oh? What else were you telling [pronoun.obj]?"
            show gale neutral
            Gale "Well, I was just asking [pronoun.obj] what [pronoun.subj] thought about your offer to join us."
            show emma curious
            N "Emmaline's eyes seem to brighten a bit at the mention."
            Emma "-?"
            show mae amused
            Mae "Well, so? What do you think?"

            menu:
                "Well, I would like to learn more about this new magical ability I have.":
                    jump choice2_a
                "After seeing what the Golden Scales are doing to people, I feel like I can't sit back and watch.":
                    jump choice2_b
                "You all seem like really great people, I would love to help.":
                    jump choice2_c
                "I don't have much else to do, so why not?":
                    jump choice2_d
            
            label choice2_a:
                $hiddenChar = "gale"
                hide galebody
                hide gale
                python:
                    showMC([right], True)
                show mc thinking at right
                MC "Well, I would like to learn more about this new magical ability I have."
                show mae smiling
                N "Mae looks thrilled by my answer."
                Mae "Excellent!"
                python:
                    relationship.mae += 1
                jump choice2_after

            label choice2_b:
                $hiddenChar = "mae"
                hide maebody
                hide mae
                python:
                    showMC([left], True)
                show mc serious at left
                MC "After seeing what the Golden Scales are doing to people, I feel like I can't sit back and watch."
                show gale smiling
                N "Gale nods in agreement with my answer."
                Gale "Glad to have you on board."
                python:
                    relationship.gale += 1
                jump choice2_after

            label choice2_c:
                $hiddenChar = "mae"
                hide maebody
                hide mae
                python:
                    showMC([left], True)
                show mc smiling at left
                MC "You all seem like really great people, I would love to help."
                show emma excited
                N "Emmaline becomes ecstatic upon hearing this."
                Emma "[pronoun.contractCap] really gonna join?"
                python:
                    relationship.emma += 1
                jump choice2_after

            label choice2_d:
                $hiddenChar = "mae"
                hide maebody
                hide mae
                python:
                    showMC([left], True)
                show mc smiling at left
                MC "I don't have much else to do, so why not?"
                N "The group seems to accept this answer."
                jump choice2_after
            
        label choice2_after:
            show emma excited
            Emma "Yaaay! New friends!"
            N "Emmaline throws herself around my neck, nearly dragging me to the ground with her."
            
            if (hiddenChar == "gale"):
                python:
                    hideMC()
                hide mc
            
            show galebody injured at right
            show gale nervous at right
            Gale "Don't get too excited, Emmaline. We still need to talk to the others about this."

            if (hiddenChar == "mae"):
                python:
                    hideMC()
                hide mc
            
            show maebody at left
            show mae neutral at left
            Mae "Yes, Aldona might need a little convincing."
            Emma "I'll convince her!"
            N "As Emmaline releases her arms from me, I notice that her wounds from the battle are gone."
            hide galebody
            hide gale
            python:
                showMC([right], True)
            show mc thinking at right
            MC "Hey - where did your wounds go?"
            show mae amused
            Mae ""
            N "Mae steps towards me and holds out her hand, and the same green glow radiates around it as when she healed Jo's leg."
            N "As she touches the wounds on my body, I can tell that they are healing."
            show mae neutral
            Mae "My healing abilities aren't as strong as the other mages at the hospital here, but I can heal minor wounds like these."
            N "As she works her way up my body, she starts to heal the cuts on my face with a gentle touch."
            show mae amused
            N "Just as she's about to finish the last one, she prods a finger into it and pushes me back."
            python:
                showMC([right])
            show mc pained
            MC "Ow!"
            Mae "But maybe I'll leave this one, just for staring at my breasts eariler."
            show mc embarrassed
            MC "I'm sorry!"
            show emma amused
            Emma "Ooo - looks like [firstName] is already in the hot seat!"
            python:
                hideMC()
            hide mc
            show galebody injured at right
            show gale amused at right
            Gale ""
    
    # -----------------------------------------------------------------------------------------------------
    label chapter1_scene8:
        play ambience ambience_town_night
        play music music_calm_night
        hide galebody
        hide gale
        hide maebody
        hide mae
        hide emmabody
        hide emma
        N "We make our way through the streets of Strathmore to the Monroe Inn, where the Guild is basing their operations out of."
        N "It has been a long night for all of us. The street lamps flicker quietly as our feet tap against the stone road."
        scene bg monroe ext night
        N "We approach the Inn, and I can see the lights are still on inside."
        N "It has very classic tudor-style architecture, as would be expected of an inn in a world like this."
        N "What is unexpected is how large this building is."
        N "It's almost like two inns stitched together. It's probably big enough to house a small army."
        N "I guess that's why the Guild chose here as their base of operations."
        python:
            showMC([left])
        show mc thinking at left
        MC "Wow. This place is massive."
        show maebody at right
        show mae assured at right
        Mae "The Monroe is the heartbeat of this city."
        Mae "It's one of the few inns in Strathmore, so it needs to be big enough to accommodate the tourism here."
        MC "Are there a lot of tourists?"
        Mae "During parts of the year, usually uring holidays and festivals. Most of the big tourist attractions are in Lynndam."
        MC "Where's Lynndam?"
        show galebody at center
        show gale assured at center
        Gale "It's the capital."
        show mc nervous
        MC "Right."
        hide galebody
        hide gale
        show emmabody at center
        show emma happy at center
        Emma "I absolutely love the Midsummer Festival in Lynndam!"
        Emma "So many games, pretty lights, and tasty cart snacks!"
        show mc thinking
        MC "Is that coming up soon?"
        show mae inquisitive
        show emma concerned
        N "The three look at me a bit suspiciously."
        Mae "No... it was just two weeks ago."
        show mc nervous
        Emma "Are you okay [firstName]? Everyone knows about the Midsummer Festival!"
        N "I should be a little bit more careful before I speak."
        MC "Oh, no - I mean - I had gotten kidnapped by the Golden Scales, and that's how I ended up in Mulberry Town. I honestly don't remember much before they attacked me."
        python:
            hideMC()
        hide mc
        show galebody at left
        show gale solemn at left
        show mae solemn
        Gale ""
        Emma "That's terrible!"
        Mae "I'm sorry to hear that. Maybe there's something one of our associates can do to help."
        N "I feel a little bit bad lying to them, but this story is a lot more believable than what really happened."
        show mae neutral
        Mae "Anyway, we've stood our here chatting long enough. Let's go inside and introduce you."
        Mae "I'm sure Aldona has been pacing around the inn all night."

        scene bg monroe int night
        play sound door_open
        pause 1
        stop ambience
        play bgSound ambience_fireplace
        play music music_cozy_place
        N "As we enter the door, I'm hit with the warm smell of stew that was being served earlier that day."
        N "The interior of the inn is roomy, but still somehow feels cozy."
        N "Nearly everything is carved out of a red oak wood, whose polish reflects even more warmly from the lanterns that light the room, and the large hearth that sits in the center back wall."

        scene cg aldona introduction
        N "There is a woman with long white hair weaving her way back and forth between the empty tables in the quiet inn."
        N "She looks pensive."
        Emma "We're back!"
        N "The woman looks up to us at the door. Her face shifts from a concerned pensiveness to a stern expression."

        scene bg monroe int night
        play music music_in_trouble
        show aldobody at right
        show aldo serious at right
        Paladin "You're back a lot later than you were supposed to be."
        show maebody at left
        show mae nervous at left
        Mae "It was a lot more trouble getting out of the town than we realized."
        show aldo irritated
        Paladin "You're an entire day late!"
        Monk "Come on, Aldona."

        scene cg kaz introduction
        N "On the other side of the room another woman speaks up, a woman with short-cut curly hair leaning back in a chair."
        Monk "They clearly ran into a little snag, but they made it back just fine."

        scene bg monroe int night
        show emmabody at left
        show emma nervous at left
        Emma "Yeah... we actually almost died."
        show galebody at center
        show gale exasperated at center
        Gale "..."
        show aldobody at right
        show aldo exasperated at right
        AldoFirst "That's exactly what I was worried about!"
        Emma "But like Kaz said, we're fine!"
        show aldo irritated
        AldoFirst "I knew that mission was too risky for just three of you."
        hide galebody
        hide gale
        show maebody at center
        show mae nervous at center
        Mae "Well, if it makes it better, we did get some good information on the Scales."
        show aldo nervous
        AldoFirst "Well, I guess that's good. Then I guess it-"
        N "She seems to suddenly notice me standing with them, and narrows her eyes."
        show aldo suspicious
        AldoFirst "Who is this?"
        show mae assured
        show emma excited
        Emma "This is [firstName] [lastName]! [pronoun.subjCap] saved us when we were on our way back."
        AldoFirst "Oh?"
        Mae "Yes, if it were not for [pronoun.obj] we would not have made it back there."
        N "Aldona looks like she is thinking this over for a second before speaking again, but just as she is about to say more a horned, curvaceous woman emerges from the back room."
        Warlock "My, my - what is all of this commotion about?"
        Emma "Alarice! We have a new friend!"
        Warlock "Oh?"
        N "The woman walks over to me, moving with her hips swaying back and forth in synchronization with her... um..."

        scene cg alarice introduction
        #play sound tiddy_timpani
        AlaFirst "[pronoun.contractCap] so cute, you mean we get to keep [pronoun.obj]?"
        AldoFirst "I didn't say [pronoun.subj] could-"
        Emma "See, look! Alarice likes [pronoun.obj]!"
        Gale "{size=-10}Alarice likes everyone...{/size}"
        KazFirst "Sorry about Alarice, [firstName]. She can be a little handsy."

        scene bg monroe int night
        show alabody at right
        show ala smiling at right
        AlaFirst "My apologies, young bard. I just can't help but get excited at the prospect of another subject in our midst."
        python:
            showMC([left])
        show mc nervous at left
        MC "Subject?"
        N "Mae clears her throat audibly."
        python:
            hideMC()
        hide mc
        show maebody at left
        show mae irritated at left
        Mae "Yes, the subject - changing it."
        hide alabody
        hide ala
        show mae serious
        Mae "Aldona, [firstName] has shown promise of great magical abilities that could be a great benefit to our team."
        Mae "[pronoun.subjCap] [pronoun.subjHasHave] only just awakened to [pronoun.adj] power, but even at these levels boosted our strength enough to fend off many more men than we would ordinaily be able to."
        show aldobody at right
        show aldo nervous at right
        AldoFirst "..."
        Mae "I understand that you are a bit skeptical of the idea of bringing strangers on board with us-"
        Mae "but I think turning [firstName] away woul be a greatly missed opportunity that could shift the tides in fighting against the Scales."
        show aldo serious eyesclosed
        N "Aldona's expression grows pensive again. She seems reluctant, but unable to deny the reasoning of Mae."
        AldoFirst "If that is all true, then fine. We'll give [pronoun.obj] a shot."
        show emmabody at center
        show emma excited at center
        show mae assured
        Emma "-!"
        show aldo serious
        AldoFirst "But I'll be keeping an eye on them."
        Mae "As expected."
        stop music
        hide emmabody
        hide emma
        hide maebody
        hide mae
        N "Aldona turns to me and bows her head slightly."
        AldoFirst "I apologize for my harsh conduct earlier. My name is Aldona Fortwright, Fifth Knight of Lynndam."

        menu:
            "It's understandable. I would be worried in this situation, too. {i}*bows*{/i} [firstName] [lastName], Miss Aldona.":
                jump choice3_a
            "A pleasure to formally meet. {i}*bows*{/i} [firstName] [lastName].":
                jump choice3_b
            "Thanks. You already know my name.":
                jump choice3_c

        label choice3_a:
            python:
                showMC([left])
            show mc neutral at left
            MC "It's understandable. I would be worried in this situation, too. {i}*bows*{/i} [firstName] [lastName], Miss Aldona."
            show aldo assured
            N "Aldona seems flattered by my response."
            Aldo "I'm glad you can see my side of things."
            show aldo neutral
            Aldo "I hope that we can work well together in the future."
            python:
                relationship.aldo += 1
            jump choice3_after

        label choice3_b:
            python:
                showMC([left])
            show mc neutral at left
            MC "A pleasure to formally meet. {i}*bows*{/i} [firstName] [lastName]."
            show aldo neutral
            N "Aldona seems satisfied with my response."
            Aldo "I hope that we can work well together in the future."
            jump choice3_after

        label choice3_c:
            python:
                showMC([left])
            show mc neutral at left
            MC "Thanks. You already know my name."
            show aldo neutral
            N "Aldona looks a bit miffed by my response, but retains her formality. I can hear Kaz snort from across the room."
            Aldo "Indeed."
            python:
                relationship.aldo -= 1
                relationship.kaz += 1
            jump choice3_after

        label choice3_after:
            python:
                hideMC()
            hide mc
            hide aldobody
            hide aldo
            play music music_cozy_place
            N "Alarice and Kaz seem to take the cue from Aldona. Alarice takes a small bow."
            show alabody at left
            show ala smiling at left
            AlaFirst "Mistress Alarice Peigne."
            N "Kaz waves from where she is seated, not seeming too interested in getting up."
            show kazbody at right
            show kaz smiling at right
            KazFirst "Kaz Freehold."
            N "With introductions out of the way, Aldona turns to address the room."
            hide kazbody
            hide kaz
            hide alabody
            hide ala
            show aldobody at right
            show aldo neutral at right
            Aldo "The innkeeper is already asleep by now, but she set aside a number of rooms for us to use - including some spares."

            python:
                bestGirl = relationship.bestGirl()

            if (bestGirl == "emma"):
                $bgName = "Emmaline"
                show emmabody at left
                show emma neutral at left
                Emma "There's an empty one next to mine, I'll show [firstName] where it is on the way to my room."
            if (bestGirl == "mae"):
                $bgName = "Mae"
                show maebody at left
                show mae neutral at left
                Mae "There's an empty one next to mine, I'll show [firstName] where it is on the way to my room."
            if (bestGirl == "gale"):
                $bgName = "Gale"
                show galebody at left
                show gale neutral at left
                Gale "There's an empty one next to mine, I'll show [firstName] where it is on the way to my room."
            if (bestGirl == "aldo"):
                $bgName = "Aldona"
                Aldo "There's an empty one next to mine, I'll show [firstName] where it is on the way to my room."
            if (bestGirl == "kaz"):
                $bgName = "Kaz"
                show kazbody at left
                show kaz neutral at left
                Kaz "There's an empty one next to mine, I'll show [firstName] where it is on the way to my room."
            if (bestGirl == "ala"):
                $bgName = "Alarice"
                show alabody at left
                show ala neutral at left
                Ala "There's an empty one next to mine, I'll show [firstName] where it is on the way to my room."

            Aldo "With that all handled, everyone get some sleep."
            Aldo "We can go over the results of your mission tomorrow when the others get back."
            
            scene bg monroe int night
            N "The group dissipates and heads up to their various rooms."
            N "I follow [bgName] up the stairs and into the hall on the left. She walks past rows of doors until she stops at one at the end of hall."

            if (bestGirl == "emma"):
                show emmabody at right
                show emma smiling at right
                Emma "You can use this room here. If you need anything, I'll be next door."
            if (bestGirl == "mae"):
                show maebody at right
                show mae smiling at right
                Mae "You can use this room here. If you need anything, I'll be next door."
            if (bestGirl == "gale"):
                show galebody at right
                show gale smiling at right
                Gale "You can use this room here. If you need anything, I'll be next door."
            if (bestGirl == "aldo"):
                show aldobody at right
                show aldo neutral at right
                Aldo "You can use this room here. If you need anything, I'll be next door."
            if (bestGirl == "kaz"):
                show kazbody at right
                show kaz smiling at right
                Kaz "You can use this room here. If you need anything, I'll be next door."
            if (bestGirl == "ala"):
                show alabody at right
                show ala smiling at right
                Ala "You can use this room here. If you need anything, I'll be next door."

            python:
                showMC([left])
            show mc smiling at left
            MC "Thanks."

            scene bg monroe room night
            play ambience ambience_town_night volume 0.5
            N "The room is relatively plain, but it has a rustic charm compared to what I'm used to. A window on the wall looks down onto the street below."
            N "I collapse into bed."
            python:
                showMC()
            show mc tired
            MC "{i}*sigh*{/i}"
            python:
                hideMC()
            hide mc
            N "What an exhausting day. Maybe after some sleep, tomorrow will be a little less hectic."
            N "I blow out the candle lamp on the night stand, and doze off almost immediately."
            N "At least... I don't have to figure this out all alone."
            scene black
            pause 2
            stop music
            pause 2

    # -----------------------------------------------------------------------------------------------------
    label chapter1_scene9:
        scene bg monroe room day
        play ambience ambience_city_day
        N "As I wake up, I can hear the quiet murmuring of townspeople on the street from my window."
        N "I take a look outside, and the sun has already risen to the highest point in the sky."
        N "I guess it figures that I would sleep in after being up nearly through the night yesterday."
        N "I was so tired that I didn't even bother undressing before bed last night, so all I need to do is fix my hair before heading downstairs."
        
        scene bg monroe int day
        play music music_happy
        play ambience ambience_inn_day
        N "As I descend the stairs into the main area, I can see that the Monroe is certainly as popular as Mae said it was."
        N "Nearly all of the tables are occupied by people chatting and enjoying brunch. The bar has a handful of daytime drinkers at it, and workers walk in and out of the doors behing them with plates."
        N "My eyes scan around looking for familiar faces, until I find the Guild all together seated at a larger table towards the back corner of the main floor."
        N "I make my way over to them."
        show maebody at left
        show mae amused at left
        Mae "Ah, [pronoun.contract] awake."
        show aldobody at right
        show aldo assured at right
        Aldo "Good morning, [firstName]."
        show galebody at center
        show gale neutral at center
        Gale "I guess it's more like afternoon now."
        hide maebody
        hide mae
        show alabody at left
        show ala nervous at left
        Ala "Well you can't blame [pronoun.obj]. I would be exhausted too after a night like that! Poor thing."
        hide aldobody
        hide aldo
        show emmabody at right
        show emma excited at right
        Emma "[firstName]! Sit next to me!"
        N "Emmaline excitedly scoots to make a space next to her and pats it repeatedly. I indulge her and take a seat."
        N "Kaz is leaning on the table across from me."
        hide galebody
        hide gale
        show kazbody at center
        show kaz smiling at center
        Kaz "How'd ya sleep last night?"
        hide alabody
        hide ala
        python:
            showMC([left])
        show mc smiling at left
        MC "Well enough, I'm feeling pretty good today."
        N "As we're talking, a middle-aged woman comes up to the table."
        hide emmabody
        hide emma
        show mlkbody at right
        show mlk smiling at right
        Innkeep "Is this the young musician I've been hearing about?"
        hide kazbody
        hide kaz
        show aldobody at center
        show aldo neutral at center
        Aldo "[firstName], this is Mary Lynn Kearne. She's the owner of the Monroe, and has been very kindly letting us stay here while we work to fight against the Golden Scales."
        show mlk smiling wink
        hide aldobody
        hide aldo
        MLK "Anything to help the cause!"
        MC "Nice to meet you."
        show mlk smiling
        MLK "What do you play?"
        MC "Oh, I play the mandolin."
        MLK "Ooh - exciting!"
        show mlk smiling wink
        MLK "Maybe you can put on a performance for our customers some time. I'm sure they'd go wild for that!"
        show emmabody at center
        show emma happy at center
        show mc nervous
        Emma "A performance at the inn? That'd be so cool!"
        MC "I guess - I, uh-"
        hide emmabody
        hide emma
        show maebody at center
        show mae amused at center
        Mae "[firstName] just woke up a few minutes ago, that might be a lot for [pronoun.obj] to take in."
        show mlk smiling
        MLK "Oh - I'm sorry! Where are my manners."
        MLK "Let me go talk to the chef, and he'll get something whipped up for you."
        show mlk smiling wink
        MLK "On the house, of course."
        hide mlkbody
        hide mlk
        N "Mary Lynn walks away and the party chuckles a bit."
        show galebody at right
        show gale amused at right
        Gale "She can be a little pushy sometimes, but she's sweet."
        show mc thinking
        MC "Oh - how is Jo doing?"
        show gale serious
        show mae assured
        N "The table looks a bit more serious."
        Mae "I checked on him this morning. He's likely to make a full recovery, but it's going to take him a while."
        hide galebody
        hide gale
        show aldobody at right
        show aldo solemn eyesclosed at right
        Aldo "I am in your debt, [firstName] [lastName]."
        show mc surprised
        MC "Wait - is Jo {i}your{/i} uncle?"
        show aldo serious
        Aldo "Who else's uncle would he be?"
        show mc nervous
        MC "Well, I guess I can kind of see the resemblance..."
        hide maebody
        hide mae
        show kazbody at center
        show kaz smiling at center
        Kaz "It's the white hair."
        show aldo irritated
        Aldo "-?!"
        python:
            hideMC()
        hide mc
        show emmabody at left
        show emma amused at left
        Emma "And they're both so serious all the time!"
        N "As the Guild is having another round of chuckles - except for Aldona this time - I look to the front of the inn as three figures enter in through the doorway."

        scene cg inn entrance girls
        pause 2
        N "The reason I looked over originally was because I noticed that one of the women was huge."
        N "After ducking in through the entrance, she stands much higher than everyone else in the room - and looks fit enough to take on everyone in it."
        N "I then notice the other two women with her, who as far as people go looked like just about polar opposites."
        N "One so soft and friendly looking that I bet even a rabbit would eat out of her hand-"
        N "The other one looking more like a rabbit that would bite your hand if you tried to feed it."
        Kaz "It looks like they're back on time."
        Emma "HEY GUYS!! OVER HERE!"
        Aldo "Please, Emmaline. We're in a building with other people."

        scene bg monroe int day
        N "The group of three approaches our table."
        show aldobody at left
        show aldo serious at left
        Aldo "I trust everything went well?"
        show imarabody at right
        show imara smiling at right
        Barbarian "Just as planned, no problem at all."
        N "The large woman notices me almost immediately."
        show imara smiling wink
        Barbarian "New person?"
        show maebody at center
        show mae assured at center
        Mae "Yes. Gale, Emmaline and I had a close call on our mission. This is [firstName] [lastName]. [pronoun.subjCap] helped us out greatly, and agreed to join the team."
        Barbarian "Ah!"
        show imara smiling
        show aldo neutral
        Aldo "[firstName], this is Imara Oakheart,"
        hide maebody
        hide mae
        show chibody at center
        show chi smiling at center
        Aldo "Chiyo,"
        hide aldobody
        hide aldo
        show silbody at left
        show sil irritated at left
        Aldo "and Silver."
        N "As I stand up to greet them more properly, Chiyo bounces over to me and cups both of my hands with hers."
        Chi "It's so great to meet you! I'm Chiyo!"
        N "As Chiyo's voice bubbles like sweet sugar while greeting me, Silver's expression sours even more."
        stop music
        Sil "We don't need any more people."
        N "Her words cut through the air like a sharpened piece of glass, silencing the entire table. She glares at me for a moment more."
        show sil angry
        Sil ""
        hide silbody
        hide sil
        N "With a twist of her cape, she walks away and storms upstairs."
        python:
            showMC([left])
        show mc nervous at left
        MC "..."
        N "Imara surprises me with the clap of a large hand on my shoulder."
        Imara "Pay no mind to her, she's just tired from a long mission."
        python:
            hideMC()
        hide mc
        show kazbody at left
        show kaz amused at left
        Kaz "Still, that was a bit more pissy than she usually is."
        show imara thinking
        Imara "Well, we had a little bit of a disagreement along the way."
        show chi solemn
        Chi "I think it might be my fault."
        hide kazbody
        hide kaz
        show maebody at left
        show mae inquisitive at left
        Mae "You did say everything went well, right?"
        show imara neutral
        Imara "Yes, the mission went over well, regardless of any disagreements."
        hide maebody
        hide mae
        show aldobody at left
        show aldo neutral at left
        Aldo "Well, I'll have to have a talk with her later."
        hide chibody
        hide chi
        show galebody at center
        show gale neutral at center
        Gale "It's probably best to let her cool off for a bit, anyway."
        show aldo assured
        Aldo "Right. Imara, Chiyo, have a seat. We have much to discuss."