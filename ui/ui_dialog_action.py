# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_action.ui'
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

class Ui_dialog_action(object):
    def setupUi(self, dialog_action):
        if not dialog_action.objectName():
            dialog_action.setObjectName(u"dialog_action")
        dialog_action.resize(365, 155)
        self.main_vlayout = QVBoxLayout(dialog_action)
        self.main_vlayout.setSpacing(6)
        self.main_vlayout.setObjectName(u"main_vlayout")
        self.main_vlayout.setContentsMargins(20, -1, 15, 9)
        self.lbl_dialog = QLabel(dialog_action)
        self.lbl_dialog.setObjectName(u"lbl_dialog")
        font = QFont()
        font.setPointSize(11)
        self.lbl_dialog.setFont(font)
        self.lbl_dialog.setWordWrap(True)

        self.main_vlayout.addWidget(self.lbl_dialog)

        self.btn_box = QDialogButtonBox(dialog_action)
        self.btn_box.setObjectName(u"btn_box")
        self.btn_box.setOrientation(Qt.Orientation.Horizontal)
        self.btn_box.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Yes)

        self.main_vlayout.addWidget(self.btn_box)


        self.retranslateUi(dialog_action)
        self.btn_box.accepted.connect(dialog_action.accept)
        self.btn_box.rejected.connect(dialog_action.reject)

        QMetaObject.connectSlotsByName(dialog_action)
    # setupUi

    def retranslateUi(self, dialog_action):
        dialog_action.setWindowTitle(QCoreApplication.translate("dialog_action", u"Dialog", None))
        self.lbl_dialog.setText(QCoreApplication.translate("dialog_action", u"Are you sure you want to [action]? [Additional comment]", None))
    # retranslateUi

