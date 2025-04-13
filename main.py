#%%
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from analisar_texto import analisar_texto
from variaveis import FP, I, FN, N, PS
from regras import define_regras

rules = define_regras(FP, I, FN, N, PS)
PS_ctrl = ctrl.ControlSystem(rules)
PS_simulador = ctrl.ControlSystemSimulation(PS_ctrl)

texto = "o filme foi ruim"
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
