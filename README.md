# 🔐 Générateur de Mots de Passe Sécurisés

## Description

Ce projet est un générateur de mots de passe sécurisé développé en Python dans le cadre du module 1PRJ1.
Il permet de générer, analyser et sauvegarder des mots de passe personnalisés.

## Fonctionnalités

- Génération de mots de passe configurables
- Analyse de la force (Faible à Très Fort)
- Historique des 10 derniers mots de passe
- Interface console simple

## Installation

```bash
git clone <url_du_repo>
cd password_generator
python main.py
```

## Exemple d’utilisation

Générer un mot de passe de 12 caractères avec majuscules et chiffres → Force : Fort → Sauvegarde automatique.

## Architecture

- `generer_mdp()` : génération
- `analyser_force()` : sécurité
- `sauvegarder()` : gestion fichier
- `menu()` : interface utilisateur

## Technologies

- Python 3.8+
- Modules : random, os

## Auteurs

- Mathis : Développement et documentation
