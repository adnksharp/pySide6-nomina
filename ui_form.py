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
        self.hl1 = QLabel(Widget)
        self.hl1.setObjectName(u"hl1")
        sizePolicy2.setHeightForWidth(self.hl1.sizePolicy().hasHeightForWidth())
        self.hl1.setSizePolicy(sizePolicy2)
        self.hl1.setStyleSheet(u"color:#888")
        self.hl1.setScaledContents(False)
        self.hl1.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.hl1)

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
        self.hl2 = QLabel(Widget)
        self.hl2.setObjectName(u"hl2")
        sizePolicy2.setHeightForWidth(self.hl2.sizePolicy().hasHeightForWidth())
        self.hl2.setSizePolicy(sizePolicy2)
        self.hl2.setStyleSheet(u"color:#888")
        self.hl2.setScaledContents(False)
        self.hl2.setWordWrap(True)

        self.horizontalLayout_10.addWidget(self.hl2)

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
        self.hl3 = QLabel(Widget)
        self.hl3.setObjectName(u"hl3")
        sizePolicy2.setHeightForWidth(self.hl3.sizePolicy().hasHeightForWidth())
        self.hl3.setSizePolicy(sizePolicy2)
        self.hl3.setStyleSheet(u"color:#888")
        self.hl3.setScaledContents(False)
        self.hl3.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.hl3)

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

        self.hEdit = QPushButton(Widget)
        self.hEdit.setObjectName(u"hEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.hEdit.sizePolicy().hasHeightForWidth())
        self.hEdit.setSizePolicy(sizePolicy4)
        self.hEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.hEdit)


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
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy5)
        self.label_21.setStyleSheet(u"color:#888")
        self.label_21.setScaledContents(False)
        self.label_21.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_21)

        self.isrM1 = QLineEdit(Widget)
        self.isrM1.setObjectName(u"isrM1")
        self.isrM1.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.isrM1.sizePolicy().hasHeightForWidth())
        self.isrM1.setSizePolicy(sizePolicy3)
        self.isrM1.setStyleSheet(u"color:#888;background:black")
        self.isrM1.setFrame(False)

        self.verticalLayout_4.addWidget(self.isrM1)

        self.isrM2 = QLineEdit(Widget)
        self.isrM2.setObjectName(u"isrM2")
        self.isrM2.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.isrM2.sizePolicy().hasHeightForWidth())
        self.isrM2.setSizePolicy(sizePolicy3)
        self.isrM2.setStyleSheet(u"color:#888;background:black")
        self.isrM2.setFrame(False)

        self.verticalLayout_4.addWidget(self.isrM2)

        self.isrM3 = QLineEdit(Widget)
        self.isrM3.setObjectName(u"isrM3")
        self.isrM3.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.isrM3.sizePolicy().hasHeightForWidth())
        self.isrM3.setSizePolicy(sizePolicy3)
        self.isrM3.setStyleSheet(u"color:#888;background:black")
        self.isrM3.setFrame(False)

        self.verticalLayout_4.addWidget(self.isrM3)

        self.label_22 = QLabel(Widget)
        self.label_22.setObjectName(u"label_22")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy6)
        self.label_22.setStyleSheet(u"color:#888")
        self.label_22.setScaledContents(False)
        self.label_22.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_22)


        self.horizontalLayout_16.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_23 = QLabel(Widget)
        self.label_23.setObjectName(u"label_23")
        sizePolicy5.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy5)
        self.label_23.setStyleSheet(u"color:#888")
        self.label_23.setScaledContents(False)
        self.label_23.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_23)

        self.isrP1 = QLineEdit(Widget)
        self.isrP1.setObjectName(u"isrP1")
        self.isrP1.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.isrP1.sizePolicy().hasHeightForWidth())
        self.isrP1.setSizePolicy(sizePolicy3)
        self.isrP1.setStyleSheet(u"color:#888;background:black")
        self.isrP1.setFrame(False)

        self.verticalLayout_5.addWidget(self.isrP1)

        self.isrP2 = QLineEdit(Widget)
        self.isrP2.setObjectName(u"isrP2")
        self.isrP2.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.isrP2.sizePolicy().hasHeightForWidth())
        self.isrP2.setSizePolicy(sizePolicy3)
        self.isrP2.setStyleSheet(u"color:#888;background:black")
        self.isrP2.setFrame(False)

        self.verticalLayout_5.addWidget(self.isrP2)

        self.isrP3 = QLineEdit(Widget)
        self.isrP3.setObjectName(u"isrP3")
        self.isrP3.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.isrP3.sizePolicy().hasHeightForWidth())
        self.isrP3.setSizePolicy(sizePolicy3)
        self.isrP3.setStyleSheet(u"color:#888;background:black")
        self.isrP3.setFrame(False)

        self.verticalLayout_5.addWidget(self.isrP3)

        self.isrP4 = QLineEdit(Widget)
        self.isrP4.setObjectName(u"isrP4")
        self.isrP4.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.isrP4.sizePolicy().hasHeightForWidth())
        self.isrP4.setSizePolicy(sizePolicy3)
        self.isrP4.setStyleSheet(u"color:#888;background:black")
        self.isrP4.setFrame(False)

        self.verticalLayout_5.addWidget(self.isrP4)


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

        self.imss = QLineEdit(Widget)
        self.imss.setObjectName(u"imss")
        self.imss.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.imss.sizePolicy().hasHeightForWidth())
        self.imss.setSizePolicy(sizePolicy3)
        self.imss.setStyleSheet(u"color:#888;background:black")
        self.imss.setFrame(False)

        self.horizontalLayout_17.addWidget(self.imss)


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

        self.uDeductions = QLineEdit(Widget)
        self.uDeductions.setObjectName(u"uDeductions")
        self.uDeductions.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.uDeductions.sizePolicy().hasHeightForWidth())
        self.uDeductions.setSizePolicy(sizePolicy3)
        self.uDeductions.setStyleSheet(u"color:#888;background:black")
        self.uDeductions.setFrame(False)

        self.horizontalLayout_18.addWidget(self.uDeductions)


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

        self.mDeductions = QLineEdit(Widget)
        self.mDeductions.setObjectName(u"mDeductions")
        self.mDeductions.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.mDeductions.sizePolicy().hasHeightForWidth())
        self.mDeductions.setSizePolicy(sizePolicy3)
        self.mDeductions.setStyleSheet(u"color:#888;background:black")
        self.mDeductions.setFrame(False)

        self.horizontalLayout_19.addWidget(self.mDeductions)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.dEdit = QPushButton(Widget)
        self.dEdit.setObjectName(u"dEdit")
        sizePolicy4.setHeightForWidth(self.dEdit.sizePolicy().hasHeightForWidth())
        self.dEdit.setSizePolicy(sizePolicy4)
        self.dEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.dEdit)


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
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy7)

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

        self.hTotal = QLCDNumber(Widget)
        self.hTotal.setObjectName(u"hTotal")
        sizePolicy4.setHeightForWidth(self.hTotal.sizePolicy().hasHeightForWidth())
        self.hTotal.setSizePolicy(sizePolicy4)
        self.hTotal.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.hTotal.setFrameShape(QFrame.Shape.NoFrame)
        self.hTotal.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_21.addWidget(self.hTotal)


        self.verticalLayout_2.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_28 = QLabel(Widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"color:#888")

        self.horizontalLayout_22.addWidget(self.label_28)

        self.hExtra = QLCDNumber(Widget)
        self.hExtra.setObjectName(u"hExtra")
        sizePolicy4.setHeightForWidth(self.hExtra.sizePolicy().hasHeightForWidth())
        self.hExtra.setSizePolicy(sizePolicy4)
        self.hExtra.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.hExtra.setFrameShape(QFrame.Shape.NoFrame)
        self.hExtra.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_22.addWidget(self.hExtra)


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

        self.dISR = QLCDNumber(Widget)
        self.dISR.setObjectName(u"dISR")
        sizePolicy4.setHeightForWidth(self.dISR.sizePolicy().hasHeightForWidth())
        self.dISR.setSizePolicy(sizePolicy4)
        self.dISR.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dISR.setFrameShape(QFrame.Shape.NoFrame)
        self.dISR.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_23.addWidget(self.dISR)


        self.verticalLayout_6.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_31 = QLabel(Widget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"color:#888")

        self.horizontalLayout_24.addWidget(self.label_31)

        self.dIMSS = QLCDNumber(Widget)
        self.dIMSS.setObjectName(u"dIMSS")
        sizePolicy4.setHeightForWidth(self.dIMSS.sizePolicy().hasHeightForWidth())
        self.dIMSS.setSizePolicy(sizePolicy4)
        self.dIMSS.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dIMSS.setFrameShape(QFrame.Shape.NoFrame)
        self.dIMSS.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_24.addWidget(self.dIMSS)


        self.verticalLayout_6.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_33 = QLabel(Widget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"color:#888")

        self.horizontalLayout_26.addWidget(self.label_33)

        self.dMore = QLCDNumber(Widget)
        self.dMore.setObjectName(u"dMore")
        sizePolicy4.setHeightForWidth(self.dMore.sizePolicy().hasHeightForWidth())
        self.dMore.setSizePolicy(sizePolicy4)
        self.dMore.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dMore.setFrameShape(QFrame.Shape.NoFrame)
        self.dMore.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_26.addWidget(self.dMore)


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

        self.sTotal = QLCDNumber(Widget)
        self.sTotal.setObjectName(u"sTotal")
        sizePolicy4.setHeightForWidth(self.sTotal.sizePolicy().hasHeightForWidth())
        self.sTotal.setSizePolicy(sizePolicy4)
        self.sTotal.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sTotal.setFrameShape(QFrame.Shape.NoFrame)
        self.sTotal.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_27.addWidget(self.sTotal)


        self.verticalLayout_8.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_36 = QLabel(Widget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"color:#888")

        self.horizontalLayout_28.addWidget(self.label_36)

        self.aDeductions = QLCDNumber(Widget)
        self.aDeductions.setObjectName(u"aDeductions")
        sizePolicy4.setHeightForWidth(self.aDeductions.sizePolicy().hasHeightForWidth())
        self.aDeductions.setSizePolicy(sizePolicy4)
        self.aDeductions.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.aDeductions.setFrameShape(QFrame.Shape.NoFrame)
        self.aDeductions.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_28.addWidget(self.aDeductions)


        self.verticalLayout_8.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_37 = QLabel(Widget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"color:#888")

        self.horizontalLayout_29.addWidget(self.label_37)

        self.final_2 = QLCDNumber(Widget)
        self.final_2.setObjectName(u"final_2")
        sizePolicy4.setHeightForWidth(self.final_2.sizePolicy().hasHeightForWidth())
        self.final_2.setSizePolicy(sizePolicy4)
        self.final_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.final_2.setFrameShape(QFrame.Shape.NoFrame)
        self.final_2.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_29.addWidget(self.final_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_29)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)

        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy8)
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
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(Widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout_11.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Nomina", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Horas trabajadas:", None))
        self.hours.setText(QCoreApplication.translate("Widget", u"0", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"Pago por hora:", None))
        self.payment.setText(QCoreApplication.translate("Widget", u"0", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"Clasificaci\u00f3n de horas", None))
        self.hl1.setText(QCoreApplication.translate("Widget", u"Base (0 a 40):", None))
        self.hBase.setText(QCoreApplication.translate("Widget", u"40", None))
        self.hl2.setText(QCoreApplication.translate("Widget", u"Dobles (40.01 a 65):", None))
        self.hTwo.setText(QCoreApplication.translate("Widget", u"15", None))
        self.hl3.setText(QCoreApplication.translate("Widget", u"Triples (> 65)\n"
"+15% de bonus:", None))
        self.hPlus.setText(QCoreApplication.translate("Widget", u"15", None))
        self.hEdit.setText(QCoreApplication.translate("Widget", u"Modificar", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"Descuentos", None))
        self.label_18.setText(QCoreApplication.translate("Widget", u"ISR:", None))
        self.label_21.setText(QCoreApplication.translate("Widget", u"Sueldo maximo ($)", None))
        self.isrM1.setText(QCoreApplication.translate("Widget", u"8000", None))
        self.isrM2.setText(QCoreApplication.translate("Widget", u"13500", None))
        self.isrM3.setText(QCoreApplication.translate("Widget", u"25000", None))
        self.label_22.setText(QCoreApplication.translate("Widget", u"m\u00e1s", None))
        self.label_23.setText(QCoreApplication.translate("Widget", u"Pago (%)", None))
        self.isrP1.setText(QCoreApplication.translate("Widget", u"0", None))
        self.isrP2.setText(QCoreApplication.translate("Widget", u"10", None))
        self.isrP3.setText(QCoreApplication.translate("Widget", u"19", None))
        self.isrP4.setText(QCoreApplication.translate("Widget", u"23", None))
        self.label_19.setText(QCoreApplication.translate("Widget", u"IMSS (%):", None))
        self.imss.setText(QCoreApplication.translate("Widget", u"3.5", None))
        self.label_20.setText(QCoreApplication.translate("Widget", u"Sindicato ($):", None))
        self.uDeductions.setText(QCoreApplication.translate("Widget", u"150", None))
        self.label_25.setText(QCoreApplication.translate("Widget", u"Gastos varios ($):", None))
        self.mDeductions.setText(QCoreApplication.translate("Widget", u"220", None))
        self.dEdit.setText(QCoreApplication.translate("Widget", u"Modificar", None))
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

