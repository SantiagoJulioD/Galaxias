import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import gzip

column_names = [
    "ID",
    "Epoca",
    "RA_deg",
    "Dec_deg",
    "Paralaje_arcsec",
    "MovimientoPropio_masyr",
    "Vr_kms",
    "Long_gal_deg",
    "Lat_gal_deg",
    "Dist_metodo1_pc",
    "Dist_metodo2_pc"
]

with gzip.open("subsample_GalEx_2M.txt.gz", "rt") as f:
    df = pd.read_csv(f, sep=",", header=None, names=column_names)

df['Dist_pc'] = df['Dist_metodo2_pc']
fill = df.loc[df['Dist_metodo2_pc'].isna(),'Dist_metodo1_pc']
df['Dist_pc'] = df['Dist_pc'].fillna(fill)

df['x'] = df['Dist_pc']*np.cos(df['Long_gal_deg']*np.pi/180)*np.cos(df['Lat_gal_deg']*np.pi/180)-8000
df['y'] = df['Dist_pc']*np.sin(df['Long_gal_deg']*np.pi/180)*np.cos(df['Lat_gal_deg']*np.pi/180)
df['z'] = df['Dist_pc']*np.sin(df['Lat_gal_deg']*np.pi/180)

df = df[(df['Lat_gal_deg']>-10) & (df['Lat_gal_deg']<10)]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(df['x'], df['y'], df['z'])
ax.set(zlim=(-20000,20000))

plt.show()