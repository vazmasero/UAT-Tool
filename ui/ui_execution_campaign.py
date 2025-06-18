# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'execution_campaign.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_execution_campaign(object):
    def setupUi(self, execution_campaign):
        if not execution_campaign.objectName():
            execution_campaign.setObjectName(u"execution_campaign")
        execution_campaign.resize(720, 510)
        self.verticalLayout = QVBoxLayout(execution_campaign)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.lbl_campaign = QLabel(execution_campaign)
        self.lbl_campaign.setObjectName(u"lbl_campaign")
        font = QFont()
        font.setPointSize(28)
        self.lbl_campaign.setFont(font)
        self.lbl_campaign.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_campaign)

        self.hlayout_table = QHBoxLayout()
        self.hlayout_table.setObjectName(u"hlayout_table")
        self.tbl_steps = QTableWidget(execution_campaign)
        if (self.tbl_steps.columnCount() < 9):
            self.tbl_steps.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_steps.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_steps.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_steps.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_steps.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_steps.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_steps.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_steps.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_steps.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_steps.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        if (self.tbl_steps.rowCount() < 4):
            self.tbl_steps.setRowCount(4)
        self.tbl_steps.setObjectName(u"tbl_steps")
        self.tbl_steps.setRowCount(4)

        self.hlayout_table.addWidget(self.tbl_steps)

        self.btn_add_file = QPushButton(execution_campaign)
        self.btn_add_file.setObjectName(u"btn_add_file")

        self.hlayout_table.addWidget(self.btn_add_file)


        self.verticalLayout.addLayout(self.hlayout_table)

        self.hlayout_btn_campaign = QHBoxLayout()
        self.hlayout_btn_campaign.setObjectName(u"hlayout_btn_campaign")
        self.hlayout_btn_campaign.setContentsMargins(300, -1, -1, -1)
        self.btn_save_campaign = QPushButton(execution_campaign)
        self.btn_save_campaign.setObjectName(u"btn_save_campaign")

        self.hlayout_btn_campaign.addWidget(self.btn_save_campaign)

        self.btn_end_campaign = QPushButton(execution_campaign)
        self.btn_end_campaign.setObjectName(u"btn_end_campaign")

        self.hlayout_btn_campaign.addWidget(self.btn_end_campaign)

        self.btn_back = QPushButton(execution_campaign)
        self.btn_back.setObjectName(u"btn_back")

        self.hlayout_btn_campaign.addWidget(self.btn_back)


        self.verticalLayout.addLayout(self.hlayout_btn_campaign)


        self.retranslateUi(execution_campaign)

        QMetaObject.connectSlotsByName(execution_campaign)
    # setupUi

    def retranslateUi(self, execution_campaign):
        execution_campaign.setWindowTitle(QCoreApplication.translate("execution_campaign", u"Form", None))
        self.lbl_campaign.setText(QCoreApplication.translate("execution_campaign", u"[Campaign name]", None))
        ___qtablewidgetitem = self.tbl_steps.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("execution_campaign", u"Block", None));
        ___qtablewidgetitem1 = self.tbl_steps.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("execution_campaign", u"Case", None));
        ___qtablewidgetitem2 = self.tbl_steps.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("execution_campaign", u"Action", None));
        ___qtablewidgetitem3 = self.tbl_steps.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("execution_campaign", u"Expected result", None));
        ___qtablewidgetitem4 = self.tbl_steps.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("execution_campaign", u"Requirements affected", None));
        ___qtablewidgetitem5 = self.tbl_steps.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("execution_campaign", u"OK", None));
        ___qtablewidgetitem6 = self.tbl_steps.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("execution_campaign", u"NO OK", None));
        ___qtablewidgetitem7 = self.tbl_steps.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("execution_campaign", u"Comments", None));
        ___qtablewidgetitem8 = self.tbl_steps.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("execution_campaign", u"Files", None));
        self.btn_add_file.setText(QCoreApplication.translate("execution_campaign", u"Add file", None))
        self.btn_save_campaign.setText(QCoreApplication.translate("execution_campaign", u"Save campaign", None))
        self.btn_end_campaign.setText(QCoreApplication.translate("execution_campaign", u"End campaign", None))
        self.btn_back.setText(QCoreApplication.translate("execution_campaign", u"Back", None))
    # retranslateUi

