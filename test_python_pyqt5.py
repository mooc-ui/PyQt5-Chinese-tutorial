import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        menubar = self.menuBar()  # 菜单栏类的实例，有了这句就可以添加菜单栏（file、tool）

        #添加菜单栏
        fileMenu = menubar.addMenu('File')  # 添加菜单栏File
        #一级子菜单
        impMenu = QMenu('Import', self)   # 添加子菜单栏Import
        fileMenu.addMenu(impMenu) # 添加Import菜单在file菜单栏下面

        #二级子菜单
        impAct = QAction('Import mail', self) # 将Import mail这个菜单栏准备成一个动作，加到其他菜单栏的下面，弄成一个子菜单；当点击某一个子菜单的时候就会出现该菜单
        impMenu.addAction(impAct) # 将Import mail这个菜单加到Import菜单下面

        #一级子菜单
        newAct = QAction('New', self)  #注意这里的Import和New虽然看起来是同一级；但是创建方法不同
        fileMenu.addAction(newAct)


#==================================my_test============================================
        #添加菜单栏
        fileMenu1 = menubar.addMenu('test')  # 添加菜单栏tool
        # 一级子菜单
        imp_tool = QMenu('plug', self)
        fileMenu1.addMenu(imp_tool)  #end

        #二级子菜单
        impplugAct = QAction('plug_2', self) # 将Import mail这个菜单栏准备成一个动作，加到其他菜单栏的下面，弄成一个子菜单；当点击某一个子菜单的时候就会出现该菜单
        imp_tool.addAction(impplugAct) # 将Import mail这个菜单加到Import菜单下面


        self.setGeometry(300, 300, 300, 200) # setGeometry(左右， 上下， 宽， 高)  ;窗口显示的位置坐标是: 屏幕的（300，250）像素处。窗口大小为: 200 * 220。setGeometry(); 方法的前两个参数定位了窗口的x轴和y轴位置。第三个参数是定义窗口的宽度，第四个参数是定义窗口的高度。

        self.setWindowTitle('Submenu')  #设置窗口名字
        self.show()#显示


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())