# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(450, 291)
        MainWindow.setMaximumSize(QSize(450, 291))
        MainWindow.setWindowTitle("SLT Go")
        icon = QIcon()
        icon.addFile(":/images/AF_FON_RGB_white.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(
            "*{\n"
            "	color: rgb(0, 0, 0);\n"
            "	background-color: rgb(0, 127, 204);\n"
            "	border:0px solid;\n"
            "}\n"
            "\n"
            "#frame_2{\n"
            "	border-radius : 8px;\n"
            "	border:2px solid;\n"
            "	border-color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            "	border-radius : 5px;\n"
            "	background-color: rgba(255, 255, 255, 100);\n"
            "	text-align:left;\n"
            "	padding:10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "	background-color: rgba(0, 0, 0, 100);\n"
            "}\n"
            "\n"
            "#profileBtn{\n"
            "	border-radius : 28px;\n"
            "	text-align:center;\n"
            "}\n"
            "\n"
            "#page_Profile,#page_Logo,#page_about,#page_connect,#page_disconnect,#page_wait{	\n"
            "	background-image: url(:/images/SLTGO_logo1.jpeg);\n"
            "}\n"
            "\n"
            "QLineEdit{\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgba(0, 0, 0, 200);\n"
            "	border-radius : 8px;\n"
            "}\n"
            "QLabel{\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgba(0, 123, 198, 200);\n"
            "}\n"
            "#homeBtn,#aboutBtn,#saveBtn{\n"
            "	text-align:center;\n"
            "	background-color: rgb(0, 127, 204);\n"
            "}"
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName("homeBtn")
        icon1 = QIcon()
        icon1.addFile(":/images/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(20, 20))
        self.homeBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.homeBtn)

        self.aboutBtn = QPushButton(self.frame_2)
        self.aboutBtn.setObjectName("aboutBtn")
        icon2 = QIcon()
        icon2.addFile(":/images/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutBtn.setIcon(icon2)
        self.aboutBtn.setIconSize(QSize(20, 20))
        self.aboutBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.aboutBtn)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.connectBtn = QPushButton(self.frame_2)
        self.connectBtn.setObjectName("connectBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectBtn.sizePolicy().hasHeightForWidth())
        self.connectBtn.setSizePolicy(sizePolicy)
        self.connectBtn.setMinimumSize(QSize(0, 33))
        font = QFont()
        font.setBold(False)
        self.connectBtn.setFont(font)
        self.connectBtn.setLayoutDirection(Qt.LeftToRight)
        self.connectBtn.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(":/images/link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.connectBtn.setIcon(icon3)
        self.connectBtn.setCheckable(False)
        self.connectBtn.setAutoRepeat(False)
        self.connectBtn.setAutoExclusive(False)
        self.connectBtn.setAutoDefault(False)
        self.connectBtn.setFlat(True)

        self.verticalLayout_2.addWidget(self.connectBtn)

        self.disconnectBtn = QPushButton(self.frame_2)
        self.disconnectBtn.setObjectName("disconnectBtn")
        sizePolicy.setHeightForWidth(
            self.disconnectBtn.sizePolicy().hasHeightForWidth()
        )
        self.disconnectBtn.setSizePolicy(sizePolicy)
        self.disconnectBtn.setMinimumSize(QSize(0, 33))
        self.disconnectBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(":/images/link-slash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.disconnectBtn.setIcon(icon4)
        self.disconnectBtn.setFlat(True)

        self.verticalLayout_2.addWidget(self.disconnectBtn)

        self.verticalSpacer = QSpacerItem(
            20, 19, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.profileBtn = QPushButton(self.frame_2)
        self.profileBtn.setObjectName("profileBtn")
        self.profileBtn.setMinimumSize(QSize(0, 56))
        font1 = QFont()
        font1.setPointSize(10)
        self.profileBtn.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(":/images/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn.setIcon(icon5)
        self.profileBtn.setFlat(True)

        self.verticalLayout_2.addWidget(self.profileBtn)

        self.horizontalLayout.addWidget(self.frame_2)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_disconnect = QWidget()
        self.page_disconnect.setObjectName("page_disconnect")
        self.stackedWidget.addWidget(self.page_disconnect)
        self.page_connect = QWidget()
        self.page_connect.setObjectName("page_connect")
        self.stackedWidget.addWidget(self.page_connect)
        self.page_wait = QWidget()
        self.page_wait.setObjectName("page_wait")
        self.stackedWidget.addWidget(self.page_wait)
        self.page_about = QWidget()
        self.page_about.setObjectName("page_about")
        self.stackedWidget.addWidget(self.page_about)
        self.page_Logo = QWidget()
        self.page_Logo.setObjectName("page_Logo")
        self.verticalLayout_3 = QVBoxLayout(self.page_Logo)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget.addWidget(self.page_Logo)
        self.page_Profile = QWidget()
        self.page_Profile.setObjectName("page_Profile")
        self.verticalLayout_4 = QVBoxLayout(self.page_Profile)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.label_3 = QLabel(self.page_Profile)
        self.label_3.setObjectName("label_3")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_password = QLineEdit(self.page_Profile)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(0, 35))
        self.lineEdit_password.setInputMethodHints(
            Qt.ImhHiddenText
            | Qt.ImhNoAutoUppercase
            | Qt.ImhNoPredictiveText
            | Qt.ImhSensitiveData
        )
        self.lineEdit_password.setMaxLength(100)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEdit_password, 3, 0, 1, 1)

        self.lineEdit_userName = QLineEdit(self.page_Profile)
        self.lineEdit_userName.setObjectName("lineEdit_userName")
        self.lineEdit_userName.setMinimumSize(QSize(0, 35))
        self.lineEdit_userName.setMaxLength(100)

        self.gridLayout.addWidget(self.lineEdit_userName, 1, 0, 1, 1)

        self.label_usernName = QLabel(self.page_Profile)
        self.label_usernName.setObjectName("label_usernName")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.label_usernName.setFont(font3)
        self.label_usernName.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_usernName, 0, 0, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout)

        self.saveBtn = QPushButton(self.page_Profile)
        self.saveBtn.setObjectName("saveBtn")
        icon6 = QIcon()
        icon6.addFile(":/images/disk.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveBtn.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.saveBtn, 0, Qt.AlignRight)

        self.stackedWidget.addWidget(self.page_Profile)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.homeBtn.setDefault(True)
        self.aboutBtn.setDefault(True)
        self.connectBtn.setDefault(False)
        self.stackedWidget.setCurrentIndex(4)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        self.connectBtn.setText(
            QCoreApplication.translate("MainWindow", "  Connect", None)
        )
        self.disconnectBtn.setText(
            QCoreApplication.translate("MainWindow", "  Disconnect", None)
        )
        self.profileBtn.setText(
            QCoreApplication.translate("MainWindow", " Profile", None)
        )
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Password", None))
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "**********", None)
        )
        self.lineEdit_userName.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "94123456789@sltgo", None)
        )
        self.label_usernName.setText(
            QCoreApplication.translate("MainWindow", "User Name", None)
        )
        self.saveBtn.setText("")
        pass

    # retranslateUi
