import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from skyfield.api import load, Topos

# Şanlıurfa'nın koordinatları
sanliurfa = Topos('37.1591 N', '38.7969 E')

# Efemeris dosyalarını yükleyin
planets = load('de421.bsp')
earth = planets['earth'] + sanliurfa
sun = planets['sun']
mars = planets['mars barycenter']
jupiter = planets['jupiter barycenter']
saturn = planets['saturn barycenter']

# Zaman ölçeğini ayarlayın
ts = load.timescale()
start_time = ts.now()
frames = 365
interval_minutes = 60

# Her gezegenin anlık konumunu hesaplayan fonksiyon
def update_positions(frame):
    t = start_time + frame * interval_minutes / (60 * 24)  # Dakikayı güne çevir
    sun_pos = earth.at(t).observe(sun).apparent().position.au
    earth_pos = planets['earth'].at(t).observe(sun).apparent().position.au
    mars_pos = earth.at(t).observe(mars).apparent().position.au
    jupiter_pos = earth.at(t).observe(jupiter).apparent().position.au
    saturn_pos = earth.at(t).observe(saturn).apparent().position.au

    sun_point.set_data(sun_pos[0], sun_pos[1])
    sun_point.set_3d_properties(sun_pos[2])
    earth_point.set_data(earth_pos[0], earth_pos[1])
    earth_point.set_3d_properties(earth_pos[2])
    mars_point.set_data(mars_pos[0], mars_pos[1])
    mars_point.set_3d_properties(mars_pos[2])
    jupiter_point.set_data(jupiter_pos[0], jupiter_pos[1])
    jupiter_point.set_3d_properties(jupiter_pos[2])
    saturn_point.set_data(saturn_pos[0], saturn_pos[1])
    saturn_point.set_3d_properties(saturn_pos[2])

    return sun_point, earth_point, mars_point, jupiter_point, saturn_point

# 3D grafik penceresi
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')
ax.set_title('Güneş Sistemi Canlı Simülasyonu (Şanlıurfa)')

# Güneş, Dünya, Mars, Jüpiter ve Satürn için grafik noktaları
sun_point, = ax.plot([], [], [], 'o', color='orange', markersize=10, label='Sun')
earth_point, = ax.plot([], [], [], 'o', color='blue', markersize=8, label='Earth')
mars_point, = ax.plot([], [], [], 'o', color='red', markersize=8, label='Mars')
jupiter_point, = ax.plot([], [], [], 'o', color='brown', markersize=8, label='Jupiter')
saturn_point, = ax.plot([], [], [], 'o', color='green', markersize=8, label='Saturn')
ax.legend()

# Animasyonu başlat
anim = FuncAnimation(fig, update_positions, frames=frames, interval=100, blit=True)

# Grafiği göster
plt.show()
