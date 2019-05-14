import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    view = [0,
            0,
            1];
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],
             [255,
              255,
              255]]

    color = [0, 255, 0]
    tmp = new_matrix()
    ident( tmp )

    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    step_3d = 100
    consts = ''
    coords = []
    coords1 = []
    symbols['.white'] = ['constants',
                         {'red': [0.2, 0.5, 0.5],
                          'green': [0.2, 0.5, 0.5],
                          'blue': [0.2, 0.5, 0.5]}]
    reflect = '.white'

    # print symbols
    for command in commands:
        print(command)
        op = command['op']
        args = command['args']
        if args:
            if op == 'move':
                t = make_translate(float(args[0]), float(args[1]), float(args[2]))
                matrix_mult( stack[-1], t )
                stack[-1] = [ x[:] for x in t]
            elif op == 'rotate':
                theta = float(args[1]) * (math.pi / 180)
                if args[0] == 'x':
                    t = make_rotX(theta)
                elif args[0] == 'y':
                    t = make_rotY(theta)
                else:
                    t = make_rotZ(theta)
                matrix_mult( stack[-1], t )
                systems[-1] = [ x[:] for x in t]
            elif op == 'scale':
                t = make_scale(float(args[0]), float(args[1]), float(args[2]))
                matrix_mult( stack[-1], t )
                stack[-1] = [ x[:] for x in t]
            elif op == 'box':
                pass

        else:
            if op == 'push':
                stack.append([x[:] for x in stack[-1]])
            elif op == 'pop':
                stack.pop()
            elif op == 'display':
                display(screen)

        # print command['op']
