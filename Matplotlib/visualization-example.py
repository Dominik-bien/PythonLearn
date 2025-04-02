import pandas as pd
import matplotlib.pyplot as plt

# Załaduj dane z CSV (przykład z pliku 'dane_GUS.csv')
df = pd.read_csv('dane_GUS.csv')

# Sprawdzenie pierwszych kilku wierszy, by zrozumieć strukturę danych
print(df.head())

# Rozbijamy kolumnę "Rok" na lata (zakładając, że format to '2019-2023')
df[['Rok_Początek', 'Rok_Koniec']] = df['Rok'].str.split('-', expand=True)

# Zamieniamy wartości "Rok_Początek" na int
df['Rok_Początek'] = df['Rok_Początek'].astype(int)
df['Rok_Koniec'] = df['Rok_Koniec'].astype(int)

# Rozwijamy dane, tworząc rekordy dla każdego roku w zakresie
expanded_data = []
for index, row in df.iterrows():
    for year in range(row['Rok_Początek'], row['Rok_Koniec'] + 1):
        expanded_data.append({
            'Rok': year,
            'Wartość': row['Wartość']
        })

# Tworzymy nowy DataFrame z rozwiniętych danych
expanded_df = pd.DataFrame(expanded_data)

# Wizualizacja danych
plt.figure(figsize=(10, 6))
plt.plot(expanded_df['Rok'], expanded_df['Wartość'], marker='o', color='b', label='Wartość')
plt.title('Wartości w latach 2019-2023')
plt.xlabel('Rok')
plt.ylabel('Wartość')
plt.grid(True)
plt.legend()
plt.show()
