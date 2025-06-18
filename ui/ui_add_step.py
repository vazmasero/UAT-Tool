# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_step.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_form_requirement(object):
    def setupUi(self, form_requirement):
        if not form_requirement.objectName():
            form_requirement.setObjectName(u"form_requirement")
        form_requirement.resize(572, 408)
        self.verticalLayout = QVBoxLayout(form_requirement)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.hlayout_action = QHBoxLayout()
        self.hlayout_action.setObjectName(u"hlayout_action")
        self.hlayout_action.setContentsMargins(5, -1, 5, -1)
        self.lbl_action = QLabel(form_requirement)
        self.lbl_action.setObjectName(u"lbl_action")

        self.hlayout_action.addWidget(self.lbl_action)

        self.le_action = QLineEdit(form_requirement)
        self.le_action.setObjectName(u"le_action")

        self.hlayout_action.addWidget(self.le_action)


        self.verticalLayout.addLayout(self.hlayout_action)

        self.hlayout_expected = QHBoxLayout()
        self.hlayout_expected.setObjectName(u"hlayout_expected")
        self.hlayout_expected.setContentsMargins(5, -1, 5, -1)
        self.lbl_expected = QLabel(form_requirement)
        self.lbl_expected.setObjectName(u"lbl_expected")

        self.hlayout_expected.addWidget(self.lbl_expected)

        self.le_expected = QLineEdit(form_requirement)
        self.le_expected.setObjectName(u"le_expected")

        self.hlayout_expected.addWidget(self.le_expected)


        self.verticalLayout.addLayout(self.hlayout_expected)

        self.hlayout_requirement = QHBoxLayout()
        self.hlayout_requirement.setObjectName(u"hlayout_requirement")
        self.hlayout_requirement.setContentsMargins(5, -1, 300, -1)
        self.b_requirement = QLabel(form_requirement)
        self.b_requirement.setObjectName(u"b_requirement")

        self.hlayout_requirement.addWidget(self.b_requirement)

        self.cb_requirement = QComboBox(form_requirement)
        self.cb_requirement.setObjectName(u"cb_requirement")

        self.hlayout_requirement.addWidget(self.cb_requirement)

        self.hlayout_requirement.setStretch(1, 30)

        self.verticalLayout.addLayout(self.hlayout_requirement)

        self.hlayout_comment = QHBoxLayout()
        self.hlayout_comment.setObjectName(u"hlayout_comment")
        self.hlayout_comment.setContentsMargins(5, -1, 5, -1)
        self.lbl_comment = QLabel(form_requirement)
        self.lbl_comment.setObjectName(u"lbl_comment")

        self.hlayout_comment.addWidget(self.lbl_comment)

        self.le_comment = QLineEdit(form_requirement)
        self.le_comment.setObjectName(u"le_comment")

        self.hlayout_comment.addWidget(self.le_comment)


        self.verticalLayout.addLayout(self.hlayout_comment)

        self.hlayout_btn_step = QHBoxLayout()
        self.hlayout_btn_step.setObjectName(u"hlayout_btn_step")
        self.hlayout_btn_step.setContentsMargins(300, -1, -1, 0)
        self.btn_add_step = QPushButton(form_requirement)
        self.btn_add_step.setObjectName(u"btn_add_step")

        self.hlayout_btn_step.addWidget(self.btn_add_step)

        self.btn_cancel = QPushButton(form_requirement)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_step.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.hlayout_btn_step)


        self.retranslateUi(form_requirement)

        QMetaObject.connectSlotsByName(form_requirement)
    # setupUi

    def retranslateUi(self, form_requirement):
        form_requirement.setWindowTitle(QCoreApplication.translate("form_requirement", u"Form", None))
        self.lbl_action.setText(QCoreApplication.translate("form_requirement", u"Action:", None))
        self.lbl_expected.setText(QCoreApplication.translate("form_requirement", u"Expected result:", None))
        self.b_requirement.setText(QCoreApplication.translate("form_requirement", u"Affected requirements:", None))
        self.lbl_comment.setText(QCoreApplication.translate("form_requirement", u"Comments:", None))
        self.btn_add_step.setText(QCoreApplication.translate("form_requirement", u"Add", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_requirement", u"Cancel", None))
    # retranslateUi

