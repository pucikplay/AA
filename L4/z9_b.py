from z9_a_1 import nakamoto,grundspan
import numpy as np
import random as rnd
import matplotlib.pyplot as plt

n_vals = [1,3,6,12,24,48]
q_vals = [q for q in np.arange(0.005,0.5,0.005)]
no_tests = 10000

# Symulator sprowadza się to sprawdzania kto policzy kolejny blok
# prawdopodobieństwo jest proporcjonalne do posiadanej mocy obliczeniowej,
# czyli odpowiednio q i 1-q dla adwersarza i uczciwych użytkowników
# jeśli po wygenerowaniu n bloków na gałęzi uczciwej gałąź adwersarza jest dłuższa
# to atak zakończył się sukcesem. Jeśli nie, dajemy adwersarzowi jeszcze pewną
# liczbę bloków na dogonienie odpowiadającą parametrowi cutoff.
# Jeśli nie uda się mu dogonić to atak kończy się niepowodzeniem
def dsa(n, q, cutoff):
    legit_branch = 0 # długość gałęzi uczciwej
    adv_branch = 0 # długość gałęzi adwersarza

    while True:
        if rnd.random() <= q: # przedłuż gałęzie w zależności od mocy obliczeniowej
            adv_branch += 1
        else:
            legit_branch += 1

        if legit_branch < n: # dopóki gałąź uczciwa < n licz dalej
            continue
        
        if adv_branch >= legit_branch: # jeśli gałąź adwersarza nie krótsza to sukces
            return True
        elif legit_branch >= n + cutoff: # jeśli nie udało się dogonić to porażka
            return False

# Metoda Monte Carlo, wykonujemy symuulację wielokrotnie i uśredniamy wynik
def mc_dsa(n, q, t, cutoff):
    succ = 0

    for _ in range(t):
        if dsa(n, q, cutoff):
            succ += 1
    
    return succ/t

if __name__ == "__main__":
    for n in n_vals:
        p_nakamoto = []
        p_grundspan = []
        p_sim = []
        for q in q_vals:
            p_nakamoto.append(nakamoto(n,q))
            p_grundspan.append(grundspan(n,q))
            p_sim.append(mc_dsa(n,q,no_tests,50))
        plt.scatter(q_vals, p_nakamoto, label='nakamoto', s=5)
        plt.scatter(q_vals, p_grundspan, label='grundspan', s=5)
        plt.scatter(q_vals, p_sim, label='simulated', s=5)
        plt.xlabel('q')
        plt.ylabel('p_nq')
        plt.title('n={}'.format(n))
        plt.legend()
        plt.savefig('L4/charts/n={}_sim.png'.format(n), dpi=300)
        plt.close()

    p_cutoff = {0: [], 10: [], 50: [], 100: []}
    for q in q_vals:
        p_cutoff[0].append(mc_dsa(24,q,no_tests,0))
        p_cutoff[10].append(mc_dsa(24,q,no_tests,10))
        p_cutoff[50].append(mc_dsa(24,q,no_tests,50))
        p_cutoff[100].append(mc_dsa(24,q,no_tests,100))
    plt.scatter(q_vals, p_cutoff[0], label='0', s=5)
    plt.scatter(q_vals, p_cutoff[10], label='10', s=5)
    plt.scatter(q_vals, p_cutoff[50], label='50', s=5)
    plt.scatter(q_vals, p_cutoff[100], label='100', s=5)
    plt.xlabel('q')
    plt.ylabel('p_nq')
    plt.title('n={}'.format(n))
    plt.legend()
    plt.savefig('L4/charts/cutoff.png'.format(n), dpi=300)
    plt.close()
