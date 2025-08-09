import streamlit as st
import pandas as pd
import plotly.express as px

## Configuração da página
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)

df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

## Barra lateral
st.sidebar.header("Filtros")

## Filtro anos
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis)

## Filtro senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionados = st.sidebar.multiselect("Senioridade", senioridades_disponiveis, default=senioridades_disponiveis)

## Filtro contratos
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis)

## Filtro tamanho
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)