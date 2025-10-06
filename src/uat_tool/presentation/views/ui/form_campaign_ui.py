# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_campaign.ui'
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

class Ui_form_campaign(object):
    def setupUi(self, form_campaign):
        if not form_campaign.objectName():
            form_campaign.setObjectName(u"form_campaign")
        form_campaign.resize(697, 504)
        self.verticalLayout = QVBoxLayout(form_campaign)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.hlayout_id = QHBoxLayout()
        self.hlayout_id.setObjectName(u"hlayout_id")
        self.hlayout_id.setContentsMargins(5, -1, 5, -1)
        self.lbl_identification = QLabel(form_campaign)
        self.lbl_identification.setObjectName(u"lbl_identification")

        self.hlayout_id.addWidget(self.lbl_identification)

        self.le_identification = QLineEdit(form_campaign)
        self.le_identification.setObjectName(u"le_identification")
        self.le_identification.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.hlayout_id.addWidget(self.le_identification)

        self.lbl_description = QLabel(form_campaign)
        self.lbl_description.setObjectName(u"lbl_description")

        self.hlayout_id.addWidget(self.lbl_description)

        self.le_description = QLineEdit(form_campaign)
        self.le_description.setObjectName(u"le_description")

        self.hlayout_id.addWidget(self.le_description)

        self.hlayout_id.setStretch(3, 50)

        self.verticalLayout.addLayout(self.hlayout_id)

        self.hlayout_system = QHBoxLayout()
        self.hlayout_system.setObjectName(u"hlayout_system")
        self.hlayout_system.setContentsMargins(5, -1, 200, -1)
        self.lbl_system = QLabel(form_campaign)
        self.lbl_system.setObjectName(u"lbl_system")

        self.hlayout_system.addWidget(self.lbl_system)

        self.cb_system = QComboBox(form_campaign)
        self.cb_system.addItem("")
        self.cb_system.addItem("")
        self.cb_system.addItem("")
        self.cb_system.addItem("")
        self.cb_system.addItem("")
        self.cb_system.setObjectName(u"cb_system")

        self.hlayout_system.addWidget(self.cb_system)

        self.lbl_version = QLabel(form_campaign)
        self.lbl_version.setObjectName(u"lbl_version")

        self.hlayout_system.addWidget(self.lbl_version)

        self.le_version = QLineEdit(form_campaign)
        self.le_version.setObjectName(u"le_version")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_version.sizePolicy().hasHeightForWidth())
        self.le_version.setSizePolicy(sizePolicy)

        self.hlayout_system.addWidget(self.le_version)

        self.lbl_blocks = QLabel(form_campaign)
        self.lbl_blocks.setObjectName(u"lbl_blocks")

        self.hlayout_system.addWidget(self.lbl_blocks)

        self.lw_blocks = QListWidget(form_campaign)
        self.lw_blocks.setObjectName(u"lw_blocks")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lw_blocks.sizePolicy().hasHeightForWidth())
        self.lw_blocks.setSizePolicy(sizePolicy1)
        self.lw_blocks.setMinimumSize(QSize(250, 40))
        self.lw_blocks.setMaximumSize(QSize(400, 100))

        self.hlayout_system.addWidget(self.lw_blocks)


        self.verticalLayout.addLayout(self.hlayout_system)

        self.hlayout_btn_campaign = QHBoxLayout()
        self.hlayout_btn_campaign.setSpacing(2)
        self.hlayout_btn_campaign.setObjectName(u"hlayout_btn_campaign")
        self.hlayout_btn_campaign.setContentsMargins(420, -1, -1, -1)
        self.btn_accept = QPushButton(form_campaign)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_campaign.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(form_campaign)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_campaign.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.hlayout_btn_campaign)


        self.retranslateUi(form_campaign)

        QMetaObject.connectSlotsByName(form_campaign)
    # setupUi

    def retranslateUi(self, form_campaign):
        form_campaign.setWindowTitle(QCoreApplication.translate("form_campaign", u"Form", None))
        self.lbl_identification.setText(QCoreApplication.translate("form_campaign", u"Id:", None))
        self.le_identification.setText("")
        self.le_identification.setPlaceholderText(QCoreApplication.translate("form_campaign", u"[Identification]", None))
        self.lbl_description.setText(QCoreApplication.translate("form_campaign", u"Description:", None))
        self.le_description.setText("")
        self.le_description.setPlaceholderText(QCoreApplication.translate("form_campaign", u"[Description]", None))
        self.lbl_system.setText(QCoreApplication.translate("form_campaign", u"System:", None))
        self.cb_system.setItemText(0, QCoreApplication.translate("form_campaign", u"USSP", None))
        self.cb_system.setItemText(1, QCoreApplication.translate("form_campaign", u"CISP", None))
        self.cb_system.setItemText(2, QCoreApplication.translate("form_campaign", u"AUDI", None))
        self.cb_system.setItemText(3, QCoreApplication.translate("form_campaign", u"EXCHANGE", None))
        self.cb_system.setItemText(4, QCoreApplication.translate("form_campaign", u"NA", None))

        self.lbl_version.setText(QCoreApplication.translate("form_campaign", u"Version:", None))
        self.le_version.setText("")
        self.le_version.setPlaceholderText(QCoreApplication.translate("form_campaign", u"[Version]", None))
        self.lbl_blocks.setText(QCoreApplication.translate("form_campaign", u"Test blocks:", None))
        self.btn_accept.setText(QCoreApplication.translate("form_campaign", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_campaign", u"Cancel", None))
    # retranslateUi

