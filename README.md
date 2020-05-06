# Online Image Filter
Median or Mean image filter using python. The goal of this project is to offer a online median/mean filter. The project would read a PPM file, apply the filter per pixel, write the buffer to a new file. The new file is sent back by the server. 

## How to Setup
This server runs off of Flask, as such, it must be installed. Nothing else is required. <br />
`
pip install flask
`
<br /> This code was developed and tested with python 3.8

Run the server. <br />
`
python server.py
`
<br /> Visit localhost:5000 to see the result
