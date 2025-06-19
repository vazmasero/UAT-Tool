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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_form_campaign(object):
    def setupUi(self, form_campaign):
        if not form_campaign.objectName():
            form_campaign.setObjectName(u"form_campaign")
        form_campaign.resize(697, 504)
        self.verticalLayout = QVBoxLayout(form_campaign)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.lbl_campaign = QLabel(form_campaign)
        self.lbl_campaign.setObjectName(u"lbl_campaign")
        font = QFont()
        font.setPointSize(28)
        self.lbl_campaign.setFont(font)
        self.lbl_campaign.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_campaign)

        self.hlayout_id = QHBoxLayout()
        self.hlayout_id.setObjectName(u"hlayout_id")
        self.hlayout_id.setContentsMargins(5, -1, 5, -1)
        self.lbl_id = QLabel(form_campaign)
        self.lbl_id.setObjectName(u"lbl_id")

        self.hlayout_id.addWidget(self.lbl_id)

        self.le_id = QLineEdit(form_campaign)
        self.le_id.setObjectName(u"le_id")
        self.le_id.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.hlayout_id.addWidget(self.le_id)

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
        self.cb_system.setObjectName(u"cb_system")

        self.hlayout_system.addWidget(self.cb_system)

        self.lbl_version = QLabel(form_campaign)
        self.lbl_version.setObjectName(u"lbl_version")

        self.hlayout_system.addWidget(self.lbl_version)

        self.le_version = QLineEdit(form_campaign)
        self.le_version.setObjectName(u"le_version")

        self.hlayout_system.addWidget(self.le_version)

        self.lbl_blocks = QLabel(form_campaign)
        self.lbl_blocks.setObjectName(u"lbl_blocks")

        self.hlayout_system.addWidget(self.lbl_blocks)

        self.cb_blocks = QComboBox(form_campaign)
        self.cb_blocks.setObjectName(u"cb_blocks")

        self.hlayout_system.addWidget(self.cb_blocks)


        self.verticalLayout.addLayout(self.hlayout_system)

        self.hlayout_creation = QHBoxLayout()
        self.hlayout_creation.setObjectName(u"hlayout_creation")
        self.hlayout_creation.setContentsMargins(5, -1, 300, -1)
        self.lbl_creation = QLabel(form_campaign)
        self.lbl_creation.setObjectName(u"lbl_creation")

        self.hlayout_creation.addWidget(self.lbl_creation)

        self.le_creation = QLineEdit(form_campaign)
        self.le_creation.setObjectName(u"le_creation")

        self.hlayout_creation.addWidget(self.le_creation)

        self.lbl_update = QLabel(form_campaign)
        self.lbl_update.setObjectName(u"lbl_update")

        self.hlayout_creation.addWidget(self.lbl_update)

        self.le_update = QLineEdit(form_campaign)
        self.le_update.setObjectName(u"le_update")

        self.hlayout_creation.addWidget(self.le_update)


        self.verticalLayout.addLayout(self.hlayout_creation)

        self.hlayout_btn_campaign = QHBoxLayout()
        self.hlayout_btn_campaign.setSpacing(2)
        self.hlayout_btn_campaign.setObjectName(u"hlayout_btn_campaign")
        self.hlayout_btn_campaign.setContentsMargins(420, -1, -1, -1)
        self.btn_create_campaign = QPushButton(form_campaign)
        self.btn_create_campaign.setObjectName(u"btn_create_campaign")

        self.hlayout_btn_campaign.addWidget(self.btn_create_campaign)

        self.btn_cancel = QPushButton(form_campaign)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_campaign.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.hlayout_btn_campaign)


        self.retranslateUi(form_campaign)

        QMetaObject.connectSlotsByName(form_campaign)
    # setupUi

    def retranslateUi(self, form_campaign):
        form_campaign.setWindowTitle(QCoreApplication.translate("form_campaign", u"Form", None))
        self.lbl_campaign.setText(QCoreApplication.translate("form_campaign", u"[New/Edit campaign]", None))
        self.lbl_id.setText(QCoreApplication.translate("form_campaign", u"Id:", None))
        self.le_id.setText("")
        self.le_id.setPlaceholderText(QCoreApplication.translate("form_campaign", u"[Identification]", None))
        self.lbl_description.setText(QCoreApplication.translate("form_campaign", u"Description:", None))
        self.le_description.setText("")
        self.le_description.setPlaceholderText(QCoreApplication.translate("form_campaign", u"[Description]", None))
        self.lbl_system.setText(QCoreApplication.translate("form_campaign", u"System:", None))
        self.cb_system.setPlaceholderText(QCoreApplication.translate("form_campaign", u"[System]", None))
        self.lbl_version.setText(QCoreApplication.translate("form_campaign", u"Version:", None))
        self.le_version.setText("")
        self.le_version.setPlaceholderText(QCoreApplication.translate("form_campaign", u"[Version]", None))
        self.lbl_blocks.setText(QCoreApplication.translate("form_campaign", u"Test blocks:", None))
        self.cb_blocks.setPlaceholderText(QCoreApplication.translate("form_campaign", u"[Blocks]", None))
        self.lbl_creation.setText(QCoreApplication.translate("form_campaign", u"Creation time:", None))
        self.le_creation.setText("")
        self.le_creation.setPlaceholderText(QCoreApplication.translate("form_campaign", u"[Creation time]", None))
        self.lbl_update.setText(QCoreApplication.translate("form_campaign", u"Last update:", None))
        self.le_update.setText("")
        self.le_update.setPlaceholderText(QCoreApplication.translate("form_campaign", u"[Last update]", None))
        self.btn_create_campaign.setText(QCoreApplication.translate("form_campaign", u"Create campaign", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_campaign", u"Cancel", None))
    # retranslateUi

