# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'requirements_page.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(760, 563)
        self.home_page_title = QLabel(Form)
        self.home_page_title.setObjectName(u"home_page_title")
        self.home_page_title.setGeometry(QRect(40, 20, 231, 71))
        font = QFont()
        font.setPointSize(26)
        self.home_page_title.setFont(font)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 90, 531, 24))
        self.searchfilter_layout = QHBoxLayout(self.layoutWidget)
        self.searchfilter_layout.setObjectName(u"searchfilter_layout")
        self.searchfilter_layout.setContentsMargins(0, 0, 0, 0)
        self.searchBug_bar = QLineEdit(self.layoutWidget)
        self.searchBug_bar.setObjectName(u"searchBug_bar")
        self.searchBug_bar.setClearButtonEnabled(True)

        self.searchfilter_layout.addWidget(self.searchBug_bar)

        self.spacerSearch_bar = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.searchfilter_layout.addItem(self.spacerSearch_bar)

        self.filterby_label = QLabel(self.layoutWidget)
        self.filterby_label.setObjectName(u"filterby_label")
        font1 = QFont()
        font1.setPointSize(10)
        self.filterby_label.setFont(font1)

        self.searchfilter_layout.addWidget(self.filterby_label)

        self.filterSystem = QComboBox(self.layoutWidget)
        self.filterSystem.setObjectName(u"filterSystem")
        self.filterSystem.setEditable(True)

        self.searchfilter_layout.addWidget(self.filterSystem)

        self.visor_bugs = QTableWidget(Form)
        if (self.visor_bugs.columnCount() < 6):
            self.visor_bugs.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.visor_bugs.rowCount() < 4):
            self.visor_bugs.setRowCount(4)
        self.visor_bugs.setObjectName(u"visor_bugs")
        self.visor_bugs.setGeometry(QRect(40, 130, 681, 361))
        self.visor_bugs.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.visor_bugs.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.visor_bugs.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.visor_bugs.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed|QAbstractItemView.EditTrigger.SelectedClicked)
        self.visor_bugs.setShowGrid(True)
        self.visor_bugs.setGridStyle(Qt.PenStyle.SolidLine)
        self.visor_bugs.setSortingEnabled(False)
        self.visor_bugs.setWordWrap(True)
        self.visor_bugs.setCornerButtonEnabled(False)
        self.visor_bugs.setRowCount(4)
        self.visor_bugs.setColumnCount(6)
        self.visor_bugs.horizontalHeader().setVisible(True)
        self.visor_bugs.horizontalHeader().setCascadingSectionResizes(True)
        self.visor_bugs.horizontalHeader().setHighlightSections(True)
        self.visor_bugs.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.visor_bugs.horizontalHeader().setStretchLastSection(False)
        self.layoutWidget_2 = QWidget(Form)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(390, 510, 329, 26))
        self.homeButton_Layout = QHBoxLayout(self.layoutWidget_2)
        self.homeButton_Layout.setObjectName(u"homeButton_Layout")
        self.homeButton_Layout.setContentsMargins(0, 0, 0, 0)
        self.add_bug_button = QPushButton(self.layoutWidget_2)
        self.add_bug_button.setObjectName(u"add_bug_button")

        self.homeButton_Layout.addWidget(self.add_bug_button)

        self.edit_bug_button = QPushButton(self.layoutWidget_2)
        self.edit_bug_button.setObjectName(u"edit_bug_button")

        self.homeButton_Layout.addWidget(self.edit_bug_button)

        self.remove_bug_button = QPushButton(self.layoutWidget_2)
        self.remove_bug_button.setObjectName(u"remove_bug_button")

        self.homeButton_Layout.addWidget(self.remove_bug_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.home_page_title.setText(QCoreApplication.translate("Form", u"Requirements", None))
        self.searchBug_bar.setPlaceholderText(QCoreApplication.translate("Form", u"Search by ID...", None))
        self.filterby_label.setText(QCoreApplication.translate("Form", u"Filter by:", None))
        self.filterSystem.setPlaceholderText(QCoreApplication.translate("Form", u"System", None))
        ___qtablewidgetitem = self.visor_bugs.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.visor_bugs.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"System", None));
        ___qtablewidgetitem2 = self.visor_bugs.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Section", None));
        ___qtablewidgetitem3 = self.visor_bugs.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Definition", None));
        ___qtablewidgetitem4 = self.visor_bugs.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Creation date", None));
        ___qtablewidgetitem5 = self.visor_bugs.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Last update", None));
        self.add_bug_button.setText(QCoreApplication.translate("Form", u"Add", None))
        self.edit_bug_button.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.remove_bug_button.setText(QCoreApplication.translate("Form", u"Remove", None))
    # retranslateUi

