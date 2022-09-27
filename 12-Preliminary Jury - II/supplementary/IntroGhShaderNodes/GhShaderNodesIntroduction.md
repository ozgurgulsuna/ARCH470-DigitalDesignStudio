
<h1><sub>Introduction to Material Nodes  with</sub> </sub>	<br> GhShaderNodes </h1>

### **What are material nodes and is it possible to control the materials using grasshopper definitons?**

Material nodes are type of nodes that produce a material definition when combined. There are many types of blocks in this node system, there are ones for combining textures, colors, for blending materials and etc.

![fig-1](https://user-images.githubusercontent.com/38794995/148677138-6e2346f6-aa93-469e-8fea-703dad8e43b7.jpg)

It helps us not only to create textures from scratch but control them using our parameters within grasshopper.

Here are some useful links to further understand this concept:
- https://en.wikipedia.org/wiki/Procedural_texture
- https://youtu.be/Wx9vmYwQeBg

## Getting Started
1. We need to have a grasshopper plugin to generate our materials. It is called GhShaderNodes and can be downloaded from the link below;
https://github.com/mcneel/GhShaderNodes/releases/tag/v0.1.1
As stated in the release it is written for ***Rhino 6.3.18*** and as today it is an outdated version of rhino. But it is not the end of the world, some of the features of this plugin is still working for Rhino 7 and near complete features work within Rhino 6.
We will continue with Rhino 7.

2. After installing this plugin just as all other plugins on grasshopper (tutorial here: https://youtu.be/vBh1UHg6ZHQ) keeping in mind that sometimes you need to unblock the .gha (grasshopper assembly) from the properties in windows. we will have one last step remaining.

3. We need to turn on the private content inside Rhino to enable the custom materials we will define.
It is as easy as writing ``` TestShowPrivateContent ``` in the command line. This enables the hidden materials under material library. The one we will use is "Cycles XML".

![fig-2](https://user-images.githubusercontent.com/38794995/148678063-6d3d1f4d-9799-4e0d-abae-fb59c0fb4ebd.png)

4. The installation process is done and we can play with our new nodes.
Here is a tutorial video for installation, https://discourse.mcneel.com/t/ghshadernodes-raytraced-rhino-6-2018-05-03/61985?page=2


## Node Types

![fig-3](https://user-images.githubusercontent.com/38794995/148678405-bf3fd970-a666-4435-a49e-fd94bdeee522.png)


- *BSDF Nodes*
	These nodes are the core material nodes and we will modify them, connect different textures to them and combine them. BSDF stands 			for bidirectional scattering distribution funciton and this contains the mathematical definitions. Sub types consist of;
	 - Principled BSDF
   - Diffuse BSDF
   - Glass BSDF
   - Glossy BSDF
   - Refraction BSDF
					 ...

- *Color Nodes*
	These nodes are the to generate ramp color and mix different colors, namely;
	 - Color Ramp
	 - Color Mix

- *Converter Nodes*
	To convert different color spaces into other we use converter nodes, basic examples are;
	 - Color2Bw
	 - Combine RGB
	 - Seperate RGB
	      ...

- *Input Nodes*
	We have couple of input nodes from the environment, we can get;
	 - Camera Data
	 - Geometry
	 - Light Path
	 - Texture Coordinate
   	   ...

- *Math and Vector Algebra Nodes*
	For generic mathematical oprations we have these node groups;
	 - Add
	 - Substract
	 - Minimum
	 - Sine
	 - Tangent
	 - Dot Product
	 - Cross Product
	      ...

- *Operation Nodes*
	Operation in this group are blending, addition and background. These are to combine BSDF nodes;
	 - Blend
	 - Add
	 - Background
	 
- *Texture Nodes*
	Texture that we import or generate inside grasshopper;
	 - Imagge
	 - Gradient
	 - Noise
	 - Wave
  	   ...
	 
- *Output Node*
	The node to export the material into Rhino;
	 - Output
	 

## Example Node Systems
Starting in grasshopper, first we create a color ramp and its factor is fed by noise texture,Then its color output sourced onto the surface of the material with output node.

System is shown below.
![fig-4](https://user-images.githubusercontent.com/38794995/148683427-b37b850f-efac-4ce9-80d1-27ea1849dee5.png)

Now lets change the primary shader to glossy one and control the roughness with the same noise texture.
![fig-5](https://user-images.githubusercontent.com/38794995/148683529-645445d3-bdb9-4b98-ba76-6fb60affaea3.png)

We can use emission node to make our texture emissive in the pixels we want.
![fig-6](https://user-images.githubusercontent.com/38794995/148683545-73ab5a59-a90d-4c87-9cc5-ae3f5df37f1e.png)

The effect is more clear in the next one with red coloured areas has the emission texture mapped.
![fig-8](https://user-images.githubusercontent.com/38794995/148683590-af3c2657-a390-4b40-b374-f1f309e38ebd.png)

Here some links for more advanced node systems
- https://discourse.mcneel.com/t/ghshadernodes/112600
- https://discourse.mcneel.com/t/watercolouring-using-grasshopper/112220/3
- https://discourse.mcneel.com/t/ghshadernodes-raytraced-rhino-6-2018-05-03/61985/28?page=2

Two notices that need to be adressed
- to set the material in rhino we right click the output node and select the already added Cycles XML material.
- Disabling and re-enabling the output node ensures that our material definition is applied.

![fig-10](https://user-images.githubusercontent.com/38794995/148683842-2eb101fb-9dec-4a2a-9d37-7415686ef5f6.png)


## Notes
- These cycles materials work only for the ray-traced render engine (cycles) because the light paths need to be calculated.
- Although this plugin is compiled for Rhino 6, some of the features still work for Rhino 7. (Could not get the image textures to import)


