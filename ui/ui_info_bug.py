# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_bug.ui'
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

        self.le_status = QLineEdit(self.tab_info)
        self.le_status.setObjectName(u"le_status")
        self.le_status.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.hlayout_status.addWidget(self.le_status)

        self.lbl_system = QLabel(self.tab_info)
        self.lbl_system.setObjectName(u"lbl_system")

        self.hlayout_status.addWidget(self.lbl_system)

        self.le_system = QLineEdit(self.tab_info)
        self.le_system.setObjectName(u"le_system")

        self.hlayout_status.addWidget(self.le_system)

        self.lbl_version = QLabel(self.tab_info)
        self.lbl_version.setObjectName(u"lbl_version")

        self.hlayout_status.addWidget(self.lbl_version)

        self.le_version = QLineEdit(self.tab_info)
        self.le_version.setObjectName(u"le_version")

        self.hlayout_status.addWidget(self.le_version)

        self.lbl_id = QLabel(self.tab_info)
        self.lbl_id.setObjectName(u"lbl_id")

        self.hlayout_status.addWidget(self.lbl_id)

        self.le_id = QLineEdit(self.tab_info)
        self.le_id.setObjectName(u"le_id")

        self.hlayout_status.addWidget(self.le_id)


        self.verticalLayout_2.addLayout(self.hlayout_status)

        self.hlayout_date = QHBoxLayout()
        self.hlayout_date.setObjectName(u"hlayout_date")
        self.lbl_creation = QLabel(self.tab_info)
        self.lbl_creation.setObjectName(u"lbl_creation")

        self.hlayout_date.addWidget(self.lbl_creation)

        self.le_creation = QLineEdit(self.tab_info)
        self.le_creation.setObjectName(u"le_creation")

        self.hlayout_date.addWidget(self.le_creation)

        self.lbl_update = QLabel(self.tab_info)
        self.lbl_update.setObjectName(u"lbl_update")

        self.hlayout_date.addWidget(self.lbl_update)

        self.le_update = QLineEdit(self.tab_info)
        self.le_update.setObjectName(u"le_update")

        self.hlayout_date.addWidget(self.le_update)


        self.verticalLayout_2.addLayout(self.hlayout_date)

        self.hlayout_campaign = QHBoxLayout()
        self.hlayout_campaign.setObjectName(u"hlayout_campaign")
        self.lbl_campaign = QLabel(self.tab_info)
        self.lbl_campaign.setObjectName(u"lbl_campaign")

        self.hlayout_campaign.addWidget(self.lbl_campaign)

        self.le_campaign = QLineEdit(self.tab_info)
        self.le_campaign.setObjectName(u"le_campaign")

        self.hlayout_campaign.addWidget(self.le_campaign)

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

        self.tab_widget_bug.addTab(self.tab_info, "")
        self.tab_history = QWidget()
        self.tab_history.setObjectName(u"tab_history")
        self.verticalLayout_3 = QVBoxLayout(self.tab_history)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.list_history = QListWidget(self.tab_history)
        QListWidgetItem(self.list_history)
        self.list_history.setObjectName(u"list_history")

        self.verticalLayout_3.addWidget(self.list_history)

        self.tab_widget_bug.addTab(self.tab_history, "")

        self.verticalLayout.addWidget(self.tab_widget_bug)

        self.hlayout_btn_bug = QHBoxLayout()
        self.hlayout_btn_bug.setObjectName(u"hlayout_btn_bug")
        self.hlayout_btn_bug.setContentsMargins(300, -1, -1, -1)
        self.btn_close_bug = QPushButton(info_bug)
        self.btn_close_bug.setObjectName(u"btn_close_bug")

        self.hlayout_btn_bug.addWidget(self.btn_close_bug)

        self.btn_edit_bug = QPushButton(info_bug)
        self.btn_edit_bug.setObjectName(u"btn_edit_bug")

        self.hlayout_btn_bug.addWidget(self.btn_edit_bug)

        self.btn_delete_bug = QPushButton(info_bug)
        self.btn_delete_bug.setObjectName(u"btn_delete_bug")

        self.hlayout_btn_bug.addWidget(self.btn_delete_bug)

        self.btn_back = QPushButton(info_bug)
        self.btn_back.setObjectName(u"btn_back")

        self.hlayout_btn_bug.addWidget(self.btn_back)


        self.verticalLayout.addLayout(self.hlayout_btn_bug)


        self.retranslateUi(info_bug)

        self.tab_widget_bug.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(info_bug)
    # setupUi

    def retranslateUi(self, info_bug):
        info_bug.setWindowTitle(QCoreApplication.translate("info_bug", u"Form", None))
        self.lbl_title.setText(QCoreApplication.translate("info_bug", u"[Bug name]", None))
        self.lbl_status.setText(QCoreApplication.translate("info_bug", u"Status:", None))
        self.le_status.setText("")
        self.le_status.setPlaceholderText(QCoreApplication.translate("info_bug", u"[Status]", None))
        self.lbl_system.setText(QCoreApplication.translate("info_bug", u"System:", None))
        self.le_system.setText("")
        self.le_system.setPlaceholderText(QCoreApplication.translate("info_bug", u"[System]", None))
        self.lbl_version.setText(QCoreApplication.translate("info_bug", u"System version:", None))
        self.le_version.setText("")
        self.le_version.setPlaceholderText(QCoreApplication.translate("info_bug", u"[System version]", None))
        self.lbl_id.setText(QCoreApplication.translate("info_bug", u"Service now ID:", None))
        self.le_id.setText("")
        self.le_id.setPlaceholderText(QCoreApplication.translate("info_bug", u"[Service now ID]", None))
        self.lbl_creation.setText(QCoreApplication.translate("info_bug", u"Creation time:", None))
        self.le_creation.setText("")
        self.le_creation.setPlaceholderText(QCoreApplication.translate("info_bug", u"[Creation time]", None))
        self.lbl_update.setText(QCoreApplication.translate("info_bug", u"Last update:", None))
        self.le_update.setText("")
        self.le_update.setPlaceholderText(QCoreApplication.translate("info_bug", u"[Update time]", None))
        self.lbl_campaign.setText(QCoreApplication.translate("info_bug", u"Campaign:", None))
        self.le_campaign.setText("")
        self.le_campaign.setPlaceholderText(QCoreApplication.translate("info_bug", u"[Campaign]", None))
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
        self.tab_widget_bug.setTabText(self.tab_widget_bug.indexOf(self.tab_info), QCoreApplication.translate("info_bug", u"Bug info", None))

        __sortingEnabled = self.list_history.isSortingEnabled()
        self.list_history.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_history.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("info_bug", u"[Change in status:...]", None));
        self.list_history.setSortingEnabled(__sortingEnabled)

        self.tab_widget_bug.setTabText(self.tab_widget_bug.indexOf(self.tab_history), QCoreApplication.translate("info_bug", u"History", None))
        self.btn_close_bug.setText(QCoreApplication.translate("info_bug", u"Close bug", None))
        self.btn_edit_bug.setText(QCoreApplication.translate("info_bug", u"Edit bug", None))
        self.btn_delete_bug.setText(QCoreApplication.translate("info_bug", u"Delete bug", None))
        self.btn_back.setText(QCoreApplication.translate("info_bug", u"Back", None))
    # retranslateUi

