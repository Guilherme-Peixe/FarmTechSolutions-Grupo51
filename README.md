# 🌾 Sistema FarmTech - Gerenciamento de Plantações

## 📌 Sobre o Projeto

O **Sistema FarmTech** é uma aplicação desenvolvida em Python com o objetivo de gerenciar plantações agrícolas e calcular automaticamente:

* Área plantada em hectares (ha)
* Quantidade de insumos necessários

O sistema foi criado como parte de um trabalho acadêmico, integrando posteriormente os dados com a linguagem R para análise estatística.

---

## 🎯 Objetivo

Permitir que o usuário:

* Cadastre plantações de **Cana** ou **Laranja**
* Calcule automaticamente a área em hectares
* Calcule a quantidade de insumos necessária
* Atualize ou exclua plantações
* Exporte os dados para um arquivo CSV
* Visualize um relatório final

---

## 🧮 Regras de Cálculo

### 🌱 Cana

* Área calculada como retângulo: comprimento × largura (em m²)
* Conversão para hectares: m² ÷ 10.000
* Insumo: Adubo
* Taxa: 250 kg por hectare

### 🍊 Laranja

* Área calculada como círculo: π × raio² (em m²)
* Conversão para hectares: m² ÷ 10.000
* Insumo: Defensivo
* Taxa: 150 litros por hectare

---

## 🖥️ Funcionalidades do Sistema

1. Cadastrar plantação
2. Mostrar plantações cadastradas
3. Atualizar plantação
4. Excluir plantação
5. Exportar plantações para CSV
6. Gerar relatório final ao sair

---

## 📂 Estrutura do Arquivo Exportado

O sistema gera um arquivo chamado:

```
plantacoes_farmtech.csv
```

Colunas do arquivo:

* cultura
* area_ha
* insumo
* quantidade

Esse arquivo é utilizado posteriormente na aplicação em R para cálculos estatísticos.

---

## ▶️ Como Executar

1. Instale o Python (versão 3 ou superior).
2. Salve o arquivo como `farm_tech_manager.py`.
3. No terminal, execute:

```
python farm_tech_manager.py
```

4. Utilize o menu interativo para operar o sistema.

---

## 📊 Integração com R

Os dados exportados em CSV são utilizados em uma aplicação em R para:

* Cálculo de média
* Cálculo de desvio padrão
* Análise estatística básica

---

## 👥 Trabalho Acadêmico

Este projeto simula um ambiente de desenvolvimento colaborativo, utilizando:

* Python para aplicação principal
* R para análise estatística
* GitHub para versionamento

---

## ✅ Status do Projeto

✔ Sistema funcional
✔ Cálculos com unidade explícita (m² e ha)
✔ Validação de entrada
✔ Exportação para CSV
✔ Estrutura organizada em funções

---

## 📌 Observação Final

O sistema foi desenvolvido com foco em clareza, organização e boas práticas de programação, facilitando a integração com análise estatística em R e a apresentação em vídeo conforme solicitado no trabalho.
