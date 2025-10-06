# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_campaign.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 510)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.lbl_bug = QLabel(Form)
        self.lbl_bug.setObjectName(u"lbl_bug")
        font = QFont()
        font.setPointSize(28)
        self.lbl_bug.setFont(font)
        self.lbl_bug.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_bug)

        self.tabBugs = QTabWidget(Form)
        self.tabBugs.setObjectName(u"tabBugs")
        self.tab_bug_info = QWidget()
        self.tab_bug_info.setObjectName(u"tab_bug_info")
        self.verticalLayout_2 = QVBoxLayout(self.tab_bug_info)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, -1, 5, -1)
        self.status_lbl = QLabel(self.tab_bug_info)
        self.status_lbl.setObjectName(u"status_lbl")

        self.horizontalLayout_2.addWidget(self.status_lbl)

        self.status_le = QLineEdit(self.tab_bug_info)
        self.status_le.setObjectName(u"status_le")
        self.status_le.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.horizontalLayout_2.addWidget(self.status_le)

        self.system_lbl = QLabel(self.tab_bug_info)
        self.system_lbl.setObjectName(u"system_lbl")

        self.horizontalLayout_2.addWidget(self.system_lbl)

        self.system_le = QLineEdit(self.tab_bug_info)
        self.system_le.setObjectName(u"system_le")

        self.horizontalLayout_2.addWidget(self.system_le)

        self.horizontalLayout_2.setStretch(1, 10)
        self.horizontalLayout_2.setStretch(3, 70)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, -1, 250, -1)
        self.sys_version_lbl = QLabel(self.tab_bug_info)
        self.sys_version_lbl.setObjectName(u"sys_version_lbl")

        self.horizontalLayout_3.addWidget(self.sys_version_lbl)

        self.comboBox = QComboBox(self.tab_bug_info)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.service_now_id_lbl = QLabel(self.tab_bug_info)
        self.service_now_id_lbl.setObjectName(u"service_now_id_lbl")

        self.horizontalLayout_3.addWidget(self.service_now_id_lbl)

        self.service_now_id_le = QLineEdit(self.tab_bug_info)
        self.service_now_id_le.setObjectName(u"service_now_id_le")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.service_now_id_le.sizePolicy().hasHeightForWidth())
        self.service_now_id_le.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.service_now_id_le)

        self.label = QLabel(self.tab_bug_info)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.listWidget_2 = QListWidget(self.tab_bug_info)
        self.listWidget_2.setObjectName(u"listWidget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy1)
        self.listWidget_2.setMaximumSize(QSize(240, 50))

        self.horizontalLayout_3.addWidget(self.listWidget_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tabBugs.addTab(self.tab_bug_info, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(4)

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.tabBugs.addTab(self.tab, "")
        self.tab_bug_history = QWidget()
        self.tab_bug_history.setObjectName(u"tab_bug_history")
        self.verticalLayout_4 = QVBoxLayout(self.tab_bug_history)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.tab_bug_history)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_4.addWidget(self.listWidget)

        self.tabBugs.addTab(self.tab_bug_history, "")

        self.verticalLayout.addWidget(self.tabBugs)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(200, -1, -1, -1)
        self.add_bug_button = QPushButton(Form)
        self.add_bug_button.setObjectName(u"add_bug_button")

        self.horizontalLayout.addWidget(self.add_bug_button)

        self.add_bug_button_2 = QPushButton(Form)
        self.add_bug_button_2.setObjectName(u"add_bug_button_2")

        self.horizontalLayout.addWidget(self.add_bug_button_2)

        self.add_bug_button_3 = QPushButton(Form)
        self.add_bug_button_3.setObjectName(u"add_bug_button_3")

        self.horizontalLayout.addWidget(self.add_bug_button_3)

        self.add_bug_button_4 = QPushButton(Form)
        self.add_bug_button_4.setObjectName(u"add_bug_button_4")

        self.horizontalLayout.addWidget(self.add_bug_button_4)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        self.tabBugs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_bug.setText(QCoreApplication.translate("Form", u"[Campaign name]", None))
        self.status_lbl.setText(QCoreApplication.translate("Form", u"Id:", None))
        self.status_le.setText("")
        self.status_le.setPlaceholderText(QCoreApplication.translate("Form", u"[Identification]", None))
        self.system_lbl.setText(QCoreApplication.translate("Form", u"Description:", None))
        self.system_le.setText("")
        self.system_le.setPlaceholderText(QCoreApplication.translate("Form", u"[Description]", None))
        self.sys_version_lbl.setText(QCoreApplication.translate("Form", u"System:", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Form", u"[System]", None))
        self.service_now_id_lbl.setText(QCoreApplication.translate("Form", u"Version:", None))
        self.service_now_id_le.setText("")
        self.service_now_id_le.setPlaceholderText(QCoreApplication.translate("Form", u"[Version]", None))
        self.label.setText(QCoreApplication.translate("Form", u"Test Blocks:", None))
        self.tabBugs.setTabText(self.tabBugs.indexOf(self.tab_bug_info), QCoreApplication.translate("Form", u"General Info", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Action", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Expected result", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Requirements affected", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"OK/NO OK", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Comments", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Files", None));
        self.tabBugs.setTabText(self.tabBugs.indexOf(self.tab), QCoreApplication.translate("Form", u"Steps", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"[Change in status:...]", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.tabBugs.setTabText(self.tabBugs.indexOf(self.tab_bug_history), QCoreApplication.translate("Form", u"History", None))
        self.add_bug_button.setText(QCoreApplication.translate("Form", u"Start/Continue Campaign", None))
        self.add_bug_button_2.setText(QCoreApplication.translate("Form", u"Edit campaign", None))
        self.add_bug_button_3.setText(QCoreApplication.translate("Form", u"Delete campaign", None))
        self.add_bug_button_4.setText(QCoreApplication.translate("Form", u"Back", None))
    # retranslateUi

