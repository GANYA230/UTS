import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Judul aplikasi
st.title("Plot Lingkaran dengan Titik Acak Berwarna")

# Fungsi untuk menghasilkan titik acak di dalam lingkaran
def generate_random_points_in_circle(n_points, radius=1):
    points = []
    for _ in range(n_points):
        # Koordinat acak dalam lingkaran menggunakan metode polar
        r = np.sqrt(np.random.uniform(0, 1)) * radius
        theta = np.random.uniform(0, 2 * np.pi)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        points.append((x, y))
    return np.array(points)

# Meminta input dari pengguna untuk jumlah titik
n_points = st.slider("Jumlah titik acak", min_value=10, max_value=100, value=50, step=5)

# Menghasilkan titik acak di dalam lingkaran dengan radius 1
points = generate_random_points_in_circle(n_points)

# Menampilkan lingkaran dengan titik acak berwarna berbeda
fig, ax = plt.subplots()
circle = plt.Circle((0, 0), 1, color='b', fill=False, linestyle='--')

# Plot lingkaran
ax.add_artist(circle)

# Plot titik acak dengan warna acak
colors = np.random.rand(n_points)
scatter = ax.scatter(points[:, 0], points[:, 1], c=colors, cmap='rainbow')

# Set tampilan lingkaran dan batas sumbu
ax.set_xlim([-1.1, 1.1])
ax.set_ylim([-1.1, 1.1])
ax.set_aspect('equal', 'box')
plt.colorbar(scatter)

# Tampilkan plot
st.pyplot(fig)
