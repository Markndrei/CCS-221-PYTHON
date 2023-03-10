import streamlit as st
import numpy as np
import matplotlib as plt
import cv2

i = int(1)

def translation(image, x, y):
        m_translation_ = np.float32([[1, 0, x],
                                    [0, 1, y],
                                    [0, 0, 1]
                                 ])
        translated_image = cv2.warpPerspective(image, m_translation_, (cols, rows))
    
        plt.axis('off')
        plt.imshow(translated_image)
        plt.show()
        st.pyplot (translated_image)
        
        
def main ():
    st.title ("Activity 3: Image Manipulator")
    Manipulation = ["Translation", "Rotation", "Scaling", "Shear", "Reflection"]
    choice = st.sidebar.selectbox("Manipulation", Manipulation)
    
    if choice == "Translation" :
        st.subheader ("Translation")
        for i in range(1,4):
            image = cv2.imread(str(i)+".PNG")
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cols, rows, dims = image.shape
        
            translation ()

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
