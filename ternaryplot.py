import math
import matplotlib
from matplotlib.patches import FancyArrow
import matplotlib.pyplot as plt


matplotlib.rcParams.update({
    "text.usetex": True
})
matplotlib.rcParams['font.size'] = 22
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

#variables
_gameTitle = ''
_x  = []
_y  = [] 

_fig, _ax = plt.subplots()

#vertices of the equilateral triangle
_vx = [0, 1, 0.5, 0]
_vy = [0, 0, math.sqrt(3)/2, 0]

#just a font
_font1 = {'family': 'serif',
            'color':  'black',
            'weight': 'normal',
            'size': 30,
        }


#conversion to cartesian
def _to_xy(a,b,c):
    try:
        return ((float(a) + 1 - float(b))/2, (math.sqrt(3)/2)*float(c))
    except ValueError as error:
        print(error)
     

def _load_file(file_name):
    try:
        file = open(file_name, 'r')
        return file
    except IOError as error:
        print(error)



def plot(*args, **kwargs):
    #placeholder code --------------------------------------------------------
    x = []
    y = []
    #transform from triangular to cartesian
    #read text file
    if len(args) == 1:
        file = _load_file(args[0])
        for line in file.readlines():
            split = line.split()
            aux = _to_xy(split[2], split[0], split[1])               
            x.append(aux[0])
            y.append(aux[1])
        file.close()
    #read arrays
    elif len(args) > 1:
        for i in range(len(args[0])):
            x.append(_to_xy(args[2][i], args[0][i], args[1][i])[0])
            y.append(_to_xy(args[2][i], args[0][i], args[1][i])[1])   

    #kwargs default definitions
    defaultKwargs = {'line_color': 'black', 
                    'line_width':  1.3,
                    'label' : '',
                    'arrow_head_width' : 0.025,
                    'show_arrow' : False,
                    'arrow_pos': 0,
                    'show_start_marker' : True,
                    'show_end_marker' : True}  
                
    kwargs = { **defaultKwargs, **kwargs }


    #plot the actual data
    _ax.plot(x, y, color = kwargs['line_color'], 
             linewidth = kwargs['line_width'], label = kwargs['label'])   
     
    if(kwargs['show_start_marker']):
        _ax.plot(x[0], y[0], marker = "o", 
            markersize = 5,
            markeredgecolor = kwargs['line_color'], 
            markerfacecolor = 'white')
        
    if(kwargs['show_end_marker']):
        _ax.plot(x[-1], y[-1], 
             marker = "o", 
             markersize = 5,
             markeredgecolor = kwargs['line_color'], 
             markerfacecolor = kwargs['line_color'])

    k = kwargs['arrow_pos']

    if(kwargs['show_arrow']): 
        arrow = FancyArrow(x[k], y[k], x[k+1]-x[k], y[k+1]-y[k], 
            shape='full', 
            lw = 0, 
            length_includes_head = True, 
            head_length = None, 
            width = 0, 
            head_width = kwargs['arrow_head_width'], 
            head_starts_at_zero = True, 
            facecolor = kwargs['line_color'],
            zorder = 3)
        
        _ax.add_patch(arrow)  

    #---------------------------------------------------------------------------------
def set_title(title):
    _ax.set_title(title, y=1.0, pad=50, **_font1)

def show_legend(**kwargs):
    default_kwargs = {'font_size' : 16}
    kwargs = { **default_kwargs, **kwargs }
    _ax.legend(fontsize = kwargs['font_size'])
    
def set_axis(strategies, **kwargs):     
    offset = .05
    #more kwargs definitions           
    default_kwargs = {'triangle_color': 'black', 
                    'triangle_line_width': 2,
                    'left_label_xpos': 0,
                    'top_label_xpos': 0,
                    'right_label_xpos': 0,
                    'left_label_ypos': 0,
                    'top_label_ypos': 0,
                    'right_label_ypos': 0}        
            
    kwargs = { **default_kwargs, **kwargs } 

    plt.axis('off')
    

    #plot the triangular axis
    _ax.plot(_vx,_vy, color = kwargs['triangle_color'], linewidth = kwargs['triangle_line_width']) 

    #draw the strategy labels
    _ax.text(kwargs['left_label_xpos']-offset, 
             kwargs['left_label_ypos']-offset, 
             strategies[0], horizontalalignment = 'center', **_font1)    
    
    _ax.text(_vx[2] + kwargs['top_label_xpos'],
             _vy[2] + offset + kwargs['top_label_ypos'],
             strategies[1], horizontalalignment = 'center', **_font1)
    
    _ax.text(_vx[1] + offset + kwargs['right_label_xpos'],
             _vy[3] - offset + kwargs['right_label_ypos'],
             strategies[2], horizontalalignment = 'center', **_font1)

def show():  
    plt.show() 

def save(figname, **kwargs):
    default_kwargs = {'dpi' : 300}
    kwargs = { **default_kwargs, **kwargs }
    plt.savefig(figname, bbox_inches='tight', dpi=kwargs['dpi'])
      

'''
REFERENCES

[1] Toshiaki Shimura, Anthony I.S. Kemp; 
Tetrahedral plot diagram: A geometrical solution for quaternary systems. 
American Mineralogist 2015;; 100 (11-12): 2545–2547. doi: https://doi.org/10.2138/am-2015-5371

[2] https://mathworld.wolfram.com/TernaryDiagram.html

[3] https://en.wikipedia.org/wiki/Ternary_plot

'''