import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Configurando o WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

# URL do site
target_url = "https://www.sofascore.com/pt/time/futebol/flamengo/5981"
driver.get(target_url)

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sc-e07a153f-0 dbKvbg"))
    )
    
    elementos = driver.find_elements(By.CLASS_NAME, "sc-e07a153f-0 dbKvbg")
    
    data = []
    for elemento in elementos:
        data.append(elemento.text)
    
    # Salvando em CSV
    with open("dados_coletados.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Dados"])
        for item in data:
            writer.writerow([item])
    
    print("Coleta concluída e salva em 'dados_coletados.csv'")

except Exception as e:
    print(f"Erro durante a coleta: {e}")

finally:
    driver.quit()

# Coletando dados de jogos de 2025
df_html = pd.read_html("https://www.sofascore.com/pt/time/futebol/flamengo/5981")[0]
df_html.to_csv("flamengo_2025.csv", index=False)

# Coletando dados de jogos de 2024
url_2024 = "https://fbref.com/en/squads/639950ae/2024/Flamengo-Stats"
df_html_2 = pd.read_html(url_2024)[1]
print("\n Dados da tabela HTML:")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'left')
pd.set_option('display.expand_frame_repr', False)
print(df_html_2.head())
df_html_2.to_csv("flamengo_2024.csv", index=False)
