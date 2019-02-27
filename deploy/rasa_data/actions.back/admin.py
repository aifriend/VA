from rasa_core_sdk import Action, CollectingDispatcher, Tracker
from rasa_core_sdk.events import ConversationPaused, SlotSet, UserUtteranceReverted, FollowupAction, Form
from rasa_core_sdk.forms import FormAction
from typing import Text, Dict, Any, List


class ActionPause(Action):
    """Pause the conversation"""

    def name(self):
        return "action_pause"

    def run(self, dispatcher, tracker, domain):
        return [ConversationPaused()]


class ActionStore(Action):
    """Takes the bot language and checks what pipelines can be used"""

    def name(self):
        return "action_store"

    def run(self, dispatcher, tracker, domain):
        spacy_languages = ['english', 'french', 'german', 'spanish',
                           'portuguese', 'french', 'italian', 'dutch']
        language = tracker.get_slot('language')
        if not language:
            return [SlotSet('language', 'that language'),
                    SlotSet('can_use_spacy', False)]

        if language in spacy_languages:
            return [SlotSet('can_use_spacy', True)]
        else:
            return [SlotSet('can_use_spacy', False)]


class ActionSetOnboarding(Action):
    """Sets the slot 'onboarding' to true/false dependent on whether the user
    has built a bot with rasa before"""

    def name(self):
        return "action_set_onboarding"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')
        # latest_action = tracker.latest_action_name
        # print(latest_action)
        # if latest_action == 'utter_first_bot_with_rasa':
        if intent == 'affirm':
            return [SlotSet('onboarding', True)]
        elif intent == 'deny':
            return [SlotSet('onboarding', False)]
        return []


class SuggestionForm(FormAction):
    """Accept free text input from the user for suggestions"""

    def name(self):
        return "suggestion_form"

    @staticmethod
    def required_slots(tracker):
        return ["suggestion"]

    def slot_mappings(self):
        return {"suggestion": self.from_text()}

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_gratitude_suggestion', tracker)
        return []


class ActionGreetUser(Action):
    """Greets the user with/without privacy policy"""

    def name(self):
        return "action_greetings_user"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')
        shown_privacy = tracker.get_slot("shown_privacy")
        name_entity = next(tracker.get_latest_entity_values("name"), None)
        if intent == "greetings":
            if shown_privacy and name_entity and name_entity.lower() != 'sara':
                dispatcher.utter_template("utter_greetings_name", tracker,
                                          name=name_entity)
                return []
            elif shown_privacy:
                dispatcher.utter_template("utter_greetings_noname", tracker)
                return []
            else:
                dispatcher.utter_template("utter_greetings", tracker)
                dispatcher.utter_template("utter_inform_privacypolicy", tracker)
                dispatcher.utter_template("utter_ask_goal", tracker)
                return [SlotSet('shown_privacy', True)]
        elif intent[:-1] == 'get_started_step' and not shown_privacy:
            dispatcher.utter_template("utter_greetings", tracker)
            dispatcher.utter_template("utter_inform_privacypolicy", tracker)
            dispatcher.utter_template("utter_"+intent, tracker)
            return [SlotSet('shown_privacy', True), SlotSet('step', intent[-1])]
        elif intent[:-1] == 'get_started_step' and shown_privacy:
            dispatcher.utter_template("utter_"+intent, tracker)
            return [SlotSet('step', intent[-1])]
        return []


class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        import csv

        self.intent_mappings = {}
        with open('data/intent_description_mapping.csv',
                  newline='',
                  encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                self.intent_mappings[row[0]] = row[1]

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
            ) -> List['Event']:

        intent_ranking = tracker.latest_message.get('intent_ranking', [])
        if len(intent_ranking) > 1:
            diff_intent_confidence = (intent_ranking[0].get("confidence") -
                                      intent_ranking[1].get("confidence"))
            if diff_intent_confidence < 0.2:
                intent_ranking = intent_ranking[:2]
            else:
                intent_ranking = intent_ranking[:1]
        first_intent_names = [intent.get('name', '')
                              for intent in intent_ranking
                              if intent.get('name', '') != 'out_of_scope']

        message_title = "Sorry, I'm not sure I've understood " \
                        "you correctly 🤔 Do you mean..."

        mapped_intents = [(name, self.intent_mappings.get(name, name))
                          for name in first_intent_names]

        buttons = []
        for intent in mapped_intents:
            buttons.append({'title': intent[1],
                            'payload': '/{}'.format(intent[0])})

        buttons.append({'title': 'Something else',
                        'payload': '/out_of_scope'})

        dispatcher.utter_button_message(message_title, buttons=buttons)

        return []


class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
            ) -> List['Event']:

        # Fallback caused by TwoStageFallbackPolicy
        if (len(tracker.events) >= 4 and
                tracker.events[-4].get('name') ==
                'action_default_ask_affirmation'):

            return []

        # Fallback caused by Core
        else:
            dispatcher.utter_template('utter_default', tracker)
            return [UserUtteranceReverted()]


class ActionNextStep(Action):

    def name(self):
        return "action_next_step"

    def run(self, dispatcher, tracker, domain):
        step = int(tracker.get_slot('step'))+1

        if step in [2, 3, 4]:
            dispatcher.utter_template("utter_continue_step{}".format(step), tracker)
        else:
            dispatcher.utter_template("utter_no_more_steps", tracker)

        return []
