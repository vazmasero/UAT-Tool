# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_email.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_form_email(object):
    def setupUi(self, form_email):
        if not form_email.objectName():
            form_email.setObjectName(u"form_email")
        form_email.resize(571, 408)
        self.verticalLayout = QVBoxLayout(form_email)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.hlayout_name = QHBoxLayout()
        self.hlayout_name.setObjectName(u"hlayout_name")
        self.hlayout_name.setContentsMargins(5, -1, 150, -1)
        self.lbl_name = QLabel(form_email)
        self.lbl_name.setObjectName(u"lbl_name")

        self.hlayout_name.addWidget(self.lbl_name)

        self.le_name = QLineEdit(form_email)
        self.le_name.setObjectName(u"le_name")

        self.hlayout_name.addWidget(self.le_name)

        self.lbl_email = QLabel(form_email)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setWordWrap(False)

        self.hlayout_name.addWidget(self.lbl_email)

        self.le_email = QLineEdit(form_email)
        self.le_email.setObjectName(u"le_email")

        self.hlayout_name.addWidget(self.le_email)


        self.verticalLayout.addLayout(self.hlayout_name)

        self.hlayout_password = QHBoxLayout()
        self.hlayout_password.setObjectName(u"hlayout_password")
        self.hlayout_password.setContentsMargins(5, -1, 150, -1)
        self.lbl_password = QLabel(form_email)
        self.lbl_password.setObjectName(u"lbl_password")

        self.hlayout_password.addWidget(self.lbl_password)

        self.le_password = QLineEdit(form_email)
        self.le_password.setObjectName(u"le_password")

        self.hlayout_password.addWidget(self.le_password)


        self.verticalLayout.addLayout(self.hlayout_password)

        self.hlayout_btn = QHBoxLayout()
        self.hlayout_btn.setObjectName(u"hlayout_btn")
        self.hlayout_btn.setContentsMargins(300, -1, -1, -1)
        self.btn_accept = QPushButton(form_email)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(form_email)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.hlayout_btn)


        self.retranslateUi(form_email)

        QMetaObject.connectSlotsByName(form_email)
    # setupUi

    def retranslateUi(self, form_email):
        form_email.setWindowTitle(QCoreApplication.translate("form_email", u"Form", None))
        self.lbl_name.setText(QCoreApplication.translate("form_email", u"Name:", None))
        self.lbl_email.setText(QCoreApplication.translate("form_email", u"Email:", None))
        self.lbl_password.setText(QCoreApplication.translate("form_email", u"Password:", None))
        self.btn_accept.setText(QCoreApplication.translate("form_email", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_email", u"Cancel", None))
    # retranslateUi

