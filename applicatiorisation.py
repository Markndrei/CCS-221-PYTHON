import streamlit as st
import numpy as np
import matplotlib as plt
import cv2

def main ():
    st.title ("Activity 3: Image Manipulator")
    Manipulation = ["Translation", "Rotation", "Scaling", "Shear", "Reflection"]
    choice = st.sidebar.selectbox("Manipulation", Manipulation)
    
    if choice == "Translation" :
        m_translation_ = np.float32([[1, 0, 100],
                                    [0, 1, 50],
                                    [0, 0, 1]
                                 ])
    
        fig, translated_image = cv2.warpPerspective(image, m_translation_, (cols, rows))
    
        plt.axis('off')
        plt.imshow(translated_image)
        plt.show()
        st.pyplot (fig)
    
    
if __name__ == '__main__' :
    main()
