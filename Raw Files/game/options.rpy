## Basics ######################################################################

define config.name = _("A normal teenager's life")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


define build.name = "LifeIsStrange"


## Sounds and music ############################################################

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################

define config.enter_transition = dissolve
define config.exit_transition = dissolve

define config.intra_transition = dissolve


define config.after_load_transition = None

define config.end_game_transition = None


## Window management ###########################################################

define config.window = "auto"

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

default preferences.text_cps = 0

default preferences.afm_time = 15

define config.save_directory = "VisualNovel-1772474136"


## Icon ########################################################################

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################

init python:

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.documentation('*.html')
    build.documentation('*.txt')

define build.itch_project = "renpytom/Visual-Novel"
