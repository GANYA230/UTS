import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Judul aplikasi
st.title("Plot Lingkaran dengan Titik Acak Berwarna")

# Fungsi untuk menghasilkan titik acak di dalam lingkaran
def generate_random_points_in_circle(n_points, radius=1):
    points = []
    for _ in range(n_points):
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

# Plot lingkaran dan titik acak
fig = go.Figure()

# Plot lingkaran
circle_x = np.cos(np.linspace(0, 2 * np.pi, 100))
circle_y = np.sin(np.linspace(0, 2 * np.pi, 100))
fig.add_trace(go.Scatter(x=circle_x, y=circle_y, mode='lines', name='Lingkaran', line=dict(color='blue')))

# Plot titik acak dengan warna acak
colors = np.random.rand(n_points)
fig.add_trace(go.Scatter(x=points[:, 0], y=points[:, 1], mode='markers',
                         marker=dict(color=colors, colorscale='Rainbow', size=10), name='Titik Acak'))

# Set layout agar proporsional
fig.update_layout(width=600, height=600, xaxis=dict(scaleanchor="y", scaleratio=1), yaxis=dict(scaleanchor="x"))

# Tampilkan plot
st.plotly_chart(fig)
