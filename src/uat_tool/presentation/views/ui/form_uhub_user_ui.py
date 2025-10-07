# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_uhub_user.ui'
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

class Ui_form_uhub_user(object):
    def setupUi(self, form_uhub_user):
        if not form_uhub_user.objectName():
            form_uhub_user.setObjectName(u"form_uhub_user")
        form_uhub_user.resize(571, 407)
        self.verticalLayout = QVBoxLayout(form_uhub_user)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.hlayout_username = QHBoxLayout()
        self.hlayout_username.setSpacing(3)
        self.hlayout_username.setObjectName(u"hlayout_username")
        self.hlayout_username.setContentsMargins(5, -1, 5, -1)
        self.lbl_username = QLabel(form_uhub_user)
        self.lbl_username.setObjectName(u"lbl_username")

        self.hlayout_username.addWidget(self.lbl_username)

        self.le_username = QLineEdit(form_uhub_user)
        self.le_username.setObjectName(u"le_username")

        self.hlayout_username.addWidget(self.le_username)

        self.lbl_email = QLabel(form_uhub_user)
        self.lbl_email.setObjectName(u"lbl_email")

        self.hlayout_username.addWidget(self.lbl_email)

        self.le_email = QLineEdit(form_uhub_user)
        self.le_email.setObjectName(u"le_email")

        self.hlayout_username.addWidget(self.le_email)

        self.lbl_password = QLabel(form_uhub_user)
        self.lbl_password.setObjectName(u"lbl_password")

        self.hlayout_username.addWidget(self.lbl_password)

        self.le_password = QLineEdit(form_uhub_user)
        self.le_password.setObjectName(u"le_password")

        self.hlayout_username.addWidget(self.le_password)


        self.verticalLayout.addLayout(self.hlayout_username)

        self.hlayout_dni = QHBoxLayout()
        self.hlayout_dni.setObjectName(u"hlayout_dni")
        self.lbl_dni = QLabel(form_uhub_user)
        self.lbl_dni.setObjectName(u"lbl_dni")

        self.hlayout_dni.addWidget(self.lbl_dni)

        self.le_dni = QLineEdit(form_uhub_user)
        self.le_dni.setObjectName(u"le_dni")

        self.hlayout_dni.addWidget(self.le_dni)

        self.lbl_phone = QLabel(form_uhub_user)
        self.lbl_phone.setObjectName(u"lbl_phone")

        self.hlayout_dni.addWidget(self.lbl_phone)

        self.le_phone = QLineEdit(form_uhub_user)
        self.le_phone.setObjectName(u"le_phone")

        self.hlayout_dni.addWidget(self.le_phone)

        self.lbl_type = QLabel(form_uhub_user)
        self.lbl_type.setObjectName(u"lbl_type")

        self.hlayout_dni.addWidget(self.lbl_type)

        self.cb_type = QComboBox(form_uhub_user)
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.setObjectName(u"cb_type")

        self.hlayout_dni.addWidget(self.cb_type)


        self.verticalLayout.addLayout(self.hlayout_dni)

        self.hlayout_org = QHBoxLayout()
        self.hlayout_org.setObjectName(u"hlayout_org")
        self.hlayout_org.setContentsMargins(5, -1, 5, -1)
        self.lbl_organization = QLabel(form_uhub_user)
        self.lbl_organization.setObjectName(u"lbl_organization")

        self.hlayout_org.addWidget(self.lbl_organization)

        self.cb_organization = QComboBox(form_uhub_user)
        self.cb_organization.setObjectName(u"cb_organization")

        self.hlayout_org.addWidget(self.cb_organization)

        self.lbl_role = QLabel(form_uhub_user)
        self.lbl_role.setObjectName(u"lbl_role")

        self.hlayout_org.addWidget(self.lbl_role)

        self.le_role = QLineEdit(form_uhub_user)
        self.le_role.setObjectName(u"le_role")

        self.hlayout_org.addWidget(self.le_role)


        self.verticalLayout.addLayout(self.hlayout_org)

        self.hlayout_jurisdiction = QHBoxLayout()
        self.hlayout_jurisdiction.setObjectName(u"hlayout_jurisdiction")
        self.lbl_jurisdiction = QLabel(form_uhub_user)
        self.lbl_jurisdiction.setObjectName(u"lbl_jurisdiction")
        self.lbl_jurisdiction.setWordWrap(False)

        self.hlayout_jurisdiction.addWidget(self.lbl_jurisdiction)

        self.le_jurisdiction = QLineEdit(form_uhub_user)
        self.le_jurisdiction.setObjectName(u"le_jurisdiction")

        self.hlayout_jurisdiction.addWidget(self.le_jurisdiction)

        self.lbl_aoi = QLabel(form_uhub_user)
        self.lbl_aoi.setObjectName(u"lbl_aoi")

        self.hlayout_jurisdiction.addWidget(self.lbl_aoi)

        self.le_aoi = QLineEdit(form_uhub_user)
        self.le_aoi.setObjectName(u"le_aoi")

        self.hlayout_jurisdiction.addWidget(self.le_aoi)


        self.verticalLayout.addLayout(self.hlayout_jurisdiction)

        self.hlayout_btn_uhub_user = QHBoxLayout()
        self.hlayout_btn_uhub_user.setObjectName(u"hlayout_btn_uhub_user")
        self.hlayout_btn_uhub_user.setContentsMargins(300, -1, -1, -1)
        self.btn_accept = QPushButton(form_uhub_user)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_uhub_user.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(form_uhub_user)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_uhub_user.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.hlayout_btn_uhub_user)


        self.retranslateUi(form_uhub_user)

        QMetaObject.connectSlotsByName(form_uhub_user)
    # setupUi

    def retranslateUi(self, form_uhub_user):
        form_uhub_user.setWindowTitle(QCoreApplication.translate("form_uhub_user", u"Form", None))
        self.lbl_username.setText(QCoreApplication.translate("form_uhub_user", u"Username:", None))
        self.lbl_email.setText(QCoreApplication.translate("form_uhub_user", u"Email:", None))
        self.lbl_password.setText(QCoreApplication.translate("form_uhub_user", u"Password:", None))
        self.lbl_dni.setText(QCoreApplication.translate("form_uhub_user", u"DNI: ", None))
        self.lbl_phone.setText(QCoreApplication.translate("form_uhub_user", u"Phone: ", None))
        self.lbl_type.setText(QCoreApplication.translate("form_uhub_user", u"Type: ", None))
        self.cb_type.setItemText(0, QCoreApplication.translate("form_uhub_user", u"ADMIN", None))
        self.cb_type.setItemText(1, QCoreApplication.translate("form_uhub_user", u"USER", None))

        self.lbl_organization.setText(QCoreApplication.translate("form_uhub_user", u"Organization", None))
        self.lbl_role.setText(QCoreApplication.translate("form_uhub_user", u"Role:", None))
        self.lbl_jurisdiction.setText(QCoreApplication.translate("form_uhub_user", u"Jurisdiction:", None))
        self.lbl_aoi.setText(QCoreApplication.translate("form_uhub_user", u"AoI:", None))
        self.btn_accept.setText(QCoreApplication.translate("form_uhub_user", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_uhub_user", u"Cancel", None))
    # retranslateUi

