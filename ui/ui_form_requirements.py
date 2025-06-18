# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_requirements.ui'
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
        form_requirement.resize(571, 408)
        self.verticalLayout = QVBoxLayout(form_requirement)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 39, -1)
        self.hlayout_id = QHBoxLayout()
        self.hlayout_id.setObjectName(u"hlayout_id")
        self.lbl_id = QLabel(form_requirement)
        self.lbl_id.setObjectName(u"lbl_id")

        self.hlayout_id.addWidget(self.lbl_id)

        self.le_id = QLineEdit(form_requirement)
        self.le_id.setObjectName(u"le_id")

        self.hlayout_id.addWidget(self.le_id)


        self.verticalLayout.addLayout(self.hlayout_id)

        self.hlayout_system = QHBoxLayout()
        self.hlayout_system.setObjectName(u"hlayout_system")
        self.lbl_system = QLabel(form_requirement)
        self.lbl_system.setObjectName(u"lbl_system")

        self.hlayout_system.addWidget(self.lbl_system)

        self.cb_system = QComboBox(form_requirement)
        self.cb_system.setObjectName(u"cb_system")

        self.hlayout_system.addWidget(self.cb_system)


        self.verticalLayout.addLayout(self.hlayout_system)

        self.hlayout_section = QHBoxLayout()
        self.hlayout_section.setObjectName(u"hlayout_section")
        self.lbl_section = QLabel(form_requirement)
        self.lbl_section.setObjectName(u"lbl_section")

        self.hlayout_section.addWidget(self.lbl_section)

        self.cb_section = QComboBox(form_requirement)
        self.cb_section.setObjectName(u"cb_section")

        self.hlayout_section.addWidget(self.cb_section)


        self.verticalLayout.addLayout(self.hlayout_section)

        self.hlayout_definition = QHBoxLayout()
        self.hlayout_definition.setObjectName(u"hlayout_definition")
        self.lbl_definition = QLabel(form_requirement)
        self.lbl_definition.setObjectName(u"lbl_definition")

        self.hlayout_definition.addWidget(self.lbl_definition)

        self.le_definition = QLineEdit(form_requirement)
        self.le_definition.setObjectName(u"le_definition")

        self.hlayout_definition.addWidget(self.le_definition)


        self.verticalLayout.addLayout(self.hlayout_definition)

        self.hlayout_btn_requirement = QHBoxLayout()
        self.hlayout_btn_requirement.setObjectName(u"hlayout_btn_requirement")
        self.hlayout_btn_requirement.setContentsMargins(300, -1, -1, -1)
        self.btn_accept = QPushButton(form_requirement)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_requirement.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(form_requirement)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_requirement.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.hlayout_btn_requirement)


        self.retranslateUi(form_requirement)

        QMetaObject.connectSlotsByName(form_requirement)
    # setupUi

    def retranslateUi(self, form_requirement):
        form_requirement.setWindowTitle(QCoreApplication.translate("form_requirement", u"Form", None))
        self.lbl_id.setText(QCoreApplication.translate("form_requirement", u"ID:", None))
        self.lbl_system.setText(QCoreApplication.translate("form_requirement", u"System:", None))
        self.lbl_section.setText(QCoreApplication.translate("form_requirement", u"Section", None))
        self.lbl_definition.setText(QCoreApplication.translate("form_requirement", u"Definition:", None))
        self.btn_accept.setText(QCoreApplication.translate("form_requirement", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_requirement", u"Cancel", None))
    # retranslateUi

