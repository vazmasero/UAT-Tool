# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_uhub_user.ui'
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

class Ui_form_uhub_user_form(object):
    def setupUi(self, form_uhub_user_form):
        if not form_uhub_user_form.objectName():
            form_uhub_user_form.setObjectName(u"form_uhub_user_form")
        form_uhub_user_form.resize(571, 408)
        self.verticalLayout = QVBoxLayout(form_uhub_user_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.hlayout_username = QHBoxLayout()
        self.hlayout_username.setSpacing(3)
        self.hlayout_username.setObjectName(u"hlayout_username")
        self.hlayout_username.setContentsMargins(5, -1, 5, -1)
        self.lbl_username = QLabel(form_uhub_user_form)
        self.lbl_username.setObjectName(u"lbl_username")

        self.hlayout_username.addWidget(self.lbl_username)

        self.le_username = QLineEdit(form_uhub_user_form)
        self.le_username.setObjectName(u"le_username")

        self.hlayout_username.addWidget(self.le_username)

        self.lbl_email = QLabel(form_uhub_user_form)
        self.lbl_email.setObjectName(u"lbl_email")

        self.hlayout_username.addWidget(self.lbl_email)

        self.le_email = QLineEdit(form_uhub_user_form)
        self.le_email.setObjectName(u"le_email")

        self.hlayout_username.addWidget(self.le_email)

        self.lbl_password = QLabel(form_uhub_user_form)
        self.lbl_password.setObjectName(u"lbl_password")

        self.hlayout_username.addWidget(self.lbl_password)

        self.le_password = QLineEdit(form_uhub_user_form)
        self.le_password.setObjectName(u"le_password")

        self.hlayout_username.addWidget(self.le_password)


        self.verticalLayout.addLayout(self.hlayout_username)

        self.hlayout_org = QHBoxLayout()
        self.hlayout_org.setObjectName(u"hlayout_org")
        self.hlayout_org.setContentsMargins(5, -1, 5, -1)
        self.lbl_org = QLabel(form_uhub_user_form)
        self.lbl_org.setObjectName(u"lbl_org")

        self.hlayout_org.addWidget(self.lbl_org)

        self.cb_org = QComboBox(form_uhub_user_form)
        self.cb_org.setObjectName(u"cb_org")

        self.hlayout_org.addWidget(self.cb_org)

        self.lbl_role = QLabel(form_uhub_user_form)
        self.lbl_role.setObjectName(u"lbl_role")

        self.hlayout_org.addWidget(self.lbl_role)

        self.cb_role = QComboBox(form_uhub_user_form)
        self.cb_role.setObjectName(u"cb_role")

        self.hlayout_org.addWidget(self.cb_role)


        self.verticalLayout.addLayout(self.hlayout_org)

        self.hlayout_jurisdiction = QHBoxLayout()
        self.hlayout_jurisdiction.setObjectName(u"hlayout_jurisdiction")
        self.lbl_jurisdiction = QLabel(form_uhub_user_form)
        self.lbl_jurisdiction.setObjectName(u"lbl_jurisdiction")
        self.lbl_jurisdiction.setWordWrap(False)

        self.hlayout_jurisdiction.addWidget(self.lbl_jurisdiction)

        self.cb_jurisdiction = QComboBox(form_uhub_user_form)
        self.cb_jurisdiction.setObjectName(u"cb_jurisdiction")

        self.hlayout_jurisdiction.addWidget(self.cb_jurisdiction)

        self.lbl_aoi = QLabel(form_uhub_user_form)
        self.lbl_aoi.setObjectName(u"lbl_aoi")

        self.hlayout_jurisdiction.addWidget(self.lbl_aoi)

        self.cb_aoi = QComboBox(form_uhub_user_form)
        self.cb_aoi.setObjectName(u"cb_aoi")

        self.hlayout_jurisdiction.addWidget(self.cb_aoi)


        self.verticalLayout.addLayout(self.hlayout_jurisdiction)

        self.hlayout_btn_uhub_user = QHBoxLayout()
        self.hlayout_btn_uhub_user.setObjectName(u"hlayout_btn_uhub_user")
        self.hlayout_btn_uhub_user.setContentsMargins(300, -1, -1, -1)
        self.btn_accept = QPushButton(form_uhub_user_form)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_uhub_user.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(form_uhub_user_form)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_uhub_user.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.hlayout_btn_uhub_user)


        self.retranslateUi(form_uhub_user_form)

        QMetaObject.connectSlotsByName(form_uhub_user_form)
    # setupUi

    def retranslateUi(self, form_uhub_user_form):
        form_uhub_user_form.setWindowTitle(QCoreApplication.translate("form_uhub_user_form", u"Form", None))
        self.lbl_username.setText(QCoreApplication.translate("form_uhub_user_form", u"Username:", None))
        self.lbl_email.setText(QCoreApplication.translate("form_uhub_user_form", u"Email:", None))
        self.lbl_password.setText(QCoreApplication.translate("form_uhub_user_form", u"Password:", None))
        self.lbl_org.setText(QCoreApplication.translate("form_uhub_user_form", u"Organization", None))
        self.lbl_role.setText(QCoreApplication.translate("form_uhub_user_form", u"Role:", None))
        self.lbl_jurisdiction.setText(QCoreApplication.translate("form_uhub_user_form", u"Jurisdiction:", None))
        self.lbl_aoi.setText(QCoreApplication.translate("form_uhub_user_form", u"AoI:", None))
        self.btn_accept.setText(QCoreApplication.translate("form_uhub_user_form", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_uhub_user_form", u"Cancel", None))
    # retranslateUi

