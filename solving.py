import kociemba
from rubik_solver import utils
from io import StringIO 
import sys
from scipy.spatial import distance as dist

cube_colors = [[255, 255, 255], [0, 255, 255], [255, 0, 0], [1, 255, 0], [0, 0, 225], [0, 125, 255]]
cube_colors_names = ['white', 'yellow', 'blue', 'green', 'red', 'orange']
#color_map = {'white': 0, 'yellow': 1, 'blue': 3, 'green': 2, 'red': 4, 'orange': 5}
color_map = {'white': 3, 'yellow': 0, 'blue': 5, 'green': 2, 'red': 4, 'orange': 1}
color_map_inv = {v: k for k, v in color_map.items()}
color_map_rubik = {'white': 'w', 'yellow': 'y', 'blue': 'b', 'green': 'g', 'red': 'r', 'orange': 'o'}
kociemba_map = {'white': 'D', 'yellow': 'U', 'blue': 'B', 'green': 'F', 'red': 'L', 'orange': 'R'}

def get_colors(img):
    h, w = img.shape[0:2]
    colors = []
    i = 0
    while i < 9:
        #print(i)
        color = img[(h//3) * (i//3) + h//6, (w//3) * (i%3) + w//6]
        colors.append(color)
        i = i+1
    #print(colors)
    return colors


def get_cube_color(color):
    dist_min = 10000
    j = 0
    for i in range(6):
        
        distanc = dist.euclidean(cube_colors[i], color)
        #np.sum(np.square(color - cube_colors[i]))
        if distanc < dist_min:
            j = i
            dist_min = distanc
            #print(dist)

    return cube_colors_names[j]

def get_matrix(colors):

    matrix = []
    i = 0
    #print(colors)
    while i <9:
        matrix.append(get_cube_color(colors[i]))
        i = i+1
    #print(matrix)
    return matrix

def add_matrix(matrix, cube_flat):
    center_color =  matrix[4]
    #no = center_color
    matrix_no = np.zeros(9)
    for i in range(9):
        matrix_no[i] = color_map[matrix[i]]

    no = color_map[center_color]
    cube_flat[9*no:9*no+9] = matrix_no
    return cube_flat


def get_cube_kociemba(cube_flat):
    s= kociemba_map[color_map_inv[cube_flat[0]]]
    i = 1
    while i < len(cube_flat):
        s= s + kociemba_map[color_map_inv[cube_flat[i]]]
        i=i+1
    return s

def cube_encode(img_list):
    i = 0
    cube_flat = np.zeros(54)
    while i < len(img_list):
        colors = get_colors(img_list[i])
        matrix = get_matrix(colors)
        add_matrix(matrix, cube_flat)
        i = i+1
    #print(cube_flat)
    cube = get_cube_kociemba(cube_flat)
    return cube





def cube_solver(img_format, visualise = True):
    no_of_boxes = []
    img_list = []
    if visualise:
        print('The Cube is being converted...')
    for i in range(1000):
        mask_path = '/root/Mask_RCNN/mask'
        #no_of_stacks = save_results_top_face(input_image_path, 'result.jpg', mask_path)

        img_path  = img_format + str(i+1) + '.jpg'
        img = cv2.imread(img_path)
        if isinstance(img, np.ndarray):
            
            flat_save_path = '/root/Mask_RCNN/flat' + str(i+1) + '.jpg'
            curent_mask_path = mask_path + str(1) + '.jpg'
            no_of_stacks = save_results_top_face(img_path, 'result.jpg', mask_path)
            is_flat = flat_extractor(img_path, curent_mask_path, flat_save_path)
            if visualise:
                if not is_flat:
                    no_of_boxes.append(0)
                    print('Face not detected!!!')
                    print('==========')
                    i = i+1
                    continue
                else:
                    print('Face detected!')
            img = cv2.imread(flat_save_path)
            img_list.append(img)
    cube = cube_encode(img_list)
    #print(cube)
    if visualise:
        print('The cube is being solved...')
    print('The algorithm to solve the cube is: ')
    algo = kociemba.solve(cube)
    print(algo)
    steps = 1
    for s in algo:
        if s==' ':
            steps += 1
    print('No. of steps: ', steps)
    #print(cube('F'))
    #solver = CFOPSolver(cube)
    #
    #utils.solve(cube, 'CFOP')
    #with Capturing() as output:
    #    solver.solve()
    #print('Solved!')
    #print('The steps you need to solve the cube are: \n \n' + (output[-1][6:]))

