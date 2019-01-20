import pandas as pd
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag

dane=pd.read_csv(r"C:\Users\madga\Desktop\projekt13\baza.csv", sep=',t', engine='python', delimiter=',')
# print(dane)
kolumnab=dane["sygnal1"]
kolumnaf=dane["liczby"]

t = np.linspace (0, 37.9, 200*37.9)
plt.plot(t, kolumnab)
plt.title("Czysty sygnał")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()

#przefiltrowany1
przefiltrowany=ag.pasmowozaporowy(kolumnab, 200, 49, 51)
#przefiltrowany2
przefiltrowany2=ag.pasmowoprzepustowy(przefiltrowany, 200, 1, 50)
plt.plot(t, przefiltrowany2)
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [-]')
plt.title("Przefiltrowany sygnał")
plt.show()

# Wyświetla wystukane przez OB cyfry, poprzez wyszukanie najwiękych wartości w kolumnie 'sygnal1'
print(dane[dane.sygnal1>1.2]['liczby'])
