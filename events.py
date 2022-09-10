import random

"""
key is character qualities
"""
intro_quality_descriptions = {"considerate": ["taking care of the orphan of $pr1 sister"],
                            "kind": ["teaching the kids of $pr1 $place to fish"],
                            "brave": ["hunting a wolf that attacked the animals of a nearby farmer"],
                            "smart": ["building a dam on the nearby river to prevent spring flood"],
                            "loyal": ["defending his best friend in $pr1 $pl_quality $place despite a scandal"]}

"""
key is character flaws
"""
intro_flaw_descriptions = {"dumb": ["losing precious time doing things without thinking about the consequences"],
                         "bloodthirsty": ["suppressing $pr1 urges for violence at the slightest frustration"],
                         "obnoxious": ["shamelessly belittling people failing to meet $pr1 expectations"],
                         "know-it-all": ["while antagonizing everyone with unhelpful pieces of advice"],
                         "lunatic": ["though unexpected mood swings made $pr2 unpredictable"]}

"""
key is character reason
"""
trigger_dict = {"repair $pr1 past mistakes":[""],
                "become the hero of common folks":[""],
                "achieve $pr1 destiny":[""],
                "avoid a prophecy":[""],
                "avenge $pr1 family":[""],
                "be rich":[""],
                "settle a debt":[""],
                "win the admiration of the one $pr0 loves":[""]}

"""
key is character flaws
"""
crucible_dict = {"dumb": [""],
                 "bloodthirsty": [""],
                 "obnoxious": [""],
                 "know-it-all": [""],
                 "lunatic": [""]}


"""
key is character goal
"""
ending_dict = {"kill the $important_figure":[""],
               "steal the $magic_object":[""],
               "get magical powers":[""],
               "restore the balance":[""],
               "settle in peace":[""]}

"""
key is event action
"""
misc_event_initial_action = {"recon":["The $pro_profession needed to ask the $misc_figure how to $misc_action. "],
                             "attack":["The time for confrontation had come. Gathering $pr1 strength, the $pro_profession attacked the $target. "],
                             "train":["Knowing $pr0 wasn't strong enough to prevail, the $pro_profession started to train. "],
                             "move":["The $target was in the $location, far away from here. The $pro_profession started traveling. "],
                             "recover":["The $pro_profession needed to recover the $misc_object. In order to do so, $pr0 spent some time casing the $location where the $misc_object was held. "]}

#TODO: rename to obstacle ? 
#TODO: update with notion of difficulty later
misc_event_opponent_reaction = {"recon":["The $ant_profession tried to hinder the $pro_profession by blocking the access to the $misc_figure. "],
                                "attack":["The $target put up a fight. "],
                                "train":["The lesson was though, and the $pro_profession struggled. "],
                                "move":["A storm started to blow. "],
                                "recover":["The $misc_object was guarded by a small army. "]}


# keys are event action + protagonist flaws. Describes protagonist sets in its ways
misc_event_character_evolve = {"recon":{ "dumb": [""],
                                        "bloodthirsty": [""],
                                        "obnoxious": [""],
                                        "know-it-all": [""],
                                        "lunatic": [""]},
                                "attack":{  "dumb": [""],
                                            "bloodthirsty": [""],
                                            "obnoxious": [""],
                                            "know-it-all": [""],
                                            "lunatic": [""]},
                                "train":{   "dumb": [""],
                                            "bloodthirsty": [""],
                                            "obnoxious": [""],
                                            "know-it-all": [""],
                                            "lunatic": [""]},
                                "move":{    "dumb": [""],
                                            "bloodthirsty": [""],
                                            "obnoxious": [""],
                                            "know-it-all": [""],
                                            "lunatic": [""]},
                                "recover":{ "dumb": [""],
                                            "bloodthirsty": [""],
                                            "obnoxious": [""],
                                            "know-it-all": [""],
                                            "lunatic": [""]},
                             }

# keys are event action + protagonist flaws. Describes protagonist able to evolve
misc_event_character_persist = {"move":{ "dumb": ["The $pro_profession got a map describing how to get to the location, but didn't know how to read it. Instead of asking for help, $pr0 tossed it to the wind. "],
                                        "bloodthirsty": ["A kind $misc_figure wanted to show the $pro_profession the way, but insteand $pr0 decided to rob him of his possession. "],
                                        "obnoxious": ["When a $misc_figure agreed to guide the $pro_profession, $pr0 thought everything was well. But $pr0 couldn't help but antagonize $pr1 guide every step of the way. Thus, the $pro_profession was left alone. "],
                                        "know-it-all": ["The $pro_profession knew a lot of trivia about the surrounding area. None of it was useful to find a direction."],
                                        "lunatic": [""]},
                                "attack":{  "dumb": [""],
                                            "bloodthirsty": [""],
                                            "obnoxious": [""],
                                            "know-it-all": [""],
                                            "lunatic": [""]},
                                "train":{   "dumb": [""],
                                            "bloodthirsty": [""],
                                            "obnoxious": [""],
                                            "know-it-all": [""],
                                            "lunatic": [""]},
                                "recon":{    "dumb": [""],
                                            "bloodthirsty": [""],
                                            "obnoxious": [""],
                                            "know-it-all": [""],
                                            "lunatic": [""]},
                                "recover":{ "dumb": [""],
                                            "bloodthirsty": [""],
                                            "obnoxious": [""],
                                            "know-it-all": [""],
                                            "lunatic": [""]},
                             }


# Success -> protagonist overcomes the obstacle 
# Failure -> protagonist fails to overcome obstacle
misc_event_outcome = {"recon":{"success":["The $pro_profession talked at length to the $misc_figure, who was keen to share the needed information. "],
                                        "failure":["The $misc_figure was nowhere to be found. Traces of blood could be found in the $location. "]},
                             "attack":{"success":["After a bloody fight, the $pro_profession managed to land a decisive blow. Breathless, he realized that the battle was won. "], 
                                       "failure":["The $pro_profession suffered a heavy blow and fell unconscious. "]},
                             "train":{"success":["The $pro_profession found a masterful $misc_figure, who was convinced by $pr1 $pro_quality to teach $pr2 what he needed to know. "],
                                      "failure":["The $pro_profession found a masterful $misc_figure, but was too $pro_flaw to understand the wisdom that was imparted. "]},
                             "move":{"success":["The $pro_profession managed to reach the $location with no trouble. "],
                                     "failure":["The $pro_profession got lost, and failed to reach the $location. "]},
                             "recover":{"success":["One night, the $pro_profession broke in and retrieve the $misc_object, and then managed to get out of the $location. "],
                                        "failure":["When the $pro_profession tried to retrieve the $misc_object, $pr0 got caught and had to run away. "]}}


evt_action =["recon","attack","train","move","recover"]

class Quest:
    """
    characters = {"protagonist":Character, "antagonist":Character, "support":list(Character)}
    """
    def __init__(self, characters, nb_events):
        self.characters = characters
        self.objective = characters["protagonist"].goal
        self.nb_events = nb_events
        self.quest_plotline = self.generate_plotline()

    def generate_plotline(self):
        quest_plotline = Plotline(self.characters)
        initial_event = IntroEvent("intro", None, quest_plotline)
        quest_plotline.update_plot(initial_event)
        trigger_event = TriggerEvent("trigger", None, quest_plotline)
        quest_plotline.update_plot(trigger_event)
        for id_event in range(self.nb_events):
            event_outcome = "success" if quest_plotline.event_chain[-1].outcome == "failure" else "failure"
            #print(id_event, event_outcome, quest_plotline.event_chain[-1].outcome)
            event = Event(f"event_{id_event}", None, event_outcome, quest_plotline)
            quest_plotline.update_plot(event)
        crucible_outcome = "success" if quest_plotline.flaw_progression > 0 else "failure"                                                                                                                                                                                       
        crucible_event = CrucibleEvent("crucible", None, crucible_outcome, quest_plotline)
        quest_plotline.update_plot(crucible_event)
        ending_outcome = "success" if  quest_plotline.quest_progression > 0 else "failure" 
        ending_event = EndingEvent("ending", None, ending_outcome, quest_plotline)
        quest_plotline.update_plot(ending_event)
        print(quest_plotline.quest_progression)
        print([event.outcome for event in quest_plotline.event_chain])
        return quest_plotline

class Plotline:
    def __init__(self, characters):
        self.characters = characters
        self.location_list = []
        self.event_chain = []
        self.flaw_progression = 0
        self.quest_progression = 0

    def update_plot(self, event):
        self.event_chain.append(event)
        self.location_list.append(event.location)
        self.characters = event.characters
        self.flaw_progression += event.flaw_impact
        self.quest_progression += event.quest_impact
        print(event.name, event.quest_impact, self.quest_progression)
        return self

    def __str__(self):
        return str([(event.name, event.write_event(), event.event_type) for event in self.event_chain])

class Event:
    def __init__(self, name, location, outcome, plotline):
        self.name = name
        self.characters = plotline.characters
        self.location = location
        self.event_type = "MISC_EVENT"
        self.action = random.choice(evt_action)
        self.protagonist_behavior = random.choice(["persist","evolve"])
        self.outcome = outcome
        self.quest_impact = self.flaw_impact = 0
        if self.outcome == "success":
            self.quest_impact = 1
        elif self.outcome == "failure":
            self.quest_impact = -1
        else:
            self.quest_impact = 0 

    def initial_action(self):
        initial_action = random.choice(misc_event_initial_action[self.action])
        return initial_action

    def opponent_reaction(self):
        opponent_reaction = random.choice(misc_event_opponent_reaction[self.action])
        return opponent_reaction

    def protagonist_choice(self):
        protagonist_choice = ""
        if self.protagonist_behavior == "persist":
            protagonist_choice = misc_event_character_persist[self.action][self.plotline.characters["protagonist"].flaw]
        else:
            protagonist_choice = misc_event_character_evolve[self.action][self.plotline.characters["protagonist"].flaw]
        return protagonist_choice

    def event_outcome(self):
        event_outcome = random.choice(misc_event_outcome[self.action][self.outcome])
        return event_outcome

    def write_event(self):
        """
        - Initial action 
        - Opposing action 
        - Event outcome
        """
        event_sentence = self.initial_action() + self.opponent_reaction() + self.event_outcome() + f"The action is a {self.outcome}. "
        return event_sentence

class IntroEvent(Event):
    def __init__(self, name, location, plotline):
        self.outcome = None
        super().__init__(name, location, self.outcome, plotline)
        self.event_type = "INTRO"

    def write_event(self):
        protagonist = self.characters["protagonist"]
        intro_quality_action = random.choice(intro_quality_descriptions[protagonist.quality])
        intro_flaw_modifier = random.choice(intro_flaw_descriptions[protagonist.flaw])  
        event_sentence = f"The {protagonist.profession} was {intro_quality_action}, {intro_flaw_modifier}. "
        return event_sentence

class TriggerEvent(Event):
    def __init__(self, name, location, plotline):
        outcome = random.choice(["success","failure"]) 
        super().__init__(name, location, outcome, plotline)
        self.event_type = "TRIGGER"

class CrucibleEvent(Event):
    def __init__(self, name, location, outcome, plotline):
        super().__init__(name, location, outcome, plotline)
        self.event_type = "CRUCIBLE"

class EndingEvent(Event):
    def __init__(self, name, location, outcome, plotline):
        super().__init__(name, location, outcome, plotline)
        self.event_type = "ENDING"

    def write_event(self):
        return super().write_event()

if __name__ == "__main__":
    from characters import Character
    main_character = Character(seed=0)
    quest_characters = {"protagonist":main_character}
    quest = Quest(quest_characters,2)
    print(quest.quest_plotline)