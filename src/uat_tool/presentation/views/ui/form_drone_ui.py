# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_drone.ui'
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

class Ui_form_drone(object):
    def setupUi(self, form_drone):
        if not form_drone.objectName():
            form_drone.setObjectName(u"form_drone")
        form_drone.resize(571, 408)
        self.verticalLayout = QVBoxLayout(form_drone)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.hlayout_operator = QHBoxLayout()
        self.hlayout_operator.setSpacing(3)
        self.hlayout_operator.setObjectName(u"hlayout_operator")
        self.hlayout_operator.setContentsMargins(5, -1, 250, -1)
        self.lbl_operator = QLabel(form_drone)
        self.lbl_operator.setObjectName(u"lbl_operator")

        self.hlayout_operator.addWidget(self.lbl_operator)

        self.cb_operator = QComboBox(form_drone)
        self.cb_operator.setObjectName(u"cb_operator")

        self.hlayout_operator.addWidget(self.cb_operator)

        self.hlayout_operator.setStretch(0, 5)

        self.verticalLayout.addLayout(self.hlayout_operator)

        self.hlayout_name = QHBoxLayout()
        self.hlayout_name.setObjectName(u"hlayout_name")
        self.hlayout_name.setContentsMargins(5, -1, 150, -1)
        self.lbl_name = QLabel(form_drone)
        self.lbl_name.setObjectName(u"lbl_name")

        self.hlayout_name.addWidget(self.lbl_name)

        self.le_name = QLineEdit(form_drone)
        self.le_name.setObjectName(u"le_name")

        self.hlayout_name.addWidget(self.le_name)

        self.lbl_sn = QLabel(form_drone)
        self.lbl_sn.setObjectName(u"lbl_sn")
        self.lbl_sn.setWordWrap(False)

        self.hlayout_name.addWidget(self.lbl_sn)

        self.le_sn = QLineEdit(form_drone)
        self.le_sn.setObjectName(u"le_sn")

        self.hlayout_name.addWidget(self.le_sn)


        self.verticalLayout.addLayout(self.hlayout_name)

        self.hlayout_manufacturer = QHBoxLayout()
        self.hlayout_manufacturer.setObjectName(u"hlayout_manufacturer")
        self.hlayout_manufacturer.setContentsMargins(5, -1, 200, -1)
        self.lbl_manufacturer = QLabel(form_drone)
        self.lbl_manufacturer.setObjectName(u"lbl_manufacturer")

        self.hlayout_manufacturer.addWidget(self.lbl_manufacturer)

        self.le_manufacturer = QLineEdit(form_drone)
        self.le_manufacturer.setObjectName(u"le_manufacturer")

        self.hlayout_manufacturer.addWidget(self.le_manufacturer)

        self.lbl_model = QLabel(form_drone)
        self.lbl_model.setObjectName(u"lbl_model")

        self.hlayout_manufacturer.addWidget(self.lbl_model)

        self.le_model = QLineEdit(form_drone)
        self.le_model.setObjectName(u"le_model")

        self.hlayout_manufacturer.addWidget(self.le_model)


        self.verticalLayout.addLayout(self.hlayout_manufacturer)

        self.hlayout_tracker = QHBoxLayout()
        self.hlayout_tracker.setObjectName(u"hlayout_tracker")
        self.hlayout_tracker.setContentsMargins(5, -1, 150, -1)
        self.lbl_tracker_type = QLabel(form_drone)
        self.lbl_tracker_type.setObjectName(u"lbl_tracker_type")

        self.hlayout_tracker.addWidget(self.lbl_tracker_type)

        self.cb_tracker_type = QComboBox(form_drone)
        self.cb_tracker_type.addItem("")
        self.cb_tracker_type.addItem("")
        self.cb_tracker_type.setObjectName(u"cb_tracker_type")

        self.hlayout_tracker.addWidget(self.cb_tracker_type)

        self.lbl_transponder_id = QLabel(form_drone)
        self.lbl_transponder_id.setObjectName(u"lbl_transponder_id")

        self.hlayout_tracker.addWidget(self.lbl_transponder_id)

        self.le_transponder_id = QLineEdit(form_drone)
        self.le_transponder_id.setObjectName(u"le_transponder_id")

        self.hlayout_tracker.addWidget(self.le_transponder_id)


        self.verticalLayout.addLayout(self.hlayout_tracker)

        self.hlayout_btn_drone = QHBoxLayout()
        self.hlayout_btn_drone.setObjectName(u"hlayout_btn_drone")
        self.hlayout_btn_drone.setContentsMargins(300, -1, -1, -1)
        self.btn_accept = QPushButton(form_drone)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_drone.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(form_drone)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_drone.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.hlayout_btn_drone)


        self.retranslateUi(form_drone)

        QMetaObject.connectSlotsByName(form_drone)
    # setupUi

    def retranslateUi(self, form_drone):
        form_drone.setWindowTitle(QCoreApplication.translate("form_drone", u"Form", None))
        self.lbl_operator.setText(QCoreApplication.translate("form_drone", u"Operator:", None))
        self.lbl_name.setText(QCoreApplication.translate("form_drone", u"Name:", None))
        self.lbl_sn.setText(QCoreApplication.translate("form_drone", u"Serial Number:", None))
        self.lbl_manufacturer.setText(QCoreApplication.translate("form_drone", u"Manufacturer:", None))
        self.lbl_model.setText(QCoreApplication.translate("form_drone", u"Model:", None))
        self.lbl_tracker_type.setText(QCoreApplication.translate("form_drone", u"Tracker type:", None))
        self.cb_tracker_type.setItemText(0, QCoreApplication.translate("form_drone", u"BLIP", None))
        self.cb_tracker_type.setItemText(1, QCoreApplication.translate("form_drone", u"GCS-API", None))

        self.lbl_transponder_id.setText(QCoreApplication.translate("form_drone", u"Transponder ID:", None))
        self.btn_accept.setText(QCoreApplication.translate("form_drone", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_drone", u"Cancel", None))
    # retranslateUi

