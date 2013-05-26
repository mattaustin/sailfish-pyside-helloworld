#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide.QtCore import Qt, QUrl
from PySide.QtDeclarative import QDeclarativeView
from PySide.QtGui import QApplication
import sys


class View(QDeclarativeView):

    qml_path = 'qml/main.qml'
    window_title = 'Hello World'

    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)

        self.setAttribute(Qt.WA_OpaquePaintEvent)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.viewport().setAttribute(Qt.WA_OpaquePaintEvent)
        self.viewport().setAttribute(Qt.WA_NoSystemBackground)

        self.setWindowTitle(self.window_title)
        self.setSource(QUrl.fromLocalFile(self.qml_path))
        self.setResizeMode(QDeclarativeView.SizeRootObjectToView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    view.showFullScreen()
    sys.exit(app.exec_())
