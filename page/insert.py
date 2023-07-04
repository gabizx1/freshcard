import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('CRIAR FLASHCARD')
    
    with st.form(key='insert'):
        input_name = st.text_input(label='Insira o nome:')
        input_age = st.number_input(label='Insira a matrícula:', format='%d', step=1)
        input_per = st.text_input(label='Insira a pergunta:',)
        input_res = st.text_input(label='Insira a resposta:',)
        input_ass = st.text_input(label='Insira o assunto:',)
        input_serie = st.text_input(label='Insira a serie:',)
        input_materia = st.text_input(label='Insira a matéria:',)

        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_name, input_age, input_per,input_res,input_ass,input_serie,input_materia)
            st.success('Cliente incluido com sucesso')
            