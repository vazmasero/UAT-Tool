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
    QTableWidgetItem, QWidget)

class Ui_home_page(object):
    def setupUi(self, home_page):
        if not home_page.objectName():
            home_page.setObjectName(u"home_page")
        home_page.resize(850, 650)
        self.actionNew_Campaign = QAction(home_page)
        self.actionNew_Campaign.setObjectName(u"actionNew_Campaign")
        self.actionView_Campaigns = QAction(home_page)
        self.actionView_Campaigns.setObjectName(u"actionView_Campaigns")
        self.actionNew_Block = QAction(home_page)
        self.actionNew_Block.setObjectName(u"actionNew_Block")
        self.actionNew_Case = QAction(home_page)
        self.actionNew_Case.setObjectName(u"actionNew_Case")
        self.actionView_Cases = QAction(home_page)
        self.actionView_Cases.setObjectName(u"actionView_Cases")
        self.actionNew_Requirement = QAction(home_page)
        self.actionNew_Requirement.setObjectName(u"actionNew_Requirement")
        self.actionView_Requirements = QAction(home_page)
        self.actionView_Requirements.setObjectName(u"actionView_Requirements")
        self.actionNew_Asset = QAction(home_page)
        self.actionNew_Asset.setObjectName(u"actionNew_Asset")
        self.actionView_Assets = QAction(home_page)
        self.actionView_Assets.setObjectName(u"actionView_Assets")
        self.centralwidget_bugs = QWidget(home_page)
        self.centralwidget_bugs.setObjectName(u"centralwidget_bugs")
        self.visor_bugs = QTableWidget(self.centralwidget_bugs)
        if (self.visor_bugs.columnCount() < 12):
            self.visor_bugs.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.visor_bugs.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        if (self.visor_bugs.rowCount() < 4):
            self.visor_bugs.setRowCount(4)
        self.visor_bugs.setObjectName(u"visor_bugs")
        self.visor_bugs.setGeometry(QRect(40, 130, 771, 421))
        self.visor_bugs.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.visor_bugs.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.visor_bugs.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.visor_bugs.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed|QAbstractItemView.EditTrigger.SelectedClicked)
        self.visor_bugs.setShowGrid(True)
        self.visor_bugs.setGridStyle(Qt.PenStyle.SolidLine)
        self.visor_bugs.setSortingEnabled(False)
        self.visor_bugs.setWordWrap(True)
        self.visor_bugs.setCornerButtonEnabled(False)
        self.visor_bugs.setRowCount(4)
        self.visor_bugs.setColumnCount(12)
        self.visor_bugs.horizontalHeader().setVisible(True)
        self.visor_bugs.horizontalHeader().setCascadingSectionResizes(True)
        self.visor_bugs.horizontalHeader().setHighlightSections(True)
        self.visor_bugs.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.visor_bugs.horizontalHeader().setStretchLastSection(False)
        self.home_page_title = QLabel(self.centralwidget_bugs)
        self.home_page_title.setObjectName(u"home_page_title")
        self.home_page_title.setGeometry(QRect(40, 10, 251, 71))
        font = QFont()
        font.setPointSize(36)
        self.home_page_title.setFont(font)
        self.layoutWidget = QWidget(self.centralwidget_bugs)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(560, 560, 239, 26))
        self.homeButton_Layout = QHBoxLayout(self.layoutWidget)
        self.homeButton_Layout.setObjectName(u"homeButton_Layout")
        self.homeButton_Layout.setContentsMargins(0, 0, 0, 0)
        self.add_bug_button = QPushButton(self.layoutWidget)
        self.add_bug_button.setObjectName(u"add_bug_button")

        self.homeButton_Layout.addWidget(self.add_bug_button)

        self.edit_bug_button = QPushButton(self.layoutWidget)
        self.edit_bug_button.setObjectName(u"edit_bug_button")

        self.homeButton_Layout.addWidget(self.edit_bug_button)

        self.remove_bug_button = QPushButton(self.layoutWidget)
        self.remove_bug_button.setObjectName(u"remove_bug_button")

        self.homeButton_Layout.addWidget(self.remove_bug_button)

        self.widget = QWidget(self.centralwidget_bugs)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(41, 90, 510, 24))
        self.searchfilter_layout = QHBoxLayout(self.widget)
        self.searchfilter_layout.setObjectName(u"searchfilter_layout")
        self.searchfilter_layout.setContentsMargins(0, 0, 0, 0)
        self.searchBug_bar = QLineEdit(self.widget)
        self.searchBug_bar.setObjectName(u"searchBug_bar")
        self.searchBug_bar.setClearButtonEnabled(True)

        self.searchfilter_layout.addWidget(self.searchBug_bar)

        self.searchType = QComboBox(self.widget)
        self.searchType.addItem("")
        self.searchType.addItem("")
        self.searchType.setObjectName(u"searchType")

        self.searchfilter_layout.addWidget(self.searchType)

        self.spacerSearch_bar = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.searchfilter_layout.addItem(self.spacerSearch_bar)

        self.filterby_label = QLabel(self.widget)
        self.filterby_label.setObjectName(u"filterby_label")
        font1 = QFont()
        font1.setPointSize(10)
        self.filterby_label.setFont(font1)

        self.searchfilter_layout.addWidget(self.filterby_label)

        self.filterStatus = QComboBox(self.widget)
        self.filterStatus.setObjectName(u"filterStatus")
        self.filterStatus.setEditable(True)

        self.searchfilter_layout.addWidget(self.filterStatus)

        self.filterSystem = QComboBox(self.widget)
        self.filterSystem.setObjectName(u"filterSystem")
        self.filterSystem.setEditable(True)

        self.searchfilter_layout.addWidget(self.filterSystem)

        home_page.setCentralWidget(self.centralwidget_bugs)
        self.menubar_home = QMenuBar(home_page)
        self.menubar_home.setObjectName(u"menubar_home")
        self.menubar_home.setGeometry(QRect(0, 0, 850, 24))
        self.menubar_home.setFont(font1)
        self.menuCampaigns = QMenu(self.menubar_home)
        self.menuCampaigns.setObjectName(u"menuCampaigns")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.menuCampaigns.setFont(font2)
        self.menuTest_Cases = QMenu(self.menubar_home)
        self.menuTest_Cases.setObjectName(u"menuTest_Cases")
        self.menuRequirements = QMenu(self.menubar_home)
        self.menuRequirements.setObjectName(u"menuRequirements")
        self.menuAssets = QMenu(self.menubar_home)
        self.menuAssets.setObjectName(u"menuAssets")
        self.menuStatistics = QMenu(self.menubar_home)
        self.menuStatistics.setObjectName(u"menuStatistics")
        home_page.setMenuBar(self.menubar_home)
        self.statusbar_bugs = QStatusBar(home_page)
        self.statusbar_bugs.setObjectName(u"statusbar_bugs")
        home_page.setStatusBar(self.statusbar_bugs)

        self.menubar_home.addAction(self.menuCampaigns.menuAction())
        self.menubar_home.addAction(self.menuTest_Cases.menuAction())
        self.menubar_home.addAction(self.menuRequirements.menuAction())
        self.menubar_home.addAction(self.menuAssets.menuAction())
        self.menubar_home.addAction(self.menuStatistics.menuAction())
        self.menuCampaigns.addAction(self.actionNew_Campaign)
        self.menuCampaigns.addAction(self.actionView_Campaigns)
        self.menuTest_Cases.addAction(self.actionNew_Block)
        self.menuTest_Cases.addAction(self.actionNew_Case)
        self.menuTest_Cases.addAction(self.actionView_Cases)
        self.menuRequirements.addAction(self.actionNew_Requirement)
        self.menuRequirements.addAction(self.actionView_Requirements)
        self.menuAssets.addAction(self.actionNew_Asset)
        self.menuAssets.addAction(self.actionView_Assets)

        self.retranslateUi(home_page)

        QMetaObject.connectSlotsByName(home_page)
    # setupUi

    def retranslateUi(self, home_page):
        home_page.setWindowTitle(QCoreApplication.translate("home_page", u"MainWindow", None))
        self.actionNew_Campaign.setText(QCoreApplication.translate("home_page", u"New Campaign", None))
        self.actionView_Campaigns.setText(QCoreApplication.translate("home_page", u"View Campaigns", None))
        self.actionNew_Block.setText(QCoreApplication.translate("home_page", u"New Block", None))
        self.actionNew_Case.setText(QCoreApplication.translate("home_page", u"New Case", None))
        self.actionView_Cases.setText(QCoreApplication.translate("home_page", u"View Cases", None))
        self.actionNew_Requirement.setText(QCoreApplication.translate("home_page", u"New Requirement", None))
        self.actionView_Requirements.setText(QCoreApplication.translate("home_page", u"View Requirements", None))
        self.actionNew_Asset.setText(QCoreApplication.translate("home_page", u"New Asset", None))
        self.actionView_Assets.setText(QCoreApplication.translate("home_page", u"View Assets", None))
        ___qtablewidgetitem = self.visor_bugs.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("home_page", u"Status", None));
        ___qtablewidgetitem1 = self.visor_bugs.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("home_page", u"System", None));
        ___qtablewidgetitem2 = self.visor_bugs.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("home_page", u"Creation time", None));
        ___qtablewidgetitem3 = self.visor_bugs.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("home_page", u"Last update", None));
        ___qtablewidgetitem4 = self.visor_bugs.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("home_page", u"Service now ID", None));
        ___qtablewidgetitem5 = self.visor_bugs.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("home_page", u"Campaign", None));
        ___qtablewidgetitem6 = self.visor_bugs.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("home_page", u"Affected requirements", None));
        ___qtablewidgetitem7 = self.visor_bugs.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("home_page", u"Short description", None));
        ___qtablewidgetitem8 = self.visor_bugs.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("home_page", u"Long description", None));
        ___qtablewidgetitem9 = self.visor_bugs.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("home_page", u"Severity", None));
        ___qtablewidgetitem10 = self.visor_bugs.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("home_page", u"Impact", None));
        ___qtablewidgetitem11 = self.visor_bugs.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("home_page", u"Comments", None));
        self.home_page_title.setText(QCoreApplication.translate("home_page", u"Bugs List", None))
        self.add_bug_button.setText(QCoreApplication.translate("home_page", u"Add bug", None))
        self.edit_bug_button.setText(QCoreApplication.translate("home_page", u"Edit bug", None))
        self.remove_bug_button.setText(QCoreApplication.translate("home_page", u"Remove bug", None))
        self.searchBug_bar.setPlaceholderText(QCoreApplication.translate("home_page", u"Search...", None))
        self.searchType.setItemText(0, QCoreApplication.translate("home_page", u"Service now ID", None))
        self.searchType.setItemText(1, QCoreApplication.translate("home_page", u"Short description", None))

        self.filterby_label.setText(QCoreApplication.translate("home_page", u"Filter by:", None))
        self.filterStatus.setPlaceholderText(QCoreApplication.translate("home_page", u"Status", None))
        self.filterSystem.setPlaceholderText(QCoreApplication.translate("home_page", u"System", None))
        self.menuCampaigns.setTitle(QCoreApplication.translate("home_page", u"Test Campaigns", None))
        self.menuTest_Cases.setTitle(QCoreApplication.translate("home_page", u"Test Cases", None))
        self.menuRequirements.setTitle(QCoreApplication.translate("home_page", u"Requirements", None))
        self.menuAssets.setTitle(QCoreApplication.translate("home_page", u"Assets", None))
        self.menuStatistics.setTitle(QCoreApplication.translate("home_page", u"Statistics", None))
    # retranslateUi

