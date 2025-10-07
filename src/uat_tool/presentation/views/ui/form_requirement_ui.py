# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_requirement.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_form_requirement(object):
    def setupUi(self, form_requirement):
        if not form_requirement.objectName():
            form_requirement.setObjectName(u"form_requirement")
        form_requirement.resize(571, 408)
        self.verticalLayout = QVBoxLayout(form_requirement)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 39, -1)
        self.hlayout_code = QHBoxLayout()
        self.hlayout_code.setObjectName(u"hlayout_code")
        self.lbl_code = QLabel(form_requirement)
        self.lbl_code.setObjectName(u"lbl_code")

        self.hlayout_code.addWidget(self.lbl_code)

        self.le_code = QLineEdit(form_requirement)
        self.le_code.setObjectName(u"le_code")

        self.hlayout_code.addWidget(self.le_code)


        self.verticalLayout.addLayout(self.hlayout_code)

        self.hlayout_systems = QHBoxLayout()
        self.hlayout_systems.setObjectName(u"hlayout_systems")
        self.lbl_systems = QLabel(form_requirement)
        self.lbl_systems.setObjectName(u"lbl_systems")

        self.hlayout_systems.addWidget(self.lbl_systems)

        self.lw_systems = QListWidget(form_requirement)
        self.lw_systems.setObjectName(u"lw_systems")
        self.lw_systems.setMinimumSize(QSize(200, 30))
        self.lw_systems.setMaximumSize(QSize(300, 50))

        self.hlayout_systems.addWidget(self.lw_systems)


        self.verticalLayout.addLayout(self.hlayout_systems)

        self.hlayout_sections = QHBoxLayout()
        self.hlayout_sections.setObjectName(u"hlayout_sections")
        self.lbl_sections = QLabel(form_requirement)
        self.lbl_sections.setObjectName(u"lbl_sections")

        self.hlayout_sections.addWidget(self.lbl_sections)

        self.lw_sections = QListWidget(form_requirement)
        self.lw_sections.setObjectName(u"lw_sections")
        self.lw_sections.setMinimumSize(QSize(200, 40))
        self.lw_sections.setMaximumSize(QSize(300, 50))

        self.hlayout_sections.addWidget(self.lw_sections)


        self.verticalLayout.addLayout(self.hlayout_sections)

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
        self.lbl_code.setText(QCoreApplication.translate("form_requirement", u"Code*:", None))
        self.lbl_systems.setText(QCoreApplication.translate("form_requirement", u"System(s):", None))
        self.lbl_sections.setText(QCoreApplication.translate("form_requirement", u"Section(s):", None))
        self.lbl_definition.setText(QCoreApplication.translate("form_requirement", u"Definition*:", None))
        self.btn_accept.setText(QCoreApplication.translate("form_requirement", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_requirement", u"Cancel", None))
    # retranslateUi

