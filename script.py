import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger le fichier CSV dans un DataFrame
file_path = 'dataset.csv'  # Assurez-vous de mettre le bon nom de fichier ici
df = pd.read_csv(file_path, delimiter=';', decimal=',', encoding='latin-1')

# KPIs
total_users = df['Utilisateurs'].sum()
average_sessions_per_user = df['Sessions'].mean()
total_revenue = df['Chiffre d\'affaires'].sum()
conversion_rate = (df['Transactions'].sum() / total_users) * 100  # en pourcentage
average_transaction_value = df['Chiffre d\'affaires'].sum() / df['Transactions'].sum()

# Afficher les KPIs
print(f"Total Users: {total_users}")
print(f"Average Sessions per User: {average_sessions_per_user}")
print(f"Total Revenue: {total_revenue}")
print(f"Conversion Rate: {conversion_rate:.2f}%")
print(f"Average Transaction Value: {average_transaction_value:.2f}")

# Générer des graphiques
# Graphique à barres pour les utilisateurs par continent
users_by_continent = df.groupby('Continent')['Utilisateurs'].sum()
users_by_continent.plot(kind='bar', title='Utilisateurs par Continent')
plt.xlabel('Continent')
plt.ylabel('Utilisateurs')
plt.savefig('utilisateurs_par_continent.png')
plt.close()

# Graphique en nuage de points pour les pages vues en fonction du chiffre d'affaires
plt.scatter(df['Pages vues'], df['Chiffre d\'affaires'])
plt.title('Pages vues vs Chiffre d\'affaires')
plt.xlabel('Pages vues')
plt.ylabel('Chiffre d\'affaires')
plt.savefig('pages_vues_vs_CA.png')
plt.close()
