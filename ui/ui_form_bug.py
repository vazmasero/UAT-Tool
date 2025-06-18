# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_bug.ui'
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

class Ui_form_bug(object):
    def setupUi(self, form_bug):
        if not form_bug.objectName():
            form_bug.setObjectName(u"form_bug")
        form_bug.resize(720, 510)
        self.main_vlayout = QVBoxLayout(form_bug)
        self.main_vlayout.setSpacing(15)
        self.main_vlayout.setObjectName(u"main_vlayout")
        self.main_vlayout.setContentsMargins(30, 10, 30, 25)
        self.lbl_bug = QLabel(form_bug)
        self.lbl_bug.setObjectName(u"lbl_bug")
        font = QFont()
        font.setPointSize(24)
        self.lbl_bug.setFont(font)
        self.lbl_bug.setWordWrap(True)

        self.main_vlayout.addWidget(self.lbl_bug)

        self.hlayout_status = QHBoxLayout()
        self.hlayout_status.setSpacing(15)
        self.hlayout_status.setObjectName(u"hlayout_status")
        self.hlayout_status.setContentsMargins(-1, -1, 10, -1)
        self.lbl_status = QLabel(form_bug)
        self.lbl_status.setObjectName(u"lbl_status")

        self.hlayout_status.addWidget(self.lbl_status)

        self.le_status = QLineEdit(form_bug)
        self.le_status.setObjectName(u"le_status")
        self.le_status.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.hlayout_status.addWidget(self.le_status)

        self.lbl_system = QLabel(form_bug)
        self.lbl_system.setObjectName(u"lbl_system")

        self.hlayout_status.addWidget(self.lbl_system)

        self.system_le = QLineEdit(form_bug)
        self.system_le.setObjectName(u"system_le")

        self.hlayout_status.addWidget(self.system_le)

        self.lbl_version = QLabel(form_bug)
        self.lbl_version.setObjectName(u"lbl_version")

        self.hlayout_status.addWidget(self.lbl_version)

        self.le_version = QLineEdit(form_bug)
        self.le_version.setObjectName(u"le_version")

        self.hlayout_status.addWidget(self.le_version)

        self.lbl_id = QLabel(form_bug)
        self.lbl_id.setObjectName(u"lbl_id")

        self.hlayout_status.addWidget(self.lbl_id)

        self.le_id = QLineEdit(form_bug)
        self.le_id.setObjectName(u"le_id")

        self.hlayout_status.addWidget(self.le_id)


        self.main_vlayout.addLayout(self.hlayout_status)

        self.hlayout_date = QHBoxLayout()
        self.hlayout_date.setSpacing(15)
        self.hlayout_date.setObjectName(u"hlayout_date")
        self.hlayout_date.setContentsMargins(-1, -1, 150, -1)
        self.lbl_creation = QLabel(form_bug)
        self.lbl_creation.setObjectName(u"lbl_creation")

        self.hlayout_date.addWidget(self.lbl_creation)

        self.le_creation = QLineEdit(form_bug)
        self.le_creation.setObjectName(u"le_creation")

        self.hlayout_date.addWidget(self.le_creation)

        self.lbl_update = QLabel(form_bug)
        self.lbl_update.setObjectName(u"lbl_update")

        self.hlayout_date.addWidget(self.lbl_update)

        self.le_update = QLineEdit(form_bug)
        self.le_update.setObjectName(u"le_update")

        self.hlayout_date.addWidget(self.le_update)


        self.main_vlayout.addLayout(self.hlayout_date)

        self.hlayout_campaign = QHBoxLayout()
        self.hlayout_campaign.setSpacing(15)
        self.hlayout_campaign.setObjectName(u"hlayout_campaign")
        self.hlayout_campaign.setContentsMargins(-1, -1, 275, -1)
        self.lbl_campaign = QLabel(form_bug)
        self.lbl_campaign.setObjectName(u"lbl_campaign")

        self.hlayout_campaign.addWidget(self.lbl_campaign)

        self.cb_campaign = QComboBox(form_bug)
        self.cb_campaign.setObjectName(u"cb_campaign")

        self.hlayout_campaign.addWidget(self.cb_campaign)

        self.lbl_requirements = QLabel(form_bug)
        self.lbl_requirements.setObjectName(u"lbl_requirements")

        self.hlayout_campaign.addWidget(self.lbl_requirements)

        self.cb_requirements = QComboBox(form_bug)
        self.cb_requirements.setObjectName(u"cb_requirements")

        self.hlayout_campaign.addWidget(self.cb_requirements)


        self.main_vlayout.addLayout(self.hlayout_campaign)

        self.hlayout_urgency = QHBoxLayout()
        self.hlayout_urgency.setSpacing(15)
        self.hlayout_urgency.setObjectName(u"hlayout_urgency")
        self.hlayout_urgency.setContentsMargins(-1, -1, 275, -1)
        self.lbl_urgency = QLabel(form_bug)
        self.lbl_urgency.setObjectName(u"lbl_urgency")

        self.hlayout_urgency.addWidget(self.lbl_urgency)

        self.cb_urgency = QComboBox(form_bug)
        self.cb_urgency.setObjectName(u"cb_urgency")

        self.hlayout_urgency.addWidget(self.cb_urgency)

        self.lbl_impact = QLabel(form_bug)
        self.lbl_impact.setObjectName(u"lbl_impact")

        self.hlayout_urgency.addWidget(self.lbl_impact)

        self.cb_impact = QComboBox(form_bug)
        self.cb_impact.setObjectName(u"cb_impact")

        self.hlayout_urgency.addWidget(self.cb_impact)


        self.main_vlayout.addLayout(self.hlayout_urgency)

        self.hlayout_description = QHBoxLayout()
        self.hlayout_description.setObjectName(u"hlayout_description")
        self.hlayout_description.setContentsMargins(-1, -1, 10, -1)
        self.lbl_short = QLabel(form_bug)
        self.lbl_short.setObjectName(u"lbl_short")

        self.hlayout_description.addWidget(self.lbl_short)

        self.le_short = QLineEdit(form_bug)
        self.le_short.setObjectName(u"le_short")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_short.sizePolicy().hasHeightForWidth())
        self.le_short.setSizePolicy(sizePolicy)
        self.le_short.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.hlayout_description.addWidget(self.le_short)


        self.main_vlayout.addLayout(self.hlayout_description)

        self.hlayout_definition = QHBoxLayout()
        self.hlayout_definition.setSpacing(10)
        self.hlayout_definition.setObjectName(u"hlayout_definition")
        self.hlayout_definition.setContentsMargins(-1, 5, 10, 50)
        self.lbl_definition = QLabel(form_bug)
        self.lbl_definition.setObjectName(u"lbl_definition")

        self.hlayout_definition.addWidget(self.lbl_definition)

        self.le_definition = QLineEdit(form_bug)
        self.le_definition.setObjectName(u"le_definition")
        self.le_definition.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.hlayout_definition.addWidget(self.le_definition)


        self.main_vlayout.addLayout(self.hlayout_definition)

        self.hlayout_btn_bug = QHBoxLayout()
        self.hlayout_btn_bug.setSpacing(5)
        self.hlayout_btn_bug.setObjectName(u"hlayout_btn_bug")
        self.hlayout_btn_bug.setContentsMargins(400, -1, -1, -1)
        self.btn_add_bug = QPushButton(form_bug)
        self.btn_add_bug.setObjectName(u"btn_add_bug")

        self.hlayout_btn_bug.addWidget(self.btn_add_bug)

        self.btn_cancel = QPushButton(form_bug)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_bug.addWidget(self.btn_cancel)


        self.main_vlayout.addLayout(self.hlayout_btn_bug)


        self.retranslateUi(form_bug)

        QMetaObject.connectSlotsByName(form_bug)
    # setupUi

    def retranslateUi(self, form_bug):
        form_bug.setWindowTitle(QCoreApplication.translate("form_bug", u"Form", None))
        self.lbl_bug.setText(QCoreApplication.translate("form_bug", u"[New/Edit bug]", None))
        self.lbl_status.setText(QCoreApplication.translate("form_bug", u"Status:", None))
        self.le_status.setText("")
        self.le_status.setPlaceholderText(QCoreApplication.translate("form_bug", u"[Status]", None))
        self.lbl_system.setText(QCoreApplication.translate("form_bug", u"System:", None))
        self.system_le.setText("")
        self.system_le.setPlaceholderText(QCoreApplication.translate("form_bug", u"[System]", None))
        self.lbl_version.setText(QCoreApplication.translate("form_bug", u"System Version:", None))
        self.le_version.setText("")
        self.le_version.setPlaceholderText(QCoreApplication.translate("form_bug", u"[System Version]", None))
        self.lbl_id.setText(QCoreApplication.translate("form_bug", u"Service now ID:", None))
        self.le_id.setText("")
        self.le_id.setPlaceholderText(QCoreApplication.translate("form_bug", u"[Service now ID]", None))
        self.lbl_creation.setText(QCoreApplication.translate("form_bug", u"Creation time:", None))
        self.le_creation.setText("")
        self.le_creation.setPlaceholderText(QCoreApplication.translate("form_bug", u"[Creation time]", None))
        self.lbl_update.setText(QCoreApplication.translate("form_bug", u"Last update:", None))
        self.le_update.setText("")
        self.le_update.setPlaceholderText(QCoreApplication.translate("form_bug", u"[Last update]", None))
        self.lbl_campaign.setText(QCoreApplication.translate("form_bug", u"Campaign:", None))
        self.lbl_requirements.setText(QCoreApplication.translate("form_bug", u"Requirements affected:", None))
        self.lbl_urgency.setText(QCoreApplication.translate("form_bug", u"Urgency:", None))
        self.lbl_impact.setText(QCoreApplication.translate("form_bug", u"Impact:", None))
        self.lbl_short.setText(QCoreApplication.translate("form_bug", u"Short description: ", None))
        self.le_short.setText("")
        self.le_short.setPlaceholderText(QCoreApplication.translate("form_bug", u"[Short decription]", None))
        self.lbl_definition.setText(QCoreApplication.translate("form_bug", u"Definition:", None))
        self.le_definition.setText("")
        self.le_definition.setPlaceholderText(QCoreApplication.translate("form_bug", u"[Definition]", None))
        self.btn_add_bug.setText(QCoreApplication.translate("form_bug", u"Create bug", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_bug", u"Cancel", None))
    # retranslateUi

