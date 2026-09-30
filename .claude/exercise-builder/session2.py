from build import Code, Exercice

SESSION = {
  "numero": 2,
  "dossier": "session-2",
  "intro": """
    Ce notebook est une **révision des deux premières séances** : variables, types, listes, dictionnaires
    et fonctions (séance 1), puis conditions, boucles et packages (séance 2).
    Avec tout ça, vous avez les briques de base de (presque) n'importe quel programme !
  """,
  "items": [
    "## Partie A : échauffement (séance 1)",

    Exercice(
      titre="Révision express",
      niveau=1,
      enonce="""
        À partir du dictionnaire `roman` :
        1. mettez le **dernier** personnage de la liste dans une variable `dernier_personnage` ;
        2. ajoutez au dictionnaire une clé `"lieu"` avec la valeur `"Paris"` ;
        3. créez une fonction `anciennete` qui prend en arguments un roman (un dictionnaire comme celui-ci)
           et l'année actuelle, et qui **renvoie** le nombre d'années écoulées depuis sa publication.
      """,
      depart="""
        roman = {
          "titre": "Notre-Dame de Paris",
          "auteur": "Victor Hugo",
          "annee": 1831,
          "personnages": ["Esmeralda", "Quasimodo", "Frollo", "Phoebus"]
        }

        # 1.
        dernier_personnage = ...

        # 2.
        ...

        # 3.
        def anciennete(roman, annee_actuelle):
          pass
      """,
      solution="""
        roman = {
          "titre": "Notre-Dame de Paris",
          "auteur": "Victor Hugo",
          "annee": 1831,
          "personnages": ["Esmeralda", "Quasimodo", "Frollo", "Phoebus"]
        }

        # 1. roman["personnages"] est une liste ; l'index -1 donne le dernier élément
        #    (roman["personnages"][3] fonctionne aussi).
        dernier_personnage = roman["personnages"][-1]

        # 2.
        roman["lieu"] = "Paris"

        # 3.
        def anciennete(roman, annee_actuelle):
          return annee_actuelle - roman["annee"]

        print(anciennete(roman, 2026))
      """,
      verif="""
        assert dernier_personnage == "Phoebus", "dernier_personnage : roman[\\"personnages\\"] est une liste..."
        assert roman.get("lieu") == "Paris", "Il manque la clé \\"lieu\\" (ou elle n'a pas la bonne valeur)."
        assert anciennete(roman, 2031) == 200, "anciennete(roman, 2031) devrait renvoyer 200."
        assert anciennete({"annee": 2000}, 2026) == 26, "anciennete doit utiliser la clé \\"annee\\" du roman donné en argument."
        print("Bravo ! 🎉")
      """,
    ),

    "## Partie B : les conditions",

    Exercice(
      titre="Majeur ou mineur ?",
      niveau=1,
      enonce="""
        Créez une fonction `statut` qui prend un âge en argument et qui renvoie le string `"majeur"`
        si l'âge est supérieur ou égal à 18, et `"mineur"` sinon.
      """,
      depart="""
        def statut(age):
          # Votre code ici
          pass

        print(statut(12))
        print(statut(40))
      """,
      solution="""
        def statut(age):
          if age >= 18:
            return "majeur"
          else:
            return "mineur"

        print(statut(12))
        print(statut(40))
      """,
      verif="""
        assert statut(12) == "mineur", "statut(12) devrait renvoyer \\"mineur\\"."
        assert statut(40) == "majeur", "statut(40) devrait renvoyer \\"majeur\\"."
        assert statut(18) == "majeur", "statut(18) devrait renvoyer \\"majeur\\" : attention à > et >= !"
        assert statut(17) == "mineur", "statut(17) devrait renvoyer \\"mineur\\"."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Les mentions",
      niveau=2,
      enonce="""
        Créez une fonction `mention` qui prend une note sur 20 et qui renvoie :
        - `"Très bien"` si la note est supérieure ou égale à 16 ;
        - `"Bien"` si elle est supérieure ou égale à 14 ;
        - `"Assez bien"` si elle est supérieure ou égale à 12 ;
        - `"Passable"` si elle est supérieure ou égale à 10 ;
        - `"Ajourné"` sinon.

        Utilisez `if`, `elif` et `else`. Réfléchissez bien à l'**ordre** de vos conditions !
      """,
      depart="""
        def mention(note):
          # Votre code ici
          pass

        print(mention(15))
      """,
      solution="""
        def mention(note):
          # On commence par la condition la plus exigeante : dès qu'une condition est
          # validée, Python ignore les elif suivants.
          if note >= 16:
            return "Très bien"
          elif note >= 14:
            return "Bien"
          elif note >= 12:
            return "Assez bien"
          elif note >= 10:
            return "Passable"
          else:
            return "Ajourné"

        print(mention(15))
      """,
      verif="""
        attendus = {20: "Très bien", 16: "Très bien", 15.5: "Bien", 14: "Bien", 13: "Assez bien",
                    12: "Assez bien", 10: "Passable", 9.99: "Ajourné", 0: "Ajourné"}
        for note in attendus:
          assert mention(note) == attendus[note], f"mention({note}) renvoie {mention(note)!r} au lieu de {attendus[note]!r}."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Et / ou",
      niveau=2,
      enonce="""
        1. Créez une fonction `est_xixe_siecle` qui renvoie `True` si l'année donnée appartient au XIXe siècle
           (de 1801 à 1900 inclus), et `False` sinon. Utilisez `and`.
        2. Créez une fonction `est_weekend` qui renvoie `True` si le jour donné (un string comme `"lundi"`)
           est `"samedi"` ou `"dimanche"`, et `False` sinon. Utilisez `or`.
      """,
      depart="""
        def est_xixe_siecle(annee):
          # Votre code ici
          pass

        def est_weekend(jour):
          # Votre code ici
          pass
      """,
      solution="""
        def est_xixe_siecle(annee):
          if annee >= 1801 and annee <= 1900:
            return True
          else:
            return False

        def est_weekend(jour):
          if jour == "samedi" or jour == "dimanche":
            return True
          return False  # si on arrive ici, c'est que le return du if n'a pas été exécuté

        print(est_xixe_siecle(1862), est_weekend("mercredi"))
      """,
      verif="""
        assert est_xixe_siecle(1862) == True, "1862 est bien au XIXe siècle."
        assert est_xixe_siecle(1801) == True, "1801 est la première année du XIXe siècle."
        assert est_xixe_siecle(1900) == True, "1900 est la dernière année du XIXe siècle."
        assert est_xixe_siecle(1800) == False, "1800 appartient au XVIIIe siècle."
        assert est_xixe_siecle(1901) == False, "1901 appartient au XXe siècle."
        assert est_weekend("samedi") == True and est_weekend("dimanche") == True, "Le samedi et le dimanche sont le week-end !"
        assert est_weekend("mercredi") == False, "Le mercredi n'est pas le week-end (même s'il y a Hackspace)."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Chasse au bug : le pavé introuvable",
      niveau=2,
      enonce="""
        Cette fonction devrait classer un document selon son nombre de pages :
        50 pages ou moins → `"brochure"` ; de 51 à 500 pages → `"livre"` ; plus de 500 pages → `"pavé"`.

        Mais `categorie(800)` renvoie `"livre"` ! Trouvez l'erreur et corrigez-la.
      """,
      depart="""
        def categorie(nb_pages):
          if nb_pages > 50:
            return "livre"
          elif nb_pages > 500:
            return "pavé"
          else:
            return "brochure"

        print(categorie(800))
      """,
      solution="""
        # Le problème : 800 > 50 est vrai, donc la première condition est validée et Python
        # ne regarde jamais le elif. Il faut tester la condition la plus restrictive en premier.
        def categorie(nb_pages):
          if nb_pages > 500:
            return "pavé"
          elif nb_pages > 50:
            return "livre"
          else:
            return "brochure"

        print(categorie(800))
      """,
      verif="""
        assert categorie(800) == "pavé", "categorie(800) devrait renvoyer \\"pavé\\"."
        assert categorie(501) == "pavé", "categorie(501) devrait renvoyer \\"pavé\\"."
        assert categorie(500) == "livre", "categorie(500) devrait renvoyer \\"livre\\"."
        assert categorie(51) == "livre", "categorie(51) devrait renvoyer \\"livre\\"."
        assert categorie(50) == "brochure", "categorie(50) devrait renvoyer \\"brochure\\"."
        print("Bravo ! 🎉")
      """,
    ),

    "## Partie C : les boucles",

    """
    > 💡 **Rappel (et une nouveauté) : trois outils bien pratiques avec les boucles**
    >
    > - `len(ma_liste)` renvoie le nombre d'éléments d'une liste (ou le nombre de caractères d'un string).
    > - `ma_liste.append(element)` ajoute un élément à la fin d'une liste. On part souvent d'une liste vide `[]`
    >   qu'on remplit dans une boucle.
    > - **Nouveau** : `a % b` (modulo) renvoie le **reste** de la division de `a` par `b`. Par exemple `10 % 3` vaut `1`.
    >   Si `a % b == 0`, alors `a` est divisible par `b`.
    """,

    Code("""
      mots = ["archive", "corpus"]
      print(len(mots))        # 2
      print(len("Rennes"))    # 6

      mots.append("notice")
      print(mots)             # ['archive', 'corpus', 'notice']

      print(10 % 3)           # 1
      print(12 % 2 == 0)      # True : 12 est pair
    """),

    Exercice(
      titre="Une table des matières",
      niveau=1,
      enonce="""
        Avec une boucle `for` et `enumerate()`, imprimez la table des matières suivante à partir de la liste
        `chapitres` :
        ```
        Chapitre 1 : Introduction
        Chapitre 2 : Méthodologie
        Chapitre 3 : Résultats
        Chapitre 4 : Conclusion
        ```
        Attention : `enumerate()` commence à compter à 0...
      """,
      depart="""
        chapitres = ["Introduction", "Méthodologie", "Résultats", "Conclusion"]

        # Votre code ici
      """,
      solution="""
        chapitres = ["Introduction", "Méthodologie", "Résultats", "Conclusion"]

        for index, chapitre in enumerate(chapitres):
          print("Chapitre", index + 1, ":", chapitre)
      """,
    ),

    Exercice(
      titre="Faire la somme",
      niveau=1,
      enonce="""
        Créez une fonction `somme` qui prend une liste de nombres et qui renvoie leur somme,
        en utilisant une boucle `for` (sans utiliser la fonction `sum()` de Python, ce serait trop facile !).

        Indice : créez une variable `total` qui vaut 0 avant la boucle, et ajoutez-lui chaque nombre.
      """,
      depart="""
        def somme(nombres):
          # Votre code ici
          pass

        print(somme([1, 2, 3, 4]))
      """,
      solution="""
        def somme(nombres):
          total = 0
          for nombre in nombres:
            total = total + nombre
          return total

        print(somme([1, 2, 3, 4]))
      """,
      verif="""
        assert somme([1, 2, 3, 4]) == 10, "somme([1, 2, 3, 4]) devrait renvoyer 10."
        assert somme([]) == 0, "La somme d'une liste vide devrait être 0."
        assert somme([2.5, -1]) == 1.5, "somme([2.5, -1]) devrait renvoyer 1.5."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="La moyenne d'une liste",
      niveau=2,
      enonce="""
        Créez une fonction `moyenne` qui prend une liste de notes et qui renvoie leur moyenne.
        Cette fois, la liste peut contenir n'importe quel nombre de notes : utilisez une boucle et `len()`.

        Bonus : si la liste est vide, renvoyez `None` (sinon Python essaiera de diviser par zéro !).
      """,
      depart="""
        def moyenne(notes):
          # Votre code ici
          pass

        print(moyenne([10, 12, 14, 8]))
      """,
      solution="""
        def moyenne(notes):
          if len(notes) == 0:
            return None
          total = 0
          for note in notes:
            total = total + note
          return total / len(notes)

        print(moyenne([10, 12, 14, 8]))
      """,
      verif="""
        assert moyenne([10, 12, 14, 8]) == 11, "moyenne([10, 12, 14, 8]) devrait renvoyer 11."
        assert moyenne([15]) == 15, "moyenne([15]) devrait renvoyer 15."
        assert round(moyenne([0, 0, 20]), 2) == 6.67, "moyenne([0, 0, 20]) devrait renvoyer 6.666..."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Filtrer un corpus",
      niveau=2,
      enonce="""
        La liste `corpus` contient des dictionnaires qui décrivent des œuvres.
        Créez une fonction `titres_apres` qui prend un corpus et une année, et qui renvoie la **liste des titres**
        des œuvres publiées **à partir de** cette année (année incluse).

        Par exemple, `titres_apres(corpus, 1860)` doit renvoyer `['Les Misérables', 'Germinal', 'Bel-Ami']`.
      """,
      depart="""
        corpus = [
          {"titre": "Le Rouge et le Noir", "auteur": "Stendhal", "annee": 1830},
          {"titre": "Les Misérables", "auteur": "Victor Hugo", "annee": 1862},
          {"titre": "Madame Bovary", "auteur": "Gustave Flaubert", "annee": 1857},
          {"titre": "Germinal", "auteur": "Émile Zola", "annee": 1885},
          {"titre": "Bel-Ami", "auteur": "Guy de Maupassant", "annee": 1885},
        ]

        def titres_apres(corpus, annee):
          # Votre code ici
          pass

        print(titres_apres(corpus, 1860))
      """,
      solution="""
        corpus = [
          {"titre": "Le Rouge et le Noir", "auteur": "Stendhal", "annee": 1830},
          {"titre": "Les Misérables", "auteur": "Victor Hugo", "annee": 1862},
          {"titre": "Madame Bovary", "auteur": "Gustave Flaubert", "annee": 1857},
          {"titre": "Germinal", "auteur": "Émile Zola", "annee": 1885},
          {"titre": "Bel-Ami", "auteur": "Guy de Maupassant", "annee": 1885},
        ]

        def titres_apres(corpus, annee):
          titres = []
          for oeuvre in corpus:
            if oeuvre["annee"] >= annee:
              titres.append(oeuvre["titre"])
          return titres

        print(titres_apres(corpus, 1860))
      """,
      verif="""
        assert titres_apres(corpus, 1860) == ["Les Misérables", "Germinal", "Bel-Ami"], "titres_apres(corpus, 1860) ne renvoie pas la bonne liste."
        assert titres_apres(corpus, 1885) == ["Germinal", "Bel-Ami"], "Les œuvres publiées l'année donnée doivent être incluses (>=)."
        assert titres_apres(corpus, 1900) == [], "S'il n'y a aucune œuvre, la fonction doit renvoyer une liste vide."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Dépouiller un vote",
      niveau=2,
      enonce="""
        La liste `bulletins` contient les votes d'une assemblée. Créez une fonction `depouiller` qui renvoie
        un dictionnaire avec le nombre de voix pour chaque option, par exemple :
        `{"pour": 5, "contre": 3, "abstention": 2}`.

        Indice : commencez avec un dictionnaire où chaque option vaut 0, puis parcourez les bulletins.
      """,
      depart="""
        bulletins = ["pour", "contre", "pour", "abstention", "pour", "contre",
                     "pour", "abstention", "contre", "pour"]

        def depouiller(bulletins):
          # Votre code ici
          pass

        print(depouiller(bulletins))
      """,
      solution="""
        bulletins = ["pour", "contre", "pour", "abstention", "pour", "contre",
                     "pour", "abstention", "contre", "pour"]

        def depouiller(bulletins):
          resultats = {"pour": 0, "contre": 0, "abstention": 0}
          for bulletin in bulletins:
            resultats[bulletin] = resultats[bulletin] + 1
          return resultats

        print(depouiller(bulletins))
      """,
      verif="""
        assert depouiller(bulletins) == {"pour": 5, "contre": 3, "abstention": 2}, "Le décompte n'est pas bon."
        assert depouiller(["contre"]) == {"pour": 0, "contre": 1, "abstention": 0}, "Toutes les options doivent apparaître, même avec 0 voix."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Table de multiplication",
      niveau=2,
      enonce="""
        Créez une fonction `table` qui prend un nombre `n` et qui renvoie une liste contenant sa table de
        multiplication de 1 à 10 : `table(3)` doit renvoyer `[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]`.

        Utilisez `range()`. Attention : `range(10)` va de 0 à 9...
      """,
      depart="""
        def table(n):
          # Votre code ici
          pass

        print(table(3))
      """,
      solution="""
        def table(n):
          resultat = []
          for i in range(10):
            resultat.append(n * (i + 1))
          return resultat

        # Autre solution : range() accepte aussi un début et une fin (la fin est exclue) :
        # for i in range(1, 11):
        #   resultat.append(n * i)

        print(table(3))
      """,
      verif="""
        assert table(3) == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], "table(3) ne renvoie pas la bonne liste."
        assert table(7)[-1] == 70, "Le dernier élément de table(7) devrait être 70."
        assert len(table(1)) == 10, "La table doit contenir 10 éléments."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Doubler sa mise",
      niveau=2,
      enonce="""
        Vous placez une somme d'argent (`capital`) à un taux d'intérêt annuel (`taux`, en pourcentage).
        Chaque année, le capital est multiplié par `(1 + taux / 100)`.

        Créez une fonction `annees_pour_doubler` qui renvoie le **nombre d'années** nécessaires pour que le capital
        atteigne au moins le double de sa valeur de départ. Utilisez une boucle `while`.

        Par exemple, avec 1000 € à 10 %, il faut 8 ans.
      """,
      depart="""
        def annees_pour_doubler(capital, taux):
          # Votre code ici
          pass

        print(annees_pour_doubler(1000, 10))
      """,
      solution="""
        def annees_pour_doubler(capital, taux):
          objectif = capital * 2
          annees = 0
          while capital < objectif:
            capital = capital * (1 + taux / 100)
            annees = annees + 1
          return annees

        print(annees_pour_doubler(1000, 10))
      """,
      verif="""
        assert annees_pour_doubler(1000, 10) == 8, "annees_pour_doubler(1000, 10) devrait renvoyer 8."
        assert annees_pour_doubler(1000, 100) == 1, "À 100 %, le capital double en 1 an."
        assert annees_pour_doubler(50, 3) == 24, "annees_pour_doubler(50, 3) devrait renvoyer 24."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="L'exercice de fin de séance",
      niveau=2,
      enonce="""
        C'est l'exercice proposé à la fin du cours :
        1. Créez une fonction `comparer_a_cinq` qui prend une liste de nombres, et qui imprime pour chaque nombre
           s'il est plus grand, plus petit ou égal à 5. Testez-la avec `[1, 2, 3, 4, 5, 6, 7, 8, 9]`.
        2. Créez une fonction `comparer` qui prend deux nombres `n` et `seuil`, et qui, pour chaque nombre entre 0
           et `n`, imprime s'il est plus grand, plus petit ou égal à `seuil`.
      """,
      depart="""
        def comparer_a_cinq(liste):
          # Votre code ici
          pass

        def comparer(n, seuil):
          # Votre code ici
          pass

        comparer_a_cinq([1, 2, 3, 4, 5, 6, 7, 8, 9])
        comparer(10, 3)
      """,
      solution="""
        def comparer_a_cinq(liste):
          for nombre in liste:
            if nombre > 5:
              print(nombre, "est plus grand que 5")
            elif nombre < 5:
              print(nombre, "est plus petit que 5")
            else:
              print(nombre, "est égal à 5")

        def comparer(n, seuil):
          for nombre in range(n):
            if nombre > seuil:
              print(nombre, "est plus grand que", seuil)
            elif nombre < seuil:
              print(nombre, "est plus petit que", seuil)
            else:
              print(nombre, "est égal à", seuil)

        comparer_a_cinq([1, 2, 3, 4, 5, 6, 7, 8, 9])
        print("--")
        comparer(10, 3)
      """,
    ),

    "## Partie D : packages et mini-projets",

    Exercice(
      titre="Lancer de dés",
      niveau=2,
      enonce="""
        1. Importez le package `random`.
        2. Créez une fonction `lancer_de` qui prend un nombre de faces et qui renvoie un résultat aléatoire
           entre 1 et ce nombre (inclus). Indice : `random.randint()`.
        3. Créez une fonction `lancer_plusieurs` qui prend un nombre de lancers et un nombre de faces, et qui
           renvoie la liste des résultats.
      """,
      depart="""
        # Votre code ici

        def lancer_de(nb_faces):
          pass

        def lancer_plusieurs(nb_lancers, nb_faces):
          pass

        print(lancer_plusieurs(5, 6))
      """,
      solution="""
        import random

        def lancer_de(nb_faces):
          return random.randint(1, nb_faces)

        def lancer_plusieurs(nb_lancers, nb_faces):
          resultats = []
          for i in range(nb_lancers):
            resultats.append(lancer_de(nb_faces))
          return resultats

        print(lancer_plusieurs(5, 6))
      """,
      verif="""
        for i in range(1000):
          resultat = lancer_de(6)
          assert resultat is not None, "lancer_de ne renvoie rien."
          assert resultat >= 1 and resultat <= 6, f"lancer_de(6) a renvoyé {resultat}, qui n'est pas entre 1 et 6."
        assert len(lancer_plusieurs(10, 20)) == 10, "lancer_plusieurs(10, 20) devrait renvoyer 10 résultats."
        assert len(set(lancer_plusieurs(100, 6))) > 1, "Les résultats devraient être aléatoires !"
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Fizz Buzz",
      niveau=2,
      enonce="""
        Un grand classique des entretiens de programmation ! Créez une fonction `fizzbuzz` qui prend un nombre `n`
        et qui renvoie une liste des nombres de 1 à `n`, mais où :
        - les multiples de 3 sont remplacés par `"Fizz"` ;
        - les multiples de 5 sont remplacés par `"Buzz"` ;
        - les multiples de 3 **et** de 5 sont remplacés par `"FizzBuzz"`.

        Par exemple `fizzbuzz(6)` renvoie `[1, 2, "Fizz", 4, "Buzz", "Fizz"]`. Indice : l'opérateur `%`.
      """,
      depart="""
        def fizzbuzz(n):
          # Votre code ici
          pass

        print(fizzbuzz(15))
      """,
      solution="""
        def fizzbuzz(n):
          resultat = []
          for i in range(1, n + 1):
            # On teste d'abord le cas le plus restrictif (voir l'exercice du pavé introuvable !)
            if i % 3 == 0 and i % 5 == 0:
              resultat.append("FizzBuzz")
            elif i % 3 == 0:
              resultat.append("Fizz")
            elif i % 5 == 0:
              resultat.append("Buzz")
            else:
              resultat.append(i)
          return resultat

        print(fizzbuzz(15))
      """,
      verif="""
        assert fizzbuzz(6) == [1, 2, "Fizz", 4, "Buzz", "Fizz"], "fizzbuzz(6) ne renvoie pas la bonne liste."
        assert fizzbuzz(15)[-1] == "FizzBuzz", "15 est multiple de 3 et de 5 : il devrait être remplacé par \\"FizzBuzz\\"."
        assert len(fizzbuzz(100)) == 100, "fizzbuzz(100) devrait contenir 100 éléments (de 1 à 100)."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Le nombre mystère",
      niveau=3,
      enonce="""
        Programmez un jeu : l'ordinateur choisit un nombre au hasard entre 1 et 100, et l'utilisateur·rice doit
        le deviner. À chaque essai, l'ordinateur répond « C'est plus ! » ou « C'est moins ! ». Quand le nombre
        est trouvé, il affiche le nombre d'essais utilisés.

        Vous aurez besoin de : `random.randint()`, une boucle `while`, `input()`, `int()` et des conditions.
      """,
      depart="""
        import random

        def jeu_nombre_mystere():
          # Votre code ici
          pass

        jeu_nombre_mystere()
      """,
      solution="""
        import random

        def jeu_nombre_mystere():
          mystere = random.randint(1, 100)
          essais = 0
          proposition = 0  # une valeur de départ différente du nombre mystère pour entrer dans la boucle

          while proposition != mystere:
            proposition = int(input("Votre proposition : "))
            essais = essais + 1
            if proposition < mystere:
              print("C'est plus !")
            elif proposition > mystere:
              print("C'est moins !")

          print("Bravo ! Le nombre était", mystere, "- trouvé en", essais, "essais.")

        jeu_nombre_mystere()
      """,
    ),

    Exercice(
      titre="Le questionnaire",
      niveau=3,
      enonce="""
        Améliorons la conversation de la séance 1 !
        1. Créez une liste `questions` contenant au moins trois questions (dont une qui demande l'âge).
        2. Avec une boucle `for`, posez chaque question avec `input()` et rangez les réponses dans un
           dictionnaire `reponses` (la clé est la question, la valeur la réponse).
        3. Après la boucle, faites réagir l'ordinateur à l'âge avec des conditions : « Vous êtes jeune ! »
           en dessous de 25 ans, « Quelle expérience ! » au-dessus de 60 ans, etc.
        4. Enfin, imprimez un récapitulatif de toutes les réponses.
      """,
      depart="""
        questions = ...
        reponses = {}

        # Votre code ici
      """,
      solution="""
        questions = ["Comment vous appelez-vous ?", "Quel âge avez-vous ?", "Quelle est votre discipline ?"]
        reponses = {}

        for question in questions:
          reponses[question] = input(question + " ")

        age = int(reponses["Quel âge avez-vous ?"])
        if age < 25:
          print("Vous êtes jeune !")
        elif age > 60:
          print("Quelle expérience !")
        else:
          print("Le bel âge pour apprendre Python !")

        print("Récapitulatif :")
        for question in questions:
          print("-", question, reponses[question])
      """,
    ),
  ],
}
