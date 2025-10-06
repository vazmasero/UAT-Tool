# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_step.ui'
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
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_add_step(object):
    def setupUi(self, add_step):
        if not add_step.objectName():
            add_step.setObjectName(u"add_step")
        add_step.resize(572, 408)
        self.verticalLayout = QVBoxLayout(add_step)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.hlayout_action = QHBoxLayout()
        self.hlayout_action.setObjectName(u"hlayout_action")
        self.hlayout_action.setContentsMargins(5, -1, 5, -1)
        self.lbl_action = QLabel(add_step)
        self.lbl_action.setObjectName(u"lbl_action")

        self.hlayout_action.addWidget(self.lbl_action)

        self.le_action = QLineEdit(add_step)
        self.le_action.setObjectName(u"le_action")

        self.hlayout_action.addWidget(self.le_action)


        self.verticalLayout.addLayout(self.hlayout_action)

        self.hlayout_expected = QHBoxLayout()
        self.hlayout_expected.setObjectName(u"hlayout_expected")
        self.hlayout_expected.setContentsMargins(5, -1, 5, -1)
        self.lbl_expected_result = QLabel(add_step)
        self.lbl_expected_result.setObjectName(u"lbl_expected_result")

        self.hlayout_expected.addWidget(self.lbl_expected_result)

        self.le_expected_result = QLineEdit(add_step)
        self.le_expected_result.setObjectName(u"le_expected_result")

        self.hlayout_expected.addWidget(self.le_expected_result)


        self.verticalLayout.addLayout(self.hlayout_expected)

        self.hlayout_requirement = QHBoxLayout()
        self.hlayout_requirement.setObjectName(u"hlayout_requirement")
        self.hlayout_requirement.setContentsMargins(5, -1, 250, -1)
        self.b_requirement = QLabel(add_step)
        self.b_requirement.setObjectName(u"b_requirement")

        self.hlayout_requirement.addWidget(self.b_requirement)

        self.lw_requirements = QListWidget(add_step)
        self.lw_requirements.setObjectName(u"lw_requirements")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_requirements.sizePolicy().hasHeightForWidth())
        self.lw_requirements.setSizePolicy(sizePolicy)
        self.lw_requirements.setMinimumSize(QSize(150, 25))
        self.lw_requirements.setMaximumSize(QSize(300, 40))

        self.hlayout_requirement.addWidget(self.lw_requirements)


        self.verticalLayout.addLayout(self.hlayout_requirement)

        self.hlayout_comment = QHBoxLayout()
        self.hlayout_comment.setObjectName(u"hlayout_comment")
        self.hlayout_comment.setContentsMargins(5, -1, 5, -1)
        self.lbl_comments = QLabel(add_step)
        self.lbl_comments.setObjectName(u"lbl_comments")

        self.hlayout_comment.addWidget(self.lbl_comments)

        self.le_comments = QLineEdit(add_step)
        self.le_comments.setObjectName(u"le_comments")

        self.hlayout_comment.addWidget(self.le_comments)


        self.verticalLayout.addLayout(self.hlayout_comment)

        self.hlayout_btn_step = QHBoxLayout()
        self.hlayout_btn_step.setObjectName(u"hlayout_btn_step")
        self.hlayout_btn_step.setContentsMargins(300, -1, -1, 0)
        self.btn_accept = QPushButton(add_step)
        self.btn_accept.setObjectName(u"btn_accept")

        self.hlayout_btn_step.addWidget(self.btn_accept)

        self.btn_cancel = QPushButton(add_step)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hlayout_btn_step.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.hlayout_btn_step)


        self.retranslateUi(add_step)

        QMetaObject.connectSlotsByName(add_step)
    # setupUi

    def retranslateUi(self, add_step):
        add_step.setWindowTitle(QCoreApplication.translate("add_step", u"Form", None))
        self.lbl_action.setText(QCoreApplication.translate("add_step", u"Action:", None))
        self.lbl_expected_result.setText(QCoreApplication.translate("add_step", u"Expected result:", None))
        self.b_requirement.setText(QCoreApplication.translate("add_step", u"Affected requirements:", None))
        self.lbl_comments.setText(QCoreApplication.translate("add_step", u"Comments:", None))
        self.btn_accept.setText(QCoreApplication.translate("add_step", u"Accept", None))
        self.btn_cancel.setText(QCoreApplication.translate("add_step", u"Cancel", None))
    # retranslateUi

