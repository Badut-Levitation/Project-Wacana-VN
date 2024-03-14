default current_day = 1
default label_list = []

define j = Character("Jenny", color = "#C0C0C0")
define k = Character("Kaze", color = "#8f6138")

transform z:
  zoom 0.5

# Main game loop
label start:
    while True:
    
        call initialize_day

        call character_transition_effect(True)

        call initialize_night

        call character_transition_effect(False)

        $ current_day += 1

    return

label initialize_day:

    scene bg apartment
    show kaze normal at left,z
    with fade
    k "Good morning"

    $ today_label = "day_" + str(current_day)
    call process_label(today_label)

    # TODO Update UI color, song, etc to suit day character

    return

label initialize_night:

    scene bg apartment_night
    show kaze sad at right,z
    with fade
    k "Good night"

    $ today_label = "night_" + str(current_day)
    call process_label(today_label)

    # TODO Update UI color, song, etc to suit night character

    return

label process_label(label_name = ""):

    if renpy.has_label(label_name):
        call expression label_name
    else:
        call Log("Couldn't find Label: " + label_name + ". Please check if the label actually exists." )

    python:
        for labels in label_list:
            renpy.call(labels)
    
    $ label_list = []
    return

label character_transition_effect(nightTime):

    scene bg livingroom_night
    # Efek ini cocok untuk flashback  
    with Fade(0.1, 0.0, 0.5, color="#fff") 

    if(nightTime):
        "Transition to night"
    else:
        "Transition to day"
    
    return

label Log(message = ""):
   
    "SYSTEM" "[message]"

    return