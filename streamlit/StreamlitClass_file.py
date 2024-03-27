import streamlit as st


class StreamlitClass:
    def __init__(self):
        pass

    def selectbox(self, label, options):
        return st.selectbox(label, options)

    def number_input(self, label):
        return st.number_input(label)

    def checkbox(self, label):
        return st.checkbox(label)

    def convert_to_int(self, boolean_value):
        return int(boolean_value)
