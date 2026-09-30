from build import Code, Exercice

SESSION = {
  "numero": 6,
  "dossier": "session-6",
  "intro": """
    Ces exercices reprennent la séance 6 : le traitement automatique des langues (TAL / NLP) avec `nltk` :
    tokenisation, mots vides (stop words), étiquetage morpho-syntaxique (POS tagging), lemmatisation et
    reconnaissance d'entités nommées (NER).

    ⚠ Les modèles de `nltk` pour le POS tagging, la lemmatisation et la NER ne fonctionnent qu'en **anglais**.
    La tokenisation et les mots vides, eux, existent aussi en français.
  """,
  "items": [
    "## Préparation",

    """
    Exécutez cette cellule : elle importe `nltk`, télécharge les modèles nécessaires (cela peut prendre quelques
    secondes), et définit deux textes : un paragraphe en anglais sur l'imprimerie et le poème de Victor Hugo
    *Demain, dès l'aube* (1856).
    """,

    Code('''
      import nltk
      import string

      for modele in ["punkt_tab", "stopwords", "averaged_perceptron_tagger_eng", "wordnet", "omw-1.4",
                     "maxent_ne_chunker_tab", "words"]:
        nltk.download(modele, quiet=True)

      from nltk.tokenize import word_tokenize, sent_tokenize
      from nltk.corpus import stopwords

      # Des strings écrits les uns à la suite des autres entre parenthèses sont collés en un seul :
      texte_en = ("Johannes Gutenberg introduced movable type printing to Europe around 1450 in Mainz. "
                  "His press made books cheaper and faster to produce. "
                  "Within fifty years, printers in Venice, Paris and London had published millions of copies. "
                  "Historians often argue that the printing press transformed religion, science and politics.")

      texte_fr = """Demain, dès l'aube, à l'heure où blanchit la campagne,
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
      Un bouquet de houx vert et de bruyère en fleur."""

      print(texte_en)
    '''),

    "## Partie A : tokenisation et nettoyage",

    Exercice(
      titre="Phrases et mots",
      niveau=1,
      enonce="""
        1. Découpez `texte_en` en phrases avec `sent_tokenize()` ; mettez le résultat dans `phrases`.
        2. Découpez `texte_en` en mots avec `word_tokenize()` ; mettez le résultat dans `mots`.
        3. Imprimez `mots` : que remarquez-vous à propos de la ponctuation ? En quoi est-ce différent de
           `texte_en.split()` ?
      """,
      depart="""
        phrases = ...
        mots = ...
      """,
      solution="""
        phrases = sent_tokenize(texte_en)
        mots = word_tokenize(texte_en)

        print(len(phrases), "phrases")
        print(mots)
        print(texte_en.split())
        # word_tokenize sépare la ponctuation des mots : "Mainz." devient deux tokens, "Mainz" et ".".
        # Avec split(), la ponctuation reste collée aux mots.
      """,
      verif="""
        assert type(phrases) == list and len(phrases) == 4, "texte_en contient 4 phrases."
        assert "Gutenberg" in mots, "\\"Gutenberg\\" devrait faire partie des mots."
        assert "Mainz" in mots and "." in mots, "word_tokenize sépare la ponctuation des mots."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Nettoyer un texte français",
      niveau=1,
      enonce="""
        1. Tokenisez `texte_fr` avec `word_tokenize()` en précisant la langue : `language="french"`.
           Mettez le résultat dans `mots_fr`.
        2. Créez une liste `mots_fr_filtres` qui contient les mots de `mots_fr` :
           - en minuscules ;
           - sans les mots vides français (`stopwords.words("french")`) ;
           - uniquement s'ils sont composés de lettres (`.isalpha()`), ce qui élimine la ponctuation.
      """,
      depart="""
        mots_fr = ...
        mots_fr_filtres = ...
      """,
      solution="""
        mots_fr = word_tokenize(texte_fr, language="french")

        mots_vides = set(stopwords.words("french"))  # un set est comme une liste, mais bien plus rapide pour in

        mots_fr_filtres = []
        for mot in mots_fr:
          mot = mot.lower()
          if mot not in mots_vides and mot.isalpha():
            mots_fr_filtres.append(mot)

        print(mots_fr_filtres)
      """,
      verif="""
        assert type(mots_fr) == list and "Demain" in mots_fr, "mots_fr devrait contenir les tokens du poème."
        assert "demain" in mots_fr_filtres, "\\"demain\\" devrait être dans mots_fr_filtres (en minuscules)."
        assert "je" not in mots_fr_filtres and "la" not in mots_fr_filtres, "Les mots vides (je, la...) devraient être retirés."
        for mot in mots_fr_filtres:
          assert mot.isalpha(), f"{mot!r} n'est pas composé que de lettres."
          assert mot == mot.lower(), f"{mot!r} n'est pas en minuscules."
        print("Bravo ! 🎉")
      """,
    ),

    """
    > 💡 **Rappel : `nltk.FreqDist`**
    >
    > Compter les mots, on sait faire avec un dictionnaire (séance 3). Mais `nltk` a un outil tout prêt :
    > `nltk.FreqDist(liste_de_mots)` crée un compteur, et sa méthode `.most_common(n)` renvoie la liste des `n` mots
    > les plus fréquents, sous forme de **tuples** `(mot, nombre)`. Un tuple est comme une liste qu'on ne peut pas
    > modifier : on accède à ses éléments de la même manière, `mon_tuple[0]`.
    """,

    Exercice(
      titre="Les mots les plus fréquents",
      niveau=2,
      enonce="""
        Avec `nltk.FreqDist`, mettez dans `top5` les 5 mots les plus fréquents de `mots_fr_filtres`.
        Puis imprimez-les proprement, un par ligne, sous la forme `montagne : 1`.
      """,
      depart="""
        top5 = ...
      """,
      solution="""
        top5 = nltk.FreqDist(mots_fr_filtres).most_common(5)

        for mot, nombre in top5:
          print(mot, ":", nombre)
      """,
      verif="""
        assert type(top5) == list and len(top5) == 5, "top5 devrait être une liste de 5 éléments."
        assert type(top5[0]) == tuple and len(top5[0]) == 2, "Chaque élément de top5 devrait être un tuple (mot, nombre)."
        assert top5[0][1] >= top5[4][1], "top5 devrait être trié du plus fréquent au moins fréquent."
        print("Bravo ! 🎉")
      """,
    ),

    "## Partie B : analyse grammaticale (en anglais)",

    Exercice(
      titre="Trouver les noms",
      niveau=2,
      enonce="""
        1. Étiquetez les mots de `texte_en` avec `nltk.pos_tag()` ; mettez le résultat dans `etiquettes`.
           C'est une liste de tuples `(mot, étiquette)`.
        2. Créez une liste `noms` contenant tous les mots dont l'étiquette commence par `"NN"` (les noms : `NN`,
           `NNS`, `NNP`...). Indice : `"NNS".startswith("NN")` vaut `True`.

        La liste des étiquettes est [ici](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html).
      """,
      depart="""
        etiquettes = ...
        noms = ...
      """,
      solution="""
        etiquettes = nltk.pos_tag(word_tokenize(texte_en))
        print(etiquettes)

        noms = []
        for mot, etiquette in etiquettes:
          if etiquette.startswith("NN"):
            noms.append(mot)

        print(noms)
      """,
      verif="""
        assert type(etiquettes) == list and type(etiquettes[0]) == tuple, "etiquettes devrait être une liste de tuples (mot, étiquette)."
        assert "books" in noms and "press" in noms, "\\"books\\" et \\"press\\" sont des noms."
        assert "made" not in noms and "cheaper" not in noms, "\\"made\\" (verbe) et \\"cheaper\\" (adjectif) ne sont pas des noms."
        print("Bravo ! 🎉")
      """,
    ),

    """
    Voici la fonction du cours qui traduit une étiquette du POS tagger en catégorie comprise par le lemmatiseur
    WordNet. Exécutez-la pour pouvoir l'utiliser dans l'exercice suivant.
    """,

    Code("""
      from nltk.stem import WordNetLemmatizer
      from nltk.corpus import wordnet

      def get_wordnet_pos(treebank_tag):
        if treebank_tag.startswith('J'):
          return wordnet.ADJ
        elif treebank_tag.startswith('V'):
          return wordnet.VERB
        elif treebank_tag.startswith('N'):
          return wordnet.NOUN
        elif treebank_tag.startswith('R'):
          return wordnet.ADV
        else:
          return wordnet.NOUN
    """),

    Exercice(
      titre="Lemmatiser",
      niveau=2,
      enonce="""
        Créez une liste `lemmes` contenant le lemme (en minuscules) de chaque mot de `texte_en` composé de lettres.
        Pour que le lemmatiseur fonctionne bien, donnez-lui la catégorie grammaticale de chaque mot, grâce à
        `etiquettes` et `get_wordnet_pos()` : `lemmatiseur.lemmatize(mot, pos=...)`.

        Par exemple, `"made"` doit devenir `"make"`, et `"books"` doit devenir `"book"`.

        Réfléchissez : vaut-il mieux mettre les mots en minuscules **avant** ou **après** le POS tagging ?
      """,
      depart="""
        lemmatiseur = WordNetLemmatizer()
        lemmes = ...
      """,
      solution="""
        lemmatiseur = WordNetLemmatizer()
        lemmes = []

        # On étiquette le texte original : les majuscules aident le POS tagger (noms propres, début de phrase).
        # On ne met en minuscules qu'au moment de lemmatiser.
        for mot, etiquette in etiquettes:
          if mot.isalpha():
            lemme = lemmatiseur.lemmatize(mot.lower(), pos=get_wordnet_pos(etiquette))
            lemmes.append(lemme)

        print(lemmes)
      """,
      verif="""
        assert type(lemmes) == list, "lemmes devrait être une liste."
        assert "make" in lemmes and "made" not in lemmes, "\\"made\\" devrait être lemmatisé en \\"make\\" (avez-vous donné pos= ?)."
        assert "book" in lemmes and "books" not in lemmes, "\\"books\\" devrait être lemmatisé en \\"book\\"."
        assert "publish" in lemmes, "\\"published\\" devrait être lemmatisé en \\"publish\\"."
        assert "." not in lemmes, "Seuls les mots composés de lettres doivent être gardés."
        print("Bravo ! 🎉")
      """,
    ),

    """
    > 💡 **Rappel : lire le résultat de `ne_chunk`**
    >
    > `nltk.ne_chunk()` renvoie un arbre (`nltk.Tree`). Quand on le parcourt avec une boucle `for`, chaque élément est :
    > - soit un tuple `(mot, étiquette)` pour un mot ordinaire ;
    > - soit un sous-arbre `nltk.Tree` pour une entité nommée. Sa méthode `.label()` donne le type d'entité
    >   (`PERSON`, `GPE`, `ORGANIZATION`...) et `.leaves()` la liste des tuples `(mot, étiquette)` qui la composent.
    >
    > Pour savoir si un élément est une entité : `if type(element) == nltk.Tree:`.
    """,

    Exercice(
      titre="Les entités nommées",
      niveau=2,
      enonce="""
        Appliquez `nltk.ne_chunk()` sur `etiquettes`, et créez une liste `entites` de tuples `(texte, type)`,
        par exemple `("Johannes Gutenberg", "PERSON")`.

        Indice : pour recomposer le texte d'une entité de plusieurs mots, parcourez ses `.leaves()` et assemblez
        les mots ; ou utilisez `" ".join(liste_de_mots)`, qui colle les éléments d'une liste de strings avec des espaces.
      """,
      depart="""
        entites = ...
      """,
      solution="""
        arbre = nltk.ne_chunk(etiquettes)

        entites = []
        for element in arbre:
          if type(element) == nltk.Tree:
            mots_entite = []
            for mot, etiquette in element.leaves():
              mots_entite.append(mot)
            entites.append((" ".join(mots_entite), element.label()))

        print(entites)
      """,
      verif="""
        assert type(entites) == list and len(entites) >= 3, "Il devrait y avoir au moins 3 entités nommées dans texte_en."
        assert type(entites[0]) == tuple and len(entites[0]) == 2, "Chaque entité devrait être un tuple (texte, type)."
        textes = []
        for texte, type_entite in entites:
          textes.append(texte)
        assert "Mainz" in textes, "Mainz devrait être reconnue comme une entité."
        print("Bravo ! 🎉")
      """,
    ),

    "## Partie C : mini-projets",

    Exercice(
      titre="Le profil d'un texte",
      niveau=3,
      enonce="""
        Assemblez tout ce que vous avez fait dans une fonction `profil_texte(texte)` (pour un texte en anglais) qui
        renvoie un dictionnaire avec les clés :
        - `"nb_phrases"` : le nombre de phrases ;
        - `"nb_mots"` : le nombre de tokens composés de lettres ;
        - `"lemmes_frequents"` : les 5 lemmes les plus fréquents (sans les mots vides anglais), sous forme de liste
          de tuples `(lemme, nombre)` ;
        - `"entites"` : la liste des entités nommées `(texte, type)`.

        Bonus : transformez-la en une classe `AnalyseurNLTK`, avec une méthode par étape, comme la classe
        `NLPMachine` vue en cours.
      """,
      depart="""
        def profil_texte(texte):
          # Votre code ici
          pass

        print(profil_texte(texte_en))
      """,
      solution="""
        def profil_texte(texte):
          mots_vides = set(stopwords.words("english"))
          lemmatiseur = WordNetLemmatizer()

          etiquettes = nltk.pos_tag(word_tokenize(texte))

          nb_mots = 0
          lemmes = []
          for mot, etiquette in etiquettes:
            if mot.isalpha():
              nb_mots = nb_mots + 1
              lemme = lemmatiseur.lemmatize(mot.lower(), pos=get_wordnet_pos(etiquette))
              if lemme not in mots_vides:
                lemmes.append(lemme)

          entites = []
          for element in nltk.ne_chunk(etiquettes):
            if type(element) == nltk.Tree:
              mots_entite = []
              for mot, etiquette in element.leaves():
                mots_entite.append(mot)
              entites.append((" ".join(mots_entite), element.label()))

          return {
            "nb_phrases": len(sent_tokenize(texte)),
            "nb_mots": nb_mots,
            "lemmes_frequents": nltk.FreqDist(lemmes).most_common(5),
            "entites": entites
          }

        print(profil_texte(texte_en))
      """,
      verif="""
        profil = profil_texte(texte_en)
        assert type(profil) == dict, "profil_texte doit renvoyer un dictionnaire."
        for cle in ["nb_phrases", "nb_mots", "lemmes_frequents", "entites"]:
          assert cle in profil, f"Il manque la clé {cle!r}."
        assert profil["nb_phrases"] == 4, "texte_en contient 4 phrases."
        assert profil["nb_mots"] == 46, f"texte_en contient 46 tokens composés de lettres, et non {profil['nb_mots']}."
        assert len(profil["lemmes_frequents"]) == 5, "lemmes_frequents doit contenir 5 éléments."
        for lemme, nombre in profil["lemmes_frequents"]:
          assert lemme not in stopwords.words("english"), f"{lemme!r} est un mot vide : il ne devrait pas être dans les lemmes fréquents."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Analyser un article de Wikipédia",
      niveau=3,
      enonce="""
        Combinez avec la séance 4 (connexion internet nécessaire) :
        1. récupérez l'article de Wikipédia en anglais sur l'imprimerie
           (`https://en.wikipedia.org/wiki/Printing_press`), sans oublier l'en-tête `User-Agent` ;
        2. avec BeautifulSoup, récupérez le texte de tous les paragraphes `<p>` de l'article et assemblez-les en un
           seul string `texte_article` ;
        3. appliquez `profil_texte()` dessus. Quelles sont les personnes et les lieux les plus cités ?

        Il n'y a pas de vérification pour cet exercice : à vous d'explorer !
      """,
      depart="""
        import requests
        from bs4 import BeautifulSoup

        ENTETES = {"User-Agent": "HackspaceSHS-exercices/1.0 (cours d'initiation a Python, Universite Rennes 2)"}

        # Votre code ici
      """,
      solution="""
        import requests
        from bs4 import BeautifulSoup

        ENTETES = {"User-Agent": "HackspaceSHS-exercices/1.0 (cours d'initiation a Python, Universite Rennes 2)"}

        reponse = requests.get("https://en.wikipedia.org/wiki/Printing_press", headers=ENTETES)
        soupe = BeautifulSoup(reponse.content, "html.parser")

        paragraphes = []
        for p in soupe.find_all("p"):
          paragraphes.append(p.get_text())
        texte_article = " ".join(paragraphes)

        profil = profil_texte(texte_article)
        print(profil["nb_phrases"], "phrases,", profil["nb_mots"], "mots")
        print(profil["lemmes_frequents"])

        # Quelles entités reviennent le plus souvent ? On peut compter les tuples avec FreqDist !
        print(nltk.FreqDist(profil["entites"]).most_common(10))
      """,
    ),
  ],
}
