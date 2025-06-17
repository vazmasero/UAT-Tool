# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_bug.ui'
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

class Ui_bug_form(object):
    def setupUi(self, bug_form):
        if not bug_form.objectName():
            bug_form.setObjectName(u"bug_form")
        bug_form.resize(726, 523)
        self.main_vlayout = QVBoxLayout(bug_form)
        self.main_vlayout.setSpacing(15)
        self.main_vlayout.setObjectName(u"main_vlayout")
        self.main_vlayout.setContentsMargins(30, 10, 30, 25)
        self.lbl_bug = QLabel(bug_form)
        self.lbl_bug.setObjectName(u"lbl_bug")
        font = QFont()
        font.setPointSize(24)
        self.lbl_bug.setFont(font)
        self.lbl_bug.setWordWrap(True)

        self.main_vlayout.addWidget(self.lbl_bug)

        self.status_form_hlayout = QHBoxLayout()
        self.status_form_hlayout.setSpacing(15)
        self.status_form_hlayout.setObjectName(u"status_form_hlayout")
        self.status_form_hlayout.setContentsMargins(-1, -1, 10, -1)
        self.status_lbl = QLabel(bug_form)
        self.status_lbl.setObjectName(u"status_lbl")

        self.status_form_hlayout.addWidget(self.status_lbl)

        self.status_le = QLineEdit(bug_form)
        self.status_le.setObjectName(u"status_le")
        self.status_le.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.status_form_hlayout.addWidget(self.status_le)

        self.system_lbl = QLabel(bug_form)
        self.system_lbl.setObjectName(u"system_lbl")

        self.status_form_hlayout.addWidget(self.system_lbl)

        self.system_le = QLineEdit(bug_form)
        self.system_le.setObjectName(u"system_le")

        self.status_form_hlayout.addWidget(self.system_le)

        self.sys_version_lbl = QLabel(bug_form)
        self.sys_version_lbl.setObjectName(u"sys_version_lbl")

        self.status_form_hlayout.addWidget(self.sys_version_lbl)

        self.sys_version_le = QLineEdit(bug_form)
        self.sys_version_le.setObjectName(u"sys_version_le")

        self.status_form_hlayout.addWidget(self.sys_version_le)

        self.service_now_id_lbl = QLabel(bug_form)
        self.service_now_id_lbl.setObjectName(u"service_now_id_lbl")

        self.status_form_hlayout.addWidget(self.service_now_id_lbl)

        self.service_now_id_le = QLineEdit(bug_form)
        self.service_now_id_le.setObjectName(u"service_now_id_le")

        self.status_form_hlayout.addWidget(self.service_now_id_le)


        self.main_vlayout.addLayout(self.status_form_hlayout)

        self.date_form_layout = QHBoxLayout()
        self.date_form_layout.setSpacing(15)
        self.date_form_layout.setObjectName(u"date_form_layout")
        self.date_form_layout.setContentsMargins(-1, -1, 150, -1)
        self.creation_time_lbl = QLabel(bug_form)
        self.creation_time_lbl.setObjectName(u"creation_time_lbl")

        self.date_form_layout.addWidget(self.creation_time_lbl)

        self.creation_time_le = QLineEdit(bug_form)
        self.creation_time_le.setObjectName(u"creation_time_le")

        self.date_form_layout.addWidget(self.creation_time_le)

        self.last_update_lbl = QLabel(bug_form)
        self.last_update_lbl.setObjectName(u"last_update_lbl")

        self.date_form_layout.addWidget(self.last_update_lbl)

        self.last_update_le = QLineEdit(bug_form)
        self.last_update_le.setObjectName(u"last_update_le")

        self.date_form_layout.addWidget(self.last_update_le)


        self.main_vlayout.addLayout(self.date_form_layout)

        self.campaign_hlayout = QHBoxLayout()
        self.campaign_hlayout.setSpacing(15)
        self.campaign_hlayout.setObjectName(u"campaign_hlayout")
        self.campaign_hlayout.setContentsMargins(-1, -1, 275, -1)
        self.campaign_lbl = QLabel(bug_form)
        self.campaign_lbl.setObjectName(u"campaign_lbl")

        self.campaign_hlayout.addWidget(self.campaign_lbl)

        self.campaign_cb = QComboBox(bug_form)
        self.campaign_cb.setObjectName(u"campaign_cb")

        self.campaign_hlayout.addWidget(self.campaign_cb)

        self.requirements_lbl = QLabel(bug_form)
        self.requirements_lbl.setObjectName(u"requirements_lbl")

        self.campaign_hlayout.addWidget(self.requirements_lbl)

        self.requirements_cb = QComboBox(bug_form)
        self.requirements_cb.setObjectName(u"requirements_cb")

        self.campaign_hlayout.addWidget(self.requirements_cb)


        self.main_vlayout.addLayout(self.campaign_hlayout)

        self.urgency_hlayout = QHBoxLayout()
        self.urgency_hlayout.setSpacing(15)
        self.urgency_hlayout.setObjectName(u"urgency_hlayout")
        self.urgency_hlayout.setContentsMargins(-1, -1, 275, -1)
        self.urgency_lbl = QLabel(bug_form)
        self.urgency_lbl.setObjectName(u"urgency_lbl")

        self.urgency_hlayout.addWidget(self.urgency_lbl)

        self.urgency_cb = QComboBox(bug_form)
        self.urgency_cb.setObjectName(u"urgency_cb")

        self.urgency_hlayout.addWidget(self.urgency_cb)

        self.impact_lbl = QLabel(bug_form)
        self.impact_lbl.setObjectName(u"impact_lbl")

        self.urgency_hlayout.addWidget(self.impact_lbl)

        self.impact_cb = QComboBox(bug_form)
        self.impact_cb.setObjectName(u"impact_cb")

        self.urgency_hlayout.addWidget(self.impact_cb)


        self.main_vlayout.addLayout(self.urgency_hlayout)

        self.short_description_hlayout = QHBoxLayout()
        self.short_description_hlayout.setObjectName(u"short_description_hlayout")
        self.short_description_hlayout.setContentsMargins(-1, -1, 10, -1)
        self.short_lbl = QLabel(bug_form)
        self.short_lbl.setObjectName(u"short_lbl")

        self.short_description_hlayout.addWidget(self.short_lbl)

        self.short_le = QLineEdit(bug_form)
        self.short_le.setObjectName(u"short_le")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.short_le.sizePolicy().hasHeightForWidth())
        self.short_le.setSizePolicy(sizePolicy)
        self.short_le.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.short_description_hlayout.addWidget(self.short_le)


        self.main_vlayout.addLayout(self.short_description_hlayout)

        self.definition_hlayout = QHBoxLayout()
        self.definition_hlayout.setSpacing(10)
        self.definition_hlayout.setObjectName(u"definition_hlayout")
        self.definition_hlayout.setContentsMargins(-1, 5, 10, 50)
        self.definition_lbl = QLabel(bug_form)
        self.definition_lbl.setObjectName(u"definition_lbl")

        self.definition_hlayout.addWidget(self.definition_lbl)

        self.definition_le = QLineEdit(bug_form)
        self.definition_le.setObjectName(u"definition_le")
        self.definition_le.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.definition_hlayout.addWidget(self.definition_le)


        self.main_vlayout.addLayout(self.definition_hlayout)

        self.bug_actions_hlayout = QHBoxLayout()
        self.bug_actions_hlayout.setSpacing(5)
        self.bug_actions_hlayout.setObjectName(u"bug_actions_hlayout")
        self.bug_actions_hlayout.setContentsMargins(400, -1, -1, -1)
        self.edit_bug_btn = QPushButton(bug_form)
        self.edit_bug_btn.setObjectName(u"edit_bug_btn")

        self.bug_actions_hlayout.addWidget(self.edit_bug_btn)

        self.cancel_btn = QPushButton(bug_form)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.bug_actions_hlayout.addWidget(self.cancel_btn)


        self.main_vlayout.addLayout(self.bug_actions_hlayout)


        self.retranslateUi(bug_form)

        QMetaObject.connectSlotsByName(bug_form)
    # setupUi

    def retranslateUi(self, bug_form):
        bug_form.setWindowTitle(QCoreApplication.translate("bug_form", u"Form", None))
        self.lbl_bug.setText(QCoreApplication.translate("bug_form", u"[Edit bug #]", None))
        self.status_lbl.setText(QCoreApplication.translate("bug_form", u"Status:", None))
        self.status_le.setText("")
        self.status_le.setPlaceholderText(QCoreApplication.translate("bug_form", u"[Status]", None))
        self.system_lbl.setText(QCoreApplication.translate("bug_form", u"System:", None))
        self.system_le.setText("")
        self.system_le.setPlaceholderText(QCoreApplication.translate("bug_form", u"[System]", None))
        self.sys_version_lbl.setText(QCoreApplication.translate("bug_form", u"System Version:", None))
        self.sys_version_le.setText("")
        self.sys_version_le.setPlaceholderText(QCoreApplication.translate("bug_form", u"[System Version]", None))
        self.service_now_id_lbl.setText(QCoreApplication.translate("bug_form", u"Service now ID:", None))
        self.service_now_id_le.setText("")
        self.service_now_id_le.setPlaceholderText(QCoreApplication.translate("bug_form", u"[Service now ID]", None))
        self.creation_time_lbl.setText(QCoreApplication.translate("bug_form", u"Creation time:", None))
        self.creation_time_le.setText("")
        self.creation_time_le.setPlaceholderText(QCoreApplication.translate("bug_form", u"[Creation time]", None))
        self.last_update_lbl.setText(QCoreApplication.translate("bug_form", u"Last update:", None))
        self.last_update_le.setText("")
        self.last_update_le.setPlaceholderText(QCoreApplication.translate("bug_form", u"[Last update]", None))
        self.campaign_lbl.setText(QCoreApplication.translate("bug_form", u"Campaign:", None))
        self.requirements_lbl.setText(QCoreApplication.translate("bug_form", u"Requirements affected:", None))
        self.urgency_lbl.setText(QCoreApplication.translate("bug_form", u"Urgency:", None))
        self.impact_lbl.setText(QCoreApplication.translate("bug_form", u"Impact:", None))
        self.short_lbl.setText(QCoreApplication.translate("bug_form", u"Short description: ", None))
        self.short_le.setText("")
        self.short_le.setPlaceholderText(QCoreApplication.translate("bug_form", u"[Short decription]", None))
        self.definition_lbl.setText(QCoreApplication.translate("bug_form", u"Definition:", None))
        self.definition_le.setText("")
        self.definition_le.setPlaceholderText(QCoreApplication.translate("bug_form", u"[Definition]", None))
        self.edit_bug_btn.setText(QCoreApplication.translate("bug_form", u"Edit bug", None))
        self.cancel_btn.setText(QCoreApplication.translate("bug_form", u"Cancel", None))
    # retranslateUi

