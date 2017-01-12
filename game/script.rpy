# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init:
    #Picaud Sprites
    image picaud normal = "resource/sprites/Picaud/Normal.png"
    image picaud challenge = "resource/sprites/Picaud/Challenge.png"
    image picaud embarassed = "resource/sprites/Picaud/Embarassed.png"
    image picaud hard = "resource/sprites/Picaud/Hard.png"
    image picaud hnm = "resource/sprites/Picaud/HnM.png"
    image picaud understanding = "resource/sprites/Picaud/Understanding.png"
    image picaud normal2 = "resource/sprites/Picaud/Normal-2.png"
    image picaud challenge2 = "resource/sprites/Picaud/Challenge-2.png"
    image picaud embarassed2 = "resource/sprites/Picaud/Embarassed-2.png"
    image picaud hard2 = "resource/sprites/Picaud/Uncertainty-Hard-2.png"
    image picaud hnm2 = "resource/sprites/Picaud/HnM-2.png"
    image picaud Understanding2 = "resource/sprites/Picaud/Understanding-2.png"

    #Picaud Radheya
    image radheya angry = "resource/sprites/Radheya/Angry.png"
    image radheya deep = "resource/sprites/Radheya/Deep.png"
    image radheya determined = "resource/sprites/Radheya/Determined.png"
    image radheya happy = "resource/sprites/Radheya/Happy.png"
    image radheya normal = "resource/sprites/Radheya/Normal.png"
    image radheya pity = "resource/sprites/Radheya/Pity.png"

    #Background Image
    image throne = "resource/images/throne.jpg"
    image throne fade:
        contains:
            "resource/images/throne.jpg"
            alpha 1.0
        contains:
            "resource/images/throne.jpg"
            alpha 0.2 xoffset -3
        contains:
            "resource/images/throne.jpg"
            alpha 0.2 xoffset +3
        contains:
            "resource/images/throne.jpg"
            alpha 0.2 yoffset -3
        contains:
            "resource/images/throne.jpg"
            alpha 0.2 yoffset +3

# Declare characters used by this game.
define narrator_centered = Character(None,
                          what_size=20, #Font size
                          what_xalign=0.5, #Centers text within the window
                          window_xalign=0.5, #Centers the window horizontally
                          window_yalign=0.5, #Centers the window vertically
                          what_text_align=0.5, #Centers text within the window, just in case
                          window_background=None,#Removes the window, so only the text shows
                          window_ymaximum=300,
                          window_yminimum=0,
                          window_xfill=False,
                          what_layout="subtitle",
                          what_outlines=[(3, "#000000", 2, 2), (3, "#808080", 0, 0)],
                          #Gives an outline
                          what_slow_cps=30 #Speed at which the text appears (slow)
                          )
define narrator = Character(what_suffix = ' ▼', what_slow_cps=30)
define radheya = Character('{b}Radheya{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define picaud = Character('{b}Picaud{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define unknown_B = Character('{b}???-2{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define unknown_A = Character('{b}???{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)

#Background Music
define audio.bgm = "resource/music/gate-of-steiner.mp3"


# The game starts here.
label start:
    play music bgm
    scene throne fade

    narrator_centered "Empty throne, a lone man standing beside it."

    narrator_centered "Never mind sitting, he even does not let a speck of dust near that empty chair."

    scene throne with dissolve
    show picaud normal with dissolve

    unknown_A "My liege."

    hide picaud normal
    show radheya deep with dissolve

    radheya "Cut your mouth. I am not your ruler."

    hide radheya deep
    show picaud hard

    unknown_A "My apology, lord Radheya.{w=0.5}{nw}"

    hide picaud hard
    show picaud normal
    extend " I’ve come to inform you about our progress."

    hide picaud normal
    show radheya normal

    radheya "Just Radheya is fine. How far does it make again today?"

    hide radheya normal
    show picaud hard

    unknown_A "The laboratory confirms that we can enhance even further by using our blood vials as the driver energy fuel. It’s still just a theory, but we may need a real field test."

    show radheya deep
    hide picaud hard

    narrator "Radheya looks away, his mind seems to be over something."

    hide radheya deep
    show picaud normal

    unknown_A "Radheya?"

    hide picaud normal
    show radheya pity

    radheya "Mind me, Picaud. I can’t help but feel uneasy."

    hide radheya deep
    show picaud hard

    picaud "Is it about him?"

    hide picaud hard
    show radheya pity

    radheya "Yes…. This matter is more unnerving than I thought. We need him to continue this."

    hide radheya pity
    show picaud normal

    picaud "I don’t concur. Just you enough is fine. We just need to took the belt."

    hide picaud normal
    show radheya angry with vpunch

    radheya "{size=+10}INSOLENCE!!{/size}"

    narrator "With an aura, Radheya extorts"

    hide radheya angry
    show radheya deep

    radheya "To disrespect him is to rape and kill my pride. Do you got a death wish, Pierre Picaud?"

    hide radheya deep
    show picaud understanding

    picaud "…"

    hide picaud understanding
    show picaud normal

    picaud "Aah, what you can do then Radheya? Your strength is still at a great loss from that incident. You can never harm me."

    hide picaud normal
    show radheya deep

    radheya "That’s true. But I don’t need my strength to kill you right here and now."

    hide radheya deep
    show picaud normal

    picaud "I was just voicing my opinion. I believe what I say to be the best for our kin. You should lead us to glory."

    hide picaud normal
    show radheya deep

    narrator "The white-red lord glares, then sigh away while looking at the fleeting air."

    hide radheya deep
    show picaud normal

    picaud "No comment?"

    hide picaud normal
    show picaud understanding

    extend " Huh, I should take my leave then."

    hide picaud understanding
    show picaud hard

    picaud "Think well of my words, Radheya. You are the leader of us."

    hide picaud hard with dissolve
    show radheya deep

    narrator "Sound of shoes steps echoing in the throne room. Leaving Radheya alone in his thought."

    radheya "My Friend…."



    return
