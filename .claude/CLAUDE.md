# Hackspace SHS — contexte pour Claude

Dépôt de cours de Python pour le Hackspace SHS (Université Rennes 2, projet ERC STAGE).
Public : étudiant·es de Master en sciences humaines et sociales, **niveau zéro** en programmation.
Tout le contenu pédagogique est **en français** ; les notebooks sont faits pour **Google Colab**.

## Structure

```
README.md                              présentation du Hackspace + tableau du programme (liens vers tous les notebooks)
cours-python-resources/session-N/
  Atelier Python Session N - <sujet>.ipynb              cours (source de vérité : éditer directement)
  Atelier Python Session N - Exercices.ipynb            exercices (générés, voir plus bas)
  Atelier Python Session N - Exercices (corrigé).ipynb
.claude/exercise-builder/              générateur + vérificateur des notebooks d'exercices
```

Notebooks de cours :
- S1 `Introduction et les Bases`, S2 `Conditions et Boucles`, S3 `Fichiers`, S5 `Classes`
- S4 `Web Scraping` (requests, BeautifulSoup, API Nakala) + `Démo API Arvest` (package arvestapi, iiif-prezi3 ;
  nécessite un compte, identifiants saisis avec input/getpass — ne JAMAIS écrire d'identifiants dans un notebook)
- S6 `NLP - nltk` (pipeline pas à pas) + `NLP - spaCy` (anglais + français, displacy, TextBlob, gensim LDA, classe NLPMachine)
- S7 `Data vis` (matplotlib, pandas ; crée ses propres CSV) + `Data vis 2 - scikit-learn` (numpy, TSNE, scalers, KMeans)

Chaque notebook commence par un titre `# Atelier Python Session N : ...` suivi d'un badge « Open in Colab »
(`https://colab.research.google.com/github/stage-to-data/hackspace-shs/blob/main/<chemin url-encodé>`).
Les notebooks sont enregistrés **sans sorties** (les élèves les exécutent dans Colab).

## Ce que chaque séance enseigne (ce que les élèves sont censés savoir)

1. **Bases** : `print`, commentaires, variables, str/int/float/bool, `type()`, opérations (+ - * /, concaténation),
   `int()/float()/str()`, listes (index à partir de 0), dictionnaires, mise à jour/ajout de valeurs, `def`, indentation,
   portée des variables, `return`, `input()`.
2. **Conditions et boucles** : `if/elif/else`, `== != < > <= >=`, `and/or`, `for ... in`, `len()`, `.append()`,
   `range()`, `enumerate()`, parcourir un dict, `in` / `not in`, `while`, `import random` (`randint`, `choice`).
   (`%` n'est introduit que dans les exercices S2.)
3. **Fichiers** : `os.getcwd/listdir/path.join/path.isfile/isdir`, `open/read/write/close` avec `encoding="utf-8"`,
   modes r/w/a, méthodes de strings (lower, split, strip, count, replace), `json.loads/load/dump`,
   `csv.reader/writer` (`newline=""`). Données : `/content/sample_data` de Colab (README.md, anscombe.json,
   california_housing_train.csv).
4. **Web scraping & API** : `requests.get` avec **User-Agent obligatoire** (Wikipédia/Wikimedia renvoient 403 sans),
   codes HTTP, BeautifulSoup (`find`, `find_all`, `id=`, `class_=`, `.get()`, `.get_text()`), `!pip install`,
   `from x import y`, `with open(...)`, mode `"wb"`, `time.sleep`, f-strings, `params=`, API Nakala (datas, search, metas).
   Les images Wikipédia sont sur `thumb.wikimedia.org` ; l'image principale est dans l'élément `class_="infobox"`.
5. **Classes** : `class`, `__init__`, `self`, attributs, méthodes, `__str__`, objets contenant d'autres objets,
   héritage, `super()`, annotations de type, docstrings.
6. **NLP** : nltk (`word_tokenize`, `sent_tokenize`, stopwords, `FreqDist`, `pos_tag`, WordNetLemmatizer +
   `get_wordnet_pos`, `ne_chunk`) ; spaCy (`Doc`, attributs des tokens, `ents`, displacy, modèle français), TextBlob,
   gensim LDA.
7. **Data vis** : matplotlib (`plot`, `scatter`, `bar`, `pie`, `savefig` avant `show`, `subplots`), pandas
   (`read_csv`, `head`, `describe`, filtres, `groupby`), numpy, scikit-learn (TSNE, MinMax/StandardScaler, KMeans).

## Conventions pour écrire du contenu

- Français, vouvoiement (« vous »), ton encourageant, écriture inclusive légère (étudiant·es). Accents corrects.
- Indentation de **2 espaces** dans le code (style Colab du cours).
- Noms de variables en français (`chemin`, `ma_liste`, `donnees`...), comme dans le cours.
- Exemples ancrés dans les SHS : archives, corpus, notices bibliographiques, œuvres, histoire de Rennes...
- Textes d'exemple : domaine public (ex. Victor Hugo) ou écrits pour l'occasion.
- Ne pas utiliser une notion avant la séance qui l'enseigne ; si c'est indispensable, l'introduire
  dans un encadré « 💡 Nouveau » juste avant (« 💡 Rappel » si le cours l'a déjà vue).
- Chaque notebook de cours se termine par un lien vers le notebook d'exercices de la séance.

## Notebooks d'exercices

Générés par `.claude/exercise-builder/build.py` à partir des fichiers `sessionN.py` du même dossier.
Chaque exercice = énoncé (markdown) + cellule de départ (avec `...`/`pass`) + cellule
« ✅ Vérification » (asserts avec messages en français). Le corrigé remplace la cellule de départ
par la solution. Niveaux : ⭐ (application directe), ⭐⭐ (combinaison), ⭐⭐⭐ (mini-projet).
La séance 2 couvre les séances 1 **et** 2 (révision).

Pour régénérer puis vérifier (exécute tous les corrigés, les vérifications doivent passer, et doivent
échouer sur les notebooks élèves non remplis) :

```bash
python3 .claude/exercise-builder/build.py
<venv avec nbclient, ipykernel, bs4, nltk, pandas, matplotlib, scikit-learn>/bin/python .claude/exercise-builder/verify.py
```

⚠ Si l'enseignant modifie un notebook d'exercices à la main (dans Colab), régénérer écrasera ses
modifications : reporter d'abord ses changements dans `sessionN.py`, ou arrêter d'utiliser le
générateur pour ce notebook.
La séance 4 (parties B et C) nécessite internet (Wikipédia, API Nakala).
