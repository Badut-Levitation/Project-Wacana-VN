# Daily action flag, set true to enable the activity
default day_activity_flag = False
default night_activity_flag = False
default current_day = 1

default label_list = []

define j = Character("Jenny", color = "#C0C0C0")
define k = Character("Kaze", color = "#8f6138")

transform z:
  zoom 0.5

label start:
    while True:
        $ label_list = []

        scene bg apartment
        show kaze normal at left,z
        with fade
        k "Good morning"

        $ today_label = "day_" + str(current_day)
        
        if renpy.has_label(today_label):
            call expression today_label

        python:
            for labels in label_list:
                renpy.call(labels)

        scene bg apartment_night
        show kaze sad at right,z
        with fade
        k "Good night" 

        scene bg livingroom_night
        # Efek ini cocok untuk flashback
        with Fade(0.1, 0.0, 0.5, color="#fff")  
        "Next day..."

        $ current_day += 1

    return


# label start:
#     while True:
#         call ResetActivityFlag()
        
#         scene bg apartment
#         show kaze normal at left,z
#         with fade

#         k "Good morning"

#         "Day[current_day]_day"
#         if renpy.has_label("Day[current_day]_day"):
#             call expression Day[current_day] + "_day"

# #region activity
#         if day_activity_flag:
#             call day_activity

#         if night_activity_flag:
#             call night_activity
# #endregion

#         if renpy.has_label("Day[current_day]_night"):
#             call expression Day[current_day] + "_night"

#         scene bg apartment_night
#         show kaze sad at right,z
#         with fade

#         k "Good night" 

#         scene bg livingroom_night
#         # Efek ini cocok untuk flashback
#         with Fade(0.1, 0.0, 0.5, color="#fff")  
#         "Next day..."
        
#         $ current_day += 1

#         if not renpy.has_label("Day[current_day]"):
#             jump ending
            
#     return

label ResetActivityFlag:
    $ day_activity_flag = False
    $ night_activity_flag = False
    return

label ending:
    "the end"
    return