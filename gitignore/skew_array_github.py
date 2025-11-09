#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mini-projet 2 : SkewArray
-------------------------
Objectif
    Calculer le biais GC cumulatif (Skew) d’une séquence ADN :
        +1 pour G, -1 pour C, 0 pour A/T/lettres autres.

Ce fichier contient :
    - delta(base) : variation due à une base
    - compute_skew(seq) : profil cumulatif (skew array)
    - min_positions(skew) : indices où la courbe atteint son minimum (prépare MinimumSkew)
    - show_deltas(seq) : affichage pédagogique lettre par lettre (delta + skew)
    - plot_skew(seq, out_png) : trace et enregistre la courbe (PNG)
    - main() : petite interface ligne de commande (séquence directe OU lecture d’un FASTA simple)

Prêt pour GitHub :
    - Code structuré + docstrings
    - Aucune dépendance lourde (Matplotlib est standard)
    - Facile à étendre (lecture FASTA plus robuste, intégration Biopython, NCBI/GEO)

TODO (plus tard) :
    - Remplacer read_fasta_first_seq par Biopython (SeqIO) si besoin
    - Lire de longues séquences NCBI (RefSeq/GenBank) ou des jeux d’expression (GEO) dans d’autres scripts
"""

from typing import List
from pathlib import Path
import argparse
import matplotlib.pyplot as plt


# ---------- 1) Base -> delta -------------------------------------------------
def delta(base: str) -> int:
    """
    Retourne la variation unitaire du skew pour une base.
        G -> +1
        C -> -1
        A/T/Autre -> 0
    """
    b = base.upper()
    if b == "G":
        return 1
    if b == "C":
        return -1
    return 0


# ---------- 2) Skew cumulatif ------------------------------------------------
def compute_skew(seq: str) -> List[int]:
    """
    Construit la liste des skews cumulés le long de la séquence.
    Convention :
        skew[0] = 0 (avant la 1ère base)
        skew[i] = skew[i-1] + delta(seq[i-1])
    Longueur de sortie : len(seq) + 1
    """
    skew = [0]
    for ch in seq:
        contribution = delta(ch)               # -1, 0, +1 selon la base
        new_value = skew[-1] + contribution    # cumul
        skew.append(new_value)
    return skew


# ---------- 3) Indices du minimum -------------------------------------------
def min_positions(skew: List[int]) -> List[int]:
    """
    Renvoie toutes les positions où le skew atteint son minimum.
    Utile pour MinimumSkew (candidats OriC en génomes bactériens).
    """
    m = min(skew)
    return [i for i, v in enumerate(skew) if v == m]


# ---------- 4) Affichage pédagogique -----------------------------------------
def show_deltas(seq: str) -> None:
    """
    Affiche, pour chaque base, sa contribution (delta) et la nouvelle valeur skew.
    Pratique pour COMPRENDRE pas à pas le calcul.
    """
    print("Index | Base | Delta | Skew")
    print("-----------------------------")
    skew_val = 0
    for i, ch in enumerate(seq, start=1):
        d = delta(ch)
        skew_val += d
        print(f"{i:5d} |   {ch}   | {d:+5d} | {skew_val:4d}")


# ---------- 5) Tracé + enregistrement PNG -----------------------------------
def plot_skew(seq: str, out_png: str = "skew_plot.png", show: bool = True) -> None:
    """
    Trace la courbe du skew cumulatif et l’enregistre en PNG (300 dpi).
    Paramètres :
        - seq     : séquence ADN (string)
        - out_png : nom du fichier image (sauvegardé dans le dossier courant)
        - show    : afficher la fenêtre graphique (True par défaut)
    """
    skew = compute_skew(seq)
    positions = list(range(len(skew)))         # axe X = 0..len(seq)
    plt.figure()
    plt.plot(positions, skew, marker="o")
    plt.xlabel("Position")
    plt.ylabel("Skew cumulatif (G - C)")
    plt.title("Profil SkewArray")
    plt.grid(True)
    plt.savefig(out_png, dpi=300, bbox_inches="tight")
    print(f"[OK] Graphique enregistré : {out_png}")
    if show:
        plt.show()
    plt.close()


# ---------- 6) Lecture FASTA simple (sans Biopython) -------------------------
def read_fasta_first_seq(path: str) -> str:
    """
    Lit la 1ère séquence d’un fichier FASTA (parser minimaliste).
    - Ignore les lignes d’entête (débutant par '>')
    - Concatène les lignes de séquence
    - Met en majuscules et retire espaces
    NB : pour des FASTA complexes, préférer Biopython (SeqIO).
    """
    seq_parts: List[str] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(">"):
                continue
            seq_parts.append(line)
    return "".join(seq_parts).upper()


# ---------- 7) Interface CLI minimale ----------------------------------------
def parse_args() -> argparse.Namespace:
    """
    Options utilisateur :
        --seq   "CAGC"         : donner la séquence directement
        --fasta chemin.fasta   : lire la 1ère séquence d’un FASTA
        --no-show              : ne pas afficher la fenêtre du graphique
        --out    nom.png       : nom du fichier image à enregistrer
    """
    p = argparse.ArgumentParser(description="Calcul et tracé du SkewArray")
    p.add_argument("--seq", type=str, help="Séquence ADN (ex: CAGC)")
    p.add_argument("--fasta", type=str, help="Chemin vers un fichier FASTA (1ère séquence lue)")
    p.add_argument("--no-show", action="store_true", help="N’affiche pas la fenêtre du graphique")
    p.add_argument("--out", type=str, default="skew_plot.png", help="Nom du PNG de sortie (défaut: skew_plot.png)")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    # 1) Récupérer la séquence (priorité au FASTA si fourni)
    if args.fasta:
        fasta_path = Path(args.fasta)
        if not fasta_path.exists():
            raise FileNotFoundError(f"Fichier introuvable : {fasta_path}")
        seq = read_fasta_first_seq(str(fasta_path))
        source = f"FASTA({fasta_path.name})"
    elif args.seq:
        seq = args.seq.strip().upper()
        source = "SEQ(direct)"
    else:
        # Valeur par défaut pédagogique pour tester
        seq = "CAGC"
        source = "SEQ(defaut:CAGC)"

    # 2) Calculs
    skew = compute_skew(seq)
    mins = min_positions(skew)

    # 3) Affichages console (résumés)
    print(f"[Source] {source}")
    print(f"[Longueur séquence] {len(seq)}")
    print(f"[Skew - 1ers points] {skew[: min(10, len(skew))]}{' ...' if len(skew) > 10 else ''}")
    print(f"[Min skew] valeur={min(skew)} aux indices={mins}")

    # 4) Affichage pédagogique (petites séquences)
    if len(seq) <= 60:
        show_deltas(seq)   # utile pour comprendre ; pour de grands génomes, on éviterait

    # 5) Tracé + sauvegarde
    plot_skew(seq, out_png=args.out, show=(not args.no_show))


if __name__ == "__main__":
    main()
