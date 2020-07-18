import traceback
import loginFrame
from loginFrame import *

def main():

    try:
        frame = LoginFrame()
        frame.loginFrame()

    except Exception as e:
        traceback.print_exc()



if __name__ == "__main__" :
    main()
