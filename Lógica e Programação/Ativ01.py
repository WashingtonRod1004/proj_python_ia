def validar_dia_semana(dia_semana):
    dias_validos = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    return dia_semana.lower() in dias_validos

def pode_acessar(cargo, dia_semana):
    dias_uteis = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
    
    
    regras_acesso = {
        "gerente": lambda _: True, 
        "analista": lambda dia: dia in dias_uteis, 
        "estagiário": lambda dia: dia in dias_uteis  # Acesso em dias úteis
    }
    
   
    regra = regras_acesso.get(cargo.lower())
    
    if regra and validar_dia_semana(dia_semana):
        return regra(dia_semana.lower())
    else:
        return False


cargo = input("Digite o cargo do funcionário: ")
dia_semana = input("Digite o dia da semana: ")

if not validar_dia_semana(dia_semana):
    print("Dia da semana inválido. Por favor, insira um dia correto.")
elif pode_acessar(cargo, dia_semana):
    print("Acesso Permitido.")
else:
    print("Acesso Negado.")
