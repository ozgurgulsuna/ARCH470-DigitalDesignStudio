import numpy as np
from PIL import Image
from scipy.special import erf

from fluid import Fluid
A=100
B=100
C=20
RESOLUTION = A,B,C
DURATION = 8

INFLOW_DURATION = 200
INFLOW_RADIUS = 8
INFLOW_VELOCITY = 0.001
INFLOW_COUNT = 1

print('Generating fluid solver, this may take some time.')
fluid = Fluid(RESOLUTION, 'dye')

center = np.floor_divide(RESOLUTION, 2)
r = np.min(center)


points = np.array([center[0],center[1]*1.8 ,center[2]])
normals =  np.array([ 0, -center[1] ,0])


inflow_velocity = np.zeros_like(fluid.velocity)
inflow_dye = np.zeros(fluid.shape)
for p, n in zip(points, normals):
    #x=[5,5,5]:
    print(fluid.indices.shape,p)
    mask = np.linalg.norm(fluid.indices - points[:,None, None, None], axis=0) <= INFLOW_RADIUS
    inflow_velocity[:, mask] += normals[:, None] * INFLOW_VELOCITY
    inflow_dye[mask] = 1

frames = [[]for i in range(C)]
for f in range(DURATION):
    print(f'Computing frame {f + 1} of {DURATION}.')
    if f <= INFLOW_DURATION:
        fluid.velocity += inflow_velocity
        fluid.dye += inflow_dye

    curl = fluid.step()[1]
    # Using the error function to make the contrast a bit higher. 
    # Any other sigmoid function e.g. smoothstep would work.
    curl = (erf(curl * 2) + 1) / 4

    for c in range(C):
        color = np.dstack((curl[:,:,c], np.ones((A,B)), fluid.dye[:,:,c]))
        color = (np.clip(color, 0, 1) * 255).astype('uint8')
        frames[c].append(Image.fromarray(color, mode='HSV').convert('RGB'))
#        print('Saving simulation result.')

for c in range(C):
    frames[c][0].save('examplue'+str(c)+'.gif', save_all=True, append_images=frames[c][1:], duration=20, loop=0)
