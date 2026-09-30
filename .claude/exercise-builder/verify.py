"""Vérifie les notebooks d'exercices générés.

Usage : <python avec nbclient + dépendances du cours> verify.py [numéro de séance ...]

Pour chaque séance :
  1. le corrigé doit s'exécuter entièrement sans erreur (toutes les vérifications passent) ;
  2. dans le notebook élève, chaque cellule de départ doit être du Python valide, et chaque
     cellule ✅ Vérification doit ÉCHOUER (sinon la vérification ne vérifie rien).
Les notebooks sont exécutés dans un dossier temporaire ; input() est remplacé par un faux
utilisateur qui répond "1", "2", "3"... pour que les exercices interactifs se terminent.
"""

import os
import sys
import tempfile

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

from build import RACINE, SEANCES, charger, nom_fichier

FAUX_INPUT = """
import itertools
_reponses = itertools.cycle(range(1, 101))
# ipykernel remplace builtins.input à chaque cellule : on le masque au niveau global.
input = lambda invite="": (print(invite), str(next(_reponses)))[1]
"""

MARQUEUR_VERIF = "# ✅ Vérification"


def executer(nb, allow_errors):
  nb.cells.insert(0, nbformat.v4.new_code_cell(FAUX_INPUT))
  with tempfile.TemporaryDirectory() as dossier:
    NotebookClient(nb, timeout=300, kernel_name="python3", allow_errors=allow_errors,
                   resources={"metadata": {"path": dossier}}).execute()
  nb.cells.pop(0)
  return nb


def verifier_corrige(chemin):
  nb = nbformat.read(chemin, as_version=4)
  try:
    executer(nb, allow_errors=False)
    return []
  except CellExecutionError as e:
    return [str(e)[-3000:]]


def verifier_eleve(chemin):
  nb = nbformat.read(chemin, as_version=4)
  problemes = []
  for cellule in nb.cells:
    if cellule.cell_type == "code":
      source = "\n".join(l for l in cellule.source.splitlines() if not l.lstrip().startswith("!"))
      try:
        compile(source, "<cellule>", "exec")
      except SyntaxError as e:
        problemes.append(f"SyntaxError dans une cellule : {e}\n{cellule.source[:200]}")
  executer(nb, allow_errors=True)
  for cellule in nb.cells:
    if cellule.cell_type == "code" and cellule.source.startswith(MARQUEUR_VERIF):
      a_echoue = any(o.get("output_type") == "error" for o in cellule.outputs)
      if not a_echoue:
        problemes.append(f"Vérification qui passe sans réponse :\n{cellule.source[:300]}")
  return problemes


def main():
  numeros = [int(a) for a in sys.argv[1:]] or SEANCES
  total = 0
  for n in numeros:
    session = charger(n)
    dossier = os.path.join(RACINE, "cours-python-resources", session["dossier"])
    for corrige, fonction in ((True, verifier_corrige), (False, verifier_eleve)):
      nom = nom_fichier(session, corrige)
      problemes = fonction(os.path.join(dossier, nom))
      total += len(problemes)
      print(("OK   " if not problemes else "ECHEC") + " " + nom)
      for p in problemes:
        print("   - " + p.replace("\n", "\n     "))
  sys.exit(1 if total else 0)


if __name__ == "__main__":
  main()
