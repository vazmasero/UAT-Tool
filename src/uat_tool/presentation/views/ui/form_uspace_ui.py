# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_uspace.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_form_uspace(object):
    def setupUi(self, form_uspace):
        if not form_uspace.objectName():
            form_uspace.setObjectName(u"form_uspace")
        form_uspace.resize(571, 412)
        self.verticalLayout = QVBoxLayout(form_uspace)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.hlayout_id = QHBoxLayout()
        self.hlayout_id.setObjectName(u"hlayout_id")
        self.hlayout_id.setContentsMargins(5, -1, 200, -1)
        self.lbl_id = QLabel(form_uspace)
        self.lbl_id.setObjectName(u"lbl_id")

        self.hlayout_id.addWidget(self.lbl_id)

        self.le_identification = QLineEdit(form_uspace)
        self.le_identification.setObjectName(u"le_identification")

        self.hlayout_id.addWidget(self.le_identification)

        self.lbl_name = QLabel(form_uspace)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setWordWrap(False)

        self.hlayout_id.addWidget(self.lbl_name)

        self.le_name = QLineEdit(form_uspace)
        self.le_name.setObjectName(u"le_name")

        self.hlayout_id.addWidget(self.le_name)

        self.hlayout_id.setStretch(1, 5)
        self.hlayout_id.setStretch(3, 200)

        self.verticalLayout.addLayout(self.hlayout_id)

        self.hlayout_sectors = QHBoxLayout()
        self.hlayout_sectors.setObjectName(u"hlayout_sectors")
        self.hlayout_sectors.setContentsMargins(5, -1, 150, -1)
        self.lbl_sectors = QLabel(form_uspace)
        self.lbl_sectors.setObjectName(u"lbl_sectors")

        self.hlayout_sectors.addWidget(self.lbl_sectors)

        self.le_sectors_number = QLineEdit(form_uspace)
        self.le_sectors_number.setObjectName(u"le_sectors_number")

        self.hlayout_sectors.addWidget(self.le_sectors_number)

        self.lbl_file = QLabel(form_uspace)
        self.lbl_file.setObjectName(u"lbl_file")

        self.hlayout_sectors.addWidget(self.lbl_file)

        self.hlayout_file = QHBoxLayout()
        self.hlayout_file.setObjectName(u"hlayout_file")
        self.le_file_path = QLineEdit(form_uspace)
        self.le_file_path.setObjectName(u"le_file_path")
        self.le_file_path.setReadOnly(True)

        self.hlayout_file.addWidget(self.le_file_path)

        self.btn_browse_file = QPushButton(form_uspace)
        self.btn_browse_file.setObjectName(u"btn_browse_file")

        self.hlayout_file.addWidget(self.btn_browse_file)


        self.hlayout_sectors.addLayout(self.hlayout_file)


        self.verticalLayout.addLayout(self.hlayout_sectors)

        self.hlayout_btn_uspace = QHBoxLayout()
        self.hlayout_btn_uspace.setObjectName(u"hlayout_btn_uspace")
        self.hlayout_btn_uspace.setContentsMargins(300, -1, -1, -1)
        self.btn_accept = QPushButton(form_uspace)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_uspace.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(form_uspace)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_uspace.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.hlayout_btn_uspace)


        self.retranslateUi(form_uspace)

        QMetaObject.connectSlotsByName(form_uspace)
    # setupUi

    def retranslateUi(self, form_uspace):
        form_uspace.setWindowTitle(QCoreApplication.translate("form_uspace", u"Form", None))
        self.lbl_id.setText(QCoreApplication.translate("form_uspace", u"Id:", None))
        self.lbl_name.setText(QCoreApplication.translate("form_uspace", u"Name:", None))
        self.lbl_sectors.setText(QCoreApplication.translate("form_uspace", u"# of sectors", None))
        self.lbl_file.setText(QCoreApplication.translate("form_uspace", u"File:", None))
        self.le_file_path.setPlaceholderText(QCoreApplication.translate("form_uspace", u"No file selected", None))
        self.btn_browse_file.setText(QCoreApplication.translate("form_uspace", u"Browse...", None))
        self.btn_accept.setText(QCoreApplication.translate("form_uspace", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("form_uspace", u"Cancel", None))
    # retranslateUi

