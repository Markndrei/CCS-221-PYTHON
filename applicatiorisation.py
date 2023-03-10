import streamlit as st
import numpy as np
import matplotlib as plt
import opencv as cv2

def main ():
    st.title ("Activity 3: Image Manipulator")
    Manipulation = ["Translation", "Rotation", "Scaling", "Shear", "Reflection"]
    choice = st.sidebar.selectbox("Manipulation", Manipulation)
    
    
if __name__ == '__main__' :
    main()
