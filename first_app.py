import streamlit as st
import numpy as np
import pandas as pd

st.title(':house: CHÁ DE CASA NOVA DO MARCELO :bear:')
st.header('Bem Vindos! :sunglasses:')

st.write("Vou fazer meu chá de casa nova e conto com sua presença! :smile:")

df = pd.DataFrame({
  'Itens': ['Bacia M','Bacia P','Bacia para salada','Balde','Cinzeiro','Copos'
,'Escorredor de macarrão','Escorredor de pratos','Fronha travesseiro','Kit para guardar mantimentos'
,'Kit para guardar temperos','Lençol Casal','Lixo para pia','Pano de chão','Pano de prato'
,'Peneira P,M e G','Porta detergente e sabão','Porta escova de dente e creme dental'
,'Porta guardanapo','Porta papel higiênico','Potes de Plástico G','Potes de Plástico M'
,'Potes de Plástico P','Rodinho de pia','Toalha de banho','Toalha de rosto'],
}) 

option = st.selectbox(
    'Abaixo está minha lista de presentes, clique na seta para visualizar',
     df)

expander = st.beta_expander("Data e Local")
expander.write('Dia 01/05 as 15:00, na Rua Dom Lara, 524 - São Vicente. Até lá! :v:')

st.balloons()