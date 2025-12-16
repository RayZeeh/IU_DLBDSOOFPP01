import json
from typing import List

from models import Studiengang, Semester, Module, Pruefungsleistung


class DataHandler:
    """
    Verantwortlich für das Laden der Daten und erstellen der Klassen-Objekte.
    """

    def __init__(self):
        self.data_dir = "./data"

    # ---------- low level loader ----------

    def _load_json(self, filename: str):
        try:
            with open(f"{self.data_dir}/{filename}", "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            raise RuntimeError(f"Datei nicht gefunden: {filename}")
        except json.JSONDecodeError:
            raise RuntimeError(f"Ungültiges JSON in Datei: {filename}")

    # ---------- entity loader ----------

    def load_module(self) -> List[Module]:
        data = self._load_json("module.json")
        return [Module(**m) for m in data]

    def load_semester(self) -> List[Semester]:
        data = self._load_json("semester.json")
        return [Semester(**s) for s in data]

    def load_studiengang(self) -> Studiengang:
        data = self._load_json("studiengang.json")
        return Studiengang(**data)

    def load_pruefungsleistungen(self) -> List[Pruefungsleistung]:
        data = self._load_json("pruefungsleistung.json")
        return [Pruefungsleistung(**p) for p in data]

    # ---------- aggregate builder ----------

    def load_studiengang_komplett(self) -> Studiengang:
        """
        Baut den vollständigen Objektgraphen:
        Studiengang -> Semester -> Module
        """

        studiengang = self.load_studiengang()
        semester_liste = self.load_semester()
        module_liste = self.load_module()

        # Module den Semestern zuordnen
        for semester in semester_liste:
            for modul in module_liste:
                semester.add_modul(modul)

        studiengang.semester = semester_liste
        return studiengang
