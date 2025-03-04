# %%
import streamlit as st
import pandas as pd

# %%

st.set_page_config(layout='wide', page_title='Produção 2024', page_icon='📃')

st.title('Controle da Produção 2024')

@st.cache_data
def load_data():
    dataset = 'datasets/CONTROLE DA PRODUCAO E M.O. - 2024.csv'
    df = pd.read_csv(dataset)
    df = df.applymap(lambda x: x.title() if isinstance(x,str) else x)
    columns = df.columns
    colunas_formatadas = [coluna.title() for coluna in columns]
    df.columns = colunas_formatadas
    return df
df = load_data()
st.session_state['df'] = df

meses = df['Mês'].unique()
mes = st.sidebar.selectbox('Mês', meses, index=None, placeholder='Selecione o mês')
df_filtrado_mes = df[df['Mês'] == mes]


total_mes = df_filtrado_mes['Total'].sum()
total_mes_formatado = f'R$ {total_mes:,.2f}'
st.sidebar.markdown(f'Total: {total_mes_formatado.replace('.', '-').replace(',','.').replace('-', ',')}')

total_interno = df_filtrado_mes['Producao Interna'].sum()
total_interno_formatado = f'R$ {total_interno:,.2f}'
st.sidebar.markdown(f'Total Produção Interna: {total_interno_formatado.replace('.', '-').replace(',','.').replace('-', ',')}')

total_mo = df_filtrado_mes['Producao M.O.'].sum()
total_mo_formatado = f'R$ {total_mo:,.2f}'
st.sidebar.markdown(f'Total Produção Mão de Obra: {total_mo_formatado.replace('.', '-').replace(',','.').replace('-', ',')}')

selected = st.checkbox('Ver tabela')
if selected:
    df_filtrado_mes
