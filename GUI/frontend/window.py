# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sun Feb  6 18:11:09 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(761, 591)
        self.configurationTab = QtGui.QWidget()
        self.configurationTab.setObjectName("configurationTab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.configurationTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.configurationTree = QtGui.QTreeView(self.configurationTab)
        self.configurationTree.setObjectName("configurationTree")
        self.horizontalLayout.addWidget(self.configurationTree)
        self.configurationDetailsLayout = QtGui.QVBoxLayout()
        self.configurationDetailsLayout.setObjectName("configurationDetailsLayout")
        self.configurationEditLayout = QtGui.QVBoxLayout()
        self.configurationEditLayout.setObjectName("configurationEditLayout")
        self.configurationVariableLabel = QtGui.QLabel(self.configurationTab)
        self.configurationVariableLabel.setObjectName("configurationVariableLabel")
        self.configurationEditLayout.addWidget(self.configurationVariableLabel)
        self.configurationValueEdit = QtGui.QPlainTextEdit(self.configurationTab)
        self.configurationValueEdit.setObjectName("configurationValueEdit")
        self.configurationEditLayout.addWidget(self.configurationValueEdit)
        self.configurationEditButtonsLayout = QtGui.QHBoxLayout()
        self.configurationEditButtonsLayout.setObjectName("configurationEditButtonsLayout")
        self.configurationDefaultButton = QtGui.QPushButton(self.configurationTab)
        self.configurationDefaultButton.setObjectName("configurationDefaultButton")
        self.configurationEditButtonsLayout.addWidget(self.configurationDefaultButton)
        self.configurationSetButton = QtGui.QPushButton(self.configurationTab)
        self.configurationSetButton.setObjectName("configurationSetButton")
        self.configurationEditButtonsLayout.addWidget(self.configurationSetButton)
        self.configurationEditLayout.addLayout(self.configurationEditButtonsLayout)
        self.configurationDetailsLayout.addLayout(self.configurationEditLayout)
        self.configurationHelpLabel = QtGui.QLabel(self.configurationTab)
        self.configurationHelpLabel.setObjectName("configurationHelpLabel")
        self.configurationDetailsLayout.addWidget(self.configurationHelpLabel)
        self.configurationHelp = QtGui.QPlainTextEdit(self.configurationTab)
        self.configurationHelp.setObjectName("configurationHelp")
        self.configurationDetailsLayout.addWidget(self.configurationHelp)
        self.horizontalLayout.addLayout(self.configurationDetailsLayout)
        window.addTab(self.configurationTab, "")
        self.commandsTab = QtGui.QWidget()
        self.commandsTab.setObjectName("commandsTab")
        self.verticalLayout = QtGui.QVBoxLayout(self.commandsTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.commandsHistory = QtGui.QPlainTextEdit(self.commandsTab)
        self.commandsHistory.setObjectName("commandsHistory")
        self.verticalLayout.addWidget(self.commandsHistory)
        self.commandsWritingLayout = QtGui.QHBoxLayout()
        self.commandsWritingLayout.setObjectName("commandsWritingLayout")
        self.commandEdit = QtGui.QLineEdit(self.commandsTab)
        self.commandEdit.setObjectName("commandEdit")
        self.commandsWritingLayout.addWidget(self.commandEdit)
        self.commandSend = QtGui.QPushButton(self.commandsTab)
        self.commandSend.setObjectName("commandSend")
        self.commandsWritingLayout.addWidget(self.commandSend)
        self.verticalLayout.addLayout(self.commandsWritingLayout)
        window.addTab(self.commandsTab, "")

        self.retranslateUi(window)
        window.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        window.setWindowTitle(QtGui.QApplication.translate("window", "TabWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.configurationVariableLabel.setText(QtGui.QApplication.translate("window", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.configurationDefaultButton.setText(QtGui.QApplication.translate("window", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.configurationSetButton.setText(QtGui.QApplication.translate("window", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.configurationHelpLabel.setText(QtGui.QApplication.translate("window", "Help", None, QtGui.QApplication.UnicodeUTF8))
        window.setTabText(window.indexOf(self.configurationTab), QtGui.QApplication.translate("window", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.commandSend.setText(QtGui.QApplication.translate("window", "Envoyer", None, QtGui.QApplication.UnicodeUTF8))
        window.setTabText(window.indexOf(self.commandsTab), QtGui.QApplication.translate("window", "Commands", None, QtGui.QApplication.UnicodeUTF8))

