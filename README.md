# ⚠️ English Version Below

# Description du Projet

## Contexte
La gestion des stocks, comprenant les matières premières, les produits semi-finis et les produits finis, constitue un défi majeur pour les entreprises. Contrairement aux approches classiques basées sur des demandes déterministes, nous abordons le problème de manière stochastique en tenant compte de la variabilité de la demande grâce à des méthodes de prévision avancées.

## Problématique
Notre tâche consiste à modéliser le problème sous forme d'un programme linéaire en nombres entiers et à le résoudre avec le solveur Cplex d'IBM. Nous devons également développer une méthode d'optimisation approximative (par exemple, basée sur des scénarios) en utilisant C/Python. Enfin, une analyse des résultats numériques sera réalisée pour évaluer l'efficacité des méthodes développées.

## Objectif du Projet
1. **Recherche Opérationnelle :** Modéliser mathématiquement le problème d'optimisation visant à minimiser les coûts de production et de stockage. Linéariser les modèles pour les rendre solubles via le programme à utiliser, en s'appuyant sur des rapports tels que celui de Céline Gicquel et Jianqiang Cheng.
   
2. **Compréhension de Cplex :** Acquérir une compréhension approfondie de Cplex pour caractériser les modèles, même si la librairie docplex est utilisée dans notre cas. Cela implique la définition de contraintes, la modification des paramètres du solveur, la définition de l'objectif et la résolution du problème.
   
3. **Développement en Python :** Utiliser Python, en particulier la librairie docplex, pour coder les modèles caractérisés. Comprendre les spécificités de l'utilisation du solveur avec Python, comme l'ajout de contraintes et la résolution du modèle.

4. **Comparaison et Analyse :** Confronter et analyser les résultats numériques obtenus à partir des différentes méthodes modélisées avec le solveur. Identifier les points forts, les points faibles et les incohérences entre les modèles.



# Project Description

## Context
Managing stocks, including raw materials, semi-finished products, and finished goods, is a significant challenge for businesses. Unlike traditional approaches based on deterministic demand, we address the problem stochastically, considering demand variability through advanced forecasting methods.

## Problem Statement
Our task involves modeling the problem as an integer linear program and solving it using IBM's Cplex solver. We are also required to develop an approximate optimization method (e.g., scenario-based) using C/Python. Finally, a numerical results analysis will be conducted to assess the effectiveness of the developed methods.

## Project Objectives
1. **Operational Research:** Mathematically model the optimization problem to minimize production and storage costs. Linearize models to make them solvable using the chosen program, drawing insights from reports such as that of Céline Gicquel and Jianqiang Cheng.
   
2. **Understanding Cplex:** Gain a thorough understanding of Cplex to characterize the models, even though the docplex library is used in our case. This involves defining constraints, modifying solver parameters, setting objectives, and solving the problem.
   
3. **Python Development:** Utilize Python, specifically the docplex library, to code the characterized models. Understand the intricacies of using the solver with Python, such as adding constraints and solving the model.

4. **Comparison and Analysis:** Compare and analyze numerical results obtained from different methods modeled with the solver. Identify strengths, weaknesses, and inconsistencies among the models.

