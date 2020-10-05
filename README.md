# Automatic_Rubiks_Cube_Solver

This project allows you to input images of the faces of a cube and prints out an algorithm to solve it.
It uses Segmentation to detect the actual faces of the cube and then assumes a uniform 3*3 grid-like distribution to find the color of each piece.

Current logic: Find closest color from a set of 6 predefined colors (Logic needs to be changed with different cubes). I am working on clustering algorithms to solve this issue.

Once the colors are detected, it is converted into a format according to Kociemba Solver, and then solved by the Kociemba algorithm, which allows any configuration to be solved in less than 30 steps.
The final output is an algorithm to solve the cube (and the number of steps).

## Instructions of use:

1. Clone the repository and open cube_solving.ipynb in [Google Colaboratory](https://colab.research.google.com). 
2. The Google colab file has commands to install all the prerequisites and you simply need to run the cells to get the required. 
3. Copy the weights file from [here](https://drive.google.com/drive/folders/1unXQKfb-HFnMSqKj82VZ10dLmTdbfhrh?usp=sharing) into your google drive account and note the location. Follow instructions in the colab file to put the location (path) in a line of code.
4. Run the cells of the cube_solving.ipynb file in order upto the section 'Main Inference'. They have requirements and helper functions.
5. take images of each face of the cube such that the image in the below figure would look straight. 

<img src = '/images/cube_flat.png' width =  '50%'>

6. make a directory '/content/scramble/' and add the files in the format 'cube.png' (This format can be changed by changing the final inference function)
7. run the final inference function to get the algorithms to solve the cube. The algorithm consists of a list of characters that follow this [convention](https://ruwix.com/the-rubiks-cube/notation/).


## Example output:
Below is a screenshot of the output obtained for one cube:
![output](/images/output.png)

## Fun with Pycuber:
Pycuber is a fun interactive environment that visualises a cube. I am planning to make a web app that uses this to make a user-friendly interactive cube solver.

<img src = '/images/pycuber1.png' width =  '34%'>    <img src = '/images/pycuber2.png' width =  '63%'>
