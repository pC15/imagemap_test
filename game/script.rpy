# Imagemap demo based on Skarn's navigation map tutorial
image bg stanford = "images/stanford_base.png"
image bg campus = "images/campus_base.png"


# The game starts here.
label start:
    $ been_oval = False
    $ been_quad = False
    $ been_church = False
    $ been_history = False
    $ been_math = False
    $ been_geology = False
    $ been_langs = False
    $ been_library = False
    $ been_lib = False
    $ been_cafe = False
    $ been_design = False
    $ been_engin = False
    $ been_theater = False
    
    menu:
        "Which Imagemap do you want to play?"
        
        "Version 1":
            scene bg stanford
            "This is an imagemap demo"
            jump stanford
            
        "Version 2":
            scene bg campus
            "This is another imagemap demo"
            jump campus


label campus:
    call screen campus_map
    
label lib:
    scene bg campus
    if been_lib:
        "You've already been here. Time to go home."
        return
    "It's the Library."
    "I heard you can live in the archives, if you get kicked out of housing."
    "... Not going to chance it though."
    $ been_lib = True
    jump campus
    
label cafe:
    scene bg campus
    if been_cafe:
        "You've already been here. Time to go home."
        return
    "It's the Cafe."
    "Why am I so hungry?"
    "Maybe because I walk past the cafe all the time?"
    $ been_cafe = True
    jump campus
    
label engin:
    scene bg campus
    if been_engin:
        "You've already been here. Time to go home."
        return
    "It's the Engineering Lab."
    "Domo arigato, Mr. Roboto."
    "Thank you, gozaimasu."
    $ been_engin = True
    jump campus
    
label design:
    scene bg campus
    if been_design:
        "You've already been here. Time to go home."
        return
    "It's the Design Lab."
    "Sew, sew, fashion baby."
    "Work it, make that dress look c-ra-zy!"
    $ been_design = True
    jump campus
    
label theater:
    scene bg campus
    if been_theater:
        "You've already been here. Time to go home."
        return
    "It's the Theater."
    "But, Sempai! I love your shortness!"
    "A sempai is hitting his kouhai for being dumb."
    "I... should probably leave now."
    $ been_theater = True
    jump campus
    
label stanford:
    call screen stanford_map

label the_oval:
    scene bg stanford
    if been_oval:
        "You've already been here. Time to go home."
        return
    "It's The Oval." 
    "Quite a bit of 'grass' here, hee hee."
    "...Never change, Cali."
    $ been_oval = True
    jump stanford
    
label main_quad:
    scene bg stanford
    if been_quad:
        "You've already been here. Time to go home."
        return
    "It's the Main Quad." 
    "Kinda quiet. Maybe everyone's in class?"
    $ been_quad = True
    jump stanford
    
label church:
    scene bg stanford
    if been_church:
        "You've already been here. Time to go home."
        return
    "It's the Memorial Church."
    "If God is always listening, do they hear my silent farts?"
    $ been_church = True
    jump stanford
    
label history:
    scene bg stanford
    if been_history:
        "You've already been here. Time to go home."
        return
    "It's the History Corner."
    "Four score and seven years ago, I was not alive."
    $ been_history = True
    jump stanford
    
label math:
    scene bg stanford
    if been_math:
        "You've already been here. Time to go home."
        return
    "It's the Math Corner."
    "I know my calculus. It says U + ME = US~."
    "Man, I love that song."
    $ been_math = True
    jump stanford
    
label geology:
    scene bg stanford
    if been_geology:
        "You've already been here. Time to go home."
        return
    "It's the Geology Corner."
    "We will~, we will~, ROCK YOU!"
    "What time's the rock concert at?"
    $ been_geology = True
    jump stanford
    
label langs:
    scene bg stanford
    if been_langs:
        "You've already been here. Time to go home."
        return
    "It's the Language Corner."
    "...I can't understand a word anyone says."
    $ been_langs = True
    jump stanford
    
label library:
    scene bg stanford
    if been_library:
        "You've already been here. Time to go home."
        return
    "It's the Library."
    "Shh, the books are sleeping!"
    $ been_library = True
    jump stanford


return
