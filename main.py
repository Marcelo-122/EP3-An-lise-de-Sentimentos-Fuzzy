#%%
from skfuzzy import control as ctrl
from analisar_texto import analisar_texto
from variaveis import FP, I, FN, N, PS
from regras import define_regras

# Define o sistema fuzzy
rules = define_regras(FP, I, FN, N, PS)
PS_ctrl = ctrl.ControlSystem(rules)

# Mensagens de teste
mensagens_teste = [
    "Esse filme foi absolutamente incrível, adorei cada segundo.",
    "O atendimento foi ótimo e a comida estava excelente!",
    "Fiquei muito feliz com o resultado, superou minhas expectativas.",
    "O serviço foi horrível e a comida estava péssima.",
    "Detestei o filme, uma perda de tempo total.",
    "Foi uma experiência extremamente deprimente e lamentável.",
    "O filme teve momentos bons e ruins, no geral foi ok.",
    "Não foi ruim, mas também não foi bom.",
    "Achei o produto comum, nada de mais.",
    "Não gostei muito do atendimento, mas o lugar era bonito."
]

# Loop de análise
for i, texto in enumerate(mensagens_teste, 1):
    PS_simulador = ctrl.ControlSystemSimulation(PS_ctrl)
    fp, fn, intensif, neg = analisar_texto(texto)

    print(f"\nMensagem {i}: \"{texto}\"")
    print(f"FP: {fp}, FN: {fn}, I: {intensif}, N: {neg}")

    try:
        PS_simulador.input['Positivas'] = fp
        PS_simulador.input['Negativas'] = fn
        PS_simulador.input['Intensificadores'] = intensif
        PS_simulador.input['Negações'] = neg
        PS_simulador.compute()
        
        valor = PS_simulador.output['Polaridade do sentimento']
        if valor < 0.33:
            print("Sentimento: Negativo \nValor:", round(valor, 3))
        elif valor < 0.66:
            print("Sentimento: Neutro \nValor:", round(valor, 3))
        else:
            print("Sentimento: Positivo \nValor:", round(valor, 3))
    except KeyError:
        print("Erro: Nenhuma regra foi disparada ou entradas inválidas.")

# %%
