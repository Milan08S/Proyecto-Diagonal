from unicodedata import category
import streamlit as st
from model.Contacto import Contacto
from model.Criterio import Agenda

""" Este archivo contine las funcionalidades de la vista relacionado con la evaluacion de los anteproyectos"""


def agregar_contacto(st, controller):
    Contactos = Contacto
    Agendas = Agenda
    st.title("Agregar Contactos")
    nombre = st.text_input("Nombre: ")
    categoria = st.selectbox("Categoria:", ("Industria petrolera", "Asociacion Ganadera", "Industria Apicultora"))
    numero = st.number_input("Numero de contacto: ", 0, 4000000000, 0)

    if st.button("Agregar contacto"):
        Agendas.agregar_contactos(nombre, categoria, numero)
        st.caption("Contacto agregado")


def listar_contactos():
    st.title("Contactos: ")
    categoria = st.selectbox("Categoria: ", ("Industria petrolera", "Asociacion Ganadera", "Industria Apicultora"))
    if categoria == "Industria petrolera":
        st.subheader("Informacion: ")
        st.text('Nombre: Ecopetrol\nNumero: 315228115\n\nNombre: Alianza petrolera\nNumero: 3266151311')
    elif categoria == "Asociacion Ganadera":
        st.subheader("Informacion: ")
        st.text('Nombre: Juan ganadero\nNumero: 3185541554')
    elif categoria == "Industria Apicultora":
        st.subheader("Informacion: ")
        st.text('Nombre: Abejita Crv\nNumero: 323625615')

def preguntas_proyecto():
    nombre_pro = st.text_input("Nombre del proyeto: ")
    nombre_autor = st.text_input("Nombre del Autor: ")
    cat_pro = st.text_input("Tipo de proyecto: ")
    ind_pro = st.text_input("A que industria apunta tu proyecto?: ")
    vent_pro = st.text_input("Que tipo de ventajas competitivas ofrece tu proyecto?: ")
    impac_pro = st.text_input("Que impacto tiene tu proyecto al medio ambiente?: ")

    if st.button("Enviar"):
        st.caption("Tu proyecto ha sido enviado!, lo revisaremos lo mas pronto posible")

