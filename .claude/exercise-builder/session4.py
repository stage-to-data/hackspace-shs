from build import Code, Exercice

SESSION = {
  "numero": 4,
  "dossier": "session-4",
  "intro": """
    Ces exercices reprennent la séance 4 : parcourir du HTML avec BeautifulSoup, faire des requêtes avec
    `requests`, et interroger une API (Nakala).

    La partie A fonctionne sans internet, sur une page HTML fournie. Les parties B et C vont chercher de
    vraies pages sur le web : il faut être connecté·e (et les pages peuvent changer avec le temps !).
  """,
  "items": [
    "## Préparation",

    Code("""
      # Dans Colab, ces packages sont déjà installés.
      # Sur votre ordinateur, il faudra peut-être d'abord lancer : !pip install requests beautifulsoup4
      import os
      import json
      import csv
      import time

      import requests
      from bs4 import BeautifulSoup
    """),

    "## Partie A : BeautifulSoup (sans internet)",

    '''
    Voici le code HTML (simplifié) de la page d'un catalogue d'archives imaginaire. Exécutez la cellule pour le
    mettre dans la variable `page_html`. Prenez le temps de le lire : repérez les balises (`<h1>`, `<li>`, `<a>`...),
    leurs attributs (`id`, `class`, `href`, `src`, `data-annee`...) et leur contenu.
    ''',

    Code('''
      page_html = """
      <html>
        <head><title>Archives de Villebois - Fonds Durand</title></head>
        <body>
          <ul id="menu">
            <li><a href="/accueil">Accueil</a></li>
            <li><a href="/recherche">Recherche</a></li>
          </ul>

          <h1 id="titre-principal">Fonds photographique Durand</h1>
          <p class="description">Photographies de la vie rurale en Bretagne, 1900-1950.</p>

          <ul id="notices">
            <li class="notice" data-annee="1904">
              <a href="/notices/fd-001">Marché aux bestiaux</a>
              <span class="lieu">Rennes</span>
              <img src="/images/fd-001.jpg" alt="Marché aux bestiaux">
            </li>
            <li class="notice" data-annee="1912">
              <a href="/notices/fd-002">Pardon de Sainte-Anne</a>
              <span class="lieu">Auray</span>
              <img src="/images/fd-002.jpg" alt="Pardon de Sainte-Anne">
            </li>
            <li class="notice" data-annee="1927">
              <a href="/notices/fd-003">Battage du blé</a>
              <span class="lieu">Fougères</span>
              <img src="/images/fd-003.jpg" alt="Battage du blé">
            </li>
            <li class="notice" data-annee="1931">
              <a href="/notices/fd-004">Lavandières au bord de la Vilaine</a>
              <span class="lieu">Rennes</span>
              <img src="/images/fd-004.jpg" alt="Lavandières au bord de la Vilaine">
            </li>
            <li class="notice" data-annee="1948">
              <a href="/notices/fd-005">Retour de pêche</a>
              <span class="lieu">Douarnenez</span>
              <img src="/images/fd-005.jpg" alt="Retour de pêche">
            </li>
          </ul>
        </body>
      </html>
      """

      URL_DU_SITE = "https://archives-villebois.example"
    '''),

    Exercice(
      titre="Le titre de la page",
      niveau=1,
      enonce="""
        1. Créez une instance de `BeautifulSoup` à partir de `page_html` et mettez-la dans une variable `soupe`.
           (Ici on a directement un string, pas besoin de `response.content`.)
        2. Trouvez l'élément `<h1>` et mettez son **texte** dans une variable `titre_page`.
      """,
      depart="""
        soupe = ...
        titre_page = ...
      """,
      solution="""
        soupe = BeautifulSoup(page_html, "html.parser")

        titre_page = soupe.find("h1").get_text()
        # Ou bien, en passant par l'id : soupe.find(id="titre-principal").get_text()

        print(titre_page)
      """,
      verif="""
        assert titre_page == "Fonds photographique Durand", f"titre_page vaut {titre_page!r}. Avez-vous bien pris le texte de l'élément (.get_text() ou .string) ?"
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="La liste des photographies",
      niveau=1,
      enonce="""
        1. Combien y a-t-il d'éléments `<li>` dans la page ? Mettez ce nombre dans `nb_li`.
        2. Ce n'est pas le nombre de photographies : le menu contient aussi des `<li>` ! Avec l'argument `class_`,
           trouvez uniquement les `<li>` qui ont la classe `notice`, et créez une liste `titres` contenant le texte
           du lien `<a>` de chacune.
      """,
      depart="""
        nb_li = ...
        titres = ...
      """,
      solution="""
        nb_li = len(soupe.find_all("li"))
        print(nb_li)

        titres = []
        for notice in soupe.find_all("li", class_="notice"):
          # On peut chercher à l'intérieur d'un élément, comme dans toute la page :
          titres.append(notice.find("a").get_text())

        print(titres)
      """,
      verif="""
        assert nb_li == 7, "Il y a 7 éléments <li> dans la page (2 dans le menu, 5 notices)."
        assert titres == ["Marché aux bestiaux", "Pardon de Sainte-Anne", "Battage du blé",
                          "Lavandières au bord de la Vilaine", "Retour de pêche"], f"titres ne contient pas les bons titres : {titres}"
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Des notices structurées",
      niveau=2,
      enonce="""
        Créez une liste `notices` contenant un dictionnaire par photographie, avec les clés :
        - `"titre"` : le texte du lien ;
        - `"lien"` : la valeur de l'attribut `href` du lien ;
        - `"annee"` : la valeur de l'attribut `data-annee` de la notice, **convertie en integer** ;
        - `"lieu"` : le texte de l'élément qui a la classe `lieu`.

        Le premier élément doit donc être :
        `{"titre": "Marché aux bestiaux", "lien": "/notices/fd-001", "annee": 1904, "lieu": "Rennes"}`.
      """,
      depart="""
        notices = ...
      """,
      solution="""
        notices = []
        for element in soupe.find_all("li", class_="notice"):
          lien = element.find("a")
          notices.append({
            "titre": lien.get_text(),
            "lien": lien.get("href"),
            "annee": int(element.get("data-annee")),
            "lieu": element.find(class_="lieu").get_text()
          })

        print(notices)
      """,
      verif="""
        assert type(notices) == list and len(notices) == 5, "notices devrait être une liste de 5 dictionnaires."
        assert notices[0] == {"titre": "Marché aux bestiaux", "lien": "/notices/fd-001", "annee": 1904, "lieu": "Rennes"}, f"La première notice n'est pas correcte : {notices[0]}"
        assert notices[4]["annee"] == 1948, "L'année doit être un integer : utilisez int()."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Des liens complets",
      niveau=2,
      enonce="""
        Les attributs `src` des images sont des chemins **relatifs** (`/images/fd-001.jpg`) : pour les télécharger,
        il faudrait l'adresse complète. Créez une liste `urls_images` contenant l'URL complète de chaque image,
        en ajoutant `URL_DU_SITE` devant (comme on ajoutait `"https:"` devant les images de Wikipédia dans le cours).

        Puis, créez une liste `photos_rennes` contenant uniquement les titres des photographies prises à Rennes
        (utilisez la liste `notices` de l'exercice précédent).
      """,
      depart="""
        urls_images = ...
        photos_rennes = ...
      """,
      solution="""
        urls_images = []
        for image in soupe.find_all("img"):
          urls_images.append(URL_DU_SITE + image.get("src"))
        print(urls_images)

        photos_rennes = []
        for notice in notices:
          if notice["lieu"] == "Rennes":
            photos_rennes.append(notice["titre"])
        print(photos_rennes)
      """,
      verif="""
        assert len(urls_images) == 5, "Il y a 5 images dans la page."
        assert urls_images[0] == "https://archives-villebois.example/images/fd-001.jpg", f"La première URL n'est pas correcte : {urls_images[0]}"
        assert photos_rennes == ["Marché aux bestiaux", "Lavandières au bord de la Vilaine"], f"photos_rennes n'est pas correct : {photos_rennes}"
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Sauvegarder le résultat",
      niveau=2,
      enonce="""
        Enregistrez la liste `notices` dans un fichier `notices.json` (dans le dossier courant), en utilisant cette
        fois le mot clé `with` vu en cours (plus besoin de `close()` !). Mettez le chemin dans `chemin_notices`.
      """,
      depart="""
        chemin_notices = ...
      """,
      solution="""
        chemin_notices = os.path.join(os.getcwd(), "notices.json")

        with open(chemin_notices, "w", encoding="utf-8") as f:
          json.dump(notices, f, indent=4, ensure_ascii=False)
        # Ici, en sortant du bloc with, le fichier est fermé automatiquement.
      """,
      verif="""
        assert os.path.isfile(chemin_notices), "Le fichier notices.json n'existe pas."
        with open(chemin_notices, encoding="utf-8") as f:
          assert json.load(f) == notices, "Le fichier ne contient pas la liste notices."
        print("Bravo ! 🎉")
      """,
    ),

    "## Partie B : scraper Wikipédia (connexion internet nécessaire)",

    """
    > 💡 **Rappel : se présenter poliment**
    >
    > Quand on visite un site avec `requests`, on envoie une « carte de visite » : l'en-tête `User-Agent`.
    > Par défaut, c'est quelque chose comme `python-requests/2.32` et de nombreux sites (dont Wikipédia !)
    > refusent ces requêtes anonymes avec un code `403`. On précise donc un `User-Agent` qui dit qui on est,
    > avec l'argument `headers` :
    > ```python
    > requests.get(url, headers=ENTETES)
    > ```
    > Autre règle de politesse : ne pas envoyer des centaines de requêtes par seconde. Quand on fait des requêtes
    > dans une boucle, on attend un peu entre chaque, avec `time.sleep(1)` (1 seconde).
    """,

    Code("""
      ENTETES = {"User-Agent": "HackspaceSHS-exercices/1.0 (cours d'initiation a Python, Universite Rennes 2)"}
    """),

    Exercice(
      titre="Visiter une page",
      niveau=1,
      enonce="""
        1. Faites une requête vers l'article Wikipédia sur Rennes (`https://fr.wikipedia.org/wiki/Rennes`),
           avec les `ENTETES` ; mettez la réponse dans `reponse`.
        2. Si la requête a réussi (code 200), créez une instance de `BeautifulSoup` (`soupe_rennes`), et mettez
           le texte de l'élément qui a l'id `firstHeading` dans une variable `titre_article`.
      """,
      depart="""
        reponse = ...
        titre_article = ...
      """,
      solution="""
        reponse = requests.get("https://fr.wikipedia.org/wiki/Rennes", headers=ENTETES)
        print(reponse.status_code)

        if reponse.status_code == 200:
          soupe_rennes = BeautifulSoup(reponse.content, "html.parser")
          titre_article = soupe_rennes.find(id="firstHeading").get_text()
          print(titre_article)
      """,
      verif="""
        assert reponse.status_code == 200, f"La requête a échoué avec le code {reponse.status_code}. Avez-vous ajouté headers=ENTETES ?"
        assert titre_article == "Rennes", f"titre_article vaut {titre_article!r}."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Le sommaire",
      niveau=2,
      enonce="""
        Les grandes parties d'un article Wikipédia sont des titres `<h2>`. À partir de `soupe_rennes`, créez une liste
        `sections` contenant le texte de chaque `<h2>` de l'article.

        Indice : la méthode `.strip()` (sans argument) enlève les espaces et sauts de ligne au début et à la fin
        d'un string.
      """,
      depart="""
        sections = ...
      """,
      solution="""
        sections = []
        for titre in soupe_rennes.find_all("h2"):
          sections.append(titre.get_text().strip())

        print(sections)
      """,
      verif="""
        assert type(sections) == list and len(sections) > 5, "sections devrait contenir plusieurs titres."
        assert "Histoire" in sections, "L'article sur Rennes devrait avoir une section \\"Histoire\\"."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Cinq articles au hasard",
      niveau=2,
      enonce="""
        1. Créez une fonction `titre_aleatoire` qui visite `https://fr.wikipedia.org/wiki/Special:Random` et qui
           renvoie le titre de l'article obtenu (ou `None` si la requête a échoué).
        2. Appelez-la 5 fois dans une boucle (en attendant une seconde entre chaque requête !) et rangez les titres
           dans une liste `titres_aleatoires`.
        3. Enregistrez cette liste dans un fichier `articles_aleatoires.json`.
      """,
      depart="""
        def titre_aleatoire():
          # Votre code ici
          pass

        titres_aleatoires = ...
      """,
      solution="""
        def titre_aleatoire():
          reponse = requests.get("https://fr.wikipedia.org/wiki/Special:Random", headers=ENTETES)
          if reponse.status_code == 200:
            soupe = BeautifulSoup(reponse.content, "html.parser")
            return soupe.find(id="firstHeading").get_text()
          return None

        titres_aleatoires = []
        for i in range(5):
          titres_aleatoires.append(titre_aleatoire())
          time.sleep(1)

        print(titres_aleatoires)

        with open(os.path.join(os.getcwd(), "articles_aleatoires.json"), "w", encoding="utf-8") as f:
          json.dump(titres_aleatoires, f, indent=4, ensure_ascii=False)
      """,
      verif="""
        assert type(titres_aleatoires) == list and len(titres_aleatoires) == 5, "titres_aleatoires devrait contenir 5 titres."
        for titre in titres_aleatoires:
          assert type(titre) == str, f"{titre!r} n'est pas un titre : une requête a-t-elle échoué ?"
        assert os.path.isfile(os.path.join(os.getcwd(), "articles_aleatoires.json")), "Le fichier articles_aleatoires.json n'existe pas."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Télécharger une image",
      niveau=3,
      enonce="""
        1. Créez une fonction `telecharger(url, chemin)` qui télécharge le fichier situé à `url` et l'enregistre à
           l'emplacement `chemin`. Utilisez `requests.get()` (avec les `ENTETES` : Wikimedia les exige aussi pour
           les images !), puis écrivez `reponse.content` dans un fichier ouvert en mode `"wb"` (*write binary* :
           une image n'est pas du texte).
        2. Dans `soupe_rennes`, trouvez l'encadré de droite de l'article (l'élément qui a la classe `infobox`),
           puis la première image `<img>` qu'il contient, et téléchargez-la dans un fichier `rennes.jpg`.
           Attention, comme dans le cours, le `src` commence par `//` : il faut ajouter `"https:"` devant.
           Mettez le chemin de l'image dans `chemin_image`.
      """,
      depart="""
        def telecharger(url, chemin):
          # Votre code ici
          pass

        chemin_image = ...
      """,
      solution="""
        def telecharger(url, chemin):
          reponse = requests.get(url, headers=ENTETES)
          if reponse.status_code == 200:
            with open(chemin, "wb") as f:
              f.write(reponse.content)
          else:
            print("Échec du téléchargement :", reponse.status_code)

        chemin_image = os.path.join(os.getcwd(), "rennes.jpg")

        infobox = soupe_rennes.find(class_="infobox")
        url_image = "https:" + infobox.find("img").get("src")

        print(url_image)
        telecharger(url_image, chemin_image)
      """,
      verif="""
        assert os.path.isfile(chemin_image), "L'image n'a pas été téléchargée."
        assert os.path.getsize(chemin_image) > 1000, "Le fichier téléchargé est bien petit pour une image : ouvrez-le pour voir ce qu'il contient."
        print("Bravo ! 🎉 Ouvrez l'image dans le panneau Fichiers pour la voir.")
      """,
    ),

    "## Partie C : l'API de Nakala (connexion internet nécessaire)",

    """
    Rappel : une API renvoie directement des données structurées (du JSON), qu'on récupère avec `reponse.json()`.
    La documentation de l'API de Nakala est [ici](https://api.nakala.fr/doc).

    Dans une réponse de Nakala, les métadonnées d'une donnée se trouvent dans la liste `"metas"` : chaque
    métadonnée est un dictionnaire, dont la clé `"propertyUri"` indique de quelle propriété il s'agit
    (par exemple `"http://nakala.fr/terms#title"` pour le titre) et la clé `"value"` donne sa valeur.
    """,

    Code("""
      API_NAKALA = "https://api.nakala.fr"
    """),

    Exercice(
      titre="Lire une notice Nakala",
      niveau=2,
      enonce="""
        1. Récupérez la donnée d'identifiant `10.34847/nkl.def2v5a2` (celle du cours) et mettez le JSON de la
           réponse dans une variable `donnee`.
        2. Créez une fonction `valeurs_meta(donnee, propriete)` qui renvoie la **liste** des valeurs (`"value"`)
           de toutes les métadonnées dont le `"propertyUri"` est égal à `propriete`.
        3. Utilisez-la pour mettre le titre de la donnée dans la variable `titre_nakala`
           (propriété `"http://nakala.fr/terms#title"`) et la licence dans `licence_nakala`
           (propriété `"http://nakala.fr/terms#license"`).
      """,
      depart="""
        donnee = ...

        def valeurs_meta(donnee, propriete):
          # Votre code ici
          pass

        titre_nakala = ...
        licence_nakala = ...
      """,
      solution="""
        reponse = requests.get(f"{API_NAKALA}/datas/10.34847/nkl.def2v5a2")
        donnee = reponse.json()

        def valeurs_meta(donnee, propriete):
          valeurs = []
          for meta in donnee["metas"]:
            if meta["propertyUri"] == propriete:
              valeurs.append(meta["value"])
          return valeurs

        titre_nakala = valeurs_meta(donnee, "http://nakala.fr/terms#title")[0]
        licence_nakala = valeurs_meta(donnee, "http://nakala.fr/terms#license")[0]

        print(titre_nakala, "-", licence_nakala)
        print(valeurs_meta(donnee, "http://purl.org/dc/terms/subject"))
      """,
      verif="""
        assert titre_nakala == "Carte n°35, terrain 45", f"titre_nakala vaut {titre_nakala!r}."
        assert licence_nakala == "CC-BY-NC-SA-4.0", f"licence_nakala vaut {licence_nakala!r}."
        assert valeurs_meta(donnee, "http://purl.org/dc/terms/medium") == ["Monochrome", "Papier"], "valeurs_meta doit renvoyer toutes les valeurs de la propriété, dans une liste."
        print("Bravo ! 🎉")
      """,
    ),

    Exercice(
      titre="Une recherche exportée en CSV",
      niveau=3,
      enonce="""
        1. Faites une recherche sur Nakala avec le mot `himalaya` (`/search?q=himalaya`).
        2. Pour les **5 premiers** résultats de `["datas"]`, récupérez leur identifiant (`"identifier"`) et leur titre
           (avec votre fonction `valeurs_meta`).
        3. Enregistrez le tout dans un fichier `recherche_nakala.csv` avec une ligne d'en-tête `identifiant,titre`.
           Mettez son chemin dans `chemin_recherche`.

        > 💡 Plutôt que d'écrire les paramètres dans l'URL à la main, `requests` peut les ajouter pour vous (et
        > s'occuper des espaces et des accents) : `requests.get(f"{API_NAKALA}/search", params={"q": "himalaya"})`.
      """,
      depart="""
        chemin_recherche = ...
      """,
      solution="""
        reponse = requests.get(f"{API_NAKALA}/search", params={"q": "himalaya"})
        resultats = reponse.json()

        chemin_recherche = os.path.join(os.getcwd(), "recherche_nakala.csv")
        with open(chemin_recherche, "w", encoding="utf-8", newline="") as f:
          writer = csv.writer(f)
          writer.writerow(["identifiant", "titre"])
          for index, resultat in enumerate(resultats["datas"]):
            if index < 5:
              titres = valeurs_meta(resultat, "http://nakala.fr/terms#title")
              writer.writerow([resultat["identifier"], titres[0]])

        with open(chemin_recherche, encoding="utf-8") as f:
          print(f.read())
      """,
      verif="""
        assert os.path.isfile(chemin_recherche), "Le fichier recherche_nakala.csv n'existe pas."
        with open(chemin_recherche, encoding="utf-8") as f:
          lignes = list(csv.reader(f))
        assert lignes[0] == ["identifiant", "titre"], "La première ligne doit être l'en-tête identifiant,titre."
        assert len(lignes) == 6, f"Le fichier devrait contenir 6 lignes (l'en-tête + 5 résultats), et non {len(lignes)}."
        print("Bravo ! 🎉")
      """,
    ),
  ],
}
