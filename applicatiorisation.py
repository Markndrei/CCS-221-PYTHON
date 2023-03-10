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
        
def rotation(image, degree):
        angle = np.radians(10)
        m_rotation = np.float32([[np.cos(angle), -(np.sin (angle)), degree],
                             [np.sin(angle), np.cos(angle), 0],
                             [0, 0, 1]])
        rotated_image = cv2.warpPerspective(image, m_rotation, (int(cols), int(rows)))
    
        plt.axis('off')
        plt.imshow(rotated_image)
        plt.show()
        st.pyplot (rotated_image)
  
def scaling(image, scale):
        m_scaling_ = np.float32([[scale, 0, 0],
                            [0, scale, 0],
                            [0, 0, 1]
                            ])
    
        scaled_image = cv2.warpPerspective(image, m_scaling_, (cols * 2, rows * 2))
    
        plt.axis('off')
        plt.imshow(scaled_image)
        plt.show()
        st.pyplot (scaled_image)
    
    
    
def shear(image, x, y):
        m_shearing_ = np.float32([[1, x, 0],
                            [y, 1, 0],
                            [0, 0, 1]
                            ])
    
        sheared_image = cv2.warpPerspective(image, m_shearing_, (int(cols * 1.5), int(rows * 1.5)))
    
        plt.axis('off')
        plt.imshow(sheared_image)
        plt.show()
        st.pyplot (sheared_image)

    
def reflection():
        m_reflection_ = np.float32([[1, 0, 0],
                                [0, -1, rows],
                                [0, 0, 1]
                                ])
    
        reflected_image = cv2.warpPerspective(image, m_reflection_, (int(cols), int(rows)))
    
        plt.axis('off')
        plt.imshow(reflected_image)
        plt.show ()
        st.pyplot(reflected_image)

for i in range(1,4):
        image = cv2.imread(str(i)+".PNG")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cols, rows, dims = image.shape
        
        translation ()
        rotation ()
        scaling ()
        shear ()
        reflection ()
        

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
        for i in range(1,4):
            image = cv2.imread(str(i)+".PNG")
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cols, rows, dims = image.shape
        
            rotation ()
                      
    if choice == "Scaling" :
        st.subheader ("Scaling")
        for i in range(1,4):
            image = cv2.imread(str(i)+".PNG")
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cols, rows, dims = image.shape
        
            scaling ()
                      
    if choice == "Shear" :
        st.subheader ("Shear")
        for i in range(1,4):
            image = cv2.imread(str(i)+".PNG")
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cols, rows, dims = image.shape
        
            shear ()
                      
    if choice == "Reflection" :
        st.subheader ("Reflection")
        for i in range(1,4):
            image = cv2.imread(str(i)+".PNG")
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cols, rows, dims = image.shape
        
            reflection ()
         
    
if __name__ == '__main__' :
    main()
