# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_uas_zone.ui'
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
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

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

        self.lbl_orgs = QLabel(form_uas_zone)
        self.lbl_orgs.setObjectName(u"lbl_orgs")

        self.hlayout_name.addWidget(self.lbl_orgs)

        self.lw_orgs = QListWidget(form_uas_zone)
        self.lw_orgs.setObjectName(u"lw_orgs")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_orgs.sizePolicy().hasHeightForWidth())
        self.lw_orgs.setSizePolicy(sizePolicy)
        self.lw_orgs.setMaximumSize(QSize(200, 40))

        self.hlayout_name.addWidget(self.lw_orgs)


        self.verticalLayout.addLayout(self.hlayout_name)

        self.hlayout_area_type = QHBoxLayout()
        self.hlayout_area_type.setObjectName(u"hlayout_area_type")
        self.lbl_area_type = QLabel(form_uas_zone)
        self.lbl_area_type.setObjectName(u"lbl_area_type")

        self.hlayout_area_type.addWidget(self.lbl_area_type)

        self.cb_area_type = QComboBox(form_uas_zone)
        self.cb_area_type.addItem("")
        self.cb_area_type.addItem("")
        self.cb_area_type.addItem("")
        self.cb_area_type.setObjectName(u"cb_area_type")

        self.hlayout_area_type.addWidget(self.cb_area_type)

        self.lbl_radius = QLabel(form_uas_zone)
        self.lbl_radius.setObjectName(u"lbl_radius")

        self.hlayout_area_type.addWidget(self.lbl_radius)

        self.le_radius = QLineEdit(form_uas_zone)
        self.le_radius.setObjectName(u"le_radius")

        self.hlayout_area_type.addWidget(self.le_radius)

        self.lbl_width = QLabel(form_uas_zone)
        self.lbl_width.setObjectName(u"lbl_width")

        self.hlayout_area_type.addWidget(self.lbl_width)

        self.le_width = QLineEdit(form_uas_zone)
        self.le_width.setObjectName(u"le_width")

        self.hlayout_area_type.addWidget(self.le_width)


        self.verticalLayout.addLayout(self.hlayout_area_type)

        self.hlayout_lower_limit = QHBoxLayout()
        self.hlayout_lower_limit.setObjectName(u"hlayout_lower_limit")
        self.lbl_lower_limit = QLabel(form_uas_zone)
        self.lbl_lower_limit.setObjectName(u"lbl_lower_limit")

        self.hlayout_lower_limit.addWidget(self.lbl_lower_limit)

        self.le_lower_limit = QLineEdit(form_uas_zone)
        self.le_lower_limit.setObjectName(u"le_lower_limit")

        self.hlayout_lower_limit.addWidget(self.le_lower_limit)

        self.lbl_reference_lower = QLabel(form_uas_zone)
        self.lbl_reference_lower.setObjectName(u"lbl_reference_lower")

        self.hlayout_lower_limit.addWidget(self.lbl_reference_lower)

        self.cb_reference_lower = QComboBox(form_uas_zone)
        self.cb_reference_lower.addItem("")
        self.cb_reference_lower.addItem("")
        self.cb_reference_lower.setObjectName(u"cb_reference_lower")

        self.hlayout_lower_limit.addWidget(self.cb_reference_lower)

        self.lbl_upper_limit = QLabel(form_uas_zone)
        self.lbl_upper_limit.setObjectName(u"lbl_upper_limit")

        self.hlayout_lower_limit.addWidget(self.lbl_upper_limit)

        self.le_upper_limit = QLineEdit(form_uas_zone)
        self.le_upper_limit.setObjectName(u"le_upper_limit")

        self.hlayout_lower_limit.addWidget(self.le_upper_limit)

        self.lbl_reference_upper = QLabel(form_uas_zone)
        self.lbl_reference_upper.setObjectName(u"lbl_reference_upper")

        self.hlayout_lower_limit.addWidget(self.lbl_reference_upper)

        self.cb_reference_upper = QComboBox(form_uas_zone)
        self.cb_reference_upper.addItem("")
        self.cb_reference_upper.addItem("")
        self.cb_reference_upper.setObjectName(u"cb_reference_upper")

        self.hlayout_lower_limit.addWidget(self.cb_reference_upper)


        self.verticalLayout.addLayout(self.hlayout_lower_limit)

        self.hlayout_cause = QHBoxLayout()
        self.hlayout_cause.setObjectName(u"hlayout_cause")
        self.hlayout_cause.setContentsMargins(5, -1, 5, -1)
        self.lbl_restriction_type = QLabel(form_uas_zone)
        self.lbl_restriction_type.setObjectName(u"lbl_restriction_type")
        self.lbl_restriction_type.setWordWrap(False)

        self.hlayout_cause.addWidget(self.lbl_restriction_type)

        self.cb_restriction_type = QComboBox(form_uas_zone)
        self.cb_restriction_type.addItem("")
        self.cb_restriction_type.addItem("")
        self.cb_restriction_type.addItem("")
        self.cb_restriction_type.addItem("")
        self.cb_restriction_type.setObjectName(u"cb_restriction_type")

        self.hlayout_cause.addWidget(self.cb_restriction_type)

        self.lbl_reason = QLabel(form_uas_zone)
        self.lbl_reason.setObjectName(u"lbl_reason")

        self.hlayout_cause.addWidget(self.lbl_reason)

        self.lw_reasons = QListWidget(form_uas_zone)
        self.lw_reasons.setObjectName(u"lw_reasons")
        sizePolicy.setHeightForWidth(self.lw_reasons.sizePolicy().hasHeightForWidth())
        self.lw_reasons.setSizePolicy(sizePolicy)
        self.lw_reasons.setMaximumSize(QSize(150, 40))

        self.hlayout_cause.addWidget(self.lw_reasons)

        self.lbl_application = QLabel(form_uas_zone)
        self.lbl_application.setObjectName(u"lbl_application")

        self.hlayout_cause.addWidget(self.lbl_application)

        self.cb_application = QComboBox(form_uas_zone)
        self.cb_application.addItem("")
        self.cb_application.addItem("")
        self.cb_application.setObjectName(u"cb_application")

        self.hlayout_cause.addWidget(self.cb_application)


        self.verticalLayout.addLayout(self.hlayout_cause)

        self.hlayout_authority = QHBoxLayout()
        self.hlayout_authority.setObjectName(u"hlayout_authority")
        self.hlayout_authority.setContentsMargins(5, -1, 5, -1)
        self.lbl_message = QLabel(form_uas_zone)
        self.lbl_message.setObjectName(u"lbl_message")

        self.hlayout_authority.addWidget(self.lbl_message)

        self.le_message = QLineEdit(form_uas_zone)
        self.le_message.setObjectName(u"le_message")

        self.hlayout_authority.addWidget(self.le_message)

        self.lbl_clearance = QLabel(form_uas_zone)
        self.lbl_clearance.setObjectName(u"lbl_clearance")

        self.hlayout_authority.addWidget(self.lbl_clearance)

        self.cb_clearance = QComboBox(form_uas_zone)
        self.cb_clearance.addItem("")
        self.cb_clearance.addItem("")
        self.cb_clearance.setObjectName(u"cb_clearance")

        self.hlayout_authority.addWidget(self.cb_clearance)


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
        self.lbl_orgs.setText(QCoreApplication.translate("form_uas_zone", u"Organizations:", None))
        self.lbl_area_type.setText(QCoreApplication.translate("form_uas_zone", u"Area type: ", None))
        self.cb_area_type.setItemText(0, QCoreApplication.translate("form_uas_zone", u"POLYGON", None))
        self.cb_area_type.setItemText(1, QCoreApplication.translate("form_uas_zone", u"CIRCLE", None))
        self.cb_area_type.setItemText(2, QCoreApplication.translate("form_uas_zone", u"CORRIDOR", None))

        self.lbl_radius.setText(QCoreApplication.translate("form_uas_zone", u"Circle radius: ", None))
        self.lbl_width.setText(QCoreApplication.translate("form_uas_zone", u"Corridor width: ", None))
        self.lbl_lower_limit.setText(QCoreApplication.translate("form_uas_zone", u"Lower limit: ", None))
        self.lbl_reference_lower.setText(QCoreApplication.translate("form_uas_zone", u"Reference: ", None))
        self.cb_reference_lower.setItemText(0, QCoreApplication.translate("form_uas_zone", u"AGL", None))
        self.cb_reference_lower.setItemText(1, QCoreApplication.translate("form_uas_zone", u"AMSL", None))

        self.lbl_upper_limit.setText(QCoreApplication.translate("form_uas_zone", u"Upper limit: ", None))
        self.lbl_reference_upper.setText(QCoreApplication.translate("form_uas_zone", u"Reference", None))
        self.cb_reference_upper.setItemText(0, QCoreApplication.translate("form_uas_zone", u"AGL", None))
        self.cb_reference_upper.setItemText(1, QCoreApplication.translate("form_uas_zone", u"AMSL", None))

        self.lbl_restriction_type.setText(QCoreApplication.translate("form_uas_zone", u"Restriction type:", None))
        self.cb_restriction_type.setItemText(0, QCoreApplication.translate("form_uas_zone", u"INFORMATIVE", None))
        self.cb_restriction_type.setItemText(1, QCoreApplication.translate("form_uas_zone", u"PROHIBITED", None))
        self.cb_restriction_type.setItemText(2, QCoreApplication.translate("form_uas_zone", u"REQ.AUTHORISATION", None))
        self.cb_restriction_type.setItemText(3, QCoreApplication.translate("form_uas_zone", u"CONDITIONAL", None))

        self.lbl_reason.setText(QCoreApplication.translate("form_uas_zone", u"Reason:", None))
        self.lbl_application.setText(QCoreApplication.translate("form_uas_zone", u"Application time: ", None))
        self.cb_application.setItemText(0, QCoreApplication.translate("form_uas_zone", u"TEMPORAL", None))
        self.cb_application.setItemText(1, QCoreApplication.translate("form_uas_zone", u"PERMANENT", None))

        self.lbl_message.setText(QCoreApplication.translate("form_uas_zone", u"Message: ", None))
        self.lbl_clearance.setText(QCoreApplication.translate("form_uas_zone", u"Clearance:", None))
        self.cb_clearance.setItemText(0, QCoreApplication.translate("form_uas_zone", u"YES", None))
        self.cb_clearance.setItemText(1, QCoreApplication.translate("form_uas_zone", u"NO", None))

        self.btn_accept.setText(QCoreApplication.translate("form_uas_zone", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_uas_zone", u"Cancel", None))
    # retranslateUi

