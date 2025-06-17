# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_bug_dialog.ui'
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

class Ui_delete_bug_dialog(object):
    def setupUi(self, delete_bug_dialog):
        if not delete_bug_dialog.objectName():
            delete_bug_dialog.setObjectName(u"delete_bug_dialog")
        delete_bug_dialog.resize(365, 155)
        self.verticalLayout = QVBoxLayout(delete_bug_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, 15, -1)
        self.dialo_label = QLabel(delete_bug_dialog)
        self.dialo_label.setObjectName(u"dialo_label")
        font = QFont()
        font.setPointSize(11)
        self.dialo_label.setFont(font)
        self.dialo_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.dialo_label)

        self.btn_box = QDialogButtonBox(delete_bug_dialog)
        self.btn_box.setObjectName(u"btn_box")
        self.btn_box.setOrientation(Qt.Orientation.Horizontal)
        self.btn_box.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Yes)
        self.btn_box.setCenterButtons(False)

        self.verticalLayout.addWidget(self.btn_box)


        self.retranslateUi(delete_bug_dialog)
        self.btn_box.accepted.connect(delete_bug_dialog.accept)
        self.btn_box.rejected.connect(delete_bug_dialog.reject)

        QMetaObject.connectSlotsByName(delete_bug_dialog)
    # setupUi

    def retranslateUi(self, delete_bug_dialog):
        delete_bug_dialog.setWindowTitle(QCoreApplication.translate("delete_bug_dialog", u"Dialog", None))
        self.dialo_label.setText(QCoreApplication.translate("delete_bug_dialog", u"Are you sure you want to delete this bug? All changes and history will be lost and won't be recoverable ", None))
    # retranslateUi

