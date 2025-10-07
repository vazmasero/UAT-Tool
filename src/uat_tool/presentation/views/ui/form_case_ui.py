# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_case.ui'
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
        self.hlayout_code = QHBoxLayout()
        self.hlayout_code.setObjectName(u"hlayout_code")
        self.lbl_code = QLabel(self.tab_info)
        self.lbl_code.setObjectName(u"lbl_code")

        self.hlayout_code.addWidget(self.lbl_code)

        self.le_code = QLineEdit(self.tab_info)
        self.le_code.setObjectName(u"le_code")

        self.hlayout_code.addWidget(self.le_code)

        self.lbl_name = QLabel(self.tab_info)
        self.lbl_name.setObjectName(u"lbl_name")

        self.hlayout_code.addWidget(self.lbl_name)

        self.le_name = QLineEdit(self.tab_info)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.hlayout_code.addWidget(self.le_name)

        self.lbl_systems = QLabel(self.tab_info)
        self.lbl_systems.setObjectName(u"lbl_systems")

        self.hlayout_code.addWidget(self.lbl_systems)

        self.lw_systems = QListWidget(self.tab_info)
        self.lw_systems.setObjectName(u"lw_systems")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_systems.sizePolicy().hasHeightForWidth())
        self.lw_systems.setSizePolicy(sizePolicy)
        self.lw_systems.setMaximumSize(QSize(200, 40))

        self.hlayout_code.addWidget(self.lw_systems)

        self.lbl_sections = QLabel(self.tab_info)
        self.lbl_sections.setObjectName(u"lbl_sections")

        self.hlayout_code.addWidget(self.lbl_sections)

        self.lw_sections = QListWidget(self.tab_info)
        self.lw_sections.setObjectName(u"lw_sections")
        sizePolicy.setHeightForWidth(self.lw_sections.sizePolicy().hasHeightForWidth())
        self.lw_sections.setSizePolicy(sizePolicy)
        self.lw_sections.setMaximumSize(QSize(200, 40))

        self.hlayout_code.addWidget(self.lw_sections)


        self.verticalLayout.addLayout(self.hlayout_code)

        self.hlayout_operator = QHBoxLayout()
        self.hlayout_operator.setObjectName(u"hlayout_operator")
        self.hlayout_operator.setContentsMargins(-1, -1, 50, -1)
        self.lbl_operators = QLabel(self.tab_info)
        self.lbl_operators.setObjectName(u"lbl_operators")

        self.hlayout_operator.addWidget(self.lbl_operators)

        self.lw_operators = QListWidget(self.tab_info)
        self.lw_operators.setObjectName(u"lw_operators")
        sizePolicy.setHeightForWidth(self.lw_operators.sizePolicy().hasHeightForWidth())
        self.lw_operators.setSizePolicy(sizePolicy)
        self.lw_operators.setMaximumSize(QSize(250, 40))

        self.hlayout_operator.addWidget(self.lw_operators)

        self.lbl_drones = QLabel(self.tab_info)
        self.lbl_drones.setObjectName(u"lbl_drones")

        self.hlayout_operator.addWidget(self.lbl_drones)

        self.lw_drones = QListWidget(self.tab_info)
        self.lw_drones.setObjectName(u"lw_drones")
        sizePolicy.setHeightForWidth(self.lw_drones.sizePolicy().hasHeightForWidth())
        self.lw_drones.setSizePolicy(sizePolicy)
        self.lw_drones.setMaximumSize(QSize(250, 40))

        self.hlayout_operator.addWidget(self.lw_drones)

        self.lbl_uhub_users = QLabel(self.tab_info)
        self.lbl_uhub_users.setObjectName(u"lbl_uhub_users")

        self.hlayout_operator.addWidget(self.lbl_uhub_users)

        self.lw_uhub_users = QListWidget(self.tab_info)
        self.lw_uhub_users.setObjectName(u"lw_uhub_users")
        sizePolicy.setHeightForWidth(self.lw_uhub_users.sizePolicy().hasHeightForWidth())
        self.lw_uhub_users.setSizePolicy(sizePolicy)
        self.lw_uhub_users.setMaximumSize(QSize(250, 40))

        self.hlayout_operator.addWidget(self.lw_uhub_users)


        self.verticalLayout.addLayout(self.hlayout_operator)

        self.hlayout_comment = QHBoxLayout()
        self.hlayout_comment.setObjectName(u"hlayout_comment")
        self.lbl_comments = QLabel(self.tab_info)
        self.lbl_comments.setObjectName(u"lbl_comments")

        self.hlayout_comment.addWidget(self.lbl_comments)

        self.le_comments = QLineEdit(self.tab_info)
        self.le_comments.setObjectName(u"le_comments")

        self.hlayout_comment.addWidget(self.le_comments)


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
        form_case.setWindowTitle(QCoreApplication.translate("form_case", u"Form", None))
        self.lbl_case.setText(QCoreApplication.translate("form_case", u"[New/Test Case #]", None))
        self.lbl_code.setText(QCoreApplication.translate("form_case", u"Code:", None))
        self.le_code.setText("")
        self.le_code.setPlaceholderText(QCoreApplication.translate("form_case", u"[Code]", None))
        self.lbl_name.setText(QCoreApplication.translate("form_case", u"Name:", None))
        self.le_name.setText("")
        self.le_name.setPlaceholderText(QCoreApplication.translate("form_case", u"[Name]", None))
        self.lbl_systems.setText(QCoreApplication.translate("form_case", u"System(s):", None))
        self.lbl_sections.setText(QCoreApplication.translate("form_case", u"Section(s):", None))
        self.lbl_operators.setText(QCoreApplication.translate("form_case", u"Operator(s):", None))
        self.lbl_drones.setText(QCoreApplication.translate("form_case", u"Drone(s):", None))
        self.lbl_uhub_users.setText(QCoreApplication.translate("form_case", u"U-hub User(s)", None))
        self.lbl_comments.setText(QCoreApplication.translate("form_case", u"Comments:", None))
        self.le_comments.setText("")
        self.le_comments.setPlaceholderText(QCoreApplication.translate("form_case", u"[Comments]", None))
        self.tab_widget_case.setTabText(self.tab_widget_case.indexOf(self.tab_info), QCoreApplication.translate("form_case", u"Case info", None))
        self.btn_add_step.setText(QCoreApplication.translate("form_case", u"+", None))
        self.btn_remove_step.setText(QCoreApplication.translate("form_case", u"-", None))
        self.tab_widget_case.setTabText(self.tab_widget_case.indexOf(self.tab_steps), QCoreApplication.translate("form_case", u"Steps", None))
        self.btn_accept.setText(QCoreApplication.translate("form_case", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_case", u"Cancel", None))
    # retranslateUi

