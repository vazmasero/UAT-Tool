# -*- coding: utf-8 -*-

##########################################################################
# Form generated from reading UI file 'form_case.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
                               QLineEdit, QListWidget, QListWidgetItem, QPushButton,
                               QSizePolicy, QTabWidget, QTableView, QVBoxLayout,
                               QWidget)


class Ui_form_case(object):
    def setupUi(self, form_case):
        if not form_case.objectName():
            form_case.setObjectName(u"form_case")
        form_case.resize(717, 511)
        self.verticalLayout_2 = QVBoxLayout(form_case)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 10, 30, -1)
        self.lbl_case = QLabel(form_case)
        self.lbl_case.setObjectName(u"lbl_case")
        font = QFont()
        font.setPointSize(24)
        self.lbl_case.setFont(font)
        self.lbl_case.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lbl_case)

        self.tab_widget_case = QTabWidget(form_case)
        self.tab_widget_case.setObjectName(u"tab_widget_case")
        self.tab_info = QWidget()
        self.tab_info.setObjectName(u"tab_info")
        self.verticalLayout = QVBoxLayout(self.tab_info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.hlayout_id = QHBoxLayout()
        self.hlayout_id.setObjectName(u"hlayout_id")
        self.lbl_id = QLabel(self.tab_info)
        self.lbl_id.setObjectName(u"lbl_id")

        self.hlayout_id.addWidget(self.lbl_id)

        self.le_identification = QLineEdit(self.tab_info)
        self.le_identification.setObjectName(u"le_identification")

        self.hlayout_id.addWidget(self.le_identification)

        self.lbl_name = QLabel(self.tab_info)
        self.lbl_name.setObjectName(u"lbl_name")

        self.hlayout_id.addWidget(self.lbl_name)

        self.le_name = QLineEdit(self.tab_info)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.hlayout_id.addWidget(self.le_name)

        self.lbl_system = QLabel(self.tab_info)
        self.lbl_system.setObjectName(u"lbl_system")

        self.hlayout_id.addWidget(self.lbl_system)

        self.lw_system = QListWidget(self.tab_info)
        self.lw_system.setObjectName(u"lw_system")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lw_system.sizePolicy().hasHeightForWidth())
        self.lw_system.setSizePolicy(sizePolicy)
        self.lw_system.setMaximumSize(QSize(200, 40))

        self.hlayout_id.addWidget(self.lw_system)

        self.lbl_section = QLabel(self.tab_info)
        self.lbl_section.setObjectName(u"lbl_section")

        self.hlayout_id.addWidget(self.lbl_section)

        self.lw_section = QListWidget(self.tab_info)
        self.lw_section.setObjectName(u"lw_section")
        sizePolicy.setHeightForWidth(
            self.lw_section.sizePolicy().hasHeightForWidth())
        self.lw_section.setSizePolicy(sizePolicy)
        self.lw_section.setMaximumSize(QSize(200, 40))

        self.hlayout_id.addWidget(self.lw_section)

        self.verticalLayout.addLayout(self.hlayout_id)

        self.hlayout_operator = QHBoxLayout()
        self.hlayout_operator.setObjectName(u"hlayout_operator")
        self.hlayout_operator.setContentsMargins(-1, -1, 50, -1)
        self.lbl_operator = QLabel(self.tab_info)
        self.lbl_operator.setObjectName(u"lbl_operator")

        self.hlayout_operator.addWidget(self.lbl_operator)

        self.lw_operator = QListWidget(self.tab_info)
        self.lw_operator.setObjectName(u"lw_operator")
        sizePolicy.setHeightForWidth(
            self.lw_operator.sizePolicy().hasHeightForWidth())
        self.lw_operator.setSizePolicy(sizePolicy)
        self.lw_operator.setMaximumSize(QSize(250, 40))

        self.hlayout_operator.addWidget(self.lw_operator)

        self.lbl_drone = QLabel(self.tab_info)
        self.lbl_drone.setObjectName(u"lbl_drone")

        self.hlayout_operator.addWidget(self.lbl_drone)

        self.lw_drone = QListWidget(self.tab_info)
        self.lw_drone.setObjectName(u"lw_drone")
        sizePolicy.setHeightForWidth(
            self.lw_drone.sizePolicy().hasHeightForWidth())
        self.lw_drone.setSizePolicy(sizePolicy)
        self.lw_drone.setMaximumSize(QSize(250, 40))

        self.hlayout_operator.addWidget(self.lw_drone)

        self.lbl_uhub_user = QLabel(self.tab_info)
        self.lbl_uhub_user.setObjectName(u"lbl_uhub_user")

        self.hlayout_operator.addWidget(self.lbl_uhub_user)

        self.lw_uhub_user = QListWidget(self.tab_info)
        self.lw_uhub_user.setObjectName(u"lw_uhub_user")
        sizePolicy.setHeightForWidth(
            self.lw_uhub_user.sizePolicy().hasHeightForWidth())
        self.lw_uhub_user.setSizePolicy(sizePolicy)
        self.lw_uhub_user.setMaximumSize(QSize(250, 40))

        self.hlayout_operator.addWidget(self.lw_uhub_user)

        self.verticalLayout.addLayout(self.hlayout_operator)

        self.hlayout_comment = QHBoxLayout()
        self.hlayout_comment.setObjectName(u"hlayout_comment")
        self.lbl_comment = QLabel(self.tab_info)
        self.lbl_comment.setObjectName(u"lbl_comment")

        self.hlayout_comment.addWidget(self.lbl_comment)

        self.le_comment = QLineEdit(self.tab_info)
        self.le_comment.setObjectName(u"le_comment")

        self.hlayout_comment.addWidget(self.le_comment)

        self.verticalLayout.addLayout(self.hlayout_comment)

        self.tab_widget_case.addTab(self.tab_info, "")
        self.tab_steps = QWidget()
        self.tab_steps.setObjectName(u"tab_steps")
        self.horizontalLayout = QHBoxLayout(self.tab_steps)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tbl_steps = QTableView(self.tab_steps)
        self.tbl_steps.setObjectName(u"tbl_steps")

        self.horizontalLayout.addWidget(self.tbl_steps)

        self.vlayout_btn_steps = QVBoxLayout()
        self.vlayout_btn_steps.setSpacing(1)
        self.vlayout_btn_steps.setObjectName(u"vlayout_btn_steps")
        self.vlayout_btn_steps.setContentsMargins(-1, -1, -1, 300)
        self.btn_add_step = QPushButton(self.tab_steps)
        self.btn_add_step.setObjectName(u"btn_add_step")

        self.vlayout_btn_steps.addWidget(self.btn_add_step)

        self.btn_remove_step = QPushButton(self.tab_steps)
        self.btn_remove_step.setObjectName(u"btn_remove_step")

        self.vlayout_btn_steps.addWidget(self.btn_remove_step)

        self.horizontalLayout.addLayout(self.vlayout_btn_steps)

        self.tab_widget_case.addTab(self.tab_steps, "")

        self.verticalLayout_2.addWidget(self.tab_widget_case)

        self.hlayout_btn_case = QHBoxLayout()
        self.hlayout_btn_case.setObjectName(u"hlayout_btn_case")
        self.hlayout_btn_case.setContentsMargins(400, -1, -1, -1)
        self.btn_accept = QPushButton(form_case)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_case.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(form_case)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_case.addWidget(self.btn_cancel)

        self.verticalLayout_2.addLayout(self.hlayout_btn_case)

        self.retranslateUi(form_case)

        self.tab_widget_case.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(form_case)
    # setupUi

    def retranslateUi(self, form_case):
        form_case.setWindowTitle(
            QCoreApplication.translate(
                "form_case", u"Form", None))
        self.lbl_case.setText(
            QCoreApplication.translate(
                "form_case",
                u"[New/Test Case #]",
                None))
        self.lbl_id.setText(
            QCoreApplication.translate(
                "form_case", u"Id:", None))
        self.le_identification.setText("")
        self.le_identification.setPlaceholderText(
            QCoreApplication.translate("form_case", u"[Id]", None))
        self.lbl_name.setText(
            QCoreApplication.translate(
                "form_case", u"Name:", None))
        self.le_name.setText("")
        self.le_name.setPlaceholderText(
            QCoreApplication.translate(
                "form_case", u"[Name]", None))
        self.lbl_system.setText(
            QCoreApplication.translate(
                "form_case", u"System(s):", None))
        self.lbl_section.setText(
            QCoreApplication.translate(
                "form_case", u"Section(s):", None))
        self.lbl_operator.setText(
            QCoreApplication.translate(
                "form_case", u"Operator(s):", None))
        self.lbl_drone.setText(
            QCoreApplication.translate(
                "form_case", u"Drone(s):", None))
        self.lbl_uhub_user.setText(
            QCoreApplication.translate(
                "form_case", u"U-hub User(s)", None))
        self.lbl_comment.setText(
            QCoreApplication.translate(
                "form_case", u"Comments:", None))
        self.le_comment.setText("")
        self.le_comment.setPlaceholderText(
            QCoreApplication.translate(
                "form_case", u"[Comments]", None))
        self.tab_widget_case.setTabText(
            self.tab_widget_case.indexOf(
                self.tab_info), QCoreApplication.translate(
                "form_case", u"Case info", None))
        self.btn_add_step.setText(
            QCoreApplication.translate(
                "form_case", u"+", None))
        self.btn_remove_step.setText(
            QCoreApplication.translate(
                "form_case", u"-", None))
        self.tab_widget_case.setTabText(
            self.tab_widget_case.indexOf(
                self.tab_steps), QCoreApplication.translate(
                "form_case", u"Steps", None))
        self.btn_accept.setText(
            QCoreApplication.translate(
                "form_case", u"Accept", None))
        self.btn_cancel.setText(
            QCoreApplication.translate(
                "form_case", u"Cancel", None))
    # retranslateUi
