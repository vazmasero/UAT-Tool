# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_operator.ui'
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

class Ui_form_operator(object):
    def setupUi(self, form_operator):
        if not form_operator.objectName():
            form_operator.setObjectName(u"form_operator")
        form_operator.resize(571, 408)
        self.verticalLayout = QVBoxLayout(form_operator)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.hlayout_name = QHBoxLayout()
        self.hlayout_name.setSpacing(3)
        self.hlayout_name.setObjectName(u"hlayout_name")
        self.hlayout_name.setContentsMargins(5, -1, 250, -1)
        self.lbl_name = QLabel(form_operator)
        self.lbl_name.setObjectName(u"lbl_name")

        self.hlayout_name.addWidget(self.lbl_name)

        self.le_name = QLineEdit(form_operator)
        self.le_name.setObjectName(u"le_name")

        self.hlayout_name.addWidget(self.le_name)

        self.hlayout_name.setStretch(0, 5)
        self.hlayout_name.setStretch(1, 20)

        self.verticalLayout.addLayout(self.hlayout_name)

        self.hlayout_id = QHBoxLayout()
        self.hlayout_id.setObjectName(u"hlayout_id")
        self.hlayout_id.setContentsMargins(5, -1, 150, -1)
        self.lbl_id = QLabel(form_operator)
        self.lbl_id.setObjectName(u"lbl_id")

        self.hlayout_id.addWidget(self.lbl_id)

        self.le_easa_id = QLineEdit(form_operator)
        self.le_easa_id.setObjectName(u"le_easa_id")

        self.hlayout_id.addWidget(self.le_easa_id)

        self.lbl_verification = QLabel(form_operator)
        self.lbl_verification.setObjectName(u"lbl_verification")
        self.lbl_verification.setWordWrap(False)

        self.hlayout_id.addWidget(self.lbl_verification)

        self.le_verification_code = QLineEdit(form_operator)
        self.le_verification_code.setObjectName(u"le_verification_code")

        self.hlayout_id.addWidget(self.le_verification_code)


        self.verticalLayout.addLayout(self.hlayout_id)

        self.hlayout_email = QHBoxLayout()
        self.hlayout_email.setObjectName(u"hlayout_email")
        self.hlayout_email.setContentsMargins(5, -1, 5, -1)
        self.lbl_email = QLabel(form_operator)
        self.lbl_email.setObjectName(u"lbl_email")

        self.hlayout_email.addWidget(self.lbl_email)

        self.le_email = QLineEdit(form_operator)
        self.le_email.setObjectName(u"le_email")

        self.hlayout_email.addWidget(self.le_email)

        self.lbl_password = QLabel(form_operator)
        self.lbl_password.setObjectName(u"lbl_password")

        self.hlayout_email.addWidget(self.lbl_password)

        self.le_password = QLineEdit(form_operator)
        self.le_password.setObjectName(u"le_password")

        self.hlayout_email.addWidget(self.le_password)

        self.lbl_phone = QLabel(form_operator)
        self.lbl_phone.setObjectName(u"lbl_phone")

        self.hlayout_email.addWidget(self.lbl_phone)

        self.le_phone = QLineEdit(form_operator)
        self.le_phone.setObjectName(u"le_phone")

        self.hlayout_email.addWidget(self.le_phone)


        self.verticalLayout.addLayout(self.hlayout_email)

        self.hlayout_btn_operator = QHBoxLayout()
        self.hlayout_btn_operator.setObjectName(u"hlayout_btn_operator")
        self.hlayout_btn_operator.setContentsMargins(300, -1, -1, -1)
        self.btn_accept = QPushButton(form_operator)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_operator.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(form_operator)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_operator.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.hlayout_btn_operator)


        self.retranslateUi(form_operator)

        QMetaObject.connectSlotsByName(form_operator)
    # setupUi

    def retranslateUi(self, form_operator):
        form_operator.setWindowTitle(QCoreApplication.translate("form_operator", u"Form", None))
        self.lbl_name.setText(QCoreApplication.translate("form_operator", u"Name:", None))
        self.lbl_id.setText(QCoreApplication.translate("form_operator", u"EASA Id:", None))
        self.lbl_verification.setText(QCoreApplication.translate("form_operator", u"Verification code:", None))
        self.lbl_email.setText(QCoreApplication.translate("form_operator", u"Email:", None))
        self.lbl_password.setText(QCoreApplication.translate("form_operator", u"Password", None))
        self.lbl_phone.setText(QCoreApplication.translate("form_operator", u"Phone:", None))
        self.btn_accept.setText(QCoreApplication.translate("form_operator", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_operator", u"Cancel", None))
    # retranslateUi

