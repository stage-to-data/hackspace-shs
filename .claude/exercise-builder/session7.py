from build import Code, Exercice

SESSION = {
  "numero": 7,
  "dossier": "session-7",
  "intro": """
    Ces exercices reprennent la séance 7 : la visualisation de données avec `matplotlib`, la manipulation de
    tableaux avec `pandas`, et un premier pas en apprentissage automatique avec `scikit-learn` (réduction de
    dimension et clustering).
  """,
  "items": [
    "## Préparation",

    """
    Exécutez cette cellule : elle importe les packages et crée deux fichiers CSV :
    - `basic-data.csv` : le fichier utilisé en cours ;
    - `oeuvres.csv` : une quinzaine d'œuvres littéraires du XIXe siècle (le nombre de pages est approximatif).
    """,

    Code("""
      import os
      import csv

      import matplotlib.pyplot as plt
      import pandas as pd

      with open(os.path.join(os.getcwd(), "basic-data.csv"), "w", encoding="utf-8") as f:
        f.write("1, 2, 3, 4, 5, 6\\n40, 30, 10, 5, 5, 10\\n1, 3, 9, 10, 6, 8\\n")

      oeuvres = [
        ["titre", "auteur", "annee", "genre", "pages"],
        ["Le Rouge et le Noir", "Stendhal", 1830, "roman", 576],
        ["Hernani", "Victor Hugo", 1830, "théâtre", 180],
        ["Le Père Goriot", "Honoré de Balzac", 1835, "roman", 384],
        ["Ruy Blas", "Victor Hugo", 1838, "théâtre", 200],
        ["Les Contemplations", "Victor Hugo", 1856, "poésie", 480],
        ["Les Fleurs du mal", "Charles Baudelaire", 1857, "poésie", 256],
        ["Madame Bovary", "Gustave Flaubert", 1857, "roman", 480],
        ["Les Misérables", "Victor Hugo", 1862, "roman", 1900],
        ["Poèmes saturniens", "Paul Verlaine", 1866, "poésie", 120],
        ["Une saison en enfer", "Arthur Rimbaud", 1873, "poésie", 60],
        ["L'Assommoir", "Émile Zola", 1877, "roman", 568],
        ["Germinal", "Émile Zola", 1885, "roman", 592],
        ["Bel-Ami", "Guy de Maupassant", 1885, "roman", 416],
        ["Ubu roi", "Alfred Jarry", 1896, "théâtre", 90],
        ["Cyrano de Bergerac", "Edmond Rostand", 1897, "théâtre", 220]
      ]
      with open(os.path.join(os.getcwd(), "oeuvres.csv"), "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for ligne in oeuvres:
          writer.writerow(ligne)

      del oeuvres
      print("Fichiers créés !")
    """),

    "## Partie A : matplotlib",

    Exercice(
      titre="Réparer le graphique du cours",
      niveau=1,
      enonce="""
        Nous avons vu en cours que le premier graphique de `basic-data.csv` avait un problème : sur l'axe vertical,
        les valeurs étaient dans le désordre !

        C'est parce que `csv.reader` lit tout comme des **strings** : matplotlib ne sait pas que `" 30"` est un
        nombre, il le traite comme une étiquette. Sans regarder la solution du cours, lisez le fichier et créez deux
        listes d'**integers** : `x` (la première ligne) et `y` (la deuxième ligne). Puis tracez `y` en fonction de `x` avec `plt.plot()`, avec un
        titre et le nom des axes.

        Indice : `int(" 30")` vaut `30` (les espaces sont ignorés).
      """,
      depart="""
        x = ...
        y = ...
      """,
      solution="""
        donnees = []
        with open(os.path.join(os.getcwd(), "basic-data.csv"), encoding="utf-8") as f:
          for ligne in csv.reader(f):
            nombres = []
            for valeur in ligne:
              nombres.append(int(valeur))
            donnees.append(nombres)

        x = donnees[0]
        y = donnees[1]

        plt.plot(x, y)
        plt.title("Le graphique du cours, réparé")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()
      """,
      verif="""
        assert x == [1, 2, 3, 4, 5, 6], f"x devrait valoir [1, 2, 3, 4, 5, 6], et non {x}."
        assert y == [40, 30, 10, 5, 5, 10], f"y devrait valoir [40, 30, 10, 5, 5, 10], et non {y}."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Un diagramme en barres",
      niveau=1,
      enonce="""
        Le dictionnaire `publications` donne le nombre d'œuvres publiées par décennie dans notre corpus.
        Tracez-le en diagramme en barres avec `plt.bar()` (les décennies en abscisse, les nombres en ordonnée),
        ajoutez un titre et des noms d'axes, et enregistrez l'image dans `publications.png`.

        ⚠ Il faut appeler `plt.savefig()` **avant** `plt.show()` : après `show()`, la figure est vidée !

        Indice : `list(mon_dict.keys())` donne la liste des clés d'un dictionnaire, `list(mon_dict.values())`
        la liste de ses valeurs.
      """,
      depart="""
        publications = {"1830": 4, "1850": 3, "1860": 2, "1870": 2, "1880": 2, "1890": 2}

        # Votre code ici
      """,
      solution="""
        publications = {"1830": 4, "1850": 3, "1860": 2, "1870": 2, "1880": 2, "1890": 2}

        plt.bar(list(publications.keys()), list(publications.values()))
        plt.title("Œuvres publiées par décennie")
        plt.xlabel("Décennie")
        plt.ylabel("Nombre d'œuvres")
        plt.savefig("publications.png")
        plt.show()
      """,
      verif="""
        assert os.path.isfile("publications.png"), "Le fichier publications.png n'existe pas : avez-vous appelé plt.savefig() ?"
        assert os.path.getsize("publications.png") > 5000, "L'image est vide : appelez plt.savefig() avant plt.show() !"
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Deux graphiques côte à côte",
      niveau=2,
      enonce="""
        Avec `plt.subplots(1, 2)`, créez une figure contenant deux graphiques côte à côte (mettez-la dans une
        variable `figure`) :
        - à gauche, la courbe de `y` en fonction de `x` (exercice 1) ;
        - à droite, un diagramme en barres de la troisième ligne de `basic-data.csv` en fonction de `x`.

        Donnez un titre à chaque graphique avec `.set_title()`, et utilisez `figure.tight_layout()` pour que tout
        s'affiche bien.

        Indice : `plt.subplots(1, 2)` renvoie la figure et une **liste** de deux graphiques.
      """,
      depart="""
        figure = ...
      """,
      solution="""
        z = [1, 3, 9, 10, 6, 8]  # on pourrait aussi relire le fichier : c'est donnees[2] dans le corrigé de l'exercice 1

        figure, graphiques = plt.subplots(1, 2, figsize=(10, 4))

        graphiques[0].plot(x, y)
        graphiques[0].set_title("Deuxième ligne")

        graphiques[1].bar(x, z, color="orange")
        graphiques[1].set_title("Troisième ligne")

        figure.tight_layout()
        plt.show()
      """,
      verif="""
        assert len(figure.axes) == 2, "La figure devrait contenir 2 graphiques."
        assert figure.axes[0].get_title() != "" and figure.axes[1].get_title() != "", "Chaque graphique devrait avoir un titre."
        print("Bravo ! 🎉")
      """,
    ),

    "## Partie B : pandas",

    """
    > 💡 **Rappel et nouveautés pandas**
    >
    > `pd.read_csv(chemin)` lit un CSV dans un **DataFrame** (un tableau), et se débrouille tout seul avec
    > l'en-tête et les types des colonnes. Ensuite :
    > - `df.head()` affiche les premières lignes ; `len(df)` donne le nombre de lignes ;
    > - `df["pages"]` sélectionne une colonne ; `df["pages"].mean()`, `.sum()`, `.max()`... calculent des statistiques ;
    > - `df[df["annee"] > 1850]` ne garde que les lignes qui respectent la condition ;
    > - `df.groupby("genre").size()` compte le nombre de lignes pour chaque genre ;
    >   `df.groupby("genre")["pages"].mean()` calcule la moyenne des pages pour chaque genre.
    """,

    Exercice(
      titre="Explorer le tableau des œuvres",
      niveau=2,
      enonce="""
        1. Lisez `oeuvres.csv` avec pandas dans une variable `df`, et affichez les premières lignes.
        2. Mettez le nombre moyen de pages dans `moyenne_pages`.
        3. Mettez le nombre d'œuvres publiées après 1850 dans `nb_apres_1850`.
        4. Mettez le nombre d'œuvres par genre dans `par_genre`.
        5. Mettez le titre de l'œuvre la plus longue dans `plus_longue`.
           Indice : `df["pages"].idxmax()` donne le numéro de la ligne où se trouve le maximum, et
           `df.loc[numero, "titre"]` la valeur de la colonne `titre` à cette ligne.
      """,
      depart="""
        df = ...
        moyenne_pages = ...
        nb_apres_1850 = ...
        par_genre = ...
        plus_longue = ...
      """,
      solution="""
        df = pd.read_csv(os.path.join(os.getcwd(), "oeuvres.csv"))
        print(df.head())

        moyenne_pages = df["pages"].mean()
        nb_apres_1850 = len(df[df["annee"] > 1850])
        par_genre = df.groupby("genre").size()
        plus_longue = df.loc[df["pages"].idxmax(), "titre"]

        print(moyenne_pages, nb_apres_1850, plus_longue)
        print(par_genre)
      """,
      verif="""
        assert len(df) == 15, "df devrait contenir 15 œuvres."
        assert round(moyenne_pages, 1) == 434.8, f"La moyenne des pages devrait être 434.8, et non {moyenne_pages}."
        assert nb_apres_1850 == 11, f"11 œuvres ont été publiées après 1850, et non {nb_apres_1850}."
        assert par_genre["roman"] == 7 and par_genre["poésie"] == 4 and par_genre["théâtre"] == 4, "par_genre n'a pas les bonnes valeurs."
        assert plus_longue == "Les Misérables", f"L'œuvre la plus longue est Les Misérables, et non {plus_longue!r}."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Un camembert des genres",
      niveau=1,
      enonce="""
        Avec `plt.pie()`, dessinez la répartition des œuvres par genre à partir de `par_genre`, avec le nom de
        chaque genre en étiquette. Enregistrez l'image dans `genres.png`.

        Indices : `par_genre.values` donne les nombres, `par_genre.index` les noms des genres.
        Bonus : l'argument `autopct="%1.0f%%"` affiche les pourcentages.
      """,
      depart="""
        # Votre code ici
      """,
      solution="""
        plt.pie(par_genre.values, labels=par_genre.index, autopct="%1.0f%%")
        plt.title("Répartition des œuvres par genre")
        plt.savefig("genres.png")
        plt.show()
      """,
      verif="""
        assert os.path.isfile("genres.png"), "Le fichier genres.png n'existe pas."
        assert os.path.getsize("genres.png") > 5000, "L'image est vide : appelez plt.savefig() avant plt.show() !"
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Longueur des œuvres dans le temps",
      niveau=2,
      enonce="""
        Dessinez un nuage de points (`plt.scatter()`) avec l'année de publication en abscisse et le nombre de pages
        en ordonnée, avec **une couleur par genre** et une légende. Enregistrez l'image dans `longueur.png`.

        Inspirez-vous du code du cours : une boucle `for genre, groupe in df.groupby("genre"):` donne, pour chaque
        genre, le sous-tableau des œuvres de ce genre.
      """,
      depart="""
        couleurs = {"roman": "tab:blue", "poésie": "tab:orange", "théâtre": "tab:green"}

        # Votre code ici
      """,
      solution="""
        couleurs = {"roman": "tab:blue", "poésie": "tab:orange", "théâtre": "tab:green"}

        plt.figure(figsize=(8, 5))
        for genre, groupe in df.groupby("genre"):
          plt.scatter(groupe["annee"], groupe["pages"], label=genre, color=couleurs[genre])

        plt.title("Longueur des œuvres selon leur date de publication")
        plt.xlabel("Année de publication")
        plt.ylabel("Nombre de pages")
        plt.legend()
        plt.savefig("longueur.png")
        plt.show()
      """,
      verif="""
        assert os.path.isfile("longueur.png"), "Le fichier longueur.png n'existe pas."
        assert os.path.getsize("longueur.png") > 5000, "L'image est vide : appelez plt.savefig() avant plt.show() !"
        print("Bravo ! 🎉")
      """,
    ),

    "## Partie C : mini-projets",

    Exercice(
      titre="Les mots du poème",
      niveau=3,
      enonce="""
        Visualisons le vocabulaire du poème de Victor Hugo (séances 3 et 6) :
        1. découpez `poeme` en mots en minuscules, sans la ponctuation `.,;:!?`, et ne gardez que les mots de
           **plus de 3 lettres** (liste `mots_poeme`) ;
        2. avec pandas, `pd.Series(mots_poeme).value_counts()` compte les occurrences de chaque mot, triées de la
           plus fréquente à la moins fréquente : gardez les 10 premières avec `.head(10)` dans `top10` ;
        3. tracez `top10` en barres horizontales (`plt.barh()`), et enregistrez l'image dans `mots_poeme.png`.
           Bonus : utilisez `plt.gca().invert_yaxis()` pour avoir le mot le plus fréquent en haut.
      """,
      depart="""
        poeme = \"\"\"Demain, dès l'aube, à l'heure où blanchit la campagne,
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
        Un bouquet de houx vert et de bruyère en fleur.\"\"\"

        mots_poeme = ...
        top10 = ...
      """,
      solution="""
        poeme = \"\"\"Demain, dès l'aube, à l'heure où blanchit la campagne,
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
        Un bouquet de houx vert et de bruyère en fleur.\"\"\"

        mots_poeme = []
        for mot in poeme.lower().split():
          mot = mot.strip(".,;:!?")
          if len(mot) > 3:
            mots_poeme.append(mot)

        top10 = pd.Series(mots_poeme).value_counts().head(10)
        print(top10)

        plt.barh(top10.index, top10.values)
        plt.gca().invert_yaxis()
        plt.title("Les mots les plus fréquents de « Demain, dès l'aube »")
        plt.xlabel("Nombre d'occurrences")
        plt.tight_layout()
        plt.savefig("mots_poeme.png")
        plt.show()
      """,
      verif="""
        for mot in mots_poeme:
          assert len(mot) > 3, f"{mot!r} a 3 lettres ou moins."
          assert mot == mot.lower() and not mot.endswith(","), f"{mot!r} n'est pas nettoyé."
        assert len(top10) == 10, "top10 devrait contenir 10 mots."
        assert top10.iloc[0] == 2, "Les mots de plus de 3 lettres les plus fréquents apparaissent 2 fois."
        for mot in ["j'irai", "loin", "sans", "tombe"]:
          assert mot in top10.index, f"{mot!r} apparaît 2 fois : il devrait être dans top10."
        assert os.path.isfile("mots_poeme.png"), "Le fichier mots_poeme.png n'existe pas."
        print("Bravo ! 🎉")
      """,
    ),

    """
    > 💡 **Rappel : le pipeline scikit-learn du cours**
    >
    > Données → **standardisation** (`StandardScaler`, pour que toutes les colonnes aient la même échelle) →
    > **réduction de dimension** (`TSNE`, pour passer de nombreuses colonnes à 2, qu'on peut dessiner) →
    > **clustering** (`KMeans`, pour regrouper les points qui se ressemblent) → visualisation.
    >
    > En cours, nos données étaient purement aléatoires : il n'y avait donc aucun groupe à trouver !
    > Ici, `make_blobs()` fabrique des données qui contiennent de vrais groupes, cachés dans 10 dimensions.
    """,

    Exercice(
      titre="Retrouver des groupes cachés",
      niveau=3,
      enonce="""
        1. Exécutez le début de la cellule, qui crée un tableau `donnees` de 300 lignes et 10 colonnes.
        2. Standardisez les données avec `StandardScaler().fit_transform()`.
        3. Réduisez-les à 2 dimensions avec `TSNE(n_components=2, random_state=0)` ; mettez le résultat dans `reduit`.
        4. Appliquez `KMeans(n_clusters=3, n_init=10, random_state=0)` sur `reduit`, et mettez les étiquettes
           trouvées (`.labels_`) dans `etiquettes_kmeans`.
        5. Dessinez le nuage de points de `reduit`, coloré par cluster. Plus simple que dans le cours : l'argument
           `c=etiquettes_kmeans` de `plt.scatter()` colore automatiquement chaque point selon son étiquette !

        Indice : `reduit[:, 0]` donne la première colonne d'un tableau numpy, `reduit[:, 1]` la deuxième
        (c'est plus simple que `np.transpose()`).
      """,
      depart="""
        from sklearn.datasets import make_blobs
        from sklearn.preprocessing import StandardScaler
        from sklearn.manifold import TSNE
        from sklearn.cluster import KMeans

        donnees, vrais_groupes = make_blobs(n_samples=300, centers=3, n_features=10, random_state=42)
        print(donnees.shape)

        reduit = ...
        etiquettes_kmeans = ...
      """,
      solution="""
        from sklearn.datasets import make_blobs
        from sklearn.preprocessing import StandardScaler
        from sklearn.manifold import TSNE
        from sklearn.cluster import KMeans

        donnees, vrais_groupes = make_blobs(n_samples=300, centers=3, n_features=10, random_state=42)
        print(donnees.shape)

        standardise = StandardScaler().fit_transform(donnees)
        reduit = TSNE(n_components=2, random_state=0).fit_transform(standardise)
        etiquettes_kmeans = KMeans(n_clusters=3, n_init=10, random_state=0).fit(reduit).labels_

        plt.scatter(reduit[:, 0], reduit[:, 1], c=etiquettes_kmeans)
        plt.title("Clusters trouvés par KMeans")
        plt.show()
      """,
      verif="""
        from sklearn.metrics import adjusted_rand_score
        assert reduit.shape == (300, 2), "reduit devrait avoir 300 lignes et 2 colonnes."
        assert len(etiquettes_kmeans) == 300, "Il devrait y avoir une étiquette par point."
        assert len(set(etiquettes_kmeans)) == 3, "KMeans devrait trouver 3 clusters."
        # adjusted_rand_score compare nos clusters aux vrais groupes : 1 = identiques, 0 = au hasard.
        score = adjusted_rand_score(vrais_groupes, etiquettes_kmeans)
        print("Score de similarité avec les vrais groupes :", round(score, 2))
        assert score > 0.9, "Les clusters trouvés ne correspondent pas aux vrais groupes : avez-vous standardisé et réduit les données ?"
        print("Bravo ! 🎉")
      """,
    ),
  ],
}
