# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QTabWidget, QTableView,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(882, 647)
        self.action_add_bug = QAction(main_window)
        self.action_add_bug.setObjectName(u"action_add_bug")
        self.action_view_bugs = QAction(main_window)
        self.action_view_bugs.setObjectName(u"action_view_bugs")
        self.action_new_campaign = QAction(main_window)
        self.action_new_campaign.setObjectName(u"action_new_campaign")
        self.action_view_campaigns = QAction(main_window)
        self.action_view_campaigns.setObjectName(u"action_view_campaigns")
        self.action = QAction(main_window)
        self.action.setObjectName(u"action")
        self.action_view_cases = QAction(main_window)
        self.action_view_cases.setObjectName(u"action_view_cases")
        self.action_new_requirement = QAction(main_window)
        self.action_new_requirement.setObjectName(u"action_new_requirement")
        self.action_view_requirements = QAction(main_window)
        self.action_view_requirements.setObjectName(u"action_view_requirements")
        self.action_view_assets = QAction(main_window)
        self.action_view_assets.setObjectName(u"action_view_assets")
        self.action_new_email = QAction(main_window)
        self.action_new_email.setObjectName(u"action_new_email")
        self.action_new_operator = QAction(main_window)
        self.action_new_operator.setObjectName(u"action_new_operator")
        self.action_new_drone = QAction(main_window)
        self.action_new_drone.setObjectName(u"action_new_drone")
        self.action_new_uas_zone = QAction(main_window)
        self.action_new_uas_zone.setObjectName(u"action_new_uas_zone")
        self.action_new_uhub_organization = QAction(main_window)
        self.action_new_uhub_organization.setObjectName(u"action_new_uhub_organization")
        self.action_new_uhub_user = QAction(main_window)
        self.action_new_uhub_user.setObjectName(u"action_new_uhub_user")
        self.action_new_uspace = QAction(main_window)
        self.action_new_uspace.setObjectName(u"action_new_uspace")
        self.action_new_case = QAction(main_window)
        self.action_new_case.setObjectName(u"action_new_case")
        self.action_new_block = QAction(main_window)
        self.action_new_block.setObjectName(u"action_new_block")
        self.central_main = QWidget(main_window)
        self.central_main.setObjectName(u"central_main")
        self.verticalLayout = QVBoxLayout(self.central_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.stacked_main = QStackedWidget(self.central_main)
        self.stacked_main.setObjectName(u"stacked_main")
        self.pg_bugs = QWidget()
        self.pg_bugs.setObjectName(u"pg_bugs")
        self.verticalLayout_2 = QVBoxLayout(self.pg_bugs)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_bugs = QLabel(self.pg_bugs)
        self.lbl_bugs.setObjectName(u"lbl_bugs")
        font = QFont()
        font.setPointSize(28)
        self.lbl_bugs.setFont(font)

        self.verticalLayout_2.addWidget(self.lbl_bugs)

        self.hlayout_filter_bugs = QHBoxLayout()
        self.hlayout_filter_bugs.setSpacing(10)
        self.hlayout_filter_bugs.setObjectName(u"hlayout_filter_bugs")
        self.hlayout_filter_bugs.setContentsMargins(5, -1, 150, -1)
        self.le_search_bug = QLineEdit(self.pg_bugs)
        self.le_search_bug.setObjectName(u"le_search_bug")

        self.hlayout_filter_bugs.addWidget(self.le_search_bug)

        self.cb_search_bug = QComboBox(self.pg_bugs)
        self.cb_search_bug.addItem("")
        self.cb_search_bug.addItem("")
        self.cb_search_bug.setObjectName(u"cb_search_bug")

        self.hlayout_filter_bugs.addWidget(self.cb_search_bug)

        self.lbl_filterby_status = QLabel(self.pg_bugs)
        self.lbl_filterby_status.setObjectName(u"lbl_filterby_status")

        self.hlayout_filter_bugs.addWidget(self.lbl_filterby_status)

        self.cb_filter_status = QComboBox(self.pg_bugs)
        self.cb_filter_status.setObjectName(u"cb_filter_status")

        self.hlayout_filter_bugs.addWidget(self.cb_filter_status)

        self.cb_filter_system = QComboBox(self.pg_bugs)
        self.cb_filter_system.setObjectName(u"cb_filter_system")

        self.hlayout_filter_bugs.addWidget(self.cb_filter_system)

        self.hlayout_filter_bugs.setStretch(0, 25)
        self.hlayout_filter_bugs.setStretch(1, 10)
        self.hlayout_filter_bugs.setStretch(2, 2)

        self.verticalLayout_2.addLayout(self.hlayout_filter_bugs)

        self.tbl_bugs = QTableView(self.pg_bugs)
        self.tbl_bugs.setObjectName(u"tbl_bugs")
        self.tbl_bugs.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tbl_bugs.setCornerButtonEnabled(False)

        self.verticalLayout_2.addWidget(self.tbl_bugs)

        self.stacked_main.addWidget(self.pg_bugs)
        self.pg_campaigns = QWidget()
        self.pg_campaigns.setObjectName(u"pg_campaigns")
        self.verticalLayout_3 = QVBoxLayout(self.pg_campaigns)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_campaigns = QLabel(self.pg_campaigns)
        self.lbl_campaigns.setObjectName(u"lbl_campaigns")
        self.lbl_campaigns.setFont(font)

        self.verticalLayout_3.addWidget(self.lbl_campaigns)

        self.tbl_campaigns = QTableWidget(self.pg_campaigns)
        if (self.tbl_campaigns.columnCount() < 11):
            self.tbl_campaigns.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_campaigns.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_campaigns.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_campaigns.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_campaigns.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_campaigns.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_campaigns.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_campaigns.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_campaigns.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_campaigns.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbl_campaigns.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbl_campaigns.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        if (self.tbl_campaigns.rowCount() < 4):
            self.tbl_campaigns.setRowCount(4)
        self.tbl_campaigns.setObjectName(u"tbl_campaigns")
        self.tbl_campaigns.setRowCount(4)

        self.verticalLayout_3.addWidget(self.tbl_campaigns)

        self.stacked_main.addWidget(self.pg_campaigns)
        self.pg_test_management = QWidget()
        self.pg_test_management.setObjectName(u"pg_test_management")
        self.verticalLayout_12 = QVBoxLayout(self.pg_test_management)
        self.verticalLayout_12.setSpacing(15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lbl_management = QLabel(self.pg_test_management)
        self.lbl_management.setObjectName(u"lbl_management")
        self.lbl_management.setFont(font)

        self.verticalLayout_12.addWidget(self.lbl_management)

        self.tab_widget_management = QTabWidget(self.pg_test_management)
        self.tab_widget_management.setObjectName(u"tab_widget_management")
        self.tab_cases = QWidget()
        self.tab_cases.setObjectName(u"tab_cases")
        self.verticalLayout_13 = QVBoxLayout(self.tab_cases)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.tbl_cases = QTableWidget(self.tab_cases)
        if (self.tbl_cases.columnCount() < 6):
            self.tbl_cases.setColumnCount(6)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbl_cases.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbl_cases.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tbl_cases.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbl_cases.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tbl_cases.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tbl_cases.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        if (self.tbl_cases.rowCount() < 4):
            self.tbl_cases.setRowCount(4)
        self.tbl_cases.setObjectName(u"tbl_cases")
        self.tbl_cases.setRowCount(4)

        self.verticalLayout_13.addWidget(self.tbl_cases)

        self.tab_widget_management.addTab(self.tab_cases, "")
        self.tab_blocks = QWidget()
        self.tab_blocks.setObjectName(u"tab_blocks")
        self.verticalLayout_14 = QVBoxLayout(self.tab_blocks)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.tbl_blocks = QTableWidget(self.tab_blocks)
        if (self.tbl_blocks.columnCount() < 5):
            self.tbl_blocks.setColumnCount(5)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tbl_blocks.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tbl_blocks.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tbl_blocks.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tbl_blocks.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tbl_blocks.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        if (self.tbl_blocks.rowCount() < 4):
            self.tbl_blocks.setRowCount(4)
        self.tbl_blocks.setObjectName(u"tbl_blocks")
        self.tbl_blocks.setRowCount(4)

        self.verticalLayout_14.addWidget(self.tbl_blocks)

        self.tab_widget_management.addTab(self.tab_blocks, "")

        self.verticalLayout_12.addWidget(self.tab_widget_management)

        self.stacked_main.addWidget(self.pg_test_management)
        self.pg_requirements = QWidget()
        self.pg_requirements.setObjectName(u"pg_requirements")
        self.verticalLayout_4 = QVBoxLayout(self.pg_requirements)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_requirements = QLabel(self.pg_requirements)
        self.lbl_requirements.setObjectName(u"lbl_requirements")
        self.lbl_requirements.setFont(font)

        self.verticalLayout_4.addWidget(self.lbl_requirements)

        self.hlayout_search_requirements = QHBoxLayout()
        self.hlayout_search_requirements.setSpacing(10)
        self.hlayout_search_requirements.setObjectName(u"hlayout_search_requirements")
        self.hlayout_search_requirements.setContentsMargins(5, -1, 150, -1)
        self.le_search_requirement = QLineEdit(self.pg_requirements)
        self.le_search_requirement.setObjectName(u"le_search_requirement")

        self.hlayout_search_requirements.addWidget(self.le_search_requirement)

        self.lbl_filterby_system = QLabel(self.pg_requirements)
        self.lbl_filterby_system.setObjectName(u"lbl_filterby_system")

        self.hlayout_search_requirements.addWidget(self.lbl_filterby_system)

        self.cb_system = QComboBox(self.pg_requirements)
        self.cb_system.setObjectName(u"cb_system")

        self.hlayout_search_requirements.addWidget(self.cb_system)


        self.verticalLayout_4.addLayout(self.hlayout_search_requirements)

        self.tbl_requirements = QTableWidget(self.pg_requirements)
        if (self.tbl_requirements.columnCount() < 6):
            self.tbl_requirements.setColumnCount(6)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tbl_requirements.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tbl_requirements.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tbl_requirements.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tbl_requirements.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tbl_requirements.setHorizontalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tbl_requirements.setHorizontalHeaderItem(5, __qtablewidgetitem27)
        if (self.tbl_requirements.rowCount() < 4):
            self.tbl_requirements.setRowCount(4)
        self.tbl_requirements.setObjectName(u"tbl_requirements")
        self.tbl_requirements.setRowCount(4)

        self.verticalLayout_4.addWidget(self.tbl_requirements)

        self.stacked_main.addWidget(self.pg_requirements)
        self.pg_assets = QWidget()
        self.pg_assets.setObjectName(u"pg_assets")
        self.verticalLayout_5 = QVBoxLayout(self.pg_assets)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.title_assets = QLabel(self.pg_assets)
        self.title_assets.setObjectName(u"title_assets")
        self.title_assets.setFont(font)

        self.verticalLayout_5.addWidget(self.title_assets)

        self.tab_widget_assets = QTabWidget(self.pg_assets)
        self.tab_widget_assets.setObjectName(u"tab_widget_assets")
        self.tab_email = QWidget()
        self.tab_email.setObjectName(u"tab_email")
        self.verticalLayout_15 = QVBoxLayout(self.tab_email)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.tabl_email = QTableWidget(self.tab_email)
        if (self.tabl_email.columnCount() < 3):
            self.tabl_email.setColumnCount(3)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tabl_email.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tabl_email.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tabl_email.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        if (self.tabl_email.rowCount() < 4):
            self.tabl_email.setRowCount(4)
        self.tabl_email.setObjectName(u"tabl_email")
        self.tabl_email.setRowCount(4)

        self.verticalLayout_15.addWidget(self.tabl_email)

        self.tab_widget_assets.addTab(self.tab_email, "")
        self.tab_operators = QWidget()
        self.tab_operators.setObjectName(u"tab_operators")
        self.verticalLayout_6 = QVBoxLayout(self.tab_operators)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tbl_operators = QTableWidget(self.tab_operators)
        if (self.tbl_operators.columnCount() < 6):
            self.tbl_operators.setColumnCount(6)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tbl_operators.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tbl_operators.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tbl_operators.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tbl_operators.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tbl_operators.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tbl_operators.setHorizontalHeaderItem(5, __qtablewidgetitem36)
        if (self.tbl_operators.rowCount() < 4):
            self.tbl_operators.setRowCount(4)
        self.tbl_operators.setObjectName(u"tbl_operators")
        self.tbl_operators.setRowCount(4)

        self.verticalLayout_6.addWidget(self.tbl_operators)

        self.tab_widget_assets.addTab(self.tab_operators, "")
        self.tab_drones = QWidget()
        self.tab_drones.setObjectName(u"tab_drones")
        self.verticalLayout_7 = QVBoxLayout(self.tab_drones)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tbl_drones = QTableWidget(self.tab_drones)
        if (self.tbl_drones.columnCount() < 7):
            self.tbl_drones.setColumnCount(7)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tbl_drones.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tbl_drones.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tbl_drones.setHorizontalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tbl_drones.setHorizontalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tbl_drones.setHorizontalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tbl_drones.setHorizontalHeaderItem(5, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tbl_drones.setHorizontalHeaderItem(6, __qtablewidgetitem43)
        if (self.tbl_drones.rowCount() < 4):
            self.tbl_drones.setRowCount(4)
        self.tbl_drones.setObjectName(u"tbl_drones")
        self.tbl_drones.setRowCount(4)

        self.verticalLayout_7.addWidget(self.tbl_drones)

        self.tab_widget_assets.addTab(self.tab_drones, "")
        self.tab_uas_zones = QWidget()
        self.tab_uas_zones.setObjectName(u"tab_uas_zones")
        self.verticalLayout_8 = QVBoxLayout(self.tab_uas_zones)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.tbl_uas_zones = QTableWidget(self.tab_uas_zones)
        if (self.tbl_uas_zones.columnCount() < 6):
            self.tbl_uas_zones.setColumnCount(6)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tbl_uas_zones.setHorizontalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tbl_uas_zones.setHorizontalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tbl_uas_zones.setHorizontalHeaderItem(2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tbl_uas_zones.setHorizontalHeaderItem(3, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tbl_uas_zones.setHorizontalHeaderItem(4, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tbl_uas_zones.setHorizontalHeaderItem(5, __qtablewidgetitem49)
        if (self.tbl_uas_zones.rowCount() < 4):
            self.tbl_uas_zones.setRowCount(4)
        self.tbl_uas_zones.setObjectName(u"tbl_uas_zones")
        self.tbl_uas_zones.setRowCount(4)

        self.verticalLayout_8.addWidget(self.tbl_uas_zones)

        self.tab_widget_assets.addTab(self.tab_uas_zones, "")
        self.tab_uhub_org = QWidget()
        self.tab_uhub_org.setObjectName(u"tab_uhub_org")
        self.verticalLayout_9 = QVBoxLayout(self.tab_uhub_org)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tbl_uhub_org = QTableWidget(self.tab_uhub_org)
        if (self.tbl_uhub_org.columnCount() < 6):
            self.tbl_uhub_org.setColumnCount(6)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tbl_uhub_org.setHorizontalHeaderItem(0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tbl_uhub_org.setHorizontalHeaderItem(1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tbl_uhub_org.setHorizontalHeaderItem(2, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tbl_uhub_org.setHorizontalHeaderItem(3, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tbl_uhub_org.setHorizontalHeaderItem(4, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tbl_uhub_org.setHorizontalHeaderItem(5, __qtablewidgetitem55)
        if (self.tbl_uhub_org.rowCount() < 4):
            self.tbl_uhub_org.setRowCount(4)
        self.tbl_uhub_org.setObjectName(u"tbl_uhub_org")
        self.tbl_uhub_org.setRowCount(4)

        self.verticalLayout_9.addWidget(self.tbl_uhub_org)

        self.tab_widget_assets.addTab(self.tab_uhub_org, "")
        self.tab_uhub_user = QWidget()
        self.tab_uhub_user.setObjectName(u"tab_uhub_user")
        self.verticalLayout_10 = QVBoxLayout(self.tab_uhub_user)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.tbl_uhub_user = QTableWidget(self.tab_uhub_user)
        if (self.tbl_uhub_user.columnCount() < 7):
            self.tbl_uhub_user.setColumnCount(7)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tbl_uhub_user.setHorizontalHeaderItem(0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tbl_uhub_user.setHorizontalHeaderItem(1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tbl_uhub_user.setHorizontalHeaderItem(2, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tbl_uhub_user.setHorizontalHeaderItem(3, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tbl_uhub_user.setHorizontalHeaderItem(4, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tbl_uhub_user.setHorizontalHeaderItem(5, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tbl_uhub_user.setHorizontalHeaderItem(6, __qtablewidgetitem62)
        if (self.tbl_uhub_user.rowCount() < 4):
            self.tbl_uhub_user.setRowCount(4)
        self.tbl_uhub_user.setObjectName(u"tbl_uhub_user")
        self.tbl_uhub_user.setRowCount(4)

        self.verticalLayout_10.addWidget(self.tbl_uhub_user)

        self.tab_widget_assets.addTab(self.tab_uhub_user, "")
        self.tab_uspaces = QWidget()
        self.tab_uspaces.setObjectName(u"tab_uspaces")
        self.verticalLayout_11 = QVBoxLayout(self.tab_uspaces)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.tbl_uspaces = QTableWidget(self.tab_uspaces)
        if (self.tbl_uspaces.columnCount() < 4):
            self.tbl_uspaces.setColumnCount(4)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tbl_uspaces.setHorizontalHeaderItem(0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tbl_uspaces.setHorizontalHeaderItem(1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tbl_uspaces.setHorizontalHeaderItem(2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tbl_uspaces.setHorizontalHeaderItem(3, __qtablewidgetitem66)
        if (self.tbl_uspaces.rowCount() < 4):
            self.tbl_uspaces.setRowCount(4)
        self.tbl_uspaces.setObjectName(u"tbl_uspaces")
        self.tbl_uspaces.setRowCount(4)

        self.verticalLayout_11.addWidget(self.tbl_uspaces)

        self.tab_widget_assets.addTab(self.tab_uspaces, "")

        self.verticalLayout_5.addWidget(self.tab_widget_assets)

        self.stacked_main.addWidget(self.pg_assets)

        self.verticalLayout.addWidget(self.stacked_main)

        self.hlayout_btn = QHBoxLayout()
        self.hlayout_btn.setObjectName(u"hlayout_btn")
        self.hlayout_btn.setContentsMargins(475, -1, -1, -1)
        self.btn_start = QPushButton(self.central_main)
        self.btn_start.setObjectName(u"btn_start")

        self.hlayout_btn.addWidget(self.btn_start)

        self.btn_add = QPushButton(self.central_main)
        self.btn_add.setObjectName(u"btn_add")

        self.hlayout_btn.addWidget(self.btn_add)

        self.btn_edit = QPushButton(self.central_main)
        self.btn_edit.setObjectName(u"btn_edit")

        self.hlayout_btn.addWidget(self.btn_edit)

        self.btn_remove = QPushButton(self.central_main)
        self.btn_remove.setObjectName(u"btn_remove")

        self.hlayout_btn.addWidget(self.btn_remove)


        self.verticalLayout.addLayout(self.hlayout_btn)

        main_window.setCentralWidget(self.central_main)
        self.menu_bar_main = QMenuBar(main_window)
        self.menu_bar_main.setObjectName(u"menu_bar_main")
        self.menu_bar_main.setGeometry(QRect(0, 0, 882, 33))
        self.menu_bugs = QMenu(self.menu_bar_main)
        self.menu_bugs.setObjectName(u"menu_bugs")
        self.menu_campaigns = QMenu(self.menu_bar_main)
        self.menu_campaigns.setObjectName(u"menu_campaigns")
        self.menu_cases = QMenu(self.menu_bar_main)
        self.menu_cases.setObjectName(u"menu_cases")
        self.menu_new_test = QMenu(self.menu_cases)
        self.menu_new_test.setObjectName(u"menu_new_test")
        self.menu_requirements = QMenu(self.menu_bar_main)
        self.menu_requirements.setObjectName(u"menu_requirements")
        self.menu_assets = QMenu(self.menu_bar_main)
        self.menu_assets.setObjectName(u"menu_assets")
        self.menu_new_asset = QMenu(self.menu_assets)
        self.menu_new_asset.setObjectName(u"menu_new_asset")
        self.menu_statistics = QMenu(self.menu_bar_main)
        self.menu_statistics.setObjectName(u"menu_statistics")
        main_window.setMenuBar(self.menu_bar_main)
        self.status_bar = QStatusBar(main_window)
        self.status_bar.setObjectName(u"status_bar")
        main_window.setStatusBar(self.status_bar)

        self.menu_bar_main.addAction(self.menu_bugs.menuAction())
        self.menu_bar_main.addAction(self.menu_campaigns.menuAction())
        self.menu_bar_main.addAction(self.menu_cases.menuAction())
        self.menu_bar_main.addAction(self.menu_requirements.menuAction())
        self.menu_bar_main.addAction(self.menu_assets.menuAction())
        self.menu_bar_main.addAction(self.menu_statistics.menuAction())
        self.menu_bugs.addAction(self.action_add_bug)
        self.menu_bugs.addAction(self.action_view_bugs)
        self.menu_campaigns.addAction(self.action_new_campaign)
        self.menu_campaigns.addAction(self.action_view_campaigns)
        self.menu_cases.addAction(self.menu_new_test.menuAction())
        self.menu_cases.addAction(self.action_view_cases)
        self.menu_new_test.addAction(self.action_new_case)
        self.menu_new_test.addAction(self.action_new_block)
        self.menu_requirements.addAction(self.action_new_requirement)
        self.menu_requirements.addAction(self.action_view_requirements)
        self.menu_assets.addAction(self.menu_new_asset.menuAction())
        self.menu_assets.addAction(self.action_view_assets)
        self.menu_new_asset.addAction(self.action_new_email)
        self.menu_new_asset.addAction(self.action_new_operator)
        self.menu_new_asset.addAction(self.action_new_drone)
        self.menu_new_asset.addAction(self.action_new_uas_zone)
        self.menu_new_asset.addAction(self.action_new_uhub_organization)
        self.menu_new_asset.addAction(self.action_new_uhub_user)
        self.menu_new_asset.addAction(self.action_new_uspace)

        self.retranslateUi(main_window)

        self.stacked_main.setCurrentIndex(0)
        self.tab_widget_management.setCurrentIndex(0)
        self.tab_widget_assets.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"MainWindow", None))
        self.action_add_bug.setText(QCoreApplication.translate("main_window", u"New bug", None))
        self.action_view_bugs.setText(QCoreApplication.translate("main_window", u"View bugs", None))
        self.action_new_campaign.setText(QCoreApplication.translate("main_window", u"New campaign", None))
        self.action_view_campaigns.setText(QCoreApplication.translate("main_window", u"View campaigns", None))
        self.action.setText(QCoreApplication.translate("main_window", u"New test block", None))
        self.action_view_cases.setText(QCoreApplication.translate("main_window", u"View cases", None))
        self.action_new_requirement.setText(QCoreApplication.translate("main_window", u"New requirement", None))
        self.action_view_requirements.setText(QCoreApplication.translate("main_window", u"View requirements", None))
        self.action_view_assets.setText(QCoreApplication.translate("main_window", u"View assets", None))
        self.action_new_email.setText(QCoreApplication.translate("main_window", u"Email", None))
        self.action_new_operator.setText(QCoreApplication.translate("main_window", u"Operator", None))
        self.action_new_drone.setText(QCoreApplication.translate("main_window", u"Drone", None))
        self.action_new_uas_zone.setText(QCoreApplication.translate("main_window", u"UAS Zone", None))
        self.action_new_uhub_organization.setText(QCoreApplication.translate("main_window", u"U-hub organization", None))
        self.action_new_uhub_user.setText(QCoreApplication.translate("main_window", u"U-hub user", None))
        self.action_new_uspace.setText(QCoreApplication.translate("main_window", u"U-space", None))
        self.action_new_case.setText(QCoreApplication.translate("main_window", u"Test case", None))
        self.action_new_block.setText(QCoreApplication.translate("main_window", u"Test block", None))
        self.lbl_bugs.setText(QCoreApplication.translate("main_window", u"Bugs List", None))
        self.le_search_bug.setPlaceholderText(QCoreApplication.translate("main_window", u"Search by...", None))
        self.cb_search_bug.setItemText(0, QCoreApplication.translate("main_window", u"Service now ID", None))
        self.cb_search_bug.setItemText(1, QCoreApplication.translate("main_window", u"Short description", None))

        self.lbl_filterby_status.setText(QCoreApplication.translate("main_window", u"Filter by:", None))
        self.cb_filter_status.setPlaceholderText(QCoreApplication.translate("main_window", u"Status", None))
        self.cb_filter_system.setPlaceholderText(QCoreApplication.translate("main_window", u"System", None))
        self.lbl_campaigns.setText(QCoreApplication.translate("main_window", u"Test campaigns", None))
        ___qtablewidgetitem = self.tbl_campaigns.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("main_window", u"Id", None));
        ___qtablewidgetitem1 = self.tbl_campaigns.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("main_window", u"Description", None));
        ___qtablewidgetitem2 = self.tbl_campaigns.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("main_window", u"System", None));
        ___qtablewidgetitem3 = self.tbl_campaigns.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("main_window", u"Version", None));
        ___qtablewidgetitem4 = self.tbl_campaigns.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("main_window", u"Test blocks", None));
        ___qtablewidgetitem5 = self.tbl_campaigns.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("main_window", u"Passed", None));
        ___qtablewidgetitem6 = self.tbl_campaigns.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("main_window", u"Success", None));
        ___qtablewidgetitem7 = self.tbl_campaigns.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("main_window", u"Creation date", None));
        ___qtablewidgetitem8 = self.tbl_campaigns.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("main_window", u"Start date", None));
        ___qtablewidgetitem9 = self.tbl_campaigns.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("main_window", u"End date", None));
        ___qtablewidgetitem10 = self.tbl_campaigns.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("main_window", u"Last update", None));
        self.lbl_management.setText(QCoreApplication.translate("main_window", u"Test management", None))
        ___qtablewidgetitem11 = self.tbl_cases.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("main_window", u"Id", None));
        ___qtablewidgetitem12 = self.tbl_cases.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("main_window", u"Name", None));
        ___qtablewidgetitem13 = self.tbl_cases.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("main_window", u"System", None));
        ___qtablewidgetitem14 = self.tbl_cases.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("main_window", u"Assets", None));
        ___qtablewidgetitem15 = self.tbl_cases.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("main_window", u"Steps", None));
        ___qtablewidgetitem16 = self.tbl_cases.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("main_window", u"Comments", None));
        self.tab_widget_management.setTabText(self.tab_widget_management.indexOf(self.tab_cases), QCoreApplication.translate("main_window", u"Cases", None))
        ___qtablewidgetitem17 = self.tbl_blocks.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("main_window", u"Id", None));
        ___qtablewidgetitem18 = self.tbl_blocks.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("main_window", u"Name", None));
        ___qtablewidgetitem19 = self.tbl_blocks.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("main_window", u"System(s)", None));
        ___qtablewidgetitem20 = self.tbl_blocks.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("main_window", u"Cases", None));
        ___qtablewidgetitem21 = self.tbl_blocks.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("main_window", u"Comments", None));
        self.tab_widget_management.setTabText(self.tab_widget_management.indexOf(self.tab_blocks), QCoreApplication.translate("main_window", u"Blocks", None))
        self.lbl_requirements.setText(QCoreApplication.translate("main_window", u"Requirements", None))
        self.le_search_requirement.setPlaceholderText(QCoreApplication.translate("main_window", u"Search by ID...", None))
        self.lbl_filterby_system.setText(QCoreApplication.translate("main_window", u"Filter by:", None))
        self.cb_system.setPlaceholderText(QCoreApplication.translate("main_window", u"System", None))
        ___qtablewidgetitem22 = self.tbl_requirements.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("main_window", u"Id", None));
        ___qtablewidgetitem23 = self.tbl_requirements.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("main_window", u"System", None));
        ___qtablewidgetitem24 = self.tbl_requirements.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("main_window", u"Section", None));
        ___qtablewidgetitem25 = self.tbl_requirements.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("main_window", u"Definition", None));
        ___qtablewidgetitem26 = self.tbl_requirements.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("main_window", u"Creation date", None));
        ___qtablewidgetitem27 = self.tbl_requirements.horizontalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("main_window", u"Last update", None));
        self.title_assets.setText(QCoreApplication.translate("main_window", u"Assets management", None))
        ___qtablewidgetitem28 = self.tabl_email.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("main_window", u"Name", None));
        ___qtablewidgetitem29 = self.tabl_email.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("main_window", u"Email", None));
        ___qtablewidgetitem30 = self.tabl_email.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("main_window", u"Password", None));
        self.tab_widget_assets.setTabText(self.tab_widget_assets.indexOf(self.tab_email), QCoreApplication.translate("main_window", u"Emails", None))
        ___qtablewidgetitem31 = self.tbl_operators.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("main_window", u"Name", None));
        ___qtablewidgetitem32 = self.tbl_operators.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("main_window", u"EASA ID", None));
        ___qtablewidgetitem33 = self.tbl_operators.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("main_window", u"Verification code", None));
        ___qtablewidgetitem34 = self.tbl_operators.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("main_window", u"Email", None));
        ___qtablewidgetitem35 = self.tbl_operators.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("main_window", u"Password", None));
        ___qtablewidgetitem36 = self.tbl_operators.horizontalHeaderItem(5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("main_window", u"Phone", None));
        self.tab_widget_assets.setTabText(self.tab_widget_assets.indexOf(self.tab_operators), QCoreApplication.translate("main_window", u"Operators", None))
        ___qtablewidgetitem37 = self.tbl_drones.horizontalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("main_window", u"Operator", None));
        ___qtablewidgetitem38 = self.tbl_drones.horizontalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("main_window", u"Name", None));
        ___qtablewidgetitem39 = self.tbl_drones.horizontalHeaderItem(2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("main_window", u"Serial Number", None));
        ___qtablewidgetitem40 = self.tbl_drones.horizontalHeaderItem(3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("main_window", u"Manufacturer", None));
        ___qtablewidgetitem41 = self.tbl_drones.horizontalHeaderItem(4)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("main_window", u"Model", None));
        ___qtablewidgetitem42 = self.tbl_drones.horizontalHeaderItem(5)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("main_window", u"Tracker type", None));
        ___qtablewidgetitem43 = self.tbl_drones.horizontalHeaderItem(6)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("main_window", u"Transponder ID", None));
        self.tab_widget_assets.setTabText(self.tab_widget_assets.indexOf(self.tab_drones), QCoreApplication.translate("main_window", u"Drones", None))
        ___qtablewidgetitem44 = self.tbl_uas_zones.horizontalHeaderItem(0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("main_window", u"Name", None));
        ___qtablewidgetitem45 = self.tbl_uas_zones.horizontalHeaderItem(1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("main_window", u"Reason", None));
        ___qtablewidgetitem46 = self.tbl_uas_zones.horizontalHeaderItem(2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("main_window", u"Cause", None));
        ___qtablewidgetitem47 = self.tbl_uas_zones.horizontalHeaderItem(3)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("main_window", u"Restriction type", None));
        ___qtablewidgetitem48 = self.tbl_uas_zones.horizontalHeaderItem(4)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("main_window", u"Activaci\u00f3n time", None));
        ___qtablewidgetitem49 = self.tbl_uas_zones.horizontalHeaderItem(5)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("main_window", u"Authority", None));
        self.tab_widget_assets.setTabText(self.tab_widget_assets.indexOf(self.tab_uas_zones), QCoreApplication.translate("main_window", u"UAS Zones", None))
        ___qtablewidgetitem50 = self.tbl_uhub_org.horizontalHeaderItem(0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("main_window", u"Name", None));
        ___qtablewidgetitem51 = self.tbl_uhub_org.horizontalHeaderItem(1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("main_window", u"Role", None));
        ___qtablewidgetitem52 = self.tbl_uhub_org.horizontalHeaderItem(2)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("main_window", u"Jurisdiction", None));
        ___qtablewidgetitem53 = self.tbl_uhub_org.horizontalHeaderItem(3)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("main_window", u"AoI", None));
        ___qtablewidgetitem54 = self.tbl_uhub_org.horizontalHeaderItem(4)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("main_window", u"Email", None));
        ___qtablewidgetitem55 = self.tbl_uhub_org.horizontalHeaderItem(5)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("main_window", u"Phone", None));
        self.tab_widget_assets.setTabText(self.tab_widget_assets.indexOf(self.tab_uhub_org), QCoreApplication.translate("main_window", u"U-hub Organizations", None))
        ___qtablewidgetitem56 = self.tbl_uhub_user.horizontalHeaderItem(0)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("main_window", u"Username", None));
        ___qtablewidgetitem57 = self.tbl_uhub_user.horizontalHeaderItem(1)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("main_window", u"Email", None));
        ___qtablewidgetitem58 = self.tbl_uhub_user.horizontalHeaderItem(2)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("main_window", u"Password", None));
        ___qtablewidgetitem59 = self.tbl_uhub_user.horizontalHeaderItem(3)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("main_window", u"Organization", None));
        ___qtablewidgetitem60 = self.tbl_uhub_user.horizontalHeaderItem(4)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("main_window", u"Role", None));
        ___qtablewidgetitem61 = self.tbl_uhub_user.horizontalHeaderItem(5)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("main_window", u"Jurisdiction", None));
        ___qtablewidgetitem62 = self.tbl_uhub_user.horizontalHeaderItem(6)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("main_window", u"AoI", None));
        self.tab_widget_assets.setTabText(self.tab_widget_assets.indexOf(self.tab_uhub_user), QCoreApplication.translate("main_window", u"U-hub Users", None))
        ___qtablewidgetitem63 = self.tbl_uspaces.horizontalHeaderItem(0)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("main_window", u"Id", None));
        ___qtablewidgetitem64 = self.tbl_uspaces.horizontalHeaderItem(1)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("main_window", u"Name", None));
        ___qtablewidgetitem65 = self.tbl_uspaces.horizontalHeaderItem(2)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("main_window", u"# of sectors", None));
        ___qtablewidgetitem66 = self.tbl_uspaces.horizontalHeaderItem(3)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("main_window", u"File", None));
        self.tab_widget_assets.setTabText(self.tab_widget_assets.indexOf(self.tab_uspaces), QCoreApplication.translate("main_window", u"U-spaces", None))
        self.btn_start.setText(QCoreApplication.translate("main_window", u"Start", None))
        self.btn_add.setText(QCoreApplication.translate("main_window", u"Add", None))
        self.btn_edit.setText(QCoreApplication.translate("main_window", u"Edit", None))
        self.btn_remove.setText(QCoreApplication.translate("main_window", u"Remove", None))
        self.menu_bugs.setTitle(QCoreApplication.translate("main_window", u"Bugs", None))
        self.menu_campaigns.setTitle(QCoreApplication.translate("main_window", u"Campaigns", None))
        self.menu_cases.setTitle(QCoreApplication.translate("main_window", u"Cases", None))
        self.menu_new_test.setTitle(QCoreApplication.translate("main_window", u"New...", None))
        self.menu_requirements.setTitle(QCoreApplication.translate("main_window", u"Requirements", None))
        self.menu_assets.setTitle(QCoreApplication.translate("main_window", u"Assets", None))
        self.menu_new_asset.setTitle(QCoreApplication.translate("main_window", u"New asset", None))
        self.menu_statistics.setTitle(QCoreApplication.translate("main_window", u"Statistics", None))
    # retranslateUi

