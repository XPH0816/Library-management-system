import traceback
import src.frame.loginFrame
from src.frame.loginFrame import *

class MainFrame:
    def __init__(self):

        try:
            frame = LoginFrame()
            frame.loginFrame()

        except Exception as e:
            traceback.print_exc()
