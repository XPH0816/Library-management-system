import traceback
from ..frame.loginFrame import *

class MainFrame:
    def __init__(self):

        try:
            self.frame = LoginFrame()
            self.frame.loginFrame()

        except Exception as e:
            traceback.print_exc()
