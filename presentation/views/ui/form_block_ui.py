# -*- coding: utf-8 -*-

##########################################################################
# Form generated from reading UI file 'form_block.ui'
##
# Created by: Qt User Interface Compiler version 6.9.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
##########################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
                               QLabel, QLineEdit, QListWidget, QListWidgetItem,
                               QPushButton, QSizePolicy, QTabWidget, QTableView,
                               QVBoxLayout, QWidget)


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
        self.hlayout_id.setContentsMargins(10, -1, 10, -1)
        self.lbl_identification = QLabel(self.tab_cases)
        self.lbl_identification.setObjectName(u"lbl_identification")

        self.hlayout_id.addWidget(self.lbl_identification)

        self.le_identification = QLineEdit(self.tab_cases)
        self.le_identification.setObjectName(u"le_identification")

        self.hlayout_id.addWidget(self.le_identification)

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
        self.cb_system.addItem("")
        self.cb_system.addItem("")
        self.cb_system.addItem("")
        self.cb_system.addItem("")
        self.cb_system.addItem("")
        self.cb_system.setObjectName(u"cb_system")

        self.hlayout_id.addWidget(self.cb_system)

        self.verticalLayout_2.addLayout(self.hlayout_id)

        self.hlayout_comments = QHBoxLayout()
        self.hlayout_comments.setObjectName(u"hlayout_comments")
        self.hlayout_comments.setContentsMargins(10, -1, 10, -1)
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
        self.tbl_cases = QTableView(self.tab_info)
        self.tbl_cases.setObjectName(u"tbl_cases")

        self.verticalLayout_3.addWidget(self.tbl_cases)

        self.lw_cases = QListWidget(self.tab_info)
        self.lw_cases.setObjectName(u"lw_cases")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lw_cases.sizePolicy().hasHeightForWidth())
        self.lw_cases.setSizePolicy(sizePolicy)
        self.lw_cases.setMinimumSize(QSize(600, 30))
        self.lw_cases.setMaximumSize(QSize(500, 40))

        self.verticalLayout_3.addWidget(self.lw_cases)

        self.hlayout_btn_case = QHBoxLayout()
        self.hlayout_btn_case.setObjectName(u"hlayout_btn_case")
        self.hlayout_btn_case.setContentsMargins(450, -1, -1, -1)

        self.verticalLayout_3.addLayout(self.hlayout_btn_case)

        self.tab_widget_block.addTab(self.tab_info, "")

        self.verticalLayout.addWidget(self.tab_widget_block)

        self.hlayout_btn_block = QHBoxLayout()
        self.hlayout_btn_block.setObjectName(u"hlayout_btn_block")
        self.hlayout_btn_block.setContentsMargins(400, -1, -1, -1)
        self.btn_accept = QPushButton(form_block)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_block.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(form_block)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_block.addWidget(self.btn_cancel)

        self.verticalLayout.addLayout(self.hlayout_btn_block)

        self.retranslateUi(form_block)

        self.tab_widget_block.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(form_block)
    # setupUi

    def retranslateUi(self, form_block):
        form_block.setWindowTitle(
            QCoreApplication.translate(
                "form_block", u"Form", None))
        self.lbl_block.setText(
            QCoreApplication.translate(
                "form_block",
                u"[New/Test Block #]",
                None))
        self.lbl_identification.setText(
            QCoreApplication.translate(
                "form_block", u"Id:", None))
        self.le_identification.setPlaceholderText(
            QCoreApplication.translate(
                "form_block", u"[Identifier]", None))
        self.lbl_name.setText(
            QCoreApplication.translate(
                "form_block", u"Name:", None))
        self.le_name.setText("")
        self.le_name.setPlaceholderText(
            QCoreApplication.translate(
                "form_block", u"[Name]", None))
        self.lbl_system.setText(
            QCoreApplication.translate(
                "form_block", u"System:", None))
        self.cb_system.setItemText(
            0, QCoreApplication.translate(
                "form_block", u"USSP", None))
        self.cb_system.setItemText(
            1, QCoreApplication.translate(
                "form_block", u"CISP", None))
        self.cb_system.setItemText(
            2, QCoreApplication.translate(
                "form_block", u"AUDI", None))
        self.cb_system.setItemText(
            3, QCoreApplication.translate(
                "form_block", u"EXCHANGE", None))
        self.cb_system.setItemText(
            4, QCoreApplication.translate(
                "form_block", u"NA", None))

        self.lbl_comments.setText(
            QCoreApplication.translate(
                "form_block", u"Comments:", None))
        self.le_comments.setText("")
        self.le_comments.setPlaceholderText(
            QCoreApplication.translate(
                "form_block", u"[Comments]", None))
        self.tab_widget_block.setTabText(
            self.tab_widget_block.indexOf(
                self.tab_cases), QCoreApplication.translate(
                "form_block", u"Block Info", None))
        self.tab_widget_block.setTabText(
            self.tab_widget_block.indexOf(
                self.tab_info), QCoreApplication.translate(
                "form_block", u"Cases", None))
        self.btn_accept.setText(
            QCoreApplication.translate(
                "form_block", u"Accept", None))
        self.btn_cancel.setText(
            QCoreApplication.translate(
                "form_block", u"Cancel", None))
    # retranslateUi
