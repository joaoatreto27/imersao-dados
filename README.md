# Dashboard de Salários na Área de Dados

Este projeto é um dashboard interativo desenvolvido com [Streamlit](https://streamlit.io/) para análise de salários na área de dados. Ele utiliza dados públicos e permite ao usuário explorar informações salariais por diferentes filtros e visualizar métricas e gráficos relevantes.

## Acesso Online

O dashboard está disponível publicamente em:  
[https://joaoatreto27-imersao-dados.streamlit.app/](https://joaoatreto27-emrsao-dados.streamlit.app/)

## Funcionalidades

- **Filtros interativos:** Ano, senioridade, tipo de contrato e tamanho da empresa.
- **Métricas principais:** Salário médio, salário máximo, total de registros e cargo mais frequente.
- **Gráficos dinâmicos:**
  - Top 10 cargos por salário médio
  - Distribuição dos salários anuais
  - Proporção dos tipos de trabalho (remoto/presencial)
  - Salário médio de Cientista de Dados por país
- **Tabela detalhada:** Exibe os dados filtrados em formato tabular.

## Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Plotly

## Como Executar Localmente

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o dashboard:
   ```bash
   streamlit run app.py
   ```
3. O dashboard estará disponível em seu navegador padrão.

## Fonte dos Dados

Os dados utilizados são públicos e estão disponíveis [neste repositório](https://github.com/vqrca/dashboard_salarios_dados).

## Estrutura do Projeto

- `app.py`: Código principal do dashboard.
- `requirements.txt`: Lista de dependências do projeto.

## Personalização

Você pode adaptar os filtros, gráficos e métricas conforme sua necessidade, alterando o arquivo `app.py`.

## Licença

Este projeto é apenas para fins educacionais e de demonstração.

---

Sinta-se à vontade para contribuir ou sugerir melhorias!
