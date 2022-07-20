import random

ch_quality = ["considerate", "kind", "brave", "smart", "loyal"]
incompatible_traits_map = {"considerate": ["bloodthirsty"], "smart": ["dumb"], "kind": ["bloodthirsty"]}
ch_flaw = ["dumb", "bloodthirsty", "obnoxious", "know-it-all", "lunatic"]
ch_profession = ["mercenary", "peasant", "blacksmith", "vagabond", "assassin", "barbarian", "mercenary"]
ch_goal = [f"kill the {random.choice(['king','queen'])}",
           "steal the Amulet of Destiny",
           "get magical powers",
           "restore the balance",
           "settle in peace"]
ch_reason = ["repair $pr1 past mistakes",
             "become the hero of common folks",
             "achieve $pr1 destiny",
             "avoid a prophecy",
             "avenge $pr1 family",
             "be rich",
             "settle a debt",
             "win the admiration of the one $pr0 loves"]
incompatible_reasons_map = {"settle in peace": ["become the hero of common folks",
                                                "be rich",
                                                "avenge $pr1 family",
                                                "achieve $pr1 destiny"],
                            }
ch_sex = ["male", "female", "fluid"]
pronouns_map = {"male": ("he", "his", "him"), "female": ("she", "her", "her"), "fluid": ("they", "their", "them")}

quality_desc_map = {"considerate": ["taking care of the orphan of $pr1 sister"],
                    "kind": ["teaching the kids of $pr1 village to fish"],
                    "brave": ["hunting a wolf that attacked the animals of a nearby farmer"],
                    "smart": ["building a dam on the nearby river to prevent spring flood"],
                    "loyal": ["defending the mayor despite a scandal"]}

flaw_desc_map = {"dumb": ["losing precious time doing things without thinking about the consequences"],
                 "bloodthirsty": ["suppressing $pr1 urges for violence at the slightest frustration"],
                 "obnoxious": ["shamelessly belittling people failing to meet $pr1 expectations"],
                 "know-it-all": ["while antagonizing everyone with unhelpful pieces of advice"],
                 "lunatic": ["though unexpected mood swings made $pr2 unpredictable."]}

trigger_list = ["something"]

first_step_list = ["starts $pr1 journey."]


def get_incompatible_traits(trait_1_list, trait_2_list, incompatible_map):
    trait_1 = random.choice(trait_1_list)
    if trait_1 in incompatible_map.keys():
        trait_2_compatible_list = [trait for trait in trait_2_list if trait not in incompatible_map[trait_1]]
    else:
        trait_2_compatible_list = trait_2_list
    trait_2 = random.choice(trait_2_compatible_list)
    return trait_1, trait_2


def pronounify_sentence(sentence, ch_pronouns_map):
    sentence = sentence.replace("$pr0", ch_pronouns_map[0])
    sentence = sentence.replace("$pr1", ch_pronouns_map[1])
    sentence = sentence.replace("$pr2", ch_pronouns_map[2])
    return sentence


def generate_story_sentence(seed=0):
    random.seed(seed)

    # Protagonist description
    pro_sex = random.choice(ch_sex)
    pro_pronoun = pronouns_map[pro_sex]
    pro_quality, pro_flaw = get_incompatible_traits(ch_quality, ch_flaw, incompatible_traits_map)
    pro_profession = random.choice(ch_profession)
    pro_goal, pro_reason = get_incompatible_traits(ch_goal, ch_reason, incompatible_reasons_map)
    pro_reason = pronounify_sentence(pro_reason, pro_pronoun)

    # Antagonist description
    ant_sex = random.choice(ch_sex)
    ant_pronoun = pronouns_map[ant_sex]
    ant_flaw = random.choice([flaw for flaw in ch_flaw if flaw != pro_flaw])
    ant_profession = random.choice([profession for profession in ch_profession if profession != pro_profession])
    ant_reason = random.choice([reason for reason in ch_reason if reason != pro_reason])
    ant_reason = pronounify_sentence(ant_reason, ant_pronoun)
    premisse = (f"A {pro_quality} but {pro_flaw} {pro_profession} "
                f"wants to {pro_goal} to {pro_reason} "
                f"but a {ant_flaw} {ant_profession} won't let {pro_pronoun[2]} do it "
                f"because {ant_pronoun[0]} wants to {ant_reason}.")
    story = premisse

    # Intro scene generation
    normal_action = random.choice(quality_desc_map[pro_quality])
    normal_action = pronounify_sentence(normal_action, pro_pronoun)
    flaw_modifier = random.choice(flaw_desc_map[pro_flaw])
    flaw_modifier = pronounify_sentence(flaw_modifier, pro_pronoun)
    desc_normal = f"The {pro_profession} was {normal_action}, {flaw_modifier}. "
    trigger = random.choice(trigger_list)
    trigger = pronounify_sentence(trigger, pro_pronoun)
    incident = f"Suddenly, {trigger} happened. "
    first_step = random.choice(first_step_list)
    first_step = pronounify_sentence(first_step, pro_pronoun)
    lift_off = f"The {pro_profession} decided to {first_step}"
    intro = desc_normal + incident + lift_off

    # Concatenating the story elements
    story += "\n" + intro
    return story


# Normal scene decomposition
"""
    First, protagonist do something to achieve scene goal
    Then, antagonist react by doing something to prevent goal to be achieved
    Finally protagonist achieve/fail their goal based on decision function, but lose/gain minor outcome
"""
# Intro scene decomposition
"""
    First, protagonist do something normal to them
    Then, an event unsettle the balance
    Finally protagonist starts the adventure 
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
    for rn_seed in range(0, 10):
        print("--------------")
        gen_story = generate_story_sentence(rn_seed)
        print(gen_story)
