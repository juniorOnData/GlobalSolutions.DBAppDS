def validacao_categorias(total, categorias):
    """Validar se a soma das categorias é igual ao total de pessoas afetadas"""
    return sum(categorias) == total

def obtendo_numero_positivo(prompt):
    """Obter um número inteiro positivo da entrada do usuário com validação"""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Por favor, insira um número inteiro não negativo.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

def hub_dados_desastres():
    tipos_desastres = []
    paises = []
    cidades = []
    bairros = []
    ruas = []
    total_afetados = []
    criancas = []
    adultos = []
    idosos = []
    mobilidade_reduzida = []
    feridos = []

    num_desastres = obtendo_numero_positivo("Digite a quantidade de desastres registrados: ")

    for i in range(num_desastres):
        print(f"\nColetando dados para o desastre {i + 1}:")

        tipo = input("Tipo de desastre (ex: Incêndio, enchente, etc.): ").strip()
        pais = input("País: ").strip()
        cidade = input("Cidade: ").strip()
        bairro = input("Bairro: ").strip()
        rua = input("Rua: ").strip()

        total = obtendo_numero_positivo("Quantidade total de pessoas afetadas: ")

        while True:
            criancas_qtd = obtendo_numero_positivo("Quantidade de crianças: ")
            adultos_qtd = obtendo_numero_positivo("Quantidade de adultos: ")
            idosos_qtd = obtendo_numero_positivo("Quantidade de idosos: ")
            mobilidade_qtd = obtendo_numero_positivo("Quantidade de pessoas com mobilidade reduzida: ")
            feridos_qtd = obtendo_numero_positivo("Quantidade de feridos: ")

            categorias = [criancas_qtd, adultos_qtd, idosos_qtd, mobilidade_qtd, feridos_qtd]

            if validacao_categorias(total, categorias):
                tipos_desastres.append(tipo)
                paises.append(pais)
                cidades.append(cidade)
                bairros.append(bairro)
                ruas.append(rua)
                total_afetados.append(total)
                criancas.append(criancas_qtd)
                adultos.append(adultos_qtd)
                idosos.append(idosos_qtd)
                mobilidade_reduzida.append(mobilidade_qtd)
                feridos.append(feridos_qtd)
                break
            else:
                print("Erro: A soma das categorias não é igual ao total de pessoas afetadas.")
                print("Por favor, insira os dados novamente.")

    return {
        'tipos_desastres': tipos_desastres,
        'paises': paises,
        'cidades': cidades,
        'bairros': bairros,
        'ruas': ruas,
        'total_afetados': total_afetados,
        'criancas': criancas,
        'adultos': adultos,
        'idosos': idosos,
        'mobilidade_reduzida': mobilidade_reduzida,
        'feridos': feridos
    }

def main():
    print("Sistema de Registro de Desastres")
    print("-" * 30)

    data = hub_dados_desastres()

    print("\nDados coletados:")
    for i in range(len(data['tipos_desastres'])):
        print(f"\nDesastre {i + 1}:")
        print(f"Tipo: {data['tipos_desastres'][i]}")
        print(f"Local: {data['ruas'][i]}, {data['bairros'][i]}, {data['cidades'][i]}, {data['paises'][i]}")
        print(f"Total de afetados: {data['total_afetados'][i]}")
        print(f"Crianças: {data['criancas'][i]}")
        print(f"Adultos: {data['adultos'][i]}")
        print(f"Idosos: {data['idosos'][i]}")
        print(f"Pessoas com mobilidade reduzida: {data['mobilidade_reduzida'][i]}")
        print(f"Feridos: {data['feridos'][i]}")

if __name__ == "__main__":
    main()


total_desastres = len(tipos_desastres)
total_geral_afetados = sum(total_afetados)
soma_criancas = sum(criancas)
soma_adultos = sum(adultos)
soma_idosos = sum(idosos)
soma_mob = sum(mobilidade_reduzida)
soma_feridos = sum(feridos)


categorias = ["Crianças", "Adultos", "Idosos", "Mobilidade Reduzida", "Feridos"]
valores = [soma_criancas, soma_adultos, soma_idosos, soma_mob, soma_feridos]
indice_mais_afetado = valores.index(max(valores))
categoria_mais_afetada = categorias[indice_mais_afetado]

maior_afetados = max(total_afetados)
indice_maior = total_afetados.index(maior_afetados)

print("\n===== RELATÓRIO FINAL =====")
print(f"Total de desastres registrados: {total_desastres}\n")
print("Resumo de pessoas afetadas por categoria:")
print(f"Crianças: {soma_criancas} | Adultos: {soma_adultos} | Idosos: {soma_idosos} | Mobilidade reduzida: {soma_mob} | Feridos: {soma_feridos}")
print(f"\nCategoria mais afetada: {categoria_mais_afetada}")
print(f"Total geral de pessoas afetadas: {total_geral_afetados}")
print("\nDesastre com maior número de afetados:")
print(f"Tipo: {tipos_desastres[indice_maior]}")
print(f"Local: {ruas[indice_maior]}, {bairros[indice_maior]}, {cidades[indice_maior]}, {paises[indice_maior]}")
print("============================")
