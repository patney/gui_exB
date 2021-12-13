
"""
This function will be the framework for running the GUI.
main.py will inherit MainWindow which is the default ObjectName used in the Designer.
"""
from src.ui.main_window_manager import MainWindow
import logging
import sys

# Setup logging.
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(name)s [%(funcName)s:%(lineno)d]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    )

logger = logging.getLogger(__name__)
print('LOGGER', logger)

# In PyQt 5.5 the default exception handling was changed to cause the program to just crash without printing a trace
# This exception hook restores this functionality
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    sys.excepthook = except_hook
    main = MainWindow()
    # Loop the GUI till exited by the user.
    sys.exit(MainWindow.app.exec_())

