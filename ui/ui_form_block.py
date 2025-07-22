# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_block.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_form_block(object):
    def setupUi(self, form_block):
        if not form_block.objectName():
            form_block.setObjectName(u"form_block")
        form_block.resize(717, 511)
        self.verticalLayout = QVBoxLayout(form_block)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, 10)
        self.lbl_block = QLabel(form_block)
        self.lbl_block.setObjectName(u"lbl_block")
        font = QFont()
        font.setPointSize(24)
        self.lbl_block.setFont(font)
        self.lbl_block.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_block)

        self.tab_widget_block = QTabWidget(form_block)
        self.tab_widget_block.setObjectName(u"tab_widget_block")
        self.tab_cases = QWidget()
        self.tab_cases.setObjectName(u"tab_cases")
        self.verticalLayout_2 = QVBoxLayout(self.tab_cases)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.hlayout_id = QHBoxLayout()
        self.hlayout_id.setObjectName(u"hlayout_id")
        self.lbl_id = QLabel(self.tab_cases)
        self.lbl_id.setObjectName(u"lbl_id")

        self.hlayout_id.addWidget(self.lbl_id)

        self.le_id = QLineEdit(self.tab_cases)
        self.le_id.setObjectName(u"le_id")

        self.hlayout_id.addWidget(self.le_id)

        self.lbl_name = QLabel(self.tab_cases)
        self.lbl_name.setObjectName(u"lbl_name")

        self.hlayout_id.addWidget(self.lbl_name)

        self.le_name = QLineEdit(self.tab_cases)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.hlayout_id.addWidget(self.le_name)

        self.lbl_system = QLabel(self.tab_cases)
        self.lbl_system.setObjectName(u"lbl_system")

        self.hlayout_id.addWidget(self.lbl_system)

        self.cb_system = QComboBox(self.tab_cases)
        self.cb_system.setObjectName(u"cb_system")

        self.hlayout_id.addWidget(self.cb_system)


        self.verticalLayout_2.addLayout(self.hlayout_id)

        self.hlayout_date = QHBoxLayout()
        self.hlayout_date.setObjectName(u"hlayout_date")
        self.lbl_creation = QLabel(self.tab_cases)
        self.lbl_creation.setObjectName(u"lbl_creation")

        self.hlayout_date.addWidget(self.lbl_creation)

        self.le_creation = QLineEdit(self.tab_cases)
        self.le_creation.setObjectName(u"le_creation")

        self.hlayout_date.addWidget(self.le_creation)

        self.lbl_update = QLabel(self.tab_cases)
        self.lbl_update.setObjectName(u"lbl_update")

        self.hlayout_date.addWidget(self.lbl_update)

        self.le_update = QLineEdit(self.tab_cases)
        self.le_update.setObjectName(u"le_update")

        self.hlayout_date.addWidget(self.le_update)


        self.verticalLayout_2.addLayout(self.hlayout_date)

        self.hlayout_comments = QHBoxLayout()
        self.hlayout_comments.setObjectName(u"hlayout_comments")
        self.lbl_comments = QLabel(self.tab_cases)
        self.lbl_comments.setObjectName(u"lbl_comments")

        self.hlayout_comments.addWidget(self.lbl_comments)

        self.le_comments = QLineEdit(self.tab_cases)
        self.le_comments.setObjectName(u"le_comments")

        self.hlayout_comments.addWidget(self.le_comments)


        self.verticalLayout_2.addLayout(self.hlayout_comments)

        self.tab_widget_block.addTab(self.tab_cases, "")
        self.tab_info = QWidget()
        self.tab_info.setObjectName(u"tab_info")
        self.verticalLayout_3 = QVBoxLayout(self.tab_info)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tbl_cases = QTableWidget(self.tab_info)
        if (self.tbl_cases.columnCount() < 6):
            self.tbl_cases.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_cases.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_cases.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_cases.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_cases.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_cases.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_cases.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tbl_cases.rowCount() < 4):
            self.tbl_cases.setRowCount(4)
        self.tbl_cases.setObjectName(u"tbl_cases")
        self.tbl_cases.setRowCount(4)

        self.verticalLayout_3.addWidget(self.tbl_cases)

        self.hlayout_btn_case = QHBoxLayout()
        self.hlayout_btn_case.setObjectName(u"hlayout_btn_case")
        self.hlayout_btn_case.setContentsMargins(450, -1, -1, -1)
        self.btn_add_case = QPushButton(self.tab_info)
        self.btn_add_case.setObjectName(u"btn_add_case")

        self.hlayout_btn_case.addWidget(self.btn_add_case)

        self.btn_remove_case = QPushButton(self.tab_info)
        self.btn_remove_case.setObjectName(u"btn_remove_case")

        self.hlayout_btn_case.addWidget(self.btn_remove_case)


        self.verticalLayout_3.addLayout(self.hlayout_btn_case)

        self.tab_widget_block.addTab(self.tab_info, "")

        self.verticalLayout.addWidget(self.tab_widget_block)

        self.hlayout_btn_block = QHBoxLayout()
        self.hlayout_btn_block.setObjectName(u"hlayout_btn_block")
        self.hlayout_btn_block.setContentsMargins(400, -1, -1, -1)
        self.btn_back = QPushButton(form_block)
        self.btn_back.setObjectName(u"btn_back")

        self.hlayout_btn_block.addWidget(self.btn_back)

        self.btn_accept = QPushButton(form_block)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_block.addWidget(self.btn_accept)


        self.verticalLayout.addLayout(self.hlayout_btn_block)


        self.retranslateUi(form_block)

        self.tab_widget_block.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(form_block)
    # setupUi

    def retranslateUi(self, form_block):
        form_block.setWindowTitle(QCoreApplication.translate("form_block", u"Form", None))
        self.lbl_block.setText(QCoreApplication.translate("form_block", u"[New/Test Block #]", None))
        self.lbl_id.setText(QCoreApplication.translate("form_block", u"Id:", None))
        self.le_id.setPlaceholderText(QCoreApplication.translate("form_block", u"[Identificator]", None))
        self.lbl_name.setText(QCoreApplication.translate("form_block", u"Name:", None))
        self.le_name.setText("")
        self.le_name.setPlaceholderText(QCoreApplication.translate("form_block", u"[Name]", None))
        self.lbl_system.setText(QCoreApplication.translate("form_block", u"System:", None))
        self.lbl_creation.setText(QCoreApplication.translate("form_block", u"Creation time:", None))
        self.le_creation.setText("")
        self.le_creation.setPlaceholderText(QCoreApplication.translate("form_block", u"[Creation time]", None))
        self.lbl_update.setText(QCoreApplication.translate("form_block", u"Last update:", None))
        self.le_update.setText("")
        self.le_update.setPlaceholderText(QCoreApplication.translate("form_block", u"[Update time]", None))
        self.lbl_comments.setText(QCoreApplication.translate("form_block", u"Comments:", None))
        self.le_comments.setText("")
        self.le_comments.setPlaceholderText(QCoreApplication.translate("form_block", u"[Comments]", None))
        self.tab_widget_block.setTabText(self.tab_widget_block.indexOf(self.tab_cases), QCoreApplication.translate("form_block", u"Block Info", None))
        ___qtablewidgetitem = self.tbl_cases.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("form_block", u"Name", None));
        ___qtablewidgetitem1 = self.tbl_cases.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("form_block", u"Id", None));
        ___qtablewidgetitem2 = self.tbl_cases.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("form_block", u"Assets", None));
        ___qtablewidgetitem3 = self.tbl_cases.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("form_block", u"Comments", None));
        ___qtablewidgetitem4 = self.tbl_cases.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("form_block", u"Added", None));
        ___qtablewidgetitem5 = self.tbl_cases.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("form_block", u"Last updated", None));
        self.btn_add_case.setText(QCoreApplication.translate("form_block", u"+", None))
        self.btn_remove_case.setText(QCoreApplication.translate("form_block", u"-", None))
        self.tab_widget_block.setTabText(self.tab_widget_block.indexOf(self.tab_info), QCoreApplication.translate("form_block", u"Cases", None))
        self.btn_back.setText(QCoreApplication.translate("form_block", u"Accept", None))
        self.btn_accept.setText(QCoreApplication.translate("form_block", u"Back", None))
    # retranslateUi

