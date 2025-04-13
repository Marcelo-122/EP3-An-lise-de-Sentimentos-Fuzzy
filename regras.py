from skfuzzy import control as ctrl

def define_regras(FP, I, FN, N, PS):
    rules = [
        ctrl.Rule(FP['Alta'] & I['Alta'] & FN['Baixa'] & N['Baixa'], PS['Positiva']),
        ctrl.Rule(FP['Baixa'] & I['Alta'] & FN['Alta'] & N['Baixa'], PS['Negativa']),
        ctrl.Rule(FP['Alta'] & I['Alta'] & FN['Baixa'] & N['Alta'], PS['Negativa']),
        ctrl.Rule(FP['Baixa'] & I['Alta'] & FN['Alta'] & N['Alta'], PS['Positiva']),
        ctrl.Rule(FP['Alta'] & I['Baixa'] & FN['Alta'] & N['Baixa'], PS['Neutra']),
        ctrl.Rule(FP['Alta'] & I['Baixa'] & FN['Baixa'] & N['Baixa'], PS['Positiva']),
        ctrl.Rule(FP['Baixa'] & I['Baixa'] & FN['Alta'] & N['Baixa'], PS['Negativa'])
    ]
    return rules