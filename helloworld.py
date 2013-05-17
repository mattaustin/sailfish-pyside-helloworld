#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide.QtCore import Qt
from PySide.QtDeclarative import QDeclarativeView
from PySide.QtGui import QApplication
import os
import sys


app = QApplication(sys.argv)


class View(QDeclarativeView):

    qml_source = os.path.join('qml', 'main.qml')

    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_OpaquePaintEvent)
        self.setAttribute(Qt.WA_NoSystemBackground)

        self.viewport().setAttribute(Qt.WA_OpaquePaintEvent)
        self.viewport().setAttribute(Qt.WA_NoSystemBackground)

        self.setResizeMode(QDeclarativeView.SizeRootObjectToView)
        self.setSource(self.qml_source)


if __name__ == "__main__":
    view = View()
    view.showFullScreen()
    app.exec_()
