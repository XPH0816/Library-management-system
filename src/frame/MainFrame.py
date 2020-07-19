import traceback
import src.frame.loginFrame
from src.frame.loginFrame import *

def main():

    try:
        frame = LoginFrame()
        frame.loginFrame()

    except Exception as e:
        traceback.print_exc()



if __name__ == "__main__" :
    main()
