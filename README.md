# SkewArray — Mini-Project 2  
**Genome Analysis Fundamentals**  
*(English and Français)*  

**Période / Period :** 2025-11-06 → 2025-11-11  
**Durée approximative / Approx. duration :** 6 jours / 6 days  
**Statut / Status :** Terminé ✅ / Completed ✅

---

## ENG Overview  
This mini-project computes and visualizes the **GC SkewArray**, a classical algorithm in bacterial genomics used to identify replication origins (OriC) and termini (TerC).  
It is part of a personal learning roadmap in bioinformatics and genomic data science.

### Objective  
To calculate the cumulative GC bias along a DNA sequence and visualize its variations.

### Biological Meaning  
- GC skew measures how often **G** appears compared to **C** in a sequence.  
- When the skew curve changes direction, it often indicates **replication origin** or **termination** regions.

### Example  
```bash
python skew_array_PERSO.py --seq "AGCGCGTTGCCGATGCGTACG" and "CAGTCGCGGATCGATCGTACGCGTACGTGC"
```


**Generated Graph**  
The file `skew_plot.png` contains the GC skew curve across the sequence, where changes in slope may correspond to replication origin and terminus.

### Files  
- `skew_array.py` → algorithm and visualization  
- `skew_plot.png` → saved graphical output  
- `README.md` → this documentation file  

---

## 🇫🇷 Résumé  
Ce mini-projet calcule et visualise le **biais GC cumulatif (SkewArray)**, un outil classique de la génomique bactérienne permettant d’identifier les **origines (OriC)** et **terminaisons (TerC)** de réplication.  
Il fait partie de ma feuille de route d’apprentissage en bio-informatique et en science des données génomiques.

### Objectif  
Calculer le biais cumulatif entre les bases G et C le long d’une séquence et observer ses variations sur une courbe.

### Signification biologique  
- Le biais GC (skew) exprime la différence de fréquence entre les bases G et C.  
- Les inversions de pente du graphique indiquent souvent une **origine** ou une **terminaison de réplication**.

### Exemple  
```bash
python skew_array_PERSO.py --seq seq "AGCGCGTTGCCGATGCGTACG" and "CAGTCGCGGATCGATCGTACGCGTACGTGC"
```

**Graphique généré**  
Le fichier `skew_plot.png` affiche la courbe du biais GC cumulatif, où les changements de direction traduisent les zones critiques de réplication.

### Fichiers  
- `skew_array.py` : algorithme et visualisation  
- `skew_plot.png` : graphique enregistré  
- `README.md` : ce fichier descriptif  

### Personal notes/ Notes personnelles
This work was initially completed in skew_array.py with support from AI tools and Coursera. I then reworked, analyzed, and tested the code in skew_array_PERSO.py as a hands-on practice exercise.
Ce travail a été réalisé dans skew_array.py avec l'aide de IA et Coursera. Puis, j'ai retravaillé le code, analysé et testé dans skew_array_PERSO.py, en guise d'exercice d'application.
---

> — Yasmina Soumahoro
