# %%
import streamlit as st
import pandas as pd

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
mes = st.selectbox('Mês', meses, index=None, placeholder='Selecione o mês')
df_filtrado_mes = df[df['Mês'] == mes]

col1, col2, col3, col4 = st.columns(4)
total = df_filtrado_mes['Total'].sum()
total_formatado = f'R$ {total:,.2f}'
col1.markdown(f'Total: {total_formatado.replace('.', '-').replace(',','.').replace('-', ',')}')

df_filtrado_mes