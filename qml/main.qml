import QtQuick 1.1
import Sailfish.Silica 1.0


ApplicationWindow {
    allowedOrientations: Orientation.Portrait

    initialPage: Page {
        Column {

            anchors.fill: parent

            PageHeader {
                title: "Hello World"
            }

            Label {
                text: "Hello sailors!"
                anchors.centerIn: parent
            }

        }
    }

}
