# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QWidget)
import res_rc

class Ui_has_mari(object):
    def setupUi(self, has_mari):
        if not has_mari.objectName():
            has_mari.setObjectName(u"has_mari")
        has_mari.resize(800, 600)
        has_mari.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setBold(False)
        has_mari.setFont(font)
        has_mari.setStyleSheet(u"background-color: #A6B1D1")
        self.centralwidget = QWidget(has_mari)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #A6B1D1")
        self.input = QLineEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(200, 20, 591, 251))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        self.input.setFont(font1)
        self.input.setStyleSheet(u"background-color: #01060F;")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 171, 191))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.file_input = QPushButton(self.gridLayoutWidget)
        self.file_input.setObjectName(u"file_input")
        self.file_input.setFont(font1)
        self.file_input.setStyleSheet(u"background-color: #01060F;\n"
"\n"
"QPushButton {\n"
"    background-color: #01060F; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #A6B1D1;\n"
"}")
        icon = QIcon()
        icon.addFile(u"file_open_24dp_ A6B1D1_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.file_input.setIcon(icon)

        self.gridLayout.addWidget(self.file_input, 3, 0, 1, 1)

        self.password_generator = QPushButton(self.gridLayoutWidget)
        self.password_generator.setObjectName(u"password_generator")
        self.password_generator.setFont(font1)
        self.password_generator.setStyleSheet(u"background-color: #01060F;\n"
"\n"
"QPushButton {\n"
"    background-color: #01060F; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #A6B1D1;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"key_24dp_ A6B1D1_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.password_generator.setIcon(icon1)

        self.gridLayout.addWidget(self.password_generator, 2, 0, 1, 1)

        self.encrypt = QPushButton(self.gridLayoutWidget)
        self.encrypt.setObjectName(u"encrypt")
        self.encrypt.setFont(font1)
        self.encrypt.setStyleSheet(u"background-color: #01060F;\n"
"\n"
"QPushButton {\n"
"    background-color: #01060F; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #A6B1D1;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"password_24dp_ A6B1D1_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.encrypt.setIcon(icon2)

        self.gridLayout.addWidget(self.encrypt, 0, 0, 1, 1)

        self.decrypt = QPushButton(self.gridLayoutWidget)
        self.decrypt.setObjectName(u"decrypt")
        self.decrypt.setFont(font1)
        self.decrypt.setStyleSheet(u"background-color: #01060F;\n"
"\n"
"QPushButton {\n"
"    background-color: #01060F; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #A6B1D1;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"no_encryption_24dp_ A6B1D1_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.decrypt.setIcon(icon3)

        self.gridLayout.addWidget(self.decrypt, 1, 0, 1, 1)

        self.input_scroll = QScrollArea(self.centralwidget)
        self.input_scroll.setObjectName(u"input_scroll")
        self.input_scroll.setGeometry(QRect(200, 280, 591, 311))
        self.input_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 589, 309))
        self.output = QLabel(self.scrollAreaWidgetContents)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(0, 0, 591, 311))
        self.output.setFont(font1)
        self.output.setStyleSheet(u"background-color: #01060F;")
        self.input_scroll.setWidget(self.scrollAreaWidgetContents)
        has_mari.setCentralWidget(self.centralwidget)

        self.retranslateUi(has_mari)

        QMetaObject.connectSlotsByName(has_mari)
    # setupUi

    def retranslateUi(self, has_mari):
        has_mari.setWindowTitle(QCoreApplication.translate("has_mari", u"MainWindow", None))
        self.file_input.setText(QCoreApplication.translate("has_mari", u"file input", None))
        self.password_generator.setText(QCoreApplication.translate("has_mari", u"password generator", None))
        self.encrypt.setText(QCoreApplication.translate("has_mari", u"encrypt", None))
        self.decrypt.setText(QCoreApplication.translate("has_mari", u"decrypt", None))
        self.output.setText(QCoreApplication.translate("has_mari", u" waiting for action...", None))
    # retranslateUi

