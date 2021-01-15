import sys
import mainWin1

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = mainWin1.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
