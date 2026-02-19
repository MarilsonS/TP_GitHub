# TP Git — Student List Manager

## Marilson SOUZA DE JESUS FILHO

Projet en **Python** : un programme en ligne de commande (CLI) pour gérer une liste d’élèves.

Note : Le TP devait être fait en binôme, mais je l’ai fait seul car je n’ai pas pu assister au dernier cours à cause d’une situation familiale et je n’avais pas de partenaire. J’ai assisté aux cours précédents et j’ai fait ce TP en suivant toutes les étapes comme si j’étais en binôme.

---

## 1) Structure du projet

```
README.md
.gitignore
main.py
student.py
student_service.py
```

---

## 2) Lancer le programme

Depuis la racine du projet :

```bash
python .\main.py
```

---

## 3) Commandes dans le programme (CLI)

- `list`
- `add <id> <name>`
- `remove <id>`
- `export <format> <file_path>`
- `help`
- `quit`

---

## 4) Phases du TP

### Phase 1
J’ai créé le dépôt, puis j’ai ajouté les premiers fichiers (`README.md` et `.gitignore`).  
Après, j’ai fait mon premier commit et j’ai envoyé sur GitHub.

```bash
git add .
git commit -m "first commit"
git push -u origin main
```

(Si j’étais en binôme, l’autre personne peut faire ->)
```bash
git pull
```

---

### Phase 2
J’ai créé une branche pour les interfaces.  
J’ai ajouté `student.py` (structure id + nom).  
J’ai ajouté `student_service.py` avec les fonctions **sans implémentation**.

```bash
git checkout -b feature/interfaces
```

```bash
git add student.py
git commit -m "added student file"
```

```bash
git add student_service.py
git commit -m "added student-service, functions without implementation"
git push -u origin feature/interfaces
```

(Si j’étais en binôme, l’autre personne peut récupérer la branche comme ça)
```bash
git switch feature/interfaces
```

---

### Phase 3
J’ai vérifié si j’ai besoin d’un rebase, puis j’ai fusionné dans `main`.  
Ensuite, j’ai supprimé la branche.

```bash
git rebase main
```

```bash
git switch main
git merge feature/interfaces
git push
```

```bash
git branch -d feature/interfaces
git push origin --delete feature/interfaces
```

---

### Phase 4
Même si j’étais seul, j’ai suivi le TP avec deux branches.

#### 4A) StudentService
J’ai créé `feature/student-service` et j’ai implémenté les fonctions.

```bash
git checkout -b feature/student-service
git push -u origin feature/student-service
```

```bash
git add .
git commit -m "implemented student_service functions"
git push
```

#### 4B) Main CLI
J’ai créé `feature/main-cli` et j’ai fait l’interface CLI dans `main.py`.

```bash
git checkout -b feature/main-cli
git push -u origin feature/main-cli
```

---

### Phase 5
J’ai intégré les branches dans `main`.

D’abord, j’ai fusionné `feature/student-service` :

```bash
git switch main
git pull
git merge feature/student-service
git push
```

Après, j’ai intégré `feature/main-cli`. J’ai fait un rebase pour éviter des problèmes :

```bash
git switch feature/main-cli
git rebase main
git switch main
git merge feature/main-cli
git push
```

---

### Phase 6
J’ai ajouté un export **JSON** dans une branche, et un export **YAML** dans l’autre.

#### 6A) Export A (JSON)
```bash
git checkout -b feature/export-a
git push -u origin feature/export-a
```

```bash
git add .
git commit -m "added json support"
git push
```

#### 6B) Export B (YAML)
```bash
git checkout -b feature/export-b
git push -u origin feature/export-b
```

```bash
git add .
git commit -m "added yaml support"
git push
```

---

### Phase 7
J’ai fusionné `feature/export-a` dans `main`.  
Après, j’ai fusionné `feature/export-b` et j’ai eu un conflit.  
J’ai résolu le conflit avec l'outil de VSCode, puis j’ai fait un commit de résolution.

```bash
git switch main
git merge feature/export-a
git push
```

```bash
git switch main
git pull
git merge feature/export-b
```
![Logo](https://cdn.discordapp.com/attachments/405357359754641409/1473988401001922654/image.png?ex=6998362c&is=6996e4ac&hm=cd2659a608cb71ff5e239c11348d1b71326b8e447d94d529b2e5df6556436715)

Après la résolution du conflit :
```bash
git add .
git commit
git push
```

---
À la fin, j’ai écrit ce README. Je vais faire un commit et un push, puis ajouté un tag `v1.0` comme ça.

```bash
git tag v1.0
git push origin v1.0
```