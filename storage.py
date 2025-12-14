import json
from models import Studiengang, Semester, Module, Pruefungsleistung

class DataHandler:
    """
    Docstring for DataHandler
    """

    def __init__(self):
        pass

    def load_module(self) -> list[Module]:
        """
        
        """

        try:
            with open("./data/module.json","r",encoding="utf-8") as module:
                module_data = json.load(module)
            
            module_list: list[Module] = []
            for m in module_data:
                module_list.append(Module(**m))
            return module_list
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading modules: {e}")