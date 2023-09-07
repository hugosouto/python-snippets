import os
from profilehooks import profile

def get_filename():
    """
    Returns the name of the current file without the .py extension.

    Returns:
    filename (str): The name of the current file without the .py extension.
    """
    filename = os.path.splitext(os.path.basename(__file__))[0]

    return filename

@profile(stdout=False, filename=f'profiles/{get_filename()}.prof')
def main():
    """
    This function runs the main program logic.
    """
    # Add your code here

if __name__ == '__main__':
    main()
