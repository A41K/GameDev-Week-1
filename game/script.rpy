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
    "images/outside.jpg"
    zoom 1

image james happy:
    "images/outside.jpg"
    zoom 1

image James:
    "images/james.png"
    zoom 0.5

image Abigel:
    "images/abigel.png"
    zoom 0.5

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


label start:
    scene nroom

    timeskip "PRELUDE - The Park"

    N "There was once a beautiful time in a beautiful place. two people who seem far away started closing in the distance"

    N "You could feel the spark in their eyes. It could light a whole forest on fire, but it wasn't always like that"

    scene outside

    show james happy at center

    James "You know It's beautiful outside isn't it?" 

    hide james happy

    show abigel happy at center

    Abigel "Yes, it is. I love the smell of the flowers and the sound of the birds. It's so peaceful here."

    hide abigel happy

    show james happy at center

    James "Y'know I felt more peace everytime when we were here, together then elsewhere."
    James "It's like nature is more greener because of us."

    hide james happy

    show abigel happy at center

    Abigel "Yeah, I see it now. There's more birds here too"

    hide abigel happy

    show bird at center

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
        show james happy at center

        James "I guess... I just feel like something is different here. Like we're more connected to nature or something."

        hide james happy

        show abigel happy at center

        Abigel "I know what you mean. It's like we're in a different world when we're here."

        hide abigel happy

        jump timeskip1
    
    label no:
        show james happy at center
        James "Can we just leave now? I don't really feel like being here anymore."

        hide james happy

        show abigel happy at center

        Abigel "Oh, okay. I guess we can go if you want to."

        hide abigel happy

        jump timeskip2

    label yes:
        show james happy at center

        James "Yeah, you're right. I feel it too."

        hide james happy

        show abigel happy at center

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

    label recess:
        scene park

        show Frank at center

        Frank "Hey what's up James I thought you had class?"
        
        hide Frank

        show James at center

        James "Yeah I just skipped it. I already know it so it's just noise for me"
        
        hide James

        show Ashley at center

        Ashley "Hey James good to see you here"

        hide Ashley

        show james at center

        James "So what do we want to do today?"

        hide james

        show Kane at center

        Kane "We were thinking on buying some ZYN for the weekend, and then just walk around town"

        hide Kane

        show James at center

        James "That sounds like a great idea, I'm down for that"

        hide James

        jump Store

    label chemistry:
        N "You went to class and sat down next to Abigel."

        show Abigel at center

        Abigel "Hey James, I'm glad you came to class today."
        
        hide Abigel

        show James at center

        James "Yeah, I just didn't want to miss out on the fun we had yesterday."
        
        hide James

        show Abigel at center

        Abigel "I know, right? It was so much fun. I'm glad we got to spend time together like that."

        hide Abigel

        show James at center

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

        show Frank at center
        Frank "So, we want 4 packs and then some alcohol right?"
        hide Frank

        show Ashley at center
        Ashley "Yeah, that's right. We also want some snacks for the weekend"
        hide Ashley

        show Kane at center
        Kane "Don't forget the alcohol, we need that for sure"
        hide Kane

        N "You guys bought 4 packs of ZYN two bottles of whiskey and some snacks"

        show James at center
        James "This round is on me"
        hide James

        show Frank at center
        Frank "Nah you bought last time so it's my turn to buy"
        hide Frank
        jump teacher

        label teacher:
            if progression_points >= 1:
                N "As you were leaving the store, you ran into your chemistry teacher. He looked at you with a disappointed look on his face."
                
                show Teacher at center

                Teacher "James, I thought you were a good student. I can't believe you would skip
                class like that. I'm really disappointed in you."

                hide Teacher

                show James at center

                James "I'm sorry, I just didn't feel like going to class today. I already know the material so it felt like a waste of time."

                hide James

                show Teacher at center

                Teacher "I understand that, but you still have a responsibility to attend class and learn. Skipping class is not acceptable behavior."
               
                hide Teacher

                N "The teacher then gave you a warning and told you that if you skip class again, there will be consequences."
            
            else:
                N "As you were leaving the store, you ran into your chemistry teacher. He looked at you with a smile on his face."

                show Teacher at center

                Teacher "Hey James, I just wanted to say that I'm really proud of you for coming to class today. I know it can be tough to stay motivated sometimes, but I'm glad you're taking your education seriously."

                hide Teacher

                show James at center

                James "Thank you, I just didn't want to miss out on the fun we had yesterday. I know it's important to attend class and learn, so I made sure to come today."

                hide James

                show Teacher at center

                Teacher "That's great to hear, James. Keep up the good work and let me know if you ever need any help with the material."

                hide Teacher

    label dorm:
        N "You went to your dorm and layed down in your bed"

        show James at center

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
        N "You and ashley met up"

        show Ashley at center

        Ashley "Hey James, I'm really glad we could hang out today."
        
        hide Ashley

        show James at center

        James "Yeah, me too. I always have a great time when we're together."

        James "So, where do you want to go?"

        hide James

        show Ashley at center

        Ashley "I thought maybe we could go out and party"

        hide Ashley

        show James at center

        James "That sounds like a great idea, I'm down for that."
        
        hide James
    
    label dorm2:

    scene dorm

        N "You decided to stay in your dorm and relax for the rest of the day."
        N "You got a knock at your door"









    return