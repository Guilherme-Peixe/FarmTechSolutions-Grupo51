import math
import csv

# =========================
# CONSTANTES
# =========================
HECTARE_IN_SQM = 10000  # 1 hectare = 10.000 m²

FERTILIZER_RATE = 250   # kg por hectare - Cana
PESTICIDE_RATE = 150    # litros por hectare - Laranja

# =========================
# BASE DE DADOS
# =========================
plantations = []

# =========================
# FUNÇÕES AUXILIARES
# =========================
def get_float_input(message):
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                print("Valor deve ser maior que zero.")
            else:
                return value
        except ValueError:
            print("Erro: Digite um número válido.")

def calculate_culture_data(culture):
    if culture == "cana":
        length = get_float_input("Comprimento do talhão (m): ")
        width = get_float_input("Largura do talhão (m): ")

        # Área do retângulo em m² (metros quadrados)
        area_sqm = length * width

        # Conversão de m² para hectares
        planted_area_ha = area_sqm / HECTARE_IN_SQM

        supply = "Adubo"
        supply_amount = planted_area_ha * FERTILIZER_RATE

        return "Cana", planted_area_ha, supply, supply_amount

    elif culture == "laranja":
        radius = get_float_input("Raio do pomar (m): ")

        # Área do círculo em m² (π * r²)
        area_sqm = math.pi * radius**2

        # Conversão de m² para hectares
        planted_area_ha = area_sqm / HECTARE_IN_SQM

        supply = "Defensivo"
        supply_amount = planted_area_ha * PESTICIDE_RATE

        return "Laranja", planted_area_ha, supply, supply_amount

    else:
        return None

# =========================
# FUNÇÕES PRINCIPAIS
# =========================
def register_plantation():
    culture_input = input("Digite a cultura (Cana/Laranja): ").strip().lower()
    result = calculate_culture_data(culture_input)

    if result is None:
        print("Cultura inválida!")
        return

    culture, planted_area_ha, supply, supply_amount = result

    plantation = {
        "culture": culture,
        "planted_area_ha": planted_area_ha,
        "supply": supply,
        "supply_amount": supply_amount
    }

    plantations.append(plantation)

    print("\nPlantação cadastrada com sucesso!")
    print(f"Cultura: {culture}")
    print(f"Área plantada: {planted_area_ha:.2f} ha")
    print(f"Insumo: {supply}")
    print(f"Quantidade necessária: {supply_amount:.2f}")

def show_plantations():
    if not plantations:
        print("Nenhuma plantação cadastrada.")
        return

    print("\n=== PLANTAÇÕES CADASTRADAS ===")
    for index, plantation in enumerate(plantations, start=1):
        print(f"\nPlantação {index}")
        print(f"Cultura: {plantation['culture']}")
        print(f"Área plantada: {plantation['planted_area_ha']:.2f} ha")
        print(f"Insumo: {plantation['supply']}")
        print(f"Quantidade: {plantation['supply_amount']:.2f}")

def update_plantation():
    if not plantations:
        print("Nenhuma plantação para atualizar.")
        return

    try:
        index = int(input("Digite o número da plantação: ")) - 1

        if 0 <= index < len(plantations):
            new_area = get_float_input("Digite a nova área (ha): ")
            plantations[index]["planted_area_ha"] = new_area

            if plantations[index]["culture"] == "Cana":
                plantations[index]["supply_amount"] = new_area * FERTILIZER_RATE
            else:
                plantations[index]["supply_amount"] = new_area * PESTICIDE_RATE

            print("Plantação atualizada com sucesso.")
        else:
            print("Plantação não encontrada.")
    except ValueError:
        print("Digite um número válido.")

def delete_plantation():
    if not plantations:
        print("Nenhuma plantação para excluir.")
        return

    try:
        index = int(input("Digite o número da plantação: ")) - 1

        if 0 <= index < len(plantations):
            plantations.pop(index)
            print("Plantação removida com sucesso.")
        else:
            print("Plantação não encontrada.")
    except ValueError:
        print("Digite um número válido.")

def export_to_csv():
    if not plantations:
        print("Nenhuma plantação para exportar.")
        return

    with open("plantacoes_farmtech.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["cultura", "area_ha", "insumo", "quantidade"])

        for plantation in plantations:
            writer.writerow([
                plantation["culture"],
                plantation["planted_area_ha"],
                plantation["supply"],
                plantation["supply_amount"]
            ])

    print("Plantações exportadas com sucesso para 'plantacoes_farmtech.csv'.")

def final_report():
    if not plantations:
        print("\nNenhuma plantação registrada.")
        return

    total_area = sum(p["planted_area_ha"] for p in plantations)
    total_supply = sum(p["supply_amount"] for p in plantations)

    print("\n=== RELATÓRIO FINAL ===")
    print(f"Total de plantações: {len(plantations)}")
    print(f"Área total plantada: {total_area:.2f} ha")
    print(f"Total de insumos utilizados: {total_supply:.2f}")

# =========================
# MENU PRINCIPAL
# =========================
def main_menu():
    while True:
        print("\n=== SISTEMA FARMTECH ===")
        print("1 - Cadastrar plantação")
        print("2 - Mostrar plantações")
        print("3 - Atualizar plantação")
        print("4 - Excluir plantação")
        print("5 - Exportar plantações para CSV")
        print("0 - Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            register_plantation()
        elif option == "2":
            show_plantations()
        elif option == "3":
            update_plantation()
        elif option == "4":
            delete_plantation()
        elif option == "5":
            export_to_csv()
        elif option == "0":
            final_report()
            print("Encerrando sistema... Até logo!")
            break
        else:
            print("Opção inválida!")

# =========================
# INÍCIO DO PROGRAMA
# =========================
main_menu()