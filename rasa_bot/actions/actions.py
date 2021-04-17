# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from rasa_sdk.events import AllSlotsReset
import requests


class ActionConsultaIptu(Action):

    def name(self) -> Text:
        return "action_consulta_iptu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = ''
        codigo = tracker.get_slot('numero_iptu')
        code = 0
        try:
            code = int(codigo)
        except:
            response = 'O código de iptu informado não é válido'
        
        if(code > 0):
            response = requests.get(f"http://localhost:5000/consulta_iptu?codigo={code}")
            response = response.content
        
        dispatcher.utter_message(text=response)

        return [AllSlotsReset()]
        # return [SlotSet("resultado_consulta_iptu", response)]

class ConsultaIptuForm(FormAction):

    def name(self) -> Text:
        return "consulta_iptu_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["numero_iptu"]
