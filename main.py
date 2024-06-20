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
#
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

file_patch = 'C:/Users/Fenrir/Desktop/PyCharm/Egzamin_Zerowy/lasy12.xlsx'
df_lasy12 = pd.read_excel(file_patch)

print(df_lasy12.head())

df_melted = pd.melt(df_lasy12, id_vars=['Województwo'], var_name='Rok', value_name='Wartości')
print(df_melted.head())
df_cleaned = df_melted.dropna()


selected_wojewodztwa = ['PODLASKIE', 'OPOLSKIE', 'ŚLĄSKIE', 'MAZOWIECKIE']

filtered_data = df_cleaned[df_melted['Województwo'].isin(selected_wojewodztwa)]
print(filtered_data)

plt.figure(figsize=(12, 8))

line_styles = {'PODLASKIE': '-', 'OPOLSKIE': '--', 'ŚLĄSKIE': '-.', 'MAZOWIECKIE': ':'}
markers = {'PODLASKIE': 'o', 'OPOLSKIE': 's', 'ŚLĄSKIE': '^', 'MAZOWIECKIE': 'D'}
colors = {'PODLASKIE': 'blue', 'OPOLSKIE': 'green', 'ŚLĄSKIE': 'red', 'MAZOWIECKIE': 'purple'}

# Rysowanie linii dla każdego województwa
for wojewodztwo in selected_wojewodztwa:
    wojewodztwo_data = filtered_data[filtered_data['Województwo'] == wojewodztwo]
    plt.plot(wojewodztwo_data['Rok'], wojewodztwo_data['Wartości'],
             label=wojewodztwo, linestyle=line_styles[wojewodztwo],
             marker=markers[wojewodztwo], color=colors[wojewodztwo])

plt.title('Dane dla wybranych województw')
plt.xlabel('Rok')
plt.ylabel('Wartość')
plt.legend(title='Województwo:')
plt.savefig('Wykres 9897.png')
plt.show()