from qtpy.QtWidgets import QApplication, QMainWindow,QWidget,QFileDialog,QFormLayout,QLineEdit,QTabWidget,QMdiArea,QTextEdit,QDockWidget,QSplitter
from qtpy.QtCore import Qt,Signal
from qtpy.QtGui import QPalette,QBrush,QColor
import qtpy
from qtpy import QtGui
from qtpy import QtCore
import sys
from ui.ui_main_window import Ui_MainWindow
from LeftModuleWidget import LeftModuleWidget
from OutputWidget import OutputWidget
class MainWinUi(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWinUi,self).__init__()
        self.initUi()
    def initUi(self):
        self.setupUi(self)
        self.leftWidget = LeftModuleWidget()
        self.leftWidget.setMinimumSize(180,600)
        self.mdi = QMdiArea()
        self.mdi.setViewMode(QMdiArea.TabbedView)
        self.mdi.setTabsClosable(1)
        self.mdi.setTabsMovable(1)
        self.LeftDockWidget = QDockWidget("Modules",self)
        self.LeftDockWidget.setWidget(self.leftWidget)
        self.RightDockWidget = QDockWidget("Values",self)
        self.RightDockWidget.resize(150,150)
        #self.RifghtDockWidget.setWidget(self.leftWidget)
        self.TextOutput = OutputWidget(self) #内置于信息输出视图
        self.TextOutput.setReadOnly(True)     #仅作为信息输出，设置“只读”属性
        self.OutputDock = QDockWidget("Output",self)
        #self.OutputDock.setMinimumSize(600,150)
        self.OutputDock.setWidget(self.TextOutput)
        self.TextOutput.setText("2021-7-10 21:34 EveIDE_PLUS with monaco editor")
        splitter1 = QSplitter(Qt.Vertical)
        splitter1.addWidget(self.mdi)           #多文档视图占布局右上
        splitter1.addWidget(self.OutputDock)     #信息输出视图占布局右下
        self.addDockWidget(Qt.LeftDockWidgetArea,self.LeftDockWidget)#工程视图占布局左边
        self.addDockWidget(Qt.RightDockWidgetArea,self.RightDockWidget)

        self.setCentralWidget(splitter1)



def initDark():
    from qtmodernredux import QtModernRedux
    app = QtModernRedux.QApplication(sys.argv)
    mw = QtModernRedux.wrap(MainWinUi(),
                            titlebar_color=QColor('#555555'),
                            window_buttons_position=QtModernRedux.WINDOW_BUTTONS_RIGHT)
    mw.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    initDark()
    #app = QApplication(sys.argv)
    #mainWin = MainWinUi()
    #mainWin.show()
    #app.exec_()

'''import sys
from PySide2 import QtWidgets
# from PySide2 import QtWidgets
# from PyQt5 import QtWidgets
from qt_material import apply_stylesheet

# create the application and the main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# setup stylesheet
apply_stylesheet(app, theme='dark_teal.xml')
from qt_material import list_themes

list_themes()
# run
window.show()
app.exec_()'''