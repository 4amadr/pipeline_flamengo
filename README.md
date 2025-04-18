# Análise de Desempenho do Flamengo (2024-2025)

Este projeto analisa o desempenho do Flamengo durante os ano de 2024, comparando períodos sob os técnicos Tite e Felipe Luís. Utiliza técnicas de **ETL** e **Machine Learning** para extrair insights táticos e estatísticos.

## 📌 Objetivo
- Avaliar o impacto dos técnicos no desempenho do time.
- Identificar padrões em métricas como posse de bola, xG, xGA e resultados.
- Explorar a aplicação de modelos preditivos em contextos esportivos.

## 🛠 Tecnologias Utilizadas
- **Python** (Pandas, Numpy, Scikit-Learn)
- **Jupyter Notebook** para análise interativa.
- **ETL** para limpeza e transformação de dados.

## 📊 Estrutura do Projeto

### 1. Extração e Transformação (ETL)
- **Dados utilizados**: `flamengo_2024.csv` e `flamengo_2025.csv`.
- **Tratamento**:
  - Conversão de tipos de dados (`Date`, `Attendance`).
  - Preenchimento de valores faltantes (`xG`, `xGA`, `Attendance`).
  - Remoção de colunas irrelevantes (`Referee`, `Notes`).

### 2. Análise Exploratória (EDA)
- **Comparação entre técnicos**:
  - **Tite**: 55% de posse, 1.39 xG, 68% de vitórias em casa.
  - **Felipe Luís**: 59% de posse, 1.78 xG, maior eficiência ofensiva.
- **Visualizações**: Médias de gols, formações táticas e desempenho por local.

### 3. Modelo de Machine Learning
- **Algoritmo**: `RandomForestClassifier` para prever resultados (Vitória, Derrota, Empate).
- **Resultados**: 67% de precisão (limitado pelo tamanho do dataset).

## 📥 Como Executar o Projeto
1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/analise_flamengo.git
2. **Instale as dependências**:
   pip install pandas numpy scikit-learn jupyter
3. **Execute o jupyter notebook**:
   jupyter notebook analise_flamengo.ipynb

### Destaques Profissionais:
- **Pipeline ETL completo**: Mostra habilidade em lidar com dados reais e imperfeitos.
- **Análise comparativa**: Demonstra capacidade de traduzir dados em insights acionáveis.
- **Adaptação a limitações**: Reconhecimento de desafios (como dados escassos) e propostas de melhorias.

  ### Direitos autorais:
  - **Plataforma usada para a coleta de dados**: https://fbref.com/en/
