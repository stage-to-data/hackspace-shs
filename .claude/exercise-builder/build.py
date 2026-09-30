"""Génère les notebooks d'exercices (et leurs corrigés) pour chaque séance.

Usage : python3 .claude/exercise-builder/build.py [numéro de séance ...]

Chaque fichier sessionN.py définit un dict SESSION :
  numero, dossier, sujet, intro (markdown), items (liste)
Un item est soit un str (cellule markdown : titre de partie, encadré "Nouveau"...),
soit un Exercice, soit un Code (cellule de code identique dans les deux notebooks).
"""

import importlib
import json
import os
import sys
import textwrap
import urllib.parse
from dataclasses import dataclass
from typing import Optional

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
DEPOT_GITHUB = "stage-to-data/hackspace-shs"
SEANCES = [1, 2, 3, 4, 5, 6, 7]


@dataclass
class Exercice:
  titre: str
  niveau: int
  enonce: str
  depart: str
  solution: str
  verif: Optional[str] = None


@dataclass
class Code:
  source: str


def _lignes(texte):
  texte = textwrap.dedent(texte).strip("\n")
  parties = texte.split("\n")
  return [p + "\n" for p in parties[:-1]] + [parties[-1]]


def _md(texte):
  return {"cell_type": "markdown", "metadata": {}, "source": _lignes(texte)}


def _code(texte):
  return {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": _lignes(texte),
  }


def nom_fichier(session, corrige):
  suffixe = " (corrigé)" if corrige else ""
  return f"Atelier Python Session {session['numero']} - Exercices{suffixe}.ipynb"


def _badge_colab(session, corrige):
  chemin = f"cours-python-resources/{session['dossier']}/{nom_fichier(session, corrige)}"
  url = f"https://colab.research.google.com/github/{DEPOT_GITHUB}/blob/main/{urllib.parse.quote(chemin)}"
  return f"[![Ouvrir dans Colab](https://colab.research.google.com/assets/colab-badge.svg)]({url})"


def _entete(session, corrige):
  n = session["numero"]
  if corrige:
    mode = textwrap.dedent(f"""
      > **Ceci est le corrigé.** Il existe presque toujours plusieurs bonnes solutions : si la vôtre
      > est différente mais que la cellule ✅ Vérification passe, c'est très bien !
      > Les exercices sans corrigé sont dans `{nom_fichier(session, False)}`.
    """)
  else:
    mode = textwrap.dedent(f"""
      **Comment faire ?**
      1. Exécutez d'abord la (ou les) cellule(s) de préparation s'il y en a.
      2. Pour chaque exercice, lisez l'énoncé, puis complétez la cellule de code en dessous
         (remplacez les `...` et les `pass` par votre code).
      3. Exécutez ensuite la cellule **✅ Vérification** : elle vous dit si votre réponse est correcte.

      Niveaux : ⭐ application directe · ⭐⭐ on combine plusieurs notions · ⭐⭐⭐ mini-projet.

      Bloqué·e ? Relisez le notebook du cours, cherchez l'erreur sur internet, demandez à votre voisin·e...
      et en dernier recours, jetez un œil au corrigé : `{nom_fichier(session, True)}`.
    """)
  titre = f"# Atelier Python Session {n} — Exercices{' (corrigé)' if corrige else ''}"
  return _md(f"{titre}\n\n{_badge_colab(session, corrige)}\n\n{textwrap.dedent(session['intro']).strip()}\n\n{mode.strip()}")


def construire(session, corrige):
  cellules = [_entete(session, corrige)]
  numero = 0
  for item in session["items"]:
    if isinstance(item, str):
      cellules.append(_md(item))
    elif not hasattr(item, "niveau"):  # Code (pas isinstance : build.py peut aussi être __main__)
      cellules.append(_code(item.source))
    else:
      numero += 1
      etoiles = "⭐" * item.niveau
      cellules.append(_md(f"### Exercice {numero} — {item.titre} {etoiles}\n\n{textwrap.dedent(item.enonce).strip()}"))
      cellules.append(_code(item.solution if corrige else item.depart))
      if item.verif:
        verif = "# ✅ Vérification : exécutez cette cellule pour tester votre réponse\n" + textwrap.dedent(item.verif).strip("\n")
        cellules.append(_code(verif))
  return {
    "cells": cellules,
    "metadata": {
      "colab": {"provenance": []},
      "kernelspec": {"display_name": "Python 3", "name": "python3"},
      "language_info": {"name": "python"},
    },
    "nbformat": 4,
    "nbformat_minor": 0,
  }


def charger(n):
  sys.path.insert(0, ICI)
  return importlib.import_module(f"session{n}").SESSION


def main():
  numeros = [int(a) for a in sys.argv[1:]] or SEANCES
  for n in numeros:
    session = charger(n)
    for corrige in (False, True):
      chemin = os.path.join(RACINE, "cours-python-resources", session["dossier"], nom_fichier(session, corrige))
      with open(chemin, "w", encoding="utf-8") as f:
        json.dump(construire(session, corrige), f, ensure_ascii=False, indent=1)
        f.write("\n")
      print("écrit :", os.path.relpath(chemin, RACINE))


if __name__ == "__main__":
  main()
