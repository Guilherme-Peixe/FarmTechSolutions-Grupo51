# Instalação automática de dependências caso não existam
packages <- c("httr", "jsonlite", "ggplot2", "dplyr")
new_packages <- packages[!(packages %in% installed.packages()[,"Package"])]
if(length(new_packages)) install.packages(new_packages)

library(httr)
library(jsonlite)
library(ggplot2)
library(dplyr)

# --- PROCESSAMENTO DE DADOS E ESTATÍSTICA ---
if (file.exists("plantacoes_farmtech.csv")) {
  dados <- read.csv("plantacoes_farmtech.csv")
  
  # Forçar os nomes das colunas para garantir que o script funcione
  # Isso resolve o erro "Column not found"
  colnames(dados) <- c("culture", "area_ha", "supply", "qty")
  
  cat("\n--- RELATÓRIO ESTATÍSTICO AVANÇADO ---\n")
  
  # Resumo por Cultura
  resumo <- dados %>%
    group_by(culture) %>%
    summarise(
      Qtd_Talhoes = n(),
      Area_Media = mean(area_ha, na.rm = TRUE),
      Desvio_Padrao = sd(area_ha, na.rm = TRUE),
      Total_Insumo = sum(qty, na.rm = TRUE)
    )
  print(resumo)
  
  # Gráfico atualizado com nomes corrigidos
  p <- ggplot(dados, aes(x=culture, y=area_ha, fill=culture)) +
    geom_bar(stat="summary", fun="mean") +
    theme_minimal() +
    labs(title="Média de Área por Cultura", x="Cultura", y="Área Média (ha)")
  
  ggsave("grafico_farmtech.pdf", plot = p)
  
} else {
  stop("Erro: O arquivo 'plantacoes_farmtech.csv' não foi encontrado. Execute o Python primeiro.")
}

# 3. CONEXÃO COM API METEOROLÓGICA (IR ALÉM)
get_weather_advanced <- function(city) {
  tryCatch({
    city_enc <- URLencode(city)
    url <- paste0("https://api.hgbrasil.com/weather?key=76629731&city_name=", city_enc)
    
    res <- GET(url)
    data <- fromJSON(content(res, "text", encoding="UTF-8"))
    
    cat("\n--- MONITORIZAÇÃO CLIMÁTICA TEMPO REAL ---\n")
    cat("Localidade:", data$results$city, "\n")
    cat("Condição:", data$results$description, "\n")
    cat("Temperatura:", data$results$temp, "°C\n")
    cat("Humidade:", data$results$humidity, "%\n")
    cat("Velocidade do Vento:", data$results$wind_speedy, "\n")
    cat("------------------------------------------\n")
    
  }, error = function(e) {
    cat("Aviso: Não foi possível obter dados da API (verifique a ligação à internet).\n")
  })
}

get_weather_advanced("Ribeirao Preto")