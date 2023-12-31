import streamlit as st

import controller.cliente as cliente

def editar():
    st.title('EDITAR FLASHCARD')
    
    with st.form(key='insert'):
        input_id = st.text_input(label='Insira o ID:',)
        input_per = st.text_input(label='Insira a pergunta:',)
        input_res = st.text_input(label='Insira a resposta:',)
        input_ass = st.text_input(label='Insira o assunto:',)
        input_materia = st.text_input(label='Insira a matéria:',)

        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.editar(input_id, input_per,input_res,input_ass,input_materia)
            st.success('Cliente alterado com sucesso')