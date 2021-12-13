import PyQt5.QtWidgets as Qt
"""
Example of showing a custom pop up message when called.
There is a QMessage box in PyQt5.
"""
class PopMessage:
    # Inherent the Parent GUI which gives  access to all elements.
    def __init__(self, parent=None):
        super().__init__()
        self.main = parent

    def show_pop_message(self, box_type='YN',
                         pop_msg='Nothing passed to pop message',
                         level='info',
                         win_title='User Message'):

        # pop_msg = '<b>' + str(pop_msg)
        pop_msg = str(pop_msg)
        msg_box = Qt.QMessageBox(self.main)
        box_bttns = {'YN': msg_box.Yes | msg_box.No, 'OK': msg_box.Ok}[box_type.upper()]
        self.main.app.processEvents()
        mbox = {'critical': msg_box.critical,
                'info': msg_box.information,
                'warn': msg_box.warning,
                'ques': msg_box.question}[level]
        user_response = mbox(self.main, win_title, pop_msg, box_bttns)

        return {16384: True, 65536: False}.get(user_response, None)