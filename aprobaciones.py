from dataclasses import dataclass


@dataclass(frozen=True)
class Tarea:
    nombre: str
    requiere_revision: bool


def mostrar_plan(tareas: list[Tarea]) -> None:
    for requiere_revision, titulo in [(False, "Listas"), (True, "Por revisar")]:
        print(titulo)
        for tarea in tareas:
            if tarea.requiere_revision == requiere_revision:
                print(f"  - {tarea.nombre}")


if __name__ == "__main__":
    mostrar_plan([
        Tarea("Ordenar notas", False),
        Tarea("Compartir borrador", True),
        Tarea("Contar pendientes", False),
    ])
