import random

ch_quality = ["considerate", "kind", "brave", "smart", "loyal"]
incompatible_traits_map = {"considerate": ["bloodthirsty"], "smart": ["dumb"], "kind": ["bloodthirsty"]}
ch_flaw = ["dumb", "bloodthirsty", "obnoxious", "know-it-all", "lunatic"]
ch_profession = ["mercenary", "peasant", "blacksmith", "vagabond", "assassin", "barbarian"]
ch_goal = ["kill the king",
           "steal the Amulet of Destiny",
           "get magical powers",
           "restore the balance",
           "settle in peace"]
ch_reason = ["repair $pr1 past mistakes",
             "become the hero of common folks",
             "achieve $pr1 destiny",
             "avoid a prophecy",
             "avenge $pr1 family",
             "be rich"]
incompatible_reasons_map = {"settle in peace": ["become the hero of common folks",
                                                "be rich",
                                                "avenge $pr1 family",
                                                "achieve $pr1 destiny"],
                            }
ch_sex = ["male", "female", "fluid"]
pronouns_map = {"male": ("he", "his", "him"), "female": ("she", "her", "her"), "fluid": ("they", "their", "them")}


def generate_story_sentence(seed=0):
    random.seed(seed)
    pro_sex = random.choice(ch_sex)
    pro_pronoun = pronouns_map[pro_sex]
    pro_quality = random.choice(ch_quality)
    if pro_quality in incompatible_traits_map.keys():
        flaw_list = [flaw for flaw in ch_flaw if flaw not in incompatible_traits_map[pro_quality]]
    else:
        flaw_list = ch_flaw
    pro_flaw = random.choice(flaw_list)
    pro_profession = random.choice(ch_profession)
    pro_goal = random.choice(ch_goal)
    if pro_goal in incompatible_reasons_map.keys():
        reason_list = [reason for reason in ch_reason if reason not in incompatible_reasons_map[pro_goal]]
    else:
        reason_list = ch_reason
    # print(reason_list)
    pro_reason = random.choice(reason_list)
    pro_reason = pro_reason.replace("$pr1", pro_pronoun[1])
    ant_flaw = random.choice([flaw for flaw in ch_flaw if flaw != pro_flaw])
    ant_profession = random.choice([profession for profession in ch_profession if profession != pro_profession])
    story = (f"This is the story of a {pro_quality} but {pro_flaw} {pro_profession} "
             f"who wants to {pro_goal} to {pro_reason} "
             f"but a {ant_flaw} {ant_profession} won't let {pro_pronoun[2]} do it.")
    return story


if __name__ == '__main__':
    for rn_seed in range(0, 5):
        gen_story = generate_story_sentence(rn_seed)
        print(gen_story)
