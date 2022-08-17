intro_dict = {}

trigger_dict = {}

crucible_dict = {}

ending_dict = {}

event_dict = {}

"""
Event possibility: 
- gather information
- attack someone / something 
- train to do something
- move to a location 
- recover something (object or people)


"""


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
            event = Event(f"event_{id_event}", None, quest_plotline)
            quest_plotline.update_plot(event)
        crucible_event = CrucibleEvent("crucible", None, quest_plotline)
        quest_plotline.update_plot(crucible_event)
        ending_event = EndingEvent("ending", None, quest_plotline)
        quest_plotline.update_plot(ending_event)
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
        return self

    def __str__(self):
        return str([(event.name, event.event_type) for event in self.event_chain])

class Event:
    def __init__(self, name, location, plotline):
        self.name = name
        self.characters = plotline.characters
        self.location = location
        self.event_type = "MISC_EVENT"
        self.outcome = None
        self.flaw_impact = 0
        self.quest_impact = 0

    def initial_action(self):
        return

    def opponent_reaction(self):
        return

    def write_event(self):
        return

class IntroEvent(Event):
    def __init__(self, name, location, plotline):
        super().__init__(name, location, plotline)
        self.event_type = "INTRO"

class TriggerEvent(Event):
    def __init__(self, name, location, plotline):
        super().__init__(name, location, plotline)
        self.event_type = "TRIGGER"

class CrucibleEvent(Event):
    def __init__(self, name, location, plotline):
        super().__init__(name, location, plotline)
        self.event_type = "CRUCIBLE"

class EndingEvent(Event):
    def __init__(self, name, location, plotline):
        super().__init__(name, location, plotline)
        self.event_type = "ENDING"

#print(__name__)
if __name__ == "__main__":
    from characters import Character
    main_character = Character(seed=0)
    quest_characters = {"protagonist":main_character}
    quest = Quest(quest_characters,2)
    print(quest.quest_plotline)