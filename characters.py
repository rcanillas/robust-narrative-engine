import random

# TODO: define Entity class with type ?

ch_quality = ["considerate", "kind", "brave", "smart", "loyal"]
ch_flaw = ["dumb", "bloodthirsty", "obnoxious", "know-it-all", "lunatic"]
ch_profession = ["mercenary", "peasant", "blacksmith", "vagabond", "assassin", "barbarian", "mercenary"]


ch_goal = [f"kill the $important_figure",
           "steal the $magic_object",
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

incompatible_traits_map = {"considerate": ["bloodthirsty"], "smart": ["dumb"], "kind": ["bloodthirsty"]}

incompatible_reasons_map = {"settle in peace": ["become the hero of common folks",
                                                "be rich",
                                                "avenge $pr1 family",
                                                "achieve $pr1 destiny",
                                                "settle a debt"],
                            }
ch_sex = ["male", "female", "fluid"]
pronouns_map = {"male": ("he", "his", "him"), "female": ("she", "her", "her"), "fluid": ("they", "their", "them")}

ch_base_state = {"bravery": 0, "intelligence": 0, "trustworthiness": 0, "empathy": 0}

ch_stats_modifier = {"considerate": {"empathy": 1},
                     "kind": {"empathy": 1},
                     "brave": {"bravery": 1},
                     "smart": {"intelligence": 1},
                     "loyal": {"trustworthiness": 1},
                     "dumb": {"intelligence": -1},
                     "bloodthirsty": {"empathy": -1},
                     "obnoxious": {"empathy": -1},
                     "know-it-all": {"empathy": -1},
                     "lunatic": {"empathy": -1}}


def get_compatible_traits(trait_1_list, trait_2_list, incompatible_map):
    trait_1 = random.choice(trait_1_list)
    if trait_1 in incompatible_map.keys():
        trait_2_compatible_list = [trait for trait in trait_2_list if trait not in incompatible_map[trait_1]]
    else:
        trait_2_compatible_list = trait_2_list
    trait_2 = random.choice(trait_2_compatible_list)
    return trait_1, trait_2


def generate_traits():
    sex = random.choice(ch_sex)
    pronouns = pronouns_map[sex]
    quality, flaw = get_compatible_traits(ch_quality, ch_flaw, incompatible_traits_map)
    profession = random.choice(ch_profession)
    goal, reason = get_compatible_traits(ch_goal, ch_reason, incompatible_reasons_map)
    return sex, pronouns, quality, flaw, profession, goal, reason


class Character:
    def __init__(self, seed=42):
        random.seed(seed)
        self.seed = seed
        self.sex, self.pronouns, self.quality, self.flaw, self.profession, self.goal, self.reason = generate_traits()
        self.internal_state = ch_base_state
        state_modifier_quality = ch_stats_modifier[self.quality]
        for modified_stat, modif_value in state_modifier_quality.items():
            self.internal_state[modified_stat] += modif_value
        state_modifier_flaw = ch_stats_modifier[self.flaw]
        for modified_stat, modif_value in state_modifier_flaw.items():
            self.internal_state[modified_stat] += modif_value

    def antagonize(self, character):
        quality_seed = 1
        while character.flaw == self.flaw or character.quality == self.quality:
            random.seed(self.seed + quality_seed)
            self.flaw, self.quality = get_compatible_traits(ch_quality, ch_flaw, incompatible_traits_map)
            quality_seed += 1

        profession_seed = 1
        while character.profession == self.profession:
            random.seed(self.seed + profession_seed)
            self.profession = random.choice(ch_profession)
            profession_seed += 1

        goal_seed = 1
        while character.goal == self.goal and character.reason == self.reason:
            random.seed(self.seed + goal_seed)
            self.goal, self.reason = get_compatible_traits(ch_goal, ch_reason, incompatible_reasons_map)
            goal_seed += 1

    def select_next_action(self):
        pass

    def compute_state(self):
        pass


if __name__ == '__main__':
    print('Character test')
    test_ch = Character()
    print(test_ch.__dict__)
