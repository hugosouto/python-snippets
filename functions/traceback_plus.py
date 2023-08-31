# This code prints a detailed traceback when an exception occurs

# Snippet to use this function:
# 
# import sys
# sys.path.append("D:\\OneDrive\\Documentos\\GitHub\\snippets-python")
# from functions.traceback_plus import print_exc_plus

import sys, traceback

def print_exc_plus( ):
    """ Print the usual traceback information, followed by a listing of
    all the local variables in each frame.
    """
    
    # Get the traceback object
    tb = sys.exc_info( )[2]

    # Walk the traceback frame objects
    while tb.tb_next:
        tb = tb.tb_next

    # Create a list of all the traceback frames
    stack = [ ]
    f = tb.tb_frame
    while f:
        stack.append(f)
        f = f.f_back
    stack.reverse( )

    # Print the traceback information
    traceback.print_exc( )

    # Print the locals on each frame
    print("Locals by frame, innermost last")
    for frame in stack:
        print()
        print("Frame %s in %s at line %s" % (frame.f_code.co_name,
                                             frame.f_code.co_filename,
                                             frame.f_lineno))
        for key, value in frame.f_locals.items():
            print(r"\t%20s = " % key),
            try:
                print(value)
            except:
                print("<ERROR WHILE PRINTING VALUE>")