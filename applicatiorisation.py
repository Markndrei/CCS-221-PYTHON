import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay

import tensorflow as tf

tf.compat.v1.disable_eager_execution()

option=[]    

def _cube_(bottom_lower=(0, 0, 0), side_length=3):
    """Create cube starting from the given bottom-lower point (lowest x, y, z values)"""
    bottom_lower = np.array(bottom_lower)
    
    points = np.vstack([
        bottom_lower,
        bottom_lower + [0, side_length, 0],
        bottom_lower + [side_length, side_length, 0],
        bottom_lower + [side_length, 0, 0],
        bottom_lower + [0, 0, side_length],
        bottom_lower + [0, side_length, side_length],
        bottom_lower + [side_length, side_length, side_length],
        bottom_lower + [side_length, 0, side_length],
        bottom_lower,
        
    ])   


    return points

def _plt_basic_object(points):
    """Plots a basic object, assuming its convex and not too complex"""
    
    tri = Delaunay(points).convex_hull
    
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(points[:,0], points[:,1],
                        points[:,2], triangles=tri,
                        shade=True, cmap=cm.rainbow,
                        lw=0.5
                        )
    
    ax.set_xlim3d(-5, 5)
    ax.set_ylim3d(-5, 5)
    ax.set_zlim3d(-5, 5)
    

    plt.show()
    st.pyplot (fig)





init_cube_ = _cube_(side_length=3)


def translate(points):
    def translate_obj(points, amount):
        return tf.add(points, amount)


    translation_amount = tf.constant([1, 2, 2], dtype=tf.float32)
    fig,translated_shape = translate_obj(points, translation_amount)


    with tf.compat.v1.Session() as session:

        translated_shape = session.run(translated_shape) 

    _plt_basic_object(translated_shape)
    st.pyplot (fig)

def rotate(option, points):
    def rotate_obj(points, angle):
        angle = float(angle)
        rotation_matrix = tf.stack([
                        [tf.cos(angle), tf.sin(angle), 0],
                        [-tf.sin(angle), tf.cos(angle), 0],
                        [0, 0, 1]
        ])

        fig,rotate_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))
        
        return rotate_object
        st.pyplot (fig)
        
        
    with tf.compat.v1.Session() as session:
            
        if option == "Cube":
            rotated_object = session.run(rotate_obj(init_cube_, 75)) 
            _plt_basic_object(rotated_object)

            
            
def main():
    option = st.selectbox('What shape would you like to rotate?', ('Cube', 'Pyramid', 'Triangle', 'Diamond'))

    st.write('The shape you chose is:', option)

    if option == "Cube":
        _cube_(bottom_lower=(0, 0, 0), side_length=3)
        init_cube_ = _cube_(side_length=3)
        points = tf.constant(init_cube_, dtype=tf.float32)
        translate(points)
        rotate(option, points)
        
        
if __name__ == '__main__':
    main()




       
               
