init:
  image note_img = "gui/rhythm_note.png"
  image lane_img = "gui/rhythm_lane.png"

screen note_waterfall():
  zorder 102
  modal True

  add "lane_img"

  add game_instance.map_mgr
  add game_instance.waterfall_mgr

screen game_hud():
  zorder 102

  if game_instance.is_running():
    if game_instance.miss < 15:
      vbox:
        pos(0.1, 0.1)
        text "Notes hit: %s" % game_instance.perfect
        text "Notes missed: %s" % game_instance.miss
        text "Combo: %s" % game_instance.combo
    else:
      python:
        ui.close()
        renpy.jump("stage_failed")
  else:
    python:
      ui.close()
      renpy.jump("stage_cleared")

init python:
  config.per_frame_screens.append("game_hud")

label start_game:
  python:
    game_instance = RhythmPlayground(
      fn = "beatmaps/beatmap_placeholder.txt",
      displayable = Transform("note_img", zoom=1.00),
      song_file = "songs/rhythmgame_placeholder.mp3",
      offset_map = 0.0,
      offset_game = 0,
      failsafe = True
    )
    game_instance.load()

  show screen game_hud
  call screen note_waterfall

label stage_cleared:
  hide screen game_hud
  hide screen note_waterfall

  $del game_instance
  jump chapter1_scene6

label stage_failed:
  hide screen game_hud
  hide screen note_waterfall

  $del game_instance
  return #TODO: create "game over" screen with retry option