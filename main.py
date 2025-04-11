#%%
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from analisar_texto import analisar_texto

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

rule1 = ctrl.Rule(FP['Alta'] & I['Alta'] & FN['Baixa'] & N['Baixa'], PS['Positiva'])
rule2 = ctrl.Rule(FP['Baixa'] & I['Alta'] & FN['Alta']  & N['Baixa'], PS['Negativa'])
rule3 = ctrl.Rule(FP['Alta'] & I['Alta'] & FN['Baixa'] & N['Alta'], PS['Negativa'])
rule4 = ctrl.Rule(FP['Baixa'] & I['Alta'] & FN['Alta'] & N['Alta'], PS['Positiva'])
rule5 = ctrl.Rule(FP['Alta'] & I['Baixa'] & FN['Alta'] & N['Baixa'], PS['Neutra'])
rule6 = ctrl.Rule(FP['Baixa'] & I['Baixa'], PS['Positiva'])
rule7 = ctrl.Rule(FP['Média'] & I['Média'], PS['Positiva'])

PS_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7])
PS_simulador = ctrl.ControlSystemSimulation(PS_ctrl)

texto = "o filme foi muito bom"
fp, fn, i, n = analisar_texto(texto)

print(f"FP: {fp}, FN: {fn}, I: {i}, N: {n}")

PS_simulador.input['Positivas'] = fp
PS_simulador.input['Negativas'] = fn
PS_simulador.input['Intensificadores'] = i
PS_simulador.input['Negações'] = n

PS_simulador.compute()

try:
    valor = PS_simulador.output['Polaridade do sentimento']
    if valor < 0.33:
        print("Sentimento: Negativo \nValor: " + str(valor))
    elif valor < 0.66:
        print("Sentimento: Neutro \nValor: " + str(valor))
    else:
        print("Sentimento: Positivo \nValor: " + str(valor))
except KeyError:
    print("Erro: Nenhuma regra foi disparada ou entradas inválidas.")

# %%
