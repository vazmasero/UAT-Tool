# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_bug.ui'
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
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_form_bug(object):
    def setupUi(self, form_bug):
        if not form_bug.objectName():
            form_bug.setObjectName(u"form_bug")
        form_bug.setEnabled(True)
        form_bug.resize(720, 510)
        self.verticalLayout = QVBoxLayout(form_bug)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, 25)
        self.lbl_title = QLabel(form_bug)
        self.lbl_title.setObjectName(u"lbl_title")
        font = QFont()
        font.setPointSize(22)
        self.lbl_title.setFont(font)
        self.lbl_title.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_title)

        self.tab_widget_bug = QTabWidget(form_bug)
        self.tab_widget_bug.setObjectName(u"tab_widget_bug")
        self.tab_info = QWidget()
        self.tab_info.setObjectName(u"tab_info")
        self.verticalLayout_2 = QVBoxLayout(self.tab_info)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.hlayout_status = QHBoxLayout()
        self.hlayout_status.setObjectName(u"hlayout_status")
        self.lbl_status = QLabel(self.tab_info)
        self.lbl_status.setObjectName(u"lbl_status")

        self.hlayout_status.addWidget(self.lbl_status)

        self.cb_status = QComboBox(self.tab_info)
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.setObjectName(u"cb_status")

        self.hlayout_status.addWidget(self.cb_status)

        self.lbl_system = QLabel(self.tab_info)
        self.lbl_system.setObjectName(u"lbl_system")

        self.hlayout_status.addWidget(self.lbl_system)

        self.cb_system = QComboBox(self.tab_info)
        self.cb_system.setObjectName(u"cb_system")

        self.hlayout_status.addWidget(self.cb_system)

        self.lbl_version = QLabel(self.tab_info)
        self.lbl_version.setObjectName(u"lbl_version")

        self.hlayout_status.addWidget(self.lbl_version)

        self.le_version = QLineEdit(self.tab_info)
        self.le_version.setObjectName(u"le_version")

        self.hlayout_status.addWidget(self.le_version)

        self.lbl_service_now_id = QLabel(self.tab_info)
        self.lbl_service_now_id.setObjectName(u"lbl_service_now_id")

        self.hlayout_status.addWidget(self.lbl_service_now_id)

        self.le_service_now_id = QLineEdit(self.tab_info)
        self.le_service_now_id.setObjectName(u"le_service_now_id")

        self.hlayout_status.addWidget(self.le_service_now_id)


        self.verticalLayout_2.addLayout(self.hlayout_status)

        self.hlayout_campaign = QHBoxLayout()
        self.hlayout_campaign.setObjectName(u"hlayout_campaign")
        self.lbl_campaign = QLabel(self.tab_info)
        self.lbl_campaign.setObjectName(u"lbl_campaign")

        self.hlayout_campaign.addWidget(self.lbl_campaign)

        self.cb_campaign = QComboBox(self.tab_info)
        self.cb_campaign.addItem("")
        self.cb_campaign.setObjectName(u"cb_campaign")

        self.hlayout_campaign.addWidget(self.cb_campaign)

        self.lbl_campaign_2 = QLabel(self.tab_info)
        self.lbl_campaign_2.setObjectName(u"lbl_campaign_2")

        self.hlayout_campaign.addWidget(self.lbl_campaign_2)

        self.lw_requirements = QListWidget(self.tab_info)
        self.lw_requirements.setObjectName(u"lw_requirements")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_requirements.sizePolicy().hasHeightForWidth())
        self.lw_requirements.setSizePolicy(sizePolicy)
        self.lw_requirements.setMaximumSize(QSize(200, 40))

        self.hlayout_campaign.addWidget(self.lw_requirements)


        self.verticalLayout_2.addLayout(self.hlayout_campaign)

        self.hlayout_urgency = QHBoxLayout()
        self.hlayout_urgency.setObjectName(u"hlayout_urgency")
        self.lbl_urgency = QLabel(self.tab_info)
        self.lbl_urgency.setObjectName(u"lbl_urgency")

        self.hlayout_urgency.addWidget(self.lbl_urgency)

        self.cb_urgency = QComboBox(self.tab_info)
        self.cb_urgency.addItem("")
        self.cb_urgency.addItem("")
        self.cb_urgency.addItem("")
        self.cb_urgency.setObjectName(u"cb_urgency")

        self.hlayout_urgency.addWidget(self.cb_urgency)

        self.lbl_impact = QLabel(self.tab_info)
        self.lbl_impact.setObjectName(u"lbl_impact")

        self.hlayout_urgency.addWidget(self.lbl_impact)

        self.cb_impact = QComboBox(self.tab_info)
        self.cb_impact.addItem("")
        self.cb_impact.addItem("")
        self.cb_impact.addItem("")
        self.cb_impact.setObjectName(u"cb_impact")

        self.hlayout_urgency.addWidget(self.cb_impact)


        self.verticalLayout_2.addLayout(self.hlayout_urgency)

        self.hlayout_description = QHBoxLayout()
        self.hlayout_description.setObjectName(u"hlayout_description")
        self.lbl_short_desc = QLabel(self.tab_info)
        self.lbl_short_desc.setObjectName(u"lbl_short_desc")

        self.hlayout_description.addWidget(self.lbl_short_desc)

        self.le_short_desc = QLineEdit(self.tab_info)
        self.le_short_desc.setObjectName(u"le_short_desc")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_short_desc.sizePolicy().hasHeightForWidth())
        self.le_short_desc.setSizePolicy(sizePolicy1)
        self.le_short_desc.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.hlayout_description.addWidget(self.le_short_desc)


        self.verticalLayout_2.addLayout(self.hlayout_description)

        self.hlayout_definition = QHBoxLayout()
        self.hlayout_definition.setObjectName(u"hlayout_definition")
        self.lbl_definition = QLabel(self.tab_info)
        self.lbl_definition.setObjectName(u"lbl_definition")

        self.hlayout_definition.addWidget(self.lbl_definition)

        self.le_definition = QLineEdit(self.tab_info)
        self.le_definition.setObjectName(u"le_definition")
        self.le_definition.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.hlayout_definition.addWidget(self.le_definition)


        self.verticalLayout_2.addLayout(self.hlayout_definition)

        self.hlayout_files = QHBoxLayout()
        self.hlayout_files.setObjectName(u"hlayout_files")
        self.lbl_files = QLabel(self.tab_info)
        self.lbl_files.setObjectName(u"lbl_files")

        self.hlayout_files.addWidget(self.lbl_files)

        self.le_files = QLineEdit(self.tab_info)
        self.le_files.setObjectName(u"le_files")

        self.hlayout_files.addWidget(self.le_files)

        self.btn_files = QPushButton(self.tab_info)
        self.btn_files.setObjectName(u"btn_files")
        self.btn_files.setMinimumSize(QSize(175, 0))

        self.hlayout_files.addWidget(self.btn_files)


        self.verticalLayout_2.addLayout(self.hlayout_files)

        self.tab_widget_bug.addTab(self.tab_info, "")
        self.tab_history = QWidget()
        self.tab_history.setObjectName(u"tab_history")
        self.verticalLayout_3 = QVBoxLayout(self.tab_history)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lw_history = QListWidget(self.tab_history)
        QListWidgetItem(self.lw_history)
        self.lw_history.setObjectName(u"lw_history")

        self.verticalLayout_3.addWidget(self.lw_history)

        self.tab_widget_bug.addTab(self.tab_history, "")

        self.verticalLayout.addWidget(self.tab_widget_bug)

        self.hlayout_btn_bug = QHBoxLayout()
        self.hlayout_btn_bug.setObjectName(u"hlayout_btn_bug")
        self.hlayout_btn_bug.setContentsMargins(300, -1, -1, -1)
        self.btn_accept = QPushButton(form_bug)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_bug.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(form_bug)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_bug.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.hlayout_btn_bug)


        self.retranslateUi(form_bug)

        self.tab_widget_bug.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(form_bug)
    # setupUi

    def retranslateUi(self, form_bug):
        form_bug.setWindowTitle(QCoreApplication.translate("form_bug", u"Form", None))
        self.lbl_title.setText(QCoreApplication.translate("form_bug", u"[Bug name]", None))
        self.lbl_status.setText(QCoreApplication.translate("form_bug", u"Status:", None))
        self.cb_status.setItemText(0, QCoreApplication.translate("form_bug", u"IN PROGRESS", None))
        self.cb_status.setItemText(1, QCoreApplication.translate("form_bug", u"OPEN", None))
        self.cb_status.setItemText(2, QCoreApplication.translate("form_bug", u"CLOSED", None))
        self.cb_status.setItemText(3, QCoreApplication.translate("form_bug", u"PENDING ACTION", None))

        self.lbl_system.setText(QCoreApplication.translate("form_bug", u"System:", None))
        self.lbl_version.setText(QCoreApplication.translate("form_bug", u"System version:", None))
        self.le_version.setText("")
        self.le_version.setPlaceholderText(QCoreApplication.translate("form_bug", u"[System version]", None))
        self.lbl_service_now_id.setText(QCoreApplication.translate("form_bug", u"Service now ID:", None))
        self.le_service_now_id.setText("")
        self.le_service_now_id.setPlaceholderText(QCoreApplication.translate("form_bug", u"[Service now ID]", None))
        self.lbl_campaign.setText(QCoreApplication.translate("form_bug", u"Campaign:", None))
        self.cb_campaign.setItemText(0, QCoreApplication.translate("form_bug", u"NA", None))

        self.lbl_campaign_2.setText(QCoreApplication.translate("form_bug", u"Requirements affected:", None))
        self.lbl_urgency.setText(QCoreApplication.translate("form_bug", u"Urgency:", None))
        self.cb_urgency.setItemText(0, QCoreApplication.translate("form_bug", u"Low (1)", None))
        self.cb_urgency.setItemText(1, QCoreApplication.translate("form_bug", u"Medium (2)", None))
        self.cb_urgency.setItemText(2, QCoreApplication.translate("form_bug", u"High (3)", None))

        self.lbl_impact.setText(QCoreApplication.translate("form_bug", u"Impact:", None))
        self.cb_impact.setItemText(0, QCoreApplication.translate("form_bug", u"Low (1)", None))
        self.cb_impact.setItemText(1, QCoreApplication.translate("form_bug", u"Medium (2)", None))
        self.cb_impact.setItemText(2, QCoreApplication.translate("form_bug", u"High (3)", None))

        self.lbl_short_desc.setText(QCoreApplication.translate("form_bug", u"Short description: ", None))
        self.le_short_desc.setText("")
        self.le_short_desc.setPlaceholderText(QCoreApplication.translate("form_bug", u"[Short decription]", None))
        self.lbl_definition.setText(QCoreApplication.translate("form_bug", u"Definition:", None))
        self.le_definition.setText("")
        self.le_definition.setPlaceholderText(QCoreApplication.translate("form_bug", u"[Definition]", None))
        self.lbl_files.setText(QCoreApplication.translate("form_bug", u"Additional files: ", None))
        self.le_files.setPlaceholderText(QCoreApplication.translate("form_bug", u"[Add associated files]", None))
        self.btn_files.setText(QCoreApplication.translate("form_bug", u"Browse", None))
        self.tab_widget_bug.setTabText(self.tab_widget_bug.indexOf(self.tab_info), QCoreApplication.translate("form_bug", u"Bug info", None))

        __sortingEnabled = self.lw_history.isSortingEnabled()
        self.lw_history.setSortingEnabled(False)
        ___qlistwidgetitem = self.lw_history.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("form_bug", u"[Change in status:...]", None));
        self.lw_history.setSortingEnabled(__sortingEnabled)

        self.tab_widget_bug.setTabText(self.tab_widget_bug.indexOf(self.tab_history), QCoreApplication.translate("form_bug", u"History", None))
        self.btn_accept.setText(QCoreApplication.translate("form_bug", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_bug", u"Cancel", None))
    # retranslateUi

