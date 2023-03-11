import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

two_d_arr = np.array([[800, 800, 800],
                      [800, 800, 800],
                      [800, 800, 800]])
    
x = []
y = []
replace = []
    
def fill(x, y, replace):
    
    for i in range(len(two_d_arr)):
        for j in range(len(two_d_arr[i])):
            two_d_arr[x][y] = replace
            
    img = plt.imshow(two_d_arr)
    img.set_clim([1,1000])
    plt.colorbar()
    plt.show()
    st.pyplot(img)
    
        
    
def main():
   st.title("This is Activity 1")

   x = st.slider('y',0, 2)
   st.write('Value of X: ', x)
    
   y = st.slider('x',0, 2)
   st.write('Value of Y: ', y)
    
   replace = st.slider('color',0, 1000)
   st.write('color: ', replace)
    
   fill(x, y, replace)

 if __name__ == '__main__':
   main()
