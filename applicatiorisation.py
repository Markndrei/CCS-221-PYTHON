
import numpy as np
import cv2
import matplotlib.pyplot as plt
import streamlit as st

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
    i = bytes_data
    i = int(1)
    x = []

def translation():
        m_translation_ = np.float32([[1, 0, 100],
                                    [0, 1, 50],
                                    [0, 0, 1]
                                 ])
    
        fig,translated_image = cv2.warpPerspective(image, m_translation_, (cols, rows))
    
        plt.axis('off')
        plt.imshow(translated_image)
        st.pyplot(fig)
        
def rotation():
        angle = np.radians(10)
        m_rotation = np.float32([[np.cos(angle), -(np.sin (angle)), 0],
                             [np.sin(angle), np.cos(angle), 0],
                             [0, 0, 1]])
    
        fig,rotated_image = cv2.warpPerspective(image, m_rotation, (int(cols), int(rows)))
    
        plt.axis('off')
        plt.imshow(rotated_image)
        st.pyplot(fig)
  
  
    
def scaling():
        m_scaling_ = np.float32([[1.5, 0, 0],
                            [0, 1.8, 0],
                            [0, 0, 1]
                            ])
    
        fig,scaled_image = cv2.warpPerspective(image, m_scaling_, (cols * 2, rows * 2))
    
        plt.axis('off')
        plt.imshow(scaled_image)
        st.pyplot(fig)
    
    
    
def shear():
        m_shearing_ = np.float32([[1, 0.5, 0],
                            [0, 1, 0],
                            [0, 0, 1]
                            ])
    
        fig,sheared_image = cv2.warpPerspective(image, m_shearing_, (int(cols * 1.5), int(rows * 1.5)))
    
        plt.axis('off')
        plt.imshow(sheared_image)
        st.pyplot(fig)
    
    
    
def reflection():
        m_reflection_ = np.float32([[1, 0, 0],
                                [0, -1, rows],
                                [0, 0, 1]
                                ])
    
        fig,reflected_image = cv2.warpPerspective(image, m_reflection_, (int(cols), int(rows)))
    
        plt.axis('off')
        plt.imshow(reflected_image)
        st.pyplot(fig)

for i in range(1,4):
        image = cv2.imread(str(i)+".PNG")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cols, rows, dims = image.shape
        
        translation ()
        rotation ()
        scaling ()
        shear ()
        reflection ()
        
def main():
    
        if __name__ == '__main__':
                 main()
