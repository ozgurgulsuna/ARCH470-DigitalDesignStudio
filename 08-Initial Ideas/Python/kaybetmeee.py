 
import numpy as np
from PIL import Image
from scipy.special import erf

from fluid import Fluid

RESOLUTION = 50,100,5
DURATION = 100

INFLOW_DURATION = 80
INFLOW_RADIUS = 8
INFLOW_VELOCITY = 0.01
INFLOW_COUNT = 1

print('Generating fluid solver, this may take some time.')
fluid = Fluid(RESOLUTION, 'dye')

center = np.floor_divide(RESOLUTION, 2)
r = np.min(center)


points = np.array([center[0],center[1] ,center[2]])
normals =  np.array([-center[0],-center[1] ,-center[2]])


inflow_velocity = np.zeros_like(fluid.velocity)
inflow_dye = np.zeros(fluid.shape)
for p, n in zip(points, normals):
    #x=[5,5,5]:
    print(fluid.indices.shape,p)
    mask = np.linalg.norm(fluid.indices - points[:,None, None, None], axis=0) <= INFLOW_RADIUS
    inflow_velocity[:, mask] += normals[:, None] * INFLOW_VELOCITY
    inflow_dye[mask] = 1

frames = []
for f in range(DURATION):
    print(f'Computing frame {f + 1} of {DURATION}.')
    if f <= INFLOW_DURATION:
        fluid.velocity += inflow_velocity
        fluid.dye += inflow_dye

    curl = fluid.step()[1]
    # Using the error function to make the contrast a bit higher. 
    # Any other sigmoid function e.g. smoothstep would work.
    curl = (erf(curl * 2) + 1) / 4

    for c in range(5):
        
    color = np.dstack((curl[:,:,c], np.ones((50,100)), fluid.dye[:,:,c]))
    color = (np.clip(color, 0, 1) * 255).astype('uint8')
    frames.append(Image.fromarray(color, mode='HSV').convert('RGB'))
    

print('Saving simulation result.')
frames[0].save('example.gif', save_all=True, append_images=frames[1:], duration=20, loop=0)
