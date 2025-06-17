# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bug_info.ui'
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

class Ui_bug_info_form(object):
    def setupUi(self, bug_info_form):
        if not bug_info_form.objectName():
            bug_info_form.setObjectName(u"bug_info_form")
        bug_info_form.setEnabled(True)
        bug_info_form.resize(720, 510)
        self.verticalLayout = QVBoxLayout(bug_info_form)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, 25)
        self.bug_info_lbl = QLabel(bug_info_form)
        self.bug_info_lbl.setObjectName(u"bug_info_lbl")
        font = QFont()
        font.setPointSize(22)
        self.bug_info_lbl.setFont(font)
        self.bug_info_lbl.setWordWrap(True)

        self.verticalLayout.addWidget(self.bug_info_lbl)

        self.bugs_tab_wiget = QTabWidget(bug_info_form)
        self.bugs_tab_wiget.setObjectName(u"bugs_tab_wiget")
        self.bug_info_tab = QWidget()
        self.bug_info_tab.setObjectName(u"bug_info_tab")
        self.layoutWidget = QWidget(self.bug_info_tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 588, 24))
        self.status_hlayout = QHBoxLayout(self.layoutWidget)
        self.status_hlayout.setObjectName(u"status_hlayout")
        self.status_hlayout.setContentsMargins(0, 0, 0, 0)
        self.status_lbl = QLabel(self.layoutWidget)
        self.status_lbl.setObjectName(u"status_lbl")

        self.status_hlayout.addWidget(self.status_lbl)

        self.status_le = QLineEdit(self.layoutWidget)
        self.status_le.setObjectName(u"status_le")
        self.status_le.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.status_hlayout.addWidget(self.status_le)

        self.system_lbl = QLabel(self.layoutWidget)
        self.system_lbl.setObjectName(u"system_lbl")

        self.status_hlayout.addWidget(self.system_lbl)

        self.system_le = QLineEdit(self.layoutWidget)
        self.system_le.setObjectName(u"system_le")

        self.status_hlayout.addWidget(self.system_le)

        self.sys_version_lbl = QLabel(self.layoutWidget)
        self.sys_version_lbl.setObjectName(u"sys_version_lbl")

        self.status_hlayout.addWidget(self.sys_version_lbl)

        self.sys_version_le = QLineEdit(self.layoutWidget)
        self.sys_version_le.setObjectName(u"sys_version_le")

        self.status_hlayout.addWidget(self.sys_version_le)

        self.service_now_id_lbl = QLabel(self.layoutWidget)
        self.service_now_id_lbl.setObjectName(u"service_now_id_lbl")

        self.status_hlayout.addWidget(self.service_now_id_lbl)

        self.service_now_id_le = QLineEdit(self.layoutWidget)
        self.service_now_id_le.setObjectName(u"service_now_id_le")

        self.status_hlayout.addWidget(self.service_now_id_le)

        self.layoutWidget1 = QWidget(self.bug_info_tab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 50, 426, 24))
        self.date_hlayout = QHBoxLayout(self.layoutWidget1)
        self.date_hlayout.setObjectName(u"date_hlayout")
        self.date_hlayout.setContentsMargins(0, 0, 0, 0)
        self.creation_lbl = QLabel(self.layoutWidget1)
        self.creation_lbl.setObjectName(u"creation_lbl")

        self.date_hlayout.addWidget(self.creation_lbl)

        self.creation_le = QLineEdit(self.layoutWidget1)
        self.creation_le.setObjectName(u"creation_le")

        self.date_hlayout.addWidget(self.creation_le)

        self.update_lbl = QLabel(self.layoutWidget1)
        self.update_lbl.setObjectName(u"update_lbl")

        self.date_hlayout.addWidget(self.update_lbl)

        self.update_le = QLineEdit(self.layoutWidget1)
        self.update_le.setObjectName(u"update_le")

        self.date_hlayout.addWidget(self.update_le)

        self.layoutWidget2 = QWidget(self.bug_info_tab)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 90, 401, 24))
        self.campaign_hlayout = QHBoxLayout(self.layoutWidget2)
        self.campaign_hlayout.setObjectName(u"campaign_hlayout")
        self.campaign_hlayout.setContentsMargins(0, 0, 0, 0)
        self.campaign_lbl = QLabel(self.layoutWidget2)
        self.campaign_lbl.setObjectName(u"campaign_lbl")

        self.campaign_hlayout.addWidget(self.campaign_lbl)

        self.campaign_le = QLineEdit(self.layoutWidget2)
        self.campaign_le.setObjectName(u"campaign_le")

        self.campaign_hlayout.addWidget(self.campaign_le)

        self.requirements_lbl = QLabel(self.layoutWidget2)
        self.requirements_lbl.setObjectName(u"requirements_lbl")

        self.campaign_hlayout.addWidget(self.requirements_lbl)

        self.requirements_cb = QComboBox(self.layoutWidget2)
        self.requirements_cb.setObjectName(u"requirements_cb")

        self.campaign_hlayout.addWidget(self.requirements_cb)

        self.layoutWidget3 = QWidget(self.bug_info_tab)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 130, 242, 24))
        self.urgency_hlayout = QHBoxLayout(self.layoutWidget3)
        self.urgency_hlayout.setObjectName(u"urgency_hlayout")
        self.urgency_hlayout.setContentsMargins(0, 0, 0, 0)
        self.urgency_lbl = QLabel(self.layoutWidget3)
        self.urgency_lbl.setObjectName(u"urgency_lbl")

        self.urgency_hlayout.addWidget(self.urgency_lbl)

        self.urgency_cb = QComboBox(self.layoutWidget3)
        self.urgency_cb.addItem("")
        self.urgency_cb.addItem("")
        self.urgency_cb.addItem("")
        self.urgency_cb.setObjectName(u"urgency_cb")

        self.urgency_hlayout.addWidget(self.urgency_cb)

        self.impact_lbl = QLabel(self.layoutWidget3)
        self.impact_lbl.setObjectName(u"impact_lbl")

        self.urgency_hlayout.addWidget(self.impact_lbl)

        self.impact_cb = QComboBox(self.layoutWidget3)
        self.impact_cb.addItem("")
        self.impact_cb.addItem("")
        self.impact_cb.addItem("")
        self.impact_cb.setObjectName(u"impact_cb")

        self.urgency_hlayout.addWidget(self.impact_cb)

        self.layoutWidget4 = QWidget(self.bug_info_tab)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(20, 170, 621, 61))
        self.short_description_hlayout = QHBoxLayout(self.layoutWidget4)
        self.short_description_hlayout.setObjectName(u"short_description_hlayout")
        self.short_description_hlayout.setContentsMargins(0, 0, 0, 0)
        self.short_description_lbl = QLabel(self.layoutWidget4)
        self.short_description_lbl.setObjectName(u"short_description_lbl")

        self.short_description_hlayout.addWidget(self.short_description_lbl)

        self.short_description_le = QLineEdit(self.layoutWidget4)
        self.short_description_le.setObjectName(u"short_description_le")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.short_description_le.sizePolicy().hasHeightForWidth())
        self.short_description_le.setSizePolicy(sizePolicy)
        self.short_description_le.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.short_description_hlayout.addWidget(self.short_description_le)

        self.layoutWidget5 = QWidget(self.bug_info_tab)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(20, 243, 621, 101))
        self.definition_hlayout = QHBoxLayout(self.layoutWidget5)
        self.definition_hlayout.setObjectName(u"definition_hlayout")
        self.definition_hlayout.setContentsMargins(0, 0, 0, 0)
        self.definition_lbl = QLabel(self.layoutWidget5)
        self.definition_lbl.setObjectName(u"definition_lbl")

        self.definition_hlayout.addWidget(self.definition_lbl)

        self.lineEdit_8 = QLineEdit(self.layoutWidget5)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.definition_hlayout.addWidget(self.lineEdit_8)

        self.bugs_tab_wiget.addTab(self.bug_info_tab, "")
        self.bug_history_tab = QWidget()
        self.bug_history_tab.setObjectName(u"bug_history_tab")
        self.history_list = QListWidget(self.bug_history_tab)
        QListWidgetItem(self.history_list)
        self.history_list.setObjectName(u"history_list")
        self.history_list.setGeometry(QRect(0, 0, 651, 351))
        self.bugs_tab_wiget.addTab(self.bug_history_tab, "")

        self.verticalLayout.addWidget(self.bugs_tab_wiget)

        self.actions_hlayout = QHBoxLayout()
        self.actions_hlayout.setObjectName(u"actions_hlayout")
        self.actions_hlayout.setContentsMargins(300, -1, -1, -1)
        self.close_bug_btn = QPushButton(bug_info_form)
        self.close_bug_btn.setObjectName(u"close_bug_btn")

        self.actions_hlayout.addWidget(self.close_bug_btn)

        self.edit_bug_btn = QPushButton(bug_info_form)
        self.edit_bug_btn.setObjectName(u"edit_bug_btn")

        self.actions_hlayout.addWidget(self.edit_bug_btn)

        self.delete_bug_btn = QPushButton(bug_info_form)
        self.delete_bug_btn.setObjectName(u"delete_bug_btn")

        self.actions_hlayout.addWidget(self.delete_bug_btn)

        self.back_btn = QPushButton(bug_info_form)
        self.back_btn.setObjectName(u"back_btn")

        self.actions_hlayout.addWidget(self.back_btn)


        self.verticalLayout.addLayout(self.actions_hlayout)


        self.retranslateUi(bug_info_form)

        self.bugs_tab_wiget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(bug_info_form)
    # setupUi

    def retranslateUi(self, bug_info_form):
        bug_info_form.setWindowTitle(QCoreApplication.translate("bug_info_form", u"Form", None))
        self.bug_info_lbl.setText(QCoreApplication.translate("bug_info_form", u"[Bug name]", None))
        self.status_lbl.setText(QCoreApplication.translate("bug_info_form", u"Status:", None))
        self.status_le.setText("")
        self.status_le.setPlaceholderText(QCoreApplication.translate("bug_info_form", u"[Status]", None))
        self.system_lbl.setText(QCoreApplication.translate("bug_info_form", u"System:", None))
        self.system_le.setText("")
        self.system_le.setPlaceholderText(QCoreApplication.translate("bug_info_form", u"[System]", None))
        self.sys_version_lbl.setText(QCoreApplication.translate("bug_info_form", u"System version:", None))
        self.sys_version_le.setText("")
        self.sys_version_le.setPlaceholderText(QCoreApplication.translate("bug_info_form", u"[System version]", None))
        self.service_now_id_lbl.setText(QCoreApplication.translate("bug_info_form", u"Service now ID:", None))
        self.service_now_id_le.setText("")
        self.service_now_id_le.setPlaceholderText(QCoreApplication.translate("bug_info_form", u"[Service now ID]", None))
        self.creation_lbl.setText(QCoreApplication.translate("bug_info_form", u"Creation time:", None))
        self.creation_le.setText("")
        self.creation_le.setPlaceholderText(QCoreApplication.translate("bug_info_form", u"[Creation time]", None))
        self.update_lbl.setText(QCoreApplication.translate("bug_info_form", u"Last update:", None))
        self.update_le.setText("")
        self.update_le.setPlaceholderText(QCoreApplication.translate("bug_info_form", u"[Update time]", None))
        self.campaign_lbl.setText(QCoreApplication.translate("bug_info_form", u"Campaign:", None))
        self.campaign_le.setText("")
        self.campaign_le.setPlaceholderText(QCoreApplication.translate("bug_info_form", u"[Campaign]", None))
        self.requirements_lbl.setText(QCoreApplication.translate("bug_info_form", u"Requirements affected:", None))
        self.urgency_lbl.setText(QCoreApplication.translate("bug_info_form", u"Urgency:", None))
        self.urgency_cb.setItemText(0, QCoreApplication.translate("bug_info_form", u"Low (1)", None))
        self.urgency_cb.setItemText(1, QCoreApplication.translate("bug_info_form", u"Medium (2)", None))
        self.urgency_cb.setItemText(2, QCoreApplication.translate("bug_info_form", u"High (3)", None))

        self.impact_lbl.setText(QCoreApplication.translate("bug_info_form", u"Impact:", None))
        self.impact_cb.setItemText(0, QCoreApplication.translate("bug_info_form", u"Low (1)", None))
        self.impact_cb.setItemText(1, QCoreApplication.translate("bug_info_form", u"Medium (2)", None))
        self.impact_cb.setItemText(2, QCoreApplication.translate("bug_info_form", u"High (3)", None))

        self.short_description_lbl.setText(QCoreApplication.translate("bug_info_form", u"Short description: ", None))
        self.short_description_le.setText("")
        self.short_description_le.setPlaceholderText(QCoreApplication.translate("bug_info_form", u"[Short decription]", None))
        self.definition_lbl.setText(QCoreApplication.translate("bug_info_form", u"Definition:", None))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("bug_info_form", u"[Definition]", None))
        self.bugs_tab_wiget.setTabText(self.bugs_tab_wiget.indexOf(self.bug_info_tab), QCoreApplication.translate("bug_info_form", u"Bug info", None))

        __sortingEnabled = self.history_list.isSortingEnabled()
        self.history_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.history_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("bug_info_form", u"[Change in status:...]", None));
        self.history_list.setSortingEnabled(__sortingEnabled)

        self.bugs_tab_wiget.setTabText(self.bugs_tab_wiget.indexOf(self.bug_history_tab), QCoreApplication.translate("bug_info_form", u"History", None))
        self.close_bug_btn.setText(QCoreApplication.translate("bug_info_form", u"Close bug", None))
        self.edit_bug_btn.setText(QCoreApplication.translate("bug_info_form", u"Edit bug", None))
        self.delete_bug_btn.setText(QCoreApplication.translate("bug_info_form", u"Delete bug", None))
        self.back_btn.setText(QCoreApplication.translate("bug_info_form", u"Back", None))
    # retranslateUi

