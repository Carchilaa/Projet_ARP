# Projet_ARP
Algorithme de resolution marriage stable one-to-one

## Description du Probleme - Mariage One-to-One
Etant donnée une liste d'hommes et une liste de femmes, chacun avec une liste de preferences du sexe opposé, le problème de marriage stable consiste a trouvé si possible un "mariage" qui ait la proprieté d'être stable. 

Exemple de listes de preference:
<p align="center">
<img width="438" height="285" alt="image" src="https://github.com/user-attachments/assets/aa1bc8a8-90bf-4d07-9469-676c75dd100c" />
</p>

Une situation est dit inestable, si il existe au moins un couple (A,B) et (C,D) tels que A prefère C et B prefère D. C'est a dire, aucun homme ni femme as envie de changer de couple.

Contraintes du probleme:
  Chaque couple doit etre stable => le mariage est optimal -> tout le monde est satisfait.
  Chaque homme doit avoir 1 femme partenaire
  Chaque femme doit avoir 1 homme partenaire

### Redaction du probleme en 5 étapes:
  -Etat initial =>  \
  -Les actions => isvalid(S){return oui ou non en fonction de l'etat}\
  -succeseur => suc(s,a) list des candidats pour l'etat S\
  -Etat Final => isterminal(S) -> un etat but est une valuation complete telle que chaque contrainte est satisfaite.\

  
