# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_bug_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_edit_but_dialog(object):
    def setupUi(self, edit_but_dialog):
        if not edit_but_dialog.objectName():
            edit_but_dialog.setObjectName(u"edit_but_dialog")
        edit_but_dialog.resize(365, 155)
        self.verticalLayout = QVBoxLayout(edit_but_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, 15, -1)
        self.label = QLabel(edit_but_dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.btn_box = QDialogButtonBox(edit_but_dialog)
        self.btn_box.setObjectName(u"btn_box")
        self.btn_box.setOrientation(Qt.Orientation.Horizontal)
        self.btn_box.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Yes)
        self.btn_box.setCenterButtons(False)

        self.verticalLayout.addWidget(self.btn_box)


        self.retranslateUi(edit_but_dialog)

        QMetaObject.connectSlotsByName(edit_but_dialog)
    # setupUi

    def retranslateUi(self, edit_but_dialog):
        edit_but_dialog.setWindowTitle(QCoreApplication.translate("edit_but_dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("edit_but_dialog", u"Are you sure you want to edit this bug? All changes will be applied", None))
    # retranslateUi

