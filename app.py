import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="TMA English Tutor", page_icon="✈️")

st.title("✈️ TMA English Tutor")
st.subheader("Tu instructor de bolsillo para Control de Calidad")

# Aquí conectarás tu API Key de forma segura después
api_key = st.sidebar.text_input("Pega tu API Key de Google aquí:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    # Menú de opciones
    opcion = st.sidebar.selectbox("¿Qué quieres practicar?", 
                                 ["Palabra del Día (Motores)", 
                                  "Traductor Técnico de Manuales", 
                                  "Quiz de Inspección (QC)"])

    if opcion == "Palabra del Día (Motores)":
        if st.button("Generar palabra"):
            prompt = "Dame una palabra técnica en inglés sobre motores de aviones (Cessna/Piper). Incluye: Palabra, Pronunciación figurada, Significado en español y un ejemplo de uso en un manual."
            response = model.generate_content(prompt)
            st.write(response.text)

    elif opcion == "Traductor Técnico de Manuales":
        texto = st.text_area("Pega aquí la frase del manual en inglés:")
        if st.button("Traducir como un experto"):
            prompt = f"Traduce esta frase técnica de mantenimiento al español de forma profesional para un mecánico: {texto}"
            response = model.generate_content(prompt)
            st.success(response.text)

    elif opcion == "Quiz de Inspección (QC)":
        if st.button("Empezar Quiz"):
            prompt = "Hazme una pregunta técnica corta de opción múltiple sobre una inspección de 100 horas en inglés, con traducciones de las opciones."
            response = model.generate_content(prompt)
            st.write(response.text)
else:
    st.warning("Por favor, introduce tu API Key en la barra lateral para comenzar a estudiar.")

st.info("Consejo: Usa esta app durante tu almuerzo o en el transporte para dominar el inglés de los manuales.")
