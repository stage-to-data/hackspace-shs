from build import Code, Exercice

SESSION = {
  "numero": 3,
  "dossier": "session-3",
  "intro": """
    Ces exercices reprennent la séance 3 : construire des chemins avec `os`, lire et écrire des fichiers
    texte, JSON et CSV.
  """,
  "items": [
    "## Préparation",

    """
    Exécutez la cellule suivante **une fois** : elle crée un dossier `donnees_exercices` contenant trois fichiers
    que nous allons utiliser (dans Colab, vous le verrez apparaître dans le panneau « Fichiers » à gauche) :
    - `demain_des_laube.txt` : un poème de Victor Hugo (1856) ;
    - `corpus.json` : une liste de romans du XIXe siècle (le nombre de pages est approximatif) ;
    - `inventaire.csv` : l'inventaire d'un petit fonds d'archives.

    Pas besoin de comprendre tout son contenu pour l'instant (mais vous en êtes capables !).
    """,

    Code('''
      import os
      import json
      import csv

      dossier = os.path.join(os.getcwd(), "donnees_exercices")
      if not os.path.isdir(dossier):
        os.mkdir(dossier)  # os.mkdir crée un dossier

      poeme = """Demain, dès l'aube, à l'heure où blanchit la campagne,
      Je partirai. Vois-tu, je sais que tu m'attends.
      J'irai par la forêt, j'irai par la montagne.
      Je ne puis demeurer loin de toi plus longtemps.

      Je marcherai les yeux fixés sur mes pensées,
      Sans rien voir au dehors, sans entendre aucun bruit,
      Seul, inconnu, le dos courbé, les mains croisées,
      Triste, et le jour pour moi sera comme la nuit.

      Je ne regarderai ni l'or du soir qui tombe,
      Ni les voiles au loin descendant vers Harfleur,
      Et quand j'arriverai, je mettrai sur ta tombe
      Un bouquet de houx vert et de bruyère en fleur.
      """
      f = open(os.path.join(dossier, "demain_des_laube.txt"), "w", encoding="utf-8")
      f.write(poeme)
      f.close()

      corpus = [
        {"titre": "Le Rouge et le Noir", "auteur": "Stendhal", "annee": 1830, "pages": 576},
        {"titre": "Le Père Goriot", "auteur": "Honoré de Balzac", "annee": 1835, "pages": 384},
        {"titre": "Madame Bovary", "auteur": "Gustave Flaubert", "annee": 1857, "pages": 480},
        {"titre": "Les Misérables", "auteur": "Victor Hugo", "annee": 1862, "pages": 1900},
        {"titre": "Notre-Dame de Paris", "auteur": "Victor Hugo", "annee": 1831, "pages": 940},
        {"titre": "Germinal", "auteur": "Émile Zola", "annee": 1885, "pages": 592},
        {"titre": "Bel-Ami", "auteur": "Guy de Maupassant", "annee": 1885, "pages": 416},
        {"titre": "L'Assommoir", "auteur": "Émile Zola", "annee": 1877, "pages": 568}
      ]
      f = open(os.path.join(dossier, "corpus.json"), "w", encoding="utf-8")
      json.dump(corpus, f, indent=4, ensure_ascii=False)
      f.close()

      inventaire = [
        ["cote", "description", "date", "boite"],
        ["1J1", "Correspondance familiale", "1890", "B1"],
        ["1J2", "Actes notariés", "1902", "B1"],
        ["1J3", "Photographies", "1925", "B2"],
        ["1J4", "Cartes postales", "1931", "B2"],
        ["1J5", "Carnets de voyage", "1936", "B2"],
        ["1J6", "Coupures de presse", "1948", "B3"]
      ]
      f = open(os.path.join(dossier, "inventaire.csv"), "w", encoding="utf-8", newline="")
      writer = csv.writer(f)
      for ligne in inventaire:
        writer.writerow(ligne)
      f.close()

      # On supprime ces variables pour que vous alliez bien chercher les données dans les fichiers !
      del poeme, corpus, inventaire
      print("Fichiers créés dans", dossier, ":", os.listdir(dossier))
    '''),

    "## Partie A : chemins et fichiers texte",

    Exercice(
      titre="Trouver ses fichiers",
      niveau=1,
      enonce="""
        Avec `os.getcwd()` et `os.path.join()`, construisez le chemin vers chacun des trois fichiers du dossier
        `donnees_exercices`, et rangez-les dans les variables `chemin_poeme`, `chemin_corpus` et `chemin_inventaire`.
        Vérifiez avec `os.path.isfile()` que Python les trouve bien.
      """,
      depart="""
        chemin_poeme = ...
        chemin_corpus = ...
        chemin_inventaire = ...
      """,
      solution="""
        racine = os.getcwd()
        chemin_poeme = os.path.join(racine, "donnees_exercices", "demain_des_laube.txt")
        chemin_corpus = os.path.join(racine, "donnees_exercices", "corpus.json")
        chemin_inventaire = os.path.join(racine, "donnees_exercices", "inventaire.csv")

        print(os.path.isfile(chemin_poeme), os.path.isfile(chemin_corpus), os.path.isfile(chemin_inventaire))
      """,
      verif="""
        assert os.path.isfile(chemin_poeme), "Python ne trouve pas chemin_poeme. Avez-vous exécuté la cellule de préparation ?"
        assert os.path.isfile(chemin_corpus), "Python ne trouve pas chemin_corpus."
        assert os.path.isfile(chemin_inventaire), "Python ne trouve pas chemin_inventaire."
        assert chemin_poeme.endswith("demain_des_laube.txt"), "chemin_poeme ne pointe pas vers le poème."
        assert chemin_corpus.endswith("corpus.json"), "chemin_corpus ne pointe pas vers corpus.json."
        assert chemin_inventaire.endswith("inventaire.csv"), "chemin_inventaire ne pointe pas vers inventaire.csv."
        print("Bravo ! 🎉")
      """,
    ),

    """
    > 💡 **Rappel : l'encodage**
    >
    > Pour lire un fichier qui contient des accents, précisez toujours l'encodage : `open(chemin, encoding="utf-8")`.
    > Sur Mac et dans Colab ça marche souvent sans, mais sous Windows vous obtiendrez des caractères bizarres
    > (`dÃ¨s` au lieu de `dès`) ou une erreur !
    """,

    Exercice(
      titre="Lire le poème",
      niveau=1,
      enonce="""
        1. Ouvrez et lisez le poème ; mettez son contenu dans une variable `texte` et imprimez-le.
           N'oubliez pas de fermer le fichier !
        2. Mettez le nombre de caractères du poème dans une variable `nb_caracteres` (indice : `len()`).
      """,
      depart="""
        texte = ...
        nb_caracteres = ...
      """,
      solution="""
        f = open(chemin_poeme, encoding="utf-8")
        texte = f.read()
        f.close()

        print(texte)

        nb_caracteres = len(texte)
        print(nb_caracteres, "caractères")
      """,
      verif="""
        assert type(texte) == str, "texte doit être un string : avez-vous utilisé .read() ?"
        assert texte.startswith("Demain, dès l'aube"), "texte ne contient pas le poème (ou les accents sont mal lus : encoding=\\"utf-8\\")."
        assert nb_caracteres == 580, "nb_caracteres n'a pas la bonne valeur."
        print("Bravo ! 🎉")
      """,
    ),

    """
    > 💡 **Rappel : quelques méthodes des strings**
    >
    > Comme `f.read()` pour un fichier, les strings ont leurs propres méthodes (on écrit la variable, un point,
    > puis la méthode). Elles ne modifient pas le string d'origine : elles en **renvoient** un nouveau.
    > - `texte.lower()` : tout en minuscules ; `texte.upper()` : tout en majuscules ;
    > - `texte.split()` : découpe le texte en une liste de mots (en coupant sur les espaces et les sauts de ligne) ;
    >   `texte.split("\\n")` découpe sur les sauts de ligne (`"\\n"`), donc en lignes ;
    > - `mot.strip(".,;")` : enlève les caractères indiqués au début et à la fin du mot ;
    > - `texte.count("a")` : compte le nombre d'occurrences de `"a"` dans le texte.
    >
    > Et le mot clé `in` permet de savoir si un élément est dans une liste, ou si une clé est dans un dictionnaire :
    > `if "je" in mon_dict:`.
    """,

    Code("""
      phrase = "Je partirai. Vois-tu, je sais que tu m'attends."
      print(phrase.lower())
      print(phrase.split())
      print("Vois-tu,".strip(".,;"))
      print(phrase.count("e"))
      print("je" in ["je", "tu", "il"])
    """),

    Exercice(
      titre="Compter les vers et les mots",
      niveau=1,
      enonce="""
        1. Mettez le nombre de **mots** du poème dans une variable `nb_mots`.
        2. Mettez le nombre de **vers** dans une variable `nb_vers`. Attention : les lignes vides entre les
           strophes ne sont pas des vers ! (Indice : une boucle, une condition et `len()`.)
      """,
      depart="""
        nb_mots = ...
        nb_vers = ...
      """,
      solution="""
        mots = texte.split()
        nb_mots = len(mots)

        nb_vers = 0
        for ligne in texte.split("\\n"):
          if ligne != "":
            nb_vers = nb_vers + 1

        print(nb_mots, "mots et", nb_vers, "vers")
      """,
      verif="""
        assert nb_mots == 104, f"Le poème contient 104 mots, et non {nb_mots}."
        assert nb_vers == 12, f"Le poème contient 12 vers (3 strophes de 4 vers), et non {nb_vers}."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Fréquence des mots",
      niveau=2,
      enonce="""
        Créez une fonction `frequences` qui prend un texte et qui renvoie un dictionnaire donnant le nombre
        d'occurrences de chaque mot, par exemple `{"demain": 1, "dès": 1, "l'aube": 1, ...}`.
        - Les mots doivent être en **minuscules** (« Je » et « je » sont le même mot) ;
        - la ponctuation `.,;:!?` au début et à la fin des mots doit être enlevée ;
        - s'il ne reste rien du mot (par exemple pour un `!` isolé), on l'ignore.

        C'est le même principe que l'exercice de fin de séance qui comptait les lettres !
      """,
      depart="""
        def frequences(texte):
          # Votre code ici
          pass

        print(frequences(texte))
      """,
      solution="""
        def frequences(texte):
          compteur = {}
          for mot in texte.lower().split():
            mot = mot.strip(".,;:!?")
            if mot != "":
              if mot in compteur:
                compteur[mot] = compteur[mot] + 1
              else:
                compteur[mot] = 1
          return compteur

        print(frequences(texte))
      """,
      verif="""
        assert frequences("Le chat. le chien, LE chat !") == {"le": 3, "chat": 2, "chien": 1}, "Testez votre fonction avec \\"Le chat. le chien, LE chat !\\" : on devrait obtenir {'le': 3, 'chat': 2, 'chien': 1}."
        assert frequences(texte)["je"] == 6, "Le mot \\"je\\" apparaît 6 fois dans le poème."
        assert frequences(texte)["la"] == 4, "Le mot \\"la\\" apparaît 4 fois dans le poème."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Le mot le plus fréquent",
      niveau=2,
      enonce="""
        Créez une fonction `plus_frequent` qui prend un dictionnaire de fréquences (comme celui renvoyé par
        `frequences`) et qui renvoie le mot qui a le plus d'occurrences.

        Indice : on peut parcourir les clés d'un dictionnaire avec une boucle `for cle in mon_dict:`.
        Gardez en mémoire, dans deux variables, le meilleur mot trouvé jusqu'ici et son nombre d'occurrences.
      """,
      depart="""
        def plus_frequent(freqs):
          # Votre code ici
          pass

        print(plus_frequent(frequences(texte)))
      """,
      solution="""
        def plus_frequent(freqs):
          meilleur_mot = None
          meilleur_nombre = 0
          for mot in freqs:
            if freqs[mot] > meilleur_nombre:
              meilleur_mot = mot
              meilleur_nombre = freqs[mot]
          return meilleur_mot

        print(plus_frequent(frequences(texte)))
      """,
      verif="""
        assert plus_frequent({"a": 1, "b": 5, "c": 2}) == "b", "plus_frequent({'a': 1, 'b': 5, 'c': 2}) devrait renvoyer 'b'."
        assert plus_frequent({"x": 3}) == "x", "plus_frequent({'x': 3}) devrait renvoyer 'x'."
        assert plus_frequent(frequences(texte)) == "je", "Le mot le plus fréquent du poème est \\"je\\"."
        print("Bravo ! 🎉")
      """,
    ),

    "## Partie B : fichiers JSON",

    Exercice(
      titre="Explorer le corpus",
      niveau=2,
      enonce="""
        1. Lisez le fichier `corpus.json` avec `json.load()` et mettez son contenu dans une variable `corpus`.
           (Comme `anscombe.json` dans le cours, c'est une **liste** de dictionnaires.)
        2. Créez une liste `recents` contenant les titres des romans publiés **après** 1850.
        3. Calculez le nombre total de pages du corpus dans une variable `total_pages`.
      """,
      depart="""
        corpus = ...
        recents = ...
        total_pages = ...
      """,
      solution="""
        f = open(chemin_corpus, encoding="utf-8")
        corpus = json.load(f)
        f.close()

        recents = []
        total_pages = 0
        for roman in corpus:
          if roman["annee"] > 1850:
            recents.append(roman["titre"])
          total_pages = total_pages + roman["pages"]

        print(recents)
        print(total_pages, "pages au total")
      """,
      verif="""
        assert type(corpus) == list and len(corpus) == 8, "corpus devrait être une liste de 8 romans."
        assert recents == ["Madame Bovary", "Les Misérables", "Germinal", "Bel-Ami", "L'Assommoir"], "recents ne contient pas les bons titres (dans l'ordre du fichier)."
        assert total_pages == 5856, f"Le total des pages devrait être 5856, et non {total_pages}."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Enrichir le corpus",
      niveau=2,
      enonce="""
        1. Ajoutez un nouveau roman de votre choix à la liste `corpus` (un dictionnaire avec les mêmes clés).
        2. Enregistrez la liste complète dans un nouveau fichier `corpus_complet.json`, dans le dossier
           `donnees_exercices`, avec `json.dump()` et `indent=4`. Mettez son chemin dans `chemin_corpus_complet`.

        > 💡 Par défaut, `json.dump()` remplace les accents par des codes comme `\\u00e9`. Pour garder un fichier
        > lisible, ajoutez l'argument `ensure_ascii=False` (et ouvrez le fichier avec `encoding="utf-8"`).

        Ouvrez ensuite le fichier dans Colab (double-clic dans le panneau « Fichiers ») pour admirer le résultat.
      """,
      depart="""
        chemin_corpus_complet = ...
      """,
      solution="""
        corpus.append({"titre": "Vingt mille lieues sous les mers", "auteur": "Jules Verne", "annee": 1870, "pages": 608})

        chemin_corpus_complet = os.path.join(os.getcwd(), "donnees_exercices", "corpus_complet.json")
        f = open(chemin_corpus_complet, "w", encoding="utf-8")
        json.dump(corpus, f, indent=4, ensure_ascii=False)
        f.close()
      """,
      verif="""
        assert os.path.isfile(chemin_corpus_complet), "Le fichier corpus_complet.json n'existe pas."
        f = open(chemin_corpus_complet, encoding="utf-8")
        relu = json.load(f)
        f.close()
        assert len(relu) == 9, f"Le fichier devrait contenir 9 romans, il en contient {len(relu)}."
        for cle in ["titre", "auteur", "annee", "pages"]:
          assert cle in relu[-1], f"Il manque la clé {cle!r} dans le roman ajouté."
        print("Bravo ! 🎉")
      """,
    ),

    "## Partie C : fichiers CSV",

    Exercice(
      titre="Lire l'inventaire",
      niveau=2,
      enonce="""
        Lisez le fichier `inventaire.csv` avec `csv.reader()`, et créez une liste `cotes_b2` contenant les cotes
        de tous les documents rangés dans la boîte `"B2"`.

        Attention : la première ligne du fichier est un en-tête (`cote, description, date, boite`), pas un document !
        Indice : `enumerate()` vous donne le numéro de la ligne.
      """,
      depart="""
        cotes_b2 = ...
      """,
      solution="""
        cotes_b2 = []

        f = open(chemin_inventaire, encoding="utf-8")
        lecteur = csv.reader(f)
        for numero, ligne in enumerate(lecteur):
          # On saute l'en-tête (ligne 0). Chaque ligne est une liste : [cote, description, date, boite]
          if numero > 0 and ligne[3] == "B2":
            cotes_b2.append(ligne[0])
        f.close()

        print(cotes_b2)
      """,
      verif="""
        assert cotes_b2 == ["1J3", "1J4", "1J5"], f"cotes_b2 devrait valoir ['1J3', '1J4', '1J5'], et non {cotes_b2}."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Un tableau des auteurs",
      niveau=2,
      enonce="""
        À partir de la liste `corpus` (lue à l'exercice « Explorer le corpus »), créez un fichier `auteurs.csv`
        dans le dossier `donnees_exercices`, avec une ligne d'en-tête `auteur,nb_romans` puis une ligne par auteur
        indiquant son nombre de romans dans le corpus. Mettez son chemin dans `chemin_auteurs`.

        Indices :
        - commencez par compter les romans de chaque auteur dans un dictionnaire (comme dans « Fréquence des mots ») ;
        - ouvrez le fichier avec `open(chemin, "w", encoding="utf-8", newline="")` : sans `newline=""`, Windows
          ajoute des lignes vides entre chaque ligne du CSV.

        Ouvrez ensuite le fichier dans Colab : on peut aussi l'ouvrir dans un tableur comme Excel ou LibreOffice !
      """,
      depart="""
        chemin_auteurs = ...
      """,
      solution="""
        # On relit le corpus d'origine (la liste corpus a pu être modifiée à l'exercice précédent) :
        f = open(chemin_corpus, encoding="utf-8")
        corpus = json.load(f)
        f.close()

        nb_romans = {}
        for roman in corpus:
          auteur = roman["auteur"]
          if auteur in nb_romans:
            nb_romans[auteur] = nb_romans[auteur] + 1
          else:
            nb_romans[auteur] = 1

        chemin_auteurs = os.path.join(os.getcwd(), "donnees_exercices", "auteurs.csv")
        f = open(chemin_auteurs, "w", encoding="utf-8", newline="")
        writer = csv.writer(f)
        writer.writerow(["auteur", "nb_romans"])
        for auteur in nb_romans:
          writer.writerow([auteur, nb_romans[auteur]])
        f.close()
      """,
      verif="""
        assert os.path.isfile(chemin_auteurs), "Le fichier auteurs.csv n'existe pas."
        f = open(chemin_auteurs, encoding="utf-8")
        lignes = list(csv.reader(f))
        f.close()
        assert lignes[0] == ["auteur", "nb_romans"], "La première ligne doit être l'en-tête auteur,nb_romans."
        assert len(lignes) == 7, f"Le fichier devrait contenir 7 lignes (l'en-tête + 6 auteurs), et non {len(lignes)}."
        assert ["Victor Hugo", "2"] in lignes, "Victor Hugo devrait avoir 2 romans."
        assert ["Stendhal", "1"] in lignes, "Stendhal devrait avoir 1 roman."
        print("Bravo ! 🎉")
      """,
    ),

    "## Partie D : mini-projet",

    Exercice(
      titre="Fiche d'analyse automatique",
      niveau=3,
      enonce="""
        Créez une fonction `analyser_fichier` qui prend deux arguments, `chemin_entree` (un fichier texte) et
        `chemin_sortie` (un fichier JSON à créer), et qui :
        1. lit le fichier texte ;
        2. calcule un dictionnaire contenant les clés `"nb_caracteres"`, `"nb_mots"`, `"nb_lignes"` (sans compter
           les lignes vides) et `"mot_plus_frequent"` ;
        3. enregistre ce dictionnaire dans le fichier JSON ;
        4. renvoie ce dictionnaire.

        Réutilisez vos fonctions `frequences` et `plus_frequent` ! Testez ensuite votre fonction sur le poème,
        puis sur un autre texte de votre choix (par exemple le `README.md` du dossier `sample_data` de Colab).
      """,
      depart="""
        def analyser_fichier(chemin_entree, chemin_sortie):
          # Votre code ici
          pass

        chemin_analyse = os.path.join(os.getcwd(), "donnees_exercices", "analyse_poeme.json")
        print(analyser_fichier(chemin_poeme, chemin_analyse))
      """,
      solution="""
        def analyser_fichier(chemin_entree, chemin_sortie):
          f = open(chemin_entree, encoding="utf-8")
          contenu = f.read()
          f.close()

          nb_lignes = 0
          for ligne in contenu.split("\\n"):
            if ligne != "":
              nb_lignes = nb_lignes + 1

          analyse = {
            "nb_caracteres": len(contenu),
            "nb_mots": len(contenu.split()),
            "nb_lignes": nb_lignes,
            "mot_plus_frequent": plus_frequent(frequences(contenu))
          }

          f = open(chemin_sortie, "w", encoding="utf-8")
          json.dump(analyse, f, indent=4, ensure_ascii=False)
          f.close()

          return analyse

        chemin_analyse = os.path.join(os.getcwd(), "donnees_exercices", "analyse_poeme.json")
        print(analyser_fichier(chemin_poeme, chemin_analyse))
      """,
      verif="""
        attendu = {"nb_caracteres": 580, "nb_mots": 104, "nb_lignes": 12, "mot_plus_frequent": "je"}
        resultat = analyser_fichier(chemin_poeme, chemin_analyse)
        assert resultat == attendu, f"analyser_fichier devrait renvoyer {attendu}, et non {resultat}."
        f = open(chemin_analyse, encoding="utf-8")
        assert json.load(f) == attendu, "Le fichier JSON ne contient pas la bonne analyse."
        f.close()
        print("Bravo ! 🎉")
      """,
    ),
  ],
}
