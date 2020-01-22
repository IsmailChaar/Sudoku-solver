# Sudoku-solver
This is a Sudoku solver with Backtracking. The code was very fun to write :) !

<p align="center">
  <img src="hhttps://i.ibb.co/cJ8K3wJ/Screenshot.png">
</p>

# Fonctionnement de l'algorithme

1) Trouver un espace vide
2) Essayer de placer les chiffres 1-9 dans cet espace
3) Vérifier si ce chiffre est valide à l'emplacement actuel en fonction de la matrice actuelle
  a. Si le chiffre est valide, essayer récursivement de remplir le tableau en suivant les étapes 1 à 3.
  b. S'il n'est pas valide, réinitialiser le carré que vous venez de remplir et revener à l'étape précédente.
4) Une fois que la carte est pleine par la définition de cet algorithme, nous avons trouvé une solution.
