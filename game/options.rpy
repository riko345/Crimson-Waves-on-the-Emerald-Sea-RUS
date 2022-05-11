













define config.name = _("Crimson Waves on the Emerald Sea")





define gui.show_name = False




define config.version = "0.99.2"

define config.steam_appid = 1804970

define achievement.steam_position = "top left"





define gui.about = _p("""
""")






define build.name = "CWES"







define config.has_sound = True
define config.has_music = True
define config.has_voice = False













define config.main_menu_music = "audio/Asking Questions.mp3"










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 70





default preferences.afm_time = 15
















define config.save_directory = "CrimsonWavesontheEmeraldSea-1632278569"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)



    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')




    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
