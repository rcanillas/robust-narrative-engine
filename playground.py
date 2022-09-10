import random
from characters import Character

wd_important_figures = ['king', 'queen', 'emperor', "duke", "prince", "princess", "general"]

wd_misc_figures = ["old woman", "giant", "thief", "orphan", "parents", "cook", "child", "witch", "brother", "sister",
                   "monster", "fairy", "beggar", "old man", "husband", "wife", "shepperd", "stepmother"]

wd_misc_animals = ["wolf", "frog", "horse", "bird"]

wd_places = ['village', 'city', 'capital', 'desert oasis', 'forest', 'hideout', 'seaside', 'fortress', 'at sea', 'road',
             'kingdom', 'ruins', 'stairs', 'church', 'palace', 'cottage', 'island', 'town', 'prison', 'tower', 'house',
             'kitchen', 'cavern', 'in the mountain', 'alongside a river']

wd_times = ["day", "night", "noon", "dusk", "dawn"]

wd_place_quality = ['crowded', "isolated", "remote", "comfortable", "famished", "collapsing", "tenebrous"]

obj_magic = ["Amulet of Destiny", "Crown of Rulers", "Potions of Eternal Knowledge", "Diadem of True Wisdom",
             "Sword of Eternal Strength"]

obj_misc = ["tome", "axe", "gift", "key", "ring", "food", "tree", "sword", "door", "window", "fire", "treasure",
            "ship", "magic spell", "crown"]

wd_keyword_map = {"$important_figure": wd_important_figures,
                  "$magic_object": obj_magic,
                  "$place": wd_places,
                  "$pl_quality": wd_place_quality,
                  "$misc_object": obj_misc,
                  "$misc_figure": wd_misc_figures,
                  "$misc_animal": wd_misc_animals,}

adj_suspense = ["mysterious", "strange", "innocuous", "unusual", "tight lipped"]
adj_keyword_map = {"$suspense_adj": adj_suspense}

adj_misc = [{"text": "ugly", "target": ["all"]},
            {"text": "talking", "target": ["obj", "an"]},
            {"text": "long lost", "target": ["all"]},
            {"text": "happy", "target": ["ch", "an"]},
            {"text": "disguised", "target": ["ch"]},
            {"text": "asleep", "target": ["ch", "an"]},
            {"text": "splendid", "target": ["all"]},
            {"text": "blind", "target": ["ch", "an"]},
            {"text": "hidden", "target": ["all"]},
            {"text": "far away", "target": ["pl"]},
            {"text": "poisonous", "target": ["obj", "an", "fd"]},
            {"text": "lucky", "target": ["all"]},
            {"text": "secret", "target": ["all"]},
            {"text": "evil", "target": ["all"]},
            {"text": "flying", "target": ["obj", "an"]},
            {"text": "tiny", "target": ["all"]},
            {"text": "cursed", "target": ["all"]},
            {"text": "lost", "target": ["all"]},
            {"text": "frightful", "target": ["ch", "an"]},
            {"text": "secret", "target": ["ch", "an"]},
            {"text": "stolen", "target": ["obj", "an"]},
            {"text": "wise", "target": ["ch", "an"]},
            {"text": "force of nature", "target": ["ch", "an"]},
            {"text": "secret", "target": ["all"]}, ]

evt_quality_descriptions = {"considerate": ["taking care of the orphan of $pr1 sister"],
                            "kind": ["teaching the kids of $pr1 $place to fish"],
                            "brave": ["hunting a wolf that attacked the animals of a nearby farmer"],
                            "smart": ["building a dam on the nearby river to prevent spring flood"],
                            "loyal": ["defending his best friend in $pr1 $pl_quality $place despite a scandal"]}

evt_flaw_descriptions = {"dumb": ["losing precious time doing things without thinking about the consequences"],
                         "bloodthirsty": ["suppressing $pr1 urges for violence at the slightest frustration"],
                         "obnoxious": ["shamelessly belittling people failing to meet $pr1 expectations"],
                         "know-it-all": ["while antagonizing everyone with unhelpful pieces of advice"],
                         "lunatic": ["though unexpected mood swings made $pr2 unpredictable"]}

evt_misc = ["rescue", "dream", "fight", "storm", "breakout", "death", "trap", "bad argument",
            "love at first sight", "revelation", " meeting", "split up", "journey", "trial", "plan", "metamorphosis",
            "chase"]

act_misc = ["%pr_object %object is broken", "%character is hurt", "time goes by for a while"]

evt_keywords_map = {"$misc_event": evt_misc}

evt_triggers = {"repair $pr1 past mistakes": ["One day, a $misc_figure appeared and asked for the $pr_profession. He was bringing news from an old friend that the $pr_profession betrayed long ago to avoid a dire condamnation."],
                "become the hero of common folks": ["As usual, the guardsmen were roughing up an innocent $misc_figure right there on the street. Bolstered by the protection of the $important_figure, they believed they could get away with anything."],
                "achieve $pr1 destiny": ["When $pr0 was young, a seer told the $ch_profession that $pr2 were headed toward greatness, and that the $misc_animals would be the sign to become what $pr0 was truly meant to be. Disbelieving at first, the $pr_profession was not so certain when $pr0 found a wounded $misc_animal at $pr1 doorstep."],
                "avoid a prophecy": ["The stench of bad omens was clinging to the $pr_profession since $pr0 disturbed an old wizard in a ruined $place. 'A $misc_event awaits you', the priest said, 'and you better be ready to face it, or risk a fate worth than death'."],
                "avenge $pr1 family": ["But at night, there was nothing to keep the nightmares at bay. The smell of the fire in the $place, the screams of $pr1 family getting caught, the laughter of the mercenaries. There was only one thing that could make the nightmares stop. Justice."],
                "be rich": ["The $pr_profession stops for a moment as a rich $important_figure travel through the $place. Such finery, such comfort, while the $pr_profession has to work all day to earn scraps and leftovers. 'Not anymore', $pr0 thinks."],
                "settle a debt": ["Some say there is no price for a life. Well, they never met the $pr_profession, because he promised a hefty sum to one important $important_figure, and judging by the soldiers at $pr1 doorstep, the time had come to collect."],
                "win the admiration of the one $pr0 loves": ["After a good day of work, what is nicer than to find the warmth of a loving embrace ? For the $pr_profession, nothing. This why $pr0 had to convince the one $pr0 loved that $pr1 intention were serious."]}

evt_first_steps = ["starts $pr1 journey."]


def characterize_sentence(sentence, character):
    sentence = sentence.replace("$pr0", character.pronouns[0])
    sentence = sentence.replace("$pr1", character.pronouns[1])
    sentence = sentence.replace("$pr2", character.pronouns[2])
    sentence = sentence.replace("$pr_profession", character.profession)
    return sentence


def replace_keywords_from_sentence(sentence, keyword_maps):
    for keyword_map in keyword_maps:
        for keyword, keyword_list in keyword_map.items():
            if keyword in sentence:
                sentence = sentence.replace(keyword, random.choice(keyword_list))
    return sentence


def generate_story_sentence(seed=0):
    random.seed(seed)
    # Protagonist description
    protagonist = Character(seed)

    # Antagonist description
    antagonist = Character(seed+42)
    antagonist.antagonize(protagonist)
    ant_pronoun = antagonist.pronouns
    ant_flaw = antagonist.flaw
    ant_profession = antagonist.profession
    ant_reason = antagonist.reason
    ant_reason = characterize_sentence(ant_reason, antagonist)
    ch_keyword_map = {"$ant_profession": [ant_profession]}
    keyword_maps = [wd_keyword_map, adj_keyword_map, ch_keyword_map, evt_keywords_map]

    premisse = (f"A {protagonist.quality} but {protagonist.flaw} {protagonist.profession} "
                f"wants to {characterize_sentence(protagonist.goal, protagonist)} "
                f"to {characterize_sentence(protagonist.reason,protagonist)} "
                f"but a {antagonist.flaw} {antagonist.profession} won't let {protagonist.pronouns[2]} do it "
                f"because {antagonist.pronouns[0]} wants "
                f"to {characterize_sentence(antagonist.reason, antagonist)}.")
    premisse = replace_keywords_from_sentence(premisse, keyword_maps)
    story = premisse

    # Intro scene generation
    normal_action = random.choice(evt_quality_descriptions[protagonist.quality])
    normal_action = characterize_sentence(normal_action, protagonist)
    flaw_modifier = random.choice(evt_flaw_descriptions[protagonist.flaw])
    flaw_modifier = characterize_sentence(flaw_modifier, protagonist)
    desc_normal = f"The {protagonist.profession} was {normal_action}, {flaw_modifier}. "
    trigger = random.choice(evt_triggers[protagonist.reason])
    incident = characterize_sentence(trigger, protagonist) + " "
    first_step = random.choice(evt_first_steps)
    first_step = characterize_sentence(first_step, protagonist)
    lift_off = f"The {protagonist.profession} decided to {first_step}"
    intro = desc_normal + incident + lift_off
    intro = replace_keywords_from_sentence(intro, keyword_maps)
    # Concatenating the story elements
    story += "\n" + intro
    return story


# Normal scene decomposition
"""
    First, protagonist do something to achieve scene goal
    Then, antagonist react by doing something to prevent goal to be achieved
    Finally protagonist achieve/fail their goal based on decision function, but lose/gain minor outcome
    and decide to next scene goal.
"""
# Intro scene decomposition
"""
    First, protagonist do something normal to them
    Then, an event unsettle the balance
    Finally protagonist starts the adventure by next scene goal
"""

# Story decomposition
"""
    Scene 1 -> Intro scene
    Scene 2 -> Outcome Success or Failure
    Scene 3 -> Inverted Outcome from previous scene
    Scene 4 -> Crucible scene
    Scene 5 -> Outcome Success of Failure
    Scene 6 -> Inverted Outcome from previous scene
    Scene 7 -> Final scene
"""

if __name__ == '__main__':
    for rn_seed in range(0, 5):
        print("--------------")
        gen_story = generate_story_sentence(rn_seed)
        print(gen_story)
