# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_uas_zone.ui'
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

class Ui_form_uas_zone(object):
    def setupUi(self, form_uas_zone):
        if not form_uas_zone.objectName():
            form_uas_zone.setObjectName(u"form_uas_zone")
        form_uas_zone.resize(571, 408)
        self.verticalLayout = QVBoxLayout(form_uas_zone)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.hlayout_name = QHBoxLayout()
        self.hlayout_name.setSpacing(3)
        self.hlayout_name.setObjectName(u"hlayout_name")
        self.hlayout_name.setContentsMargins(5, -1, 5, -1)
        self.lbl_name = QLabel(form_uas_zone)
        self.lbl_name.setObjectName(u"lbl_name")

        self.hlayout_name.addWidget(self.lbl_name)

        self.le_name = QLineEdit(form_uas_zone)
        self.le_name.setObjectName(u"le_name")

        self.hlayout_name.addWidget(self.le_name)

        self.lbl_reason = QLabel(form_uas_zone)
        self.lbl_reason.setObjectName(u"lbl_reason")

        self.hlayout_name.addWidget(self.lbl_reason)

        self.le_reason = QLineEdit(form_uas_zone)
        self.le_reason.setObjectName(u"le_reason")

        self.hlayout_name.addWidget(self.le_reason)


        self.verticalLayout.addLayout(self.hlayout_name)

        self.hlayout_cause = QHBoxLayout()
        self.hlayout_cause.setObjectName(u"hlayout_cause")
        self.hlayout_cause.setContentsMargins(5, -1, 5, -1)
        self.lbl_cause = QLabel(form_uas_zone)
        self.lbl_cause.setObjectName(u"lbl_cause")

        self.hlayout_cause.addWidget(self.lbl_cause)

        self.cb_cause = QComboBox(form_uas_zone)
        self.cb_cause.setObjectName(u"cb_cause")

        self.hlayout_cause.addWidget(self.cb_cause)

        self.lbl_restriction = QLabel(form_uas_zone)
        self.lbl_restriction.setObjectName(u"lbl_restriction")
        self.lbl_restriction.setWordWrap(False)

        self.hlayout_cause.addWidget(self.lbl_restriction)

        self.cb_restriction = QComboBox(form_uas_zone)
        self.cb_restriction.setObjectName(u"cb_restriction")

        self.hlayout_cause.addWidget(self.cb_restriction)

        self.hlayout_cause.setStretch(1, 5)
        self.hlayout_cause.setStretch(3, 5)

        self.verticalLayout.addLayout(self.hlayout_cause)

        self.hlayout_authority = QHBoxLayout()
        self.hlayout_authority.setObjectName(u"hlayout_authority")
        self.hlayout_authority.setContentsMargins(5, -1, 5, -1)
        self.lbl_authority = QLabel(form_uas_zone)
        self.lbl_authority.setObjectName(u"lbl_authority")

        self.hlayout_authority.addWidget(self.lbl_authority)

        self.cb_authority = QComboBox(form_uas_zone)
        self.cb_authority.setObjectName(u"cb_authority")

        self.hlayout_authority.addWidget(self.cb_authority)

        self.lbl_activation = QLabel(form_uas_zone)
        self.lbl_activation.setObjectName(u"lbl_activation")

        self.hlayout_authority.addWidget(self.lbl_activation)

        self.cb_activation = QComboBox(form_uas_zone)
        self.cb_activation.setObjectName(u"cb_activation")

        self.hlayout_authority.addWidget(self.cb_activation)

        self.hlayout_authority.setStretch(1, 5)
        self.hlayout_authority.setStretch(3, 5)

        self.verticalLayout.addLayout(self.hlayout_authority)

        self.hlayout_btn_uas_zone = QHBoxLayout()
        self.hlayout_btn_uas_zone.setObjectName(u"hlayout_btn_uas_zone")
        self.hlayout_btn_uas_zone.setContentsMargins(300, -1, -1, -1)
        self.btn_accept = QPushButton(form_uas_zone)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_uas_zone.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(form_uas_zone)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_uas_zone.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.hlayout_btn_uas_zone)


        self.retranslateUi(form_uas_zone)

        QMetaObject.connectSlotsByName(form_uas_zone)
    # setupUi

    def retranslateUi(self, form_uas_zone):
        form_uas_zone.setWindowTitle(QCoreApplication.translate("form_uas_zone", u"Form", None))
        self.lbl_name.setText(QCoreApplication.translate("form_uas_zone", u"Name:", None))
        self.lbl_reason.setText(QCoreApplication.translate("form_uas_zone", u"Reason:", None))
        self.lbl_cause.setText(QCoreApplication.translate("form_uas_zone", u"Cause:", None))
        self.lbl_restriction.setText(QCoreApplication.translate("form_uas_zone", u"Restriction type:", None))
        self.lbl_authority.setText(QCoreApplication.translate("form_uas_zone", u"Authority:", None))
        self.lbl_activation.setText(QCoreApplication.translate("form_uas_zone", u"Activation time:", None))
        self.btn_accept.setText(QCoreApplication.translate("form_uas_zone", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_uas_zone", u"Cancel", None))
    # retranslateUi

