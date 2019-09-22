from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebView

app = QApplication([])
win = QWebView()

html = '''<html>
<head>
<title>A Sample Page</title>
</head>
<body>
<h1>Hello, World!</h1>
<hr />
I have nothing to say.
</body>
</html>'''
win.setHtml(html)

win.show()
app.exec_()
