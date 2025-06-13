# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'requirements_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_requirement_form(object):
    def setupUi(self, requirement_form):
        if not requirement_form.objectName():
            requirement_form.setObjectName(u"requirement_form")
        requirement_form.resize(571, 408)
        self.layoutWidget = QWidget(requirement_form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 60, 411, 241))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.requirement_id_label = QLabel(self.layoutWidget)
        self.requirement_id_label.setObjectName(u"requirement_id_label")

        self.horizontalLayout_4.addWidget(self.requirement_id_label)

        self.requirement_id_input = QLineEdit(self.layoutWidget)
        self.requirement_id_input.setObjectName(u"requirement_id_input")

        self.horizontalLayout_4.addWidget(self.requirement_id_input)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.requirement_sec_label = QLabel(self.layoutWidget)
        self.requirement_sec_label.setObjectName(u"requirement_sec_label")

        self.horizontalLayout_3.addWidget(self.requirement_sec_label)

        self.requirement_sec_combo = QComboBox(self.layoutWidget)
        self.requirement_sec_combo.setObjectName(u"requirement_sec_combo")

        self.horizontalLayout_3.addWidget(self.requirement_sec_combo)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.requirement_sys_label = QLabel(self.layoutWidget)
        self.requirement_sys_label.setObjectName(u"requirement_sys_label")

        self.horizontalLayout_2.addWidget(self.requirement_sys_label)

        self.requirement_sys_combo = QComboBox(self.layoutWidget)
        self.requirement_sys_combo.setObjectName(u"requirement_sys_combo")

        self.horizontalLayout_2.addWidget(self.requirement_sys_combo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.requirement_def_label = QLabel(self.layoutWidget)
        self.requirement_def_label.setObjectName(u"requirement_def_label")

        self.horizontalLayout.addWidget(self.requirement_def_label)

        self.requirement_def_input = QLineEdit(self.layoutWidget)
        self.requirement_def_input.setObjectName(u"requirement_def_input")

        self.horizontalLayout.addWidget(self.requirement_def_input)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.layoutWidget1 = QWidget(requirement_form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(320, 310, 158, 26))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.accept_requirement = QPushButton(self.layoutWidget1)
        self.accept_requirement.setObjectName(u"accept_requirement")

        self.horizontalLayout_5.addWidget(self.accept_requirement)

        self.cancel_requirement = QPushButton(self.layoutWidget1)
        self.cancel_requirement.setObjectName(u"cancel_requirement")

        self.horizontalLayout_5.addWidget(self.cancel_requirement)


        self.retranslateUi(requirement_form)

        QMetaObject.connectSlotsByName(requirement_form)
    # setupUi

    def retranslateUi(self, requirement_form):
        requirement_form.setWindowTitle(QCoreApplication.translate("requirement_form", u"Form", None))
        self.requirement_id_label.setText(QCoreApplication.translate("requirement_form", u"Identifier:", None))
        self.requirement_sec_label.setText(QCoreApplication.translate("requirement_form", u"System:", None))
        self.requirement_sys_label.setText(QCoreApplication.translate("requirement_form", u"Section:", None))
        self.requirement_def_label.setText(QCoreApplication.translate("requirement_form", u"Definition:", None))
        self.accept_requirement.setText(QCoreApplication.translate("requirement_form", u"Accept", None))
        self.cancel_requirement.setText(QCoreApplication.translate("requirement_form", u"Cancel", None))
    # retranslateUi

