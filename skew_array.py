import matplotlib.pyplot as plt

def delta(base):
    """Retourne +1 pour G, -1 pour C, 0 sinon."""
    b = base.upper()  # rend la lettre insensible à la casse
    if b == "G":
        return 1
    if b == "C":
        return -1
    return 0

# mini-vérifications visuelles
print("G ->", delta("G"))   # attendu +1
print("C ->", delta("C"))   # attendu -1
print("A ->", delta("A"))   # attendu 0
print("T ->", delta("T"))   # attendu 0
print("N ->", delta("N"))   # attendu 0
#Je demande à Python de vérifier si delta("G") donne bien 1
assert delta("G") == 1
assert delta("C") == -1

def compute_skew(seq):
    """Construit le profil cumulatif du skew (version 3 : logique avec delta)."""
    skew = [0]
    for ch in seq:
        contribution = delta(ch)          # -1 si C, +1 si G, 0 sinon
        new_value = skew[-1] + contribution
        skew.append(new_value)
    return skew

print("compute_skew('CAGC') ->", compute_skew("CAGC"))

assert compute_skew("CAGC") == [0, -1, -1, 0, -1]
print("Test compute_skew : OK ✅")

def show_deltas(seq):
    print("Index | Base | Delta | Skew")
    print("-----------------------------")
    skew = [0]
    for i, ch in enumerate(seq, start=1):
        d = delta(ch)                 # contribution de la base
        current = skew[-1] + d        # nouvelle valeur cumulée
        skew.append(current)
        print(f"{i:5d} |   {ch}   | {d:+5d} | {current:4d}")

show_deltas("CAGC")

def min_positions(skew):
    """Renvoie la liste des indices où skew atteint son minimum."""
    m = min(skew)
    return [i for i, v in enumerate(skew) if v == m]

# démo rapide sur notre exemple
s = compute_skew("CAGC")
print("Skew:", s)
print("Indices du minimum:", min_positions(s))  # attendu : [1, 2, 4]

def plot_skew(seq):
    """Trace la courbe du skew cumulatif pour une séquence donnée."""
    skew = compute_skew(seq)
    positions = list(range(len(skew)))     # axe des X = positions
    plt.plot(positions, skew, marker="o")  # trace la courbe
    plt.xlabel("Position")
    plt.ylabel("Skew cumulatif (G - C)")
    plt.title("Profil SkewArray")
    plt.grid(True)
    plt.savefig("skew_plot.png", dpi=300, bbox_inches="tight")
    print("Graphique enregistré sous le nom : skew_plot.png ✅")
    plt.show()

# démo
plot_skew("CAGC")
