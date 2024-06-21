import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

# Zad.1
# labels = ['Włochy','Hiszpania', 'Francja', 'Inne',]
# sizes = [24.8, 13, 6.7, 55.5]
# colors = ['lightcoral', 'skyblue', 'springgreen', 'thistle',]
# explode = [0.1, 0, 0, 0]
#
# plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=135)
#
# plt.title('Najczęściej odwiedzane kraje przez Polaków')
# plt.axis('equal')
# plt.savefig('Wykres odwiedzanych krajów przez Polaków.pdf')
# plt.show()



# Zad.2
# file_patch = 'C:/Users/Fenrir/Desktop/PyCharm/Egzamin_Zerowy/konie11.xlsx'
# df = pd.read_excel(file_patch)
# print(df.head())
#
# opolskie_data= df[df['Nazwa'] == 'OPOLSKIE']
# print(opolskie_data.head())
#
# lata = opolskie_data['Rok']
# wartosci = opolskie_data['Wartość']
#
# plt.figure(figsize=(10,6))
# plt.bar(lata, wartosci, color='skyblue', width=0.6)
#
# plt.title('Dane dla województwa opolskiego')
# plt.xlabel('Lata')
# plt.ylabel('Wartość')
# plt.savefig('Wykres2.jpg')
# plt.show()


# Zad.3
# file_patch = 'C:/Users/Fenrir/Desktop/PyCharm/Egzamin_Zerowy/lasy11.xlsx'
# df_lasy = pd.read_excel(file_patch)
# print(df_lasy.head())
#
# df_melted = pd.melt(df_lasy, id_vars=['Województwo'], var_name='Rok',
#                     value_name='Wartość')
# print(df_melted.head())
#
# df_cleaned = df_melted.dropna()
# print(df_cleaned.head())
#
# selected_województwa = ['POMORSKIE', 'OPOLSKIE', 'MAŁOPOLSKIE', 'MAZOWIECKIE']
# filtered_data = df_cleaned[df_melted['Województwo'].isin(selected_województwa)]
#
# print(filtered_data.head())
#
# pomorskie_data = filtered_data[filtered_data['Województwo'] == 'POMORSKIE']
# opolskie_data = filtered_data[filtered_data['Województwo'] == 'OPOLSKIE']
# małopolskie_data = filtered_data[filtered_data['Województwo'] == 'MAŁOPOLSKIE']
# mazowieckie_data = filtered_data[filtered_data['Województwo'] == 'MAZOWIECKIE']
#
# print(pomorskie_data.head())
#
# plt.figure(figsize=(10,6))
# markers = {'POMORSKIE': 'o', 'OPOLSKIE': 's', 'MAŁOPOLSKIE': '^', 'MAZOWIECKIE': 'D'}
# colors = {'POMORSKIE': 'skyblue', 'OPOLSKIE': 'green', 'MAŁOPOLSKIE': 'yellow', 'MAZOWIECKIE': 'red'}
#
# for województwo in selected_województwa:
#     województwo_data = filtered_data[filtered_data['Województwo'] == województwo]
#     plt.scatter(województwo_data['Rok'], województwo_data['Wartość'],
#                 label=województwo, marker=markers[województwo], color= colors[województwo], s=100)
# plt.title('Dane dla wybranych województw:')
# plt.xlabel('Rok')
# plt.ylabel('Wartość')
# plt.legend(title='Województwo')
# plt.savefig('Wykres 3.png')
#
# plt.show()

# Zad.1
# labels = ['Pilka nozna', 'Siatkowka', 'Koszykowka', 'Inne']
# sizes = [24.8, 13, 6.7, 55.5]
# colors = ['red', 'blue', 'orange', 'green']
# explode = [0.1, 0, 0, 0]
#
# plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=0)
# plt.title('Wyniki ogladalnosci - II-IV 2022')
# plt.axis('equal')
# plt.savefig('Wykres Sportów.pdf')
# plt.show()



# Zad.2

# file_patch = 'C:/Users/Fenrir/Desktop/PyCharm/Egzamin_Zerowy/kozy12.xlsx'
# df_kozy12 = pd.read_excel(file_patch)
# print(df_kozy12.head())
#
# podlaskie_data = df_kozy12[df_kozy12['Nazwa'] == 'PODLASKIE']
# print(podlaskie_data.head())

# lata = podlaskie_data['Rok']
# wartosc = podlaskie_data['Wartość']
# plt.figure(figsize=(10,6))
# plt.bar(lata, wartosc, color='red', width=0.2,)
# plt.title('Wartość dla województwa Podlaskiego w latach', color='skyblue')
# plt.xlabel('Rok', color='green')
# plt.ylabel('Wartość', color='red')
# plt.savefig("Wykres Kóz.jpg")
# plt.show()

# Zad.3

# file_patch = 'C:/Users/Fenrir/Desktop/PyCharm/Egzamin_Zerowy/lasy12.xlsx'
# df_lasy12 = pd.read_excel(file_patch)
#
# print(df_lasy12.head())
#
# df_melted = pd.melt(df_lasy12, id_vars=['Województwo'], var_name='Rok', value_name='Wartości')
# print(df_melted.head())
# df_cleaned = df_melted.dropna()
#
#
# selected_wojewodztwa = ['PODLASKIE', 'OPOLSKIE', 'ŚLĄSKIE', 'MAZOWIECKIE']
#
# filtered_data = df_cleaned[df_melted['Województwo'].isin(selected_wojewodztwa)]
# print(filtered_data)
#
# plt.figure(figsize=(12, 8))
#
# line_styles = {'PODLASKIE': '-', 'OPOLSKIE': '--', 'ŚLĄSKIE': '-.', 'MAZOWIECKIE': ':'}
# markers = {'PODLASKIE': 'o', 'OPOLSKIE': 's', 'ŚLĄSKIE': '^', 'MAZOWIECKIE': 'D'}
# colors = {'PODLASKIE': 'blue', 'OPOLSKIE': 'green', 'ŚLĄSKIE': 'red', 'MAZOWIECKIE': 'purple'}
#
# # Rysowanie linii dla każdego województwa
# for wojewodztwo in selected_wojewodztwa:
#     wojewodztwo_data = filtered_data[filtered_data['Województwo'] == wojewodztwo]
#     plt.plot(wojewodztwo_data['Rok'], wojewodztwo_data['Wartości'],
#              label=wojewodztwo, linestyle=line_styles[wojewodztwo],
#              marker=markers[wojewodztwo], color=colors[wojewodztwo])
#
# plt.title('Dane dla wybranych województw')
# plt.xlabel('Rok')
# plt.ylabel('Wartość')
# plt.legend(title='Województwo:')
# plt.savefig('Wykres 9897.png')
# plt.show()

# Zad 1.

# labels = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec']
# zyski_filmowe = [50, 40.5, 38, 21.5, 26, 32,]
# zyski_gier = [22, 32.5, 41.5, 77, 66, 50,]
# plt.figure(figsize=(10, 6))
# plt.grid(True)
#
# plt.plot(labels, zyski_filmowe, 'b--', label='Filmy')
# plt.plot(labels, zyski_gier, 'g-', label='Gry')
#
#
# plt.title("Zyski z filmów i gier")
# plt.legend(loc = 2)
# plt.xlabel('Miesiąc', color="grey")
# plt.ylabel('Zyski', color='red')
# plt.ylim(0, 100)
# plt.yticks(range(0, 101, 20))
# plt.savefig("Wykres zmordenizowany.pdf")
# plt.show()

# Zad. 2
# # Załaduj dane z pliku Excel
# df = pd.read_excel('mieszkania1.xlsx')
#
# # Filtruj dane za rok 2016
# df_2016 = df[df['Rok'] == 2016]
#
# # Grupowanie danych według 'Formy budownictwa' i sumowanie 'Wartość'
# data = df_2016.groupby('Formy budownictwa')['Wartość'].sum()
#
# # Stwórz wykres kołowy
# plt.figure(figsize=(10, 7))
# plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
# plt.title('Wykres kołowy dla danych za 2016 rok')
#
# # Zapisz wykres w formacie PDF
# plt.savefig('wykres_kolowy_2016.pdf', format='pdf')
#
# # Wyświetl wykres
# plt.show()

# Zad. 3
#
# df_turystyka = pd.read_excel('turystyka1.xlsx')
#
# print(df_turystyka.head())
#
# df_turystyka.columns = df_turystyka.iloc[0]
# df_turystyka = df_turystyka.drop(0)
#
# df_turystyka = df_turystyka.reset_index(drop=True)
#
# df_long = pd.melt(df_turystyka, var_name='Year', value_name='Value')
#
# df_long.to_excel('C:/Users/Fenrir/Desktop/PyCharm/Egzamin_Zerowy/uporzątkowane dane.xlsx', index=False)
# print(df_long.head())
#
# years = df_long['Year'].unique()
# yearly_data = {year: df_long[df_long['Year'] == year].reset_index(drop=True) for year in years}
#
# print('Dane dla roku 2014:')
# print(yearly_data[2014].head())
#
# for year, data in yearly_data.items():
#     data.to_excel(f'C:/Users/Fenrir/Desktop/PyCharm/Egzamin_Zerowy/dane_{year}.xlsx', index=False)
#
# dane_2015 = yearly_data[2015]['Value'].astype(float).reset_index(drop=True)
# dane_2016 = yearly_data[2016]['Value'].astype(float).reset_index(drop=True)
#
# index_2015 = range(len(dane_2015))
# index_2016 = range(len(dane_2016))
#
# plt.figure(figsize=(10,6))
# plt.plot(index_2015, dane_2015, 'r--', label='2015 Data')
# plt.plot(index_2016, dane_2016, 'b:', label='2016 Data')
# plt.title('Turyści xD', fontsize=14)
# plt.xlabel('Index', fontsize=12)
# plt.ylabel('Value', fontsize=12)
# plt.legend()
# plt.grid(True)
#
# plt.tight_layout()
# plt.show()

# Zad.1
#
# labels = ['RMF FM', 'Radio Zet', 'Eska', 'Inne']
# sizes = [24.8, 13, 6.7, 55.5]
# colors = ['orange', 'skyblue', 'green', 'purple']
# explode = [0.1, 0, 0, 0]
#
# plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%',startangle=80, shadow=True)
#
# plt.title('Wyniki słuchalności - II-IV 2017')
# plt.axis('equal')
# plt.savefig('Wykres 76.pdf')
# plt.show()

# Zad. 2
#
# file_patch = 'turcja.xlsx'
# df = pd.read_excel(file_patch, sheet_name=0)
# df.to_excel('C:/Users/Fenrir/Desktop/PyCharm/Egzamin_Zerowy/Wczytane_dane.xlsx', index=False)
# print(df.head())
#
# df_ankara = df[(df['city'] == 'Ankara') & (df['years'] >= 2005) & (df['years'] <= 2010)]
# plt.figure(figsize=(10, 6))
# plt.bar(df_ankara['years'], df_ankara['pop'], color='darkblue')
# plt.title('Populacja w Ankara na przestzreni lat')
# plt.ylabel('Populacja ludzi', fontsize=12, color='purple')
# plt.xlabel('lata', fontsize=13, color='red')
# plt.xticks(df_ankara['years'])
# plt.grid(axis='y', linestyle='--', alpha=0.8)
# plt.tight_layout()
# plt.savefig('Wykres kjlhdf.jpg')
# plt.show()
# print(df_ankara.head())

# Zad. 3
## Załaduj dane z pliku Excel
# file_path = 'stacjepaliw.xlsx'
# df = pd.read_excel(file_path)
#
# # Usuń kolumnę 'Unnamed: 0' jeśli istnieje
# df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
#
# # Przekształć dane do formatu "czystych danych"
# df_tidy = df.melt(id_vars='Nazwa', var_name='Rok', value_name='Liczba Stacji')
# df_tidy = df_tidy.rename(columns={'Nazwa': 'Województwo'})
#
# # Konwersja kolumny 'Rok' na typ string, aby uniknąć problemów podczas filtrowania
# df_tidy['Rok'] = df_tidy['Rok'].astype(str)
#
# # Wyodrębnij dane dla województwa śląskiego i małopolskiego
# slaskie = df_tidy[(df_tidy['Województwo'] == 'ŚLĄSKIE') & (df_tidy['Rok'] >= '2015')]
# malopolskie = df_tidy[(df_tidy['Województwo'] == 'MAŁOPOLSKIE') & (df_tidy['Rok'] >= '2015')]
#
# # Wykres liniowy dla danych województwa śląskiego i małopolskiego
# plt.figure(figsize=(10, 6))
#
# # Dane dla Śląska
# plt.plot(slaskie['Rok'], slaskie['Liczba Stacji'], marker='o', label='Śląskie')
#
# # Dane dla Małopolski
# plt.plot(malopolskie['Rok'], malopolskie['Liczba Stacji'], marker='o', label='Małopolskie')
#
# # Ustawienia wykresu
# plt.title('Liczba stacji paliw w województwach Śląskim i Małopolskim (2015-2019)')
# plt.xlabel('Rok')
# plt.ylabel('Liczba stacji paliw')
# plt.legend(title='Województwo')
# plt.grid(True)
# plt.tight_layout()
#
# # Zapisz wykres do pliku
# plt.savefig('Wykres_35424.png')
#
# # Pokaż wykres
# plt.show()

# Zad. 1
# lata = [2017, 2018, 2019, 2020]
# mezczyzni = [18.66, 18.64, 18.62, 18.50]
# kobiety = [19.90, 19.88, 19.86, 19.70]
#
# plt.plot(lata, mezczyzni, label='Mężczyźni')
# plt.plot(lata, kobiety, label='Kobiety', color='orange')
#
# plt.title("Liczba ludności w Polcse według płci")
# plt.legend(loc=5)
# plt.yticks([18, 19, 20], ['18 mln', '19 mln','20 mln'])
# plt.xticks([2017, 2018, 2019, 2020],['2017', '2018', '2019', '2020'])
# plt.savefig('Wykres płci.pdf')
# plt.show()


# Zad.2
# file_path = 'konie.xlsx'
# df = pd.read_excel(file_path)
# print(df.head())
#
# lodzkie_data = df[df['Nazwa'] == 'ŁÓDZKIE']
#
# print(lodzkie_data.head())
#
# lata = lodzkie_data['Rok']
# wartosc = lodzkie_data['Wartość']
#
# plt.figure(figsize=(10, 6))
# plt.bar(lata, wartosc, color='skyblue', width=0.2)
# plt.title('Wartości dla województwa Łódzkiego od 2015-2020', color='red', size=18)
# plt.xlabel('Rok', color='blue')
# plt.ylabel('Wartości', color='purple')
# plt.xticks([2015, 2016, 2017, 2018, 2019, 2020], ['2015', '2016', '2017', '2018', '2019', '2020'])
# plt.grid(True)
# plt.savefig('Wykres wartości dla Łodzi.jpg')
#
# plt.show()



#Zad.3

# file_path = 'lasy17.xlsx'
# df = pd.read_excel(file_path)
#
# print(df.head())
#
# df_long = pd.melt(df, id_vars=['Województwo'], var_name='Rok', value_name='Wartość')
#
# print(df_long.head())
#
# selected_regions = ['POMORSKIE', 'OPOLSKIE', 'MAŁOPOLSKIE', 'MAZOWIECKIE']
# filtered_data = df_long[df_long['Województwo'].isin(selected_regions)]
# print(filtered_data)
#
# plt.figure(figsize=(10,6))
#
# color_markers= {
#     'POMORSKIE': ('blue', 'o'),
#     'OPOLSKIE': ('red', '^'),
#     'MAŁOPOLSKIE':('purple', 'D'),
#     'MAZOWIECKIE':('green', '>')
# }
# for region,(color, marker) in color_markers.items():
#     subset = filtered_data[filtered_data['Województwo'] == region]
#     plt.scatter(subset['Rok'], subset['Wartość'], label=region, color=color, marker=marker, s=100 )
#
# plt.xlabel('Rok', color='green')
# plt.ylabel('Wartość', color='red')
# plt.title('P0wierzchnia lasów wg regionu i roku')
# plt.legend('Województwo')
# plt.grid(True)
#
# plt.savefig('Tabela Lasu17.png')
# plt.show()

# zad.1
# x = [14, 18, 20.5, 30.6]
# y = [10, 12.4, 17.6, 15.6]
#
# colors = ['yellowgreen', 'brown', 'brown', 'lightcoral']
# sizes = [100, 100, 100, 100]
#
# plt.scatter(x, y, c=colors,s=sizes, marker="+", linewidths=5)
# plt.title('Wykres punktowy - 4 plusy')
# plt.xlabel('Oś pozioma', fontsize=12, color='green')
# plt.ylabel('Oś pionowa', fontsize=12, color='lightcoral')
# plt.yticks([10, 11, 12, 13, 14, 15, 16, 17],['10', '11', '12', '13', '14', '15', '16', '17'],color='lightcoral')
# plt.xticks([15, 17.5, 20, 22.5, 25, 27.5, 30],['15.0', '17.5', '20.0', '22.5', '25.0', '27.5', '30.0'],color='turquoise')
# plt.savefig('jsfbakqubf.png')
# plt.grid(True)
# plt.show()

# zad.2

# file_path = 'licea12.xlsx'
# df = pd.read_excel(file_path)
# print(df.head())
#
# labels = df['Nazwa']
# values = df['Wartość']
#
# plt.figure(figsize=(10,8))
# plt.bar(labels, values, color=plt.cm.Paired.colors, width=0.75)
#
# plt.title('Wartość dla różnych wojewódźtw')
# plt.xlabel('Województwa', color='grey')
# plt.ylabel('Wartość', color='purple')
#
# plt.xticks(rotation=90, size=9)
#
# plt.savefig('ehjfjh.png')
# plt.show()

# Zad 1.
# labels = ['B', 'C', 'D', 'E', 'F', 'A']
# sizes = [22.22, 13.33, 23.89, 17.22, 12.22, 11.11]
# colors = ['yellow', 'slateblue', 'teal', 'royalblue', 'forestgreen', 'orange']
# explode = [0, 0.1, 0, 0, 0.1, 0]
# plt.pie(sizes, labels=labels, colors=colors, explode=explode, startangle=70, autopct='%1.2f%%')
#
# plt.title('Tytuł')
# plt.savefig('hdgbsjgfb.png')
# plt.show()

# zad.2
# file_path = 'licea3.xlsx'
# df = pd.read_excel(file_path)
# print(df.head())
#
# labels = df['Nazwa']
# values = df['Wartość']
#
# plt.figure(figsize=(10,6))
# plt.bar(labels, values, color=plt.cm.Paired.colors, width=0.75)
#
# plt.title('Wartość dla różnych województw w 2018r', color='red')
# plt.xlabel('Województwa', color='blue')
# plt.ylabel('Wartość', color='green')
# plt.xticks(rotation=90)
# plt.savefig('kjdbs.png')
# plt.show()

# Zad 3.
file_path = 'produkcja3.xlsx'
df = pd.read_excel(file_path)
print(df.head())

df = df.drop(index=1)
df = df.set_index('Rok').T
df = df.reset_index().rename(columns={'index': 'Rok'})
df['Rok'] = pd.to_numeric(df['Rok'])

plt.figure(figsize=(12, 8))
plt.plot(df['Rok'], df['Wartość'], marker='o', color='red')

plt.title('Pordukcja w latach 2011-2019:')
plt.xlabel('Rok', color='skyblue')
plt.ylabel('Wartość (mln zł)', color='red')
plt.grid(True)

plt.savefig('hjdefvaejfb.pdf')

plt.show()