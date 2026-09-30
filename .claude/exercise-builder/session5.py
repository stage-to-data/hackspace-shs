from build import Code, Exercice

SESSION = {
  "numero": 5,
  "dossier": "session-5",
  "intro": """
    Ces exercices reprennent la séance 5 : la programmation orientée objet. Créer une classe avec `__init__`
    et `self`, lui donner des attributs et des méthodes, créer des instances, et hériter d'une autre classe
    avec `super()`.

    Fil rouge : nous allons construire petit à petit un outil pour gérer une bibliothèque.
  """,
  "items": [
    "## Partie A : une première classe",

    Exercice(
      titre="La classe Livre",
      niveau=1,
      enonce="""
        Créez une classe `Livre` dont la méthode `__init__` prend trois arguments (`titre`, `auteur`, `annee`) et
        les range dans trois attributs du même nom.

        Créez ensuite deux instances : `livre_1` pour *Les Misérables* (Victor Hugo, 1862) et `livre_2` pour
        *Germinal* (Émile Zola, 1885), puis imprimez l'auteur de `livre_2`.
      """,
      depart="""
        class Livre:
          # Votre code ici
          pass

        livre_1 = ...
        livre_2 = ...
      """,
      solution="""
        class Livre:

          def __init__(self, titre, auteur, annee):
            self.titre = titre
            self.auteur = auteur
            self.annee = annee

        livre_1 = Livre("Les Misérables", "Victor Hugo", 1862)
        livre_2 = Livre("Germinal", "Émile Zola", 1885)

        print(livre_2.auteur)
      """,
      verif="""
        test = Livre("Madame Bovary", "Gustave Flaubert", 1857)
        assert test.titre == "Madame Bovary", "L'attribut titre n'est pas correct."
        assert test.auteur == "Gustave Flaubert", "L'attribut auteur n'est pas correct."
        assert test.annee == 1857, "L'attribut annee n'est pas correct."
        assert livre_1.titre == "Les Misérables" and livre_2.annee == 1885, "livre_1 ou livre_2 n'a pas été créé correctement."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Des méthodes",
      niveau=1,
      enonce="""
        Reprenez votre classe `Livre` (copiez-la ci-dessous) et ajoutez-lui deux méthodes :
        - `description()` qui renvoie un string du type `"Germinal (Émile Zola, 1885)"` ;
        - `age(annee_actuelle)` qui renvoie le nombre d'années écoulées depuis la publication.

        > 💡 Pour construire un string à partir de variables, on peut utiliser une **f-string** (vue en séance 4) :
        > on met un `f` devant les guillemets, et les variables entre accolades : `f"{self.titre} ({self.auteur})"`.

        N'oubliez pas : les méthodes prennent toujours `self` comme premier argument, et après avoir modifié la
        classe, il faut **recréer** les instances pour qu'elles aient les nouvelles méthodes.
      """,
      depart="""
        class Livre:
          # Votre code ici
          pass

        livre_2 = Livre("Germinal", "Émile Zola", 1885)
        print(livre_2.description())
        print(livre_2.age(2026))
      """,
      solution="""
        class Livre:

          def __init__(self, titre, auteur, annee):
            self.titre = titre
            self.auteur = auteur
            self.annee = annee

          def description(self):
            return f"{self.titre} ({self.auteur}, {self.annee})"

          def age(self, annee_actuelle):
            return annee_actuelle - self.annee

        livre_2 = Livre("Germinal", "Émile Zola", 1885)
        print(livre_2.description())
        print(livre_2.age(2026))
      """,
      verif="""
        test = Livre("Germinal", "Émile Zola", 1885)
        assert test.description() == "Germinal (Émile Zola, 1885)", f"description() renvoie {test.description()!r}."
        assert test.age(1985) == 100, "age(1985) devrait renvoyer 100 pour un livre de 1885."
        print("Bravo ! 🎉")
      """,
    ),

    """
    > 💡 **Rappel : `__str__`**
    >
    > Essayez `print(livre_2)` : Python affiche quelque chose comme `<__main__.Livre object at 0x7f...>`, pas très
    > parlant ! Comme `__init__`, il existe d'autres méthodes « spéciales » (entourées de deux tirets bas) que
    > Python appelle tout seul à certains moments. `__str__(self)` est appelée quand on fait `print()` ou `str()`
    > sur une instance : elle doit renvoyer un string.
    """,

    Exercice(
      titre="Un affichage lisible",
      niveau=2,
      enonce="""
        Ajoutez une méthode `__str__` à la classe `Livre`, qui renvoie la même chose que `description()`.
        Vérifiez que `print(livre_2)` affiche désormais `Germinal (Émile Zola, 1885)`.

        Astuce : dans une méthode, on peut appeler une autre méthode de la classe avec `self.`.
      """,
      depart="""
        class Livre:
          # Votre code ici (copiez votre classe et ajoutez __str__)
          pass

        livre_2 = Livre("Germinal", "Émile Zola", 1885)
        print(livre_2)
      """,
      solution="""
        class Livre:

          def __init__(self, titre, auteur, annee):
            self.titre = titre
            self.auteur = auteur
            self.annee = annee

          def description(self):
            return f"{self.titre} ({self.auteur}, {self.annee})"

          def age(self, annee_actuelle):
            return annee_actuelle - self.annee

          def __str__(self):
            return self.description()

        livre_2 = Livre("Germinal", "Émile Zola", 1885)
        print(livre_2)
      """,
      verif="""
        assert str(Livre("Germinal", "Émile Zola", 1885)) == "Germinal (Émile Zola, 1885)", "str(livre) ne renvoie pas la description."
        assert Livre("Germinal", "Émile Zola", 1885).age(1985) == 100, "N'oubliez pas de garder les méthodes précédentes !"
        print("Bravo ! 🎉")
      """,
    ),

    "## Partie B : des objets qui contiennent des objets",

    Exercice(
      titre="La classe Bibliotheque",
      niveau=2,
      enonce="""
        Créez une classe `Bibliotheque` :
        - `__init__(self, nom)` range le nom dans un attribut `nom`, et crée un attribut `livres` qui est une
          liste vide ;
        - `ajouter(self, livre)` ajoute un `Livre` à la liste ;
        - `nombre(self)` renvoie le nombre de livres ;
        - `par_auteur(self, auteur)` renvoie la liste des **titres** des livres de cet auteur.

        Créez ensuite une instance `ma_bibliotheque` et ajoutez-y au moins trois livres, dont deux de Victor Hugo.
      """,
      depart="""
        class Bibliotheque:
          # Votre code ici
          pass

        ma_bibliotheque = ...
      """,
      solution="""
        class Bibliotheque:

          def __init__(self, nom):
            self.nom = nom
            self.livres = []

          def ajouter(self, livre):
            self.livres.append(livre)

          def nombre(self):
            return len(self.livres)

          def par_auteur(self, auteur):
            titres = []
            for livre in self.livres:
              if livre.auteur == auteur:
                titres.append(livre.titre)
            return titres

        ma_bibliotheque = Bibliotheque("Bibliothèque du Hackspace")
        ma_bibliotheque.ajouter(Livre("Les Misérables", "Victor Hugo", 1862))
        ma_bibliotheque.ajouter(Livre("Notre-Dame de Paris", "Victor Hugo", 1831))
        ma_bibliotheque.ajouter(Livre("Germinal", "Émile Zola", 1885))

        print(ma_bibliotheque.nombre())
        print(ma_bibliotheque.par_auteur("Victor Hugo"))
      """,
      verif="""
        test = Bibliotheque("Test")
        assert test.nom == "Test", "L'attribut nom n'est pas correct."
        assert test.livres == [], "Une nouvelle bibliothèque doit avoir une liste de livres vide."
        test.ajouter(Livre("A", "X", 2000))
        test.ajouter(Livre("B", "Y", 2001))
        test.ajouter(Livre("C", "X", 2002))
        assert test.nombre() == 3, "nombre() devrait renvoyer 3 après avoir ajouté 3 livres."
        assert test.par_auteur("X") == ["A", "C"], "par_auteur(\\"X\\") devrait renvoyer ['A', 'C']."
        assert test.par_auteur("Z") == [], "par_auteur doit renvoyer une liste vide si l'auteur est absent."
        assert Bibliotheque("Autre").livres == [], "Chaque bibliothèque doit avoir sa propre liste : créez-la dans __init__ !"
        assert len(ma_bibliotheque.par_auteur("Victor Hugo")) >= 2, "ma_bibliotheque doit contenir au moins deux livres de Victor Hugo."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Le plus ancien",
      niveau=2,
      enonce="""
        Ajoutez à `Bibliotheque` une méthode `plus_ancien(self)` qui renvoie le **livre** (l'instance de `Livre`,
        pas son titre) le plus ancien de la bibliothèque, ou `None` si la bibliothèque est vide.

        Pour ne pas tout réécrire, on peut créer une nouvelle classe qui **hérite** de `Bibliotheque` et qui ajoute
        simplement la nouvelle méthode : `class BibliothequePlus(Bibliotheque):`.
      """,
      depart="""
        class BibliothequePlus(Bibliotheque):
          # Votre code ici
          pass
      """,
      solution="""
        class BibliothequePlus(Bibliotheque):

          def plus_ancien(self):
            if len(self.livres) == 0:
              return None
            ancien = self.livres[0]
            for livre in self.livres:
              if livre.annee < ancien.annee:
                ancien = livre
            return ancien

        test = BibliothequePlus("Test")
        test.ajouter(Livre("Germinal", "Émile Zola", 1885))
        test.ajouter(Livre("Le Rouge et le Noir", "Stendhal", 1830))
        test.ajouter(Livre("Les Misérables", "Victor Hugo", 1862))
        print(test.plus_ancien())
      """,
      verif="""
        test = BibliothequePlus("Test")
        assert test.plus_ancien() is None, "plus_ancien() doit renvoyer None pour une bibliothèque vide."
        rouge = Livre("Le Rouge et le Noir", "Stendhal", 1830)
        test.ajouter(Livre("Germinal", "Émile Zola", 1885))
        test.ajouter(rouge)
        test.ajouter(Livre("Les Misérables", "Victor Hugo", 1862))
        assert test.plus_ancien() is rouge, "plus_ancien() devrait renvoyer le livre Le Rouge et le Noir (l'objet, pas son titre)."
        assert test.nombre() == 3, "BibliothequePlus doit hériter des méthodes de Bibliotheque."
        print("Bravo ! 🎉")
      """,
    ),

    "## Partie C : l'héritage",

    Exercice(
      titre="Les manuscrits",
      niveau=2,
      enonce="""
        Un manuscrit est un livre particulier : il a en plus une **cote** (son identifiant dans le fonds d'archives).
        Créez une classe `Manuscrit` qui hérite de `Livre` :
        - son `__init__` prend en plus un argument `cote`, appelle le `__init__` de `Livre` avec `super()`, puis
          range la cote dans un attribut `cote` ;
        - sa méthode `description()` renvoie la description d'un livre suivie de la cote entre crochets, par exemple :
          `"Journal (Anonyme, 1789) [ms. 1J42]"`. Utilisez `super().description()` pour ne pas réécrire le début !
      """,
      depart="""
        class Manuscrit(Livre):
          # Votre code ici
          pass

        journal = Manuscrit("Journal", "Anonyme", 1789, "1J42")
        print(journal.description())
      """,
      solution="""
        class Manuscrit(Livre):

          def __init__(self, titre, auteur, annee, cote):
            super().__init__(titre, auteur, annee)
            self.cote = cote

          def description(self):
            return f"{super().description()} [ms. {self.cote}]"

        journal = Manuscrit("Journal", "Anonyme", 1789, "1J42")
        print(journal.description())
        print(journal)          # __str__ est hérité de Livre, et appelle la nouvelle description() !
        print(journal.age(2026)) # age() est hérité de Livre
      """,
      verif="""
        test = Manuscrit("Journal", "Anonyme", 1789, "1J42")
        assert test.cote == "1J42", "L'attribut cote n'est pas correct."
        assert test.titre == "Journal" and test.annee == 1789, "Les attributs de Livre doivent être définis (avec super().__init__)."
        assert test.description() == "Journal (Anonyme, 1789) [ms. 1J42]", f"description() renvoie {test.description()!r}."
        assert test.age(1889) == 100, "Un Manuscrit doit hériter de la méthode age() de Livre."
        print("Bravo ! 🎉")
      """,
    ),

    "## Partie D : mini-projets",

    Exercice(
      titre="Un analyseur de texte",
      niveau=3,
      enonce="""
        En préparation de la séance sur le traitement du langage, créez une classe `AnalyseurTexte` :
        - `__init__(self, texte)` range le texte dans un attribut `texte` ;
        - `mots(self)` renvoie la liste des mots du texte, en minuscules, sans la ponctuation `.,;:!?` au début et
          à la fin (et sans les mots vides) ;
        - `nb_mots(self)` renvoie le nombre de mots ;
        - `frequences(self)` renvoie un dictionnaire `{mot: nombre d'occurrences}` ;
        - `plus_frequent(self)` renvoie le mot le plus fréquent.

        C'est une version « orientée objet » des exercices de la séance 3 : réutilisez vos idées !
      """,
      depart="""
        class AnalyseurTexte:
          # Votre code ici
          pass

        analyseur = AnalyseurTexte("Le chat dort. Le chien dort aussi ! Le chat rêve.")
        print(analyseur.frequences())
      """,
      solution="""
        class AnalyseurTexte:

          def __init__(self, texte):
            self.texte = texte

          def mots(self):
            resultat = []
            for mot in self.texte.lower().split():
              mot = mot.strip(".,;:!?")
              if mot != "":
                resultat.append(mot)
            return resultat

          def nb_mots(self):
            return len(self.mots())

          def frequences(self):
            compteur = {}
            for mot in self.mots():
              if mot in compteur:
                compteur[mot] = compteur[mot] + 1
              else:
                compteur[mot] = 1
            return compteur

          def plus_frequent(self):
            freqs = self.frequences()
            meilleur = None
            for mot in freqs:
              if meilleur is None or freqs[mot] > freqs[meilleur]:
                meilleur = mot
            return meilleur

        analyseur = AnalyseurTexte("Le chat dort. Le chien dort aussi ! Le chat rêve.")
        print(analyseur.frequences())
      """,
      verif="""
        test = AnalyseurTexte("Le chat dort. Le chien dort aussi ! Le chat rêve.")
        assert test.mots() == ["le", "chat", "dort", "le", "chien", "dort", "aussi", "le", "chat", "rêve"], f"mots() renvoie {test.mots()}."
        assert test.nb_mots() == 10, "nb_mots() devrait renvoyer 10."
        assert test.frequences() == {"le": 3, "chat": 2, "dort": 2, "chien": 1, "aussi": 1, "rêve": 1}, "frequences() ne renvoie pas le bon dictionnaire."
        assert test.plus_frequent() == "le", "plus_frequent() devrait renvoyer \\"le\\"."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Sauvegarder sa bibliothèque",
      niveau=3,
      enonce="""
        Combinons avec la séance 3 ! Créez une classe `BibliothequeJSON` qui hérite de `BibliothequePlus`, avec :
        - une méthode `sauvegarder(self, chemin)` qui enregistre les livres dans un fichier JSON, sous forme d'une
          liste de dictionnaires `{"titre": ..., "auteur": ..., "annee": ...}` (on ne peut pas enregistrer
          directement des instances de `Livre` en JSON !) ;
        - une méthode `charger(self, chemin)` qui lit un tel fichier et ajoute à la bibliothèque un `Livre` pour
          chaque dictionnaire.

        Testez en sauvegardant une bibliothèque, puis en la chargeant dans une nouvelle instance.
      """,
      depart="""
        import os
        import json

        class BibliothequeJSON(BibliothequePlus):
          # Votre code ici
          pass
      """,
      solution="""
        import os
        import json

        class BibliothequeJSON(BibliothequePlus):

          def sauvegarder(self, chemin):
            donnees = []
            for livre in self.livres:
              donnees.append({"titre": livre.titre, "auteur": livre.auteur, "annee": livre.annee})
            with open(chemin, "w", encoding="utf-8") as f:
              json.dump(donnees, f, indent=4, ensure_ascii=False)

          def charger(self, chemin):
            with open(chemin, encoding="utf-8") as f:
              donnees = json.load(f)
            for element in donnees:
              self.ajouter(Livre(element["titre"], element["auteur"], element["annee"]))

        chemin = os.path.join(os.getcwd(), "ma_bibliotheque.json")

        originale = BibliothequeJSON("Originale")
        originale.ajouter(Livre("Les Misérables", "Victor Hugo", 1862))
        originale.ajouter(Livre("Germinal", "Émile Zola", 1885))
        originale.sauvegarder(chemin)

        copie = BibliothequeJSON("Copie")
        copie.charger(chemin)
        for livre in copie.livres:
          print(livre)
      """,
      verif="""
        chemin_test = os.path.join(os.getcwd(), "test_bibliotheque.json")
        test = BibliothequeJSON("Test")
        test.ajouter(Livre("Germinal", "Émile Zola", 1885))
        test.ajouter(Livre("Bel-Ami", "Guy de Maupassant", 1885))
        test.sauvegarder(chemin_test)
        with open(chemin_test, encoding="utf-8") as f:
          assert json.load(f) == [{"titre": "Germinal", "auteur": "Émile Zola", "annee": 1885},
                                  {"titre": "Bel-Ami", "auteur": "Guy de Maupassant", "annee": 1885}], "Le fichier JSON n'a pas le bon contenu."
        copie = BibliothequeJSON("Copie")
        copie.charger(chemin_test)
        assert copie.nombre() == 2, "Après charger(), la bibliothèque devrait contenir 2 livres."
        assert type(copie.livres[0]) == Livre and copie.livres[1].titre == "Bel-Ami", "charger() doit ajouter des instances de Livre."
        print("Bravo ! 🎉")
      """,
    ),
  ],
}
