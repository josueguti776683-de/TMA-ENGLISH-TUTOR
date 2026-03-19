import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="TMA Elite Trainer", page_icon="✈️", layout="wide")

# Título y Sidebar
st.title("✈️ TMA Elite Trainer: Road to QC")
st.sidebar.header("Panel de Control")
api_key = st.sidebar.text_input("Pega tu API Key de Google:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    # Menú Principal de Opciones
    opcion = st.sidebar.selectbox(
        "¿Qué vamos a entrenar hoy?",
        ["Inicio", "Vocabulario (Grupos de 5-10)", "Diccionario Técnico", "Estudio de Manuales", "Práctica de Escritura"]
    )

    if opcion == "Inicio":
        st.write("### Bienvenido, futuro Inspector de QC.")
        st.info("Selecciona un módulo en el menú de la izquierda para empezar a volar.")

    elif opcion == "Vocabulario (Grupos de 5-10)":
        st.subheader("📦 Entrenamiento de Memoria")
        num = st.slider("¿Cuántas palabras quieres aprender?", 5, 10, 5)
        if st.button("Generar Sesión"):
            prompt = f"Genera una lista de {num} palabras técnicas de mantenimiento aeronáutico. Para cada una incluye: Palabra, Pronunciación fonética, Significado sencillo y un ejemplo corto tipo manual AMM."
            response = model.generate_content(prompt)
            st.write(response.text)

    elif opcion == "Diccionario Técnico":
        st.subheader("📖 Diccionario Aero-Técnico")
        busqueda = st.text_input("Escribe la palabra o componente:")
        if busqueda:
            prompt = f"Actúa como un manual técnico. Explica qué es '{busqueda}' en un avión, su función y dame 2 ejemplos de cómo aparece en un manual de mantenimiento (AMM)."
            response = model.generate_content(prompt)
            st.write(response.text)

    elif opcion == "Estudio de Manuales":
        st.subheader("📚 Asistente de Teoría")
        texto_manual = st.text_area("Pega aquí el párrafo del manual de tu escuela que quieres estudiar:")
        if st.button("Analizar y Traducir"):
            prompt = f"Analiza este texto técnico: '{texto_manual}'. Primero tradúcelo al español técnico, luego explica los 3 conceptos más importantes para un examen de TMA."
            response = model.generate_content(prompt)
            st.write(response.text)

    elif opcion == "Práctica de Escritura":
        st.subheader("✍️ Training de Escritura Técnica")
        if st.button("Dame una palabra para escribir"):
            prompt = "Dame una palabra técnica aeronáutica difícil. No me des el significado aún."
            response = model.generate_content(prompt)
            st.session_state['word_to_write'] = response.text
        
        if 'word_to_write' in st.session_state:
            st.write(f"Escribe la palabra: **{st.session_state['word_to_write']}**")
            intento = st.text_input("Tu respuesta:")
            if intento.lower() == st.session_state['word_to_write'].lower().strip():
                st.success("¡Correcto! Así se escribe en un reporte de QC.")
            elif intento:
                st.error("Sigue practicando, la precisión es clave en aviación.")

else:
    st.warning("Por favor, ingresa tu API Key en la barra lateral para activar los sistemas.")
