## CharlieFuu69
## Ren'Py RhythmBeats!

## RPY Module: Rhythm Action System

## © 2023 CharlieFuu69 - GNU GPL v3.0
## Google-translated and modified by a-murph

################################################################################

init python:
    """
    ----------------------------------------------------------------------------
                        <- /!\ USEFUL INFORMATION /!\ -> 
    All documented items beginning with (UNDOCUMENTED) are 
    elements that RhythmBeats uses internally, and that do not have as much 
    relevance to the end user, except for wanting to review the code 
    module source. 

    To increase performance on Windows, you can unlock the plan 
    High Performance power by running the following command in Powershell: 

    powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
    ----------------------------------------------------------------------------
    """

    import json
    import os
    import pygame
    import itertools

    config.pygame_events.extend([
        pygame.FINGERDOWN,
        pygame.FINGERUP
    ])

    def logger(level, content):
        print("[%s] %s" % (level, content))

    ## -------------------------------------------------------------------------- ##
    ## Clases

    class RhythmBeatsException(Exception):
        """A simple class for throwing exceptions called Ren'Py RhythmBeats."""
        pass

    class RhythmPlayground:

        def __init__(self, fn, displayable, song_file, offset_map = 0.0, offset_game = 0, threshold = 100, max_score = 1000, failsafe = False):
            """Constructor for the class RhythmPlayground(). 
            Receives 8 parameters (3 required) at the time the request is created. 
            class instance. 

            These parameters are the following: 

            fn (str): 
            This parameter is required, and receives a string with the path 
            of the BEAT file relative to the /game folder of your game. 
            This file can be read even inside an RPA package. 

            displayable (str o displayable): 
            This parameter is mandatory, and receives as an argument an element 
            displayable that will be used to display each note on the screen. 
            You can pass as argument an image path, or some displayable 
            from Ren'Py like Image() or Transform(). 

            song_file (str o list): 
            This parameter is required, and receives a string as argument. 
            text with the path of the audio file containing the song 
            to play during the game.  You can also pass a list 
            to create a playback queue, for example, in the case of 
            you want to add a short silence before the song starts 
            actual of the game 
            Details: https://www.renpy.org/doc/html/audio.html#renpy.music.play 

            offset_map (int o float): 
            If it is not 0, this parameter receives an integer as an argument. 
            or a floating point number representing time (in seconds) 
            that the beatmap must compensate with respect to the musical track, in case 
            that there is a discrepancy between the two. 
            Positive values delay the beatmap with respect to the music track, 
            while negative values advance it. 

            offset_game (int): 
            If it is not 0, this parameter receives an integer as an argument. 
            A that represents the time (in milliseconds) that is added as a 
            compensation customizable by the player, fulfilling a role 
            similar to the Timing gauge that some rhythm games have. 

            Tip: Store that number in a persistent variable so that the 
            player does not have to calibrate again and again every time it starts 
            the game.  Then you pass that variable as the argument of this parameter. 

            threshold (int): 
            If it is not 100, this parameter receives as an argument an integer, 
            A that represents the base time threshold (in milliseconds) for 
            detect if the player has hit a note. 
            By default the threshold has been set to 100ms (0.1 seconds), which 
            which gives a total of 200ms to hit a note. 

            max_score (int): 
            This parameter receives as an argument an integer that represents 
            a 'hypothetical' maximum number of points that could be received per note. 
            By default, the hypothetical maximum that could be received is 
            1000 points. 

            failsafe (bool): 
            Safe mode allows you to play the beatmap without having to play the notes. 
            It is useful in case you want to visually adjust the cascade of notes with respect to 
            of the music (using offset_map). 
            If True, it will run the beatmap in safe mode.  If it is False, the 
            game will run normally. 
            """

            ####################################################################
            ## MODIFIABLE ATTRIBUTES 

            ## ------------------- SPRITEMANAGERS AREA ------------------- ## 
            self.map_mgr = SpriteManager(update = self.map_callback)
            self.waterfall_mgr = SpriteManager(update = self.waterfall_callback, event = self.tap_events)

            ## ---------------- MAIN ROUTES AND SETTINGS ----------------- ##

            ## Relative paths.
            self.fn = fn
            self.displayable = displayable
            self.song_file = song_file
            self.miss_sound = None

            ## Game calibration and scoring margin per note.
            self.offset = offset_map + (offset_game / 1000.0)
            self.threshold = (threshold / 1000.0)
            self.max_score = max_score

            ## Run in safe mode
            self.failsafe = failsafe

            ## Pygame key handle
            self.left_key = pygame.K_c
            self.right_key = pygame.K_m

            ####################################################################
            ## ATTRIBUTES NOT MODIFIABLE BY THE USER (RESERVED)

            ## System operating parameters
            self.core_tick = 0.01667
            self.waterfall_tick = 0.001
            self.map_delta = 1.04

            ## ----------------- LOADED BEATMAPS DATA ----------------- ##

            ## Storing the loaded beatmap.
            self.lane_L = list()
            self.lane_R = list()

            ## Storage/Group of sprites
            self.spritegroup = list()

            ## ------------- COMPUTATION AND ACTIVITY OF THE GAME ------------- ##

            ## Timestamp rates and beatmap progress
            self.index = {"left" : 0, "right" : 0}
            self.note_pass = {"left" : 0, "right" : 0}
            self.key_tap = {"left" : 0.0, "right" : 0.0}
            self.timestamp_log = list()
            self.map_progress = (0, 0)
            self.last_tap = 0.0

            ## Game computation
            self.combo = 0
            self.perfect = 0
            self.miss = 0
            self.stage_score = 0
            self.note_score = 0

            ## Music track playback status
            self.playback_active = False

            ## Is the beatmap still running?
            self.running = {"left" : True, "right" : True}
            self.epoch = 0.0

            ## Pressing the keys (or the area on a touch screen)
            self.left = False
            self.right = False


        ## ------------------------------------------------------------------ ##
        ## Methods for internal use of RhythmBeats

        def tap_events(self, ev, x, y, st):
            """
            (UNDOCUMENTED) 
            This method collects pygame events to recognize touches 
            of the player in the game.
            """

            ## Get the state of the game keys.
            if renpy.windows or renpy.linux:
                keys = pygame.key.get_pressed()
                self.left = keys[self.left_key]
                self.right = keys[self.right_key]


        def get_note_score(self, diff):
            """
            (UNDOCUMENTED) 
            This method calculates a score for each musical note, based on 
            of the milliseconds of offset obtained when playing a note. 
            The score obtained per note is inversely proportional to the time 
            offset when playing a note, so lower precision will give 
            less points per note."""

            diff = abs(diff) * 1000.0
            max_time = self.threshold * 1000.0

            rv = int(self.max_score - (self.max_score * (diff / max_time)))

            return rv


        def map_callback(self, st):
            """
            (UNDOCUMENTED) 
            This method is responsible for computing player interactions, 
            in order to determine if the player hits or misses any note. 
            The rhythmic system operates with respect to a given epoch time. 
            in seconds, provided by a SpriteManager() without displayables. 

            It does not return any value important to the developer or the player."""

            ## Play the song
            if not self.playback_active:
                renpy.music.play(self.song_file, channel="music", loop=False, tight=True)
                self.playback_active = True

            ## ------------------------------------------------------------------ ##
            ## Area of interactions

            if self.is_running():
                self.epoch = round(st, 2)

            if self.left:
                self.key_tap["left"] = st
            if self.right:
                self.key_tap["right"] = st

            ## ------------------------------------------------------------------ ##
            ## Tap analysis area

            ## Determines if the index of each note row has come to an end
            self.running["left"] = self.note_pass["left"] < len(self.lane_L)
            self.running["right"] = self.note_pass["right"] < len(self.lane_R)

            ## Get the difference between the timestamp of the key and the beatmap
            DIFF_L = self.key_tap["left"] - self.lane_L[self.index["left"]]
            DIFF_R = self.key_tap["right"] - self.lane_R[self.index["right"]]

            ## Gets if the played note is within the detection threshold
            HIT_L = all((DIFF_L >= -self.threshold, DIFF_L <= self.threshold))
            HIT_R = all((DIFF_R >= -self.threshold, DIFF_R <= self.threshold))

            ## Gets if the current timestamp has been ignored by the player
            BAD_L = all((st - self.threshold > self.lane_L[self.index["left"]], self.key_tap["left"] < st + self.threshold))
            BAD_R = all((st - self.threshold > self.lane_R[self.index["right"]], self.key_tap["right"] < st + self.threshold))

            ## ------------------------------------------------------------------ ##
            ## Computer area

            ## Keypad L
            if HIT_L and self.running["left"]:
                self.index["left"] += 1 if self.index["left"] < len(self.lane_L) -1 else 0
                self.timestamp_log.append(DIFF_L)
                self.note_pass["left"] += 1
                self.combo += 1
                self.perfect += 1
                self.stage_score += self.get_note_score(DIFF_L)
                self.note_score = self.get_note_score(DIFF_L)

                self.last_tap = DIFF_L * 1000.0

            elif BAD_L and self.running["left"]:
                if not self.failsafe:
                    renpy.play(self.miss_sound, channel = "audio")
                    self.combo = 0
                    self.miss += 1

                self.index["left"] += 1 if self.index["left"] < len(self.lane_L) -1 else 0
                self.note_pass["left"] += 1
                self.note_score = 0


            ## Keypad R
            if HIT_R and self.running["right"]:
                self.index["right"] += 1 if self.index["right"] < len(self.lane_R) -1 else 0
                self.timestamp_log.append(DIFF_R)
                self.note_pass["right"] += 1
                self.combo += 1
                self.perfect += 1
                self.stage_score += self.get_note_score(DIFF_R)
                self.note_score = self.get_note_score(DIFF_R)

                self.last_tap = DIFF_R * 1000.0

            elif BAD_R and self.running["right"]:
                if not self.failsafe:
                    renpy.play(self.miss_sound, channel = "audio")
                    self.combo = 0
                    self.miss += 1

                self.index["right"] += 1 if self.index["right"] < len(self.lane_R) -1 else 0
                self.note_pass["right"] += 1
                self.note_score = 0

            ## This constantly updates a tuple with the progress of the beatmap. 
            self.map_progress = (self.note_pass["left"] + self.note_pass["right"], len(self.lane_L + self.lane_R))

            return 0.016 ## ~60 Hz


        def sprite_creator(self):
            """
            (UNDOCUMENTED) 
            This method creates 'n' number of sprites for the SpriteManager() 
            depending on the number of notes in the beatmap."""

            def add_note(timestamp, lane):
                sprite = self.waterfall_mgr.create(self.displayable)
                sprite.x = 642 if lane == "LEFT" else 1147
                sprite.y = -120

                self.spritegroup.append((sprite, timestamp, lane))

            for left, right in self.beatmap_object():
                if isinstance(left, float):
                    add_note(left, "LEFT")
                if isinstance(right, float):
                    add_note(right, "RIGHT")
            self.spritegroup = tuple(self.spritegroup)


        def notetrace(self, moverange, heading, timestamp, epoch):
            """
            (NO DOCUMENTADO)
            This function calculates the coordinates of the notes that are falling, 
            regarding the timestamp of that note and the current epoch time."""

            trace = abs(moverange[0] - moverange[1])
            start = epoch - (timestamp - self.map_delta)
            timerange = (epoch * start) / timestamp

            if heading == "Y":
                rv = (trace * timerange) - abs(moverange[0])

                if rv < moverange[0]:
                    rv = moverange[0]
                elif rv > moverange[1]:
                    rv = moverange[1]

            return rv


        def waterfall_callback(self, st):
            """
            (UNDOCUMENTED) 
            This method updates the position of each note in the waterfall 
            visible on the screen."""

            for sp, stamp, lane in self.spritegroup:
                if lane=="LEFT" and st > stamp - self.map_delta:
                    sp.y = self.notetrace((-120, 805), "Y", stamp, st)

                if lane=="RIGHT" and st > stamp - self.map_delta:
                    sp.y = self.notetrace((-120, 805), "Y", stamp, st)

                if st > stamp + 0.9:
                    sp.destroy()

            return self.waterfall_tick


        ## ------------------------------------------------------------------ ##
        ## Methods for external use (End user)

        def load(self):
            """This method loads and processes the sequences of a beatmap file from 
            a specific song.  The `.beat` file must be pointed to in the 
            when an instance of the class is created. 

            This must be called after instantiating the class.  does not receive any 
            argument ni tampoco return the data."""

            logger("Process", "Loading beatmap...")

            try:
                with renpy.file(self.fn, "UTF-8") as beatmap:
                    logger("Stats", "Relative path: %s." % self.fn)
                    logger("Debug", beatmap)

                    bmpdata = beatmap.readlines()

                    for keypad in bmpdata[1:]:
                        keypad = keypad.replace("\n", "").replace("\r", "").split("|")

                        left = keypad[0]
                        right = keypad[1]

                        if left != "" or right != "":
                            if not "End" in left:
                                self.lane_L.append(eval(left) + self.offset)

                            if not "End" in right:
                                self.lane_R.append(eval(right) + self.offset)

                    ## Casting from list to tuple
                    self.lane_L = tuple(self.lane_L)
                    self.lane_R = tuple(self.lane_R)

                    logger("Stats", "Offset final: %ss." % self.offset)
                    logger("Stats", "Full Combo: %s notas." % (len(self.lane_L) + len(self.lane_R)))

                    beatmap.close()

                    logger("Process", "Preparing waterfall (SpriteManager)...")
                    self.sprite_creator()
                    logger("OK", "Beatmap ready to run.\n")

            except Exception as open_error:
                raise RhythmBeatsException("(%s) %s" % (type(open_error), str(open_error)))


        def beatmap_object(self):
            """This method returns an iterable `itertools.zip_longest` object with the 
            beatmap to display the taps on a screen.  This helps 
            iterate the beatmap with only 1 for loop on a screen =D 

            This must be called after instantiating the class.  does not receive any 
            arguments in particular."""

            return itertools.zip_longest(self.lane_L, self.lane_R, fillvalue = "End")


        def accuracy_rate(self):
            """
            This method returns a tuple with the average precision of the player 
            during the game, and the reaction tendency (behind or ahead) 
            with arrows. 

            **Return format:** 
            (Average reaction time, reaction trend) 

            Average precision values ​​are returned in milliseconds, while 
            that the reaction trend arrows are returned as unicode strings. 
            You can use this method to obtain statistics during the game or 
            at the end =D"""

            average_ms = 0.0

            ## This conditional prevents a possible ZeroDivisionError exception.
            if len(self.timestamp_log) > 0:
                average_ms = round(sum(self.timestamp_log) / len(self.timestamp_log), 4) * 1000.0

            if average_ms == 0.0:
                reaction = u"{font=DejaVuSans.ttf}⇋{/font}"
            elif average_ms < 0.0:
                reaction = u"{font=DejaVuSans.ttf}◂{/font}"
            elif average_ms > 0.0:
                reaction = u"{font=DejaVuSans.ttf}▸{/font}"

            return abs(average_ms), reaction


        def is_running(self):
            """This method returns `True` if the map is still running. In the 
            otherwise, it returns `False` if all the notes in the 
            Beatmap."""

            return self.running["left"] or self.running["right"]
