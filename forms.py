import streamlit as st
import json
import os

# Função para salvar os dados em um arquivo JSON com encoding correto
def save_to_json(data):
    with open("user_data.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

# Função para gerar o link de download para o arquivo JSON
def download_link(file_path, file_name):
    with open(file_path, "r", encoding="utf-8") as file:
        btn = st.download_button(
            label="Baixar arquivo JSON",
            data=file,
            file_name=file_name,
            mime="application/json"
        )
    return btn

# Função para excluir o arquivo JSON
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

# Título do aplicativo
st.title("Formulário de Informações do Usuário")

# Criação do formulário
with st.form(key="user_form"):
    nome = st.text_input("Nome")
    idade = st.number_input("Idade", min_value=1, max_value=120, step=1)
    email = st.text_input("Email")
    cidade = st.text_input("Cidade")
    profissao = st.text_input("Profissão")
    
    # Botão para submeter o formulário
    submit_button = st.form_submit_button(label="Enviar")

# Processa os dados após submissão do formulário
if submit_button:
    # Coletando os dados em um dicionário
    user_data = {
        "Nome": nome,
        "Idade": idade,
        "Email": email,
        "Cidade": cidade,
        "Profissão": profissao
    }
    
    # Exibe os dados coletados
    st.write("### Dados Coletados:")
    st.json(user_data)
    
    # Salva os dados em um arquivo JSON
    save_to_json(user_data)
    
    # Opção para download do arquivo JSON
    download_link("user_data.json", "user_data.json")
    
    # Exclui o arquivo JSON após o download
    delete_file("user_data.json")
