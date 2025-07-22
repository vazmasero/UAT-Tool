# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_uhub_org.ui'
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

class Ui_form_uhub_org(object):
    def setupUi(self, form_uhub_org):
        if not form_uhub_org.objectName():
            form_uhub_org.setObjectName(u"form_uhub_org")
        form_uhub_org.resize(571, 408)
        self.verticalLayout = QVBoxLayout(form_uhub_org)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.hlayout_name = QHBoxLayout()
        self.hlayout_name.setSpacing(3)
        self.hlayout_name.setObjectName(u"hlayout_name")
        self.hlayout_name.setContentsMargins(5, -1, 5, -1)
        self.lbl_name = QLabel(form_uhub_org)
        self.lbl_name.setObjectName(u"lbl_name")

        self.hlayout_name.addWidget(self.lbl_name)

        self.le_name = QLineEdit(form_uhub_org)
        self.le_name.setObjectName(u"le_name")

        self.hlayout_name.addWidget(self.le_name)

        self.lbl_email = QLabel(form_uhub_org)
        self.lbl_email.setObjectName(u"lbl_email")

        self.hlayout_name.addWidget(self.lbl_email)

        self.le_email = QLineEdit(form_uhub_org)
        self.le_email.setObjectName(u"le_email")

        self.hlayout_name.addWidget(self.le_email)

        self.lbl_phone = QLabel(form_uhub_org)
        self.lbl_phone.setObjectName(u"lbl_phone")

        self.hlayout_name.addWidget(self.lbl_phone)

        self.le_phone = QLineEdit(form_uhub_org)
        self.le_phone.setObjectName(u"le_phone")

        self.hlayout_name.addWidget(self.le_phone)


        self.verticalLayout.addLayout(self.hlayout_name)

        self.hlayout_role = QHBoxLayout()
        self.hlayout_role.setObjectName(u"hlayout_role")
        self.hlayout_role.setContentsMargins(5, -1, 5, -1)
        self.lbl_role = QLabel(form_uhub_org)
        self.lbl_role.setObjectName(u"lbl_role")

        self.hlayout_role.addWidget(self.lbl_role)

        self.le_role = QLineEdit(form_uhub_org)
        self.le_role.setObjectName(u"le_role")

        self.hlayout_role.addWidget(self.le_role)

        self.lbl_jurisdiction = QLabel(form_uhub_org)
        self.lbl_jurisdiction.setObjectName(u"lbl_jurisdiction")
        self.lbl_jurisdiction.setWordWrap(False)

        self.hlayout_role.addWidget(self.lbl_jurisdiction)

        self.le_jurisdiction = QLineEdit(form_uhub_org)
        self.le_jurisdiction.setObjectName(u"le_jurisdiction")

        self.hlayout_role.addWidget(self.le_jurisdiction)

        self.lbl_aoi = QLabel(form_uhub_org)
        self.lbl_aoi.setObjectName(u"lbl_aoi")

        self.hlayout_role.addWidget(self.lbl_aoi)

        self.le_aoi = QLineEdit(form_uhub_org)
        self.le_aoi.setObjectName(u"le_aoi")

        self.hlayout_role.addWidget(self.le_aoi)


        self.verticalLayout.addLayout(self.hlayout_role)

        self.hlayout_btn_uhub_org = QHBoxLayout()
        self.hlayout_btn_uhub_org.setObjectName(u"hlayout_btn_uhub_org")
        self.hlayout_btn_uhub_org.setContentsMargins(300, -1, -1, -1)
        self.btn_accept = QPushButton(form_uhub_org)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_uhub_org.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(form_uhub_org)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_uhub_org.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.hlayout_btn_uhub_org)


        self.retranslateUi(form_uhub_org)

        QMetaObject.connectSlotsByName(form_uhub_org)
    # setupUi

    def retranslateUi(self, form_uhub_org):
        form_uhub_org.setWindowTitle(QCoreApplication.translate("form_uhub_org", u"Form", None))
        self.lbl_name.setText(QCoreApplication.translate("form_uhub_org", u"Name:", None))
        self.lbl_email.setText(QCoreApplication.translate("form_uhub_org", u"Email:", None))
        self.lbl_phone.setText(QCoreApplication.translate("form_uhub_org", u"Phone:", None))
        self.lbl_role.setText(QCoreApplication.translate("form_uhub_org", u"Role:", None))
        self.lbl_jurisdiction.setText(QCoreApplication.translate("form_uhub_org", u"Jurisdiction:", None))
        self.lbl_aoi.setText(QCoreApplication.translate("form_uhub_org", u"AoI:", None))
        self.btn_accept.setText(QCoreApplication.translate("form_uhub_org", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_uhub_org", u"Cancel", None))
    # retranslateUi

