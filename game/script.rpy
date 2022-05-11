




define c = Character("Cecil", color="#bcf7c1", image="cecil")
define cn = Character(" ", color="#fff", image="cecil", what_prefix='{i}', what_suffix='{/i}')
define nn = Character(" ", color="#fff", image="nemo", what_prefix='{i}', what_suffix='{/i}')
define n = Character("[nemoname]", color="#7bdaed", image="nemo")
define a = Character("Ambrose", color="#911418", image="ambrose")
define an = Character("Ambrose", color="#911418", image="ambrosen")
define l = Character("Lucie", color="#874cba", image="lucie")
define leland = Character("Leland", color="#9a4fab", image="leland")
define annie = Character("Annie", color="#a11b5a", image="annie")
define nar = Character(" ")
define na = Character("???")
define carm = Character("Carmila", color="#67578c")
define Cop = Character("Officer", color="#fff")
define guard = Character("Guard", color="#fff")
define man = Character("[manname]", color="#b1a5c2", image="npcman")
define Woman = Character("[womanname]", color="#c2a5b2", image="npcwoman")
define s = Character("Scott", color="#c2a5b2", image="scott")
define landon = Character("Landon", color="#dbbaa0")
define mary = Character("Marybelle", color="#d6859d")

default nemoname = "Nemo"
default manname = "Gentleman"
default womanname = "Lady"
default cecilpov = True
default chapter_num = "One"



label start:

    $ save_name = "Psychics and Charlatans"
    $ chapter_num = "One"

    call chapter from _call_chapter

    play music "audio/Isolation Waltz.mp3" fadein 1.5
    queue music "audio/Isolation Waltz.mp3"

    scene bg psychic:
        zoom 0.7
        yalign 0.25
        xalign 0.1
        linear 3.5 yalign 0.92
    with fade

    pause 2.5

    show cecil up frown at side

    cn frown "\"Psychic Corner - reconnect with loved ones across time and space\"."
    cn frown "Can they really help me find her...?"


    show npcfem1 at center:
        zoom 0.8



    with softeaseleft

    na "Oh, Monsieur!"
    na "Are you by any chance in need of something? Perhaps searching for something?"

    c frowntalk arm1 "H-How did you know?!"

    show cecil frown

    show npcfem1 at curtsy

    na "My name is Carmila. I see all, I know all."
    carm "Come in, my next session is about to start."

    show npcfem1 at curtsy
    show bg psychic at curtsy

    c frowntalk arm2 "O-Okay!"

    show cecil frown arm1


    scene bg room2:
        zoom 0.5
        yalign 0.4
    with fade

    $ nemoname = "Young Man"

    nar "The darkened interior of the shop smells strongly of frankincense. At best, it's overwhelming—at worst it's completely nauseating."
    nar "A group of downtrodden town folk and travelers are scattered around the room, keeping to themselves, as a well-dressed man walks around talking to people."

    show npcmasc3 at center:
        xalign 0.6
        zoom 0.8
    show cecil seance up frown at side
    with dissolve

    "Gentleman" "Hello there, young Monsieur."
    "Gentleman" "It's so rare to see such a young child with us. May I ask why you're paying us a visit here today?"

    c frowntalk "I-I'm looking for my neighbor!"
    c frowntalk arm2 "She's my best friend in the world!"

    show cecil frown

    "Gentleman" "Oh my, how sad! What has happened to her?"

    c frowntalk unsure arm3 eye2 "About a week ago she ran away from home and didn't tell me where or why. So now I'm looking for her."

    show cecil frown

    "Gentleman" "How noble of you, young Monsieur!"
    show cecil eye1 arm1
    "Gentleman" "With Miss Carmila's aid, I'm sure you'll find her."

    c up talk "Thank you!"

    show cecil smile

    scene bg room2:
        zoom 0.5
        yalign 0.4
    with dissolve

    nar "The gentleman walks away and starts conversing with a woman with a handkerchief in her hands for her tears."
    nar "After a few moments, Miss Carmila walks in the room and motions for us to follow her down a dark corridor into a candlelit chamber."

    scene seance cg 1:
        zoom 0.85
    show cecil seance up frown at side
    with fade

    carm "Come, let us all sit and show respect for the spirits here with us today."

    cn frown "Spirits...?"
    cn unsure arm2 "Eh? Like ghosts?!"
    show cecil arm1
    carm "For today's session, I ask you all for patience and guidance. The spirits are all around us and sometimes are disoriented."
    carm "Sometimes the words they tell me are meant for others in the room, or need more clarification that you can help me with. So, please treat me as the vessel for thoughts and help me translate them for you."
    show cecil up
    carm "In fact, I'm hearing some words right now... a sudden death... leaving a widow behind... Oh, how tragic."

    nar "The woman who had been crying into her handkerchief in the lobby raises her head."

    show cecil unsure

    carm "This man left the world all too soon and his betroden wife cannot move on yet."
    carm "I believe his wife is here in the audience with us, aren't you?"

    "Grieving Woman" "Y-Yes...! My husband passed away recently."

    carm "He is in the room with us."

    nar "Some people audibly gasp at her words."

    cn frown "He's here?!"

    carm "Mhmm... I see..."
    carm "Oh, dear... you tried your best, didn't you? Caring for him even in his sickness..."

    "Grieving Woman" "...!"
    "Grieving Woman" "Yes... He suddenly came down with an illness. Before I knew it, he..."

    carm "He's sad he cannot be with you any longer, but even more saddened to see you in such a state."
    carm "He wishes you well and hopes you will move on. That you will keep living in his memory."

    "Grieving Woman" "—!"
    "Grieving Woman" "Yes... Yes, of course! Ah, he's too kind, even now..."

    nar "The woman starts sobbing into her handkerchief again, trying her best to maintain some composure."

    cn up arm2 "Amazing..."

    show cecil arm1

    carm "I'm overjoyed I could help deliver such a happy message."
    carm "Even across the veil, I can receive and deliver such messages. Now, what is the next message..."

    nar "She closes her eyes and starts muttering a chant to herself."

    carm "I'm hearing a name... so many names at once, this will be difficult... Something that starts with an R? Maybe an M?"

    nar "The man across the table from the proprietoress perks up."

    "Weary Gentleman" "An M name?"

    carm "Yes, a name that starts with an M... Perhaps Matthew? Maybe a Michael? Hmm... Mark?"

    "Weary Gentleman" "Michael, yes!"

    carm "Ah, he's someone close to you, isn't he? A brother?"
    carm "No... your son?"

    "Weary Gentleman" "Yes!"
    "Weary Gentleman" "My son, Michael..."

    carm "Another tragic death, I can tell... Gone far before his time."
    carm "It was an accident, wasn't it?"

    "Weary Gentleman" "Yes... our son died in childbirth not long ago."

    carm "It wasn't your fault."
    carm "Nothing you could have done would have prevented this."
    carm "Your son wants you to move on from this. The spirits are telling me your next child will live past childbirth."

    "Weary Gentleman" "Really?!"
    "Weary Gentleman" "Thank you... thank you so much...!"

    nar "The esper gracefully dips her head with a cordial smile as the other guests clap."

    cn frown "Wow... she's able to communicate with the dead {/i}and{i} tell the future!"

    carm "Let us have a moment of silence while the spirits speak to me about our next guest."
    carm "Mmm... yes... oh, how my heart aches at hearing this..."
    carm "A missing friend..."

    c up "...!"

    show cecil frown

    show seance cg 1 as seancezoom:
        zoom 0.98
        xalign 0.74
        yalign 0.0
    with Dissolve(1.3)

    carm "A young child... a young girl, perhaps? Let me listen to the spirits a moment longer..."
    carm "...Yes, a young girl. Perhaps a sister? No... a close friend?"

    c frowntalk arm2 "Y-Yes! I'm looking for my best friend!"

    show cecil frown arm1

    carm "Ah, how sweet, you've run away from home to look for your dear friend."

    c frowntalk arm3 "I-I'm not a run away! I'm an orphan."

    show cecil frown

    carm "..."
    carm "Your friend is somewhere far away from here... It will take you a while to find her."
    show cecil arm1
    carm "The spirits tell me you'll find her, but she'll be resistant to going home."

    c frowntalk unsure "Why...?"

    show cecil frown

    carm "That is all the spirits are telling me at this moment."
    carm "I can tell though that you will find her safely."

    cn frown down "I'll find her... I'm going to find Lucie...!"




    hide seancezoom with Dissolve(1.2)

    show cecil up

    nar "Carmila straightens her shoulders and starts muttering more chants, bringing everyone back to focus on her."

    carm "Mhmm... The spirits are getting more active now... my, even more clearer perhaps?"
    carm "There is a woman. A beautiful, young woman."
    carm "They're telling me she has a lover. Or maybe someone who'd like to be?"

    show seance cg 2:
        zoom 0.77
    with dissolve

    show nemo seance up frown arm2 at left
    show npcfem1 at seancecolor:
        xalign 0.97
        zoom 0.82
    with dissolve

    nar "A young man sits up, now alert."

    carm "Her name is eluding me, though. I'm hearing many names right now."
    carm "Josephine... Julia... Genevieve... Ah, does she have several middle names, perhaps?"

    n frowntalk arm1 "My girlfriend!"

    show nemo frown

    carm "Ah, of course."
    carm "Your girlfriend... The spirits are telling me you're troubled about your relationship."

    n frowntalk "Yes! I... I've been thinking of proposing to her."

    show nemo frown

    carm "Her family is opposed, aren't they?"
    carm "But the spirits also tell me... You're having your own problems with her, aren't you?"

    n unsure frowntalk eye2 arm2 "Yes... When I brought up the idea of us getting married, she started growing distant. Why?"

    show nemo frown

    carm "Hmm..."

    nar "She closes her eyes once more to chant."

    carm "I fear she may have found someone else. Someone her family is more approving of."

    n eye1 arm1 "...!"

    show nemo frown

    carm "She doesn't want to upset you, but she wants to be with someone of a higher social status. It would be best to move on."
    carm "I'm sorry for this turn of events."

    n up eye3 "..."

    show nemo smile

    stop music fadeout 5

    nar "The man chuckles to himself."

    n talk "Ah, I guess it's good it was never serious, then."
    n eye1 down "In fact, I'm glad she doesn't even exist."

    show nemo smile

    play music "audio/Horroriffic.mp3" fadein 1.5
    queue music "audio/Horroriffic.mp3"

    carm "W-Whatever do you mean?"

    n frowntalk "I'm saying none of that is true. Your cold reading is decent, but it careens when someone gives your assistant fake information."

    show nemo frown

    carm "...!"

    n frowntalk eye2 arm2 "You gather basic information based on how they look—a woman alone in black crying is most likely mourning for her husband—and then get your assistant to find further details."
    n eye1 "For the people your assistant doesn't have time to get to, you start making general guesses and hone in on details depending on their responses."
    n arm1 eye3 "It's easy for you to take money from people in agony, isn't it?"

    show nemo frown eye1


    "Grieving Woman" "Is this true, madam?!"

    cn unsure frown arm3 "This... This was all fake?"

    show npcfem1 at seancecolor:
        easein 0.1 xoffset 10
        easein 0.1 xoffset -14
        easein 0.1 xoffset 7
        easein 0.1 xoffset 0

    carm "O-Of course not!"
    carm "Timothy, escort this charlatan out!"


    n grin "It's the pot calling the kettle black when pushed into a corner."

    show nemo smile


    "Weary Gentleman" "What a farce—! I knew we shouldn't have come here!"

    nar "The grieving man escorts his wife, now sobbing, out into the lobby."

    carm "Wait, wait! I can deliver more messages for you from beyond!"


    n frowntalk "The lies are only soothing when they think they're true."

    show nemo frown
    show npcfem1 at seancecolor:
        easein 0.1 xoffset 13
        easein 0.1 xoffset -16
        easein 0.1 xoffset 8
        easein 0.1 xoffset -4
        easein 0.1 xoffset 0

    carm "Out! Out, the lot of you!"

    stop music fadeout 5

    show black with sideswipe

    c up "...!"
    c frowntalk down "W-Why me too?!"

    show cecil frown

    scene bg psychicshop:
        zoom 0.7
        xalign 0.1 yalign 0.92
    show nemo down frown at center
    show cecil down frown arm2 at side
    with vpunch

    n frowntalk eye2 arm2 "Hoy! I can see myself out!"

    show nemo frown

    nar "The young man lands flat on the pavement. Too little too late, though, as behind him the other guests file out of the establishment."

    c frown "..."

    play music "audio/Isolation Waltz.mp3" fadein 2
    queue music "audio/Isolation Waltz.mp3"

    cn unsure eye2 "What do I do now? I was going to ask her where Lucie might be..."

    n unsure eye1 arm1 "..."

    cn frown arm1 "...! What's that guy looking my way for?"

    n up frowntalk arm2 "Hey, kid."
    n "You should be more careful about where ya go. There're con artists like that all over nowadays."

    show nemo frown

    cn down frown eye1 arm3 "His clothes are dirty and he talks with such an accent. And look at all the women he made cry! I don't trust him one bit."

    c frowntalk "Then why'd you stop by?"

    show cecil frown
    show nemo smile

    nar "He pulls out a coin and flips it."

    n grin eye3 "Payday!"
    n eye1 arm1 talk "A local gave me some spare change to defraud them."

    show nemo smile

    c up frowntalk "...!"
    c down frowntalk "So you really don't care, do you?"

    show cecil frown

    n down frowntalk "Care about what? Not letting vulnerable people hear false promises?"
    n "Those people coming here who've lost people—who've had them taken away from them—they're not going to get closure like this."
    n "They're gonna keep coming back hoping to hear more false words from the ones they lost."
    n "And those leeches will keep taking their money."
    n eye3 "...When you reach that stage, all you want is 5 more minutes with them. But that 5 minutes will never be enough."
    n eye1 "They're not giving them hope. They're just prolonging their grief and profiting from it."

    show nemo frown

    c "..."

    cn frown "The other visitors have mostly left, but... I can still see the grieving widow sobbing into her handkerchief. She just wanted to hear from her husband one more time."
    cn unsure frown arm1 "And I... I just want to find Lucie."

    c frowntalk arm3 "How'd you do it, then?"

    show cecil frown

    n up frowntalk "Do what? Tell it was bull?"
    n "It's not that hard to read people and make generalizations about them."
    n talk "You, though... you're an open book to read cold."

    show nemo smile

    c frowntalk "W-What does that mean?!"

    show cecil frown

    n talk arm2 "Let's see..."
    n arm1 "You're about, what, 12?"

    show nemo smile

    c frowntalk "13!"

    show cecil frown

    n frowntalk "You said you're looking for your friend, right? You only recently started looking for her, maybe in the past day or two."
    n talk "You're from nearby but you don't get out much. After all, you're from a rich family- probably not a noble, though. Newer money, maybe?"

    show nemo smile

    c up "—!"
    show bg psychic at shakeonce:
        zoom 0.706
        xalign 0.1 yalign 0.92
    show nemo at shakeonce
    c down frowntalk "I-I'm an orphan!"

    show cecil frown

    n frowntalk "Not in those clothes, you're not."
    n arm2 "After just a couple of nights of sleeping outside you'll get dirt on your clothes. After several weeks, your boots will get scuffed."
    n talk arm1 "But look at you, you look like you just stepped out of a tailor."

    show nemo smile

    cn up frown "H-He's going to turn me in for being a runaway!"
    cn arm1 "I've... I've got to get away!"


    hide cecil with hpunch

    n down frowntalk "Wh—! Hoy, where do ya think you're going?!"

    show nemo frown

    scene bg psychicshop:
        zoom 0.7
        xalign 0.1 yalign 0.92
    show cecil down frown arm1 at side
    with sideswipe

    stop music fadeout 4

    cn frown "I can't go home until I find her! Then we can go home together!"
    cn unsure "I... I don't want to go home until then!"






    scene bg backalley:
        zoom 0.6
        xalign 0.5 yalign 0.6
    show cecil down frown arm1 at side
    with sideswipe

    c frowntalk "Huff... huff..."

    cn frown up "Did... Did I... outrun him?"


    play sound "audio/dirt_footsteps.mp3"

    c "...!"
    c down frowntalk arm2 "Wh-Who's there?"

    show cecil frown

    play music "audio/Horroriffic.mp3" fadein 1.5
    queue music "audio/Horroriffic.mp3"

    na "Heh..."
    na "Kids shouldn't be running around on their own."


    show npcboy1:
        xalign -0.1 yalign 0.0
        zoom 0.67
    show npcboy4:
        xalign 1.2 yalign 0.0
        zoom 0.67
    with dissolve
    show npcboy3:
        xalign 0.2 yalign 0.1
        zoom 0.85
    show npcboy5:
        xalign 0.8 yalign 0.1
        zoom 0.8
    with dissolve

    cn unsure arm1 "These guys look even shadier than that lout back there!"

    na "Move aside."


    show npcboy3:
        xalign 0.1 yalign 0.1
        zoom 0.85
    show npcboy5:
        xalign 0.9 yalign 0.1
        zoom 0.8
    with ease
    show npcboy6:
        xalign 0.5 yalign 0.2
    with dissolve

    na "I haven't had fresh blood in a while."
    na "Such a scrawny kid... but he'll do."

    cn "—!"
    cn frown "V-Vampires!"
    cn frown "Father always said there's nothing worse than a vampire, someone who has become a ghoul..."
    cn frown "But now... what do I do?!"

    hide npcboy3
    hide npcboy5
    hide npcboy1
    hide npcboy4
    with Dissolve(0.4)

    "Vampire Leader" "C'mon, a little blood won't kill ya if you don't struggle."

    nar "The vampire snatches my arm—"


    show cecil up
    with greenlight

    show npcboy6:
        xalign 0.5 yalign 0.2 zoom 0.8
    with hpunch

    "Vampire Leader" "—?!"
    c frowntalk "Ah!"

    show cecil frown

    show npcboy6 at shakeonce

    "Vampire Leader" "The hell was that?!"

    cn frown "W-What was that?!"
    cn frown "It was some kind of flash when he touched my arm..."


    play sound "audio/gunshot1.mp3"

    "Vampire Leader" "Dammit—!"


    show npcboy6 at right:
        xalign 1.0
    with easeinleft
    show nemo down frown arm2 at left with easeinleft

    n frowntalk "See, this is why you shouldn't run off."
    n "Go to a blood bar if you're thirsty. You're not getting any blood here."

    show nemo frown

    show npcboy6 at shakeonce

    "Vampire Leader" "That what ya think?! Looks like I'll have 2 meals today!"

    show npcboy3 behind npcboy6 at right:
        zoom 0.63
        xalign 1.3
    with easeinright

    "Vampire" "Blazes, he's got a gun!"

    hide npcboy3 with easeoutright

    n down frowntalk arm1 "Move aside, kid!"

    show nemo frown


    scene nemogun1:
        yalign 0.25
    with sideswipe

    nar "With a shove, I land on the dirt a few feet behind the man as he brandishes a gun at the vampires."


    show black with sideswipe

    show gunshot
    show gunshotsparkles

    play sound "audio/gunshot1.mp3"

    nar "The flashes from the gun's muzzle are about all I can make out in the chaos."

    show gunshot as gs2:
        yoffset 500
        xoffset -100
        zoom 0.8
    show gunshotsparkles as gss2:
        yoffset 500
        xoffset -100
        zoom 0.8

    play sound "audio/gunshot2.mp3"

    pause(0.1)

    show gunshot as gs3:
        yoffset -400
        xoffset 100
        zoom 0.65
    show gunshotsparkles as gss3:
        yoffset -400
        xoffset 100
        zoom 0.65

    queue sound "audio/gunshot1.mp3"

    nar "The man seems unphased and keeps knocking the vampires to the ground before they can get a hit in."

    hide black
    hide gunshot
    hide gunshotsparkles
    hide gs2
    hide gss2
    hide gs3
    hide gss3
    with sideswipe

    nar "A shiv almost hits the man's shoulder—almost."



    nar "He topples one vampire down by knocking their legs down while shooting at another."


    show black with sideswipe

    show gunshot:
        yoffset -200
    show gunshotsparkles:
        yoffset -200

    play sound "audio/gunshot1.mp3"

    pause(0.1)

    show gunshot as gs2:
        yoffset 500
        xoffset -100
        zoom 0.9
    show gunshotsparkles as gss2:
        yoffset 500
        xoffset -100
        zoom 0.9

    queue sound "audio/gunshot2.mp3"

    cn frown "There's... no blood... What's he shooting them with?"

    show gunshot as gs3:
        yoffset 200
        xoffset -200
        zoom 0.9
    show gunshotsparkles as gss3:
        yoffset 200
        xoffset -200
        zoom 0.9

    queue sound "audio/gunshot1.mp3"

    nar "Another strike. Another hit."
    nar "Try as they might, the vampires can't seem to get a hit on the young man."

    scene bg backalley:
        zoom 0.6
        xalign 0.5 yalign 0.6
    with sideswipe

    show npcboy6 at left:
        zoom 0.78
        xalign 0.15
    show nemo down frown arm2 at right
    show cecil unsure frown at side
    with hpunch

    show npcboy6 at shakeonce

    "Vampire Leader" "Ergh-!!"

    show nemo at shake

    n "—!"

    show nemo frown
    show npcboy6:
        ease 0.35 xalign 0.9
    with ease

    hide npcboy6
    hide nemo
    with hpunch


    play sound "audio/gunshot2.mp3"

    nar "The head vampire lunges at the young man and tackles him to the ground. Even after two shots to the chest, the man can't shake him."

    c frowntalk "W-Wait!"

    show cecil frown

    nar "I run past the groaning vampires on the ground to get to the man and the leader."

    cn down frown arm2 "It might not be much, but I've got to do something!"

    show cecil arm1

    with hpunch

    nar "I use my weight to shove the leader off of the man, but he's quick to his feet again."
    nar "Just a minute ago he looked mostly normal, but now there's a visible bloodlust in his demeanor."

    show npcboy6 at center:
        yalign 0.23
        zoom 0.85
    with Dissolve(0.15)

    "Vampire Leader" "Get... out... of my way...!"

    show npcboy6 at center:
        yalign 0.23
        zoom 0.9
    with Dissolve(0.15)

    nar "He tears past the man and focuses right back on me."

    show npcboy6 at center:
        yalign 0.23
        zoom 0.95
    with Dissolve(0.15)

    c frowntalk "Ack! Get away from me!"

    show cecil frown

    show npcboy6 at center:
        yalign 0.23
        zoom 1.0
    with Dissolve(0.15)

    cn frown "This guy just won't stop-!"


    with hpunch

    nar "I try to kick him away, but he's unfazed and only comes closer."

    show npcboy6 at center:
        yalign 0.23
        zoom 1.05
    with Dissolve(0.15)

    nar "Instinctively I throw my hands up to defend myself."


    with greenlight

    hide npcboy6 with hpunch

    c frowntalk "—!"

    show cecil frown

    cn frown "That flash again!"
    cn frown "Why is there a reaction when I touch him?"

    n "Kid!"

    show nemo frown


    show nemo up frown arm2 at center:
        zoom 1.2
    with dissolve

    stop music fadeout 10

    n frowntalk "Are you alright?"

    show nemo frown

    c unsure frowntalk arm2 "Y-Yes..."

    cn frown eye2 "What was that flash...?"

    show cecil eye1

    nar "Around us, the vampire gang is laid out on the ground."

    n frowntalk eye2 "Looks like the leader here turned enraged at the thought of fresh blood... a little too common, honestly."

    show nemo frown eye1

    play music "audio/Isolation Waltz.mp3" fadein 2.5
    queue music "audio/Isolation Waltz.mp3"

    c frowntalk eye2 arm3 "...Thanks."

    show cecil frown

    n surprise talk "What was that?"

    show nemo smile

    c down frowntalk "I-I... I said thank you..."

    show cecil frown

    n talk up eye3 "Heh."
    n eye1 surprise arm1 "I guess a rich kid like you doesn't have much to thank others for, huh?"

    show nemo smile

    c eye5 "..."

    na "You lads alright?!"

    show cop behind nemo:
        xalign -0.5 yalign -0.9 zoom 0.45 alpha 0.0
        ease 1.2 xalign 0.0 alpha 1.0
    show cop as cop2 behind nemo:
        xalign -0.5 yalign -0.9 zoom 0.45 alpha 0.0
        ease 1.0 xalign 1.0 alpha 1.0

    show cecil eye1 neutral
    show nemo up frown

    nar "A group of coppers run up to us, waving their batons."

    Cop "We heard a mighty clamor from this way."
    Cop "—!"
    show cop at shake
    Cop "Johnny, get on yer feet!"

    nar "The lead vampire groans on the ground while a handful of the coppers start handcuffing the men."

    Cop "Well, it looks like you lot aren't hurt at least."
    Cop "We've been on high alert recently for vampire attacks."

    n up frowntalk "Why's that? There's been an increase in them?"

    show nemo down frown

    Cop "There's reports of a rash of attacks a couple cities south of here, 'round Lauremburg. Saying there's some kind of serial attacker at a college or somethin'."
    Cop "We'll take these louts in for now. Stay safe out there."


    show nemo eye2

    hide cop
    hide cop2
    with softeaseout

    cn unsure frown arm2 "A series of attacks... that sounds like what Lucie was looking into."

    c up arm1 eye3 frowntalk "Thanks for your help, but I've got to be off now."

    show cecil frown eye1

    n eye1 frowntalk "And where is that to? To get attacked again?"

    show nemo frown

    c down talk arm2 "To look for my friend, of course!"
    c up frowntalk arm3 "She'd been rather interested in vampire attacks recently, so that might be where she's gone."

    show cecil frown

    n eye2 up "..."
    n eye1 frowntalk "It's about time I leave town too. It sounds like we're heading in the same direction now."

    show nemo frown

    c down frowntalk arm2 "I can't have some old guy tailing me, that's creepy!"

    show cecil frown
    show nemo at shakeonce

    n down frowntalk arm2 "I'm barely 23!"
    n up "And besides, that's where my partner is."

    show nemo frown

    cn frown eye2 arm3 "What, your partner in crime?"

    show cecil arm1

    n frowntalk arm1 "You keep running around on your own and you'll be shipped back to your estate before you know it—or worse, some vampire's meal."

    show nemo frown

    c arm3 "..."

    show cecil frown

    $ nemoname = "Nemo"

    n talk "The name's Nemo. If you want, we can travel to Lauremburg together."

    show nemo smile
    show cecil eye1

    cn "What a weird name."

    nar "The man holds out his hand."

    cn up "Do I. Do I shake this?"
    cn arm1 "I'm running low on money. When I tried to board the train, I was turned around until I found my mommy. The coppers keep looking at me funny when I try to get my bearings straight."

    c frowntalk neutral "Alright, I'll go with you."

    show cecil frown

    stop music fadeout 1








    $ cecilpov = False
    $ save_name = "Bar Hopping"
    $ chapter_num = "Two"

    call chapter from _call_chapter_1

    scene bg city1:
        zoom 0.6
        yalign 0.8
        xalign 0.5
    show nemo up eye3 arm2 frown at side
    with fadee

    play music "audio/Winter.mp3" fadein 2
    queue music "audio/Winter.mp3"

    $ nemopov = True

    nn frown "I've got little money in my pocket, a runaway kid with no common sense, and no way to get the gems I was looking for."
    nn "And to top it off, I'm already heading home... This week is going swell."
    nn eye2 "If there really is a rash of attacks on campus, then the faster I can get back, the better."
    nn "Scott might have my neck for returning empty-handed, but he'll have to forgive me. Stopping vampire attacks comes before research."

    show cecil up frown arm3 at center:
        yoffset 100
    with dissolve

    c frowntalk "Where are we going?"

    show cecil frown

    n frowntalk eye1 "You made a fuss when I took a couple bills from that posh, so I thought we'd try something, ah, free."

    show nemo frown

    c down frowntalk "You mean legal."

    show cecil frown

    n frowntalk "Legal, sure, sure."
    n talk "It's not like that chap's gonna miss a couple bills, anyway."

    show nemo frown

    c frowntalk "How'd you reckon that? It's his money."

    show cecil frown

    nn down eye2 arm2 "This is going to be a long week. And that's {/i}if{i} we can get to the train fast enough."

    n frowntalk up eye1 arm1 "If you want to do this more {i}frugally{/i}, then we've got to do some searching."

    show nemo frown

    c up frowntalk "Why a pub?"

    show cecil frown

    n frowntalk "When you want to know something, you go to a pub."
    n eye3 talk "Well, you can when you're older."
    n eye1 frowntalk "Stay outside for a bit, okay?"
    n frowntalk "If someone comes up to you, ignore them and walk inside."

    show nemo frown

    c frowntalk eye2 "Yes, yes..."

    show cecil frown

    n frowntalk "And don't wander off."

    show nemo frown
    show cecil at shakeonce

    c frowntalk eye1 down "Are you going to go yet?!"

    show cecil frown

    nn eye2 "You ran headfirst into an alley and immediately got jumped by vampires. I can't assume you know anything about staying safe."

    n frowntalk eye1 "Alright, I won't be long."

    show nemo frown


    scene black with fade

    $ nemopov = False

    nar "The tavern is in a lull as it's midday—the patrons inside are all in their own corners while the barmaids are getting ready for a long shift as night approaches."
    nar "Only a handful of women are behind the bar while the rest are cleaning up or walking around in the back."

    show nemo seance up smile at side
    show npcfem3 at center:
        zoom 0.78
    with dissolve

    $ nemopov = True

    n talk "Sasha."

    show nemo smile

    "Sasha" "...!"
    "Sasha" "Nemo! What brings you out this way?"

    n talk eye3 arm2 "Sightseeing, running some errands, the lot."
    n eye1 "I'm trying to head south, you know anyone heading that way?"

    show nemo smile

    "Sasha" "Ah, I think there was a family leaving out for Oxwell today."
    "Sasha" "They were staying at Maria's inn, they might still be there."

    n talk arm1 "Thank you!"

    show nemo smile

    nar "I give her a peck on the cheek and walk towards the front door."

    "Sasha" "Next time you're in town, stop by and I might have some work for you!"

    n talk "Sure, as long as it's not being a bouncer again."

    show nemo smile

    nar "I wave to her and head out."


    scene bg city1:
        zoom 0.6
        yalign 0.8
        xalign 0.5
    show nemo up arm2 smile at side
    show cecil up frown arm3 at center:
        yoffset 100
    with dissolve

    c down frowntalk "Well? D'you find something?"

    show cecil frown

    nn frown eye2 "Does he still have an attitude because I copped a few bills?"

    n frowntalk eye1 "There's a family heading south. If we hurry, we might can catch them before they leave town."

    show nemo frown

    c frowntalk "And steal their carriage?"

    show cecil frown

    n down frowntalk arm1 "And ask for a ride! I don't steal everything, yknow!"

    show nemo frown

    c eye2 "..."

    show cecil frown

    nar "If I remember right, Maria's inn is only a couple blocks down."

    n eye3 frowntalk "If you want to get anywhere free, then you'd better offer up some physical work in return."

    show nemo frown

    c eye1 frowntalk arm1 "What does that mean?"

    show cecil frown

    n eye1 talk up "See, physical labor is when you use your arms and legs to do hard work, like farming or lifting crates—"

    show nemo smile

    show cecil at shake

    c frowntalk eye1 "I know what physical labor is!"

    show cecil frown

    n talk "Then you've got an idea already. Traveling through the countryside isn't as simple as just sitting in a carriage until you arrive."
    show cecil eye2
    n grin "'Course for you it probably is, but not for the rest of us."

    nn frown "If he pouts any longer, his face'll stay that way forever."
    nn frown "Maybe he's one of those kids who stays angry until he's fed."

    n frowntalk "You've been out before, haven't you?"

    show nemo frown

    show cecil at shakeonce

    c up frowntalk eye1 "What d'you mean? Of course I've left home before!"

    show cecil frown

    n frowntalk "Alright, alright. Where to?"

    show nemo frown

    c down frowntalk eye2 "Around town."

    show cecil frown

    n grin "Ah."

    show cecil eye4 with Dissolve(0.4)

    show cecil at shakeslow

    c frowntalk arm3 "D-Don't act all smug! I've been to town plenty of times! I've even been with Father on his business trips a couple times!"

    show cecil frown

    n talk "And where was that to?"

    show nemo smile

    show cecil eye1 with Dissolve(0.4)

    c frowntalk "Er... Well, we took a train..."

    show cecil frown

    n talk "Did you ever get {i}off{/i} the train?"

    show nemo smile

    c frowntalk eye1 "Yes!"
    c frowntalk eye2 "...Briefly."

    show cecil frown

    n grin "..."

    show cecil at shakeslow

    c frowntalk eye1 arm2 "It was somewhere in the mountains! There were trees every which way."
    c frowntalk arm1 "I've been places, okay?"

    show cecil frown

    n eye3 talk "Okay, okay."
    n eye1 "But clearly not alone."

    show nemo smile

    c eye2 "..."
    c frowntalk "My maid Annie was always with me."

    show cecil frown

    n talk "Oh, you've got a maid all to yourself?"

    show nemo smile

    show cecil eye4 with Dissolve(0.4)

    c frowntalk "S-She's the family maid!"
    c frowntalk eye5 "She just... mostly looks after me..."

    show cecil frown

    n frowntalk "What d'you think she's doing now?"

    show nemo frown

    show cecil eye2 with Dissolve(0.4)

    c frowntalk "...Frantically running around the estate."

    show cecil frown

    n frowntalk "Don't suppose she'd come looking for you, do ya?"

    show nemo frown

    c unsure "..."

    n frowntalk "...Sounds like we've got to get a move on, then."

    show nemo frown

    scene bg city1:
        zoom 0.7
        yalign 0.8
        xalign 0.5
    with sidefade

    $ nemopov = False

    nar "We make our way past a pop-up market on the side of the street. ...I'd love an apple right now, but I finally got the kid's mind off of my last pilfering."
    nar "This part of town definitely is more familiar now that I'm looking around. It's been a couple years, but it's coming back to me."

    nn "I haven't been here since—"

    $ nemopov = True

    show nemo up arm2 eye3 frown at side
    show cecil up frown arm3 at center:
        yoffset 100
    with dissolve

    c frowntalk "Hey, mister."

    show cecil frown

    n eye1 arm1 frowntalk "You can just call me Nemo, you know."

    show nemo frown

    c frowntalk "Why are you helping me?"

    show cecil frown

    nn frown arm2 eye2 surprise "Well, it is a fair question, but how do I answer it...?"

    n frowntalk eye1 up "You ran away to help someone else. Sure, you seem spoiled as hell, but you're not a spoiled brat."
    n frowntalk eye2 "And... you remind me of my little sister when she was younger. Naive, but earnest."

    show nemo frown

    c frowntalk arm2 "You have a sister?"

    show cecil frown

    nn down eye3 "I just had to keep talking, didn't I?"

    n frowntalk up eye2 arm1 "Had."

    show nemo frown

    c frowntalk arm1 "Had—Oh..."

    show cecil frown scared eye2

    nar "The kid looks away awkwardly. Well, enough of that conversation."

    n frowntalk eye1 "Looks like we're here."

    show nemo frown
    show cecil eye1 neutral

    nar "I point to the building across the street—a somewhat dodgy-looking but well-meaning inn run by an older couple."
    nar "Out in front is a carriage that a young man is packing."

    n talk "And it looks like our ride is still here."

    show nemo smile

    c surprise frowntalk arm1 "What d'you plan on doing?"

    show cecil frown

    n talk "C'mon."

    show nemo smile

    scene bg city1:
        zoom 0.7
        yalign 0.8
        xalign 0.5
    with sidefade

    show nemo up smile arm1 at side
    show cecil up frown arm3 at right:
        yoffset 100
        xalign 1.1
    with dissolve

    n talk "Ahoy!"

    show nemo smile

    nar "I raise my cap at the man who promptly stops what he's doing to wave our direction."

    show npcman smile at left:
        zoom 0.7
        alpha 0 alpha 0 xalign -0.4
        linear 0.9 alpha 1 xalign 0.3

    pause(0.8)

    man talk "Good day! Can I help you with something?"

    show npcman frown

    n talk "I was actually looking if you needed help loading."

    show nemo smile

    man talk "That'd be much obliged. What would it cost us?"

    show npcman smile

    n talk "We're just looking to travel south of here, to get to the train station in Tradere."

    show nemo smile

    nar "He holds out a hand."

    man talk "Sounds like a deal, then."

    show npcman smile

    stop music fadeout 2








    scene black with fade

    $ nemopov = False
    $ cecilpov = True
    $ quick_menu = False

    $ save_name = "A Motherly Touch"
    $ chapter_num = "Three"

    call chapter from _call_chapter_2

    scene bg city1:
        zoom 0.7
        yalign 0.8
        xalign 0.5
    with fade

    play music "audio/Isolation Waltz.mp3" fadein 2
    queue music "audio/Isolation Waltz.mp3"

    nar "Nemo immediately goes to the crates on the ground and starts lifting them like they're nothing."
    nar "I try the same thing, but I can't even get one off the ground..."

    show cecil unsure frown arm1 at side
    show nemo surprise frown eye2 at center
    with dissolve

    n frowntalk "...Why don't you go sit over there while we do this?"

    show nemo frown

    nar "He nods over to the front steps of the inn where a woman is sitting with a small toddler."

    c frowntalk eye3 "Okay..."

    show cecil frown

    scene bg city1:
        zoom 0.7
        yalign 0.8
        xalign 0.7
    with sidefade

    show npcwoman up smile at center:
        zoom 0.7
    show cecil up frown arm1 at side
    with dissolve

    Woman talk "Ah, good evening."

    show npcwoman smile

    cn frown "I've... I've never actually talked to a lady before alone like this. Annie doesn't count. Lucie definitely doesn't count."
    cn arm2 down "I've got to be the perfect gentleman-!"

    c frowntalk up "H-Hi."

    show cecil frown arm1

    Woman talk "Hi. What's your name?"

    show npcwoman smile

    c frowntalk arm2 "C-Cecil."

    show cecil frown arm1

    Woman talk "Cecil, what a nice name."
    $ womanname = "Elizabeth"
    $ manname = "Eustice"
    Woman "My name is Elizabeth and that's my husband Eustice."
    Woman "And this little one is Owen!"

    show npcwoman smile at curtsy

    nar "She raises the arms of the toddler who's sitting beside her, causing the child to start giggling."
    nar "All I do is nod awkwardly."

    Woman talk "Come here and sit down."

    show npcwoman smile


    show bg city1 at curtsy
    show npcwoman at curtsy

    pause(0.5)

    show npcwoman:
        ease 1.5 zoom 0.85 yalign 0.2
    show bg city1:
        ease 1.5 zoom 0.78

    pause(1.4)

    Woman talk "Your hair is a bit messy... a growing young man should always keep a comb in his back pocket!"

    show npcwoman smile

    nar "She strokes her fingers through my hair, attempting to straighten it out."

    show cecil eye4

    show npcwoman at shake
    show bg city1 at shake

    c down frowntalk arm2 "Wh-wh-!"

    show cecil unsure frown

    Woman talk "Haha, I'm just cleaning you up a bit. It's alright."
    show cecil arm1
    Woman "Even if you don't have a home, you should try to keep your hair straight. It'll make you feel better."

    show npcwoman smile

    nar "She continues running her fingers through my hair. Her hands are so warm..."

    Woman talk "If you don't have a comb, start running your fingers through your hair from the bottom and work your way up slowly."
    Woman "You'll get more knots out that way."

    show npcwoman smile

    show cecil eye1

    c up frowntalk "Oh... I didn't know that."

    show cecil frown

    nar "She straightens my tie."

    Woman talk "Do you have any parents?"

    show npcwoman smile

    c unsure eye2 "..."

    cn frown "I can't give her the impression I'm a runaway. But... how do I answer her?"

    show npcwoman at shakeslow

    Woman frowntalk "Oh, I didn't mean to upset you."

    show cecil eye1 neutral

    show bg city1 at curtsy
    show npcwoman smile at curtsy

    nar "She pats my head."
    show cecil eye2
    nar "No one's done that before."

    Woman talk "Where are you and your brother heading to?"

    show npcwoman smile

    c down frowntalk arm3 eye1 "We're not brothers! He—"

    cn scared frown arm1 eye2 "Wait! If they find out we're not related then they might call the coppers on me!"

    Woman frowntalk "Ah, I'm sorry! Where are you and your friend headed to?"

    show npcwoman frown

    c up frowntalk arm1 eye1 "We're looking for my best friend. She's been missing for a couple weeks now."

    show cecil frown

    Woman frowntalk "Oh no! I do hope she's okay."

    show npcwoman frown

    c frowntalk "I'll find her, don't worry!"

    show cecil frown
    show npcwoman smile

    nar "She rests her hand on her lap and smiles at me."

    Woman talk "I'm sure you will."
    Woman "Have you ever been out this way?"

    show npcwoman smile

    c frowntalk "I haven't... He has, but this place is all new to me."

    show cecil frown

    Woman talk "Chin up!"

    show npcwoman smile

    nar "I bolt upright at her words."

    Woman talk "You seem so focused on finding your friend, but remember to not lose sight of the road ahead of you."
    Woman "Look around you and enjoy the view."
    Woman "I pray you'll cherish the journey."

    show npcwoman smile

    show npcman behind npcwoman:
        zoom 0.6
        xalign 0.07
        yalign 1.0
    with easeinleft

    show nemo behind npcman:
        zoom 0.6
        xalign -0.29
        yalign -0.02
    with easeinleft

    man talk "That should be it!"

    show npcman smile

    nar "The man dusts off his pants and waves towards us."

    man talk "Beloved, we're done! Let's head out so we can get a fair way before nightfall."

    show npcman smile

    stop music fadeout 2










    $ save_name = "Bumpy Ride"
    $ chapter_num = "Four"
    $ cecilpov = False

    call chapter from _call_chapter_3

    scene bg wagon day:
        zoom 0.65
        yalign 0.5
        xalign 0.7
    with fade
    play foley "audio/carriage.mp3" fadein 1 volume 0.5

    play music "audio/La Citadelle.mp3" fadein 2
    queue music "audio/La Citadelle.mp3"

    nn "The ride is a little bumpy but it's blazes better than going by foot."
    nn "Cecil looks mildly terrified by the whole \"we're in a rickety wooden carriage\" thing. He must be used to those fancy closed carriages."
    nn "Hmm, maybe I should start a conversation. We don't know anything about the couple, really."

    $ nemopov = True

    show nemo up smile arm2 at side
    show npcman smile at center:
        zoom 0.8
        xalign 0.3
    show cecil up frown arm1 at right:
        zoom 0.8
        xalign 1.0
        yoffset 200
    with dissolve

    n talk "Thank you for letting us ride with you two."

    show nemo smile

    man talk "Thank you for the help loading everything!"
    man "We were staying in town long enough to get my son checked out by the doctor there, so now we're heading home."
    man "What brings you two south?"

    show npcman smile

    n talk arm1 "We're trying to get home too. Lauremburg, to be exact."

    nn frown "Well, my home at least."

    show nemo smile

    man talk "Lauremburg! I've heard it's beautiful during fall."

    show npcman smile

    n talk "It definitely is. Where do you call home?"

    show nemo smile

    man talk "Oxwell! It's quaint compared to Lauremburg, but the countryside is worth it."
    man talk "I have a wonderful workshop out there."

    show npcman smile

    n frowntalk "A shop? You a blacksmith?"

    show nemo frown

    man talk "An inventor!"
    man talk "Truth be told, I brought a few of my inventions with me to town to find a seller while we were here..."

    show npcman smile

    show npcwoman frown behind npcman at left:
        zoom 0.65
        xalign -0.1
    with easeinleft

    Woman frowntalk "I told you the answer was going to be no!"
    show npcwoman frown

    man talk "I was multitasking, dear!"

    show npcman frown

    hide npcwoman with easeoutleft

    man talk "Ah, if I had, though... What a wonder!"
    show npcman smile

    show npcman:
        xalign 0.1
    with easeinright

    show cecil:
        xalign 1.1
        zoom 1.1
    with dissolve

    c frowntalk "What kind of inventions have you made?"

    show cecil frown

    man talk "What have I made? Would you ask a painter what they've painted? My, what have I {i}not{/i} made!"
    man talk "Here, here, look with your own eyes!"
    show npcman smile

    show npcman at curtsy

    nn frown "The man hurriedly yanks a bag from behind him and passes it to Cecil."
    show cecil:
        easein 0.4 yoffset 220
        easein 0.25 yoffset 200
    nn "Cecil timidly shifts through the bag, pulling out a variety of items to further inspect carefully."
    nn frown "I grab one item that catches my eye. It looks like... well, it's hard to describe. At least with the other items I could imagine a potential use for them."

    n unsure frowntalk "What's this?"

    show nemo frown

    man talk "That, my boy, is a tool to subdue vampires!"
    show npcman smile

    show cecil at shakeonce

    c frowntalk "Really?!"

    show cecil frown

    n up talk "How good is it?"

    show nemo smile

    man talk "I don't know yet!"
    show nemo unsure eye3 arm2
    show cecil unsure arm3
    man talk "Soon, though- soon I will be able to test it! I just need to find a volunteer."
    show npcman smile

    show npcwoman frown behind npcman at left:
        zoom 0.65
        xalign -0.2
    with easeinleft

    Woman down frowntalk "That's not happening."
    show npcwoman frown

    hide npcwoman with easeoutleft

    man down talk "Not with that attitude, it's not!"
    man up "Sigh... In theory it should work."
    show npcman frown

    nn eye2 up frown "In theory."

    show nemo eye1 arm1
    show cecil up

    man talk "Vampires have heightened senses—not by an outrageous amount, but heightened nonetheless."
    man talk "Most notably, they reportedly have a heightened sense of smell."
    man talk "This might normally be an advantage to them, but with anything you can flip an advantage upside down."
    show npcman frown

    n frowntalk "Overwhelm their senses."

    show nemo smile
    show npcman at curtsy

    man talk "Exactly!"
    man talk "For us folks in the countryside, it's normal to put up garlic around our doors to ward off vampires. However, it's not the garlic that does the trick."
    show npcman smile

    n frowntalk "Garlic is something easy to get and very pungent. It won't kill them but they certainly don't like it."
    n frowntalk "I suppose if you stuff enough of something terribly smelling it could incapacitate one briefly, especially if they're hit with it all at once."

    show nemo smile
    show cecil arm3

    nar "Cecil looks back and forth at us, wide-eyed."

    man talk "And that's what this item does! Stuff it with garlic, peppers, the lot, close it up, and hold it near any vampire coming your way."
    man talk "Of course, you should only use it against hostile ones, but if they could all manage their tendencies then we wouldn't need this, now would we?"
    show npcman smile

    n frowntalk "Sadly true."
    n "Have you tried anything else to work against vampires?"

    show nemo frown

    man talk "I've wanted to tinker with the effects of specific gems on them and how we can dilute them, but, well, money is tight..."
    show npcman frown

    show npcwoman frown behind npcman at left:
        zoom 0.65
        xalign -0.2
    with easeinleft

    Woman down talk "And I'm not giving you my gems for your arts and crafts!"
    show npcwoman smile

    hide npcwoman with easeoutleft

    n talk "I've wondered the same thing. Right now I'm working with a professor on researching the effects of precious metals and natural gems on vampires."
    n eye2 frowntalk "Some gems definitely hurt vampires and might kill them, but we haven't narrowed down the list enough."
    n eye1 talk unsure arm2 "Not exactly easy or cheap to get gems, y'know."

    show nemo up smile

    c frowntalk arm3 "Why gems? Why can they hurt vampires?"

    show cecil frown

    n frowntalk arm1 "That's harder to say—you can speculate about it, though."
    n "Certain gems have been used for millennia for different spiritual uses, like warding off evil."
    n "There are some gems that hurt vampires. Just a small touch is like burning them."

    show nemo frown

    c unsure eye2 "..."

    n talk "Some gems have been described for other uses than just warding evil, though. They might be fairy tales, but we want to try them out."
    n talk "It's a small lead towards a cure to vampirism."

    show nemo smile

    c frowntalk eye1 "A cure?"

    show cecil frown

    man talk "Haha! A cure to vampirism would be worth more than any gem on earth!"

    show npcman smile

    n talk "Definitely."
    n frowntalk eye2 "Can't imagine any worse fate than having to rely on a constant supply of blood and becoming feral if you can't get any."
    show cecil unsure
    n down "Going into an all-fired rage and attacking anyone near you..."
    n eye1 up frown "—!"
    n eye3 down frowntalk arm2 "Sorry, I got a lil' carried away."
    n eye2 up arm1 "Speaking of gems..."

    show nemo frown

    nar "I pull out my gun and unload a couple bullets."

    n eye1 talk "These bullets are made to hurt vampires."
    n talk "They're made of rubber and dipped in liquidated gems. These in particular are aquamarine."

    show nemo smile
    show cecil:
        easein 0.4 yoffset 220
        easein 0.25 yoffset 200

    c frowntalk up arm2 "Woah... So these are what you used to take out those guys."
    c talk "They're really pretty."

    show cecil smile arm1

    n talk "Since they're bullets they pack a punch, but they have to touch skin before they're fully effective."

    show nemo smile

    man talk "It's a beauty, for sure."
    man talk "That gun of yours is very ornate, too. A family heirloom?"
    show npcman smile

    n eye2 frowntalk "Just something I've had for a long time."

    show nemo frown

    nar "I tuck it away before he can inspect it anymore. Better safe than sorry."
    show nemo eye1
    show cecil:
        easein 0.4 yoffset 220
        easein 0.25 yoffset 200
    nar "Cecil hands me the bullets back, still transfixed on them."

    nn frown "Does he really like gems?"

    nar "He rubs his eyes and yawns."

    man talk "Hah, had a long morning?"
    show nemo smile
    man talk "Sit back and relax, we'll be stopping in a few hours."
    show npcman smile

    stop foley fadeout 2
    stop music fadeout 2







    $ quick_menu = False

    scene black with fade

    $ nemopov = False
    $ cecilpov = True
    $ save_name = "That Aquamarine Sky"
    $ chapter_num = "Five"

    call chapter from _call_chapter_4

    scene bg wagon night:
        zoom 0.65
        yalign 0.5
        xalign 0.7
    with fade

    play foley "audio/crickets.mp3" volume 0.8

    play music "audio/Isolation Waltz.mp3" fadein 2
    queue music "audio/Isolation Waltz.mp3"

    show cecil night up frown arm1 at side
    show npcwoman night smile:
        zoom 0.7
        xalign 0.48
    with dissolve

    pause(0.4)

    show npcwoman at curtsy

    Woman talk "Here you go."

    show npcwoman smile

    nar "The woman hands me a pair of blankets. I stare at her blankly."
    show cecil eye2 scared
    hide npcwoman with dissolve
    cn "When the man said we'd be stopping here for the night, it didn't really set in that we'd actually be {/i}sleeping{i} out here until now."

    show nemo night up frown:
        zoom 0.65
        xalign 0.26
    show cecil eye1 neutral
    with dissolve

    nar "The man tends to a fire near their wagon. Nemo is a few feet away, setting up another fire."

    show nemo at center:
        zoom 1.0
    with Dissolve(0.7)

    c frowntalk "Why are you making another fire?"

    show cecil frown

    n frowntalk eye3 "Warmer."
    n eye2 "And I'd rather not sleep so close to strangers."
    n frowntalk eye1 "You're free to sleep wherever."

    show nemo frown

    c eye2 unsure "..."

    cn eye1 "Sakes alive, we're really sleeping outside in the middle of nowhere."

    n talk arm2 "Mind handin' me one of those blankets?"

    show nemo smile

    c up frowntalk "O-Oh!"

    show bg wagon night at curtsy
    show nemo at curtsy

    cn frown eye2 "I was kind of hoping they were both for me."

    show cecil eye1

    n talk "Ever had a sleepover?"

    show nemo smile

    c frowntalk surprise "A what?"

    show cecil frown

    n frowntalk unsure "...Y'know, when you invite people over and you sleep on the floor?"

    show nemo frown

    c frowntalk arm3 "Why would we sleep on the floor when I have enough beds?"

    show cecil frown
    show nemo eye3

    nar "Nemo mutters something under his breath and unfolds the blanket."

    n frowntalk up eye1 arm1 "Watch how I do this."

    show nemo smile:
        easein 0.4 yoffset 20
        easein 0.25 yoffset 0
        easein 0.25 xoffset 14
        easein 0.35 xoffset -18
        easein 0.25 xoffset 8
        easein 0.35 xoffset 0
    show cecil up

    nar "He holds two of the corners and throws it in the air."

    c arm2 frowntalk "Oh! That's what Annie does with blankets!"

    show cecil frown arm1

    n talk "After you do that... Take some loose dirt for a pillow."
    n "Or you can use your arm, I guess."

    show nemo smile

    cn unsure frown "Annie would be horrified."

    c frowntalk arm2 "What about animals?"

    show cecil frown arm1

    n frowntalk "Eh, the fire should keep most animals away."

    show nemo frown

    c frowntalk "And bugs?"

    show cecil frown

    n frowntalk eye3 "You've already got one on you."

    show nemo smile eye1 at shake
    show bg wagon night at shake

    c frowntalk arm2 "W-Where?!"

    show cecil frown

    n talk arm2 eye3 "Hah! I'm kidding, I'm kidding."
    n eye1 arm1 "You'll get bugs on you, that's inevitable."

    show nemo smile

    cn frown eye2 arm3 "I don't want bugs near me..."

    show cecil eye1

    nar "He strokes the fire and sits down on his blanket."
    show cecil arm1
    nar "I reluctantly take off my shoes and do the same."

    cn frown up "I guess this is like falling asleep by the fireplace... except more bugs. And no plush chairs."

    n frowntalk "Don't sweat it so much, I've slept outside more times than I can count."

    show nemo frown

    c frowntalk "Are you homeless?"

    show cecil frown

    n eye3 talk up arm2 "Hah! Do I look that disheveled to you?"
    n eye1 arm1 "No, my home is in Lauremburg. I'll show it to ya when we get there."

    show nemo smile

    c frowntalk up arm2 "You have family there?"

    show cecil frown arm1

    n frowntalk arm2 eye2 "Well, it depends on your definition of family..."
    show nemo eye1
    extend " I don't have any blood relatives."

    show nemo frown

    c frowntalk "N-None?"

    show cecil frown

    n frowntalk arm1 eye3 "None."
    n eye2 "My mother died in childbirth. My father died in a factory accident a few years later. After that, I was on my own."
    n frowntalk "The orphanages were glorified prisons for children. I stayed in a couple of 'em but some were worse than the streets. Overcrowded, hostile..."
    n frowntalk "I met all sorts of orphans and runaways back then. Fires, disease, mine collapses, mechanical failures..."
    n frown arm2 "..."
    n frowntalk eye1 "What about you?"

    show nemo frown

    c frowntalk "...I don't have any siblings. Just my parents."

    show cecil frown

    cn frown "What would it be like to wake up and have another person in the next room over? To live with someone else your age?"

    n frowntalk "What's so special about this friend of yours?"

    show nemo frown at shakeonce
    show bg wagon night at shakeonce

    c down arm2 frowntalk "What's special about her? Everything!"
    c frowntalk "She's like a doll! She always looks so elegant!"
    c frowntalk "She's my best friend, we always visit each other! We even do some homeschooling work together!"
    c frowntalk "There's nothing not to like about Lucie!"

    show cecil frown

    n frowntalk "Lucie, eh...?"
    n talk arm1 "I hope you find her."

    show nemo smile

    c neutral arm1 talk "...Thank you."

    show cecil smile

    n frowntalk eye3 "Now, get some rest. And try not to turn over into the fire."

    show nemo smile eye1

    c down arm3 frowntalk "I-I'm not that close to it!"

    cn frown unsure arm1 "Right...?"

    n talk "Night."

    show nemo smile

    stop foley fadeout 2
    stop music fadeout 2









    $ chapter_num = "Six"
    $ save_name = "Travelers"
    call chapter from _call_chapter_5

    $ nemopov = True
    $ cecilpov = False

    scene bg wagon day:
        zoom 0.7
        yalign 0.8
        xalign 0.5
    with fade

    show npcman at left:
        zoom 0.65
        xalign -0.2
    show npcwoman at left:
        zoom 0.65
        xalign 0.2
    show cecil up smile at center:
        yoffset 200
        xalign 0.8
    show nemo up smile arm2 at side
    with dissolve

    play music "audio/La Citadelle.mp3" fadein 2
    queue music "audio/La Citadelle.mp3"

    show cecil:
        easein 0.4 yoffset 220
        easein 0.25 yoffset 200

    c talk arm2 "Thank you for everything!"

    show cecil smile

    n talk "Have safe travels!"

    show nemo smile

    man talk "You too!"

    show npcman smile

    Woman talk "Stay safe out there!"

    show npcwoman smile

    nar "We wave the family off as they continue down the path, leaving us close to Tradere."

    scene bg countryside:
        zoom 0.97
        xalign 0.5
        yalign 0.2
        linear 3.8 yalign 0.85
    with sidefade

    pause(1.8)

    show cecil up frown arm3 at center:
        yoffset 100
        zoom 1.1
    show nemo up smile arm1 at side
    with dissolve

    c frowntalk "What now?"

    show cecil frown

    n frowntalk "We walk."

    show nemo smile

    c surprise frowntalk "How far?"

    show cecil frown

    n frowntalk eye2 arm2 "Er... a few hours? Might have to camp out again? We'll see."

    show nemo frown eye1 arm1

    show cecil at shakeonce

    c frowntalk down arm2 "\"We'll see\"?! So we are lost!"

    show cecil frown

    n frowntalk down "We're not lost! This path leads to Tradere, trust me. It'll just be a while, so no need in gettin' in a rush."
    n up grin "Hope your shoes are broken in."

    show nemo smile

    c unsure arm3 eye2 "..."

    nn smile "Heh. A little walking'll do the kid some good."
    nn eye2 frown "We'll have to spend another night out but maybe we can hitch another ride if we're lucky."

    nar "Cecil trudges alongside me, his polished shoes unfit for the gravelly, grassy path."

    show nemo eye1

    c frowntalk surprise eye1 "Do you usually rough it like this?"

    show cecil frown

    n frowntalk eye2 arm2 "Usually? I guess. Whichever way I can get somewhere faster."
    n arm1 eye1 "It's too expensive to have a chauffeur from town to town."

    nn frown eye2 unsure "Not like Ambrose hasn't offered me one, but..."

    n frowntalk up eye1 "Train is the best to go on, but it doesn't stop in every town. That's why we've got to travel to Tradere on our own."

    show nemo frown

    c frowntalk eye1 arm3 neutral "I know that part. There's a train station in town."
    show cecil eye2
    extend " I managed to hop on it for a stop until they kicked me off when they found out I was alone."

    show cecil frown

    n frowntalk unsure eye3 "And yet you still continued south..."

    show nemo frown eye1
    show cecil at shake

    c frowntalk eye1 down arm2 "Of course! I'm dead set on this!"
    show cecil at shakeslow
    c unsure eye2 arm3 "...And it's not like I can show back up empty handed after running away..."

    show cecil frown

    n grin eye3 arm2 up "That's the spirit! Don't half-ass things."
    n frowntalk eye1 "...But consider throwing some caution to the wind. Especially around shady people."

    show nemo frown

    c frowntalk eye2 arm3 "I should've taken that advice about you..."

    show cecil frown

    n talk arm1 "Hmm? You're gonna walk to Tradere and board the train all on your own?"

    show nemo smile
    show cecil at shakeslow

    c "..."

    n talk arm1 "Look on the bright side—it's nice and sunny out here, no rain clouds in sight."

    show nemo smile

    show cecil at shakeslow

    c frowntalk "Hot and sweltering out here..."

    show cecil frown

    n frowntalk "Too bad for you that your friend ran away at the end of summer. Another month or two and it'd be cooler."

    show nemo frown

    c frowntalk "Too bad for me..."

    show cecil frown
    show nemo smile

    nn "I can't help but smile. He's dragging his feet like she used to."
    nn "She got smart and realized I wouldn't wait on her if she slowed down so I'd carry her some of the way. Of course, she was a lot younger than this kid..."

    n talk arm1 "Y'know, some rich people do this for fun."

    show nemo smile

    c frowntalk eye1 arm1 "What, staying outside with bugs?"

    show cecil frown

    n frowntalk "Yeah, actually. It's called camping. They pitch some tarps together for a tent, make a fire, and sleep there."
    n frowntalk "Some even go walking like this in mountains and parks. They call it hiking."

    show nemo smile

    show cecil at shakeonce

    c frowntalk arm2 "Some posh fellows out here with the bugs and critters?! No thank you!"
    c frowntalk arm3 "I'll stick to a warm armchair by the fireplace, thank you."

    show cecil frown

    n talk "Of course you would."

    show nemo smile

    scene bg countryside:
        zoom 0.97 xalign 0.5 yalign 0.85
    with sidefade

    $ nemopov = False

    nar "We pass by several farm houses and crop fields on the trail. It's peaceful out here."

    nn "I've grown so used to city living that it's hard to imagine owning a farm far away from factories, town houses, carriages..."
    nn "Would it be a nice place to retire?"
    nn "To be outlived by him..."

    $ nemopov = True

    show nemo up frown at side
    show cecil unsure frown at center:
        yoffset 120
        zoom 0.75
    with dissolve

    c frowntalk "M-Mister..."

    show cecil frown

    nar "I turn around to see Cecil bent over several feet behind me trying to catch his breath."

    nn eye2 "I honestly forgot he was here."

    show cecil:
        zoom 0.9
    with dissolve

    n frowntalk eye1 "Slowin' us down, kid."

    show nemo frown

    nn frown "I guess my strides are longer than his. It's going to take a lot longer if I have to go with his pace."

    show npcmasc5 at left:
        xalign -0.5
        yalign 1.0
        zoom 0.67
        alpha 0.0
        linear 1.0 alpha 1.0 xalign 0.0
    with dissolve

    nar "An older man approaches from a nearby intersection and walks over to Cecil."

    "Older Gentleman" "Are you alright, sonny?"

    show cecil at shakeslow

    c frowntalk "F... Fine..."

    show cecil frown

    "Older Gentleman" "You're not gonna get far travelin' like that. Don't run, walk."

    show cecil at shakeslow
    c frowntalk "H-Hwah?"

    show cecil frown

    "Older Gentleman" "Here."

    show npcmasc5 at curtsy

    nar "The man hands Cecil a flask of water. To my surprise, Cecil accepts it and drinks up."

    c frowntalk up "Phew..."
    c frowntalk arm2 "Thank you, mister."

    show cecil smile arm1:
        easein 0.4 yoffset 140
        easein 0.25 yoffset 120

    nar "Cecil reaches up to hand back the man's flask."

    with greenlight

    show nemo down
    with hpunch

    c frowntalk "—!"

    show cecil frown at shakeonce

    nar "A flash of light dances on their hands when they touch."

    nn frown "What was that—?!"

    show npcmasc5:
        ease 0.5 xalign -1.0
    with dissolve

    show cecil unsure at right:
        ease 0.25 yoffset 100 zoom 1.4 xalign 0.8






    nar "The man recoils back and assumes a defensive stance. I step in between him and Cecil."

    n frowntalk "What was that, Cecil?"

    show nemo frown

    c eye2 "..."

    show cecil frown

    n frowntalk "Cecil?"

    show nemo frown

    show cecil at shake

    c frowntalk eye1 "I-I don't know!!"

    show cecil frown

    show npcmasc5 at left:
        yalign 1.0 xalign 0.0 zoom 0.67
    with dissolve

    nar "The man clasps his shaking hand, silently looking at the ground. Behind me, Cecil looks physically fine albeit shaken up."
    nar "I put my hand on my holster."

    n frowntalk "You alright, sir?"

    show nemo frown

    "Older Gentleman" "..."

    n frowntalk "Sir?"

    show nemo frown

    nar "He opens his mouth, but not to speak."
    nar "Fangs appear from beyond his lips."

    "Older Gentleman" "{color=#ff2e2e}Blood Art—{/color}"


    scene black
    show gunshot
    show gunshotsparkles

    play sound "audio/gunshot1.mp3"

    pause(1.1)





    scene bg countryside:
        zoom 0.97 xalign 0.5 yalign 0.85
    show npcmasc5 at left:
        yalign 1.0 xalign 0.0 zoom 0.67
    show cecil unsure frown at right:
        yoffset 100 zoom 1.4 xalign 0.8
    show nemo down frown at side

    nar "Before he can move, I shoot a warning shot."

    "Older Gentleman" "—!"


    play sound "audio/dirt_running.mp3" fadeout 2
    show npcmasc5:
        ease 0.5 xalign -1.0
    with dissolve

    nar "That's all it takes for the man to quickly walk off."

    show cecil at shakeslow

    c frowntalk arm2 eye1 "Was he really a vampire? I can't believe there was one out this far!"
    c frowntalk "And he almost attacked us!"

    show cecil frown

    n eye2 arm2 "..."

    nn frown "No... That light startled him and must have hurt him. He was probably thinking out of self defense."

    n frowntalk eye1 up "Listen, if you ever hear a vampire start uttering the words \"Blood Arts\", high tail it the other direction."
    n eye2 "I guess you could call it a spell of some sort... It's an ability some vampires have learned that lets them use their blood for self defense."
    n "It's rare, though, so you shouldn't have to worry about it much."

    show nemo frown
    show cecil at shake

    c frowntalk "W-Wait, I drank water after a vampire! A-Am I going to turn into one now?!"

    show cecil frown:
        easein 0.3 yoffset 115
        easein 0.15 yoffset 100
        easein 0.25 yoffset 110
        easein 0.10 yoffset 100
    show nemo eye1 up

    nar "I pat his head."

    n talk "It's going to take a lot more than that to turn you."

    show nemo smile

    show cecil at shakeonce

    c frowntalk arm3 "How are you so sure?!"

    show cecil frown

    n grin "Trust me."

    nn smile "It's going to be a full day of walking... Well, no time to waste!"

    stop music fadeout 2










    $ save_name = "That Emerald Water"
    $ chapter_num = "Seven"

    call chapter from _call_chapter_6

    scene bg city3:
        zoom 0.545
        yalign 0.8
        xalign 0.5
    with fade

    $ nemopov = False
    $ cecilpov = True

    show cecil up smile arm2 at side
    show nemo up smile arm2 at center
    with dissolve

    c frowntalk "Wow..."

    play music "audio/La Citadelle.mp3" fadein 2
    queue music "audio/La Citadelle.mp3"

    show cecil at shakeslow

    cn smile "It took a full day to get here, but we're finally in Tradere!"
    show cecil at curtsy
    cn "One step closer to Lauremburg... One step closer to Lucie!"

    n talk arm1 "C'mon, let's head to town and see what the train schedule looks like."

    show nemo smile

    hide nemo with softeaseout

    cn smile "Tradere... It's a big transportation and marketplace hub, from what I remember Annie telling me."

    show bg city3:
        zoom 0.65
    with dissolve

    show bg city3:
        easein 1.8 xalign 0.2
        easein 1.3 xalign 1.0
        easein 1.3 xalign 0.1
        easein 1.3 xalign 0.9
        easein 1.9 xalign 0.5

    cn "It's even bigger and busier than I imagined...! So many workers running from store to store, so many carriages and horses..."
    cn "This is what real towns are like. People working. People talking. People {/i}everywhere{i}."
    cn arm1 "Will Lauremburg be like this?"
    cn arm3 frown unsure "Lucie... why did you come out this far on your own? What's so interesting about vampire attacks?"

    show bg city3:
        zoom 0.545
    with dissolve

    show nemo up frown at center with softeaseleft

    n frowntalk "If you trip up I'll leave you behind."

    show nemo smile

    c frowntalk "Wh-Wh—"

    c arm2 down "Wait up!"

    show cecil frown arm3

    hide nemo with softeaseout

    show cecil up

    nar "Nemo casually heads further into town, clearly used to the area."
    nar "There's so many people walking around that he's able to blend into the crowd easily."

    show nemo up frown at center:
        zoom 1.2
    with dissolve

    c frowntalk "Is this place always this busy?"

    show cecil frown

    n frowntalk "Yes, all day every day."
    n arm2 eye2 "People from all across the country come in through the port on the river and the trains. The marketplace here is one of the best to get foreign foods and items."
    n eye1 "I was here a little over a week ago."

    show nemo frown

    cn frown "Is he always on the road?"

    c frowntalk "Are you just a vagabond?"

    show cecil frown neutral

    n frowntalk arm1 "At heart I still am."
    n talk "Traveling is second nature to me. You learn to go wherever the winds take your sail."

    show nemo frown

    cn frown eye2 "Perpetually traveling... being a lone wanderer... the concept feels so foreign to me."
    cn frown scared "Sleeping by the fire last night was kind of fun, but to do that on the regular... to not have a home you regularly return to..."
    cn frown "He said he couldn't imagine a fate worse than needing blood constantly or going mad, but..."

    show cecil neutral

    n frowntalk arm2 "Sure seems like there's more people in town today. Maybe someone's having a sale?"

    show nemo frown arm1

    stop music fadeout 2

    scene bg city3:
        xalign 0.3
        zoom 0.65
        yalign 0.8
    with sidefade

    show cecil up frown arm1 at side
    show nemo up frown at center
    with dissolve

    play music "audio/Isolation Waltz.mp3" fadein 4
    queue music "audio/Isolation Waltz.mp3"

    nar "We approach the train station to see a crowd of people gathering outside it."

    n frowntalk surprise eye2 "What's going on...?"
    n frowntalk up eye1 "Ahoy!"

    show nemo frown


    show nemo at left with ease

    show npcmasc1 behind nemo at right:
        zoom 0.78
        xalign 1.0
        yalign 0.3
    with easeinright

    n frowntalk "What seems to be the trouble?"

    show nemo frown

    "Gentleman" "The trains aren't running, I'm afraid."

    n frowntalk surprise "Pardon?"

    show nemo frown

    "Gentleman" "There was a horrible collision down the line that they're still fixing up. Last they telegraphed, the wreckage is still smoldering."
    show nemo down
    show cecil unsure
    "Gentleman" "It'll be at least a week or more before any train can safely leave southbound."

    c unsure frown "—!"

    n frowntalk "A week... dang..."

    show nemo frown at shake
    show npcmasc1 at shake
    show bg city3 at shake

    c frowntalk arm2 "O-Over a week?! We can't wait that long!"

    show cecil frown arm1

    n eye2 arm2 "..."
    n frowntalk eye1 arm1 "C'mon."

    show nemo frown

    c frowntalk arm2 "Why? We have to get to Lauremburg!"

    show cecil frown

    n frowntalk "C'mon, Cecil."
    n frowntalk "The train isn't going to get here any faster standing around."

    show nemo frown

    c arm3 "..."

    show cecil frown


    scene bg city3:
        xalign 0.5 zoom 0.56 yalign 0.8
    show cecil unsure frown arm1 at side
    with sidefade

    nar "The crowded train station fades behind us as Nemo walks away."

    c frowntalk arm2 "Hey..."

    show cecil frown

    scene bg pier:
        zoom 0.65
        yalign 0.1 xalign 0.5
        linear 1.0
        ease 3.5 yalign 0.7 xalign 0.5
    with fadee

    play foley "audio/seagulls.mp3" fadein 2

    pause(0.8)

    nar "I trail behind him until we end up at the shore. By now, the sun is starting to set."
    nar "Lots of smaller ships line the waterfront with sailors coming and going."

    cn "I've never actually seen sailors in person. Some of them are more gruff than I imagined. ...Some are a lot younger than I imagined."

    show nemo pink sad frown at center
    show cecil pink unsure frown arm3 at side
    with dissolve

    n frowntalk eye3 arm2 "Sigh..."
    n frowntalk eye2 "Hate to say it, but..."
    n frowntalk arm1 down "I'm going to rent a boat for us."

    show nemo frown

    c frowntalk surprise "A boat?"

    show cecil frown

    n frowntalk "This river snakes downward past Lauremburg. We can sail to it from here."

    show nemo frown

    c frowntalk up arm2 "R-Really?!"

    show cecil frown arm1

    n frowntalk "Yes. It's not like we can use the money for train tickets, anyway."
    n frowntalk "Wait here and I'll get a skiff."

    show nemo frown


    hide nemo with Dissolve(1)

    cn frown unsure "Is it just the setting sun playing tricks on my eyes..."
    cn frown "...Or does he look dismayed by this?"

    stop foley fadeout 2


    scene bg sea:
        zoom 0.6
        xalign 0.5
        yalign 0.7
    with fadee

    show nemo blue up smile:
        zoom 1.1
        xalign 0.5
        yalign 0.1
    show cecil blue up frown at side
    with dissolve


    play foley "audio/waves.mp3" fadein 1

    show bg sea at bigcurtsy:
        zoom 0.6
        xalign 0.5
        yalign 0.7
    show nemo at bigcurtsy

    n talk "...And we're off!"

    show bg sea at curtsy
    show nemo smile at curtsy

    cn frown unsure "Just hold on, just hold on—!"
    cn frown "Don't let him know you're scared! And definitely don't get seasick!"

    n grin arm2 "Hah, you look pale. Don't tell me this is your first time on a boat."

    show nemo smile

    c frowntalk arm2 "I-I've been on boats before... but they were for small laps around a lake..."

    show cecil frown arm3 eye2

    n talk "Just think of this as a long lap in a really long lake. It's basically the same thing."

    show nemo smile at curtsy, shakeslow

    nar "Nemo does something with the rope at the front of the boat before grabbing the oar (?) again. Does he have to row all the way there?"

    c frowntalk up eye1 "This boat's a lot smaller than some of the ones at the pier."

    show cecil frown

    n frowntalk arm1 "It's called a skiff. Sailors use these in rough waters and for sailing."

    show nemo frown

    c frowntalk "Do you go sailing often?"

    show cecil frown

    n down eye2 arm2 "..."
    n frowntalk eye3 "When I was younger than you, I was a deckhand on a boat owned by a wealthy family."
    n frowntalk eye2 "I worked on several bigger boats like that for years."

    show nemo frown

    cn frown surprise arm1 "Why doesn't he do that anymore?"
    cn frown unsure "He seems good at sailing. I haven't even noticed any choppy waves."

    c frowntalk neutral "Have you always worked odd jobs?"

    show cecil frown

    n frowntalk up eye3 "Whatever I could get my hands on in whatever town I ended up at. Money was always running short."

    show nemo frown eye2

    c frowntalk surprise "\"Was\"?"

    show cecil frown

    n frowntalk "...Is."

    show nemo frown

    nar "He turns back to the water. Even though it's dark out here with only the moonlight lighting the world, he doesn't seem perturbed."

    c frowntalk up "How do you know where you're going?"

    show cecil frown

    n frowntalk eye1 arm1 "D'you forget where you were?"
    n frowntalk "Lauremburg is due south of here. All I have to do is follow the river down."

    show nemo frown eye2

    cn eye2 "It's so big, though... in the darkness, I can't see the banks on either side."

    show bg sea at curtsy
    show nemo at curtsy

    c frowntalk arm2 eye1 "Oh! Don't sailors use constellations to guide them?"

    show cecil smile
    show nemo eye1

    nar "He looks up and nods."

    show cecil arm1

    n frowntalk arm2 "Unless you're traveling the continent, the constellations stay relatively the same depending on the time of the year. They change with the season, but they return to the same spots every year."
    n frowntalk arm1 "You'll always see the constellation Ophiuchus in the summer 'nd you can determine the directions depending on how he's holding Serpens."
    n frowntalk eye3 "As long as the sky is clear enough, you'll never get lost."

    show nemo frown eye2

    show bg sea:
        zoom 0.6
        xalign 0.5
        yalign 0.0
    show nemo:
        yalign -0.1
    with ease

    cn frown "The stars are really pretty tonight, but I don't see how he can read them that well. They just look like gems scattered across the sky to me."
    cn frown "Oh, right."

    show bg sea:
        zoom 0.6
        xalign 0.5
        yalign 0.7
    show nemo:
        yalign 0.1
    with ease

    c frowntalk neutral "You and that man were talking about rare gems, weren't you?"

    show cecil frown

    n eye1 "...?"
    n frowntalk "What about them?"

    show nemo frown

    c frowntalk eye2 arm3 "...My father has always described his job as being a jeweler, but I think he mainly imports gems."
    c "On the few business trips I've been on with him, they were talking about importing crates from overseas."
    c arm1 "He's shown me a lot of pretty gems, too."

    show cecil frown

    cn scared "\"There are some gems that hurt vampires. Just a small touch is like burning them\"."
    cn arm3 "That vampire... What was that flash that happened when I touched him?"

    c frowntalk unsure arm1 eye1 "Mister... Gems can hurt vampires, right?"

    show cecil frown

    n frowntalk arm2 "If they touch their skin, yes."
    n arm1 "I haven't seen any that hurt them without touching 'em, but most vampires will back off anyway if they see you brandishing one."

    show nemo frown

    c frowntalk arm2 "What if you touch a gem and then touch a vampire?"

    show cecil frown arm1

    n frowntalk eye3 "Not gonna work."

    show nemo frown eye1

    c frowntalk arm2 "What if you hold a gem for a {i}really{/i} long time?"

    show cecil frown arm1

    n frowntalk eye3 "No."

    show nemo frown eye1

    c arm3 eye2 "..."

    cn frown "Then what was it?"

    scene bg sea:
        zoom 0.6
        xalign 0.5
        yalign 0.7
    with Dissolve(1.0)

    nar "I lean back against the side of the boat and put my hand into the water."

    show bg sea:
        zoom 0.6
        easein 2.0 xalign 0.5 yalign 0.0

    cn frown "I used to be scared of nighttime."
    cn frown "Annie would have to check my closet and room multiple times before I'd go to bed."
    cn frown "But out here, with a thousand gems glowing down upon us... it's serene."



    show bg sea:
        zoom 0.6
        easein 2.0 xalign 0.5 yalign 0.7

    pause(1)
    cn frown "Nemo's real good at steering. It's almost like he's not even thinking about it."
    cn frown "His gaze is fixed far off on the distant horizon."

    scene bg sea:
        zoom 0.6
        xalign 0.5
        yalign 0.7
    show nemo blue up smile at center:
        zoom 1.1
    show cecil blue neutral frown at side
    with dissolve

    n frowntalk "Get some sleep. It'll be a few more hours before we reach Lauremburg."

    show nemo smile


    scene bg sea:
        zoom 0.6
        xalign 0.5
        yalign 0.7
    with dissolve

    pause(1)

    stop foley fadeout 2
    stop music fadeout 2









    $ save_name = "A Partner or Two"
    $ chapter_num = "Eight"

    call chapter from _call_chapter_7



    scene bg city4:
        zoom 0.5
        yalign 0.6
        xalign 0.5
    with fade

    $ nemopov = False
    $ cecilpov = False


    play foley "audio/seagulls.mp3" fadein 2

    nn frown "I didn't expect to be back here so quickly. I'll have to apologize to Scott for the delay, but he should understand. Safety comes first."
    nn frown "Blazes, they might have already caught the guy."
    nn frown "That might be too wishful thinking, though... There's a lot of vampires that call Lauremburg home."

    nar "Even after I secure the boat to the dock, Cecil is still fast asleep."

    nn "I guess not all kids are light sleepers."

    show bg city4 at shakeonce

    nar "I step back into the boat and shake his shoulder."

    $ nemopov = True

    show nemo up smile arm2 at side

    n frowntalk "Cecil, wake up."

    show nemo frown

    show cecil up frown eye3 at center:
        yoffset 100
    with dissolve

    show cecil eye1 at shakeslow

    c frowntalk "Hwah...?"

    show cecil frown

    nar "He groggily turns around and stops once his eyes land on the city behind him."

    play music "audio/Winter.mp3" fadein 5
    queue music "audio/Winter.mp3"

    $ achievement.grant("lauremburg")
    init:
        $ achievement.register("lauremburg")
        $ achievement.sync()
    $ achievement.sync()

    n talk eye1 arm1 "Welcome to Lauremburg!"
    n eye3 grin "Only took us a few days to get here despite all the trouble, not too bad if I say so myself..."

    show nemo smile eye1
    show cecil arm2 at shake

    c frowntalk "W-We're really here!"

    show cecil smile arm1 at cecilcurtsy
    show bg city4 at curtsy

    nar "I step out of the boat and help him up."

    stop foley fadeout 3

    hide cecil with dissolve

    show bg city4:
        zoom 0.8
    with dissolve

    show bg city4:
        easein 3.5 xalign 0.1
        easein 3.5 xalign 0.9
        repeat

    nn frown "The fisherman probably has a shop somewhere in town where I can return it later. But, as for now..."
    nn frown "We should make our way to the university. I'll talk to Scott after we find Ambrose."
    nn eye2 down "Knowing him, he's stressed out of his mind and furious at these attacks."

    show bg city4:
        zoom 0.5
        yalign 0.6
        xalign 0.5
    with dissolve

    show cecil up smile at center:
        yoffset 100
    with dissolve

    n talk eye1 up "Alright kid. You think your friend is here looking into the vampire attacks, right?"

    show nemo smile
    show cecil:
        easein 0.4 yoffset 120
        easein 0.25 yoffset 100
        repeat

    c talk arm2 "Right!"

    show cecil smirk:
        yoffset 100
    with ease

    n talk "Then we'll go to the university and find out more about them."

    show nemo smile

    c frowntalk surprise arm3 "Are you just going to start interrogating every chap you come across?"

    show cecil frown

    n frowntalk "I told ya already, I've got a partner here on campus."
    n talk "We'll see what's happening and if they've seen your friend, okay?"

    show nemo smile

    nar "He looks at me suspiciously but nods his head."


    scene bg college1:
        zoom 0.7
        yalign 0.8
        xalign 0.5
    show nemo up frown at side
    with fadee

    nn frown "The vampire attacks haven't put a damper on the university it seems."

    show bg college1:
        zoom 0.9
    with dissolve

    show bg college1:
        easein 3.5 xalign 0.1
        easein 3.5 xalign 0.9
        repeat

    nar "Around us people are walking around, heading to class, talking to each other."

    nn frown "Maybe all the attacks have only happened at night? It's hard to be scared of a potential vampire biting you in broad daylight."
    nn arm2 "There's definitely extra security now. I don't remember even half of these guards being stationed here."
    nn eye2 "The coppers haven't found the culprit yet, that's for sure."
    nn eye1 down "Is the extra security to make people feel at ease or to try to catch them?"


    show nemo up arm1

    show bg college1:
        zoom 0.7
        xalign 0.5
    with dissolve

    show cecil up smile at center:
        yoffset 100
    with dissolve

    show cecil:
        easein 1.0 xalign 0.0
        easein 0.3 yoffset 80
        easein 0.25 yoffset 100
        easein 1.4 xalign 0.75
        easein 0.4 yoffset 80
        easein 0.25 yoffset 100
        easein 1.0 xalign 0.3
        easein 0.3 yoffset 80
        easein 0.2 yoffset 100
        easein 1.1 xalign 0.95
        easein 0.4 yoffset 80
        easein 0.25 yoffset 100
        easein 1.0 xalign 0.6
        easein 0.25 yoffset 80
        easein 0.2 yoffset 100
        repeat

    nn frown "Cecil seems to be enjoying it here, at least. He's looking around all wide-eyed at the aging buildings and people."
    nn unsure arm2 eye2 "Man, how'd a kid this sheltered think he'd make it far on his own...?"
    nn down eye1 arm1 "We should get a move on, though, because I'm not enjoying all the glares I'm getting from the guards."
    nn up eye2 "Admittedly, we must stick out like sore thumbs here—a laborer and a posh child strolling around a prestigious university..."

    show cecil up smile:
        easein 1.0 xalign 0.5 yoffset 100

    na "Ahoy, Nemo!"

    show cecil frown:
        ease 1.0 xalign 0.9

    show npc worker at left:
        zoom 0.6
        xalign 0.1
        yalign 0.35
    with dissolve

    n up eye1 "...!"
    n talk arm2 "Ahoy, Landon! How goes work?"

    show nemo smile

    landon "Good, good. I haven't seen you around in a couple weeks, what gives?"

    n frowntalk arm1 "I took a quick trip up north. One of the professors wanted me to pick 'em something up."

    show nemo smile

    landon "They've got you bein' an errand boy now? Tough luck these days!"
    landon "Still, good thing you headed out when you did. It's not safe anymore at night."

    n frowntalk down "Do tell. I just got back to town."

    show nemo frown
    show npc worker at shake

    landon "Some mad vampire has been attacking every few nights! Teacher, student, pedestrian, there's no difference."
    landon "Not a soul's died yet, but it's only a matter of time."

    nn eye2 "So they've just been attacks, not murders thus far. Still, if they were attacked and the victims are all alive, at least one of them should have seen the assailant."

    n frowntalk up eye1 "Horrible!"

    show nemo frown

    landon "It is! Ambrose sir's worried straight."
    landon "If you just got back to town, you should go see him. He's at a donor party at the cathedral."

    nar "I gently tip my cap."

    n talk "Thank you."
    n "C'mon, let's see what's happening in front of the cathedral."

    show nemo smile


    scene bg college1:
        zoom 0.7
        xalign 0.9
        yalign 0.8
    with sidefade

    show cecil up frown arm3 at center:
        yoffset 100
    show nemo up frown at side
    with dissolve

    c frowntalk "How'd you know that gardener?"

    show cecil frown

    n frowntalk "I've been coming here for about two years. I know most everyone here, 'cept for them new guards."
    n frowntalk arm2 "Remember what I told that gentleman on the carriage? I'm working with a professor here to find a cure for vampirism."

    show nemo frown arm1

    c surprise frowntalk "What's in it for you?"

    show cecil frown

    n grin "You kidding? It'll be worth millions!"

    show nemo smile

    c frowntalk eye2 unsure "Of course..."

    show cecil frown

    n frowntalk "C'mon, we're almost there. Don't get lost up here."

    show nemo smile

    scene bg cathedral:
        zoom 0.55
        xalign 0.5 yalign 0.0
        linear 0.7
        easein 2.3 yalign 0.8
    with fade

    $ nemopov = False

    pause(1)

    nn "Just as expected, the cathedral is crawling with blood suckers—that is, to say, rich investors."
    nn "Some of 'em seem nice, the others would clean a body of blood faster than a vampire if they thought it'd make 'em even richer."

    nar "Naturally, the security is even tighter here. I grab Cecil's wrist and lead him around the back."

    nn "If you want to get into somewhere uninvited, you either gotta act like you belong there or find someone to invite you in."
    nn "And since our clothes are dirty from the road, we'll have to go with the latter."
    nn "Maybe we should've stopped by the washroom before this... too late now."

    $ nemopov = True

    show bg cathedral
    show cecil unsure frown at center:
        yoffset 120
    show nemo up frown eye2 at side
    with dissolve

    c frowntalk arm3 "There's a lot of guards looking at us... Are you sure this is the right way?"

    show cecil frown

    n grin eye1 "'Course! Don't worry."

    nn frown eye2 "Just leave the worrying to me."
    show npcfem4 at left:
        zoom 0.7
        xalign -0.1
    with easeinleft
    nn up eye1 "Ah!{w} Marybelle is here and standing precariously close to the wine table. This should work."

    n talk "Ahoy, Marybelle!"

    show nemo smile

    mary "..."


    hide npcfem4 with easeoutleft

    n surprise frown "...?!"

    c frowntalk down arm3 "...Fantastic."

    show cecil frown

    show cecil:
        ease 0.8 zoom 1.2 xalign 1.38 yoffset 198

    pause(0.8)

    show guard behind cecil:
        zoom 0.4
        xalign 0.0
        yalign 1.0
    show guard as guard3 behind cecil:
        zoom 0.4
        xalign 0.8
        yalign 1.0
    show guard as guard2 behind cecil:
        zoom 0.55
        xalign 0.4
        yalign 0.15
    with dissolve

    guard "Sir."
    guard "If you're done calling on our guests, we'd like you to leave."

    nn frown down eye2 "Damn."
    nn frown "I'll get you back for this, Mary!"

    n talk arm2 eye3 surprise "Gentlemen, I'm sorry for the confusion. I was simply trying to talk to an acquaintance—"

    show nemo frown eye1

    guard "Yes, yes, I'm sure you were. You can talk to her after the party away from school grounds."
    guard "Come on, let's go."

    nn frown down arm1 eye2 "Dammit... Looks like I'll have to go home and wait until tonight."

    show cecil surprise

    "{color=#911418}???{/color=#911418}" "Ah, there you are!"

    n up eye1 smile "—!"


    show guard:
        xalign -0.1
    with easeinleft
    show guard as guard2:
        xalign 0.85
    show guard as guard3:
        xalign 1.1
    with easeinleft
    show cecil:
        xalign 1.5
    with easeinright
    show ambrose up smile coat glove glass parasol behind cecil at center:
        zoom 1.1
        xalign 0.18
        yalign 0.13
    with Dissolve(1.0)

    a talk eye3 "My assistant told me there was someone over here. Thank you guards, you can return to your places."

    show ambrose smile

    guard "..."


    hide guard
    hide guard2
    hide guard3
    with dissolve

    show ambrose eye1 with dissolve

    n talk "Security is a tad touchy now, eh?"

    show nemo smile

    a frowntalk eye2 "They're all rather trigger happy, I'm afrai—"
    a eye1 frown down "..."
    a frowntalk unsure "...Who is this?"

    show ambrose frown

    nn frown "That didn't take long for him to notice."
    nn frown eye2 surprise "Now, how am I going to explain this...?"

    show cecil:
        easein 0.4 yoffset 222
        easein 0.25 yoffset 198

    c talk arm2 up "I'm Cecil."

    show cecil frown arm1

    a frowntalk "...Hi."

    show ambrose frown

    n talk up eye1 "So, ah, this is Cecil."

    show nemo smile

    a frowntalk "Yes."

    show ambrose frown

    n frowntalk "We met a couple days ago and he wanted to get to Lauremburg so I offered to bring him."

    show nemo frown

    a frowntalk "I see."

    show ambrose frown down

    nar "He shoots me a \"you better have a longer explanation for this later\" look before taking a long sip of his wine."

    a frowntalk up eye3 "I'd love to talk more, but I've got a party to attend to."
    a frowntalk eye1 "I'll be at the apartment in an hour or two."

    show ambrose frown

    nn frown "He's not mad at me for something, right?"

    n talk "Alright."
    n "I still need to stop by Professor Scott's office, but that shouldn't take long."

    show nemo smile


    hide ambrose with Dissolve(1.2)

    n frown eye2 arm2 "..."

    nn surprise "I think he might be mad at me."


    scene bg college1:
        zoom 0.7
        xalign 0.9
        yalign 0.8
    with sidefade

    show cecil surprise frown arm3 at center:
        yoffset 100
    show nemo up frown at side
    with dissolve

    c frowntalk "Who was that man? He looked important."

    show cecil frown

    n surprise grin "Judge everyone by their looks, aye?"

    show nemo frown

    c frowntalk "He looked a lot better off than you and that's a fact."

    show cecil frown

    nn eye2 "Kids really don't hold back, do they?!"

    n frowntalk eye3 up "He's just the headmaster."

    show nemo smile eye1

    show cecil arm2 at shake

    c shock surprise "He-Headmaster?! Of the whole university?"

    show cecil frown

    n frowntalk eye3 "That's what being a headmaster means, yes."

    show nemo smile

    c frowntalk arm1 "How d'you know him?"

    show cecil frown

    n frowntalk eye2 arm2 "That's a story for another time."
    n talk eye1 arm1 "Let's stop by the professor's office and then we can take a break."

    show nemo frown


    scene bg office1:
        zoom 0.5
        xalign 0.5
    with fadee

    show nemo pink up frown at side
    show cecil pink surprise frown arm3 at center:
        yoffset 100
    with dissolve

    n frowntalk surprise "Scott?"

    nn frown "Why is his office so empty and unlocked? He's good about locking up before he steps out."

    hide cecil with dissolve

    nar "I leave Cecil at the door and walk in. I turn one of the gas lights on and hear a grumbling from the back."

    n frowntalk "Scott, it's me, Nemo."

    show nemo frown

    s "Urgh..."

    show scott pink frown up at center:
        zoom 0.7
    with dissolve


    nn frown sad "He looks terrible."
    nn frown "He's not the most fashionable gentleman in town, but he's never looked this haggard."

    n frowntalk "Everything alright?"

    show nemo frown

    s talk "...Haven't been able to sleep."

    show scott frown

    nn eye2 up "I guess the attacks have stressed everyone out."

    s talk "Were you able to find the gems?"

    show scott frown

    n frowntalk eye3 surprise "...Not yet."
    n frowntalk eye1 "I couldn't find them while I was there. I hurried back when I heard about the attacks."

    show nemo frown

    s down "...?!"
    show scott at shake
    s talk "What good will that do us?!"
    s talk "How do you expect to stop these attacks without a cure?!"

    show scott frown

    n frowntalk down "Hoy, calm down. I'll look for the gems in town."

    show nemo frown

    show scott at shake

    s talk "Don't you think I've done that?"
    s talk "Every merchant told me I'd have to go north to find them of the purity I want."
    s talk "I knew I should've gone on my own..."

    show scott frown

    nn frown arm2 eye2 "Sleep deprived or not, he's not thinking straight."

    nar "I shuffle around in his desk until I find his flask and toss it at him."

    n frowntalk eye1 "Drink something and get some sleep."

    show nemo frown

    s "..."
    s up talk "...Thanks."

    show scott frown

    n frowntalk arm1 "I'll be back later and you better be more lucid."

    show nemo frown


    scene bg college1:
        zoom 0.7
        xalign 0.9
        yalign 0.8
    with sidefade

    show cecil surprise frown arm3 at center:
        yoffset 100
    show nemo up frown eye2 arm2 at side
    with dissolve

    n frowntalk "...Sorry for that."
    n frowntalk eye1 "He's normally a lot, well, normal."
    n frowntalk eye3 "The attacks are taking a toll on everyone, looks like."

    show nemo frown eye1

    show cecil:
        easein 0.45 yoffset 120
        easein 0.25 yoffset 100

    nar "Cecil kicks the ground and slumps as he walks."

    n talk arm1 "No more stops for the night, how does that sound? We'll rest some and then eat dinner."
    n "So come on, stand up straight a little longer."

    show nemo frown

    c frowntalk unsure "Okay..."

    show cecil frown

    nn frown surprise "He's thinking about running off to find his friend, I bet. As tired as he is though, he won't try it right away."
    nn frown arm2 eye3 "I think I'll collapse on the couch as soon as we get home..."
    show nemo up smile
    extend " Ah, that'll be nice."

    stop music fadeout 2









    $ save_name = "The Headmaster"
    $ chapter_num = "Nine"

    call chapter from _call_chapter_8



    scene bg office2:
        zoom 0.4
        yalign 0.7
        xalign 0.5
    with fade

    $ nemopov = False
    $ cecilpov = True

    play music "audio/Isolation Waltz.mp3" fadein 4
    queue music "audio/Isolation Waltz.mp3"

    show cecil pink up smile at side
    show nemo pink up smile arm2 at center
    with dissolve

    c frowntalk arm2 "Woah!"

    cn smile arm1 "When Nemo opened the door to the apartment, I wasn't expecting much. I certainly wasn't expecting an entire studio!"
    cn "This place must contain the next apartment or two, all squished together to make one big suite!"
    cn "And the furniture is so nice... it's so ornate and pretty!"

    hide nemo with dissolve

    nar "Nemo plops down on one of the couches in the parlor."

    cn "This apartment is so big, I bet it has multiple parlors!"

    show bg office2:
        zoom 0.6
        xalign 0.85
        yalign 0.6
    with dissolve

    nar "I walk up to a desk and start opening the drawers, trying to see if it's one of those desks that doubles as a sewing machine or something else."
    nar "Relics and trinkets from different places line the walls alongside occasional photographs."

    cn "I think I've seen some of these in books about far away countries, but a lot of them I have no clue about. I could spend hours looking at them all!"

    show bg office2:
        easein 2.0 xalign 0.25
        linear 1.0
    pause(1)
    show nemo pink up frown at center with Dissolve(1.0)

    c frowntalk surprise arm3 "Who's place is this? I know it can't be yours."

    show cecil frown

    n frowntalk "It's Ambrose's. That's the headmaster guy you saw earlier."

    show nemo smile

    c unsure "..."

    show bg office2 at shakeslow
    show nemo pink at shakeslow

    cn frown arm2 "I-I've been running around in the headmaster's home?!"
    cn frown "How'd he even have the key to get in?"

    n talk surprise "What, {i}now{/i} you're getting nervous?"

    show nemo smile

    c frowntalk eye5 arm3 "I-It's just... This place is really nice."

    show cecil frown

    n frowntalk arm2 "Surely you lived in a mansion or something."

    show nemo frown

    c frowntalk eye1 "Yes, but this place... It's much more lived in."

    show nemo up

    cn frown neutral "I don't know how to describe it."

    c frowntalk arm1 "It... It feels relaxing."

    show cecil frown

    "{color=#911418}???{/color=#911418}" "I'll take that as a compliment."

    play music "audio/a432.mp3" fadein 2
    queue music "audio/a432.mp3"


    show nemo at left:
        xalign -0.5
    show ambrose pink up smile glass at right
    with easeinright

    c up "...!"

    a talk eye3 "Make yourself at home. You must be tired from traveling so far."

    show ambrose smile eye1

    n frowntalk arm2 eye2 "We did make it back as quick as possible..."

    show nemo frown surprise eye1

    a frowntalk down eye3 "I was talking to the child, not you."

    show ambrose frown eye1

    with hpunch

    nar "Mr. Ambrose hits Nemo's knee, making him move his feet off the couch so he can sit down."

    n "..."

    cn frown "It's only polite to take a seat when your host sits, right?"

    show bg office2 at curtsy
    show nemo at curtsy
    show ambrose at curtsy

    nar "I walk over and sit in an ornate armchair across from them."

    a frowntalk eye3 up "I was rather rushed earlier, I do apologize."
    show nemo up
    a talk eye1 "My name is Ambrose Prideaux. I'm the headmaster of Prideaux University."

    show ambrose smile

    cn frown "Nemo really wasn't kidding, then...!"

    c frowntalk arm2 "I-It's nice to meet you!"

    show cecil frown arm1

    stop music fadeout 2

    a talk eye3 "And this one here..."

    show ambrose smile

    cn frown "Huh?"

    play music "audio/Baltic Levity.mp3" fadein 2
    queue music "audio/Baltic Levity.mp3"


    show ambrose at curtsy

















    show cg leroy:
        zoom 0.78
    with dissolve

    a talk eye1 "...Is Leroy!"

    show ambrose smile

    $ achievement.grant("leroy")
    init:
        $ achievement.register("leroy")
        $ achievement.sync()
    $ achievement.sync()

    c frowntalk "H-Hi Leroy!"

    cn frown "Who names their dog \"Leroy\"?!"

    a talk "He's about 3 years old and he mostly sleeps all day."

    show ambrose smile

    cn frown "The dog looks asleep right now...!"

    c frowntalk "Can I pet him?"

    show cecil frown

    nar "Mr. Ambrose holds him closer to me and I pat Leroy's head."

    cn frown "So warm... Are all dogs this soft?"











    hide cg leroy with dissolve

    show ambrose at curtsy

    stop music fadeout 2

    nar "He puts Leroy down on the couch, where he plops his head on Nemo's leg."

    n frowntalk arm1 "Let's get down to it. What's up with these attacks?"

    show nemo frown

    play music "audio/a432.mp3" fadein 2
    queue music "audio/a432.mp3"

    a frowntalk eye3 "Sigh..."
    a frowntalk eye1 "They started after you left."
    a frowntalk eye2 "Reports started coming in of people being accosted at night by a vampire and drained of some of their blood."
    a frowntalk eye3 "There was nothing similar about the victims either, aside from them walking around town near and on campus at night."
    a frowntalk "Some of them were professors or students, some were laborers, one was even a young lady."
    a frowntalk eye1 "There's been 4 attacks that have been reported so far. None of them got a good look at the assailant other than he was a middle aged man, though we're unsure if it's all the same attacker."
    a frowntalk "The police have increased their patrols and are now taking up residence here. I can't look around without seeing a handful of unfamiliar guards."

    show ambrose frown

    cn frown unsure eye2 "His university has turned into a feeding frenzy for vampires and he's unable to stop any of it. I feel bad for him."

    show cecil eye1

    a frowntalk eye3 "Some people feel more at ease with the extra security, but I know several students and professors who refuse to attend their night classes."
    a frowntalk eye2 "Admittedly, I've been double-locking the doors and windows before bed every night..."
    a frowntalk eye1 "That's why you came back, right?"

    show ambrose frown

    nar "Nemo nods."

    n frowntalk "We heard about them and hurried here."

    show nemo frown

    a frowntalk "Then, please—"

    show ambrose frown:
        easein 0.5 xoffset -200

    nar "Mr. Ambrose clasps Nemo's hand in his."

    a frowntalk "Find the attacker!"

    show ambrose frown

    n grin "Did you think I'd come back empty handed just to check up on you? Of course I'm going to hunt down the scum."

    show nemo smile
    show ambrose:
        easein 1.0 xoffset 0

    nar "Mr. Ambrose relaxes and lays back on his couch, relieved. Nemo hands him a glass of water from the coffee table."

    a frowntalk eye3 up "Thank you..."
    a talk eye1 "So, tell me what brings you into town then, Cecil."

    show ambrose smile

    c up frown arm1 eye1 "...!"

    cn frown "Ack! He's addressing me again!"
    cn frown unsure "I can't just tell him why, right? He's a headmaster and stuff! He'll turn me in!"
    cn frown "He'll say how it's too dangerous for a kid to be here without their parents with so many attacks happening and ship me back north. I have to make up a lie!"

    c frowntalk eye2 "I-I... uhm..."
    c arm3 "Well... I... You see..."

    show cecil frown

    n talk "Hah!{w} Idiot, Ambrose can already assume you're a runaway. There's no point in hiding it."

    show nemo smile at shakeonce
    show ambrose at shakeonce
    show bg office2 at shakeonce

    c frowntalk up arm2 eye1 "Re-Really?!"

    show cecil frown

    a frowntalk "Your clothes are a tad dirty, but I assume that's from your unorthodox travels. They're still vastly more posh than what an orphan would wear."

    show ambrose frown

    c frowntalk eye2 arm3 unsure "Oh..."

    cn frown "How many orphans have these two seen, anyway?!"

    show nemo frown

    c frowntalk eye1 "Well... I'm looking for my friend Lucie."
    c frowntalk "She ran away from home about a week ago and I want to find her."

    show cecil frown

    a frowntalk unsure "What does she look like?"

    show ambrose frown

    c frowntalk up arm2 "She's my age and she's really pretty! She's like a doll!"
    c talk arm1 "Her hair is really light and long and curly and she has pretty purple eyes. Lucie's always wearing fancy dresses. She's from a rich family too."

    show cecil smile arm1

    n surprise eye2 "..."

    a frowntalk "...What makes you think she came here?"

    show ambrose frown

    c frowntalk "Before she left, she was reading the newspaper a lot and had clippings of vampire attacks. That's why I think she came to Lauremburg—she saw the newspaper report and headed south."

    show cecil frown

    a frowntalk "Why would she be interested in vampire attacks? They're rather grisley for such a young lady."

    show ambrose frown

    c frowntalk eye3 unsure "I don't really know..."
    c frowntalk eye2 arm3 "Whenever I asked her, she said it was research and would hide it."

    show cecil frown up arm1 eye1

    a frowntalk eye3 "I'm afraid I haven't seen anyone like that around campus. It's not typical that we have children walking around."
    a frowntalk eye2 "Lauremburg is a big city, though, and I don't leave campus much."

    show ambrose frown eye1

    cn frown down eye3 arm3 "Darn."
    cn frown eye2 unsure "When this guy said he was the headmaster, I was really hopeful..."
    cn frown "...He's right, though, Lauremburg looks really big. Maybe she's only walking around at night."
    cn frown "Wait, no, please don't be walking around alone at night, Lucie!"

    c frowntalk eye1 up arm1 "Thank you for all your help."

    show cecil frown

    n frowntalk up eye1 arm2 "Cheer up, we'll look for her tomorrow, alright?"

    show nemo smile

    c frowntalk down "Hmph... Why tomorrow?"

    show cecil frown

    n frowntalk eye3 "I say tomorrow because I'm darn tired and I'm going to take a nap. You should too."

    show nemo frown eye1

    nar "He throws his hand towards one of the doors on his left."

    n frowntalk arm1 eye2 "You can lay down in the bedroom over there."

    show nemo frown eye1

    c frowntalk up arm1 eye1 "Huh?"
    c frowntalk arm2 "Wait, are we staying here?"

    show cecil frown arm1

    n frowntalk "Unless you want to sleep outside again, yes."

    show nemo frown

    a frowntalk up eye2 "Ah, look at the time... My breaks are getting shorter and shorter."
    a talk eye1 "I've got a couple more meetings to attend to tonight, so you might have to eat supper alone. I'll be back before bedtime, though."
    a talk "Get some rest, okay?"

    show ambrose smile


    hide ambrose with softeaseout

    hide nemo with dissolve

    cn frown up eye1 "We're staying in such a nice place tonight..."
    cn frown "And tomorrow, we're going to patrol around town and find Lucie."
    cn smile arm2 "We'll find her."

    stop music fadeout 2









    $ save_name = "Late Night Drink"
    $ chapter_num = "Ten"

    call chapter from _call_chapter_9



    scene bg office2 night:
        zoom 0.55
        yalign 0.65
        xalign 0.5
    with fade

    play foley "audio/fireplace.mp3" fadein 1

    play music "audio/Winter.mp3" fadein 3
    queue music "audio/Winter.mp3"

    $ nemopov = True
    $ cecilpov = False

    show nemo pinknight up smile arm2 nocap at side
    show ambrosen pinknight up smile:
        zoom 1.3
        xoffset 175
        yalign 0.13
    with dissolve

    nn "Nothing better than a drink after a long day."
    nn "A good drink, good company..."

    show ambrosen talk

    a "Want some more to drink?"

    show ambrosen smile

    nar "I let him top off my drink."

    nn frown "He's terrible at picking comfortable furniture but damn good at picking brandy."

    show ambrosen down frowntalk

    a "Ah... This would taste better if I knew there wasn't an attacker running loose out there right now."

    show ambrosen frown

    n talk "It's just a matter of time now."
    n "Stop fretting so much or you'll be the next one attacked."

    show nemo smile
    show ambrosen talk unsure

    a "Would you protect me?"

    show ambrosen smile

    n grin surprise "You kidding? I'd grab Leroy and run."

    show nemo smile up arm1

    nar "He tries to hide his smirk behind his wine glass."





    show cecil pinknight neutral frown eye3 arm1 behind ambrosen at right:
        xalign 1.3
        zoom 1.0
        yoffset 150
    with easeinright

    c frowntalk "Mmm... Dinner was good..."

    show cecil frown

    n frowntalk "Did you take a nap afterwards?"

    show nemo smile

    c frowntalk "Mhm... What are you drinking?"

    show cecil frown

    n frowntalk "Something you can try when you're older."

    show nemo smile

    c frowntalk unsure eye2 "Aww..."
    c frowntalk eye1 "We're going to go out tomorrow, right?"

    show cecil frown

    n frowntalk "Only if you go to bed."

    show nemo frown

    c frowntalk eye3 "Okay..."
    c frowntalk "Goodnight..."

    show cecil frown


    hide cecil with softeaseout

    show ambrosen down frown

    nn frown eye2 "He could barely keep his head up long enough to talk. He must not have napped earlier when we got here."
    nn frown "Looks like he'll be knocked out tonight. Won't have to worry about him sneaking out on his own, at least."

    n eye1 "..."

    nn eye2 unsure "Oh no, he's giving me that look again."

    show ambrosen unsure frowntalk

    a "Are you ready to explain why you came home with a kid yet?"

    show ambrosen frown

    n frowntalk up arm2 "Eh..."

    show nemo frown
    show ambrosen unsure frowntalk:
        easein 0.12 xoffset 185
        easein 0.12 xoffset 170
        easein 0.12 xoffset 190
        easein 0.12 xoffset 165
        easein 0.12 xoffset 175

    a "\"Eh\"?!"

    show ambrosen frown

    n frowntalk down eye1 "Look at him! He has no common sense and is about as gullible as they come."
    n "He was scooped up by some medium and then immediately got attacked by vampires."

    show nemo frown eye2
    show ambrosen eye3 frowntalk

    a "And you call me the soft one..."

    show ambrosen frown

    nar "He takes a long sip of his wine."

    show ambrosen eye2 frowntalk neutral

    a "I just... I don't want you getting too attached again."
    show ambrosen eye1
    a "He's a runaway, not an orphan. He has a family to return to."

    show ambrosen frown

    n "..."

    nn frown "What does he think I am, child services?"

    n frowntalk eye3 arm1 "When he finds his friend, we'll telegraph his family and send them both on the first train north."

    show nemo frown eye1
    show ambrosen eye2 unsure

    a "..."
    show ambrosen frowntalk
    a "About his friend, though..."

    show ambrosen frown

    nn frown down "He noticed it too, didn't he?"

    show ambrosen up frowntalk eye1

    a "What do you know about her?"

    show ambrosen frown

    n up frowntalk "That was the most I'd heard about her today."
    n down "I know what you're hinting at."

    show nemo frown up
    show ambrosen frowntalk neutral

    a "Do you think it's her?"

    show ambrosen frown

    nn frown eye2 "It does sound a lot like her. Something impulsive she'd do without a care in the wind for others."

    n frowntalk eye3 "Who knows? It sounds stupid and reckless enough for her to come up with."

    show nemo frown eye1
    show ambrosen eye3 down frowntalk

    a "Sigh... And you're not worried about it at all?"

    show ambrosen frown

    n frowntalk eye2 "What's there to worry about?"

    nn frown arm2 "It's not like I can stop this."

    show ambrosen frowntalk eye1

    a "It'll get ugly quick if that's the case."

    show ambrosen frown

    n talk up eye1 arm1 "Hah! You think?"

    show nemo frown

    nar "I take a quick swig of my drink."

    n talk eye3 "It might turn into a comedy."

    show nemo frown eye2
    show ambrosen neutral frowntalk eye1

    a "Then stay here."
    a "It doesn't have to be like that."

    show ambrosen frown

    n frowntalk eye3 arm2 "You know I can't."
    n eye2 arm1 "Staying in one place all the time isn't how I got here."

    show nemo frown
    show ambrosen down frowntalk

    a "Then stop treating here like a side stop instead of the destination."

    show ambrosen frown

    n frowntalk eye3 "Sigh..."

    nn frown eye2 "This conversation again."

    nar "I take another long sip."
    nar "He leans closer and rests his head on my shoulder."

    nn eye3 "I wish it were that simple."

    stop music fadeout 2
    stop foley fadeout 2







label latelatenightdrink:

    $ save_name = "Late Late Night Drink"
    $ chapter_num = "Eleven"

    call chapter from _call_chapter_10



    scene bg cecilbedroom night:
        zoom 0.8
        yalign 0.6
    show cecil night up frown eye3 at side
    with fade

    $ nemopov = False
    $ cecilpov = True

    cn frown "Mmm..."
    cn frown "Thirsty..."

    play music "audio/Isolation Waltz.mp3" fadein 2
    queue music "audio/Isolation Waltz.mp3"

    show cecil eye1

    nar "I sit up in bed, albeit a little wobbly. It's weird and disorienting to wake up in a bed that's not mine."
    nar "My mouth is annoyingly dry and I can't go back to sleep."

    cn frown surprise "What time is it...?"

    nar "Outside, it's still clearly dark. Lamp posts are on but from the other windows I can see the lights are all off."
    nar "The moon is still high in the sky. Maybe it's only been an hour or two since I fell asleep."

    cn frown up "I'll just grab a quick glass of water and go back to sleep."


    scene bg office2 night:
        zoom 0.6 yalign 0.6 xalign 0.5
    show cecil pinknight frown eye3 at side
    with sidefade

    cn frown "Surely Mr. Ambrose and Nemo are asleep—"

    stop music



    play music "audio/Nightmare.mp3" fadein 1
    queue music "audio/Nightmare.mp3"

    c frowntalk scared arm2 eye1 "—!!"

    scene cg bite1:
        zoom 0.85 xalign 0.5
    show cecil pinknight frown eye7 at side
    with dissolve

    cn frown "Blood."
    cn frown arm1 "Streaming from Nemo's arm is blood."
    cn frown "And right beside him is Mr. Ambrose, licking it up."
    cn frown "Nemo's eyes are closed. He doesn't make a sound."
    cn frown scared "What do I do?"
    cn frown "What can {/i}I{i} do?"
    cn frown "I'm not a gun-slinger like him. The best I could manage was to shove a vampire and then immediately get attacked again."
    cn frown "But I... I have to do something!"

    c frowntalk eye1 "W..."
    with hpunch
    c frowntalk "WAKE UP!!"

    show cecil frown

    show cg bite2 as cgbite2:
        zoom 0.85 xalign 0.5
    show cecil pinknight frown eye7 arm2 at side
    with hpunch

    a "—?!"
    n "Hwah?"

    stop music fadeout 6

    a "What are you doing up?"

    c frowntalk down eye1 "What am I doing up? What do you think you're doing?!"

    show cecil frown arm3



    a "Getting a late night drink."

    c "..."

    stop music
    play music "audio/Baltic Levity.mp3" fadein 2
    queue music "audio/Baltic Levity.mp3"

    show cg bite3 as cgbite3:
        zoom 0.85 xalign 0.5
    with dissolve

    n frowntalk "What's with all the racket?"

    c frowntalk unsure "Y-You're awake?!"

    show cecil frown

    n frowntalk "'Course!"

    c frowntalk "You didn't drink too much?"

    show cecil frown

    n "Why d'you think I was drinking so much?"
    n "Why are you still up?"

    c frowntalk eye5 unsure arm3 "I-I wanted to get some water."

    show cecil frown

    a "There's some glasses in the far right cabinet in the kitchen."

    cn frown "I don't even care about my dry mouth anymore. I just want to go back to sleep and wake up to find this was a terrible, embarrassing dream."

    show bg office2 night:
        zoom 0.6 yalign 0.6 xalign 0.5
    with sidefade

    nar "I walk over to the kitchen and grab a glass from where he said they were. Behind me, they're whispering something."

    cn frown eye6 "Just get the water. Just get a glass of water and go back to bed."
    cn frown eye2 "Ignore that you're staying at a vampire's home. Tomorrow's Cecil can deal with that."

    hide bg office2 night with sidefade

    nar "When I walk back through the parlor, they're both still sitting on the couch looking at me."


    c frowntalk "G-Goodnight."

    show cecil frown

    a "Goodnight."

    n "Knock before you come in next time."

    c frowntalk eye1 down arm2 "You're in the parlor!"

    show cecil frown

    n "And it's our parlor!"

    stop music


    scene bg cecilbedroom night:
        zoom 0.87
        yalign 0.6
    show cecil night eye3 scared frown at side
    with hpunch

    cn frown "I pray I'll never have to encounter something like that again."

    show cecil neutral


    play foley "audio/clock.mp3"

    nar "I take a long sip of water."


    pause(1.0)

    cn frown unsure eye2 "Why is he giving blood to a vampire?"
    cn frown "No, why is he so close to one in the first place?"
    cn frown "The way he talks, this is his {/i}home{i}. Why does he choose to live with a {/i}vampire{i}?"
    cn frown "Annie always taught me vampires are good-for-nothin's, that all they want is to take from people."


    pause(1.0)

    cn frown scared "I thought he hated vampires."

    c "..."

    nar "I side-eye the door to the room and lock it before climbing back into bed."

    stop foley fadeout 2











    $ save_name = "One Too Many Drinks"
    $ chapter_num = "Twelve"

    call chapter from _call_chapter_11

    $ nemopov = True
    $ cecilpov = False

    scene bg office2:
        zoom 0.45
        yalign 0.65
        xalign 0.5
    show nemo pink down frown arm2 eye3 nocap shirttie at side
    with fade

    play music "audio/Winter.mp3" fadein 2
    queue music "audio/Winter.mp3"

    n frowntalk "Ugh..."

    show nemo frown

    nar "I roll over and clasp my throbbing head until the room stops spinning."

    nn frown eye2 "Okay, maybe I had one too many drinks last night."

    show nemo eye1

    a "Here."

    show ambrose pink smile at center:
        zoom 1.1
        xoffset 175
    with dissolve

    nar "Ambrose walks over and hands me a glass of water."

    a talk "Good morning."

    show ambrose smile

    nar "I sit up in bed and take a few swallows."

    n frowntalk up "Good morning..."

    nn frown eye2 "He's in a good mood this morning. He doesn't usually get up this much earlier than me."
    nn frown eye3 down "Mmm, my head is still groggy... Nothing to do but drink it off."
    nn frown eye2 "No, that's not it... There's something nagging at me aside from this hangover, but what was it...?"

    n "..."

    nn frown eye1 up arm1 "Cecil!"
    nn frown eye2 "The little idiot got all scared when he saw Ambrose last night.{w} ...I guess I did forget to mention he's a vampire..."

    show nemo eye1

    a frowntalk "You should talk to him before breakfast."

    show ambrose frown

    n frowntalk eye2 arm2 "It's your fault for making out on the couch..."

    show nemo frown

    a talk eye3 "Who said he was too comfy to go to bed?"
    a eye1 "Get dressed and come on."

    show ambrose smile


    scene bg office2:
        xalign 0.25 yalign 0.6 zoom 0.75
        easein 2.0 xalign 0.7 yalign 0.6 zoom 0.75
    show nemo pink up frown arm2 nocap at side
    with fade


    play sound "audio/knock.mp3"

    n frowntalk "Cecil? Are you awake?"

    show nemo frown

    "..."

    n frowntalk arm1 "Cecil."

    show nemo frown

    c "...I'm up."

    n frowntalk "Can I come in?"

    show nemo frown

    c "..."
    c "Yes."

    nar "I can hear the sound of light footsteps and the door unlocking."


    scene bg cecilbedroom:
        zoom 0.8
        yalign 0.7
    with sidefade

    show cecil neutral frown eye2 at center:
        yoffset 100
    show nemo up frown nocap at side
    with dissolve

    nn frown "I'm a bit surprised to see him fully dressed already. How late did I sleep in...?"

    n talk "So, ah... How did you sleep?"

    show nemo frown

    c frowntalk "Okay."

    show cecil frown

    n talk arm2 "Pretty different sleeping in a bed that's not yours, isn't it?"

    show nemo smile

    c frowntalk "Yes."

    show cecil frown

    n talk "You ready for some breakfast?"

    show nemo smile

    c "..."

    c frowntalk eye1 down "Why are you helping a vampire?"

    show cecil frown

    nn frown arm1 down "I can tell already by the look in his eyes."
    nn frown "Nothing I say will make sense to him. It's not that I can't explain myself eloquently enough or give a good enough case. It's not that he's too stubborn or stupid to understand."
    nn frown "It's that his world view can't encompass this yet."
    nn frown "He was raised in a way so as to not understand vampires. As sheltered as he is, I'm sure the first vampires he ever saw in person were the ones that attacked him in that alley."
    nn frown "Those eyes won't accept this yet."
    nn frown "I had the same look when I was his age."

    c frowntalk arm3 "Well?"

    show cecil frown
    show nemo up eye3 arm2

    nar "I shrug."

    n frowntalk "Things happen."

    show nemo frown eye1 arm1
    show cecil at shake

    c frowntalk "\"Things happen\"?"

    show cecil frown

    n frowntalk eye2 arm2 "Things just... happen."
    n frowntalk arm1 "I came to the university a couple years ago when I heard there was a professor researching a cure to vampirism."
    n frowntalk "While I was in town, I started working odd jobs. Most of 'em were on campus since I was already here."
    n frowntalk arm2 "One thing led to another and..."

    show nemo frown

    c frowntalk "And what?"

    show cecil frown

    n frowntalk down eye4 "And that's it!"
    n eye6 "You're too young to understand."

    show nemo frown eye3

    c frowntalk "I still don't get why you're helping a vampire."

    show cecil frown

    n frowntalk eye2 arm1 "Look... Not every vampire is constantly bloodthirsty and ready to attack people on a whim."
    n frowntalk eye1 "Most vampires are just snobby elites. You see how rich Ambrose is, a lot of vampires are the same way."
    n frowntalk up "He's not going to attack you like some hoodlum in a back alley."
    n frowntalk "Now come on before breakfast gets cold. We can look for your friend after breakfast."

    show nemo smile

    c talk arm2 up "Okay!"

    show cecil smile

    nn frown "Well, at least that perked him up."


    scene bg office2:
        zoom 0.45
        yalign 0.65
        xalign 0.5
    with fade

    show ambrose pink up smile at right:
        xalign 1.9
    show nemo pink up frown nocap at side
    show cecil pink up frown at left:
        yoffset 220
        xoffset 600
    with dissolve

    a talk "How did you sleep, Cecil?"

    show ambrose smile
    show cecil scared arm3 eye2

    nn frown arm2 "...And now he's back to acting nervous."

    c frowntalk "Okay."

    show cecil frown

    a talk eye3 "I don't have many guests over I'm afraid, so I hope it wasn't too dusty in there."
    a frowntalk eye2 "Today I have a board meeting followed by a couple faculty meetings so I won't be home until dinner."

    show ambrose smile eye1

    nn frown eye2 "I wonder if we should swing by Scott's office today. He seemed so out of it yesterday, maybe he's feeling better today."
    nn frown surprise "I already told Cecil we'd search for his \"friend\", though... Hmm..."

    c frowntalk eye1 surprise "Why are you a vampire?"

    show cecil frown:
        easein 0.12 xoffset 615
        easein 0.12 xoffset 585
        easein 0.12 xoffset 615
        easein 0.12 xoffset 585
        easein 0.12 xoffset 600
    show ambrose frown at shake
    show bg office2 at shake



    nn frown eye1 surprise arm1 "I almost spit out my water."

    a frowntalk eye2 "Well... It's a family tradition. And, I wanted to."
    a talk eye1 "What do you know about vampires, Cecil?"

    show ambrose frown
    show nemo up

    c frowntalk arm1 "...They need blood to live. They don't like harsh things."

    show cecil frown

    a frowntalk "Mhm, that's true, but it doesn't really paint the full picture of a vampire in your head, does it?"
    a eye3 "Vampires are just an offshoot of humans. We're still humans, though some would rather call us enhanced humans."
    a eye1 "Our senses are heightened, so we don't like harsh things like lots of sunlight or strong smells. That's why I carry a parasol—being in the sun too long gives me headaches."
    a "We still need food and water, but we also need blood at least once a week. In exchange for needing blood—for needing a part of a \"regular\" human's life—we live longer than other humans."
    a eye3 talk "It's hard to say exactly how long, though, but I'll most likely live twice as long as Nemo here."

    show ambrose smile

    nn frown down eye2 arm2 "Just had to word it like that to spite me, didn't ya?"

    a talk eye1 "Of course, I'm still considered a new vampire!"
    a frowntalk eye2 "I only became a vampire about, oh, 3 or so years ago? So I'm about a year older than Nemo."
    a talk eye1 "But don't worry, I always have a few flasks of blood handy."

    show ambrose smile

    c frowntalk "Then what about last night?"

    show cecil frown
    show ambrose eye4 frown

    nn frown eye4 surprise "Lord, this child is even denser than I thought!"

    n frowntalk down "Forget about what adults do!"

    nn frown eye5 "I cannot get drunk on the couch again when we have company over..."

    a eye5 talk "...We can talk more later tonight when I'm done with work. Farewell!"

    show ambrose frown


    hide ambrose with softeaseout

    nn frown "That's right, run away and leave me with him..."

    n frowntalk eye3 "Sigh... You ready to walk around town some more?"

    show nemo frown eye1
    show cecil:
        easein 0.4 yoffset 250
        easein 0.25 yoffset 220
        easein 0.4 yoffset 240
        easein 0.4 yoffset 220

    c talk up "Yes!"

    show cecil smile

    stop music fadeout 4







label brokeandunloved:


    $ save_name = "The Broke & The Unloved"
    $ chapter_num = "Thirteen"

    call chapter from _call_chapter_12

    $ nemopov = False
    $ cecilpov = True

    scene bg college1:
        zoom 0.6
        yalign 0.65
        xalign 0.5
    show cecil up frown arm2 at side
    with fade

    play music "audio/La Citadelle.mp3" fadein 2
    queue music "audio/La Citadelle.mp3"

    cn "Wow... I knew Lauremburg had to be amazing, but I wasn't expecting all this!"
    cn smirk "The university is beautiful. Every part of it feels like a piece of history, carefully maintained. But the rest of town feels so cherished and cared for."
    cn arm1 "It's not just a tourist destination. It's a place the people here enjoy."
    cn "I can understand a little now why Mr. Ambrose likes it here so much and why Nemo calls it his home."
    cn "Mr. Ambrose reminds me of the campus—carefully composed but not as intimidating as he looks."
    cn neutral frown "He seems really nice... but he's a vampire!"
    cn surprise "Nemo still never told me why he's helping him. Is he giving him blood in exchange for money?"
    cn down arm3 "No, that can't be it—Nemo's as broke as they get."

    show nemo up frown arm2 at center:
        zoom 1.1
    with dissolve

    c frowntalk up "I think you're getting scammed by that guy."

    show cecil frown

    n surprise talk "How so?"

    show nemo smile

    c frowntalk arm2 "You're giving him blood and you're still broke!"

    show cecil frown arm1

    n eye3 talk arm1 up "Hahah!"
    n eye1 surprise grin "You know, you're far more sheltered than I ever thought you were."

    show nemo smile up

    c frowntalk surprise arm3 "What d'you mean?"

    show cecil frown

    n grin surprise "Tell me, have you ever seen your parents kiss?"

    show nemo smile at shakeonce
    show bg college1 at shakeonce

    c frowntalk down arm2 eye4 "Wh-What?! Of course not, that's indecent!"

    show cecil frown arm3

    n talk "Ever taken a fancy to someone?"

    show nemo smile

    c frowntalk "I like Lucie!"

    show cecil frown

    n up talk "I mean, like, {i}really{/i} liked someone. Love someone."

    show nemo smile

    cn eye5 "Now he's just being vague to tease me."

    c frowntalk unsure "I-I... I like Lucie..."

    show cecil frown

    n frowntalk surprise arm2 "Oh boy..."

    show nemo frown eye2

    nar "He rubs his neck and shifts his weight uncomfortably."

    n frowntalk eye1 arm1 up "Look... When you really like someone, you love them."
    n frowntalk "They're never far from your thoughts—they might not always be on your mind, but they always come back."
    n frowntalk "You might be walking in a market weeks away by train and see a trinket that reminds you of them and you smile."
    n frowntalk down eye3 "Even when they'd dam—darn—frustrating, you can't find it in yourself to hate them. You work things out together."
    n frowntalk up eye1 "That's how it is for Ambrose and I."

    show nemo smile

    c frowntalk up eye1 arm2 "Always thinking about someone... That's how I am with Lucie!"

    show cecil frown

    n talk eye3 "Uh-huh, uh-huh..."
    n eye1 "But, I think most of all..."
    n "They're home."

    show nemo smile

    c frowntalk down eye2 arm3 "Now you're talking gibberish."

    show cecil frown

    n talk eye3 arm2 "Home isn't a building, idiot."

    show nemo smile eye1 arm1

    cn unsure eye1 "Home isn't... a building? What does that mean? Of course home is a building!"

    nar "Nemo ruffles my hair, making it messier than when I woke up this morning."

    show nemo smile at shakeonce
    show bg college1 at shakeonce

    c frowntalk eye4 "H-Hey!"

    show cecil frown

    n talk "Wait a few more years—maybe by then you can whole-heartedly say you love someone."
    n "I hope that happens for you."

    stop music fadeout 4

    show nemo smile


    scene bg city4:
        zoom 0.5
        yalign 0.65
        xalign 0.5
    with slowfade

    play music "audio/Isolation Waltz.mp3" fadein 3
    queue music "audio/Isolation Waltz.mp3"

    nar "It's one alleyway after another—one street melding into another, all leading to nothing."
    nar "Nemo leads the way. It's not clear if he even knows where he's heading."
    nar "We pass hundreds of people, each set on their own paths."


    show cecil up frown arm1 at side
    show nemo down frown arm2 at center:
        zoom 1.1
    with dissolve

    n "...!"

    c frowntalk arm3 "What's wrong, mister?"

    show cecil frown

    n frowntalk eye2 "...Nothin—"

    show nemo frown

    show bg city4 at shakeonce
    show nemo up eye1 at shakeonce

    c frowntalk arm1 "W-Wait!"

    show cecil frown

    cn "Nemo's sudden stop in the road almost makes me miss the person standing outside a shop several feet from us."

    show leland up frown eye2 hat behind nemo at left:
        zoom 0.28
        xalign 0.13
        yalign 0.8
        blur 2
    with dissolve

    cn "It's Lucie's uncle."
    cn "He's standing outside a bakery and hasn't noticed us yet."

    c frowntalk arm2 up "Mr. Leland!"

    show cecil frown arm1

    n frowntalk down arm1 eye1 "Hey, hold on—"

    show nemo frown eye2

    c frowntalk arm2 "Mr. Leland! It's me, Cecil!"

    cn smile "Yes! He noticed me!"


    show nemo down frown arm2 eye2 behind leland:
        ease 1.0 zoom 0.85 yalign 0.05 xalign 1.3

    pause(0.7)

    show leland up frown eye1 at left:
        zoom 1.15
        xalign 0.0
        yalign 0.15
        blur 0
    with dissolve

    nar "The tall, orderly gentleman strides our way and tips his hat. Standing next to Nemo, the pair look like complete opposites."

    cn frown arm1 "Just focus on the bridge of his nose. Don't stare at the scar, Annie said that's the utmost of rudeness!"
    cn eye2 "Of course, it'd be easier if he wasn't so tall..."

    show cecil eye1

    leland frowntalk "...Well, if this isn't interesting."
    leland frowntalk "How do you do, Cecil—"

    show leland frown at shakeonce
    show nemo at shakeonce
    show bg city4 at shakeonce

    c frowntalk up arm2 "D-Do you know where Lucie is?!"

    show cecil frown

    leland down "Hmm...?"
    leland frowntalk "You didn't leave with her?"

    show leland frown up

    c frowntalk down eye2 arm3 "No, I came here to find her after I heard she vanished."

    show cecil frown

    leland frowntalk eye2 "That's rather troublesome... Here I was assuming she hadn't left on her own."
    show cecil neutral eye1
    leland "I didn't find a record of her at any of the local inns, either..."
    show nemo grimace
    leland eye3 down "I do pray she hasn't been {i}kidnapped{/i}."

    show leland frown eye1
    show cecil up shock arm1

    nar "I let out a gasp."

    show nemo at shakeonce
    show leland at shakeonce
    show bg city4 at shakeonce

    c frowntalk arm2 down "I won't let that happen!"
    c frowntalk "If I find her first, I'll come for you!"

    show cecil frown

    show nemo frown eye2:
        ease 1.0 zoom 0.9 yalign 0.05 xalign 0.65
    show leland at left:
        ease 1.1 zoom 1.2 xalign -5.0 yalign 0.15


    nar "I tug on Nemo's sleeve."

    show nemo at curtsy
    show leland at curtsy
    show bg city4 at curtsy

    c frowntalk arm2 down "We need to keep looking for her!"

    show cecil frown arm1

    n frowntalk "...Ay."

    show nemo frown

    cn arm3 eye2 surprise "Why does Nemo look so irked? Does he get this way around every proper gentleman?"

    show cecil eye1 up

    show nemo down frown arm2 eye2 behind leland:
        ease 1.0 yalign 0.05 xalign 1.3

    show leland up frown eye1 at left:
        ease 1.0 zoom 1.15 xalign 0.0 yalign 0.15

    pause(0.7)

    leland frowntalk eye3 up "Then I must bid you a good day, Cecil... Nemo. I must continue looking for her as well."
    leland eye1 "Please telegraph this inn if you happen upon her."

    show leland frown eye1

    nar "He hands me a small slip of paper with fancy writing on it. I can't read it well."


    hide leland with Dissolve(1.0)

    pause(0.2)

    show nemo:
        ease 1.2 zoom 1.0 xalign 0.5 yalign 0.1

    pause(1.0)

    n frowntalk "...C'mon, let's get going. There's still some areas we haven't looked at."

    show nemo frown

    hide nemo with softeaseout

    show bg city4 at shakeonce

    c frowntalk "W-Wait!"

    show cecil frown


    scene bg city4:
        zoom 0.5
        yalign 0.65
        xalign 0.35
    show cecil down frown arm3 at side
    with sidefade

    cn "I can barely keep up with his pace. His stride is already bigger than mine, but something seems to have sparked his determination."

    show bg city4 at shakeonce

    c frowntalk arm2 "Wait, mister!"

    show cecil frown arm3 unsure

    show nemo down frown arm1 at center:
        zoom 1.1
    with dissolve

    n frowntalk "What?"

    show nemo frown

    c frowntalk arm1 "L-Let... Let me catch my breath..."

    cn frown eye3 "Phew..."

    c frowntalk eye1 neutral "Why... Why are you so determined now?"

    show cecil frown

    n frowntalk eye2 arm2 "...I remembered there's people waiting for you to return home."
    n arm1 "If her uncle has already come out this way, then what about your family? Won't they be worried sick by now?"

    show nemo frown eye1

    c frowntalk eye2 arm3 unsure "Yes..."

    show cecil frown

    n frowntalk "Don't forget about them while you're searching for her."

    show nemo frown

    scene bg garden:
        zoom 0.7
        yalign 0.6
        xalign 0.5
    with sidefade

    nar "The two of us traverse back alley ways and regular streets for what feels like hours until we take a break."
    nar "Nemo sighs and takes a long look around us."

    show nemo up frown eye3 arm2 at center
    show cecil up frown arm3 at side
    with dissolve

    n frowntalk "C'mon, we've done enough walking today."

    show nemo frown

    c frowntalk "We have?"

    show cecil frown

    n frowntalk "I've got a better idea for finding her... but first, let's head back."

    show nemo frown

    stop music fadeout 6


    scene bg office2:
        zoom 0.5
        xalign 0.5
        yalign 0.65
    with fadee

    cn "If Mr. Leland came all the way out here, then we must have come to the same conclusion about Lucie."
    cn "She really did run off chasing after vampires attacking people."
    cn "Gah, I should have asked him why, though!"
    cn "Maybe if I could figure out why she'd be dead set on it—"

    play music "audio/a432.mp3" fadein 2
    queue music "audio/a432.mp3"

    show ambrose pink up smile at right:
        xalign 1.7
    show nemo pink up frown nocap at left:
        xalign -0.5
    show cecil pink neutral frown eye2 arm3 at side
    with dissolve

    a frowntalk "Potatoes, Cecil?"

    show ambrose smile
    show cecil up eye1

    nar "Mr. Ambrose passes me a bowl of smashed potatoes."

    c frowntalk arm1 "O-Oh, thank you."

    show cecil frown

    a talk "So, where are you from Cecil? All I've heard is \"up north\"."

    show ambrose smile

    c talk arm2 "I'm from Parehaven! It's really hilly where my house is and there's a lot of other mansions scattered around it like Lucie's."
    c frowntalk arm1 "There's trees and vineyards as far as you can see..."
    c talk arm2 "But I've seen so many nice places and people while coming here! There were some buildings that were taller than any I thought were possible! And we sailed on such a big river!"

    show cecil smile arm1

    a frowntalk "Do you leave home much, Cecil?"

    show ambrose frown
    show nemo at bounce2

    n talk eye3 arm2 "Hah! A house cat gets out more than him."

    show nemo smile arm1 surprise eye1

    c frowntalk down eye5 arm3 "I have to spend a lot of time at home... I'm homeschooled and I have to take my pills once every week or two."

    show cecil frown
    show ambrose unsure

    n frowntalk "Pills? You're on medicine and you ran off from home?"

    show nemo frown at shakeonce
    show ambrose at shakeonce
    show bg office2 at shakeonce

    c frowntalk unsure arm2 eye1 "I-It's not like that! I took my dose before leaving! I feel fine!"

    show cecil frown

    a frowntalk "If you start feeling sick, we can take you to one of the doctors here. We have a fine medical staff."

    show ambrose frown

    c shock eye2 arm1 "Ah, I think the pills are specially made by our doctor..."

    show cecil frown

    n frowntalk "Specially made...?"

    show nemo frown

    c frowntalk eye1 arm2 "I-I'll be fine! I'm fine!"

    show cecil frown arm1

    n arm2 eye2 "..."

    show nemo frown

    c talk neutral arm3 "I once went 3 weeks without my pills before Annie made me take them! I was hiding out at a friend's house while she was looking for me."

    show cecil smile

    a frowntalk up "So you have other friends? Surely they're worried about Lucie and yourself too?"

    show ambrose frown

    c frowntalk eye2 arm2 "They are! ...Probably."
    c frowntalk eye1 arm1 "We're friends with other kids in town, but Lucie plays with me more often. She's an only child too."

    show cecil frown

    a frowntalk "Are your parents home often?"

    show ambrose frown

    c frowntalk surprise arm3 "Of course not! They have work to do."

    show cecil frown

    a frowntalk unsure eye2 "...Of course."

    show ambrose frown
    show cecil up

    nar "I glance over at Nemo, who's poking his string beans with his head leaning against his fist."

    c frowntalk "Your vegetables are going to get cold if you keep staring at 'em, mister."

    show cecil frown
    show ambrose up

    n frowntalk eye3 arm1 up "You're one to talk. Look at all the carrots you have left!"

    show nemo frown eye1

    c frowntalk down "Carrots are weird! Vegetables shouldn't be so bright and crunchy, they should be green!"

    show cecil frown

    n frowntalk eye3 down "Sigh..."

    show ambrose eye1

    n frowntalk eye1 up "You about ready to head out?"

    show nemo frown

    c frowntalk up arm1 "Head out? Where are we going?"

    show cecil frown
    show ambrose eye3 smile

    n grin "To stake out a place and wait for the attacker, of course."

    show nemo at shakeonce
    show ambrose at shakeonce
    show bg office2 at shakeonce

    c shock arm2 "Really?! I'm ready whenever!"

    show cecil frown

    n talk "Good. I think I have just the place in mind..."

    show nemo smile

    stop music fadeout 3










    $ save_name = "Interlopers"
    $ chapter_num = "Fourteen"

    call chapter from _call_chapter_13

    $ nemopov = True
    $ cecilpov = False

    scene bg cathedralinside:
        zoom 0.5
        yalign 0.65
        xalign 0.5
    show nemo cathedral down frown arm2 eye3 at side
    with fadee





    nn frown "Such an empty cathedral... It'll be perfect for tonight."
    nn frown eye2 "The less people out, the better. ...Though maybe a scapegoat would be nice."


    show bg cathedralinside:
        zoom 0.7
        yalign 0.6
    with dissolve
    show bg cathedralinside:
        easein 5.0 xalign 0.0
        easein 5.0 xalign 1.0
        repeat

    nn frown eye3 "Multiple attacks where no one got a good enough look at the attacker... no deaths... are there multiple attackers?"
    nn frown "If there's multiple attackers, then that can make things harder in identifying them. It'd also answer how there's been so many, but it's not answering {i}why{/i}."
    nn frown eye2 "Maybe it's a group of people...? But it keeps going back to \"why\" multiple people would be attacking strangers."
    nn frown "None of the victims had anything in common other than being locals and out at night."
    nn frown eye3 arm1 "No, I should be looking at the original motive, what caused this."
    nn frown "The first attack was on a student walking home from a night class. Was there something about her that set the vampire off?"
    nn frown eye2 "Was the vampire running low on blood and out of options? Or was it more methodical?"

    show bg cathedralinside:
        zoom 0.5
        yalign 0.65
        xalign 0.5
    show cecil cathedral up frown at center:
        yoffset 100
    with dissolve

    c frowntalk arm3 "I just saw something move in the courtyard over there!"

    show cecil frown

    n frowntalk eye1 "Let's head out, then."

    show nemo frown


    scene bg city2:
        zoom 0.65
        yalign 0.1 xalign 0.5
        ease 3.0 yalign 0.8
    with fade

    pause(1.0)

    $ nemopov = False

    nn frown "The courtyard that was hosting a party just yesterday is now empty and bare... except for one couple."

    $ nemopov = True

    show cecil cathedral unsure frown at center:
        yoffset 120
    show nemo cathedral surprise frown at side
    with dissolve

    n frowntalk "Ahoy."

    show nemo frown

    show cecil:
        xalign 1.4
    with easeinright

    show npcfem2 at cathedralcolor:
        zoom 0.7
        xalign 0.0
        yalign 0.6
    show npcmasc4 at cathedralcolor:
        zoom 0.7
        xalign 0.5
        yalign 0.7
    with Dissolve(0.8)

    "Gentleman" "Good evening!"

    nn frown "Are they from out of town?"

    n frowntalk "The university is rather empty tonight. What brings you lot out?"

    show nemo frown
    show npcfem2 at cathedralcolor:
        easein 0.12 xoffset 15
        easein 0.12 xoffset -15
        easein 0.12 xoffset 15
        easein 0.12 xoffset -15
        easein 0.12 xoffset 0

    "Lady" "My! Is that any way to address a lady?"

    "Gentleman" "Perhaps the kids should return home and think about their manners instead of prowling around the city at night."

    nn frown "He has an interesting choice of words."

    show cecil at shakeslow

    c frowntalk "Let's go somewhere else..."

    show cecil frown

    hide npcfem2
    hide npcmasc4
    with dissolve

    n "..."

    show nemo frown

    nn frown "Cecil is too trusting. No, maybe it's not that he's too trusting—he just doesn't understand a lot of life's nuances yet."
    nn frown "He's lived relatively alone his whole life with little to see of the outside world. Yes, that's why..."

    play music "audio/Nightmare.mp3" fadein 1
    queue music "audio/Nightmare.mp3"


    scene black with sideswipe

    hide nemo
    hide cecil

    $ nemopov = False

    pause(0.1)

    show gunshot
    show gunshotsparkles

    play sound "audio/gunshot1.mp3"

    nn "That's why he doesn't follow his instincts properly."

    "Lady" "AGH!"

    show nemogun1:
        yalign 0.4
    hide black
    with sideswipe

    nar "The woman falls to the ground after her failed attempt to lunge at us."
    nar "Her company, however, tries to make up for it."


    play sound "audio/gunshot2.mp3"

    nn "I don't know if these are the vampires we're looking for, but either way they're looking for prey and need to be stopped-!"

    hide nemogun1
    show black
    hide gunshot
    hide gunshotsparkles
    with sideswipe

    play sound "audio/gunshot1.mp3"
    queue sound "audio/gunshot2.mp3"

    show gunshot as gs2:
        yoffset 300
        xoffset -100
    show gunshotsparkles as gss2:
        yoffset 300
        xoffset -100

    n "Cecil, get back!"

    scene bg city2:
        zoom 0.65 xalign 0.5 yalign 0.8
    with sideswipe

    $ nemopov = True

    show cecil cathedral unsure frown at center:
        yoffset 120
        ease 0.2 xalign 0.8 yoffset 160 zoom 0.85
    show nemo cathedral surprise frown at side
    with hpunch

    nar "The man makes a lunge for my right arm as I push Cecil back."

    n down grimace "—!"

    show nemo frown


    play sound "audio/gunshot1.mp3"

    nar "I only barely manage to kick him away. Barely."
    show npcfem2 behind cecil at cathedralcolor:
        zoom 0.7 xalign -0.5 yalign 0.6
        ease 0.4 xalign 0.6
        ease 0.2 alpha 0.0
    show cecil:
        linear 0.4
        ease 0.2 alpha 0.0
    nar "The woman gets back on her feet and makes a dash for Cecil."

    n frowntalk "Dammit—!"

    show nemo frown

    $ nemopov = False

    hide nemo
    hide cecil
    scene black

    stop music fadeout 0.5

    na "{color=#ff2e2e}Blood Art <Impalement>.{/color}"


    play sound "<from 1>audio/stab.mp3"
    play foley "audio/stab.mp3"
    show impalement

    nar "A hail of red spikes fall onto the woman from the sky."
    nar "They glisten beautifully in the moonlight—beautifully but deadly."

    stop foley 
    stop sound

    scene bg city2:
        zoom 0.65 xalign 0.5 yalign 0.8
    with sideswipe

    $ nemopov = True

    play music "audio/Asking Questions.mp3" fadein 2
    queue music "audio/Asking Questions.mp3"

    show cecil cathedral unsure frown eye2 at center:
        yoffset 100 zoom 1.4
    show nemo cathedral surprise frown at side
    with hpunch

    n frowntalk "Cecil, are you okay?!"

    show nemo frown

    c "..."

    show cecil frown

    nar "The spikes skewer the woman to the ground."
    nar "Most appear to have hit her dress, but a few are definitely burrowed into her skin."
    nar "Cecil looks away from the woman and is now transfixed on something else."

    show bg city2:
        ease 5 yalign 0.0
    show cecil:
        ease 4.5 yalign -2.0

    nar "I look up, meeting Cecil's gaze."
    scene lucie cg 1 night:
        zoom 1.2
        yalign 0.0
        xalign 1.0
    with dissolve
    $ nemopov = False
    nar "On such a bright night, vampires looking for easy prey weren't the only ones out lurking."
    nar "Against that bright moon..."
    show lucie cg 1-1:
        zoom 1.2 yalign 0.0 xalign 1.0
    with dissolve
    show lucie cg 1-1:
        easein 3.0 xalign 0.7

    stop music fadeout 4

    nar "...Was Lucie."









    $ save_name = "The Huntress"
    $ chapter_num = "Fifteen"

    call chapter from _call_chapter_14

    $ nemopov = False
    $ cecilpov = True









    scene lucie cg 1-1:
        zoom 0.8
        yalign 0.0 xalign 0.5
    show cecil seance up frown arm1 at side
    with fade

    play music "audio/Fairy Dance.mp3" fadein 2
    queue music "audio/Fairy Dance.mp3"

    $ achievement.grant("lucie")
    init:
        $ achievement.register("lucie")
        $ achievement.sync()
    $ achievement.sync()


    show lucie cg 1-1 at shakeonce

    c shock "Lucie!"

    cn smile arm2 "Lucie's here! And she's okay!"
    cn "I don't know what those red spikes were but Lucie's safe!"

    c talk arm1 "Lucie, you're okay!"

    show cecil smile

    l "Of course I am! Why were you about to let yourself get attacked?"
    l "...!"


    show lucie cg 1-2:
        zoom 0.8
        yalign 0.0 xalign 0.5
    with Dissolve(0.2)

    l "Why are {i}you{/i} here?!"

    cn up frown arm1 "Huh? Who is she talking to?"

    show nemocutin night 1:
        yalign 0.0
    with softeaseleft

    nar "Nemo shrugs, though his face is darkened under the brim of his cap."

    show nemocutin 2

    n "You're the one at my home. I should be the one asking why you're here."
    n "If you wanted to come all the way out here just to see me, you should have telegraphed first!"

    show nemocutin 3

    l "Why would I ever want to see you?!"

    cn surprise "Huh? Huh?"

    show nemocutin at shakeonce
    show lucie cg 1-2 at shakeonce

    cn "They know each other?!"

    show nemocutin 4

    n "You shouldn't be out alone searching for criminals."

    show nemocutin 3

    l "Stay out of this and out of my way, Robin!"

    show nemocutin 5

    n "..."

    cn unsure "Robin...?"

    hide nemocutin with dissolve

    show lucie cg 1 night:
        zoom 0.8
        yalign 0.0 xalign 0.5
    with Dissolve(1.2)

    nar "Lucie turns to leave."

    c frowntalk up arm2 "W-Wait, Lucie!"

    show cecil frown

    show lucie cg 1-1:
        zoom 0.8
        yalign 0.0 xalign 0.5
    with Dissolve(1.2)

    l "..."
    l "Cecil, why are you here?"

    c talk arm1 "Isn't it obvious? I'm here to help my best friend!"

    show cecil smile

    show lucie cg 1-3:
        zoom 0.8
        yalign 0.0 xalign 0.5
    with dissolve

    l "Wh-Wh...!"
    show lucie cg 1-3 at shakeonce
    l "I-I don't need any help!"
    l "These vampires are dangerous. Don't assume you'll be fine on your own."

    c frowntalk "Then let me come with you!"

    show cecil frown unsure

    l "G-Go home! I don't need help!"

    stop music fadeout 3

    show lucie cg 1 night with dissolve



    scene bg city2:
        zoom 0.65
        yalign 0.1 xalign 0.5
        linear 1.0
        ease 3.0 yalign 0.8
    with fadee

    pause(0.2)

    show nemo cathedral down frown eye2 arm2 at center
    show cecil cathedral unsure frown at side
    show guard behind nemo:
        zoom 0.4
        xalign 0.0
        yalign 1.0
    show guard as guard3 behind nemo:
        zoom 0.4
        xalign 1.0
        yalign 1.0
    with dissolve

    n "..."

    nar "A group of guards are already cuffing the couple that Nemo stopped."

    n frowntalk "...They're most likely not the attacker we're looking for."

    show nemo frown

    c frowntalk "What makes you say that?"

    show cecil frown

    n frowntalk "They were too conspicuous. None of the victims remember seeing a couple out, they were all alone."
    n frowntalk "These guys are probably just copycats that wanted some free blood."

    show nemo frown

    c "..."

    play music "audio/Isolation Waltz.mp3" fadein 5
    queue music "audio/Isolation Waltz.mp3"

    cn "How does he know Lucie? Why was she so mad to see him?"
    cn eye2 "Lucie can be, uh, what did Annie call it? \"Temperamental\"? \"Feisty\"? \"Insolent\"?"
    cn "But... I've never seen her so angry."

    n frowntalk "Let's head back for now. All this commotion will probably discourage any more attacks tonight."

    show nemo frown at curtsy
    show bg city2 at curtsy
    show guard at curtsy
    show guard as guard3 at curtsy
    show cecil eye1

    nar "I nod."

    cn "What did he do to make her so mad?"


    scene bg office2 night:
        zoom 0.55
        yalign 0.65
        xalign 0.5
    with slowfade

    play foley "audio/fireplace.mp3" fadein 1

    nar "The apartment is warm from the fireplace. Mr. Ambrose is reading by the fire with Leroy asleep on the rug."

    cn "I'm worn out, but I... I can't go to sleep just yet."

    show cecil pinknight frown unsure arm3 eye2 at side
    show nemo pinknight down frown arm2 eye2 nocap at left:
        xalign -0.6
    show ambrosen pinknight up frown at right:
        xalign 1.6
    with dissolve

    an frowntalk unsure "...How did it go?"

    show ambrosen frown

    n frowntalk "We found a couple loitering about looking for some fresh blood but not the actual culprits."
    n frowntalk "The coppers took 'em in for questioning but I doubt they'll find anything."

    show nemo frown

    an frowntalk up eye3 "Well, that's two less miscreants out there."
    an frowntalk unsure eye1 "...What's wrong, Cecil?"

    show ambrosen frown

    c "..."
    c frowntalk eye1 "Nemo, how do you know Lucie?"
    c frowntalk "And why was she so angry at you?"

    show cecil frown
    show ambrosen down eye2

    n up frown eye2 "..."
    n frowntalk eye1 arm1 "She's my little sister."

    show nemo frown at shake
    show ambrosen at shake
    show bg office2 night at shake

    c frowntalk "H-Huh?!"
    c frowntalk arm2 "But... But... Lucie's always said she's an only child! And you referred to your little sister in the past tense when you mentioned her before!"

    show cecil frown

    n frowntalk arm2 eye3 "Look at how she acts at seeing me. D'you think she considers herself my little sister anymore?"

    show nemo frown arm1

    c frowntalk arm3 "Why was she acting like that?"

    show cecil frown

    n frowntalk arm2 eye2 "...Don't worry about it."

    show nemo frown at shake
    show ambrosen at shake
    show bg office2 night at shake

    c frowntalk arm2 "I will worry about it! As her friend, I want to know!"

    show cecil frown arm3

    n frowntalk down eye1 arm1 "It's between the two of us, okay?"
    n frowntalk eye3 up "I'm going to help send you both home before either of you get hurt."

    show nemo frown eye1

    c "..."
    c frowntalk "Why won't you tell me?"

    show cecil frown

    n frowntalk eye2 "...If she's never mentioned me, then she wants to move on. Just leave it at that."

    show nemo frown

    cn eye2 "...What do I say to this?"
    cn "Lucie's never mentioned having siblings, but it's undeniable they know each other."
    cn "Why was she so mad at him, though? Why doesn't she still consider him her brother?"

    n frowntalk eye1 "Get some sleep, it's been a long day. We'll look for her and the attacker some more tomorrow."

    show nemo frown

    c "..."
    c frowntalk "...Okay."

    show cecil frown

    stop foley fadeout 2
    stop music fadeout 3


    scene bg cecilbedroom night:
        zoom 0.8
        yalign 0.7
    with slowfade


    play foley "audio/clock.mp3"

    cn "Nemo's a pickpocket. He said he works any kind of job he can get—he told me he was a deckhand as a kid."
    cn "I even overheard him getting into an argument with Mr. Ambrose earlier when he tried to give him some pocket change."
    cn "But Lucie's an aristocrat. Annie says she's \"old money\"."
    cn "I only remember seeing her around town the past couple of years, but her uncle has lived in that estate for decades."
    cn "I don't understand it."
    cn "I've accepted everything he's said up until this point. I've gone along with everything he's done so far—okay, most things."
    cn "Why is this the thing he keeps from me? What's so different now?"
    cn "It's family business. But I'm here for Lucie. If he did something to make her that mad..."
    cn "...Can I still trust him?"


    pause(1)

    cn "What were those weird red spikes tonight?"
    cn "They were so pretty against the moonlight... but they hurt that woman."
    cn "If Nemo could do something like that, he would've done it before. Unless that's just something else he's keeping from me."

    c "..."

    cn "I can't stay here."
    cn "I'm tired, but I just can't sleep with all of this."
    cn "I have to find someone who'll actually talk to me."

    stop foley fadeout 2








    $ save_name = "Carnage"
    $ chapter_num = "Sixteen"

    call chapter from _call_chapter_15



    $ nemopov = True
    $ cecilpov = False

    scene bg office2 night:
        zoom 0.5
        yalign 0.65
        xalign 0.5
    show nemo pinknight down frown arm2 eye3 nocap shirttie at side
    show ambrosen pinknight down frown at center:
        zoom 1.25
        xoffset 60
    with fade

    play foley "audio/fireplace.mp3" fadein 1

    play music "audio/Winter.mp3" fadein 4
    queue music "audio/Winter.mp3"

    n frowntalk "I'm going to need more than that."

    show nemo frown

    nar "Ambrose pours me some more bourbon. Beside us, the fire crackles on, its embers slowly losing strength."

    show nemo eye2

    nn frown "Lucie is here, throwing herself into danger like I was afraid of."
    nn frown "It looks like she's learned some attacks for self defense, but that won't be enough for every encounter."
    nn frown "She's taken to becoming a vampire well."
    nn frown eye3 "But, I... I still don't want to see her be a vampire forever."
    nn frown eye2 "Leland was surprised that she wasn't with Cecil, so he has no damn idea where she is either. That means she's probably either in a hotel somewhere on her own or slumming it."
    nn frown "Hotels would be suspicious of a child wanting a room alone, but some would probably turn a blind eye if she forked up enough money..."
    nn frown "I couldn't tell how dirty her clothes were, so I can't tell if she's been sleeping on the streets or not."
    nn frown eye3 "Man, all she'd have to do is ask for help..."

    show nemo eye1 up

    an frowntalk "Why didn't you tell Cecil more?"

    show ambrosen frown

    n frowntalk eye3 "I told him the truth. What more is there to tell?"

    show nemo frown eye2

    an frowntalk "About her anger towards you."

    show ambrosen frown

    n frowntalk arm1 "It's none of his business."

    show nemo frown eye3

    nar "I take a long drink."

    n frowntalk eye1 "...Besides, what can I say? We'd be here all night if I tried explaining everything. And even then he probably wouldn't believe it."
    n frowntalk "You saw how long it took just to convince him not every vampire will attack people."

    show nemo frown

    nn frown eye2 down "...Wait."
    nn frown "Why has he been so averse to vampires this entire time? Does he not know Lucie is a vampire?"
    nn frown "He looked so angry when I refused to tell him more about the two of us, but he doesn't even realize Lucie's keeping as much from him as I am."

    an frowntalk "Was Lucie hiding that she's a vampire from him?"

    show ambrosen frown

    n frowntalk up eye3 "That's what I'm thinking. The kid acted like he'd never seen a vampire before—I think he'd act a little differently knowing his best friend and her uncle are vampires."
    n frowntalk eye2 "If he wants to get mad at me, let him be. Lucie'll have some things to answer for on her own."
    n frowntalk eye3 "We'll catch the attacker, prove it's not the vampire that killed her parents, and send the kids back home—simple as that."
    n frowntalk eye2 down "...They shouldn't be exposed to that kind of bloodshed."

    show nemo frown
    show ambrosen eye2

    nar "Ambrose rubs his neck."

    nn frown "He knows. He knows that regardless how much time passes, I'll never forget that night. I'll never stop having nightmares about it."
    nn frown eye3 "He can't imagine what it was like to be there."
    nn frown eye2 "I dislike a lot of things about him."
    nn frown "I dislike how he tries to sneak money in my pockets before I wake up. I dislike how he nags me about staying home in the apartment longer and to stop going on travels."
    nn frown "The thing I hate, though, that I'll never be able to understand—"
    nn frown eye3 "—Is the fact that he's a vampire."

    an frowntalk eye1 "Why are you so confident the attacker on campus isn't the same one that killed her parents?"

    show ambrosen frown

    n eye2 "..."
    n frowntalk eye3 "If you were there, you'd understand."
    n frowntalk "This attacker just wants blood. Even the people left in critical condition weren't assaulted in a brutal sense, they were just roughed up for their blood."
    n frowntalk eye2 "That thing, that night."
    n frowntalk "It didn't care about blood."

    stop music fadeout 4

    n frowntalk "It just wanted carnage."

    show nemo frown

    stop foley fadeout 2









    $ save_name = "Loyalty"
    $ chapter_num = "Seventeen"

    call chapter from _call_chapter_16

    $ nemopov = False
    $ cecilpov = True

    scene bg city2:
        zoom 0.65
        yalign 0.1 xalign 0.5
        ease 3.0 yalign 0.8
    show cecil cathedral unsure frown at side
    with fade

    play music "audio/Asking Questions.mp3" fadein 2
    queue music "audio/Asking Questions.mp3"

    play foley "audio/crickets.mp3"

    pause(1.0)

    cn frown "It's so dark out here... Where is the university?"
    show bg city2 at shake
    cn frown "Mr. Ambrose's apartment is right beside campus! H-How did I get this turned around?!"
    cn frown eye2 "There's too many weird noises..."
    show bg city2 at shakeslow
    cn frown arm2 eye1 "B-But I won't turn back! I've come this far to find Lucie and now we're under the same moonlight! I'll find her and help her with whatever is ailing her!"

    show cop:
        xalign -0.4 zoom 0.7 alpha 0.0 yalign 0.2
        ease 1.3 xalign 0.5 zoom 0.7 alpha 1.0

    pause (0.2)

    Cop "Kid, are you lost?"

    show cop:
        xalign 0.5
        zoom 0.7
        alpha 1.0

    show cop at shake
    show bg city2 at shake

    c frowntalk arm1 "...!"

    show cecil frown

    cn frown "I almost scream. From a dark alleyway emerges a copper, horribly scaring me. I didn't even see him."

    c frowntalk eye2 "I-I..."

    show cecil frown

    Cop "It's too dangerous for a kid to be out and about right now! Haven't you heard of the vampire prowler?"

    c frowntalk "Y-Yes sir... But y'see, my friend..."
    show cop at shakeslow
    show bg city2 at shakeslow
    c frowntalk eye1 arm2 "My friend is out here too! A-And I have to find her!"
    c frowntalk "She's my age and she has really long blonde hair and she's wearing a really pretty pink and cream dress."

    show cecil frown
    Cop "Your friend is missing? You shouldn't be wandering around alone looking for her."
    Cop "How about this—why don't we head down to the station and see if anyone's reported seeing her?"

    stop music fadeout 6

    cn frown eye2 arm1 "...I don't know if this is the right thing to do."
    cn frown eye3 "If he figures out I'm a runaway, he'll ship me home. But going with him would probably be safer than walking around on my own."
    cn frown eye2 "Someone might have reported seeing her, too, so going to the police department might not be pointless."
    cn frown neutral "If he asks where I'm from, I'll give him Mr. Ambrose's address."

    c eye1 talk arm2 "Alright! Thank you for your help, mister."

    show cecil frown

    stop foley fadeout 3


    scene bg police:
        zoom 0.6 xalign 0.5 yalign 0.75
    show cecil police up frown at side
    with fadee

    play music "audio/Isolation Waltz.mp3" fadein 3
    queue music "audio/Isolation Waltz.mp3"

    show bg police:
        ease 1.9 zoom 0.8 yalign 0.7 xalign 0.0
        ease 2.3 xalign 1.0
        ease 1.4 xalign 0.5 zoom 0.65

    cn frown "This place... it's big!"
    cn frown "I didn't know what to expect when he said police department, but it feels like their entire city government is here."

    nar "Even though it's got to be very early in the morning, the place is bustling. Several coppers and some guards from campus pass us by as we walk through the lobby."

    cn frown "Is it always like this? Or is it especially busy because of the attacks?"

    show cop at center:
        zoom 0.65
        yalign 0.2
    with dissolve

    Cop "Stay right here, I'm going to grab a lad who might know more—{w=0.5}wait, what was your name again?"

    c frowntalk arm2 "C-Cecil!"

    show cecil frown unsure arm3 eye5

    nar "I stutter my name out, tempted to give a fake name instead but my own tongue betrays me."
    nar "A week ago I would have been appalled at the idea of lying to a copper to his face."
    show cecil eye2
    hide cop
    with dissolve
    nar "The man steps away quickly, briefly saying things to various other workers as he passes them."

    cn frown eye1 "He's going to get a list of reports, right? Not a telegraph from home saying to turn in anyone who looks like me, right?"
    cn frown eye2 "If he's not back in 5 minutes, I'm leaving."

    na "C...Cecil!"

    c eye1 arm1 up "...!"


    show annie police at center:
        zoom 0.9
    show cop behind annie:
        zoom 0.55
        xalign 0.0
        yalign 0.25
    with dissolve

    show annie at shakeslow

    annie talk "Cecil, you're here! I can't believe I finally found you!"

    show annie frown at shake
    show cop at shake
    show bg police at shake

    c frowntalk "I-I can't believe you found me either!"

    cn frown "H-How did Annie find me?!"

    annie talk "Thank you so much for your help, officer."

    show annie frown


    show cop:
        ease 2.0 xalign 1.1 alpha 0.0

    show cecil neutral eye2

    annie down frowntalk "I've been worried to death that something had happened to you!"
    hide cop
    show annie at shakeonce
    annie frowntalk "Don't run off again like that! Do you know how much trouble you've put your parents through? Put me through?"
    annie frowntalk "Oh, how dangerous a stunt this was! You could have been killed, or kidnapped, or hurt, or killed—and all for what? A little attention?"
    annie frowntalk "You had me positively worried sick! I didn't think I'd make it out of bed every morning until Mr. Leland said he was taking a ferry to Lauremburg to search for little Lucie!"
    annie frowntalk "I just knew you had to be here with her, and right I was!"

    show annie frown

    cn unsure smile "Annie can really talk the ear off a donkey, can't she...?"

    c talk eye3 "I-I'm glad to see you too, Annie."
    c frowntalk eye1 neutral "I didn't run away with Lucie though, I came here to find her. She ran away on her own."

    show cecil frown eye2
    show annie at shake

    annie frowntalk "If she ran off a cliff, would you follow? You would just to see what's so fascinating about the other side, wouldn't you?"
    annie frowntalk "And you even left your medicine behind!"

    show annie frown at shake
    show bg police at shake

    c frowntalk down eye1 "I-I'm perfectly fine without it!"

    show cecil frown
    show annie up

    nar "She places her hand on my arm."

    show cecil up

    annie talk "Don't worry. It's alright now."
    stop music fadeout 2
    annie talk "You're safe now and we can go home."
    annie talk "Your father will be waiting for you."

    show annie smile

    c scared "...!"


    play music "audio/Horroriffic.mp3" fadein 2
    queue music "audio/Horroriffic.mp3"

    show annie at shakeslow

    annie talk "It'll be alright, you're safe with me now! Your parents will be so happy to see you home safely!"
    annie talk "Let's head back home."

    show annie smile

    c frowntalk eye7 "H-Home..."

    cn frown down eye3 "No!"


    show annie frown at shake:
        zoom 0.65
    with hpunch

    c frowntalk "I don't want to go home!"

    show cecil frown

    annie frowntalk "Cecil!"

    show annie frown



    scene bg city2:
        zoom 0.65
        yalign 0.8 xalign 0.5
    show cecil cathedral scared frown eye3 at side
    with sideswipe

    cn frown "I don't want to go home!"
    cn frown "I don't want to take any more pills!"


    scene bg city2:
        zoom 0.75
        yalign 0.8 xalign 0.55
    show cecil cathedral scared frown at side
    with sideswipe

    cn frown "I don't want to see them again!"
    cn frown "I don't care where I'm going—"
    cn frown eye3 "—Anywhere is better than there!"

    show nemo cathedral up frown at center:
        zoom 0.75
    with dissolve

    n "...!"
    n frowntalk "Cecil—!"

    show nemo frown


    show nemo cathedral surprise frown at center:
        ease 0.5 zoom 1.3
    with hpunch

    n frowntalk "Why did you leave?"
    n frown "..."
    n frowntalk up "It's alright now."
    n frowntalk "It'll be alright..."

    show nemo frown

    scene bg city2:
        zoom 0.65
        yalign 0.8 xalign 0.5
    with dissolve

    cn frown "Yes..."
    show black with dissolve
    cn frown "Anywhere but there."

    stop music fadeout 3









    $ save_name = "The Watcher"
    $ chapter_num = "Eighteen"

    call chapter from _call_chapter_17

    $ nemopov = True
    $ cecilpov = False

    scene bg office2:
        zoom 0.4
        yalign 0.7
        xalign 0.5
    show nemo pink down frown arm2 eye3 nocap shirttie at side
    with fade



    n frown "..."



    nn eye1 "He's still out cold. I wasn't expecting to carry him back here, but at least he doesn't look hurt..."
    nn eye2 "I couldn't find any bite marks on his exposed skin last night. Something rattled him terribly, though."

    show nemo eye1 up arm1
    show ambrosen pink down frown at center:
        zoom 0.85
    with dissolve

    play music "audio/a432.mp3" fadein 2
    queue music "audio/a432.mp3"

    nar "Ambrose eyes the door while sipping his coffee."

    an frowntalk "I'll keep an eye on him."
    an frowntalk "Are you going to go after Lucie?"

    show ambrosen frown

    n frowntalk "Looks like I have to."

    show nemo frown

    nn down eye2 "I doubt I can convince her to come here, but I should still try to find her."
    nn eye3 "She's alone out there and this kid won't stay put knowing she's so close. It's a terrible combination."

    show nemo up eye2
    show ambrosen pink up frown at center:
        ease 1.5 zoom 1.25 xoffset 60

    pause(1.0)

    nar "He caresses my cheek with his hand."

    an talk "It'll be alright."
    an "You'll find Lucie, both of them will be reunited, and we'll have a big supper tonight."

    show ambrosen smile
    show nemo eye3

    nar "I nod, but I'm unable to meet his optimistic eyes."

    stop music fadeout 2


    scene bg college1:
        zoom 0.7
        yalign 0.8
        xalign 0.5
    show nemo up frown at side
    with fadee

    play music "audio/Winter.mp3" fadein 2
    queue music "audio/Winter.mp3"

    nn "Scott wasn't at his office yesterday, so I'd better stop by today to check on him... He's not slacking off, is he?"
    nn "I know research is important to him, but sometimes he just takes it too far. His physical health slips way too often."

    scene bg hallway1:
        zoom 0.8
        xalign 0.5
        yalign 0.65
    show nemo pink up frown at side
    with fade

    n frowntalk "...Scott?"

    show nemo frown

    "..."

    s "...Come in."


    scene bg office1:
        zoom 0.5
        xalign 0.5
    show nemo pink up frown at side
    with sidefade

    show scott pink up frown at center:
        zoom 0.6
        yalign 0.5
    with dissolve

    nn "He certainly looks a lot better, although there's still bags under his eyes."

    n frowntalk "Feelin' alright, Scott?"

    show nemo frown

    s frowntalk "...I'm better."

    show scott frown

    n frowntalk surprise "What happened?"

    show nemo frown

    s frowntalk "Long nights."
    s frowntalk eye2 "...I might have tried a drink I concocted—"

    show scott frown

    n frowntalk unsure eye3 "Oh, come on..."

    show nemo frown
    show scott down at shake

    s frowntalk eye1 "It was just a little something! I'm feeling much better now."
    show nemo eye1
    s frowntalk up "My night classes are still canceled for the next week, but still."

    show scott frown
    show nemo arm2

    nar "All I can do is shake my head and sigh."

    nn "He's twice my age—maybe even more—but he has to be kept on such a tight leash."
    nn arm1 "After becoming a vampire as a young man, he's now regretted the decision as his wife has grown older than him and refuses to turn."
    nn up eye3 "Finding a cure is all he can hope for."
    nn "It's all we can hope for."


    scene bg city4:
        zoom 0.5
        yalign 0.6
        xalign 0.5
    show nemo up frown eye2 at side
    with sidefademedium

    nn "Cecil was so distressed last night. What did he run into?"
    nn eye3 "He was mumbling something about not wanting to go back... Go back the way he came?"
    nn eye2 surprise "Did he run into more vampires? Knowing his luck, he might have."
    nn "Maybe he ran into some scary coppers who gave him a hard time for being out so late."
    nn "Or... Did he run into someone from home?"
    nn "What happened to him?"


    show leland up frown hat at center
    with dissolve

    n down eye1 "..."

    leland frowntalk "Good morning."

    show leland frown

    n frowntalk "...Good morning."

    show nemo frown

    leland frowntalk "Where is she?"

    show leland frown at shake
    show bg city4 at shake

    n talk "Hah! You really think she'd come to me for help? The heat must really be getting to ya."
    n frowntalk "You still haven't found her, huh?"

    show nemo frown

    leland eye3 frowntalk "It seems she hasn't forgotten how to live on the streets."

    show leland frown

    nn surprise eye2 smile arm2 "I don't know if I should be proud or disappointed."
    n frowntalk eye1 down arm1 "It's a safe assumption, then... that she really is looking for her parent's killer."

    show nemo frown
    show leland eye2

    nar "Leland's good eye gazes to the far off horizon. The scar on his face from that night appears brighter than ever in the midday sun."

    leland frowntalk "...That's most likely the case, yes."

    show leland frown

    n frowntalk eye3 "Sigh..."
    n frowntalk eye2 "She's too stubborn to leave without an answer or until the attacker is caught."
    n frowntalk "If it's not the killer, then this cycle is just going to continue every time vampire attacks pop up."

    show nemo frown eye1

    leland frowntalk "Yes..."
    leland frown "..."
    show nemo up
    leland frowntalk down "I don't know how to give her that closure. The answers she seeks... they're beyond any of these attacks."
    leland frowntalk eye1 "...Unless you know something."

    show leland frown at shake
    show bg city4 at shake

    n grimace down "I've already told you lot everything!"
    n "Not a day goes by that I don't think about that infernal night..."
    n "That massacre... You were there, you should understand, but yet... but yet, you let her become a vampire...!"
    show leland frown at shake
    show bg city4 at shake
    n "If I knew who did it, we wouldn't be standing here!"

    nar "The people nearby start side-eyeing us."

    show nemo frown

    leland frowntalk eye2 "...I shouldn't have worded it that way. I apologize."

    show leland frown eye3

    n "..."

    leland frowntalk "She may put on a tough act, but she's still a child. She's my only family left."
    leland eye1 "I don't want her to get hurt."

    show leland frown

    nn eye2 "And yet you let her become a damned vampire."

    n frowntalk "...Ay."

    show nemo frown

    nn "The only thing I can do to help right now is to catch this attacker."

    show nemo eye1

    leland frowntalk "I'll leave you to find this attacker."

    show leland frown at curtsy
    pause(0.7)
    show leland hat:
        ease 1.6 xalign 1.4 alpha 0.0

    nar "He tips his hat and walks off."

    nn "Leland doesn't want her out here either, but..."
    nn eye2 "He doesn't want her alone out here, but he mainly doesn't want her looking for the killer to begin with."

    n "..."

    nn eye3 "Some things may be better left alone."

    stop music fadeout 3









    $ save_name = "Siblings"
    $ chapter_num = "Nineteen"

    call chapter from _call_chapter_18

    $ nemopov = False
    $ cecilpov = True

    scene bg cecilbedroom:
        zoom 0.86
        yalign 0.6
        xalign 0.5
    show cecil eye3 frown neutral at side
    with fade



    c "..."

    cn frown "Where am I...?"

    nar "Something warm pushes against my leg."
    show cecil eye1
    show bg cecilbedroom at curtsy
    nar "I sit up to see Leroy trying to get comfortable beside me."

    cn frown eye2 "Oh... I'm in Mr. Ambrose's apartment."

    c eye1 "..."

    play music "audio/Isolation Waltz.mp3" fadein 2
    queue music "audio/Isolation Waltz.mp3"

    show bg cecilbedroom at shake

    cn frown up "H-How did I get back here?!"
    cn frown unsure "What happened...?"
    cn frown "I was out looking for Lucie... then I ran into a copper... then..."
    cn frown "Annie!"
    cn frown "Annie was there! She's in Lauremburg looking for me!"
    cn frown scared "I... I can't let her take me home... not yet..."

    a "Are you up, Cecil?"

    c up "...!"


    scene bg office2:
        zoom 0.4
        yalign 0.7
        xalign 0.5
    with sidefade

    show cecil pink unsure eye2 arm3 frown at side
    show ambrose pink up smile at center:
        xalign 0.8
    with dissolve

    c frowntalk "I-I'm up..."

    cn frown arm1 "What time is it?"

    a talk "I hope you've had enough rest. You slept half the day away."

    show ambrose frown at shake
    show bg office2 at shake

    c frowntalk eye1 "H-Huh?!"

    show cecil frown

    nar "Sure enough, the sun is high in the sky, beating down on the streets below."

    c frowntalk "How did I get here?"

    show cecil frown

    a frowntalk eye3 "After you left, Nemo went looking for you and said he came across you in a panic. You were out cold by the time he brought you back here."
    a eye1 "Do you remember what you were doing?"

    show ambrose frown

    c frowntalk "I just... wanted to get as far away as I could from where I was..."
    cn frown eye2 "I don't remember where I was running. I just remember running."
    c frowntalk "I'm sorry."
    show cecil frown

    a frowntalk eye3 "You caused quite a stir, you know. Please don't run away again. We want to help."
    show cecil eye1
    a frowntalk eye2 "Nemo's still out, he went looking for your friend."
    a frowntalk eye1 "It's the weekend so I don't have {i}too{/i} much work to do, but you're free to stay here and wait on him or walk around campus with me."

    show ambrose smile

    cn "Waiting on Nemo might take all day... but if I go with Mr. Ambrose, we might find or see something."
    cn eye2 "He's a vampire, but..."

    c frowntalk eye1 neutral "I'll go with you. If that's alright."

    show cecil frown

    a talk "That's fine."

    show ambrose smile

    stop music fadeout 2


    scene bg hallway1:
        zoom 0.8
        xalign 0.5
        yalign 0.65
    show cecil pink up frown at side
    show ambrose pink up frown eye2 glove glass coat at center:
        xalign 0.8
    with fadee

    play music "audio/a432.mp3" fadein 2
    queue music "audio/a432.mp3"

    cn frown "He knows his way around the place so well. I can't imagine how many times he's walked through these halls."
    cn frown eye2 neutral "Come to think of it, I... I don't really know a lot about him."

    c frowntalk eye1 up "Mister?"

    show cecil frown

    a frowntalk eye1 "Hm?"

    show ambrose frown

    c frowntalk "How old is this place? It's your family's university, right?"

    show cecil frown

    a talk "It is. It's been part of our family for centuries, ever since one of my ancestors had it built."
    a talk "I've lived my entire life here."

    show ambrose smile

    c frowntalk "On campus? Or in your apartment?"

    show cecil frown

    a frowntalk "No."

    show ambrose frown

    nar "He places a hand on the wall."

    a frowntalk "Here."

    show ambrose smile

    c frowntalk "Here?"
    c shock arm2 "You mean, this building?!"

    show cecil frown

    a talk eye3 "Yes."
    show cecil arm1
    a frowntalk eye2 "This was my childhood home, but... after my father passed away a few years ago, I moved out."
    a frowntalk eye1 "I let them turn it into a faculty and classroom building for the university and moved into that apartment suite."
    a talk "Not too long after that, I met Nemo."

    show ambrose smile

    cn frown eye2 neutral "It's hard imagining this place being a home, with all the people walking through it right now."

    c frowntalk eye1 "Why would you move out of somewhere so big and fancy?"

    show cecil frown

    nar "He laughs to himself."

    a talk eye3 "I have a lot of good memories here. Seeing my father come home every night, playing with our dogs, reading by the fireplace on a rocking chair..."
    a frowntalk eye2 "But it's too big for one person. Even big places can become claustrophobic."
    a frowntalk eye3 "So I thought it best to let it be repurposed."

    show ambrose frown

    cn frown eye2 "Good memories..."

    show ambrose up smile eye2:
        ease 1.5 zoom 0.8 xalign 0.3

    show cecil eye1

    nar "Mr. Ambrose makes small talk with a gentleman that approaches him. I look around the area some more, not straying too far."

    hide ambrose with dissolve

    cn frown eye2 arm3 "It's his childhood home, but he was fine with letting it go? With letting other people use it?"
    cn frown "There's so many people here now, so many offices and classrooms... but it was his."

    nar "A group of students walk by, eagerly chatting about something from their class."

    cn frown "It's hard to picture moving from somewhere you've spent your entire life, but to do so after a parent passed... Would I be able to do that?"
    cn frown eye2 "...No, Mr. Ambrose said his father came home every night."
    cn frown unsure "What would that be like?"
    cn frown "What would it be like to lose that?"

    show cecil up frown eye1

    a "Cecil."

    show ambrose pink up smile glove glass coat at center:
        xalign 0.8
    with dissolve

    nar "He waves me over and we continue walking."

    c frowntalk "What's it like being a vampire?"
    c frowntalk arm2 "W-Wait! Do the people here know you're a vampire?"

    show cecil frown

    a talk eye3 "Hah, of course they do. It's something you could hide, but it's much more commonplace around aristocrats to be open about."
    show cecil arm1
    a eye1 "I've only been one for about 3 years now. It's... nice, I suppose."

    show ambrose smile

    c frowntalk surprise arm3 "\"Suppose\"?"

    show cecil frown

    a frowntalk "To be honest, I haven't noticed many changes aside from wanting blood and having better senses. I'm still young so it's hard to notice my aging slowing down."
    a frowntalk "When I get older it'll be easier to notice."
    a frowntalk eye2 "A lot of vampires turned when they were younger... It's not a choice you can undo, though."
    a frowntalk down "I can't understand why Leland let her turn at such a young age..."
    a eye3 "He must have been desperate to hold on to the last bit of his family, but..."

    show ambrose eye2 frown

    c frowntalk up "Huh?"

    show cecil frown

    a talk down eye3 "I, ah—I mean, it'd be so tragic {i}if{/i} she had!"

    show ambrose smile

    cn frown "Lucie..."

    show ambrose frown at shake
    show bg hallway1 at shake

    c frowntalk arm2 "Lucie's a vampire?!"

    show cecil frown scared

    a sad eye2 "..."
    a frowntalk "You really didn't know, did you..."
    a frowntalk eye1 "Both her and her uncle are vampires. From what I've heard, she turned into a vampire after parting from Nemo."

    show ambrose frown

    cn frown "She's a vampire... But, she acts so normal..."
    cn frown "I've never seen her drink blood, or... Well, I guess that's it."

    c frowntalk "Why... Why is she a vampire?"

    show cecil frown

    a frowntalk eye3 "...That is something you'll have to ask her."

    show ambrose frown

    cn frown eye2 arm1 "\"She turned into a vampire\"..."

    c frowntalk eye1 neutral "How do you become a vampire?"

    show cecil frown
    show ambrose eye5 at shakeonce

    nar "Mr. Ambrose lets out a surprised cough."
    nar "He looks around at the people nearby. They're all several feet away from us, in their own conversations."

    show ambrose eye3 with dissolve

    a frowntalk "It's a bit graphic to explain, but I'll try."
    a frowntalk eye2 up "When a vampire sucks blood from a human, they're not draining them completely, they're only drinking a portion of the person's entire blood supply."
    a frowntalk "However, there's a sweet spot in between draining a person completely of blood and almost draining them that will turn a person into a vampire. It's dangerous."

    show ambrose frown

    c frowntalk "But people can be born as vampires instead, right?"

    show cecil frown

    a frowntalk eye1 "No."
    a frowntalk "A vampire has to be created from a living human. Two vampires having a child will just have a human child."

    show ambrose frown

    cn frown scared eye2 "So... Lucie fully chose this."
    cn frown "She wasn't born a vampire. It was her decision."
    cn frown eye3 "Lucie, I—"

    stop music fadeout 2

    show cecil eye1

    scene bg hallway1:
        zoom 0.82
        xalign 0.5
        yalign 0.65
    show cecil pink up frown at side
    with sideswipe

    show guard at left:
        zoom 0.6
        xalign 0.0
        yalign 0.3
    show lucie pink up frown behind guard at right:
        yoffset 130
        xalign 1.1
    with dissolve

    show guard at shake

    play music "audio/Fairy Dance.mp3" fadein 2
    queue music "audio/Fairy Dance.mp3"

    "Guard" "Hold it! Don't walk off when I'm asking questions."

    l frowntalk eye3 "And I'm done entertaining questions. Good day."

    show lucie frown

    c "—!"
    show lucie at shake
    show guard at shake
    show bg hallway1 at shake
    c frowntalk "Lucie!"

    show cecil frown

    l eye1 "...!"

    show lucie frown


    show guard:
        ease 1.3 xalign -2.5 zoom 0.85 alpha 0.0
    show lucie down:
        ease 1.0 xalign -0.3

    pause(0.9)

    show ambrose pink down frown glove glass coat at center:
        xalign 1.75
        yalign 0.15
    with dissolve

    a frowntalk "What seems to be the problem here? Just a child running around on her own?"
    a frowntalk "You guards can leave her to me."

    show ambrose frown

    l eye2 "..."

    show lucie frown:
        ease 0.5 xoffset -300



    a frowntalk "Where do you think you're going? Trying to fix all your problems on your own?"

    show ambrose frown

    l frowntalk "I'm more than capable of making it by myself."

    show lucie frown eye1

    c frowntalk "But you don't have to! Let me help!"

    show cecil frown
    show lucie:
        ease 0.5 xoffset 0

    l grimace eye2 "..."
    show lucie at shake
    l eye1 "If it weren't for {i}him{/i}, the trail wouldn't have gone cold...! So I don't need anyone's help!"

    show lucie frown

    a frowntalk "If it weren't for him, you'd be dead."
    show ambrose frown

    l grimace eye2 "...!"

    nar "All this commotion has made quite a few heads turn our way and even more people coming to see what's the fuss about."

    show annie down frown behind lucie, ambrose at center:
        zoom 0.6
        yalign 1.0
    with dissolve

    annie frowntalk "Cecil! So this is where you've run to!"

    show annie frown
    show lucie eye1 frown

    c scared shock "...!"

    show cecil frown
    show ambrose behind lucie

    show lucie:
        ease 0.5 zoom 1.6 xalign 1.0 yoffset 40

    nar "As Annie rounds the corner, Lucie grabs my wrist with her delicate, gloved hand and starts running."

    show lucie:
        ease 0.7 xalign -8.0
    hide cecil
    with dissolve

    hide lucie with dissolve

    show ambrose at shake

    a frowntalk "Wait—!"

    show ambrose frown


    scene bg college1:
        zoom 0.7
        yalign 0.8
        xalign 0.5
    show cecil unsure frown at side
    show lucie down frown eye2 at center:
        yoffset 100
        zoom 1.1
    with sideswipe

    c frowntalk "Lucie—!"

    show cecil frown
    show lucie at shake

    l frowntalk "Just save it for now!"

    show lucie frown


    scene bg parlor:
        zoom 0.7
        yalign 0.8
        xalign 0.5
    show cecil unsure frown at side
    show lucie down frown eye3 at center:
        yoffset 100
        zoom 1.1
    with sideswipe

    nar "She pulls me into an empty area and lets go of my arm."

    c frowntalk arm2 "Lu... Lucie..."

    show cecil frown arm1 eye3

    nar "A moment passes before we're both able to catch our breaths."

    c talk unsure arm2 "Lucie... I'm so glad you're okay..."

    show cecil smile arm1

    l frowntalk eye3 up "Meanwhile you seem to be getting caught at every turn... Phew..."

    show lucie frown

    c talk eye2 "Hah... hah..."

    show cecil smile eye1

    l frowntalk down eye1 "Why are you with him?"

    show lucie frown

    c talk up "With Nemo? I happened upon him while traveling south. He offered to help me reach Lauremburg."
    c frowntalk "He's helped me get this far. I'd still be stuck way up north if it weren't for him."
    c frowntalk unsure "Is he... Is he really your brother?"

    show cecil frown

    stop music fadeout 10

    l eye2 sad "..."
    l frowntalk eye3 "Yes..."
    l frowntalk eye2 "...And no."

    show lucie frown

    cn frown "What kind of answer is that?"

    show lucie eye3 up at cecilcurtsy

    nar "She takes off her gloves and plops down on the floor."

    l frowntalk "...Sit down."

    show lucie frown at cecilcurtsy:
        ease 0.5 zoom 1.3 yoffset -20
    show bg parlor at curtsy

    play music "audio/Asking Questions.mp3" fadein 2
    queue music "audio/Asking Questions.mp3"

    pause (1.0)

    l sad "..."
    l frowntalk eye2 up "I'm from the house of Fleur. My father was a successful businessman just like his father before him and so on."
    l frowntalk "10 years ago, my family was having a frolic on our boat. The boat wasn't near shore and it was late at night."
    l frowntalk eye3 "A vampire boarded the boat and killed almost everyone on board, including the crew. My parents as well."

    show lucie frown eye2

    c scared frowntalk "...!"
    show lucie at shake:
        yoffset -20
    show bg parlor at shake

    c frowntalk "Th-That's horrible!"

    show cecil frown

    cn frown eye2 "It's terrible to hear, but the way she's describing it... It's so dispassionate and blunt."
    cn frown "Her eyes have such an indifferent look to them."

    show cecil eye1

    l frowntalk "Nemo was just a deckhand on board. He found me and fled the boat with me before the attacker could reach us."
    l frowntalk "We're not related by blood. Nemo happened to find me before he fled."
    l frowntalk sad "I was too young to remember anything about it."
    l frowntalk "After that, he raised me as his little sister but didn't tell me about that night."

    show lucie frown

    c frowntalk "I'm..."

    cn frown eye2 "I don't know what to say. It's hard to believe, and yet..."
    cn frown "A decade ago, she was about 3 years old."
    cn frown "A decade ago, Nemo... Nemo would have been around 13 years old."
    cn frown "...He was our age. He was working for a living with no family."
    cn frown "He saw all the adults around him be murdered by a vampire."
    cn frown scared eye3 "I don't know what I'd do if that happened to me today."

    c frowntalk eye1 "So... You hate him because he took you?"

    show cecil frown
    show lucie down eye1 at shake:
        yoffset -20

    l frowntalk "He lied!"
    l frowntalk "He told me my parents died of diseases! He kept it from me for almost 8 years!"
    l frowntalk eye2 "My uncle found out I was still alive and found me. He was the only one willing to tell me the truth."

    show lucie frown sad

    nar "Her voice falters as her words become quieter."

    l frowntalk "I... I have to find the attacker. That's the whole reason I became a vampire."

    show lucie frown

    nar "I grab her hand to try to reassure her—"


    show lucie eye1 at shaketwice:
        yoffset -20
    show bg parlor
    with greenlight

    l grimace "Ow—!"

    show lucie frown

    c shock "—!"

    cn frown "T-That green light again! I forgot all about it!"
    cn frown "Why would it come back when I touched Lucie, though?!"

    l down eye2 "..."

    show lucie at shakeslow:
        yoffset -20
    show bg parlor at shakeslow

    c frowntalk unsure arm2 "I-I'm sorry! I don't know what that is!"

    show cecil frown

    show lucie eye3 at curtsy:



    nar "She slips her gloves back on and stands up, not meeting my eyes."

    stop music fadeout 10

    l frowntalk eye1 "I need to find where I'm going to scout tonight."

    show lucie frown

    c frowntalk "I'm coming with you."
    c talk arm2 "We'll catch the criminal together, I promise!"

    show cecil smile arm1
    show lucie at shakeslow

    l frowntalk eye5 "Y-You shouldn't make such childish promises, Cecil..."

    show lucie frown

    c talk eye3 "It'll be alright, don't worry!"

    cn smile eye1 "It'll be fine now."












    $ save_name = "Split Path"
    $ chapter_num = "Twenty"

    call chapter from _call_chapter_19

    $ cecilpov = False

    scene bg college1:
        zoom 0.7
        yalign 0.8
        xalign 0.5
    show nemo up frown at side
    with fadee

    play music "audio/Asking Questions.mp3" fadein 2
    queue music "audio/Asking Questions.mp3"



    nn "Dammit... I should've known Cecil would run away the second he saw Lucie! The kid can't stay put to save his life."
    nn "Now I've got 2 kids, completely alone, looking for a bloodthirsty vampire at night. And for some ungodly reason they're hoping he's a killer! Perfect."
    nn "At least Lucie has picked up a thing or two about fighting. Cecil'll just be dead weight to her. I wouldn't be surprised if she made him sit alone while she went off fighting."


    scene bg cathedral:
        zoom 0.6
        xalign 0.5 yalign 0.6
    with sidefade

    nn "...What is Lucie going to say about me?"
    nn "Is she going to tell him the truth? Is it going to be some bastardization of what Leland told her?"
    nn "Cecil'll believe anything she tells him without questioning it."
    nn "Lucie... where'd you run off to?!"


    scene bg cathedralinside:
        zoom 0.55
        xalign 0.5 yalign 0.0
        easein 2.3 yalign 0.65
    show nemo cathedral up frown arm2 at side
    with fade
    $ nemopov = True

    n frown "—!"
    n frowntalk "Cecil!"

    show nemo frown

    show cecil cathedral up frown at center:
        yoffset 100 xalign 0.2
    show lucie cathedral down frown behind cecil at right:
        yoffset 100 xalign 0.75
    with dissolve

    c "...!"

    nn surprise eye2 "Of course they're here, staking out this place. Waiting for nightfall."

    n frowntalk up eye1 arm1 "Cecil!"

    show nemo frown
    show lucie:
        ease 0.8 xoffset -200
        easein 0.25 xoffset -215
        easein 0.30 xoffset -190
        easein 0.25 xoffset -209
        easein 0.30 xoffset -200
        ease 1.1 xoffset 0

    c neutral eye2 "..."


    show cecil at shake
    show lucie at shake
    show bg cathedralinside at shake

    n frowntalk down "Are you really just going to listen to her? Don't you have even a bit of thinking on your own?"

    show nemo frown
    show cecil eye1 at shake

    c frowntalk down arm2 "I do!"
    c frowntalk "You've— All of you've been treating me like I'm a lost puppy this entire time! I don't need to be kept on a leash!"
    c frowntalk "I came here because I decided to! I ran away because I wanted to! Not because someone told me to!"
    show cecil at shake
    c frowntalk arm3 "And now I'm going to help Lucie because I want to and you're not going to stop me!"

    show cecil frown

    n unsure eye2 "..."


    show cecil:
        ease 2.0 xalign 2.0 alpha 0.0
    show lucie:
        ease 2.0 xalign 2.9 alpha 0.0

    pause(2.3)


    scene bg office2:
        zoom 0.5
        yalign 0.65
        xalign 0.5
    show nemo pink down frown eye3 nocap at side
    show ambrose pink unsure frown at center:
        xoffset 60
    with fadee

    a frowntalk "Did you—"
    show ambrose frown at center:
        ease 0.4 zoom 1.3 xoffset 130
    a frown "..."

    n frowntalk unsure "What'd I do wrong...?"
    n frowntalk "I can't do a damn thing right."
    n frown eye2 "..."
    n frowntalk "What was I supposed to do? Leave a toddler there?"
    n frowntalk "There, where everyone else was so butchered they couldn't get an accurate body count? In that hell?"

    show nemo frown

    a "..."

    stop music fadeout 4

    nn eye3 "It's alright. You don't have to say anything."
    nn "I already know."












    $ save_name = "Nobody"
    $ chapter_num = "Twenty-One"

    call chapter from _call_chapter_20

    $ nemopov = False
    $ cecilpov = True

    scene bg hallway1:
        zoom 0.8
        xalign 0.5
        yalign 0.65
    show lucie pink up frown at center
    show cecil pink up frown at side
    with fade


    play music "audio/Isolation Waltz.mp3" fadein 2
    queue music "audio/Isolation Waltz.mp3"

    nar "Having left the cathedral for now to avoid Nemo, Lucie and I sneak from corridor to corridor, avoiding anyone who might find us suspicious."

    cn frown eye2 unsure "We might be making ourselves more suspicious doing things this way..."

    show lucie down at shake

    l frowntalk "Keep up!"

    show lucie frown

    c frowntalk arm2 eye1 up "Sorry!"

    cn frown arm3 neutral "We just need to find a quiet room to hide out in until nightfall. It's hard, though, considering all these rooms have different schedules."
    cn frown down eye1 "When we think we've found one, people start coming inside!"
    cn frown eye2 neutral "If we keep moving rooms, though, eventually it'll be night. ...If we're not caught first, that is."

    show cecil eye1

    show lucie up eye2:
        ease 0.6 zoom 0.95 xoffset 120 yoffset 10
        linear 0.35
        ease 0.9 zoom 0.90 xoffset -100 yoffset 20
        linear 0.35
        ease 0.92 zoom 0.85 xoffset 300 yoffset 30
        linear 0.35
        ease 0.95 zoom 0.80 xoffset -295 yoffset 40
        linear 0.35
        ease 0.83 zoom 0.75 xoffset 0 yoffset 50
        linear 0.35
        ease 0.73 zoom 0.73 xoffset -120 yoffset 55
        linear 0.35
        ease 0.60 zoom 0.70 xoffset 0 yoffset 60

    nar "Lucie quietly steps down an empty hallway. Her hair sways with her movement, but I notice the back of her hair is starting to become matted from lack of care."

    cn frown "Her hair is so long, it's always been hard for her to brush it herself—not that she cares to keep it up, either."
    cn frown "Mister Leland isn't with her to brush it for her like he usually does."
    cn frown unsure eye2 "Does she know he's here?"

    stop music fadeout 3

    show lucie eye1:
        ease 1.3 zoom 1.1 yoffset 20
    show bg hallway1:
        ease 1.3 zoom 0.9

    c frowntalk up arm1 eye1 "Say, where've you been staying?"

    show cecil frown

    l frowntalk "Right here."

    show lucie frown

    c frowntalk surprise "Huh?"

    show cecil frown

    play music "audio/Fairy Dance.mp3" fadein 2
    queue music "audio/Fairy Dance.mp3"

    l frowntalk down eye2 "I tried to lodge in an inn but they wouldn't accept my money. None of them would! I even offered a little extra, but no."
    show lucie:
        easein 0.25 xoffset 9
        easein 0.35 xoffset -11
        easein 0.25 xoffset 7
        easein 0.35 xoffset 0
    l pout eye3 "\"Bring your father by and we'll talk\". When I told 'em he's 6 feet under they started calling for the coppers!"
    l frowntalk up eye1 "So I've been sleeping in empty rooms on campus. Classrooms, sitting rooms, whatever was quiet and vacant."
    l talk "It helped me with patrolin', too, since I'm already on campus."

    show lucie smile

    c frowntalk unsure arm2 "That's horrible!"

    cn arm1 eye2 smile "She spends a few nights out roughing it and her accent starts to shine..."

    show cecil eye1 frown neutral

    l frowntalk "It's okay! Because..."

    show lucie frown

    $ renpy.music.set_pause(True, channel="music")


    hide cecil
    show luciechibicg:
        zoom 0.85
    with hpunch

    play music2 "audio/Baltic Levity.mp3"
    queue music2 "audio/Baltic Levity.mp3"

    $ achievement.grant("teddy")
    init:
        $ achievement.register("teddy")
        $ achievement.sync()
    $ achievement.sync()

    l "I have Teddy with me!"

    cn "Ack! She brought that thing with her?!"

    c "W-Why did you bring tha—him with you?"

    cn "Everytime I see that {i}thing{/i} it looks even more haggard and distressed. When will she put it out of its misery?"

    l "Teddy's kept me company so I haven't been alone."

    c "I-I'm sure he has."

    l "He's supposed to bring me good luck but I haven't been too lucky yet."
    l "But tonight!"
    l "Tonight something will happen! I'm sure of it!"

    cn "Well, it'd be hard for her to be wrong..."

    stop music2 fadeout 2


    show lucie smile
    show cecil pink unsure smile eye2 at side
    hide luciechibicg
    with dissolve

    nar "She—thankfully—puts away the beheaded stuffed animal and we go back to searching for an empty room."

    $ renpy.music.set_pause(False, channel="music")

    c frowntalk eye1 neutral "There's guards down this corridor."

    cn frown "Has Mr. Ambrose told any of them to look for us?"

    l frowntalk "So?"

    show lucie frown:
        ease 1.8 zoom 0.6 yoffset 80

    nar "Lucie turns the corner and heads down the hallway."

    show lucie at shake:
        zoom 0.6 yoffset 80
    show bg hallway1 at shake

    c frowntalk "W-Wait!"

    show cecil frown

    l frowntalk "Can't be scared of nothin'!"

    show lucie frown:
        ease 0.4 xalign 1.0 alpha 0.0

    nar "Before she reaches where the guards are talking, she makes a sharp turn and darts into a room."

    scene bg room1 alt:
        zoom 0.4 yalign 0.5 xalign 0.5
    show lucie up frown at center:
        yoffset 20
    show cecil unsure frown at side
    with sideswipe

    c frowntalk "Huff... huff..."

    show cecil frown

    l frowntalk "What's the matter?"

    show lucie frown

    c frowntalk eye3 "No... Nothing..."

    cn frown eye2 "She's a natural at this—!!"

    show cecil eye1

    l frowntalk "I think this room is empty for at least a couple hours."
    l talk "Things'd be a lot harder if everyone weren't too scared to stay out a night!"

    show lucie smile

    c frowntalk "You said it..."

    show cecil up frown
    show lucie:
        easein 0.4 yoffset 40
        easein 0.25 yoffset 20

    nar "She finds a chair and plops down."
    show lucie at center:
        ease 1.5 zoom 1.2 yoffset 40
    show bg room1 alt:
        ease 1.5 zoom 0.5 xalign 0.5
    extend " I close the door carefully and sit down."

    cn frown eye2 "It'll be nightfall soon... After that, we've got to hope the attacker strikes again."
    cn frown unsure eye1 "But wait, what if he doesn't? I'll have to sleep out here on campus!"
    cn "This is going to be a long day... or week!"

    show lucie:
        easein 0.4 yoffset 60
        easein 0.25 yoffset 40
    show cecil neutral

    nar "Lucie pulls out her zombie teddy and starts poking at its single ear."

    cn surprise eye2 arm3 "Now that I think about it, didn't she say something odd that night?"

    c frowntalk eye1 "Lucie, the other night you called Nemo something different, didn't you?"

    show cecil frown

    l eye2 up frown "Mhm."
    show lucie frowntalk
    extend " It sort of just came out."

    show lucie frown

    c frowntalk "What was it?"

    show cecil frown

    l frowntalk "...I called him Robin to make him mad."

    show lucie frown

    cn neutral "I didn't want to say it to his face, but Nemo is an odd name."

    c frowntalk arm1 "...That's his real name, isn't it? Robin, not Nemo."

    show cecil frown unsure

    l frowntalk "...Yes."
    l eye3 "He changed it after the attack. At least, that's what my uncle told me."

    show lucie frown

    nar "Lucie turns back to her teddy while I sit here, dumbfounded."

    cn "It's hard to process it."
    show lucie eye1
    cn "It seems so simple, to start going by another name, but to do it for good..."
    cn "Why did he do it?"
    cn "Was he that desperate to flee from that night? To not look back?"
    stop music fadeout 3
    scene black
    cn "To become Nobody?"


    scene bg cathedralinside:
        zoom 0.55
        xalign 0.5 yalign 0.65
    show cecil cathedral neutral frown arm3 at side
    show lucie cathedral up frown at center:
        yoffset 20
        ease 0.5 xoffset 400
        linear 1
        ease 0.6 xoffset -200
        linear 1
        ease 0.55 xoffset 250
        linear 1
        ease 0.49 xoffset -630
        linear 0.8
        ease 0.71 xoffset 320
        linear 1
        ease 0.6 xoffset -400
        linear 0.7
        ease 0.7 xoffset 510
        linear 1
        ease 0.8 xoffset -150
        linear 0.7
        repeat
    with fade

    play music "audio/Isolation Waltz.mp3" fadein 2
    queue music "audio/Isolation Waltz.mp3"

    nar "The cathedral is eerily quiet. Not even the wind can be heard here."
    nar "Lucie looks around, opening up doors and looking out windows."

    c frowntalk surprise "Do you know where you're going?"

    show cecil frown

    l talk "Nope."

    show lucie smile

    cn frown eye2 "Sounds about right..."
    hide lucie with dissolve
    cn frown neutral eye1 "Somehow, this cathedral is much scarier tonight than it was before."
    cn frown "It's dead quiet, but I keep looking over my shoulder, half expecting a vampire to be poised to attack."
    show bg cathedralinside at shake
    cn frown down arm2 "No! I can't be scared! I'm a gentleman, I have to be brave for Lucie!"

    c "..."

    cn unsure "Brave for Lucie... Who's walking around the scaffolding..."

    show bg cathedralinside at shake

    c frowntalk "L-Lucie, get down from there!!"

    show cecil frown

    l "I can see real good up here!"

    show bg cathedralinside at shake

    c frowntalk "That's too dangerous!!"

    show cecil frown
    show lucie cathedral frown eye2 at center:
        yoffset 20
    with dissolve

    l "..."
    l frowntalk "You're no fun."

    show lucie frown

    cn frown "...A gentleman isn't supposed to just be brave, but also keep ladies out of danger! Yes, that's what I'll do!"
    cn smile up "Whenever she's doing something dangerous, I'll simply remind her not to do it!"
    cn frown arm1 up "Oh, that reminds me..."

    show lucie eye1

    c frowntalk "Lucie, what were those red things near you the other night?"

    show cecil frown

    l frowntalk "The other night? When you were attacked and almost mauled?"

    show lucie frown

    c frowntalk scared eye2 "W-When you were on the roof. Yes."

    show cecil frown eye1 neutral

    l frowntalk "Blood."

    show lucie frown

    c frowntalk surprise arm3 "Blood...? Wait, wait, who's blood?"

    show cecil frown

    l frowntalk "Mine."
    show cecil neutral
    l frowntalk "Vampires can learn how to manipulate their blood in certain ways. It takes a lot of training and it's hard to find people willing to teach it unless you have the money or prestige."
    l frowntalk "My uncle wanted me to learn how to defend myself. It took months, but now I can turn my blood into small spikes."
    l frowntalk sad eye2 "It's really tiring, though... I slept the entire next day and needed extra blood afterwards."

    show lucie frown

    c frowntalk up arm2 "That's so cool though!"

    show cecil frown
    show lucie eye5 at shakeslow with dissolve

    l frowntalk "I-It's just for self defense..."

    show lucie frown

    stop music fadeout 1


    play sound "<from 0.4>audio/thud.mp3" fadein 0.5
    pause(1.0)

    show lucie down eye1

    c down arm3 frowntalk "Something's outside...!"

    show cecil frown

    l frowntalk down eye1 "Stay here!"

    show lucie frown:
        ease 0.6 xalign 2.0 alpha 0.0

    pause(0.3)

    show bg cathedralinside at shake

    c frowntalk arm3 "Wait—!"

    nar "In a leap and a bound, she darts out the door, leaving me behind."
    cn frown unsure "Was she always this fast...?!"


    scene bg cathedral night:
        zoom 0.6 yalign 0.75 xalign 0.5
    show cecil night scared frown at side
    with sideswipe

    play music "audio/Asking Questions.mp3" fadein 2
    queue music "audio/Asking Questions.mp3"

    c frowntalk "Lucie!"

    show cecil frown

    show lucie night down frown at center:
        zoom 0.35 yalign 0.96 blur 0.9
    with dissolve

    nar "In the opening in front of the cathedral, Lucie is standing off against a dark figure."
    nar "Even though the moon is nearly full tonight, it's hard to distinguish anything about the dark figure other than it's an adult. It moves too fast to tell anything else."

    show lucie at shake

    l frowntalk "Stay back!"

    stop music fadeout 0.5

    show lucie frown:
        ease 0.7 xalign 1.4 alpha 0.0

    play music "audio/Nightmare.mp3" fadein 2
    queue music "audio/Nightmare.mp3"

    nar "The figure rushes her. She narrowly dodges, the edges of her dresses ruffling as she steps back."

    cn frown eye2 "It's dangerous for me to get too close... I only got in the way whenever Nemo was fighting."
    cn frown "Is there really nothing I can do for her?"

    l "{color=#ff2e2e}Blood Art <Impalement>!{/color}"

    play sound "<from 1>audio/stab.mp3"
    play foley "audio/stab.mp3"
    scene impalement

    nar "Red spikes slice through the air, aimed directly at the figure."
    nar "They're able to dodge some of them, but a few hit their mark and gouge into their arm."


    stop foley

    l "—!"

    cn "It impaled them, but they're still running! Lucie—!"


    scene black

    show gunshotsparkles
    show gunshot

    play sound "audio/gunshot2.mp3"

    nar "A single gunshot rings through the air. The figure collapses on the ground."

    scene bg cathedral night:
        zoom 0.6 yalign 0.75 xalign 0.5
    show cecil night scared frown at side
    with fade

    cn frown "Was that—"

    stop music fadeout 2

    show guard at center:
        zoom 0.6
    with easeinleft

    "Guard" "You there! Are you two okay?"

    c frowntalk eye3 "Yes..."

    show cecil frown eye1

    hide guard with easeoutleft
    show lucie night sad frown:
        zoom 0.5 xalign 0.5 yalign 1.0
    with dissolve
    show lucie at center:
        ease 1.8 zoom 0.9 yalign 0.0
    show bg cathedral night:
        ease 2 zoom 0.75

    play music "audio/Asking Questions.mp3" fadein 2
    queue music "audio/Asking Questions.mp3"

    pause(1.0)

    nar "Lucie bends down to look at the vampire. He's out cold."

    cn frown "I'm not great at guessing ages, but he looks around Nemo's age. He probably goes to school here."

    l eye2 "..."

    cn frown "He's too young."


    play sound "audio/thud.mp3"
    pause(1.0)

    show bg cathedral night at shake
    show lucie down eye1 at shake

    c frowntalk arm2 "What was that?!"

    show cecil frown

    l frowntalk "Over there!"

    show lucie frown dress1:
        ease 0.7 xalign 2.2 alpha 0.0

    nar "Lucie rushes off in the darkness, leaving the unconscious man to the guards."

    c frowntalk "Wait up!"

    show cecil frown arm3


    scene bg city2:
        zoom 0.65 yalign 0.8 xalign 0.5
    show cecil cathedral unsure frown arm3 at side
    with sidefade

    cn frown "What...?"

    nar "A block away, a man and a woman lay on the ground. The woman is trying to get up and clasping her neck."

    show bg city2 at shake

    c frowntalk arm2 scared "A-Are you okay?!"

    show cecil frown arm1

    show lucie cathedral frown at right:
        zoom 0.9
        yoffset 60 xalign 0.5
    show npcfem3 at cathedralcolor:
        zoom 0.7 yalign 0.1 xalign 0.3
    with dissolve

    show npcfem3 at cathedralcolor:
        linear 0.4
        ease 0.4 yalign 0.7
    show lucie:
        ease 0.4 yoffset 110
        ease 0.25 yoffset 60
        linear 0.2
        ease 0.55 xalign 1.0

    nar "Lucie helps the woman to her feet. Her neck is scratched, but not bleeding."

    l frowntalk "What happened?"

    show lucie frown
    show npcfem3 at cathedralcolor, shakeslow

    "Woman" "I-I was heading to grab a notebook I'd left in my office..."
    "Woman" "I thought someone was following me so I ran, but I wasn't fast enough..."

    nar "The man on the ground moans."

    c frowntalk "Wait..."

    show cecil frown

    nar "I step closer to him."

    show lucie down at shake

    l frowntalk "Don't get too close!"

    show lucie frown

    c scared arm1 shock "...!"

    cn frown "The half-conscious man is the professor Nemo's been working with."

    leland "Lucie!"

    hide npcfem3 with dissolve
    show lucie:
        ease 0.9 xalign -0.5
    pause(0.1)
    show guard at left:
        alpha 0.0 zoom 0.45 xalign 1.4
        ease 1.2 alpha 1.0 xalign 0.35
    show guard as guard2 at right:
        alpha 0.0 zoom 0.45 xalign 1.5
        ease 1.2 alpha 1.0 xalign 1.1
    pause(0.05)
    show leland cathedral frown down hat at center:
        alpha 0.0 xalign 1.5 yalign 0.15
        ease 1.3 alpha 1.0 xalign 1.15

    nar "Mr. Leland and a group of guards make their way towards us across the grass."

    l eye2 "..."

    show lucie frown:
        ease 0.5 yoffset 140
    pause(0.5)
    show lucie:
        ease 0.5 xoffset 35
        linear 0.25
        ease 0.5 xoffset -35
        linear 0.25
        repeat

    nar "Lucie bends down beside Mr. Scott and begins to look through his pockets."

    c frowntalk surprise arm3 "What're you doing?"

    show cecil frown

    l frowntalk "Proof."

    show lucie frown

    cn frown "Proof...?"

    l frowntalk "There's gotta be something here. Something."
    l frowntalk "Anything."

    show lucie frown

    c scared "..."
    c frowntalk arm1 "Lucie, I don't—"

    show cecil frown

    show lucie up:
        ease 0.25 xoffset 0

    l talk "—!"

    hide guard
    hide guard2
    with dissolve

    show lucie frown:
        ease 1.0 zoom 1.1 xalign -0.8
    show leland:
        ease 1.0 zoom 1.2 xalign 2.5
    show bg city2:
        ease 1.0 zoom 0.75

    nar "She pulls out a small, ornate brooch from Mr. Scott's breast pocket."

    l frowntalk "This..."
    l frowntalk "This is a brooch with the Fleur insignia."

    show lucie frown at shake
    show leland at shake
    show bg city2 at shake

    c frowntalk arm2 up "Really?!"

    show cecil frown
    show lucie sad

    nar "She silently nods her head, not taking her eyes off of it."

    leland frowntalk eye3 "Your mother used to wear that all the time... I haven't seen it in years."

    show leland frown

    cn frown "So, that means..."

    c frowntalk "You did it Lucie!"
    c talk "You found your parents' attacker!"
    c "I'm so happy for you, Lucie."

    show cecil smile

    nar "Mr. Leland places a hand on her shoulder and bends down."

    show lucie up

    leland up talk eye1 "It's alright. It's over now."
    leland "I'll talk to the officers later. For now, let's head to the inn."

    show leland smile

    cn neutral "It's over... It's really over."
    cn arm1 "She found him and now we're going home."
    cn frown eye2 "Admittedly, I feel guilty leaving on such short notice. I never got the chance to say thank you to Nemo for helping me."
    cn scared "...I came all this way to help Lucie, but now that we're heading home, I..."

    hide leland with dissolve

    show lucie eye1:
        ease 1.0 zoom 1.4 yoffset 10

    pause(0.5)

    show cecil up eye1

    nar "Lucie grasps my hand with her gloved hand."

    l up talk "We can go home now."

    show lucie smile

    c frowntalk neutral "...Yes."

    show cecil frown
    show lucie:
        ease 0.4 yoffset 60
        ease 0.25 yoffset 10

    stop music fadeout 10

    l talk "Let's go."

    show lucie smile

    c scared eye2 "..."
    c unsure talk eye1 "Alright."

    show cecil smile










    $ quick_menu = False

    scene black with fadee

    show text2 "1 Month Later":
        alpha 0.0 xalign 0.5 yalign 0.41
        linear 1.0 xalign 0.5 yalign 0.48 alpha 1.0

    pause(2)

    $ save_name = "Apprehension"
    $ chapter_num = "Twenty-Two"

    call chapter from _call_chapter_21

    $ nemopov = True
    $ cecilpov = False

    scene bg office2:
        zoom 0.5
        yalign 0.65
        xalign 0.5
    show nemo pink up frown arm2 eye3 nocap at side
    with fade

    play music "audio/a432.mp3" fadein 2
    queue music "audio/a432.mp3"






    play sound "audio/clinking.mp3" fadein 0.5

    nar "I run the plates under water and scrub away anything that's left."
    show nemo arm1 eye2
    nar "When I'm done, I hand them to Ambrose. He gently dries them with a hand towel and places them on the countertop."
    nar "The radio plays softly in the sitting room."

    show ambrosen pink up smile at center:
        zoom 1.25
        xoffset 60
    with dissolve

    an talk "What's on your mind?"

    show ambrosen smile

    n frowntalk eye3 "Just wondering if I should try fixing the lamp in the guest bedroom before dinner."

    show nemo frown eye2

    an talk "The roast will take a while before it's ready, unless you'd rather eat out."

    show ambrosen smile

    n frowntalk eye1 "Roast is fine."

    show nemo frown

    nar "He places the towel on the counter and starts preparing the roast."

    an frowntalk "It's been a while since you traveled."
    an frowntalk "That's what's on your mind, isn't it?"

    show ambrosen frown

    n unsure eye2 arm2 "..."

    nn "With Scott in jail, I haven't had any excuses to go anywhere. No errands to run a few cities over."
    nn eye3 "It doesn't sit right with me."
    nn "As a kid, if you stayed in one place for too long you'd run out of work. The coppers would try to throw you in an orphanage, or worse, a factory."
    nn eye2 "Lucie and I traveled from city to city several times over, looking for any kind of work or shelter that'd keep us together."
    nn down "But most of all... that fear. That nagging fear that I'd be accused of that massacre or that the culprit would find and silence us."
    nn "In hindsight, it's hard to imagine any regular copper fingering the crime on a 13 year old. A kid doesn't think like that, though."

    show nemo up arm1 eye1

    nar "I feel a hand on my shoulder."

    an frowntalk "You don't have to run anymore."

    show ambrosen frown

    n eye3 talk surprise "It's hard to tell if I'm even running anymore or if my feet just won't stop walking."

    nn frown eye2 down "Of course you're still running."

    show nemo up eye1

    an talk eye3 "Then let me walk beside you."
    an eye1 "Would a vacation work?"

    show ambrosen smile

    n grin surprise "Like where?"

    show nemo smile

    an frowntalk eye3 "Anywhere. Really, I don't care."
    an talk eye1 "And neither do you, right?"

    show ambrosen smile

    n frowntalk eye2 up "I guess not."
    n frowntalk eye1 surprise "Are you sure you can take that much time off? When you had a summer cold a fortnight ago, they acted like classes had to be canceled campus-wide."

    show nemo frown

    an frowntalk unsure eye3 "Ah, that might be an issue... Especially with no holidays close by..."
    an talk eye1 "What if we make it for an occasion?"

    show ambrosen smile

    n frowntalk eye3 "I hope you're not about to say \"we'll say it's your birthday\"."

    show nemo frown eye1

    an frowntalk eye2 "What about..."
    an frowntalk up "For a honeymoon?"

    show ambrosen smile eye1

    n frowntalk shock "Huh?"

    show nemo neutral



    an frowntalk "Stay with me."

    show ambrosen frown

    n eye2 arm2 "..."

    nn "Over two years ago, I arrived here and met him. I couldn't stand him."
    nn arm1 "A young, rich vampire controlling an entire subsection of the city. A man who relishes in being more than human."
    nn "A man who solely devoted himself to work so he could avoid processing his grief and loneliness."

    n frowntalk up eye3 "I'm not becoming a vampire."

    show nemo frown
    show ambrosen eye3

    nar "He sighs."

    an frowntalk "I know."

    show ambrosen smile eye1
    show nemo eye2

    nar "His hand rests on the side of my face."

    nn shock "I want to say yes."
    nn eye1 "I want to drop the plate I'm washing and kiss him."
    nn "I {i}should{/i} say yes."
    nn "But like an idiot I just stand there, staring at him."

    stop music fadeout 4


    play sound "audio/knock.mp3"

    show nemo up
    pause(0.4)

    an unsure frown "...?"

    show ambrosen:
        ease 1.5 zoom 0.7

    nar "Ambrose walks over to answer the door."

    an frowntalk down "...!"

    show ambrosen frown

    play music "audio/Fairy Dance.mp3" fadein 2
    queue music "audio/Fairy Dance.mp3"


    show ambrosen:
        ease 0.5 xalign 1.0
    pause(0.35)
    show lucie pink eye2 up frown at center:
        zoom 0.73 xalign -0.5 yoffset 110 alpha 0.0
        ease 1.2 xalign 0.3 alpha 1.0
    pause(1)

    n frowntalk sad "...Lucie!"

    show nemo frown eye2

    nar "The apprehension in my stomach about the future is replaced with a new anxiety of the present."

    n frowntalk down eye1 "What's wrong?"

    show nemo frown

    l down "..."

    show lucie frown eye1:
        ease 1.5 zoom 1.1
        linear 0.2
        ease 0.4 yoffset 170
        ease 0.4 yoffset 110
    pause(2.5)

    nar "She pulls out a tiny brooch from her pocket and hands it to me."

    l frowntalk "Did my mother ever wear this?"

    show lucie frown

    nn surprise eye2 "The detailing is pretty ornate, sure, but..."

    n frowntalk up eye1 arm2 "...I'm sorry. I don't remember."
    n frowntalk eye3 "I was too young to be allowed near the clients."

    show nemo frown eye1

    l sad eye2 "..."

    nar "Her eyes linger on the brooch."

    n frowntalk eye3 "I'll go to the jail and ask Scott what happened."

    show lucie eye1 up at shake

    nn frown down eye2 "I wanted to distance myself from this, but I can't ignore it if she's come all this way asking for help."
    nn "Something's nagging at her and it's going to keep bothering her until it's laid to rest."

    show nemo eye1 up
    show lucie:
        ease 0.35 yoffset 150
        ease 0.25 yoffset 110
        linear 0.15
        ease 1.5 zoom 0.6
        ease 0.4 yoffset 180
    pause(2.55)
    hide lucie with dissolve

    nar "To my surprise, Lucie nods and sits down in the parlor."
    nar "I look at Ambrose who waves me off."

    stop music fadeout 3


    scene bg police:
        zoom 0.7 xalign 0.5 yalign 0.7
    show nemo police eye2 frown at side
    with sidefademedium

    nn "It's odd, coming here to see someone."
    nn eye3 "I was almost thrown in a couple jails as a kid for pilfering, but it's a whole different feeling coming to one for visitation."
    nn eye2 "Not to mention..."
    nn down "He was accused of the Fleur family murders."

    n eye1 "..."

    play music "audio/Asking Questions.mp3" fadein 2
    queue music "audio/Asking Questions.mp3"

    show scott police neutral frown nogood at center:
        zoom 0.75
    with dissolve

    nar "A disheveled, worn out-looking man approaches me, handcuffs shackling his wrists and legs."

    s frowntalk "...Nemo."

    show scott frown

    n frowntalk "Scott."

    show nemo frown eye3

    nar "Despite not being charged with the murders from a decade ago, he confessed immediately to some of the attacks on campus. A harsh but understandable sentence of 5 years of prison labor was handed down to him."

    nn "On one hand, I can't help but feel it's too long. He's an acquaintance, after all."
    nn eye2 "But the reality is he attacked several people. That can't be so easily forgiven with a slap on the wrist."

    show nemo eye1

    s frowntalk eye2 "It's all horribly humbling."
    s frowntalk eye1 "At night, my mind still wanders to what lecture plans I should make."

    show scott frown

    n frowntalk "What happened?"

    show nemo frown

    s eye2 unsure "..."
    s frowntalk "I thought I'd try something rather different this time for an experiment..."

    show scott frown

    nn sad "Oh no."

    s frowntalk "...But I suppose it took more blood than I should have used... I'm so ashamed one of my experiments went this far."

    show scott frown

    nar "He shakes his head."

    n frowntalk eye2 down "I hate to ask this of you, but..."
    show scott eye1
    n frowntalk eye1 "This was found on your person when you were caught. Do you have any idea how it got there?"

    show nemo frown
    show scott at curtsy

    nar "He takes the small brooch into his hands."

    show scott at shake:
        yoffset 0

    s frowntalk "A madam's brooch? Heavens no!"
    s frowntalk "I may have mood swings but adultery has never crossed my mind!"

    show scott frown

    n frowntalk "The woman who owned this isn't alive."

    show nemo frown

    s frowntalk "Isn't alive...?"
    show scott at shake
    s frowntalk "N-Now I know I was out of it when the urge for blood hit me, but I swear I haven't killed a soul!"

    show scott frown

    n frowntalk "Where were you residing 10 years ago?"

    show nemo frown

    s frowntalk neutral "10 years ago? I was living in Cresedina, working with another professor there."
    s frowntalk "Who's brooch is this?"

    show scott frown

    nn eye2 arm2 "Cresedina... That's a coastal town several hours away by train."

    n frowntalk eye1 "You didn't come here at all?"

    show nemo frown arm1

    s frowntalk "My first time in Lauremburg was 8 years ago. I was touring the university after I'd been offered a job here."

    show scott frown

    n eye2 arm2 "..."

    nn eye3 "I wanted to keep my distance from this. It's Lucie who needs closure, not me."
    nn eye2 "So, I ignored it."
    nn "I ignored the doubt in the back of my mind as well."
    nn eye3 "But now... Now it will consume her even further."


    stop music fadeout 3









    $ save_name = "Apologies"
    $ chapter_num = "Twenty-Three"

    call chapter from _call_chapter_22

    $ nemopov = False
    $ cecilpov = True

    scene bg college1:
        zoom 0.65
        yalign 0.65
        xalign 0.5
    show cecil down frown arm3 at side
    with fade

    play music "audio/Isolation Waltz.mp3" fadein 2
    queue music "audio/Isolation Waltz.mp3"


    show bg college1 at shake

    cn "I can't believe it! Not nary a bit!"
    cn "I can't believe I'm back in Lauremburg. I can't believe Lucie ran off again on her own."
    show bg college1 at shake
    cn arm2 "And most of all... I can't believe I'm looking for her all over again!"
    cn eye2 "What does she call herself doing, running off again without telling me?"
    cn unsure arm3 "She'd better be here, too! If she's not... well... it's going to be a pain, that's for sure!"
    cn eye3 "It's going to be a real big pain if Annie finds me, too... She can't be too far behind."
    cn scared eye1 "Why did Lucie come back here to begin with...?"

    c eye2 "..."

    cn arm1 "I don't have any clues to go off of, but... he might. It'll be real unlucky if he's left town, though..."
    cn down smile eye1 "I think Mr. Ambrose's place was this way. I'm sure I'll find it before sunset!"

    show cecil up frown

    n "Well, well. Look what the cat dragged in."

    show nemo up frown at center with dissolve

    c shock "...!"
    c frowntalk arm2 "N-Nemo!"

    show cecil frown arm1

    n frowntalk "Hi, Cecil."

    show nemo smile

    c scared eye2 "..."

    cn "I left after yelling at him and didn't say anything else."
    cn "No goodbye."
    cn "No thank you."
    cn eye3 "Nothing."
    cn eye2 "And yet, now I'm back, asking for help again."

    c frowntalk "I-I..."
    c frowntalk eye5 "I just wanted—I mean, I was thinking—w-well, I wanted... to say..."
    c frowntalk crying "That... uhm..."

    show cecil frown

    nar "He puts a hand on my head."

    n frowntalk "It's okay."

    show nemo smile

    c "..."


    scene cg cecilhug:
        zoom 0.78 yalign 0.8 xalign 0.5
    with Dissolve(0.5)

    c "I'm sorry...!"
    c "I said all those things I didn't mean... and I didn't even thank you for helping me..."
    c "I wouldn't have made it here without you. I never would have found Lucie."

    n "And now you're back here alone, looking for her?"

    c "I'm sorry..."
    c "You were just trying to help us, and I...!"

    scene cg cecilhug2:
        zoom 0.78 yalign 0.8 xalign 0.5
    with Dissolve(1.1)

    n "It's okay."
    n "But you can't keep sneaking out and running off, alright?"

    $ achievement.grant("apologize")
    init:
        $ achievement.register("apologize")
        $ achievement.sync()
    $ achievement.sync()

    c "Okay..."

    n "You're trying to find Lucie, aren't you?"

    c "Mhmm..."

    n "Alright, let's go to her."

    scene bg college1:
        zoom 0.65
        yalign 0.65
        xalign 0.5
    show cecil up crying at side
    show nemo up smile at center:
        zoom 1.15
    with dissolve

    c frowntalk "Huh?"

    show cecil frown

    n frowntalk "Unless she ran off, she should be sitting in Ambrose's parlor."
    n frowntalk eye2 surprise "'Course, knowing her she might already be halfway to Timbuktu by now."

    show nemo frown

    c shock arm2 -crying "Sh-She's there?! Then where're you coming from?"

    show cecil frown arm1

    n frowntalk eye1 up "The jail."

    show nemo frown

    cn frown unsure eye3 arm3 "He finally got caught, didn't he?"

    show cecil down eye1
    show nemo at shake

    n frowntalk down "Quit lookin' at me like that!"
    n frowntalk arm2 eye2 "I was visiting Scott."

    show nemo frown

    c frowntalk surprise "Scott...?"

    cn frown neutral eye2 "Oh... Was that the professor?"
    cn frown scared "Wait, why would he want to see him...?!"

    show cecil eye1 neutral

    n frowntalk eye3 up "Lucie was asking me about this."

    show nemo frown eye1 arm1 at curtsy

    nar "He pulls out a fancy looking brooch with the Fleur insignia on it."

    c frowntalk surprise "Isn't that...?"

    show cecil frown

    n frowntalk eye3 "It's the brooch she found on him."
    n frowntalk eye2 "Something's not sitting right with her about it."

    show nemo neutral

    c frowntalk "Like what?"

    show cecil frown

    n frowntalk eye1 up "...Let's save that for when we get back, okay?"

    show nemo smile at curtsy
    show bg college1 at curtsy

    c talk arm2 up "Okay!"

    show cecil smile arm1

    nar "We walk through the same courtyards on campus as we had a month prior, the only noticeable difference being fewer guards present."

    n talk arm2 "What've you been up to since you went home?"

    show nemo smile

    c frowntalk arm3 eye2 down "Schoolwork..."

    show cecil frown

    n grin eye3 "Hah, don't sound so glum! There's a lotta orphans out here who'd kill to learn how to read."

    show nemo smile eye1

    c frowntalk "Reading's one thing, but math's a whole beast..."

    cn frown up eye1 "Wait... He's an orphan..."

    c frowntalk arm2 "Do... Do you know how to read?!"

    show cecil frown
    show nemo at shake

    n frowntalk eye4 down "O-Of course I do!"
    n frowntalk eye5 "...The sailors I worked with taught me a little bit so I'd be able to read maps and signage without asking so many questions. I picked up the rest when I taught Lucie."

    show nemo frown

    c talk "Oh... Good!"
    show nemo eye1 up arm1
    c frowntalk arm3 "I've been doing a lot of schoolwork and playing with Lucie."

    show cecil smile

    n frowntalk "And...?"

    show nemo frown

    c frowntalk surprise "And?"

    show cecil frown

    n frowntalk surprise "That's it?"

    show nemo frown

    c frowntalk "Yes?"

    show cecil frown

    n frowntalk "Haven't been nowhere?"

    show nemo frown

    c frowntalk "No, of course not."
    c frowntalk unsure eye2 "Father was really mad I ran away, so I was grounded."
    c frowntalk up eye3 "I hadn't any plans for traveling anyway."

    show cecil frown

    n frowntalk "What's he going to think about this stunt?"

    show nemo frown

    c eye1 talk arm2 "It's my rebellious phase!"

    show cecil smile

    n frowntalk "Of course..."

    show nemo frown
    stop music fadeout 1

    annie "This is your rebellious phase, is it?"

    play music "audio/Asking Questions.mp3" fadein 2
    queue music "audio/Asking Questions.mp3"

    show nemo:
        ease 0.8 zoom 1.0 xalign 1.5
    pause(0.2)
    show annie frown down:
        zoom 0.75 xalign -0.5 alpha 0.0
        ease 1.0 xalign 0.2 alpha 1.0

    c frowntalk "A-Annie!"

    cn frown arm3 scared eye2 "Darnit, how'd she find me this fast?!"

    n frowntalk up "Good evening."

    show nemo frown
    show annie at shakeslow

    annie frowntalk "And who is this... {i}acquaintance{/i} of yours, Cecil?"

    show annie frown

    c frowntalk arm2 up eye1 "He's Lucie's brother! He lives here."
    c frowntalk arm1 "Lucie and I came to see him!"

    show cecil frown

    annie frowntalk "All on your lonesome?"

    show annie frown

    c frowntalk down "...Yes, all on our own!"
    c frowntalk arm3 "You lot would never let us come all the way out here, even chaperoned!"
    c frowntalk eye2 "You'd just tell me no and that'd be the end of the story. What good is sitting at home all day going to do me?"

    show cecil frown eye1
    show nemo surprise eye2

    nar "Nemo mutters something along the lines of \"what good'll you be if you're kidnapped\", but it's out of earshot of Annie."

    c frowntalk unsure arm1 "I want to help Lucie with this one last thing. Then we'll come home."

    show cecil frown

    annie eye2 "..."
    annie frowntalk eye1 "And you're really Lucie's brother?"

    show annie frown

    n frowntalk eye1 up "Yes, ma'am. I moved out of the estate a while back to make my own living here."
    n frowntalk eye3 "Lucie left home to come visit me... I'm sorry for the trouble she's caused you. I'm going to talk to Leland about them being here."

    show nemo frown eye1

    cn smirk arm2 "I think I'm starting to see the appeal to lying!"

    annie frowntalk "...Do you at least have your pills?"

    show annie frown

    c frown eye5 arm3 "..."

    show cecil frown

    annie frowntalk "You forgot them, I know."

    show annie frown

    cn frown "I'm fine without them... It's almost like she's trying to embarrass me in front of Nemo."

    show annie:
        ease 1.0 zoom 1.0 yoffset -120
        linear 0.2
        ease 0.4 yoffset -60
        ease 0.25 yoffset -120
        linear 0.1
        ease 0.7 zoom 0.75 yoffset 0

    pause(2.7)

    nar "She pulls out a small container and hands it to me. I begrudgingly take it."

    annie up frowntalk "I'll be staying at an inn nearby, so telegraph the lobby if you need anything. I expect to hear from you sometime before the week is over, whether it's just checking in or that you're ready to leave."
    annie down "There had better be at least a pill or two missing from that bottle by the end of the week or your father will have my head. And I don't mean throwing them out, they're too expensive for that."

    show annie frown

    c frowntalk down "I understand..."

    show cecil frown

    annie frowntalk "Be on your best behavior. And remember..."
    annie "This'll be your last vacation on your own."

    show annie frown

    stop music fadeout 3

    pause(0.5)


    hide annie with dissolve

    pause(0.5)

    show nemo at center with ease

    n frowntalk surprise "...Some maid, huh?"

    show nemo frown

    c frowntalk eye4 arm2 "Don't tell me you fancy her!"

    show cecil frown
    show nemo at shake

    n frowntalk down "Are you that daft?!"

    show nemo frown

    pause(0.3)


    scene bg garden:
        zoom 0.7
        yalign 0.6
        xalign 0.5
    show cecil up frown at side
    with sidefade

    play music "audio/Isolation Waltz.mp3" fadein 2
    queue music "audio/Isolation Waltz.mp3"

    cn eye2 "Not much has changed to the campus since I was last here. ...It's a bit comforting, actually."
    cn smile eye1 "I should show Lucie around while we're here."
    cn frown arm2 scared "Wait! Is she okay to walk around during the day willy-nilly? Ambrose always carries a parasol with him to keep the sun out."
    cn frown arm3 eye2 "Lucie's never been one to play outside for long, either. I can't just drag her around in the sunshine."

    show nemo up frown arm2 at center with dissolve

    c frowntalk eye1 up "...Say, Nemo."

    show cecil frown

    n "Hmm?"

    c frowntalk neutral "What d'you think of Lucie being a vampire?"

    show cecil frown

    n frowntalk eye2 down "...I hate it."
    n frowntalk eye3 "I know she agreed to it, but... she's just too young."

    show nemo frown eye2

    c frowntalk surprise "But she agreed to it, didn't she?"

    show cecil frown

    n frowntalk eye1 "I know you might think you're a good judge of yourself, but trust me, you're not at your age."
    n frowntalk "Kids shouldn't be allowed to make life-changing, irreversible decisions. The only choices kids make should be who they want to play with that day."

    show nemo frown

    c frown eye2 down "Hmph!"

    n frowntalk eye3 "Maybe she'll regret it, maybe she won't. But she should at least have a way to reverse it."

    show nemo frown

    cn frown neutral eye1 "A way to reverse it..."

    stop music fadeout 3









    $ save_name = "Clover"
    $ chapter_num = "Twenty-Four"

    call chapter from _call_chapter_23

    $ nemopov = True
    $ cecilpov = False

    scene bg hallway1:
        zoom 0.8
        xalign 0.5
        yalign 0.65
    show nemo pink up frown at side
    with fade


    play music "audio/Winter.mp3" fadein 4
    queue music "audio/Winter.mp3"

    nar "We walk down the familiar corridor to my home. The sun is setting fast outside."

    nn eye2 "I can't say I'm surprised by the audacity of these kids, but damn, can't they sit still for 5 minutes?"
    nn "If I'm surprised at anything, it'd be that Cecil got here all on his own this time. Maybe he did pick up a thing or two with me."
    nn surprise eye3 "...He got here because of things I taught him... Does that make me a bad influence...?!"


    scene bg office2:
        zoom 0.4
        yalign 0.7
        xalign 0.5
    show nemo pink up frown at side
    show cecil pink up frown at left:
        zoom 0.8 yoffset 100 xalign 0.05
    with sidefade

    show lucie pink up frown behind cecil at center:
        zoom 0.8 yoffset 110 xalign 0.4
    show ambrose pink up smile at right:
        zoom 1.1 xalign 2.75 yalign 0.13
    with dissolve

    show cecil:
        ease 0.4 yoffset 120
        ease 0.3 yoffset 70
        repeat

    c talk arm2 "Lucie!"

    show cecil smile:
        ease 0.4 yoffset 100
    show lucie at shake

    l frowntalk unsure "Cecil?!"

    show lucie frown

    n frowntalk arm2 "Wow, you're still here."

    show nemo arm1

    a frowntalk unsure "How do you keep running into each other?"

    show ambrose smile
    show lucie at shakeslow

    l grimace "D-Did you really follow me back here...?!"

    show lucie frown

    c down frowntalk arm3 "Of course! You never run anything by me first!"

    show cecil smile up

    n frowntalk "I mean, you shoulda guessed he'd follow you again."

    show nemo frown

    l eye5 down "..."
    show lucie at shake
    l grimace "J-Just don't get lost again!"

    show lucie frown

    nn surprise eye2 "I could say that to both of you."

    show cecil arm1
    n frowntalk up eye1 "...Hey, Cecil."
    show ambrose frown
    n frowntalk "Can I see that pill bottle your maid handed you?"

    show nemo frown

    c talk eye3 "Sure, you can take 'em too if you want!"

    show cecil smile eye1:
        ease 1.3 zoom 1.2
        linear 0.2
        ease 0.4 yoffset 160
        ease 0.25 yoffset 100
        linear 0.15
        ease 1.0 zoom 0.8

    pause(2.5)

    nar "He hands me the semi-opaque pill bottle."

    l frowntalk eye1 unsure "You ran into Annie?"

    show lucie frown
    show cecil at shake

    c frowntalk down arm2 "Yes, she somehow already caught up to us!"

    show cecil frown arm3

    a frowntalk eye2 "I don't think the \"somehow\" is much of a question."

    show ambrose frown
    show cecil neutral
    show lucie up

    nar "I let a couple of the pills spill into my open palm."
    nar "They're medium-sized and hard."
    show ambrose eye1

    show lucie:
        ease 1.0 zoom 1.0
    show cecil arm1:
        ease 1.0 zoom 1.0

    pause(0.7)

    l frowntalk "I always thought they looked like gummies, but they're rather hard, aren't they?"

    show lucie frown

    c frowntalk eye3 "If you tried to chew on them, you'd break your teeth."

    show cecil eye1 frown

    nn down "They're hard, sure, but the weirder thing... The \"pills\" are a bright, somewhat transparent green."

    n frowntalk "...Ambrose, put on your gloves and tell me what you think."

    show nemo frown

    show ambrose glove with Dissolve(0.5)

    a up "..."
    a unsure frowntalk "Are these...emeralds?"

    show ambrose frown

    c frowntalk surprise arm3 "Emeralds?"

    show cecil frown

    n frowntalk "Looks like 'em, doesn't it? They're too dark to be peridot."

    show nemo frown
    show ambrose -glove with Dissolve(0.5)

    nar "Ambrose hesitantly slips a glove off."

    show ambrose down frowntalk at shake
    with greenlight

    a frowntalk "—!"

    show ambrose frown

    nn "As expected... There was a reaction to him touching them."

    a frowntalk "These... They're definitely gems."

    show ambrose frown
    show cecil at shakeslow

    c frowntalk scared arm1 "What...?"

    show cecil frown

    n frowntalk "Your maid didn't hand you the wrong bottle, did she?"

    show nemo frown

    c frowntalk eye2 "No... Those are my typical pills."
    c frowntalk "I take one every week or so. Father gets mad when I slack off."

    show cecil frown

    nn arm2 "Now, why would a parent make their kid eat gems...?"
    nn eye3 "This doesn't seem to be something the maid could do alone- it's not like she has a reason, either."
    nn eye2 "His father is some kind of jeweler, right? That's got to be where the gems are coming from."
    nn "But why...?"

    n eye1 "..."
    n frowntalk arm1 "Ambrose, touch his hand. Without your glove."

    nn frown surprise eye2 "I might be sleeping on the couch after this, but it'll help confirm something."

    show nemo eye1 down

    show ambrose at shake
    show cecil eye1 at shake
    with greenlight

    a frowntalk down "—!"

    show ambrose frown

    nn "The same spark of light that happened in that alleyway and with that old man flashes brightly."

    show ambrose sad

    n frowntalk "This is what happens whenever you touch a vampire, doesn't it?"

    nn frown eye2 "Lucie's playing a \"proper lady\" now, so she must wear her gloves all the time."

    show nemo eye1

    c frowntalk "Wh..."
    c frown "..."
    c frowntalk eye2 arm3 "...This is from the pills I'm taking?"

    show cecil frown eye1

    n frowntalk up "Most likely, yes."
    n frowntalk arm2 eye2 "I've never heard of anyone swallowing gems like this, but if you've been taking these for years... Well, that's the only reason for the reaction you have to touching vampires that I can think of."

    show nemo frown eye2 arm1

    c eye2 "..."

    nn surprise eye2 "I told his maid I'd return them both home as soon as possible..."
    nn down "But is that the safest option for them?"

    show nemo up eye1 arm1

    l frowntalk up eye3 "Don't take 'em."
    l frowntalk eye1 "They don't look like they taste good. So don't take anymore of 'em."

    show lucie frown

    nn surprise eye2 arm2 "I'm glad she's grown up to be a doctor..."

    n frowntalk up eye1 arm1 "Do you want me to hold onto them for now?"

    show nemo frown

    c "..."
    c frowntalk eye3 arm1 "Yes."

    show cecil frown eye2

    nn eye2 "Sounds like I have another question for Scott. That can wait until tomorrow, though."

    show nemo eye1

    nar "Cecil slumps on the couch beside Lucie."

    nn eye3 "Not a whole lot he can do right now except think about it."

    show nemo eye1
    show lucie:
        ease 1.0 zoom 1.1 xalign 0.8
    show ambrose:
        linear 0.5
        ease 0.7 xalign 3.0
    pause(0.8)
    show cecil behind lucie
    show lucie:
        ease 1.0 zoom 1.2 xalign -0.25
    pause(0.8)
    show ambrose behind lucie

    pause(0.1)

    l frowntalk up eye1 "What'd that lout say?"

    show lucie frown

    n eye2 arm2 down "..."

    nn "Lies aren't going to cut it anymore."
    nn eye3 "Anything Leland and I try to tell her just to please her, she'll see through."

    n frowntalk eye1 arm1 "He admitted to most of the campus attacks."
    n frowntalk eye3 "The brooch, however... he doesn't remember. He doesn't know how it ended up on his person."

    show nemo frown eye1

    l down eye2 "..."
    l frowntalk eye1 "What about the murders?"

    show lucie frown

    n frowntalk eye2 "...The first time he came to town was half a decade ago, when he was touring campus."
    n frowntalk "At least, that's what he told me."

    show nemo frown down eye1

    l eye2 "..."

    n frowntalk down arm2 eye3 "...If you wanted someone to ask for his alibi, you could have just telegraphed."
    n frowntalk arm1 eye1 "What really brought you out here again?"

    show nemo frown

    l sad "..."
    l frowntalk "I... I thought that the brooch looked similar to one I saw months ago in a guest room... But when I went back to look for it, it was gone..."
    l eye1 "But that brooch must have just looked similar, right?"
    l "My mother owned multiple similar looking brooches, and this one has been with Scott the entire time, right?"

    show lucie frown

    n unsure eye2 "..."

    nn down eye3 "Dammit Leland, when I said catching the guy wouldn't be enough to give her closer, this isn't what I meant!"

    n frowntalk up eye1 arm1 "...I'll figure it out. It'll be alright."
    n talk "For now, though, it's time to eat. And after that it's your bedtime."

    show nemo smile
    show lucie up:
        ease 0.7 xalign 0.2
    pause(0.3)
    show cecil up smile eye1:
        ease 0.8 zoom 1.2 xalign -0.3
    pause(0.66)
    show lucie behind cecil:
        ease 0.7 xalign -0.25
    show cecil:
        ease 0.4 yoffset 160
        ease 0.35 yoffset 100
        repeat

    c talk up eye1 arm2 "Food!"

    show cecil smile

    l down grimace eye2 "Bedtime..."

    show lucie frown

    stop music fadeout 3









    $ save_name = "Midnight Rendezvous"
    $ chapter_num = "Twenty-Five"

    call chapter from _call_chapter_24

    $ nemopov = False
    $ cecilpov = True

    scene bg cecilbedroom night:
        zoom 0.8
        yalign 0.6
    show cecil night up frown eye1 at side
    with fade



    play music "audio/Isolation Waltz.mp3" fadein 2
    queue music "audio/Isolation Waltz.mp3"

    cn surprise "Where did Lucie go?"
    cn eye2 neutral "I thought I'd seen all of the apartment when I was here before, but some parts feel completely new."
    cn eye1 "Lucie definitely hasn't gone to bed just yet, so maybe she's..."


    scene bg city2:
        zoom 0.65 xalign 0.6 yalign 0.0
    show cecil night neutral frown at side
    show lucie night eye2 frown at center:
        yoffset 50
    with sidefade

    cn "Here."

    nar "Lucie has a blanket draped around her as she sits on the balcony, looking down at the street below."
    nar "By now, the street lamps are on and most people are on their way home."
    show lucie eye1:
        ease 1.0 zoom 1.15
    show bg city2:
        ease 1.1 zoom 0.75
    nar "I sit beside her."
    nar "There's a nice, cool breeze in the air. Summer is coming to a close and autumn is about to begin."

    c frowntalk "Have you been here before? To the city, I mean."

    show cecil frown

    l frowntalk "A few times."
    l frowntalk eye2 "Nemo liked to travel a lot and bounced from job to job."
    l frowntalk "Some of them wound us up back here."
    l frowntalk eye3 "At one point I worked under a seamstress in town. I'd get the creases out of her fabric, rearrange her lace, thread the needles, whatever she needed."

    show lucie frown eye1

    c frowntalk "Did you like it?"

    show cecil frown

    l frowntalk "Work is work."
    l frowntalk eye2 "...It was an easier job than most, that's for sure."

    show lucie frown

    nar "Lucie's gaze stays on the horizon."

    cn frown scared "That brooch is eating away at her, isn't it?"
    cn frown eye2 "Mr. Leland must have told her to stop worrying about it when she asked him, so she came all the way here for answers."
    cn frown eye3 "...Or worse, she felt she couldn't trust his answer and didn't even ask."
    cn frown eye1 "To come all the way here again, but seek out Nemo this time..."

    c frowntalk "Lucie... Do you really hate Nemo?"

    show cecil frown

    l frowntalk down "He lied to me."
    l frowntalk "He told me my parents died—"

    show lucie frown

    c frowntalk down arm3 "That's not what I asked."
    c frowntalk "Do you hate him?"

    show cecil frown
    show lucie at shakeslow

    l frowntalk "...He lied to me, Cecil."

    show lucie frown

    c frowntalk "When I met him, he said he's looking for a cure to vampirism. That's why he came back here."
    c frowntalk neutral "He's looking for it for you, isn't he?"

    show cecil frown
    show lucie at shake

    l grimace "H-He just wants to sell it once he finds it!"

    show lucie at shake
    show bg city2 at shake

    c frowntalk down arm2 "No, he doesn't!"
    c frowntalk "It's for you!"

    show cecil frown

    l crying sad "..."

    show cecil arm1

    nar "Lucie pulls out her atrocious teddy bear head and holds it close to her."

    cn frown unsure "That thing has to be several years old."
    cn frown "There's no way Mr. Leland bought that for her."

    show lucie sobbing with dissolve

    l "Why did he lie?"

    show lucie frown

    c scared "..."


    cn frown eye3 "Seeing her like this now... It's obvious why."

    show cecil eye1

    l frowntalk "I just..."
    l frowntalk "I wish... I wish he didn't lie to me..."

    show lucie frown

    c "..."

    nar "I wrap my arms around her and pull her close."

    scene bg city2:
        zoom 0.75 xalign 0.6 yalign 0.0
    with dissolve

    pause(0.5)

    stop music fadeout 3









    $ save_name = "Emerald"
    $ chapter_num = "Twenty-Six"

    call chapter from _call_chapter_25

    $ nemopov = True
    $ cecilpov = False

    scene bg city4:
        zoom 0.55
        yalign 0.65
        xalign 0.5
    show nemo up frown eye3 at side
    with fade



    nar "Just like yesterday, I cross the street and approach the jailhouse."

    scene bg police:
        zoom 0.6 xalign 0.5 yalign 0.75
    show nemo police up frown eye3 at side
    with sidefade

    play music "audio/Asking Questions.mp3" fadein 4
    queue music "audio/Asking Questions.mp3"

    nn eye2 arm2 down "Back here again... This is {i}not{/i} going to become a regular occurrence for me."
    nn eye3 "I just need another answer."
    nn eye2 arm1 "No, that's not it. I can only think of one reason why his parents are giving him emeralds. I just want Scott to tell me I've gone mad and it's not something so sinister."
    nn "Coming all the way out here again in the hopes of hearing someone tell me I'm wrong..."
    nn eye3 smile "Heh, maybe I did rub off on Lucie too much."


    show nemo eye1 frown up
    show scott police down frown nogood at center:
        zoom 0.8 xalign 0.6
    with dissolve

    s frowntalk "Again?"

    show scott frown

    n talk "Cheer up, I brought you a luncheon plate!"
    n arm2 "It wasn't exactly easy getting this in, y'know."

    show nemo smile arm1

    s frowntalk unsure "And what's in it for you?"

    show scott frown

    n talk "Can't I bring a former colleague a warm meal?"
    n grin "And ask him a couple easy questions while he eats?"

    show nemo smile

    nar "The guard opens the container to inspect the meal before handing it to him."

    s frowntalk up "...Alright, go for it."

    show scott frown

    n eye3 talk "It's an easy question, don't worry."

    show nemo frown eye1

    nar "I pull out the pill bottle and hand it to the guard to give to him."

    n frowntalk "What do you make of this?"

    show nemo frown

    s unsure "..."

    nar "A true scholar, he doesn't blurt out the obvious and instead inspects it carefully first."

    s frowntalk up "A vial of emeralds, eh?"
    s frowntalk "They could be fashioned into rings, I suppose. I'm not one to understand jewelry but these look high grade."

    show scott frown

    n frowntalk "What do you think would happen if you swallow one?"

    show nemo frown

    s frowntalk unsure "Swallow one...?"
    s eye2 "..."
    s frowntalk eye1 neutral "It could possibly be a cure to vampirism."
    s "Gems this high grade aren't easy to come by, that's for sure."

    show scott frown

    n frowntalk "What if you're not a vampire?"

    show nemo frown

    s frowntalk unsure "Swallowing gems willy-nilly?"
    s frowntalk "What are you getting at, kid?"

    show scott frown

    n frowntalk eye2 surprise arm2 "...Hear me out, this sounds far-fetched but just listen."
    n frowntalk eye1 "I got this vial from a kid whose parents told him to take 'em. He's definitely human, unless he somehow has amnesia of getting bitten or something."
    n frowntalk arm1 "I wanted your opinion on why they'd do that."

    show nemo frown

    s frowntalk "...What kind of business are you messing in?"

    show scott frown

    n frowntalk down "It's from my little sister's friend, now answer the question."

    show nemo frown
    show scott eye2

    nar "He grunts and settles down in his chair, thinking it over."

    s frowntalk down "Well... There's still folks out there who have an ingrained hatred for vampires."

    show scott frown eye1

    nar "He eyes me before continuing."

    s frowntalk "For some, it's personal... For others, it's a generational, family thing."
    show nemo eye2
    s frowntalk "Blazes, I imagine some chaps have some kind of superiority complex over us."
    s frowntalk eye2 "I had a lad in my morning class a couple years ago who wouldn't look me in the eyes."

    show scott frown

    nar "For some reason, I can't meet his gaze right now either."

    s frowntalk "I imagine his parents think along the same lines."
    s frowntalk "To keep themselves—or just the kid—from becoming a vampire."

    show scott frown

    stop music fadeout 2

    pause(0.5)


    scene bg hallway1:
        zoom 0.8
        xalign 0.5
        yalign 0.65
    show nemo pink down arm2 eye2 frown at side
    with fade

    n "..."

    nn "To hate vampires that much..."
    nn arm1 "...No, it doesn't matter. There's no good reasoning behind poisoning your kid."
    nn sad "With Lucie's trust in Leland wavering, maybe... Maybe it's best if they don't go home."


    scene bg office2:
        zoom 0.4
        yalign 0.7
        xalign 0.5
    show nemo pink up frown eye3 at side
    with sidefade

    n frowntalk "I'm home—"

    show nemo frown eye1 surprise

    show cecil pink scared frown arm2 at center:
        zoom 1.4
    with hpunch

    play music "audio/Ambush in Rattlesnake Gulch.mp3" fadein 2
    queue music "audio/Ambush in Rattlesnake Gulch.mp3"

    c frowntalk "NEMO!!"

    show cecil frown

    n "—?!"
    n frowntalk "What's with you? Calm down, what's wrong?"

    show nemo frown

    c frowntalk "Lu... Lucie..."

    show cecil frown

    nn eye2 "Oh no."

    n frowntalk eye1 "Did she run off again?"

    show nemo frown

    c frowntalk eye3 "N... No..."

    show cecil frown

    nar "I look around. Ambrose must have gone to work already."

    c frowntalk eye1 "Mister... Leland..."

    show cecil frown

    n frowntalk "Leland?"
    n frowntalk "Wait, was Leland here?"

    show nemo frown
    show bg office2:
        ease 1.0 zoom 0.5 xalign 0.65

    pause(0.8)

    nar "I lead Cecil over to a chaise lounge, but he's hesitant to sit down."
    nar "He clings to my sleeve."

    c frowntalk eye2 "I tried to stop him..."

    show cecil frown

    n frowntalk "What did Leland do?"

    show nemo frown

    c frowntalk eye1 "Mister Leland... He took Lucie home...!"

    show cecil frown

    stop music fadeout 3









    $ quick_menu = False

    scene black with fadee

    show text2 "15 Minutes Prior":
        alpha 0.0 xalign 0.5 yalign 0.41
        linear 1.0 xalign 0.5 yalign 0.48 alpha 1.0

    pause(2)

    $ save_name = "Doll in Distress"
    $ chapter_num = "Twenty-Seven"

    call chapter from _call_chapter_26

    $ nemopov = False
    $ cecilpov = True

    scene bg office2:
        zoom 0.4
        yalign 0.7
        xalign 0.5
    show ambrose pink up smile glass glove at right:
        yalign 0.13
    show lucie pink up frown behind ambrose at left:
        yoffset 120 xalign 0.0
    show cecil pink up frown at side
    with fade



    play music "audio/Isolation Waltz.mp3" fadein 2
    queue music "audio/Isolation Waltz.mp3"



    a frowntalk eye3 "I've got a meeting to attend to in half an hour, so I'd best be on my way."
    a frowntalk eye1 "Nemo will be back soon. Don't have us running around campus again, please."

    show ambrose frown
    show lucie pout eye2 down:
        easein 0.25 xoffset 11
        easein 0.35 xoffset -12
        easein 0.25 xoffset 8
        easein 0.35 xoffset -16
        easein 0.25 xoffset 12
        easein 0.35 xoffset -11
        easein 0.25 xoffset 7
        easein 0.35 xoffset 0

    nar "Lucie grumbles something and pokes at Teddy."

    c talk arm2 "We won't, especially not without the cookies Miss Marybelle made!"

    show cecil smile arm1

    show ambrose eye3 behind lucie:
        ease 1.5 xalign -1.5 alpha 0.0

    pause(1.25)

    nar "Mr. Ambrose sighs and walks out the door."
    show lucie frown:
        ease 0.9 zoom 0.75
        linear 0.2
        ease 0.4 yoffset 170
        ease 0.3 yoffset 100
        ease 0.4 yoffset 135
    pause (2.0)
    nar "Lucie slumps back in her chair, unperturbed by her own unladylike slouch."

    c neutral frown "..."

    cn surprise eye2 "What do I do now...?"
    cn frown "Nemo might be a while and Mr. Ambrose has work to do, so we're all alone again for a couple hours."
    cn frown unsure "Annie {/i}shouldn't{i} come looking for me again so soon after giving her blessing to Nemo, but if we stay here too long she'll definitely be dragging me home."
    cn frown neutral "But, the reason we're here..."

    c frowntalk eye1 "Why didn't you want to ask your uncle about the brooch?"

    show cecil frown

    l frowntalk down eye3 "...You really are dense sometimes..."

    show lucie frown at shake
    show bg office2 at shake

    c frowntalk down arm2 "What's that supposed to mean?!"
    show lucie eye1
    c frowntalk arm3 neutral "...You think it was a fake or planted or something. But you didn't even try to ask him, did you?"

    show cecil frown

    l frowntalk eye3 "It would've just been more lies compounded upon one another."
    l frowntalk eye2 "...Sit down. You're making me antsy, pacing around like that."

    show lucie frown

    c "..."

    show cecil frown


    show bg office2:
        ease 1.5 zoom 0.6 xalign 0.3 yalign 0.6
    show lucie frown:
        ease 1.2 zoom 1.2 xalign -0.25
    pause(1.2)
    show bg office2 at curtsy
    show lucie:
        ease 0.4 yoffset 130
        ease 0.3 yoffset 110
    pause(0.75)
    show cecil neutral frown

    nar "Now that I'm closer, I notice in her lap is a small sewing kit. She delicately threads a needle and starts repairing a small tear in Teddy."

    l frowntalk "I don't want to go home for a while."

    show lucie frown

    c frowntalk surprise "Huh? Why?"

    show cecil frown

    l frowntalk "They're all the same."
    l frowntalk "They all think they're protecting me by lying."
    l grimace "Why is that their first go-to?! To act like I can't handle anything?!"

    c frowntalk down "And running away will solve it?"

    show cecil frown
    show lucie at shake

    l eye1 "—?!"

    cn frown scared eye2 arm1 "I-I accidentally said the first thing that came to mind again—!"
    cn frown arm3 unsure "But... It's something that needed to be said."

    nar "Lucie's stare is sharper than her sewing needle."

    show lucie at shake

    l frowntalk "What... What do you know...!"

    show lucie frown at shake
    show bg office2 at shake

    c frowntalk down arm2 eye1 "I know Mister Leland and Nemo aren't bad people and care about you! But you don't talk to them when there's a problem, you just run off!"
    c frowntalk "Whenever you find out they've lied to you, you just tail it and make everyone worried!"

    show cecil frown arm3
    show lucie at shakeslow

    l frowntalk sad eye3 crying "I-I... I don't..."

    show lucie frown eye2

    c frowntalk arm2 "Yes you do! Everyone was so worried when you ran off on your own!"
    c frowntalk arm1 "Even Nemo was worried when he found out, but you don't care!"

    show cecil frown
    show lucie down grimace eye3 at shake

    nar "Lucie throws Teddy to the ground."

    show lucie at shake

    l frowntalk eye1 "Don't tell me what I care about!"

    show lucie frown

    c frowntalk "Then act like you care!"
    c frowntalk "Stop trying to get back at them by making them worry!"

    show cecil frown

    l grimace eye2 "...!!"
    show lucie at shakeslow
    l sad frowntalk "..."

    show lucie frown

    c scared "..."

    show bg office2 at curtsy
    show lucie:
        ease 0.4 yoffset 140
        ease 0.25 yoffset 110

    nar "I bend down and pick up Teddy."

    c frowntalk "We can work things out together, but not if we're apart."
    c frowntalk "You don't have to throw yourself in danger. We want to help you."

    show cecil frown

    l "..."

    show cecil smile
    show lucie:
        ease 0.4 yoffset 130
        ease 0.25 yoffset 110

    nar "She meagerly accepts Teddy back into her arms."

    cn frown scared eye2 "Maybe it is callous of me to think it, but... I can't help but wonder why she wants to catch her parent's killer."
    cn frown "Is it for revenge, or maybe to put her parents to rest?"
    cn frown arm3 "Or... Is it just a fixation for her?"

    c frowntalk eye1 "Lucie, do—"

    show cecil frown up arm1
    show lucie up frown -crying eye1

    stop music fadeout 3



    c frowntalk "Huh? Who's that?"

    show cecil frown

    l frowntalk "Maybe it's that busy woman."

    show lucie frown

    cn frown eye2 "I think she means Miss Marybelle."
    cn frown eye1 neutral "Whoever it is hasn't walked in yet, so it's definitely not Nemo or Mr. Ambrose."

    c talk "Coming!"

    show cecil frown

    play music "audio/Ambush in Rattlesnake Gulch.mp3" fadein 2
    queue music "audio/Ambush in Rattlesnake Gulch.mp3"


    show bg office2:
        ease 1.3 zoom 0.4
    show lucie sad:
        ease 1.1 zoom 1.1 xalign 1.0
    pause(0.8)
    show cecil scared
    show leland pink down frown at left:
        xalign -1.5 yalign 0.14 alpha 0.0
        ease 1.2 xalign -0.7 alpha 1.0
    pause(0.9)

    c frowntalk "Mr. Leland?!"

    show cecil frown
    show lucie at shakeslow

    l frowntalk "Wh... How did you find me?!"

    show lucie frown

    leland frowntalk "Come on. You're coming home."

    show leland frown:
        ease 0.6 xalign 0.2

    nar "Before I can protest, he's already cut the distance between himself and Lucie with a few long strides."

    show lucie at shake

    l frowntalk "W-Wait! I'm safe here, I'll be fine if I stay a few more days!"

    show lucie frown

    leland frowntalk "So now you think you're safe here? And what happens when you get snippy with that man and you leave on your own?"

    show leland frown
    show lucie eye2

    l frowntalk "I... I promise I won't leave here on my own..."

    show lucie frown

    leland frowntalk "Just like you promised me you'd not run away again?"

    show leland frown

    l "..."

    c frowntalk arm2 "Mr. Leland, please—"

    show cecil frown arm1

    leland frowntalk "I've heard enough. You can't keep doing this, Lucie. This is final."

    show leland frown:
        ease 0.2 xalign 0.4
    show lucie eye1:
        linear 0.23
        easein 0.12 xoffset 15
        easein 0.12 xoffset -15
        easein 0.12 xoffset 0

    nar "He snatches her wrist."

    leland frowntalk "Let's go home."

    show leland frown

    c frowntalk "Wait, Mr. Leland!"

    show cecil frown
    show lucie crying at shake

    l frowntalk "I don't want to! Please, just let me stay another night—!"
    l frowntalk "Please, wait—!!"

    show lucie frown:
        ease 1.2 xalign -3.3 alpha 0.0
    show leland:
        ease 1.0 xalign -3.0 alpha 0.0
    pause(1.5)



    nar "In less than a minute, Mr. Leland arrived and left with Lucie in tow."

    hide lucie
    hide leland

    cn frown "What do I do now...?"
    cn frown eye2 "Do I wait on Nemo? I don't know when he'll be back."
    cn frown "Do I go get Mr. Ambrose? He could be anywhere on campus."
    cn frown eye3 "I want to go after them, but... Mr. Leland is her legal guardian. The coppers certainly won't help."

    c eye2 crying "..."

    cn frown "Is there really nothing I can do to help her...? After coming this far?!"
    cn frown eye3 "All for naught..."

    c "..."

    cn frown "What would Nemo do if he was here?"
    cn down eye2 "Hmm... For starters, he wouldn't have let Mr. Leland leave without an argument."
    cn eye1 arm2 "He would've given him a run for his money! I bet he could talk the ear off a donkey!"
    cn scared arm1 "But... I'm not Nemo."

    c arm3 "..."

    cn eye3 "I'm not Nemo..."
    cn down eye1 arm2 "But that doesn't mean I can't try!"


    scene bg garden:
        zoom 0.7
        yalign 0.6
        xalign 0.5
    show cecil down arm2 frown at side
    with sideswipe

    cn frown "If I can find them, catch up with them, maybe..."


    scene bg college1:
        zoom 0.7
        yalign 0.8
        xalign 0.5
    show cecil down frown at side
    with sideswipe

    cn frown "Maybe...!"


    scene bg hallway1:
        zoom 0.8
        xalign 0.5
        yalign 0.65
    show cecil pink scared eye2 frown at side
    with sideswipe

    cn frown "Maybe..."


    scene bg college1:
        zoom 0.7
        yalign 0.8
        xalign 0.5
    show cecil scared eye3 frown at side
    with sidefade

    cn frown "Maybe I'll just get lost again and not find them..."
    cn frown eye2 "Right now would be a really good time to run into Nemo or Mr. Ambrose..."
    cn frown eye3 "Sigh... I suppose I'll return back to the apartment now."


    scene bg office2:
        zoom 0.4
        yalign 0.7
        xalign 0.5
    show cecil pink scared eye3 frown at side
    with fadee

    cn frown "This.. This really was the best I could do... run around in a bunch of circles, lose my breath..."
    cn frown "...And wait around for help."

    scene black with fadee


    scene bg office2:
        zoom 0.4
        yalign 0.7
        xalign 0.5
    show nemo pink frown eye1 surprise at center:
        zoom 1.2
    show cecil pink scared frown arm2 at side
    with hpunch

    c frowntalk "And that's what happened!!"

    show cecil frown

    n frowntalk eye2 arm2 "Y'know, you could have summarized for me..."
    n frowntalk eye1 arm1 down "Let's get going before they hop on a train."

    show nemo frown up:
        ease 1.3 xalign 4.0
    pause(0.8)
    show npcfem4 behind nemo:
        zoom 0.93 xalign -1.1 yalign 0.0 alpha 0.0
        ease 1.1 xalign 0.1 alpha 1.0
    pause(0.5)

    mary "What's all the commotion?"

    cn frown down arm3 eye2 "Oh, {/i}now{i} people want to come help!"

    n frowntalk "Did you see a gentleman come up here?"

    show nemo frown
    show cecil neutral eye1

    mary "No, but one of the tenants told me a young girl was arguing with her caretaker."
    mary "They were headed out the main door."

    n frowntalk eye3 down "No time to waste, then!"
    n frowntalk eye1 "Marybelle, tell Ambrose Leland's taking Lucie home. ...I know those names don't make sense, but he'll understand."

    show nemo frown
    show npcfem4:
        ease 1.0 xalign -1.1 alpha 0.0

    pause(0.6)

    nar "She scrunches her eyebrows at Nemo and leaves at a brisk pace."


    scene bg college1:
        zoom 0.7
        yalign 0.8
        xalign 0.5
    show cecil unsure frown at side
    show nemo down arm2 frown at center
    with sidefade

    n frowntalk "It's gonna be darn hard to reach her if they board a train."
    n frowntalk eye2 "The last train for the north might have left earlier today... but that might be too wishful thinking."

    show nemo frown eye1

    c frowntalk neutral arm3 "What'd you go off to do today?"

    show cecil frown

    n eye2 arm1 "..."
    n frowntalk eye1 "How do you feel about your parents?"

    show nemo frown

    c frowntalk surprise "Huh? What kind of question is that?"
    c eye2 unsure "...They're my parents."

    show cecil frown

    n frowntalk "When's the last time you saw 'em?"

    show nemo frown

    c frowntalk eye1 "I saw them when Mr. Leland, Lucie, and I went back. They were waiting for me at home and grounded me."
    c frowntalk "They left a few weeks ago for a trade deal somewhere far up north."

    show cecil frown

    n frowntalk "What about before that?"

    show nemo frown

    c frowntalk eye2 "...A few months."
    c frowntalk scared eye1 "Why?"

    show cecil frown

    n frowntalk "Speak of the devil and he shall appear..."

    show nemo frown:
        ease 0.8 xalign 1.3
    pause(0.5)
    show annie frown down:
        zoom 0.75 xalign -0.5 alpha 0.0
        ease 1.0 xalign 0.2 alpha 1.0
    pause(0.9)

    annie talk "It's time to go home, Cecil."

    show annie frown

    c "...!"

    cn frown eye2 "How does she keep finding me?!"
    cn frown "I guess we haven't strayed far from where she saw me yesterday..."

    show cecil eye1

    annie frowntalk "Mr. Leland had the common courtesy of informing me he and Lucie were heading home."
    annie "We should be on our way as well."

    show annie frown at shake
    show nemo at shake
    show bg college1 at shake

    c frowntalk arm2 "W-Wait...!"

    show cecil frown

    n frowntalk "Just a moment, ma'am."

    show nemo frown

    annie frowntalk "...What is it?"

    show annie frown

    n frowntalk "I was wondering what you knew about these."

    show nemo frown

    c frowntalk unsure arm3 "My pills...?"

    cn frown "I completely forgot I gave them to him last night."

    show annie at shakeslow

    annie frowntalk "They're his pills. Why, dare I ask, do you have them?"

    show annie frown

    n frowntalk eye2 arm2 "See, they don't exactly look like pills to me... and they certainly don't {i}behave{/i} like actual pills should."
    n frowntalk eye1 arm1 "So I was wondering if you could help me understand what they are."

    show nemo frown

    annie frowntalk "...Why do you have {i}his{/i} pills?"

    show annie frown

    n frowntalk "Are they actually pills?"

    show nemo frown

    annie frowntalk "You take one, put it in your mouth, and ingest it without eating it. I'd say that's a pill."

    show annie frown

    n frowntalk "If I take a rock, paint it green, and ingest it, wouldn't it be the same thing?"

    show nemo frown

    annie frowntalk "A rock isn't a pill."

    show annie frown

    cn frown scared eye2 "...Please never make an argument philosophical again, Nemo."

    show cecil eye1

    n frowntalk "What's these pills for?"

    show nemo frown

    annie talk "My, I didn't realize how daft the men of this town could be."

    show annie frown

    n frowntalk eye3 "Fine, I'll stop barking at a knot."
    n frowntalk eye1 "Why are you feeding him emeralds and passing it off as pills?"

    annie frowntalk eye2 "...What a crude accusation."
    annie eye1 "Cecil, let's be on our way."

    show annie frown

    c eye2 arm1 "..."


    show nemo frown up:
        ease 1.0 xalign 0.9 zoom 1.15
    show annie frown down behind nemo:
        ease 1.0 xalign -0.1
    pause(0.85)

    annie frowntalk "Cecil."

    show annie frown

    c frowntalk scared eye1 arm1 "Why do my parents have me taking Emerald pills?"

    show cecil frown

    annie frowntalk "...Let's go home, Cecil."

    show annie frown

    c frowntalk down "No."
    c frowntalk scared arm2 "I'm tired of all this. Please, just be honest with me."

    show cecil frown arm1

    annie eye2 unsure "..."
    annie frowntalk "...Your father asked that I make sure you take them. That's all."

    show annie frown

    c frowntalk "What're they for?"

    show cecil frown

    annie frowntalk "I don't know."
    annie "He warned me not to ask about them."

    show annie frown

    n frowntalk down "What's this business his father is in?"

    show nemo frown

    annie frowntalk "He's a gemstone dealer. He's somewhat of a middleman between the suppliers and buyers, with a few of the mines owned by him."
    annie frown "..."
    annie frowntalk eye1 "...I'm sorry I don't know more, but I can't let a child run around on his own. Let's go home and talk to your parents about it."

    show annie frown at shake
    show nemo at shake
    show bg college1 at shake

    c frowntalk arm2 "No!"

    show cecil frown arm1

    annie frowntalk down "It's not safe out here!"

    show annie frown

    c frowntalk arm2 "I'm safer here than at home!"
    c frowntalk arm3 eye2 crying scared "I... I don't want to go home!"

    show cecil frown

    n unsure eye2 arm2 neutral "..."

    c frowntalk arm1 eye3 "I just want to find Lucie right now. That's it."
    c frowntalk down eye1 -crying "I'm going to come back with her and we'll talk about it later."
    c frowntalk arm1 "C'mon, Nemo!"

    show cecil frown

    n eye1 up arm1 "...!"

    show nemo frown:
        ease 0.5 xalign 2.5 alpha 0.0
    hide cecil
    show annie at shake
    with hpunch

    annie frowntalk down "Wait—!"

    show annie frown


    scene bg hallway1:
        zoom 0.8
        xalign 0.5
        yalign 0.65
    show nemo pink frown eye2 arm2 at center:
        zoom 1.15
    show cecil pink scared eye2 arm3 crying frown at side
    with sideswipe

    c "..."

    cn frown "All I can do is talk a big game and run for now. I can't actually do anything."
    cn frown "Lucie protested and tried her hardest, but look at what happened to her."
    cn frown eye3 "The same's going to happen to me sooner than later."

    show cecil neutral eye1 cap

    show nemo up smile eye1 nocap arm1:
        ease 0.35 yoffset -30
        ease 0.2 yoffset 0
    show bg hallway1 at curtsy:
        ease 0.35 yoffset -40
        ease 0.2 yoffset 0

    nar "Nemo plops his hat on my head, twisting it in my hair."

    show nemo up smile eye1 arm1 at shake
    show bg hallway1 at shake

    c frowntalk arm2 eye4 down "H-Hey!"

    show cecil frown

    n frowntalk "We'll figure something out."

    show nemo smile

    pause(0.1)

    c frowntalk eye5 arm3 scared "...Thanks."

    show cecil frown

    stop music fadeout 3








    $ save_name = "Truth & Turmoil"
    $ chapter_num = "Twenty-Eight"

    call chapter from _call_chapter_27

    $ nemopov = True
    $ cecilpov = False

    scene bg garden:
        zoom 0.7
        yalign 0.6
        xalign 0.5
    show nemo down frown arm2 eye3 at side
    with fade



    play music "audio/Asking Questions.mp3" fadein 2
    queue music "audio/Asking Questions.mp3"

    nn "I hate to say it, but I don't know what I can do for him."
    nn eye2 "I don't know his parents at all—hell, I don't even know their names—and I can't see them letting their kid out of their care for long with as controlling as they've been."
    nn eye3 "Maybe... Maybe after we find Lucie I can come up with something."

    show nemo up eye1

    a "Nemo!"

    show ambrose frown sad glove glass parasol:
        xalign 2.0 alpha 0.0 yalign 0.1
        ease 1.0 xalign 0.7 alpha 1.0

    pause(0.75)

    n frowntalk arm1 "Ambrose...!"

    show nemo frown

    a frowntalk "Marybelle told me Lucie was taken. What happened?"

    show ambrose frown:
        xalign 0.7 alpha 1.0

    n frowntalk eye3 down "Leland found her and demanded she come home, it seems."
    n frowntalk eye2 "We haven't found them yet."

    show nemo frown

    a frowntalk eye3 "Then I'll help."

    show ambrose frown eye1


    show guard behind ambrose at left:
        zoom 0.55 xalign -0.2
    with dissolve
    pause(0.3)
    show ambrose:
        ease 0.5 xalign 0.1
    pause(0.4)

    a frowntalk "Be on the lookout for an aristocrat girl with long, blonde hair. She might be with a tall gentleman with a facial scar, unless she's slipped from him."

    show ambrose frown
    show guard at curtsy
    pause(0.6)
    hide guard with dissolve

    nar "The guards nod and head off."

    show ambrose at center:
        xalign 0.7
    with ease
    pause(0.05)

    a frowntalk "...This is about more than just her running off, isn't it?"

    show ambrose frown

    n frowntalk "...Aye."

    show nemo frown
    show ambrose:
        ease 0.8 zoom 1.15 xalign 0.85
    pause(0.6)

    nar "He brushes part of my bangs out of my eyes."

    a frowntalk eye3 "Whatever it is..."
    show nemo eye1 unsure
    a talk up "I'll be right here beside you."
    a eye1 "You're not alone anymore."

    show ambrose smile sad

    show ambrose:
        ease 2.0 zoom 1.3 xalign 1.5

    nar "I can't help myself."
    nar "I lean in to kiss him."

    show cecil down frown arm2 behind ambrose at right:
        zoom 0.7 yoffset 220 xalign 0.7 blur 0.2
    with hpunch

    c frowntalk "Hello! Your sister is missing and possibly already on the next train north!"

    show cecil frown
    show ambrose eye6

    n frowntalk up eye6 arm2 "Right, right."
    n frowntalk eye3 arm1 "The way it sounded, Leland's trying to skip town as fast as possible."

    show nemo frown

    a frowntalk eye1 up "Then let's head that way."

    show ambrose frown

    c frowntalk eye2 arm3 "About time..."

    show cecil frown


    scene bg city4:
        zoom 0.55
        yalign 0.65
        xalign 0.5
    show nemo down frown eye2 at side
    with fadee

    nn "Where are they?"
    nn eye1 "I can't imagine Lucie is going quietly. If she's still with him, she has to be making a fuss."
    nn eye2 "And with a child throwing a temper tantrum comes—"
    show nemo eye1

    l "LET ME GO!!"

    scene bg city4:
        zoom 0.55
        yalign 0.65
        xalign 0.5
    show lucie grimace down at center:
        zoom 0.94 xalign 0.75 yoffset 120
    show leland down frown eye3 at center:
        xalign 0.5 yalign 0.16
    show nemo down frown at side
    with sideswipe

    show lucie at shake

    leland "..."

    show lucie at shake

    nar "Leland has a firm grip on Lucie's wrist. He ignores her pleas and the worried glances from onlookers."
    show lucie at shake
    nar "Tugging away does nothing given their size difference, but she tries nonetheless."

    show leland eye1
    show lucie at shakeslow

    l frowntalk sad "Why?"
    l frowntalk "Why won't you tell me the truth?"
    l frowntalk "I know you planted the brooch."

    show lucie frown

    leland frowntalk eye2 "I don't know what you're talking about—"

    show leland frown
    show lucie at shake

    l frowntalk down "Yes you do!"
    show lucie at shake
    l frowntalk "Treating me like a baby is one thing, but deceiving me is another!"

    show lucie frown

    n frowntalk "Lucie!"

    show nemo frown

    l frowntalk sad "Nemo!"

    show lucie frown at shake

    nar "She tries to run towards me but Leland refuses to let up."

    leland frowntalk eye1 "We're leaving from here for good!"

    show leland frown
    show lucie down at shakeonce

    l frowntalk "No! Just tell me the truth!"

    show lucie frown

    leland frowntalk eye2 "...Even if you'll hate me?"

    show leland frown

    n frowntalk arm2 eye1 down "D'you think she's gonna like you more as it stands right now?"

    show nemo frown

    l frowntalk sad eye1 "Uncle... Why don't you want me investigating this?"

    show lucie frown

    leland frowntalk eye3 "...Just let it go, Lucie."

    show leland frown eye1
    show lucie at shakeslow

    l frowntalk "I can't!"
    l frowntalk eye2 "I... I have to have something..."

    show lucie frown

    n frowntalk arm1 "Leland... What really happened that night?"

    show nemo frown
    show lucie eye1

    leland eye2 "..."

    show leland frown
    show lucie at shakeslow

    l frowntalk "Just tell me, please...!"

    show lucie frown

    nar "His grip loosens on her as they meet eye to eye."

    leland frowntalk eye3 "Nothing else is going to get through to you now, isn't it..."
    leland frowntalk eye2 "To be honest... I truly don't fully remember."
    leland frowntalk eye3 "It's a blur, even now."
    leland frowntalk eye2 "We... We were having a party to celebrate a recent deal I'd made with a new client. Your father enjoyed throwing lavish parties, always looking for an excuse to have one."
    leland frowntalk "At some point in the night after we'd had supper and drinks, he started boasting about a new client he was fraternizing with on the side—a man with more influence but no tact and loose with his money. Even worse, a man who was at odds with most of our current clients."
    leland frowntalk down eye3 "My brother was always rather unperturbed by things like \"contracts\" and \"business agreements\" and \"keeping his word\", which led to us frequently having disputes. ...Including that night."

    show leland frown

    n eye3 "..."

    leland frowntalk sad "I don't know who threw the first punch. I don't know who was trying to break us up."
    leland frowntalk "I don't know who I bit first."
    leland frowntalk "When I woke up, I was being dragged onto a fishing boat from the water. At some point, I must have gone overboard."
    leland frowntalk "The officers assumed the attacker had thrown me overboard in a fight and I went along with it for a while, as my memory was too foggy."
    leland frowntalk "But... eventually, parts of that night came back to me, piece by piece."

    show leland frown

    l frowntalk sad eye1 "Uncle..."

    show lucie frown

    leland frowntalk eye1 "I didn't think anyone was left, but I wanted to know for sure. With no official body count but a few confirmed, I hired a private detective to find anyone else."
    leland frowntalk "That's how I found you."

    show leland frown

    l frowntalk "Why..."

    show lucie frown:
        ease 0.4 yoffset 150
        ease 0.25 yoffset 120

    nar "Leland strokes her head."

    leland frowntalk eye3 "I'm sorry."

    show leland frown

    l frowntalk "D... Don't leave me too..."
    l frowntalk "Please..."

    show lucie frown

    nn "I know this isn't what she wanted, but... maybe now we can move on."

    stop music fadeout 4









    $ save_name = "Reprieve"
    $ chapter_num = "Twenty-Nine"

    call chapter from _call_chapter_28

    $ nemopov = False
    $ cecilpov = True

    scene bg office2 night:
        zoom 0.5
        yalign 0.65
        xalign 0.5
    show cecil pinknight neutral frown eye3 at side
    with fadee



    play foley "audio/fireplace.mp3" fadein 1

    nar "The light from outside has faded as the fire is all that illuminates the room."
    show cecil eye2 unsure
    nar "Lucie has a pillow in her lap and her eyes on the floor. She hasn't said a word the past few hours."
    nar "Holding onto her sleeve is all I can do for her."
    show cecil eye1 neutral
    nar "Mr. Ambrose walks in with some drinks and sits down beside me."

    show ambrose pinknight up smile:
        yalign 0.1 zoom 1.1 xalign 1.1
    with dissolve

    play music "audio/Isolation Waltz.mp3" fadein 2
    queue music "audio/Isolation Waltz.mp3"

    a talk "Here, drink something. It's been a long day."

    show ambrose smile at curtsy
    show bg office2 night at curtsy

    nar "I don't even ask what's in it."
    nar "It's warm and tastes like milky caramel."

    a frowntalk "What are you thinking about doing now?"

    show ambrose smile

    c eye2 "..."

    cn frown "Just like last time, I have no clue."
    cn eye3 scared "And just like last time, I'll be shipped back up north before I realize it."

    show cecil eye1

    a talk "Don't fret so much! You don't have to figure everything out at your age."
    a "It's alright to be unsure about things."

    show ambrose eye3 smile
    show cecil neutral

    nar "He leans against the back of the couch and sips on his drink."

    a talk eye1 "What do you think of Lauremburg, Cecil?"

    show ambrose smile

    nar "I peer around the apartment."
    nar "Leroy is flopped over on a pillow in front of the fireplace. A dim light from my guest bedroom filters into the hallway."
    show cecil scared
    nar "I really like it here."

    c up talk "It's wonderful."

    show cecil frown

    a talk "Wonderful enough to stay?"

    show ambrose frown

    c frowntalk up arm2 "To—To stay?"

    show cecil frown arm1

    a talk "How would you like to study here? We have some of the finest tutors in the world."

    show ambrose smile

    c frowntalk "I... I... But I live so far away!"

    show cecil frown

    a frowntalk eye2 "Hmm... I suppose you'd just have to stay here then, wouldn't you?"

    show ambrose smile eye1

    c frowntalk scared eye2 "School work takes a lot of time, though... I'd have to fully live here."

    show cecil frown

    a talk "Is that something you'd like?"

    show ambrose smile

    nar "I glance over at Lucie."

    show ambrose:
        ease 0.7 xalign 3.0
    pause(0.4)
    show lucie pinknight eye3 frown behind ambrose:
        yoffset 120 xalign 0.3
    with dissolve

    cn frown "She's all alone now. I can't just leave her to live here."
    cn frown eye3 "...But, at the same time, I don't want to go back."

    show cecil eye1

    l "..."
    l frowntalk eye2 "I'm going to run the family business."

    show lucie frown at shake
    show ambrose unsure frown at shake
    show bg office2 night at shake

    c frowntalk up arm2 "You're what?!"

    show cecil frown arm1

    a frowntalk unsure "Th-That's a nice thought and all, but there's a bit more to running a business than just being the face of it..."
    a frowntalk "For one, do you even know what kind of business it is?"

    show ambrose frown

    l frowntalk down eye1 "It's trade, of course! Papa found nicer spices and goods from far away, so he invested in importing them while there. ...At least, that's what Uncle told me."
    l pout "I've been to several business meetings! Lots!"

    show lucie frown

    c unsure talk arm3 eye2 "Lots..."

    show cecil smile

    l frowntalk "More than you have! Probably!"
    show lucie at shake
    l frowntalk "I can do it! I will do it!"

    show lucie pout
    show cecil neutral eye1 frown


    show nemo pinknight sad frown nocap at left:
        zoom 1.1 xalign -3.5 alpha 0.0
        ease 1.0 xalign -1.4 alpha 1.0

    pause(0.9)

    n frowntalk "Not like that, you're not."

    show nemo frown
    show lucie at shake

    l frowntalk down "Yes I am! You can't stop me, either!"

    show lucie frown

    n frowntalk up eye3 "Right now you've got no custodian to manage the estate. Some louts aren't going to bat an eye at the cash flow but most people will want to do business face-to-face."
    n frowntalk eye1 "And frankly, no one's going to take you on your own seriously."

    show nemo frown

    l pout eye3 "Hmph..."

    n talk eye3 arm2 "Of course... If you were to ask for help, we might could arrange something."

    show nemo smile eye1

    l eye2 "..."

    show lucie frown

    n talk "Or, you could attempt it all on your own in that big ol' manor."

    show nemo frown

    l "....."

    show lucie frown

    n talk eye3 arm1 "Well, good luck!"

    show nemo smile


    hide nemo with easeoutleft

    show lucie:
        ease 0.5 zoom 1.1 yoffset 90 xalign 0.2

    pause(0.5)

    show lucie at shake

    l frowntalk eye1 "W-Wait!"

    show lucie frown

    show nemo pinknight sad frown nocap at left:
        zoom 1.1 xalign -3.6 alpha 0.0
        ease 1.0 xalign -1.4 alpha 1.0

    pause(0.8)

    n frowntalk "Hmm...?"

    show nemo smile

    l frowntalk down eye2 "...I...Well..."
    l frown "..."
    l frowntalk "D...Don't..."

    show lucie frown

    n frowntalk up "Don't what?"

    show nemo frown

    l frowntalk crying "Don't..."
    show lucie at shake
    l frowntalk sad "Don't leave...!"

    show lucie frown



    n neutral "...!"

    show lucie eye3 at shakeslow

    l frowntalk sobbing "You're... You're so mean...!"

    show lucie frown

    n frowntalk eye3 "And you're so stubborn."

    show nemo frown eye1
    show lucie at shakeslow

    l frowntalk "...I'm sorry..."

    show lucie frown eye2

    n frowntalk "We'll figure it out. It'll be alright."
    n frowntalk "You'll always have a home here."

    show nemo smile

    c down frown arm3 "..."

    n frowntalk eye2 arm2 "Wh-What's with that look...?"

    show nemo frown

    c frowntalk eye3 "Making a lady cry... So mean..."

    show cecil frown eye1
    show nemo at shake
    show lucie crying

    n frowntalk down eye1 "How's this back on me?!"

    show nemo frown

    l frowntalk up crying eye3 "Because you're mean and cruel."
    l talk eye1 -crying "That's why you'll be perfect as my bruiser!"

    show lucie smile
    show nemo at shake
    show cecil neutral

    n frowntalk "What kind of business are you planning on running?!"

    show nemo frown

    c frowntalk "If Lucie's going to stay here, then... I'd like to accept your offer, Mr. Ambrose."

    show cecil frown arm1
    show ambrose smile up

    n frowntalk unsure arm2 "Offer?"

    show nemo frown

    a talk eye3 "Wonderful! I imagine it'll be hard for your parents to turn down a stamped letter from a headmaster."
    a "I'll get things together on my end. You can have the guest bedroom you're already in."

    show ambrose smile

    c talk up arm2 "Thank you, thank you!"
    c "Isn't that great, Lucie? We can stay here together now!"

    show cecil smile

    n frowntalk sad "Huh?"

    show nemo frown

    a talk "Oh, I asked Cecil if he'd like to study here rather than be homeschooled. Of course, he'd also have to stay here."

    show ambrose smile
    show nemo at shake

    n frowntalk "Here?!"
    n frowntalk eye2 "Who's the soft one now..."

    show nemo frown

    nar "I pick up Leroy and plop down on the blanket."

    cn "It's going to be alright."
    cn eye3 "It's all going to be alright."
    cn arm1 "Here, I can actually set what I want to do. What's best for me."

    show cecil eye1

    a frowntalk eye3 "Of course, if you're staying here, it'll be because you're studying academics every day and not running around town alone."

    show ambrose smile eye1

    c frowntalk eye2 unsure arm3 "Aww..."

    show cecil frown

    stop music fadeout 3
    stop foley fadeout 3









    $ save_name = "One More Drink"
    $ chapter_num = "Thirty"

    call chapter from _call_chapter_29

    $ nemopov = True
    $ cecilpov = False

    scene bg office2 night:
        zoom 0.5
        yalign 0.65
        xalign 0.5
    show nemo pinknight up neutral arm2 eye2 nocap shirttie at side
    with fade

    play foley "audio/fireplace.mp3" fadein 1


    play music "audio/a432.mp3" fadein 3
    queue music "audio/a432.mp3"



    nar "Lucie and Cecil are laid on the floor, having fallen asleep on Leroy's blanket in front of the fireplace."
    nar "Despite the cross breeze from an open window, the fire flickers on."
    nar "I pour myself another drink."

    nn eye3 "With Leland having turned himself in, Lucie's guardianship falls to me again."
    nn eye2 "From the sound of it, she'll be living with me again. ...And her friend."

    show ambrosen pinknight frown at center:
        zoom 1.25
        xoffset 60
    show nemo eye1
    with dissolve

    an frowntalk "You were gone for a while. Was he talking to you?"

    show ambrosen frown

    n down eye2 "..."
    n frowntalk "He thanked me."
    n frowntalk eye3 "And then he walked off with the coppers."

    show nemo frown

    an down "..."

    show ambrosen up eye6 smile:
        ease 0.4 zoom 1.5 xoffset 100

    pause(0.2)

    nar "I turn to him thinking he's about to say something, but instead he cups my cheek in his hand and kisses me."

    n eye4 up arm1 "...!"

    an frowntalk eye6 "He lived his life stuck in the past, always afraid it'd catch up to him. I don't want to see the same for you."

    show ambrosen eye4 smile

    nar "He holds my hand."

    scene ending cg 1:
        zoom 0.8 yalign 0.0 xalign 0.5 alpha 1.0
    show endingcg:
        xalign 0.5
    with fade

    $ nemopov = False

    a "This... This is going to take some getting used to, but we'll manage."

    n "You should have thought longer about letting them stay here. Now we can't go on a honeymoon."

    a "Why not? They still have to go home and pack."

    nar "He rests his head on my shoulder."

    nn "Maybe I can get used to this."

    $ achievement.grant("ending")
    init:
        $ achievement.register("ending")
        $ achievement.sync()
    $ achievement.sync()

    pause(3)
    pause(3)

    stop foley fadeout 3

    scene black with fadee





    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
