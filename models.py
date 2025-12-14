from dataclasses import dataclass

@dataclass
class Module:
    """
    Diese Klasse
    """

    code: str
    name: str
    bestanden: bool
    ects: int
    semesterNummer: int
    bemerkung: str | None = None

@dataclass
class Semester:
    """
    Docstring for Semester
    """

    nummer: int
    studiengangName: str
    aktiv: bool

@dataclass
class Studiengang:
    """
    Docstring for Studiengang
    """

    name: str

@dataclass
class Pruefungsleistung:
    """
    Docstring for Pruefungsleistung
    """

    modulCode: str
    art: str
    note: float




