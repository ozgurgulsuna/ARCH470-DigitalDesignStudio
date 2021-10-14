<!-- [![N|Solid](https://raw.githubusercontent.com/ozgurgulsuna/ARCH470-DigitalDesignStudio/main/top.png?token=AJH7N4Z74UZBD7UN36G274TBNAFPK)](https://nodesource.com/products/nsolid)-->

<!--<img src="top.png" style=" width: 8000px;
  height: 150px;vertical-align:middle;margin:-40px 0px; object-fit:cover;"> </center>   -->
<!--![yastik](top.png)-->
<p align="center">
   <img src="top.png" >
</p>

<h1 align="center" style=" border-bottom: none ;">Pre-Course Portfolio<br><sup> ARCH470 </sup></h1>
<!--<h3 align="center" style="font-style: italic;font-size:2em;">  ARCH 470 </h3>-->
<p align="center"


This portfolio contains previous works in parallel with computational and generative design.


</p>

<!--<img src="bottom.jpeg" style=" width: 8000px;
  height:80px;vertical-align:middle;margin:0px 0px; object-fit:cover;"> </center>  -->
  
  
<p align="center">
   <img src="bottom.png" >
</p>

<!--![yastik](bottom.png)-->

<p> <br>
  </p>
  <p> <br>

<h2 align="center"> Vertical Plotter "Polargraph" </h2>
<p align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This is a simple device, that draws pictures using a normal pen, some stepper motors and a belt. It is slow and noisy, but its enough to get the job done. It is called polargraph because it uses dual-polar coordinates system internally, rather than regular cartesian system we tend to use in 3d printers and plotters. This version is designed and built by me, but the idea of vertical plotter (HEKTOR) goes all the way back to 2002. Hektor is a portable spray paint output device for computers. It was created in collaboration with engineer Uli Franke for Jürg Lehni's diploma project at ECAL (École cantonale d'art de Lausanne).
</p>


<p align="justify" width="100%">
    <img width="39%" src="polargraph-1.jpg">
    <img width="30%" src="polargraph-2.png">
    

<img width="26%" src="polargraph-3.jpg">
</p>
<p align="center" width="100%">
    <img width="37.9%" src="polargraph-4.png">
    <img width="14.2%" src="polargraph-5.jpg">
    <img width="10.7%" src="polargraph-6.jpg">  
    <img width="37.1%" src="polargraph-7.jpg">
</p>
<p align="center" width="100%">
    <img width="24%" src="polargraph-8.png">
    <img width="25%" src="polargraph-9.jpg">
    <img width="25%" src="polargraph-10.jpg">  
    <img width="25%" src="polargraph-11.jpg">
</p>

<h3 align="left"> EXHIBITION <br><sup> METU 2019 </sup></h3>

<p align="center" width="100%">
    <img width="33%" src="top.png">
    <img width="33%" src="top.png">
    <img width="33%" src="top.png">
</p>


<h3 align="right"><sup><em> Middle East Technical University, Ankara</em> </sup></h3>



 
## _The Last Markdown Editor, Ever_



[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Dillinger is a cloud-enabled, mobile-ready, offline-storage compatible,
AngularJS-powered HTML5 Markdown editor.

- Type some Markdown on the left
- See HTML in the right
- ✨Magic ✨

## Features

- Import a HTML file and watch it magically convert to Markdown
- Drag and drop images (requires your Dropbox account be linked)
- Import and save files from GitHub, Dropbox, Google Drive and One Drive
- Drag and drop markdown and HTML files into Dillinger
- Export documents as Markdown, HTML and PDF

Markdown is a lightweight markup language based on the formatting conventions
that people naturally use in email.
As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Tech

Dillinger uses a number of open source projects to work properly:

- [AngularJS] - HTML enhanced for web apps!
- [Ace Editor] - awesome web-based text editor
- [markdown-it] - Markdown parser done right. Fast and easy to extend.
- [Twitter Bootstrap] - great UI boilerplate for modern web apps
- [node.js] - evented I/O for the backend
- [Express] - fast node.js network app framework [@tjholowaychuk]
- [Gulp] - the streaming build system
- [Breakdance](https://breakdance.github.io/breakdance/) - HTML
to Markdown converter
- [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## Installation

Dillinger requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```

## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

## Docker

Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd dillinger
docker build -t <youruser>/dillinger:${package.json.version} .
```

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
