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
                  "$misc_animal": wd_misc_animals, }

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


evt_misc = ["rescue", "dream", "fight", "storm", "breakout", "death", "trap", "argument",
            "love at first sight", "revelation", " meeting", "split up", "journey", "trial", "plan", "metamorphosis",
            "chase"]

act_misc = ["breaking an object", "someone being hurt", "letting time goes by"]

evt_triggers = ["a flood occurred", "a $suspense_adj $ant_profession appeared"]

evt_first_steps = ["starts $pr1 journey."]


def pronounify_sentence(sentence, ch_pronouns_map):
    sentence = sentence.replace("$pr0", ch_pronouns_map[0])
    sentence = sentence.replace("$pr1", ch_pronouns_map[1])
    sentence = sentence.replace("$pr2", ch_pronouns_map[2])
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
    ant_reason = pronounify_sentence(ant_reason, ant_pronoun)
    ch_keyword_map = {"$ant_profession": [ant_profession]}
    keyword_maps = [wd_keyword_map, adj_keyword_map, ch_keyword_map]

    premisse = (f"A {protagonist.quality} but {protagonist.flaw} {protagonist.profession} "
                f"wants to {pronounify_sentence(protagonist.goal, protagonist.pronouns)} "
                f"to {pronounify_sentence(protagonist.reason,protagonist.pronouns)} "
                f"but a {antagonist.flaw} {antagonist.profession} won't let {protagonist.pronouns[2]} do it "
                f"because {antagonist.pronouns[0]} wants "
                f"to {pronounify_sentence(antagonist.reason, antagonist.pronouns)}.")
    premisse = replace_keywords_from_sentence(premisse, keyword_maps)
    story = premisse

    # Intro scene generation
    normal_action = random.choice(evt_quality_descriptions[protagonist.quality])
    normal_action = pronounify_sentence(normal_action, protagonist.pronouns)
    flaw_modifier = random.choice(evt_flaw_descriptions[protagonist.flaw])
    flaw_modifier = pronounify_sentence(flaw_modifier, protagonist.pronouns)
    desc_normal = f"The {protagonist.profession} was {normal_action}, {flaw_modifier}. "
    trigger = random.choice(evt_triggers)
    incident = f"Suddenly, {trigger}. "
    first_step = random.choice(evt_first_steps)
    first_step = pronounify_sentence(first_step, protagonist.pronouns)
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
    for rn_seed in range(0, 2):
        print("--------------")
        gen_story = generate_story_sentence(rn_seed)
        print(gen_story)
