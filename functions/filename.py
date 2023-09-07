import os

def get_filename():
    """
    Returns the name of the current file without the .py extension.

    Returns:
    filename (str): The name of the current file without the .py extension.
    """    filename = os.path.splitext(os.path.basename(__file__))[0]

    return filename
