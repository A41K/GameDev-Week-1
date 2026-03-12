define Abigel = Character("Abigel", color="#f5ff69")
define James = Character("James", color="#69f5ff")
define N = Character("Narator", color="#808080")
define timeskip = Character("TIMESKIP", color="#ff69f5")
define Bird = Character("Bird", color="#69ff69")

default progression_points = 0

image nroom:
    "images/narator_room.webp"
    zoom 2

image outside:
    "images/outsidebig.jpg"
    zoom 3

image abigel happy:
    "images/Abigel.webp"
    zoom 0.5

image james happy:
    "images/James.jpg"
    zoom 1

image James:
    "images/James.jpg"
    zoom 1

image Abigel:
    "images/Abigel.webp"
    zoom 1.5

image bird:
    "images/bird.png"
    zoom 0.5

image school:
    "images/school.jpg"
    zoom 2

image park:
    "images/bgdeak.jpg"
    zoom 0.75

image dohi:
    "images/bgdohi2.jpg"

image dorm:
    "images/dorm.jpg"
    zoom 0.75

image party:
    "images/bgpeaches.png"

image night:
    "images/night.jpg"

image bird:
    "images/bird.png"
    zoom 0.5



label start:
    scene nroom

    timeskip "PRELUDE - The Park"

    N "There was once a beautiful time in a beautiful place. two people who seem far away started closing in the distance"

    N "You could feel the spark in their eyes. It could light a whole forest on fire, but it wasn't always like that"

    scene outside

    show james happy at truecenter

    James "You know It's beautiful outside isn't it?" 

    hide james happy

    show abigel happy at truecenter

    Abigel "Yes, it is. I love the smell of the flowers and the sound of the birds. It's so peaceful here."

    hide abigel happy

    show james happy at truecenter

    James "Y'know I felt more peace everytime when we were here, together then elsewhere."
    James "It's like nature is more greener because of us."

    hide james happy

    show abigel happy at truecenter

    Abigel "Yeah, I see it now. There's more birds here too"

    hide abigel happy

    show bird at truecenter

    Bird "*Tweet tweet Chirp Chirp Tweet*"
    Abigel "See? Even the birds are happier when we're here."
    
    menu:
        "What should you say?"
        "I guess...":
            jump maybe
        "Can we just leave now.":
            jump no
        "Yeah, you're right. I feel it too.":
            jump yes

    hide bird

    label maybe:
        show james happy at truecenter

        James "I guess... I just feel like something is different here. Like we're more connected to nature or something."

        hide james happy

        show abigel happy at truecenter

        Abigel "I know what you mean. It's like we're in a different world when we're here."

        hide abigel happy

        jump timeskip1
    
    label no:
        show james happy at truecenter
        James "Can we just leave now? I don't really feel like being here anymore."

        hide james happy

        show abigel happy at truecenter

        Abigel "Oh, okay. I guess we can go if you want to."

        hide abigel happy

        jump timeskip2

    label yes:
        show james happy at truecenter

        James "Yeah, you're right. I feel it too."

        hide james happy

        show abigel happy at truecenter

        Abigel "I know, right? It's like the world is a little bit brighter when we're here."

        hide abigel happy

        jump timeskip1

    label timeskip2:
    N "And so, they left the beautiful place and went back to their normal lives, but they couldn't help but feel like something was missing."
    timeskip "TIME SKIP - LATER THAT DAY"
    jump school


    label timeskip1:
    N "And so, they continued to spend time together in that beautiful place, enjoying each other's company and the beauty of nature around them"
    timeskip "TIME SKIP - LATER THAT DAY"
    jump school


label school:
    
    scene school

    timeskip "CHAPTER 1 - School"

    N "You are now at school. Do you want to go to class or just skip it?"
    menu Decision:
        "What do you want to do?"
        "Go to class":
            N "Its chemistry class one of your favorites."
            jump chemistry
        "Skip class":
            $ progression_points += 1
            N "Your actions will be remembered"
            N "You skipped class and instead went with the other classes guys outside to have some fun. They were on recess"
            jump recess



    
define Frank = Character("Frank", color="#ff6969")
define Ashley = Character("Ashley", color="#69ff69")
define Kane = Character("Kane", color="#6969ff")
define Teacher = Character("Teacher", color="#ff69f5")
define Phone = Character("Phone", color="#f5ff69")

image Frank:
    "images/Frank.jpg"
    zoom 0.5

image Ashley:
    "images/Ashley.webp"
    zoom 0.5

image Kane:
    "images/Kane.jpg"
    zoom 0.5

image Teacher:
    "images/Teacher.jpg"
    zoom 0.5

label recess:

        scene park

        show Frank at truecenter

        Frank "Hey what's up James I thought you had class?"
        
        hide Frank

        show James at truecenter

        James "Yeah I just skipped it. I already know it so it's just noise for me"
        
        hide James

        show Ashley at truecenter

        Ashley "Hey James good to see you here"

        hide Ashley

        show james at truecenter

        James "So what do we want to do today?"

        hide james

        show Kane at truecenter

        Kane "We were thinking on buying some ZYN for the weekend, and then just walk around town"

        hide Kane

        show James at truecenter

        James "That sounds like a great idea, I'm down for that"

        hide James

        jump Store

label chemistry:

        N "You went to class and sat down next to Abigel."

        show Abigel at truecenter

        Abigel "Hey James, I'm glad you came to class today."
        
        hide Abigel

        show James at truecenter

        James "Yeah, I just didn't want to miss out on the fun we had yesterday."
        
        hide James

        show Abigel at truecenter

        Abigel "I know, right? It was so much fun. I'm glad we got to spend time together like that."

        hide Abigel

        show James at truecenter

        James "We laughed so hard that we almost got an F"

        hide James

        N "The class went on as usual. You actually listened and Abigel just slept and didn't really care."
        
        menu:
            "What do you want to do?"
            "Go to your dorm":
                N "You went to your dorm"
                jump dorm
            "Go to the store":
                N "You went to the store and met up with your friends"
                jump Store

label Store:

        scene dohi

        show Frank at truecenter
        Frank "So, we want 4 packs and then some alcohol right?"
        hide Frank

        show Ashley at truecenter
        Ashley "Yeah, that's right. We also want some snacks for the weekend"
        hide Ashley

        show Kane at truecenter
        Kane "Don't forget the alcohol, we need that for sure"
        hide Kane

        N "You guys bought 4 packs of ZYN two bottles of whiskey and some snacks"

        show James at truecenter
        James "This round is on me"
        hide James

        show Frank at truecenter
        Frank "Nah you bought last time so it's my turn to buy"
        hide Frank
        jump teacher

label teacher:
    
        if progression_points >= 1:
            N "As you were leaving the store, you ran into your chemistry teacher. He looked at you with a disappointed look on his face."
                
            show Teacher at truecenter

            Teacher "James, I thought you were a good student. I can't believe you would skip
            class like that. I'm really disappointed in you."

            hide Teacher

            show James at truecenter

            James "I'm sorry, I just didn't feel like going to class today. I already know the material so it felt like a waste of time."

            hide James

            show Teacher at truecenter

            Teacher "I understand that, but you still have a responsibility to attend class and learn. Skipping class is not acceptable behavior."
               
            hide Teacher

            N "The teacher then gave you a warning and told you that if you skip class again, there will be consequences."

            $ progression_points -= 1
            
        else:
            N "As you were leaving the store, you ran into your chemistry teacher. He looked at you with a smile on his face."

            show Teacher at truecenter

            Teacher "Hey James, I just wanted to say that I'm really proud of you for coming to class today. I know it can be tough to stay motivated sometimes, but I'm glad you're taking your education seriously."

            hide Teacher

            show James at truecenter

            James "Thank you, I just didn't want to miss out on the fun we had yesterday. I know it's important to attend class and learn, so I made sure to come today."

            hide James

            show Teacher at truecenter

            Teacher "That's great to hear, James. Keep up the good work and let me know if you ever need any help with the material."

            hide Teacher

            $ progression_points -= 1

label dorm:

    N "You went to your dorm and layed down in your bed"

    scene dorm

    show James at truecenter

    James "I had so much fun toda..."

    Phone "bzzz bzzz bzzz"

    James "Oh, it's my phone. I wonder who it is."

    Phone "You have a new message from Ashley"

    James "Oh, it's Ashley. I wonder what she wants."

    Phone "Hey James, do you want to hang out later? Just us two y'know"

    menu:
        "What do you want to do?"
        "Sure, that sounds great!":
            N "You agreed to hang out with Ashley later."
            jump withashley
            $ progression_points += 1

        "Sorry, I already have plans. Maybe another time?":
            N "You declined Ashley's invitation to hang out."
            jump dorm2

label withashley:
    
    scene park

    N "You and ashley met up at the park"

    show Ashley at truecenter

    Ashley "Hey James, I'm really glad we could hang out today."
        
    hide Ashley

    show James at truecenter

    James "Yeah, me too. I always have a great time when we're together."

    James "So, where do you want to go?"

    hide James

    show Ashley at truecenter

    Ashley "I thought maybe we could go out and party"

    hide Ashley

    show James at truecenter

    James "That sounds like a great idea, I'm down for that."
        
    hide James

    jump party

label party:

    scene party

    N "You and Ashley went out to party together. It was loud, there were a lot of people there."
    N "You both started drinking and having fun. You danced, you laughed, you had a great time together."
    N "And then as the night whent on you both got more and more tipsy"

    show Ashley at truecenter
    Ashley "Jamesssss I love youuuuu"
    hide Ashley 

    show James at truecenter
    James "You're just drunk Ashley, you don't know what you're saying"
    hide James

    show Ashley at truecenter
    Ashley "Immmm haviiiinngg sooo muuchh fuuunn"
    hide Ashley

    N "You both continued partying, drinking and dancing"
    N "A few hours later the party ended and you both stated stumbling back to your dorm"

    scene night

    show James at truecenter
    James "Grab on me."
    hide James

    show Ashley at truecenter
    Ashley "Okay, I'm really tired and I don't think I can walk on my own."
    hide Ashley

    N "You helped Ashley walk back to your dorm and then you both went to sleep"

    jump options
    
    
label dorm2:

    scene dorm

    N "You decided to stay in your dorm and relax for the rest of the day."
    N "You got a knock at your door"

    Abigel "Can I come in?"

    James "Sure, come on in."

    N "Abigel came in and sat down on your bed."

    show Abigel at truecenter

    Abigel "I have something to tell you James, Something important"

    hide Abigel

    show James at truecenter

    James "What is it Abigel? You can tell me anything."

    hide James

    show Abigel at truecenter

    Abigel "I know we haven't been together for that long, but I really like you James. I think I'm falling for you."
        
    hide Abigel

    show James at truecenter

    James "Abigel, I really like you too. I think I'm falling for you as well."

    hide James

    jump options

label options:
    
    timeskip "CHAPTER 2 - The Options"
        
    if progression_points >= 1:
        N "You woke up with Ashley being next to you. You had a great time last night, but you couldn't help but feel guilty about it. You had just started talking to Abigel and you really liked her, but you also had a great time with Ashley"
    else:
        N "Abigel had shocked you with her confession, but you couldn't help but feel happy that she felt that way about you."






return