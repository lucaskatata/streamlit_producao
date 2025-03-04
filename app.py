# %%
import streamlit as st
import pandas as pd

st.set_page_config(layout='wide', page_title='Produção 2024', page_icon='📃')
st.title('Controle da Produção 2024')

# %%
dataset = 'datasets/CONTROLE DA PRODUCAO E M.O. - 2024.csv'

df = pd.read_csv(dataset)

st.dataframe(df)