from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Module:
    """
    Klasse für Module innerhalb eines Semesters.
    """

    code: str
    name: str
    bestanden: bool
    ects: int
    semester_nummer: int
    bemerkung: Optional[str] = None

    def ist_bestanden(self) -> bool:
        """Gibt zurück, ob das Modul bestanden ist."""
        return self.bestanden

    def ects_wenn_bestanden(self) -> int:
        """ECTS-Punkte nur bei bestandenem Modul."""
        return self.ects if self.bestanden else 0


@dataclass
class Pruefungsleistung:
    """
    Prüfungsleistung zu einem Modul.
    """

    modul_code: str
    art: str
    note: float

    def ist_bestanden(self) -> bool:
        """Prüfung gilt als bestanden bei Note <= 4.0."""
        return self.note <= 4.0


@dataclass
class Semester:
    """
    Klasse für ein Semester innerhalb eines Studiengangs.
    """

    nummer: int
    studiengang_name: str
    aktiv: bool
    module: List[Module] = field(default_factory=list)

    def add_modul(self, modul: Module) -> None:
        """Fügt ein Modul hinzu, wenn es zu diesem Semester gehört."""
        if modul.semester_nummer == self.nummer:
            self.module.append(modul)

    def ects_gesamt(self) -> int:
        """Gesamt-ECTS aller Module im Semester."""
        return sum(m.ects for m in self.module)

    def ects_bestanden(self) -> int:
        """ECTS nur aus bestandenen Modulen."""
        return sum(m.ects_wenn_bestanden() for m in self.module)

    def alle_module_bestanden(self) -> bool:
        """Prüft, ob alle Module des Semesters bestanden sind."""
        return all(m.ist_bestanden() for m in self.module)


@dataclass
class Studiengang:
    """
    Klasse für den Studiengang.
    """

    name: str
    semester: List[Semester] = field(default_factory=list)

    def aktives_semester(self) -> Optional[Semester]:
        """Gibt das aktuell aktive Semester zurück."""
        for s in self.semester:
            if s.aktiv:
                return s
        return None

    def ects_gesamt(self) -> int:
        """Gesamt-ECTS über alle Semester."""
        return sum(s.ects_gesamt() for s in self.semester)

    def ects_bestanden(self) -> int:
        """Bestandene ECTS über alle Semester."""
        return sum(s.ects_bestanden() for s in self.semester)
