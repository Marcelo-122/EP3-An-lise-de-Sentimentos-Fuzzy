import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# FP = Frequência de palavras-chave positivas 
# FN = Frequência de palavras-chave negativas
# I = Intensificadores
# N = Negações
# PS = Polaridade do sentimento

PS = ctrl.Consequent(np.arange(0, 1, 0.01), 'Polaridade do sentimento')

FP = ctrl.Antecedent(np.arange(0, 1, 0.01), 'Positivas')
FN = ctrl.Antecedent(np.arange(0, 1, 0.01), 'Negativas')
I = ctrl.Antecedent(np.arange(0, 1, 0.01), 'Intensificadores')
N = ctrl.Antecedent(np.arange(0, 1, 0.01), 'Negações')

FP['Baixa'] = fuzz.trimf(FP.universe, [0, 0, 0.3])
FP['Média'] = fuzz.trimf(FP.universe, [0.2, 0.4, 0.6])
FP['Alta'] = fuzz.trimf(FP.universe, [0.4, 1, 1])

FN['Baixa'] = fuzz.trimf(FN.universe, [0, 0, 0.3])
FN['Média'] = fuzz.trimf(FN.universe, [0.2, 0.4, 0.6])
FN['Alta'] = fuzz.trimf(FN.universe, [0.4, 1, 1])

I['Baixa'] = fuzz.trimf(FP.universe, [0, 0, 0.3])
I['Média'] = fuzz.trimf(FP.universe, [0.2, 0.4, 0.6])
I['Alta'] = fuzz.trimf(FP.universe, [0.4, 1, 1])

N['Baixa'] = fuzz.trimf(N.universe, [0, 0, 0.3])
N['Média'] = fuzz.trimf(N.universe, [0.2, 0.4, 0.6])
N['Alta'] = fuzz.trimf(N.universe, [0.4, 1, 1])

PS['Negativa'] = fuzz.trimf(PS.universe, [0, 0, 0.3])
PS['Neutra'] = fuzz.trimf(PS.universe, [0.2, 0.4, 0.6])
PS['Positiva'] = fuzz.trimf(PS.universe, [0.4, 1, 1])