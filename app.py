import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')
# Graphique 1 - Ventes par produit
figure2 = px.bar(données, x='produit', y='qte',
                 title='Ventes par produit (quantités)',
                 labels={'qte': 'Quantités vendues', 'produit': 'Produit'},
                 color='produit')
figure2.write_html('ventes-par-produit.html')
print('ventes-par-produit.html généré avec succès !')

# Graphique 2 - Chiffre d'affaires par produit
données['chiffre_affaires'] = données['prix'] * données['qte']
figure3 = px.bar(données, x='produit', y='chiffre_affaires',
                 title="Chiffre d'affaires par produit",
                 labels={'chiffre_affaires': 'CA (€)', 'produit': 'Produit'},
                 color='produit')
figure3.write_html('ca-par-produit.html')
print("ca-par-produit.html généré avec succès !")
