from build import Code, Exercice

SESSION = {
  "numero": 1,
  "dossier": "session-1",
  "intro": """
    Ces exercices reprennent la séance 1 : `print()`, les variables, les types de données
    (string, integer, float, boolean), les listes, les dictionnaires et la création de fonctions.
  """,
  "items": [
    "## Partie A : données et variables",

    Exercice(
      titre="Mes premières variables",
      niveau=1,
      enonce="""
        Créez quatre variables qui vous décrivent :
        - `prenom` : votre prénom (un **string**) ;
        - `annee_de_naissance` : votre année de naissance (un **integer**) ;
        - `taille` : votre taille en mètres, par exemple `1.70` (un **float**) ;
        - `est_etudiant` : `True` si vous êtes étudiant·e, `False` sinon (un **boolean**).
      """,
      depart="""
        prenom = ...
        annee_de_naissance = ...
        taille = ...
        est_etudiant = ...

        print(prenom, annee_de_naissance, taille, est_etudiant)
      """,
      solution="""
        prenom = "Camille"
        annee_de_naissance = 2001
        taille = 1.68
        est_etudiant = True

        print(prenom, annee_de_naissance, taille, est_etudiant)
      """,
      verif="""
        assert type(prenom) == str, "prenom doit être un string (du texte entre guillemets)."
        assert type(annee_de_naissance) == int, "annee_de_naissance doit être un integer (un nombre entier, sans guillemets)."
        assert type(taille) == float, "taille doit être un float (un nombre avec un point, par exemple 1.70)."
        assert type(est_etudiant) == bool, "est_etudiant doit valoir True ou False (sans guillemets !)."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Devinez le type",
      niveau=1,
      enonce="""
        Pour chacune des variables `a` à `g`, **devinez son type sans exécuter de code**, puis écrivez
        votre réponse entre guillemets : `"str"`, `"int"`, `"float"`, `"bool"`, `"list"` ou `"dict"`.

        Une fois la vérification réussie, affichez les types avec `print(type(a))`, etc. pour confirmer.
      """,
      depart="""
        a = "42"
        b = 42
        c = 42.0
        d = False
        e = "False"
        f = [4, 2]
        g = {"reponse": 42}

        type_a = ...
        type_b = ...
        type_c = ...
        type_d = ...
        type_e = ...
        type_f = ...
        type_g = ...
      """,
      solution="""
        a = "42"
        b = 42
        c = 42.0
        d = False
        e = "False"
        f = [4, 2]
        g = {"reponse": 42}

        type_a = "str"    # entre guillemets : c'est du texte, même si ça ressemble à un nombre
        type_b = "int"
        type_c = "float"  # le point en fait un nombre décimal
        type_d = "bool"
        type_e = "str"    # entre guillemets : c'est du texte, pas un boolean
        type_f = "list"
        type_g = "dict"

        print(type(a), type(b), type(c), type(d), type(e), type(f), type(g))
      """,
      verif="""
        assert type_a == "str", "type_a : regardez bien les guillemets autour de 42..."
        assert type_b == "int", "type_b : un nombre entier."
        assert type_c == "float", "type_c : regardez le point !"
        assert type_d == "bool", "type_d : True et False sans guillemets sont des booleans."
        assert type_e == "str", "type_e : attention, il y a des guillemets autour de False !"
        assert type_f == "list", "type_f : les crochets [] indiquent..."
        assert type_g == "dict", "type_g : les accolades {} avec des paires clé : valeur indiquent..."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Une liste de villes",
      niveau=1,
      enonce="""
        À partir de la liste `villes` :
        1. mettez la **première** ville dans une variable `premiere` ;
        2. mettez la **troisième** ville dans une variable `troisieme` ;
        3. remplacez `"Quimper"` par `"Saint-Malo"` dans la liste, **sans réécrire toute la liste** ;
        4. mettez la **dernière** ville dans une variable `derniere`.

        > 💡 **Nouveau** : on peut aussi compter depuis la fin d'une liste avec des index négatifs :
        > `ma_liste[-1]` est le dernier élément, `ma_liste[-2]` l'avant-dernier, etc.

        N'oubliez pas : on compte à partir de 0 !
      """,
      depart="""
        villes = ["Rennes", "Brest", "Nantes", "Quimper", "Vannes"]

        # 1.
        premiere = ...

        # 2.
        troisieme = ...

        # 3.
        ...

        # 4.
        derniere = ...

        print(villes)
      """,
      solution="""
        villes = ["Rennes", "Brest", "Nantes", "Quimper", "Vannes"]

        # 1. Le premier élément est à l'index 0 :
        premiere = villes[0]

        # 2. Le troisième élément est donc à l'index 2 :
        troisieme = villes[2]

        # 3. "Quimper" est le quatrième élément, donc à l'index 3 :
        villes[3] = "Saint-Malo"

        # 4. Avec un index négatif :
        derniere = villes[-1]

        print(villes)
      """,
      verif="""
        assert premiere == "Rennes", "premiere : on compte à partir de 0 !"
        assert troisieme == "Nantes", "troisieme : on compte à partir de 0, donc la troisième ville est à l'index 2."
        assert villes[3] == "Saint-Malo", "Quimper n'a pas été remplacé par Saint-Malo."
        assert villes == ["Rennes", "Brest", "Nantes", "Saint-Malo", "Vannes"], "Les autres villes ne doivent pas changer."
        assert derniere == "Vannes", "derniere : essayez l'index -1."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Une notice bibliographique",
      niveau=1,
      enonce="""
        Le dictionnaire `notice` décrit un livre, mais il contient une erreur.
        1. Mettez le nom de l'auteur dans une variable `auteur` (en allant le chercher dans le dictionnaire !).
        2. *Les Misérables* a été publié en **1862** : corrigez la valeur de la clé `"annee"`.
        3. Ajoutez une nouvelle clé `"genre"` avec la valeur `"roman"`.
           Indice : pour ajouter une clé, on utilise exactement la même syntaxe que pour modifier une valeur.
      """,
      depart="""
        notice = {
          "titre": "Les Misérables",
          "auteur": "Victor Hugo",
          "annee": 1861
        }

        # 1.
        auteur = ...

        # 2.
        ...

        # 3.
        ...

        print(notice)
      """,
      solution="""
        notice = {
          "titre": "Les Misérables",
          "auteur": "Victor Hugo",
          "annee": 1861
        }

        # 1.
        auteur = notice["auteur"]

        # 2.
        notice["annee"] = 1862

        # 3. Si la clé n'existe pas encore, elle est créée :
        notice["genre"] = "roman"

        print(notice)
      """,
      verif="""
        assert auteur == "Victor Hugo", "auteur : utilisez notice[\\"auteur\\"]."
        assert notice["annee"] == 1862, "L'année doit être 1862 (un integer, sans guillemets)."
        assert "genre" in notice, "La clé \\"genre\\" n'existe pas dans le dictionnaire."
        assert notice["genre"] == "roman", "La valeur de \\"genre\\" doit être \\"roman\\"."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Des données dans des données",
      niveau=2,
      enonce="""
        Une liste peut contenir des dictionnaires, un dictionnaire peut contenir des listes... Et pour aller
        chercher un élément « à l'intérieur », on peut enchaîner les crochets : `ma_variable["cle"][0]`.

        À partir du dictionnaire `fonds` (un fonds d'archives) :
        1. mettez la **deuxième** cote dans une variable `deuxieme_cote` ;
        2. mettez la ville dans une variable `ville` ;
        3. mettez le nombre de pièces de la boîte `"1J3"` dans une variable `pieces_1J3`.
      """,
      depart="""
        fonds = {
          "nom": "Fonds Dupont",
          "cotes": ["1J1", "1J2", "1J3", "1J4"],
          "adresse": {"ville": "Rennes", "code_postal": "35000"},
          "pieces_par_boite": {"1J1": 12, "1J2": 7, "1J3": 31, "1J4": 4}
        }

        deuxieme_cote = ...
        ville = ...
        pieces_1J3 = ...
      """,
      solution="""
        fonds = {
          "nom": "Fonds Dupont",
          "cotes": ["1J1", "1J2", "1J3", "1J4"],
          "adresse": {"ville": "Rennes", "code_postal": "35000"},
          "pieces_par_boite": {"1J1": 12, "1J2": 7, "1J3": 31, "1J4": 4}
        }

        # fonds["cotes"] est une liste, on prend son élément d'index 1 :
        deuxieme_cote = fonds["cotes"][1]

        # fonds["adresse"] est un dictionnaire, on prend sa clé "ville" :
        ville = fonds["adresse"]["ville"]

        pieces_1J3 = fonds["pieces_par_boite"]["1J3"]
      """,
      verif="""
        assert deuxieme_cote == "1J2", "deuxieme_cote : fonds[\\"cotes\\"] est une liste... à quel index est le deuxième élément ?"
        assert ville == "Rennes", "ville : fonds[\\"adresse\\"] est lui-même un dictionnaire."
        assert pieces_1J3 == 31, "pieces_1J3 : cherchez dans fonds[\\"pieces_par_boite\\"]."
        print("Bravo ! 🎉")
      """,
    ),

    "## Partie B : les fonctions",

    """
    > 💡 **Rappel : `return`**
    >
    > Une fonction peut *imprimer* son résultat avec `print()`. Mais souvent, on veut qu'une
    > fonction nous **rende** son résultat pour pouvoir le mettre dans une variable et continuer à travailler
    > avec. Pour cela, on utilise le mot clé `return`. Quand Python rencontre `return`, il sort de la fonction
    > et renvoie la valeur indiquée.
    >
    > Rappel des opérations mathématiques : `+` (addition), `-` (soustraction), `*` (multiplication),
    > `/` (division). Comme en maths, on peut utiliser des parenthèses : `(2 + 3) * 4`.
    >
    > Exécutez la cellule suivante pour voir la différence :
    """,

    Code("""
      def ajouter_10_et_imprimer(valeur):
        print(valeur + 10)

      def ajouter_10_et_renvoyer(valeur):
        return valeur + 10

      a = ajouter_10_et_imprimer(5)  # imprime 15...
      b = ajouter_10_et_renvoyer(5)  # n'imprime rien...

      print("a vaut :", a)  # ... mais a vaut None (rien) !
      print("b vaut :", b)  # ... alors que b vaut bien 15.
    """),

    Exercice(
      titre="Se présenter",
      niveau=1,
      enonce="""
        Créez une fonction `presenter` qui prend deux arguments, `prenom` et `discipline`, et qui **imprime**
        une phrase du type : `Bonjour, je m'appelle Camille et j'étudie l'histoire.`

        Appelez ensuite votre fonction trois fois avec des arguments différents.
      """,
      depart="""
        def presenter(prenom, discipline):
          # Votre code ici
          pass

        presenter("Camille", "l'histoire")
      """,
      solution="""
        def presenter(prenom, discipline):
          print("Bonjour, je m'appelle", prenom, "et j'étudie", discipline)

        presenter("Camille", "l'histoire")
        presenter("Yanis", "la sociologie")
        presenter("Lou", "la musicologie")
      """,
    ),

    Exercice(
      titre="Calculer un âge",
      niveau=1,
      enonce="""
        Créez une fonction `age` qui prend deux arguments, `annee_de_naissance` et `annee_actuelle`,
        et qui **renvoie** (avec `return`) l'âge de la personne.

        Par exemple, `age(1802, 1885)` doit renvoyer `83`.
      """,
      depart="""
        def age(annee_de_naissance, annee_actuelle):
          # Votre code ici (n'oubliez pas le return !)
          pass

        print(age(1802, 1885))
      """,
      solution="""
        def age(annee_de_naissance, annee_actuelle):
          return annee_actuelle - annee_de_naissance

        print(age(1802, 1885))
      """,
      verif="""
        assert age(1802, 1885) is not None, "Votre fonction ne renvoie rien : avez-vous utilisé return ?"
        assert age(1802, 1885) == 83, "age(1802, 1885) devrait renvoyer 83."
        assert age(2000, 2026) == 26, "age(2000, 2026) devrait renvoyer 26."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Une moyenne",
      niveau=1,
      enonce="""
        Créez une fonction `moyenne` qui prend trois notes en arguments et qui **renvoie** leur moyenne.

        Attention aux priorités de calcul : `10 + 12 + 14 / 3` n'est pas la même chose que `(10 + 12 + 14) / 3` !
      """,
      depart="""
        def moyenne(note1, note2, note3):
          # Votre code ici
          pass

        print(moyenne(10, 12, 14))
      """,
      solution="""
        def moyenne(note1, note2, note3):
          return (note1 + note2 + note3) / 3

        print(moyenne(10, 12, 14))
      """,
      verif="""
        assert moyenne(10, 12, 14) is not None, "Votre fonction ne renvoie rien : avez-vous utilisé return ?"
        assert moyenne(10, 12, 14) == 12, "moyenne(10, 12, 14) devrait renvoyer 12. Avez-vous mis des parenthèses ?"
        assert round(moyenne(0, 0, 20), 2) == 6.67, "moyenne(0, 0, 20) devrait renvoyer 6.666..."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Chasse au bug : où est passé mon prix ?",
      niveau=2,
      enonce="""
        Exécutez la cellule ci-dessous : elle produit une erreur `NameError`.
        1. Lisez le message d'erreur et expliquez **en commentaire** pourquoi `prix_ttc` n'existe pas
           (indice : relisez la partie sur l'indentation et la portée des variables dans le cours).
        2. Corrigez la fonction pour que la variable `prix_final` contienne le prix TTC d'un article à 100 €.
      """,
      depart="""
        def calculer_prix_ttc(prix_ht):
          prix_ttc = prix_ht * 1.2

        calculer_prix_ttc(100)
        print(prix_ttc)

        prix_final = ...
      """,
      solution="""
        # prix_ttc est déclarée à l'intérieur de la fonction (niveau d'indentation 1) :
        # elle n'existe que dans la fonction, et disparaît quand la fonction se termine.
        # Pour récupérer le résultat à l'extérieur, la fonction doit le renvoyer avec return.

        def calculer_prix_ttc(prix_ht):
          prix_ttc = prix_ht * 1.2
          return prix_ttc

        prix_final = calculer_prix_ttc(100)
        print(prix_final)
      """,
      verif="""
        assert prix_final is not None, "prix_final vaut None : la fonction renvoie-t-elle quelque chose ?"
        assert round(prix_final, 2) == 120, "prix_final devrait valoir 120."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Discuter avec l'ordinateur",
      niveau=2,
      enonce="""
        Reprenons l'exercice de fin de séance ! Créez une fonction `conversation` qui, avec `input()` :
        1. demande le prénom de l'utilisateur·rice et lui dit bonjour ;
        2. demande son âge, puis lui dit quel âge il ou elle aura **l'année prochaine** ;
        3. demande ce qu'il ou elle étudie, et répond quelque chose de sympathique.

        > 💡 **Attention** : `input()` renvoie **toujours un string**, même si on tape un nombre !
        > `"20" + 1` provoque une erreur. Pour transformer un string en integer, on utilise la fonction `int()` :
        > `int("20") + 1` vaut bien `21`. (De même, `float()` transforme en float et `str()` en string.)
      """,
      depart="""
        def conversation():
          # Votre code ici
          pass

        conversation()
      """,
      solution="""
        def conversation():
          prenom = input("Bonjour ! Comment vous appelez-vous ? ")
          print("Enchanté,", prenom, "!")

          age_texte = input("Quel âge avez-vous ? ")
          age_l_an_prochain = int(age_texte) + 1
          print("L'année prochaine, vous aurez", age_l_an_prochain, "ans.")

          etudes = input("Qu'étudiez-vous ? ")
          print("Passionnant,", etudes, "! Moi, j'étudie le Python.")

        conversation()
      """,
    ),

    Exercice(
      titre="Fabrique de notices",
      niveau=3,
      enonce="""
        1. Créez une fonction `creer_notice` qui prend trois arguments (`titre`, `auteur`, `annee`) et qui
           **renvoie** un dictionnaire avec les clés `"titre"`, `"auteur"` et `"annee"`.
        2. Créez une fonction `afficher_notice` qui prend une notice (un dictionnaire) en argument et qui
           imprime par exemple : `Les Misérables , par Victor Hugo ( 1862 )`.
        3. Créez une liste `bibliotheque` contenant trois notices créées avec `creer_notice`, puis affichez
           la deuxième avec `afficher_notice`.
      """,
      depart="""
        def creer_notice(titre, auteur, annee):
          # Votre code ici
          pass

        def afficher_notice(notice):
          # Votre code ici
          pass

        bibliotheque = ...
      """,
      solution="""
        def creer_notice(titre, auteur, annee):
          notice = {
            "titre": titre,
            "auteur": auteur,
            "annee": annee
          }
          return notice

        def afficher_notice(notice):
          print(notice["titre"], ", par", notice["auteur"], "(", notice["annee"], ")")

        bibliotheque = [
          creer_notice("Les Misérables", "Victor Hugo", 1862),
          creer_notice("Madame Bovary", "Gustave Flaubert", 1857),
          creer_notice("Germinal", "Émile Zola", 1885)
        ]

        afficher_notice(bibliotheque[1])
      """,
      verif="""
        test = creer_notice("Germinal", "Émile Zola", 1885)
        assert type(test) == dict, "creer_notice doit renvoyer un dictionnaire (avez-vous utilisé return ?)."
        assert test == {"titre": "Germinal", "auteur": "Émile Zola", "annee": 1885}, "Le dictionnaire renvoyé n'a pas les bonnes clés ou valeurs."
        assert type(bibliotheque) == list, "bibliotheque doit être une liste."
        assert len(bibliotheque) == 3, "bibliotheque doit contenir trois notices."
        assert type(bibliotheque[0]) == dict, "Chaque élément de bibliotheque doit être une notice (un dictionnaire)."
        print("Bravo ! 🎉")
      """,
    ),
  ],
}
