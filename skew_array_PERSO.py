import csv
import matplotlib.pyplot as plt

def gc_variation(base): #The function counts the number of G and C nucleotides.
    b = base.upper() #The function converts the base to uppercase
    if b == "G":
        return 1
    elif b == "C":
        return -1 
    else :
        return 0

def compute_skew(genome): # Calculate the skew of the sequence.
    skew = [0] #Counting always starts from 0.
    for base in genome:
        if base == "G":
            skew.append(skew[-1] + 1) #skew[-1] is the last cumulative value in the array; update it for each processed base.
        elif base == "C":
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])
    return skew

print("compute_skew('CAGTCGCGGATCGATCGTACGCGTACGTGC')", compute_skew("CAGTCGCGGATCGATCGTACGCGTACGTGC"))  #Python will print the text followed by the count value.

# Proceed to display the results in a structured table format.
def show_gc_variation(genome):
    print("Index | Base | Delta | Skew")
    print("----------------------------")
    skew = [0]
    results = []
    for i, base in enumerate(genome, start=1):
        d = gc_variation(base) #Call the function here to measure the local effect of each base on the G/C imbalance.
        current = skew[-1] + d #Add the variation of the current base to the last recorded value in the skew list.
        skew.append(current) #Append the new skew value (current) to the skew list for plotting or further analysis.
        print(f"{i:5d} |   {base}   | {d:+d} | {current:d}") #Use an f-string to format and neatly align the calculation progress at each position to visualize the skew dynamics.
        results.append([i, base, d, current])

# --- Export CSV ---
    with open("skew_results.csv", "a", newline="", encoding="utf-8") as file: #The result of each test is saved
        writer = csv.writer(file)
        writer.writerow(["Index", "Base", "Delta", "Skew"])
        writer.writerows(results)
print("\n Résultats enregistrés dans 'skew_results.csv'")

def min_positions(skew): #Return the list of indices (positions) where the skew reaches its minimum value.
    m = min(skew)
    return [i for i, v in enumerate(skew) if v == m] #Iterate through the sequence with both index and value, then filter to keep only (in a list) the indices where the skew reaches its lowest point.

def plot_skew(genome):
    #Plot the cumulative skew curve for a given sequence.
    skew = compute_skew(genome)
    positions = list(range(len(skew)))     # X-axis: sequence positions.
    plt.plot(positions, skew, marker="o")  # Plot the curve.
    plt.xlabel("Position")
    plt.ylabel("Cumulative skew (G - C)")
    plt.title("SkewArray Profile")
    plt.grid(True)
    plt.savefig("skew_plot.png", dpi=300, bbox_inches="tight")
    print("Graph saved as skew_plot.png")
    plt.show()

#Compute and export the values.
show_gc_variation("CAGTCGCGGATCGATCGTACGCGTACGTGC")
#Generate the plot
plot_skew("CAGTCGCGGATCGATCGTACGCGTACGTGC")