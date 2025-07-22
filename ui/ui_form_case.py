# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_case.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_form_case(object):
    def setupUi(self, form_case):
        if not form_case.objectName():
            form_case.setObjectName(u"form_case")
        form_case.resize(717, 511)
        self.verticalLayout_2 = QVBoxLayout(form_case)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 10, 30, -1)
        self.lbl_case = QLabel(form_case)
        self.lbl_case.setObjectName(u"lbl_case")
        font = QFont()
        font.setPointSize(24)
        self.lbl_case.setFont(font)
        self.lbl_case.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lbl_case)

        self.tab_widget_case = QTabWidget(form_case)
        self.tab_widget_case.setObjectName(u"tab_widget_case")
        self.tab_info = QWidget()
        self.tab_info.setObjectName(u"tab_info")
        self.verticalLayout = QVBoxLayout(self.tab_info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.hlayout_id = QHBoxLayout()
        self.hlayout_id.setObjectName(u"hlayout_id")
        self.lbl_id = QLabel(self.tab_info)
        self.lbl_id.setObjectName(u"lbl_id")

        self.hlayout_id.addWidget(self.lbl_id)

        self.le_id = QLineEdit(self.tab_info)
        self.le_id.setObjectName(u"le_id")

        self.hlayout_id.addWidget(self.le_id)

        self.lbl_name = QLabel(self.tab_info)
        self.lbl_name.setObjectName(u"lbl_name")

        self.hlayout_id.addWidget(self.lbl_name)

        self.le_name = QLineEdit(self.tab_info)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.hlayout_id.addWidget(self.le_name)

        self.lbl_system = QLabel(self.tab_info)
        self.lbl_system.setObjectName(u"lbl_system")

        self.hlayout_id.addWidget(self.lbl_system)

        self.cb_system = QComboBox(self.tab_info)
        self.cb_system.setObjectName(u"cb_system")

        self.hlayout_id.addWidget(self.cb_system)


        self.verticalLayout.addLayout(self.hlayout_id)

        self.hlayout_date = QHBoxLayout()
        self.hlayout_date.setObjectName(u"hlayout_date")
        self.hlayout_date.setContentsMargins(-1, -1, 200, -1)
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


        self.verticalLayout.addLayout(self.hlayout_date)

        self.hlayout_operator = QHBoxLayout()
        self.hlayout_operator.setObjectName(u"hlayout_operator")
        self.hlayout_operator.setContentsMargins(-1, -1, 200, -1)
        self.lbl_operator = QLabel(self.tab_info)
        self.lbl_operator.setObjectName(u"lbl_operator")

        self.hlayout_operator.addWidget(self.lbl_operator)

        self.cb_operator = QComboBox(self.tab_info)
        self.cb_operator.setObjectName(u"cb_operator")

        self.hlayout_operator.addWidget(self.cb_operator)

        self.lbl_drone = QLabel(self.tab_info)
        self.lbl_drone.setObjectName(u"lbl_drone")

        self.hlayout_operator.addWidget(self.lbl_drone)

        self.cb_drone = QComboBox(self.tab_info)
        self.cb_drone.setObjectName(u"cb_drone")

        self.hlayout_operator.addWidget(self.cb_drone)

        self.hlayout_operator.setStretch(1, 5)
        self.hlayout_operator.setStretch(3, 5)

        self.verticalLayout.addLayout(self.hlayout_operator)

        self.hlayout_comment = QHBoxLayout()
        self.hlayout_comment.setObjectName(u"hlayout_comment")
        self.lbl_comment = QLabel(self.tab_info)
        self.lbl_comment.setObjectName(u"lbl_comment")

        self.hlayout_comment.addWidget(self.lbl_comment)

        self.le_comment = QLineEdit(self.tab_info)
        self.le_comment.setObjectName(u"le_comment")

        self.hlayout_comment.addWidget(self.le_comment)


        self.verticalLayout.addLayout(self.hlayout_comment)

        self.tab_widget_case.addTab(self.tab_info, "")
        self.tab_steps = QWidget()
        self.tab_steps.setObjectName(u"tab_steps")
        self.horizontalLayout = QHBoxLayout(self.tab_steps)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tbl_steps = QTableWidget(self.tab_steps)
        if (self.tbl_steps.columnCount() < 4):
            self.tbl_steps.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_steps.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_steps.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_steps.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_steps.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tbl_steps.rowCount() < 4):
            self.tbl_steps.setRowCount(4)
        self.tbl_steps.setObjectName(u"tbl_steps")
        self.tbl_steps.setRowCount(4)

        self.horizontalLayout.addWidget(self.tbl_steps)

        self.vlayout_btn_steps = QVBoxLayout()
        self.vlayout_btn_steps.setSpacing(1)
        self.vlayout_btn_steps.setObjectName(u"vlayout_btn_steps")
        self.vlayout_btn_steps.setContentsMargins(-1, -1, -1, 300)
        self.btn_add_step = QPushButton(self.tab_steps)
        self.btn_add_step.setObjectName(u"btn_add_step")

        self.vlayout_btn_steps.addWidget(self.btn_add_step)

        self.btn_remove_step = QPushButton(self.tab_steps)
        self.btn_remove_step.setObjectName(u"btn_remove_step")

        self.vlayout_btn_steps.addWidget(self.btn_remove_step)


        self.horizontalLayout.addLayout(self.vlayout_btn_steps)

        self.tab_widget_case.addTab(self.tab_steps, "")

        self.verticalLayout_2.addWidget(self.tab_widget_case)

        self.hlayout_btn_case = QHBoxLayout()
        self.hlayout_btn_case.setObjectName(u"hlayout_btn_case")
        self.hlayout_btn_case.setContentsMargins(400, -1, -1, -1)
        self.btn_accept = QPushButton(form_case)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_case.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(form_case)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_case.addWidget(self.btn_cancel)


        self.verticalLayout_2.addLayout(self.hlayout_btn_case)


        self.retranslateUi(form_case)

        self.tab_widget_case.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(form_case)
    # setupUi

    def retranslateUi(self, form_case):
        form_case.setWindowTitle(QCoreApplication.translate("form_case", u"Form", None))
        self.lbl_case.setText(QCoreApplication.translate("form_case", u"[New/Test Case #]", None))
        self.lbl_id.setText(QCoreApplication.translate("form_case", u"Id:", None))
        self.le_id.setText("")
        self.le_id.setPlaceholderText(QCoreApplication.translate("form_case", u"[Id]", None))
        self.lbl_name.setText(QCoreApplication.translate("form_case", u"Name:", None))
        self.le_name.setText("")
        self.le_name.setPlaceholderText(QCoreApplication.translate("form_case", u"[Name]", None))
        self.lbl_system.setText(QCoreApplication.translate("form_case", u"System:", None))
        self.lbl_creation.setText(QCoreApplication.translate("form_case", u"Creation time:", None))
        self.le_creation.setText("")
        self.le_creation.setPlaceholderText(QCoreApplication.translate("form_case", u"[Creation time]", None))
        self.lbl_update.setText(QCoreApplication.translate("form_case", u"Last update:", None))
        self.le_update.setText("")
        self.le_update.setPlaceholderText(QCoreApplication.translate("form_case", u"[Update time]", None))
        self.lbl_operator.setText(QCoreApplication.translate("form_case", u"Operator:", None))
        self.lbl_drone.setText(QCoreApplication.translate("form_case", u"Drone:", None))
        self.lbl_comment.setText(QCoreApplication.translate("form_case", u"Comments:", None))
        self.le_comment.setText("")
        self.le_comment.setPlaceholderText(QCoreApplication.translate("form_case", u"[Comments]", None))
        self.tab_widget_case.setTabText(self.tab_widget_case.indexOf(self.tab_info), QCoreApplication.translate("form_case", u"Case info", None))
        ___qtablewidgetitem = self.tbl_steps.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("form_case", u"Action", None));
        ___qtablewidgetitem1 = self.tbl_steps.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("form_case", u"Expected result", None));
        ___qtablewidgetitem2 = self.tbl_steps.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("form_case", u"Affected requirements", None));
        ___qtablewidgetitem3 = self.tbl_steps.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("form_case", u"Comments", None));
        self.btn_add_step.setText(QCoreApplication.translate("form_case", u"+", None))
        self.btn_remove_step.setText(QCoreApplication.translate("form_case", u"-", None))
        self.tab_widget_case.setTabText(self.tab_widget_case.indexOf(self.tab_steps), QCoreApplication.translate("form_case", u"Steps", None))
        self.btn_accept.setText(QCoreApplication.translate("form_case", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_case", u"Cancel", None))
    # retranslateUi

