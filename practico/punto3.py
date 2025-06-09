import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

cumulos = pd.read_csv('GCs_MW_vf.csv')

x_ = []
y_ = []
z_ = []
with open(r"disquito.dat") as datFile:
    x_ = [data.split()[0] for data in datFile]
with open(r"disquito.dat") as datFile:
    y_ = [data.split()[1] for data in datFile]
with open(r"disquito.dat") as datFile:
    z_ = [data.split()[2] for data in datFile]

disco = pd.DataFrame()
disco['x'] = np.array(x_).astype(float)
disco['y'] = np.array(y_).astype(float)
disco['z'] = np.array(z_).astype(float)

new_names = {cumulos.columns[i]:cumulos.columns[i].replace(' ','') for i in range(len(cumulos.columns))}
cumulos = cumulos.rename(columns=new_names)

cumulos[[cumulos == '     ']] = np.nan
cumulos[[cumulos == ' ']] = np.nan

for i in cumulos.columns[3:]:
    cumulos[i] = cumulos[i].astype(float)

cumulos['x'] = cumulos['Rsun']*np.cos(cumulos['GLAT']*np.pi/180)*np.cos(cumulos['GLON']*np.pi/180)-8
cumulos['y'] = cumulos['Rsun']*np.cos(cumulos['GLAT']*np.pi/180)*np.sin(cumulos['GLON']*np.pi/180)
cumulos['z'] = cumulos['Rsun']*np.sin(cumulos['GLAT']*np.pi/180)

fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(projection='3d')   
ax.set(xlim=(-60,60),ylim=(-60,60),zlim=(-60,60))

ax.view_init(0, -0, 0)

ax.plot(disco['x'].values,disco['y'].values,disco['z'].values,color='deepskyblue',alpha=0.5,marker='.',linestyle='none')
ax.plot(cumulos['x'].values,cumulos['y'].values,cumulos['z'].values,marker='.',linestyle='none',c='darkorange')
ax.plot(8,0,0,color='r',marker='.',linestyle='none')
plt.show()