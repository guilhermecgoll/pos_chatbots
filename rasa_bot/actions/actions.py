from typing import Text, Dict, Any, List
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
            response = response.text

        dispatcher.utter_message(text=response)

        return [SlotSet('numero_iptu', [])]