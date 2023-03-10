import streamlit as st
import numpy as np
import matplotlib as plt
import cv2

def main ():
    st.title ("Activity 3: Image Manipulator")
    Manipulation = ["Translation", "Rotation", "Scaling", "Shear", "Reflection"]
    choice = st.sidebar.selectbox("Manipulation", Manipulation)
    
    if choice == "Translation" :
        st.subheader ("Translation")

    if choice == "Rotation" :
        st.subheader ("Rotation")
                      
    if choice == "Scaling" :
        st.subheader ("Scaling")
                      
    if choice == "Shear" :
        st.subheader ("Shear")
                      
    if choice == "Reflection" :
        st.subheader ("Reflection")
         
    
if __name__ == '__main__' :
    main()
