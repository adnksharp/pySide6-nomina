# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLCDNumber,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(565, 603)
        self.verticalLayout_11 = QVBoxLayout(Widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_1.addWidget(self.label)

        self.hours = QLineEdit(Widget)
        self.hours.setObjectName(u"hours")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hours.sizePolicy().hasHeightForWidth())
        self.hours.setSizePolicy(sizePolicy1)
        self.hours.setStyleSheet(u"color:white; background:black")
        self.hours.setFrame(False)

        self.horizontalLayout_1.addWidget(self.hours)


        self.verticalLayout_11.addLayout(self.horizontalLayout_1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_16 = QLabel(Widget)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.label_16)

        self.payment = QLineEdit(Widget)
        self.payment.setObjectName(u"payment")
        sizePolicy1.setHeightForWidth(self.payment.sizePolicy().hasHeightForWidth())
        self.payment.setSizePolicy(sizePolicy1)
        self.payment.setStyleSheet(u"color:white; background:black")
        self.payment.setFrame(False)

        self.horizontalLayout_15.addWidget(self.payment)


        self.verticalLayout_11.addLayout(self.horizontalLayout_15)

        self.verticalSpacer = QSpacerItem(20, 21, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.label_11 = QLabel(Widget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.line = QFrame(Widget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setStyleSheet(u"color:#888")
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.hBase = QLineEdit(Widget)
        self.hBase.setObjectName(u"hBase")
        self.hBase.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.hBase.sizePolicy().hasHeightForWidth())
        self.hBase.setSizePolicy(sizePolicy3)
        self.hBase.setStyleSheet(u"color:#888;\n"
"background:black")
        self.hBase.setFrame(False)

        self.horizontalLayout_3.addWidget(self.hBase)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(Widget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setStyleSheet(u"color:#888")
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(True)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.hTwo = QLineEdit(Widget)
        self.hTwo.setObjectName(u"hTwo")
        self.hTwo.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.hTwo.sizePolicy().hasHeightForWidth())
        self.hTwo.setSizePolicy(sizePolicy3)
        self.hTwo.setStyleSheet(u"color:#888;\n"
"background:black")
        self.hTwo.setFrame(False)

        self.horizontalLayout_10.addWidget(self.hTwo)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setStyleSheet(u"color:#888")
        self.label_10.setScaledContents(False)
        self.label_10.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.hPlus = QLineEdit(Widget)
        self.hPlus.setObjectName(u"hPlus")
        self.hPlus.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.hPlus.sizePolicy().hasHeightForWidth())
        self.hPlus.setSizePolicy(sizePolicy3)
        self.hPlus.setStyleSheet(u"color:#888;\n"
"background:black")
        self.hPlus.setFrame(False)

        self.horizontalLayout_11.addWidget(self.hPlus)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy4)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 14, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label_17 = QLabel(Widget)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_17)

        self.line_3 = QFrame(Widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_18 = QLabel(Widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color:#888")
        self.label_18.setScaledContents(False)
        self.label_18.setWordWrap(True)

        self.horizontalLayout_16.addWidget(self.label_18)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_21 = QLabel(Widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"color:#888")
        self.label_21.setScaledContents(False)
        self.label_21.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_21)

        self.hBase_3 = QLineEdit(Widget)
        self.hBase_3.setObjectName(u"hBase_3")
        self.hBase_3.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.hBase_3.sizePolicy().hasHeightForWidth())
        self.hBase_3.setSizePolicy(sizePolicy3)
        self.hBase_3.setStyleSheet(u"color:#888;background:black")
        self.hBase_3.setFrame(False)

        self.verticalLayout_4.addWidget(self.hBase_3)

        self.hBase_4 = QLineEdit(Widget)
        self.hBase_4.setObjectName(u"hBase_4")
        self.hBase_4.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.hBase_4.sizePolicy().hasHeightForWidth())
        self.hBase_4.setSizePolicy(sizePolicy3)
        self.hBase_4.setStyleSheet(u"color:#888;background:black")
        self.hBase_4.setFrame(False)

        self.verticalLayout_4.addWidget(self.hBase_4)

        self.hBase_5 = QLineEdit(Widget)
        self.hBase_5.setObjectName(u"hBase_5")
        self.hBase_5.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.hBase_5.sizePolicy().hasHeightForWidth())
        self.hBase_5.setSizePolicy(sizePolicy3)
        self.hBase_5.setStyleSheet(u"color:#888;background:black")
        self.hBase_5.setFrame(False)

        self.verticalLayout_4.addWidget(self.hBase_5)

        self.label_22 = QLabel(Widget)
        self.label_22.setObjectName(u"label_22")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy5)
        self.label_22.setStyleSheet(u"color:#888")
        self.label_22.setScaledContents(False)
        self.label_22.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_22)


        self.horizontalLayout_16.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_23 = QLabel(Widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color:#888")
        self.label_23.setScaledContents(False)
        self.label_23.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_23)

        self.hBase_6 = QLineEdit(Widget)
        self.hBase_6.setObjectName(u"hBase_6")
        self.hBase_6.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.hBase_6.sizePolicy().hasHeightForWidth())
        self.hBase_6.setSizePolicy(sizePolicy3)
        self.hBase_6.setStyleSheet(u"color:#888;background:black")
        self.hBase_6.setFrame(False)

        self.verticalLayout_5.addWidget(self.hBase_6)

        self.hBase_7 = QLineEdit(Widget)
        self.hBase_7.setObjectName(u"hBase_7")
        self.hBase_7.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.hBase_7.sizePolicy().hasHeightForWidth())
        self.hBase_7.setSizePolicy(sizePolicy3)
        self.hBase_7.setStyleSheet(u"color:#888;background:black")
        self.hBase_7.setFrame(False)

        self.verticalLayout_5.addWidget(self.hBase_7)

        self.hBase_8 = QLineEdit(Widget)
        self.hBase_8.setObjectName(u"hBase_8")
        self.hBase_8.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.hBase_8.sizePolicy().hasHeightForWidth())
        self.hBase_8.setSizePolicy(sizePolicy3)
        self.hBase_8.setStyleSheet(u"color:#888;background:black")
        self.hBase_8.setFrame(False)

        self.verticalLayout_5.addWidget(self.hBase_8)

        self.hBase_9 = QLineEdit(Widget)
        self.hBase_9.setObjectName(u"hBase_9")
        self.hBase_9.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.hBase_9.sizePolicy().hasHeightForWidth())
        self.hBase_9.setSizePolicy(sizePolicy3)
        self.hBase_9.setStyleSheet(u"color:#888;background:black")
        self.hBase_9.setFrame(False)

        self.verticalLayout_5.addWidget(self.hBase_9)


        self.horizontalLayout_16.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_19 = QLabel(Widget)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setStyleSheet(u"color:#888")
        self.label_19.setScaledContents(False)
        self.label_19.setWordWrap(True)

        self.horizontalLayout_17.addWidget(self.label_19)

        self.hTwo_3 = QLineEdit(Widget)
        self.hTwo_3.setObjectName(u"hTwo_3")
        self.hTwo_3.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.hTwo_3.sizePolicy().hasHeightForWidth())
        self.hTwo_3.setSizePolicy(sizePolicy3)
        self.hTwo_3.setStyleSheet(u"color:#888;background:black")
        self.hTwo_3.setFrame(False)

        self.horizontalLayout_17.addWidget(self.hTwo_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_20 = QLabel(Widget)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setStyleSheet(u"color:#888")
        self.label_20.setScaledContents(False)
        self.label_20.setWordWrap(True)

        self.horizontalLayout_18.addWidget(self.label_20)

        self.hPlus_3 = QLineEdit(Widget)
        self.hPlus_3.setObjectName(u"hPlus_3")
        self.hPlus_3.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.hPlus_3.sizePolicy().hasHeightForWidth())
        self.hPlus_3.setSizePolicy(sizePolicy3)
        self.hPlus_3.setStyleSheet(u"color:#888;background:black")
        self.hPlus_3.setFrame(False)

        self.horizontalLayout_18.addWidget(self.hPlus_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_25 = QLabel(Widget)
        self.label_25.setObjectName(u"label_25")
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)
        self.label_25.setStyleSheet(u"color:#888")
        self.label_25.setScaledContents(False)
        self.label_25.setWordWrap(True)

        self.horizontalLayout_19.addWidget(self.label_25)

        self.hPlus_4 = QLineEdit(Widget)
        self.hPlus_4.setObjectName(u"hPlus_4")
        self.hPlus_4.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.hPlus_4.sizePolicy().hasHeightForWidth())
        self.hPlus_4.setSizePolicy(sizePolicy3)
        self.hPlus_4.setStyleSheet(u"color:#888;background:black")
        self.hPlus_4.setFrame(False)

        self.horizontalLayout_19.addWidget(self.hPlus_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy4.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy4)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.pushButton_3)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)


        self.horizontalLayout_20.addLayout(self.verticalLayout_9)

        self.horizontalSpacer = QSpacerItem(21, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_26 = QLabel(Widget)
        self.label_26.setObjectName(u"label_26")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy6)

        self.verticalLayout_2.addWidget(self.label_26)

        self.line_4 = QFrame(Widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_27 = QLabel(Widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"color:#888")

        self.horizontalLayout_21.addWidget(self.label_27)

        self.lcdNumber = QLCDNumber(Widget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        sizePolicy4.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy4)
        self.lcdNumber.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lcdNumber.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_21.addWidget(self.lcdNumber)


        self.verticalLayout_2.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_28 = QLabel(Widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"color:#888")

        self.horizontalLayout_22.addWidget(self.label_28)

        self.lcdNumber_2 = QLCDNumber(Widget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        sizePolicy4.setHeightForWidth(self.lcdNumber_2.sizePolicy().hasHeightForWidth())
        self.lcdNumber_2.setSizePolicy(sizePolicy4)
        self.lcdNumber_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_22.addWidget(self.lcdNumber_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_22)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_29 = QLabel(Widget)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_6.addWidget(self.label_29)

        self.line_5 = QFrame(Widget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_5)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_30 = QLabel(Widget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"color:#888")

        self.horizontalLayout_23.addWidget(self.label_30)

        self.lcdNumber_3 = QLCDNumber(Widget)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        sizePolicy4.setHeightForWidth(self.lcdNumber_3.sizePolicy().hasHeightForWidth())
        self.lcdNumber_3.setSizePolicy(sizePolicy4)
        self.lcdNumber_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lcdNumber_3.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_23.addWidget(self.lcdNumber_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_31 = QLabel(Widget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"color:#888")

        self.horizontalLayout_24.addWidget(self.label_31)

        self.lcdNumber_4 = QLCDNumber(Widget)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")
        sizePolicy4.setHeightForWidth(self.lcdNumber_4.sizePolicy().hasHeightForWidth())
        self.lcdNumber_4.setSizePolicy(sizePolicy4)
        self.lcdNumber_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lcdNumber_4.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_24.addWidget(self.lcdNumber_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_33 = QLabel(Widget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"color:#888")

        self.horizontalLayout_26.addWidget(self.label_33)

        self.lcdNumber_6 = QLCDNumber(Widget)
        self.lcdNumber_6.setObjectName(u"lcdNumber_6")
        sizePolicy4.setHeightForWidth(self.lcdNumber_6.sizePolicy().hasHeightForWidth())
        self.lcdNumber_6.setSizePolicy(sizePolicy4)
        self.lcdNumber_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lcdNumber_6.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_26.addWidget(self.lcdNumber_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_26)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_34 = QLabel(Widget)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_8.addWidget(self.label_34)

        self.line_6 = QFrame(Widget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_6)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_35 = QLabel(Widget)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"color:#888")

        self.horizontalLayout_27.addWidget(self.label_35)

        self.lcdNumber_7 = QLCDNumber(Widget)
        self.lcdNumber_7.setObjectName(u"lcdNumber_7")
        sizePolicy4.setHeightForWidth(self.lcdNumber_7.sizePolicy().hasHeightForWidth())
        self.lcdNumber_7.setSizePolicy(sizePolicy4)
        self.lcdNumber_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lcdNumber_7.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_27.addWidget(self.lcdNumber_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_36 = QLabel(Widget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"color:#888")

        self.horizontalLayout_28.addWidget(self.label_36)

        self.lcdNumber_8 = QLCDNumber(Widget)
        self.lcdNumber_8.setObjectName(u"lcdNumber_8")
        sizePolicy4.setHeightForWidth(self.lcdNumber_8.sizePolicy().hasHeightForWidth())
        self.lcdNumber_8.setSizePolicy(sizePolicy4)
        self.lcdNumber_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lcdNumber_8.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_28.addWidget(self.lcdNumber_8)


        self.verticalLayout_8.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_37 = QLabel(Widget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"color:#888")

        self.horizontalLayout_29.addWidget(self.label_37)

        self.lcdNumber_9 = QLCDNumber(Widget)
        self.lcdNumber_9.setObjectName(u"lcdNumber_9")
        sizePolicy4.setHeightForWidth(self.lcdNumber_9.sizePolicy().hasHeightForWidth())
        self.lcdNumber_9.setSizePolicy(sizePolicy4)
        self.lcdNumber_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lcdNumber_9.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_29.addWidget(self.lcdNumber_9)


        self.verticalLayout_8.addLayout(self.horizontalLayout_29)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)

        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy7)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.frame)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)


        self.horizontalLayout_20.addLayout(self.verticalLayout_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_20)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(Widget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout_11.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Nomina", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Horas trabajadas:", None))
        self.hours.setText(QCoreApplication.translate("Widget", u"40", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"Pago por hora:", None))
        self.payment.setText(QCoreApplication.translate("Widget", u"40000", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"Clasificaci\u00f3n de horas", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Base (0 a 40):", None))
        self.hBase.setText(QCoreApplication.translate("Widget", u"40", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"Dobles (40.01 a 65):", None))
        self.hTwo.setText(QCoreApplication.translate("Widget", u"15", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"Triples (> 65)\n"
"+15% de bonus", None))
        self.hPlus.setText(QCoreApplication.translate("Widget", u"15", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Modificar", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"Descuentos", None))
        self.label_18.setText(QCoreApplication.translate("Widget", u"ISR:", None))
        self.label_21.setText(QCoreApplication.translate("Widget", u"Sueldo maximo ($)", None))
        self.hBase_3.setText(QCoreApplication.translate("Widget", u"8000", None))
        self.hBase_4.setText(QCoreApplication.translate("Widget", u"13500", None))
        self.hBase_5.setText(QCoreApplication.translate("Widget", u"25000", None))
        self.label_22.setText(QCoreApplication.translate("Widget", u"m\u00e1s", None))
        self.label_23.setText(QCoreApplication.translate("Widget", u"Pago (%)", None))
        self.hBase_6.setText(QCoreApplication.translate("Widget", u"0", None))
        self.hBase_7.setText(QCoreApplication.translate("Widget", u"10", None))
        self.hBase_8.setText(QCoreApplication.translate("Widget", u"19", None))
        self.hBase_9.setText(QCoreApplication.translate("Widget", u"23", None))
        self.label_19.setText(QCoreApplication.translate("Widget", u"IMSS (%):", None))
        self.hTwo_3.setText(QCoreApplication.translate("Widget", u"3.5", None))
        self.label_20.setText(QCoreApplication.translate("Widget", u"Sindicato ($):", None))
        self.hPlus_3.setText(QCoreApplication.translate("Widget", u"150", None))
        self.label_25.setText(QCoreApplication.translate("Widget", u"Gastos varios ($):", None))
        self.hPlus_4.setText(QCoreApplication.translate("Widget", u"220", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Modificar", None))
        self.label_26.setText(QCoreApplication.translate("Widget", u"Horas trabajadas", None))
        self.label_27.setText(QCoreApplication.translate("Widget", u"Horas totales:", None))
        self.label_28.setText(QCoreApplication.translate("Widget", u"Horas extra:", None))
        self.label_29.setText(QCoreApplication.translate("Widget", u"Deducciones", None))
        self.label_30.setText(QCoreApplication.translate("Widget", u"ISR:", None))
        self.label_31.setText(QCoreApplication.translate("Widget", u"Seguro:", None))
        self.label_33.setText(QCoreApplication.translate("Widget", u"Otros:", None))
        self.label_34.setText(QCoreApplication.translate("Widget", u"Pago", None))
        self.label_35.setText(QCoreApplication.translate("Widget", u"Subtotal:", None))
        self.label_36.setText(QCoreApplication.translate("Widget", u"Deducciones:", None))
        self.label_37.setText(QCoreApplication.translate("Widget", u"Total:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Copiar", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"Guardar", None))
    # retranslateUi

