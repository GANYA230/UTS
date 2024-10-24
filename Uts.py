import streamlit as st
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


st.title("Fisika Komputasi Awan")
st.title("Nugroho Adi Pramono :sunglasses:")
circle = Circle((0, 0), 1, color='red', fill=False, linewidth=2, linestyle='-', alpha=0.2)
x = []
y = []
color = []
size = []
x.append(0)
y.append(0)
color.append((0.,.7,0.))
size.append(371)
if st.button("Data"):
    for i in range(111):
        x0 = 2*(random.random() - .5)
        y0 = 2*(random.random() - .5)
        if ((x0**2+y0**2)>1.):
            if y0>0:
                y0 = np.sqrt(1-x0**2)
            else:
                y0 = -1*(np.sqrt(1-x0**2))
            
        x.append(x0)
        y.append(y0)
        color.append((random.random(),random.random(),random.random()))
        size.append(3713*random.random() )
    
fig, ax = plt.subplots(figsize=(16, 16))
ax.add_patch(circle)

for i in range(1, len(x)):
    ax.plot([0, x[i]], [0, y[i]], color='green', linestyle='--', alpha=0.2)

ax.scatter(x, y, c=color, s=size, alpha=0.5) 

ax.set_ylabel("y")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
#ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
ax.set_title('Data Acak yang berubah setiap tombol ditekan')
ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
st.pyplot(fig)
st.caption("Lingkaran dengan ukuran dan warna acak dan tersebar didalam lingkaran dengan radius 1")
st.divider()
st.text("Buat website seperti di atas dengan menggunakan GitHub dan Streamlit.")
st.text("Kirim video saat website dijalankan.") 
st.text("Pastikan nama dan alamat website terlihat.")
st.divider()
