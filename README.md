Vous étant récemment amouraché avec une étudiante de l’UCL, vous devez faire face à
un problème logistique des plus épineux : comment se rendre à son kot à toute heure du jour
ou de la nuit alors que vous ne possédez pas de voiture ? N’étant pas du genre à attendre des
heures à Delta qu’une bonne âme daigne vous accepter dans sa voiture, vous imaginez une
plateforme de co-voiturage, laquelle vous permettrait d’exprimer votre souhait d’être pris en
stop, tout en restant au chaud dans votre canapé.
Après avoir conduit une analyse préliminaire, une série de fonctionnalités vous apparaît comme indispensable. Chaque utilisateur doit pouvoir :
  • Se créer un compte avec son nom d’utilisateur : à l’inscription, l’utilisateur doit fournir
un mot de passe permettant de protéger son compte.
  • Se connecter avec son nom d’utilisateur et le mot de passe correspondant.
  • Mettre à disposition sa voiture pour les autres utilisateurs. Il doit pour ce faire indiquer :
– la date de départ (tous les trajets durent une journée complète) ;
– les villes de départ et d’arrivée depuis une liste prédéfinie de villes. Cette liste de
villes aura été préalablement enregistrée, par un administrateur, dans la base de
données via l’interface d’administration de Django.
• Faire une recherche des véhicules disponibles sur base de la ville de départ, d’arrivée,
de la date de départ et d’en choisir un parmi ceux proposés. Bien entendu, celui-ci ne
pourra pas être réservé par d’autres personnes pour le même jour.
  • Afficher sur un calendrier les différentes réservations qu’il a faites et afficher sur un
autre calendrier les réservations de sa voiture par d’autres utilisateurs.
