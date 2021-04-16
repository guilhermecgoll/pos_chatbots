# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionConsultaIptu(Action):

    def name(self) -> Text:
        return "action_consulta_iptu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("http://localhost:5000/consulta_iptu?codigo=12")
        #print(response)
        dispatcher.utter_message(text=response.content)

        return []
