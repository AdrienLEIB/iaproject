# iaproject TIC TAC TOE

Il s'agit d'un projet noté pour valider les crédits ects de l'elective IA Programming. 
Ce travail a été réalisé par : NGOUNÉ Cédric, DJENNANE Madjid et LEIB Adrien.

Il présente 5 scripts qui chacun présentent d'une certaine façon une fonction du programme principale.

1) tictactoe_with_iarandom.py -> ce script fait jouer 2 joueurs, une ia qui va jouer de manière aléatoire et un le joueur ( vous ) . Celui-ci mets en évidence la fonction "generate_win_possibility" afin de prouver que celle-ci renvoie à chaque coup la liste des possibilités de victoire.

2) tictactoe_with_iaminimax.py -> Ce script fait jouer 2 joueurs, une ia qui se base sur le principe de minimax et un joueur ( vous ) . Celui-ci mets en avant la fonction minimax et prouve qu'elle capable de s'adapter pour chaque taille de grille. Hélas plus la taille de grille est grande et plus le nombre de calcul le sera aussi, par conséquent le temps de réponse sera plus long. C'est pourquoi un exemple rapide est disponible sur le script démo. 

3) tictactoe_with_iaminimax_demo.Py -> Ce script fait joueur 2 joueurs à un moment T de la partie sur une taille de grille de 5 de largeurs et de 2 de longueurs. Il a pour utilité de prouver que la fonction minimax fonctionne et qu'il lui faut du temps.

4) " " -> Ce script est une optimisation du minimax avec le principe d'alphabeta et un calcul différent des possibilités de victoire pour permettre un jeu plus rapide et plus cohérent.


5) " " -> Ce script prends en compte les optimisationd du script 4 , et en fait démo simple et un moment T de la partie pour prouver qu'il fonctionne correctement.
