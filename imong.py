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
    st.pyplot (img)
    
        
    
def main():
   st.title("This is Activity 1")

    x = st.slider('X1',0, 2)
    st.write('Value of X: ', x)
    
    y = st.slider('X1',0, 2)
    st.write('Value of Y: ', x)
    
    replace = st.slider('X1',0, 1000)
    st.write('Color: ', replace)
    
    fill (x,y,replace)
    
    
    print("X,Y        X,Y       X,Y")
    print("------------------------")
    print("0,0        0,1       0,2")
    print("1,0        1,1       1,2")
    print("2,0        2,1       2,2")
    
    print()

if __name__ == '__main__':
    main()
