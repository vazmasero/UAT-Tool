# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_bug_dialog.ui'
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

class Ui_new_bug_dialog(object):
    def setupUi(self, new_bug_dialog):
        if not new_bug_dialog.objectName():
            new_bug_dialog.setObjectName(u"new_bug_dialog")
        new_bug_dialog.resize(365, 155)
        self.main_vlayout = QVBoxLayout(new_bug_dialog)
        self.main_vlayout.setSpacing(6)
        self.main_vlayout.setObjectName(u"main_vlayout")
        self.main_vlayout.setContentsMargins(20, -1, 15, 9)
        self.dialog_lbl = QLabel(new_bug_dialog)
        self.dialog_lbl.setObjectName(u"dialog_lbl")
        font = QFont()
        font.setPointSize(11)
        self.dialog_lbl.setFont(font)
        self.dialog_lbl.setWordWrap(True)

        self.main_vlayout.addWidget(self.dialog_lbl)

        self.btn_box = QDialogButtonBox(new_bug_dialog)
        self.btn_box.setObjectName(u"btn_box")
        self.btn_box.setOrientation(Qt.Orientation.Horizontal)
        self.btn_box.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Yes)

        self.main_vlayout.addWidget(self.btn_box)


        self.retranslateUi(new_bug_dialog)
        self.btn_box.accepted.connect(new_bug_dialog.accept)
        self.btn_box.rejected.connect(new_bug_dialog.reject)

        QMetaObject.connectSlotsByName(new_bug_dialog)
    # setupUi

    def retranslateUi(self, new_bug_dialog):
        new_bug_dialog.setWindowTitle(QCoreApplication.translate("new_bug_dialog", u"Dialog", None))
        self.dialog_lbl.setText(QCoreApplication.translate("new_bug_dialog", u"Are you sure you want to create a new bug?", None))
    # retranslateUi

