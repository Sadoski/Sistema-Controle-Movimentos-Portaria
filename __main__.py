import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".", "..", "..", "classes.", "telas.", "conexao.", "controller.", "dao."))
from classes.classLogin import Login


if __name__ == '__main__':
    Login()
