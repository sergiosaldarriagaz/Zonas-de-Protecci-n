import streamlit as st
from PIL import Image
import os

# --- Configuración de la página ---
st.set_page_config(page_title="Quiz de Protecciones", layout="wide")

st.title("Análisis de Zonas de Protección")

# --- Creación del diseño en dos columnas ---
col1, col2 = st.columns([1, 1]) # Dos columnas de igual tamaño

# --- Columna Izquierda: Imagen ---
with col1:
    st.subheader("Diagrama Unifilar")
    image_path = "Unifilar2.png"
    
    # Verificamos que la imagen exista en la carpeta
    if os.path.exists(image_path):
        img = Image.open(image_path)
        # use_container_width ajusta la imagen al tamaño de la columna
        st.image(img, caption="Diagrama a analizar", use_container_width=True)
    else:
        st.warning(f"⚠️ No se encontró la imagen '{image_path}'. Por favor, asegúrate de subirla a la misma carpeta o repositorio que tu archivo app.py.")

# --- Columna Derecha: Pregunta y Lógica ---
with col2:
    st.markdown("### Pregunta de Análisis:")
    st.write("Observando el diagrama unifilar, **¿Cuántas zonas de protección principales hay en esta red?**")
    
    # Opciones (st.radio es el equivalente a RadioButtons)
    opcion_elegida = st.radio(
        "Selecciona tu respuesta:",
        ('4 zonas', '5 zonas', '7 zonas', '9 zonas')
    )
    
    # st.button crea el botón. type="primary" lo pone de color destacado.
    if st.button("Verificar Respuesta", type="primary"):
        
        # Lógica de validación
        if opcion_elegida == '7 zonas':
            st.success("✅ **¡Correcto!**")
            st.markdown("""
            **Las 7 zonas son:**
            1. Zona del Generador (GS).
            2. Zona de la Barra Superior de Alta Tensión.
            3. Zona del Transformador.
            4. Zona de la Barra Inferior de Baja Tensión.
            5. Zona del Alimentador (Feeder) 1.
            6. Zona del Alimentador (Feeder) 2.
            7. Zona del Alimentador (Feeder) 3.
            
            *Recuerda que las zonas deben traslaparse en los interruptores para que no queden puntos ciegos (zonas muertas).*
            """)
        else:
            st.error("❌ **Incorrecto.**")
            st.info("💡 **Pista:** Recuerda que cada equipo principal (Generador, Transformador), cada Barra de interconexión y cada línea de salida (Feeder) requiere su propia zona de protección. Cuenta cada uno de ellos de arriba hacia abajo.")
