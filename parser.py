from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    with open(fname,'r') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            if lines[i].strip() == 'line':
                i+=1
                args = [int(j) for j in lines[i].strip().split()]
                add_edge(points,args[0],args[1],args[2],args[3],args[4],args[5])
            elif lines[i].strip() == 'ident':
                ident(transform)
            elif lines[i].strip() == 'move':
                i+=1
                args = [int(j) for j in lines[i].strip().split()]
                matrix = make_translate(args[0],args[1],args[2])
                matrix_mult(matrix,transform)
            elif lines[i].strip() == 'scale':
                i+=1
                args = [int(j) for j in lines[i].strip().split()]
                matrix = make_scale(args[0],args[1],args[2])
                matrix_mult(matrix,transform)
            elif lines[i].strip() == 'rotate':
                i+=1
                args = lines[i].strip().split()
                if args[0] == 'x': matrix_mult(make_rotX(int(args[1])),transform)
                elif args[0] == 'y': matrix_mult(make_rotY(int(args[1])),transform)
                elif args[0] == 'z': matrix_mult(make_rotZ(int(args[1])),transform)
            elif lines[i].strip() == 'apply':
                matrix_mult(transform,points)
            elif lines[i].strip() == 'display':
                screen = new_screen()
                draw_lines(points, screen, color)
                display(screen)
            elif lines[i].strip() == 'save':
                i+=1
                args = lines[i].strip().split()
                screen = new_screen()
                draw_lines(points, screen, color)
                save_ppm_ascii(screen, args[0])
            elif lines[i].strip() == 'quit':
                break
            i+=1
