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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHBoxLayout, QHeaderView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

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
        self.centralwidget_campaigns = QWidget(home_page)
        self.centralwidget_campaigns.setObjectName(u"centralwidget_campaigns")
        self.visor_campaign = QTableWidget(self.centralwidget_campaigns)
        if (self.visor_campaign.columnCount() < 7):
            self.visor_campaign.setColumnCount(7)
        if (self.visor_campaign.rowCount() < 4):
            self.visor_campaign.setRowCount(4)
        self.visor_campaign.setObjectName(u"visor_campaign")
        self.visor_campaign.setGeometry(QRect(40, 60, 761, 511))
        self.visor_campaign.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.visor_campaign.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.visor_campaign.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.visor_campaign.setShowGrid(True)
        self.visor_campaign.setGridStyle(Qt.PenStyle.SolidLine)
        self.visor_campaign.setSortingEnabled(False)
        self.visor_campaign.setWordWrap(True)
        self.visor_campaign.setCornerButtonEnabled(False)
        self.visor_campaign.setRowCount(4)
        self.visor_campaign.setColumnCount(7)
        self.visor_campaign.horizontalHeader().setVisible(False)
        self.visor_campaign.horizontalHeader().setCascadingSectionResizes(False)
        self.visor_campaign.horizontalHeader().setHighlightSections(True)
        self.layoutWidget = QWidget(self.centralwidget_campaigns)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(320, 550, 259, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.new_campaign = QPushButton(self.layoutWidget)
        self.new_campaign.setObjectName(u"new_campaign")

        self.horizontalLayout.addWidget(self.new_campaign)

        self.edit_campaign = QPushButton(self.layoutWidget)
        self.edit_campaign.setObjectName(u"edit_campaign")

        self.horizontalLayout.addWidget(self.edit_campaign)

        self.delete_campaign = QPushButton(self.layoutWidget)
        self.delete_campaign.setObjectName(u"delete_campaign")

        self.horizontalLayout.addWidget(self.delete_campaign)

        home_page.setCentralWidget(self.centralwidget_campaigns)
        self.menubar_home = QMenuBar(home_page)
        self.menubar_home.setObjectName(u"menubar_home")
        self.menubar_home.setGeometry(QRect(0, 0, 850, 24))
        font = QFont()
        font.setPointSize(10)
        self.menubar_home.setFont(font)
        self.menuCampaigns = QMenu(self.menubar_home)
        self.menuCampaigns.setObjectName(u"menuCampaigns")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.menuCampaigns.setFont(font1)
        self.menuTest_Cases = QMenu(self.menubar_home)
        self.menuTest_Cases.setObjectName(u"menuTest_Cases")
        self.menuRequirements = QMenu(self.menubar_home)
        self.menuRequirements.setObjectName(u"menuRequirements")
        self.menuAssets = QMenu(self.menubar_home)
        self.menuAssets.setObjectName(u"menuAssets")
        self.menuStatistics = QMenu(self.menubar_home)
        self.menuStatistics.setObjectName(u"menuStatistics")
        home_page.setMenuBar(self.menubar_home)
        self.statusbar_campaign = QStatusBar(home_page)
        self.statusbar_campaign.setObjectName(u"statusbar_campaign")
        home_page.setStatusBar(self.statusbar_campaign)

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
        self.new_campaign.setText(QCoreApplication.translate("home_page", u"Nueva Campa\u00f1a", None))
        self.edit_campaign.setText(QCoreApplication.translate("home_page", u"Editar", None))
        self.delete_campaign.setText(QCoreApplication.translate("home_page", u"Eliminar", None))
        self.menuCampaigns.setTitle(QCoreApplication.translate("home_page", u"Test Campaigns", None))
        self.menuTest_Cases.setTitle(QCoreApplication.translate("home_page", u"Test Cases", None))
        self.menuRequirements.setTitle(QCoreApplication.translate("home_page", u"Requirements", None))
        self.menuAssets.setTitle(QCoreApplication.translate("home_page", u"Assets", None))
        self.menuStatistics.setTitle(QCoreApplication.translate("home_page", u"Statistics", None))
    # retranslateUi

