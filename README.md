# Projet-POA
Metal Gear Solid VI : Return of the Cat

# Instructions d'installation (Linux)
python3 -m pip install --user --upgrade pip

python3 -m venv env

source env/bin/activate

python3 -m pip install requests

pip install pygame

# A faire

Faire en sorte que tout les chats s'update l'état en même temps (i.e quand 1 passe à last_seen=False, tout le monde aussi)

L'idée : faire un blackboard avec un attribut "last_seen" partagé par tous les chats

Régler cône vision (DONE)

Les chats effacent le trou en marchant dessus

variable but atteint dans classe chat

Fonction chase dans chat

# Perspectives d'amélioration (plus tard)

D'autres actions style jump
D'autres sens 
- Capteurs olfactifs
- Capteurs auditifs : Si le joueur marche sur une branche, le chat se dirigera vers ce bruit

- Patrouille améliorée du chat (ex: tourner autour du trou)