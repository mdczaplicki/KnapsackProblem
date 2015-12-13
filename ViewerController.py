# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knapsackproblem.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from functools import wraps
import numpy as np
import traceback
import types

import KP
import KPC

DEBUG = True


def my_slot(*args):
    if len(args) == 0 or isinstance(args[0], types.FunctionType):
        args = []

    @QtCore.pyqtSlot(*args)
    def slot_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args)
            except:
                print("Uncaught Exception in slot")
                traceback.print_exc()
        return wrapper

    return slot_decorator


class MatplotlibWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)

        self.axis = self.figure.add_subplot(111)
        self.figure.tight_layout()
        self.axis.grid(color='#AAAAAA', which='major', linestyle='-', linewidth=0.5)

        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.canvas)


# noinspection PyAttributeOutsideInit,PyUnresolvedReferences
class UiKnapsackProblem(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.items_list = []
        if DEBUG:
            from random import randint
            self.items_list = [(randint(1, 15), randint(1, 20)) for _ in range(20)]

    def setup_ui(self, knapsack_problem):
        knapsack_problem.setObjectName("KnapsackProblem")
        knapsack_problem.resize(657, 457)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(1)
        size_policy.setHeightForWidth(knapsack_problem.sizePolicy().hasHeightForWidth())
        knapsack_problem.setSizePolicy(size_policy)
        self.central_widget = QtWidgets.QWidget(knapsack_problem)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(size_policy)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.capacity_label = QtWidgets.QLabel(self.central_widget)
        self.capacity_label.setObjectName("capacity_label")
        self.gridLayout_3.addWidget(self.capacity_label, 1, 0, 1, 1)

        self.capacity_edit = QtWidgets.QLineEdit(self.central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.capacity_edit.sizePolicy().hasHeightForWidth())
        self.capacity_edit.setSizePolicy(size_policy)
        self.capacity_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.capacity_edit.setObjectName("capacity_edit")
        self.gridLayout_3.addWidget(self.capacity_edit, 1, 1, 1, 1)

        self.frame = QtWidgets.QFrame(self.central_widget)
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3.addWidget(self.frame, 2, 0, 1, 2)

        self.weight_label = QtWidgets.QLabel(self.central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.weight_label.sizePolicy().hasHeightForWidth())
        self.weight_label.setSizePolicy(size_policy)
        self.weight_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.weight_label.setObjectName("weight_label")
        self.gridLayout_3.addWidget(self.weight_label, 3, 0, 1, 1)

        self.weight_edit = QtWidgets.QLineEdit(self.central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.weight_edit.sizePolicy().hasHeightForWidth())
        self.weight_edit.setSizePolicy(size_policy)
        self.weight_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.weight_edit.setObjectName("weight_edit")
        self.weight_edit.setValidator(QtGui.QIntValidator(0, 999))
        self.gridLayout_3.addWidget(self.weight_edit, 3, 1, 1, 1)

        self.value_label = QtWidgets.QLabel(self.central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.value_label.sizePolicy().hasHeightForWidth())
        self.value_label.setSizePolicy(size_policy)
        self.value_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.value_label.setObjectName("value_label")
        self.gridLayout_3.addWidget(self.value_label, 5, 0, 1, 1)

        self.value_edit = QtWidgets.QLineEdit(self.central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.value_edit.sizePolicy().hasHeightForWidth())
        self.value_edit.setSizePolicy(size_policy)
        self.value_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.value_edit.setObjectName("value_edit")
        self.value_edit.setValidator(QtGui.QIntValidator(0, 999))
        self.gridLayout_3.addWidget(self.value_edit, 5, 1, 1, 1)

        self.add_button = QtWidgets.QPushButton(self.central_widget)
        self.add_button.setObjectName("add_button")
        self.gridLayout_3.addWidget(self.add_button, 6, 0, 1, 2)

        self.items_tree = QtWidgets.QTreeWidget(self.central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.items_tree.sizePolicy().hasHeightForWidth())
        self.items_tree.setSizePolicy(size_policy)
        self.items_tree.setMinimumSize(QtCore.QSize(165, 0))
        self.items_tree.setMaximumSize(QtCore.QSize(200, 16777215))
        self.items_tree.setObjectName("items_tree")
        self.items_tree.header().resizeSection(0, 30)
        self.items_tree.header().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.items_tree.header().setSectionsMovable(False)
        self.gridLayout_3.addWidget(self.items_tree, 8, 0, 1, 2)

        self.remove_button = QtWidgets.QPushButton(self.central_widget)
        self.remove_button.setObjectName("remove_button")
        self.gridLayout_3.addWidget(self.remove_button, 9, 0, 1, 2)

        self.algo_combo_box = QtWidgets.QComboBox(self.central_widget)
        self.algo_combo_box.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.algo_combo_box.setObjectName("algo_combo_box")
        self.algo_combo_box.addItem("")
        self.algo_combo_box.addItem("")
        self.gridLayout_3.addWidget(self.algo_combo_box, 10, 0, 1, 2)

        self.population_label = QtWidgets.QLabel(self.central_widget)
        self.population_label.setObjectName("population_label")
        self.gridLayout_3.addWidget(self.population_label, 11, 0, 1, 1)

        self.population_edit = QtWidgets.QLineEdit(self.central_widget)
        self.population_edit.setEnabled(False)
        self.population_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.population_edit.setObjectName("population_edit")
        self.population_edit.setValidator(QtGui.QIntValidator(0, 20))
        self.gridLayout_3.addWidget(self.population_edit, 11, 1, 1, 1)

        self.iteration_label = QtWidgets.QLabel(self.central_widget)
        self.iteration_label.setObjectName("iteration_label")
        self.gridLayout_3.addWidget(self.iteration_label, 12, 0, 1, 1)

        self.iteration_edit = QtWidgets.QLineEdit(self.central_widget)
        self.iteration_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.iteration_edit.setObjectName("iteration_edit")
        self.iteration_edit.setValidator(QtGui.QIntValidator(0, 9999))
        self.gridLayout_3.addWidget(self.iteration_edit, 12, 1, 1, 1)

        self.source_label = QtWidgets.QLabel(self.central_widget)
        self.source_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.source_label.setTextFormat(QtCore.Qt.AutoText)
        self.source_label.setWordWrap(True)
        self.source_label.setObjectName("source_label")
        self.gridLayout_3.addWidget(self.source_label, 13, 0, 1, 1)

        self.source_edit = QtWidgets.QLineEdit(self.central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.source_edit.sizePolicy().hasHeightForWidth())
        self.source_edit.setSizePolicy(size_policy)
        self.source_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.source_edit.setObjectName("source_edit")
        self.gridLayout_3.addWidget(self.source_edit, 13, 1, 1, 1)

        self.eval_button = QtWidgets.QPushButton(self.central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.eval_button.sizePolicy().hasHeightForWidth())
        self.eval_button.setSizePolicy(size_policy)
        self.eval_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.eval_button.setObjectName("eval_button")
        self.gridLayout_3.addWidget(self.eval_button, 14, 0, 1, 2)

        self.matplotlib_widget = MatplotlibWidget(self.central_widget)
        self.matplotlib_widget.setObjectName("matplotlib_widget")
        self.gridLayout_3.addWidget(self.matplotlib_widget, 0, 2, 15, 1)

        knapsack_problem.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(knapsack_problem)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 657, 21))
        self.menu_bar.setObjectName("menu_bar")
        self.file_menu = QtWidgets.QMenu(self.menu_bar)
        self.file_menu.setObjectName("file_menu")
        knapsack_problem.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(knapsack_problem)
        self.status_bar.setObjectName("status_bar")
        knapsack_problem.setStatusBar(self.status_bar)
        self.save_items_action = QtWidgets.QAction(knapsack_problem)
        self.save_items_action.setObjectName("save_items_action")
        self.load_items_action = QtWidgets.QAction(knapsack_problem)
        self.load_items_action.setObjectName("load_items_action")
        self.quit_action = QtWidgets.QAction(knapsack_problem)
        self.quit_action.setObjectName("quit_action")
        self.file_menu.addAction(self.save_items_action)
        self.file_menu.addAction(self.load_items_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.quit_action)
        self.menu_bar.addAction(self.file_menu.menuAction())

        self.retranslate_ui(knapsack_problem)
        self.quit_action.triggered.connect(knapsack_problem.close)
        self.add_button.clicked.connect(self.add_item)
        self.eval_button.clicked.connect(self.draw)
        self.remove_button.clicked.connect(self.remove_item)
        self.algo_combo_box.currentIndexChanged['int'].connect(self.change_algorithm)
        self.save_items_action.triggered.connect(knapsack_problem.show)
        self.load_items_action.triggered.connect(knapsack_problem.show)
        QtCore.QMetaObject.connectSlotsByName(knapsack_problem)

    @my_slot("bool")
    def draw(self, checked):
        try:
            if not self.capacity_edit.text():
                self.__show_warning__("Error", "Please provide capacity")
                return
            iterations = self.iteration_edit.text()
            if iterations:
                iterations = int(iterations)
            else:
                iterations = None
            source = self.source_edit.text()
            if source:
                source = [int(x) for x in list(source)]
            else:
                source = None
            if self.algo_combo_box.currentIndex() == 0:
                knapsack = KP.KnapsackEvolutionary(int(self.capacity_edit.text()), self.items_list, iterations, source)
            elif self.algo_combo_box.currentIndex() == 1:
                knapsack = KPC.KnapsackEvolutionaryCrossover(int(self.capacity_edit.text()),
                                                             self.items_list, iterations=iterations)
            generator = knapsack.evolve()
            n = []
            fit = []
            for i in generator:
                n.append(i[0])
                fit.append(i[1])
            n = n[:-knapsack.no_change]
            fit = fit[:-knapsack.no_change]

            self.matplotlib_widget.axis.clear()
            self.matplotlib_widget.axis.plot(n, fit)
            self.matplotlib_widget.axis.set_ylim([0, max(fit) + 1])
            self.matplotlib_widget.axis.grid(color='#AAAAAA', which='major', linestyle='-', linewidth=0.5)
            self.matplotlib_widget.axis.set_xticks(np.arange(1, len(n), int(len(n)/10)))
            self.matplotlib_widget.axis.set_yticks(list(set(fit)))
            self.matplotlib_widget.canvas.draw()
            self.__show_warning__("Finish", "Final chromosome is:\n%s" % (''.join([str(x) for x in knapsack.source])))
        except Exception as e:
            self.__show_warning__("Error", e.args[0])

    def change_algorithm(self):
        combo_box = self.sender()
        assert isinstance(combo_box, QtWidgets.QComboBox)
        index = combo_box.currentIndex()
        if index == 0:
            self.population_edit.setDisabled(True)
            self.population_edit.clear()
        elif index == 1:
            self.population_edit.setEnabled(True)

    def remove_item(self):
        root = self.items_tree.invisibleRootItem()
        for item in self.items_tree.selectedItems():
            (item.parent() or root).removeChild(item)
            weight, value = item.text(0), item.text(1)
            self.items_list.remove((int(weight), int(value)))

    def add_item(self):
        weight = self.weight_edit.text()
        value = self.value_edit.text()
        if not weight or not value:
            self.__show_warning__("Error", "Please fill weight and value")
            return
        new_item = QtWidgets.QTreeWidgetItem(self.items_tree)
        new_item.setText(0, weight)
        new_item.setText(1, value)
        self.items_list.append((int(weight), int(value)))
        self.weight_edit.clear()
        self.value_edit.clear()

    def __show_warning__(self, title, text):
        a = QtWidgets.QMessageBox()
        a.setWindowTitle(title)
        a.setText(text)
        a.exec_()

    # noinspection PyTypeChecker,PyArgumentList
    def retranslate_ui(self, knapsack_problem):
        _translate = QtCore.QCoreApplication.translate
        knapsack_problem.setWindowTitle(_translate("KnapsackProblem", "Knapsack Problem solver"))
        self.algo_combo_box.setItemText(0, _translate("KnapsackProblem", "Standard EA"))
        self.algo_combo_box.setItemText(1, _translate("KnapsackProblem", "Crossover + Elitism EA"))
        self.weight_label.setText(_translate("KnapsackProblem", "Weight"))
        self.add_button.setText(_translate("KnapsackProblem", "Add item"))
        self.eval_button.setText(_translate("KnapsackProblem", "Evaluate"))
        self.items_tree.headerItem().setText(0, _translate("KnapsackProblem", "Weight"))
        self.items_tree.headerItem().setText(1, _translate("KnapsackProblem", "Value"))
        __sortingEnabled = self.items_tree.isSortingEnabled()
        self.items_tree.setSortingEnabled(False)
        self.items_tree.setSortingEnabled(__sortingEnabled)
        self.population_label.setText(_translate("KnapsackProblem", "Population"))
        self.iteration_label.setText(_translate("KnapsackProblem", "Iterations"))
        self.remove_button.setText(_translate("KnapsackProblem", "Remove item"))
        self.value_label.setText(_translate("KnapsackProblem", "Value"))
        self.capacity_label.setText(_translate("KnapsackProblem", "Capacity"))
        self.source_label.setText(_translate("KnapsackProblem", "Source chromosome"))
        self.file_menu.setTitle(_translate("KnapsackProblem", "File"))
        self.save_items_action.setText(_translate("KnapsackProblem", "Save items"))
        self.save_items_action.setShortcut(_translate("KnapsackProblem", "Ctrl+S"))
        self.load_items_action.setText(_translate("KnapsackProblem", "Load items"))
        self.load_items_action.setShortcut(_translate("KnapsackProblem", "Ctrl+O"))
        self.quit_action.setText(_translate("KnapsackProblem", "Quit program"))
        self.quit_action.setShortcut(_translate("KnapsackProblem", "Esc"))


class MyApp(QtWidgets.QApplication):
    def notify(self, obj, event):
        isex = False
        try:
            return QtWidgets.QApplication.notify(self, obj, event)
        except Exception:
            isex = True
            print("Unexpected Error")
            print(traceback.format_exception(*sys.exc_info()))
            return False
        finally:
            if isex:
                self.quit()

if __name__ == "__main__":
    import sys
    app = MyApp(sys.argv)
    KnapsackProblem = QtWidgets.QMainWindow()
    ui = UiKnapsackProblem()
    ui.setup_ui(KnapsackProblem)
    KnapsackProblem.show()
    sys.exit(app.exec_())
