# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_page.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_home_page(object):
    def setupUi(self, home_page):
        if not home_page.objectName():
            home_page.setObjectName(u"home_page")
        home_page.resize(850, 650)
        self.action_new_campaign = QAction(home_page)
        self.action_new_campaign.setObjectName(u"action_new_campaign")
        self.action_view_campaigns = QAction(home_page)
        self.action_view_campaigns.setObjectName(u"action_view_campaigns")
        self.action_new_block = QAction(home_page)
        self.action_new_block.setObjectName(u"action_new_block")
        self.action_new_case = QAction(home_page)
        self.action_new_case.setObjectName(u"action_new_case")
        self.action_view_cases = QAction(home_page)
        self.action_view_cases.setObjectName(u"action_view_cases")
        self.action_new_requirement = QAction(home_page)
        self.action_new_requirement.setObjectName(u"action_new_requirement")
        self.action_view_requirements = QAction(home_page)
        self.action_view_requirements.setObjectName(u"action_view_requirements")
        self.action_new_asset = QAction(home_page)
        self.action_new_asset.setObjectName(u"action_new_asset")
        self.action_new_asset.setCheckable(False)
        self.action_view_assets = QAction(home_page)
        self.action_view_assets.setObjectName(u"action_view_assets")
        self.central_widget = QWidget(home_page)
        self.central_widget.setObjectName(u"central_widget")
        self.main_vlayout = QVBoxLayout(self.central_widget)
        self.main_vlayout.setSpacing(15)
        self.main_vlayout.setObjectName(u"main_vlayout")
        self.main_vlayout.setContentsMargins(30, 10, 30, 25)
        self.bugs_title_lbl = QLabel(self.central_widget)
        self.bugs_title_lbl.setObjectName(u"bugs_title_lbl")
        font = QFont()
        font.setPointSize(36)
        self.bugs_title_lbl.setFont(font)

        self.main_vlayout.addWidget(self.bugs_title_lbl)

        self.filter_hlayout = QHBoxLayout()
        self.filter_hlayout.setSpacing(6)
        self.filter_hlayout.setObjectName(u"filter_hlayout")
        self.filter_hlayout.setContentsMargins(5, -1, 200, -1)
        self.search_bug_le = QLineEdit(self.central_widget)
        self.search_bug_le.setObjectName(u"search_bug_le")
        self.search_bug_le.setClearButtonEnabled(True)

        self.filter_hlayout.addWidget(self.search_bug_le)

        self.search_type_cb = QComboBox(self.central_widget)
        self.search_type_cb.addItem("")
        self.search_type_cb.addItem("")
        self.search_type_cb.setObjectName(u"search_type_cb")

        self.filter_hlayout.addWidget(self.search_type_cb)

        self.spacerSearch_bar = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.filter_hlayout.addItem(self.spacerSearch_bar)

        self.filter_lbl = QLabel(self.central_widget)
        self.filter_lbl.setObjectName(u"filter_lbl")
        font1 = QFont()
        font1.setPointSize(10)
        self.filter_lbl.setFont(font1)

        self.filter_hlayout.addWidget(self.filter_lbl)

        self.status_filter_cb = QComboBox(self.central_widget)
        self.status_filter_cb.setObjectName(u"status_filter_cb")
        self.status_filter_cb.setEditable(True)

        self.filter_hlayout.addWidget(self.status_filter_cb)

        self.system_filter_cb = QComboBox(self.central_widget)
        self.system_filter_cb.setObjectName(u"system_filter_cb")
        self.system_filter_cb.setEditable(True)

        self.filter_hlayout.addWidget(self.system_filter_cb)


        self.main_vlayout.addLayout(self.filter_hlayout)

        self.bugs_tabl = QTableWidget(self.central_widget)
        if (self.bugs_tabl.columnCount() < 13):
            self.bugs_tabl.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        self.bugs_tabl.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.bugs_tabl.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.bugs_tabl.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.bugs_tabl.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.bugs_tabl.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.bugs_tabl.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.bugs_tabl.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.bugs_tabl.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.bugs_tabl.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.bugs_tabl.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.bugs_tabl.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.bugs_tabl.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.bugs_tabl.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        if (self.bugs_tabl.rowCount() < 4):
            self.bugs_tabl.setRowCount(4)
        self.bugs_tabl.setObjectName(u"bugs_tabl")
        self.bugs_tabl.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bugs_tabl.sizePolicy().hasHeightForWidth())
        self.bugs_tabl.setSizePolicy(sizePolicy)
        self.bugs_tabl.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.bugs_tabl.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.bugs_tabl.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.bugs_tabl.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed|QAbstractItemView.EditTrigger.SelectedClicked)
        self.bugs_tabl.setShowGrid(True)
        self.bugs_tabl.setGridStyle(Qt.PenStyle.SolidLine)
        self.bugs_tabl.setSortingEnabled(False)
        self.bugs_tabl.setWordWrap(True)
        self.bugs_tabl.setCornerButtonEnabled(False)
        self.bugs_tabl.setRowCount(4)
        self.bugs_tabl.setColumnCount(13)
        self.bugs_tabl.horizontalHeader().setVisible(True)
        self.bugs_tabl.horizontalHeader().setCascadingSectionResizes(True)
        self.bugs_tabl.horizontalHeader().setHighlightSections(True)
        self.bugs_tabl.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.bugs_tabl.horizontalHeader().setStretchLastSection(False)

        self.main_vlayout.addWidget(self.bugs_tabl)

        self.bug_actions_hlayout = QHBoxLayout()
        self.bug_actions_hlayout.setSpacing(5)
        self.bug_actions_hlayout.setObjectName(u"bug_actions_hlayout")
        self.bug_actions_hlayout.setContentsMargins(450, -1, 10, -1)
        self.add_bug_btn = QPushButton(self.central_widget)
        self.add_bug_btn.setObjectName(u"add_bug_btn")

        self.bug_actions_hlayout.addWidget(self.add_bug_btn)

        self.edit_bug_btn = QPushButton(self.central_widget)
        self.edit_bug_btn.setObjectName(u"edit_bug_btn")

        self.bug_actions_hlayout.addWidget(self.edit_bug_btn)

        self.remove_bug_btn = QPushButton(self.central_widget)
        self.remove_bug_btn.setObjectName(u"remove_bug_btn")

        self.bug_actions_hlayout.addWidget(self.remove_bug_btn)


        self.main_vlayout.addLayout(self.bug_actions_hlayout)

        home_page.setCentralWidget(self.central_widget)
        self.menu_bar = QMenuBar(home_page)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 850, 24))
        self.menu_bar.setFont(font1)
        self.menu_campaigns = QMenu(self.menu_bar)
        self.menu_campaigns.setObjectName(u"menu_campaigns")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.menu_campaigns.setFont(font2)
        self.menuTest_Cases = QMenu(self.menu_bar)
        self.menuTest_Cases.setObjectName(u"menuTest_Cases")
        self.menu_requirements = QMenu(self.menu_bar)
        self.menu_requirements.setObjectName(u"menu_requirements")
        self.menu_assets = QMenu(self.menu_bar)
        self.menu_assets.setObjectName(u"menu_assets")
        self.menu_statistics = QMenu(self.menu_bar)
        self.menu_statistics.setObjectName(u"menu_statistics")
        home_page.setMenuBar(self.menu_bar)
        self.status_bar = QStatusBar(home_page)
        self.status_bar.setObjectName(u"status_bar")
        home_page.setStatusBar(self.status_bar)

        self.menu_bar.addAction(self.menu_campaigns.menuAction())
        self.menu_bar.addAction(self.menuTest_Cases.menuAction())
        self.menu_bar.addAction(self.menu_requirements.menuAction())
        self.menu_bar.addAction(self.menu_assets.menuAction())
        self.menu_bar.addAction(self.menu_statistics.menuAction())
        self.menu_campaigns.addAction(self.action_new_campaign)
        self.menu_campaigns.addAction(self.action_view_campaigns)
        self.menuTest_Cases.addAction(self.action_new_block)
        self.menuTest_Cases.addAction(self.action_new_case)
        self.menuTest_Cases.addAction(self.action_view_cases)
        self.menu_requirements.addAction(self.action_new_requirement)
        self.menu_requirements.addAction(self.action_view_requirements)
        self.menu_assets.addAction(self.action_new_asset)
        self.menu_assets.addAction(self.action_view_assets)

        self.retranslateUi(home_page)

        QMetaObject.connectSlotsByName(home_page)
    # setupUi

    def retranslateUi(self, home_page):
        home_page.setWindowTitle(QCoreApplication.translate("home_page", u"MainWindow", None))
        self.action_new_campaign.setText(QCoreApplication.translate("home_page", u"New Campaign", None))
        self.action_view_campaigns.setText(QCoreApplication.translate("home_page", u"View Campaigns", None))
        self.action_new_block.setText(QCoreApplication.translate("home_page", u"New Block", None))
        self.action_new_case.setText(QCoreApplication.translate("home_page", u"New Case", None))
        self.action_view_cases.setText(QCoreApplication.translate("home_page", u"View Cases", None))
        self.action_new_requirement.setText(QCoreApplication.translate("home_page", u"New Requirement", None))
        self.action_view_requirements.setText(QCoreApplication.translate("home_page", u"View Requirements", None))
        self.action_new_asset.setText(QCoreApplication.translate("home_page", u"New Asset", None))
        self.action_view_assets.setText(QCoreApplication.translate("home_page", u"View Assets", None))
        self.bugs_title_lbl.setText(QCoreApplication.translate("home_page", u"Bugs List", None))
        self.search_bug_le.setPlaceholderText(QCoreApplication.translate("home_page", u"Search...", None))
        self.search_type_cb.setItemText(0, QCoreApplication.translate("home_page", u"Service now ID", None))
        self.search_type_cb.setItemText(1, QCoreApplication.translate("home_page", u"Short description", None))

        self.filter_lbl.setText(QCoreApplication.translate("home_page", u"Filter by:", None))
        self.status_filter_cb.setPlaceholderText(QCoreApplication.translate("home_page", u"Status", None))
        self.system_filter_cb.setPlaceholderText(QCoreApplication.translate("home_page", u"System", None))
        ___qtablewidgetitem = self.bugs_tabl.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("home_page", u"Status", None));
        ___qtablewidgetitem1 = self.bugs_tabl.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("home_page", u"System", None));
        ___qtablewidgetitem2 = self.bugs_tabl.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("home_page", u"Version", None));
        ___qtablewidgetitem3 = self.bugs_tabl.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("home_page", u"Creation time", None));
        ___qtablewidgetitem4 = self.bugs_tabl.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("home_page", u"Last update", None));
        ___qtablewidgetitem5 = self.bugs_tabl.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("home_page", u"Service now ID", None));
        ___qtablewidgetitem6 = self.bugs_tabl.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("home_page", u"Campaign", None));
        ___qtablewidgetitem7 = self.bugs_tabl.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("home_page", u"Affected requirements", None));
        ___qtablewidgetitem8 = self.bugs_tabl.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("home_page", u"Short description", None));
        ___qtablewidgetitem9 = self.bugs_tabl.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("home_page", u"Definition", None));
        ___qtablewidgetitem10 = self.bugs_tabl.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("home_page", u"Urgency", None));
        ___qtablewidgetitem11 = self.bugs_tabl.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("home_page", u"Impact", None));
        ___qtablewidgetitem12 = self.bugs_tabl.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("home_page", u"Comments", None));
        self.add_bug_btn.setText(QCoreApplication.translate("home_page", u"Add bug", None))
        self.edit_bug_btn.setText(QCoreApplication.translate("home_page", u"Edit bug", None))
        self.remove_bug_btn.setText(QCoreApplication.translate("home_page", u"Remove bug", None))
        self.menu_campaigns.setTitle(QCoreApplication.translate("home_page", u"Test Campaigns", None))
        self.menuTest_Cases.setTitle(QCoreApplication.translate("home_page", u"Test Cases", None))
        self.menu_requirements.setTitle(QCoreApplication.translate("home_page", u"Requirements", None))
        self.menu_assets.setTitle(QCoreApplication.translate("home_page", u"Assets", None))
        self.menu_statistics.setTitle(QCoreApplication.translate("home_page", u"Statistics", None))
    # retranslateUi

