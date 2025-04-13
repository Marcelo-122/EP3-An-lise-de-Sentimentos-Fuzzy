from skfuzzy import control as ctrl

def define_regras(FP, I, FN, N, PS):
    rules = [

        # Positivo reforçado
        ctrl.Rule(FP['Alta'] & FN['Baixa'] & I['Alta'] & N['Baixa'], PS['Positiva']),

        # Positivo simples
        ctrl.Rule(FP['Alta'] & FN['Baixa'] & I['Baixa'] & N['Baixa'], PS['Positiva']),

        # Conflito equilibrado
        ctrl.Rule(FP['Alta'] & FN['Alta'] & I['Baixa'] & N['Baixa'], PS['Neutra']),

        # Positivo negado
        ctrl.Rule(FP['Alta'] & FN['Baixa'] & I['Alta'] & N['Alta'], PS['Negativa']),

        # Negativo reforçado
        ctrl.Rule(FP['Baixa'] & FN['Alta'] & I['Alta'] & N['Baixa'], PS['Negativa']),

        # Negativo negado
        ctrl.Rule(FP['Baixa'] & FN['Alta'] & I['Alta'] & N['Alta'], PS['Positiva']),

        # Negativo simples
        ctrl.Rule(FP['Baixa'] & FN['Alta'] & I['Baixa'] & N['Baixa'], PS['Negativa']),

        # Sem opinião
        ctrl.Rule(FP['Baixa'] & FN['Baixa'] & I['Baixa'] & N['Baixa'], PS['Neutra']),

        # Misto moderado
        ctrl.Rule(FP['Média'] & FN['Média'] & I['Média'] & N['Média'], PS['Neutra']),

        # Positivo mais forte
        ctrl.Rule(FP['Alta'] & FN['Média'] & I['Alta'] & N['Baixa'], PS['Positiva']),

        # Tendência negativa
        ctrl.Rule(FP['Média'] & FN['Alta'] & I['Baixa'] & N['Baixa'], PS['Negativa']),

        # Positivo com dúvida
        ctrl.Rule(FP['Média'] & FN['Baixa'] & I['Alta'] & N['Alta'], PS['Neutra']),

        # Positivo médio
        ctrl.Rule(FP['Alta'] & FN['Baixa'] & I['Média'] & N['Baixa'], PS['Positiva']),

        # Conflito médio
        ctrl.Rule(FP['Média'] & FN['Baixa'] & I['Média'] & N['Média'], PS['Neutra']),

        # Negativo reforçado médio
        ctrl.Rule(FP['Baixa'] & FN['Alta'] & I['Média'] & N['Baixa'], PS['Negativa']),

        # Sem opinião com negação
        ctrl.Rule(FP['Baixa'] & FN['Baixa'] & I['Baixa'] & N['Alta'], PS['Neutra'])

    ]

    return rules