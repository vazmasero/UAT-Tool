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

class Ui_info_bug(object):
    def setupUi(self, info_bug):
        if not info_bug.objectName():
            info_bug.setObjectName(u"info_bug")
        info_bug.setEnabled(True)
        info_bug.resize(720, 510)
        self.verticalLayout = QVBoxLayout(info_bug)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, 25)
        self.lbl_title = QLabel(info_bug)
        self.lbl_title.setObjectName(u"lbl_title")
        font = QFont()
        font.setPointSize(22)
        self.lbl_title.setFont(font)
        self.lbl_title.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_title)

        self.tab_widget_bug = QTabWidget(info_bug)
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
        self.cb_system.addItem("")
        self.cb_system.addItem("")
        self.cb_system.addItem("")
        self.cb_system.addItem("")
        self.cb_system.addItem("")
        self.cb_system.setObjectName(u"cb_system")

        self.hlayout_status.addWidget(self.cb_system)

        self.lbl_version = QLabel(self.tab_info)
        self.lbl_version.setObjectName(u"lbl_version")

        self.hlayout_status.addWidget(self.lbl_version)

        self.le_version = QLineEdit(self.tab_info)
        self.le_version.setObjectName(u"le_version")

        self.hlayout_status.addWidget(self.le_version)

        self.lbl_identification = QLabel(self.tab_info)
        self.lbl_identification.setObjectName(u"lbl_identification")

        self.hlayout_status.addWidget(self.lbl_identification)

        self.le_identification = QLineEdit(self.tab_info)
        self.le_identification.setObjectName(u"le_identification")

        self.hlayout_status.addWidget(self.le_identification)


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

        self.cb_requirements = QComboBox(self.tab_info)
        self.cb_requirements.setObjectName(u"cb_requirements")

        self.hlayout_campaign.addWidget(self.cb_requirements)


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
        self.lbl_description = QLabel(self.tab_info)
        self.lbl_description.setObjectName(u"lbl_description")

        self.hlayout_description.addWidget(self.lbl_description)

        self.le_description = QLineEdit(self.tab_info)
        self.le_description.setObjectName(u"le_description")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_description.sizePolicy().hasHeightForWidth())
        self.le_description.setSizePolicy(sizePolicy)
        self.le_description.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.hlayout_description.addWidget(self.le_description)


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
        self.btn_accept = QPushButton(info_bug)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_bug.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(info_bug)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_bug.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.hlayout_btn_bug)


        self.retranslateUi(info_bug)

        self.tab_widget_bug.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(info_bug)
    # setupUi

    def retranslateUi(self, info_bug):
        info_bug.setWindowTitle(QCoreApplication.translate("info_bug", u"Form", None))
        self.lbl_title.setText(QCoreApplication.translate("info_bug", u"[Bug name]", None))
        self.lbl_status.setText(QCoreApplication.translate("info_bug", u"Status:", None))
        self.cb_status.setItemText(0, QCoreApplication.translate("info_bug", u"IN PROGRESS", None))
        self.cb_status.setItemText(1, QCoreApplication.translate("info_bug", u"OPEN", None))
        self.cb_status.setItemText(2, QCoreApplication.translate("info_bug", u"CLOSED", None))
        self.cb_status.setItemText(3, QCoreApplication.translate("info_bug", u"PENDING ACTION", None))

        self.lbl_system.setText(QCoreApplication.translate("info_bug", u"System:", None))
        self.cb_system.setItemText(0, QCoreApplication.translate("info_bug", u"USSP", None))
        self.cb_system.setItemText(1, QCoreApplication.translate("info_bug", u"CISP", None))
        self.cb_system.setItemText(2, QCoreApplication.translate("info_bug", u"AUDI", None))
        self.cb_system.setItemText(3, QCoreApplication.translate("info_bug", u"EXCHANGE", None))
        self.cb_system.setItemText(4, QCoreApplication.translate("info_bug", u"NA", None))

        self.lbl_version.setText(QCoreApplication.translate("info_bug", u"System version:", None))
        self.le_version.setText("")
        self.le_version.setPlaceholderText(QCoreApplication.translate("info_bug", u"[System version]", None))
        self.lbl_identification.setText(QCoreApplication.translate("info_bug", u"Service now ID:", None))
        self.le_identification.setText("")
        self.le_identification.setPlaceholderText(QCoreApplication.translate("info_bug", u"[Service now ID]", None))
        self.lbl_campaign.setText(QCoreApplication.translate("info_bug", u"Campaign:", None))
        self.cb_campaign.setItemText(0, QCoreApplication.translate("info_bug", u"NA", None))

        self.lbl_campaign_2.setText(QCoreApplication.translate("info_bug", u"Requirements affected:", None))
        self.lbl_urgency.setText(QCoreApplication.translate("info_bug", u"Urgency:", None))
        self.cb_urgency.setItemText(0, QCoreApplication.translate("info_bug", u"Low (1)", None))
        self.cb_urgency.setItemText(1, QCoreApplication.translate("info_bug", u"Medium (2)", None))
        self.cb_urgency.setItemText(2, QCoreApplication.translate("info_bug", u"High (3)", None))

        self.lbl_impact.setText(QCoreApplication.translate("info_bug", u"Impact:", None))
        self.cb_impact.setItemText(0, QCoreApplication.translate("info_bug", u"Low (1)", None))
        self.cb_impact.setItemText(1, QCoreApplication.translate("info_bug", u"Medium (2)", None))
        self.cb_impact.setItemText(2, QCoreApplication.translate("info_bug", u"High (3)", None))

        self.lbl_description.setText(QCoreApplication.translate("info_bug", u"Short description: ", None))
        self.le_description.setText("")
        self.le_description.setPlaceholderText(QCoreApplication.translate("info_bug", u"[Short decription]", None))
        self.lbl_definition.setText(QCoreApplication.translate("info_bug", u"Definition:", None))
        self.le_definition.setText("")
        self.le_definition.setPlaceholderText(QCoreApplication.translate("info_bug", u"[Definition]", None))
        self.lbl_files.setText(QCoreApplication.translate("info_bug", u"Additional files: ", None))
        self.le_files.setPlaceholderText(QCoreApplication.translate("info_bug", u"[Add associated files]", None))
        self.btn_files.setText(QCoreApplication.translate("info_bug", u"Browse", None))
        self.tab_widget_bug.setTabText(self.tab_widget_bug.indexOf(self.tab_info), QCoreApplication.translate("info_bug", u"Bug info", None))

        __sortingEnabled = self.lw_history.isSortingEnabled()
        self.lw_history.setSortingEnabled(False)
        ___qlistwidgetitem = self.lw_history.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("info_bug", u"[Change in status:...]", None));
        self.lw_history.setSortingEnabled(__sortingEnabled)

        self.tab_widget_bug.setTabText(self.tab_widget_bug.indexOf(self.tab_history), QCoreApplication.translate("info_bug", u"History", None))
        self.btn_accept.setText(QCoreApplication.translate("info_bug", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("info_bug", u"Back", None))
    # retranslateUi

