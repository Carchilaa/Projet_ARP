# Projet_ARP - Modelisation algorithme de resolution marriage stable one-to-one
Algorithme de resolution marriage stable one-to-one

## Description du Probleme - Mariage One-to-One
Etant donnée une liste d'hommes et une liste de femmes, chacun avec une liste de preferences du sexe opposé, le problème de marriage stable consiste a trouvé si possible un "mariage" qui ait la proprieté d'être stable. 

Exemple de listes de preference:
<p align="center">
<img width="438" height="285" alt="image" src="https://github.com/user-attachments/assets/aa1bc8a8-90bf-4d07-9469-676c75dd100c" />
</p>

Une situation est dit inestable, si il existe au moins un couple (A,B) et (C,D) tels que A prefère C et B prefère D. C'est a dire, aucun homme ni femme as envie de changer de couple.

Contraintes du probleme:
  Chaque couple doit etre stable => le mariage est optimal -> tout le monde est satisfait. \
  Chaque homme doit avoir 1 femme partenaire\
  Chaque femme doit avoir 1 homme partenaire

### Redaction du probleme en 5 étapes:
  -Etat initial =>  \
  -Les actions => isvalid(S){return oui ou non en fonction de l'etat}\
  -succeseur => suc(s,a) list des candidats pour l'etat S\
  -Etat Final => isterminal(S) -> un etat but est une valuation complete telle que chaque contrainte est satisfaite.\

## Modelistation du problème
  Etat Initial S0 : On a M(1,n), un tableau vide des couples (i,j) hommes/femmes où M(i) = j.\
  Action A: A chaque homme, on le marrie temporairement a une femme qui est pas dans un couple et on test la stabilité.\
  succeseur suc(s,a): Liste de hommes est femmes deja marrié.\
  Etat final T: Le tableau M avec la liste des couples (i,j) stables.\
  c(s,s'):0

## Point importants du code.

  Le code est divisé en 2 partie importantes:
    - La verification de la stabilité \
    - L'algorithme backtrack qui permet de generer les couples.

**Pour la verification de la stabilité de tout les couples**, une fonction **is_stable()** qui prend comme parametres la liste des couples et les 2 liste des preferences de deux sexes. Pour dire que un couple est pas stable, on boucle sur tout les couples et pour chaque couple, on verifie si l'homme ne prefere pas une autre femme et de meme avec la femme. 


**Pour la creation des couples**, l'algorithme backtrack ce charge de prendre un homme h et forme un couple avec tout les femmes qui ne sont pas marries encore. En suite, il repete le processus avec l'homme h + 1. Une fois tout les couples fait, il verifie la stabilite de la solution. Si elle est pas stable, on efface les couples faites. L'algorithme s'arrete lors que la premiere solution est trouvee. Mais ceci ne veux pas dire que il y a plus de une solution possible pour resoudre ce probleme.



