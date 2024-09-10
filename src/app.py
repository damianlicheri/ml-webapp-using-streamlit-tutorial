import streamlit as st
import pandas as pd
from pickle import load

# Cargar el modelo
model = load(open("../models/random_forest_regressor_42.sav", "rb"))

# Definir la interfaz de usuario
st.markdown("<h2 style='color: blue;'>Predicción de Precio de Viviendas - Boston</h2>", unsafe_allow_html=True)
st.write("Introducir Valores (Variables Tomadas en el Censo Ciudad de Boston - CRIM, RM, DIS, LSTAT)")

# Aumentar la precisión de las entradas a 4 decimales
crim = st.text_input("CRIM", value="0.0000")
rm = st.text_input("RM", value="1.0000")
dis = st.text_input("DIS", value="1.0000")
lstat = st.text_input("LSTAT", value="1.0000")

# Botón para realizar la predicción
if st.button("Predecir"):
    # Crear un DataFrame con los valores ingresados
    data = pd.DataFrame([[float(crim), float(rm), float(dis), float(lstat)]], columns=['CRIM', 'RM', 'DIS', 'LSTAT'])

    # Realizar la predicción
    prediction = model.predict(data)[0]
    pred_class = f"{prediction:.3f} M$"

    # Mostrar el resultado
    st.write(f"La predicción del precio de la vivienda es: {pred_class}")