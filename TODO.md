* Set background color to white
* Change line color to gray
* Add provision for adding margins to the layout boxes. 
Don't calculate the spacing from the margin directly let 
the layouts do the calculations.
* Create a new editor InlineEdit [QTextEdit](https://doc.qt.io/qt-5/qtextedit.html).
References 
    * [QTextDocument](https://doc.qt.io/qt-5/qtextdocument.html). 
    * [lineCount()](https://doc.qt.io/qt-5/qtextdocument.html#lineCount)
    * [QTextObjectInterface](https://doc.qt.io/qt-5/qtextobjectinterface.html)
    A text object describes the structure of one or more elements in a text document; 
    for instance, images imported from HTML are implemented using text objects. 
    * [QTextCursor](https://doc.qt.io/qt-5/qtextcursor.html) 
    * Matplotlib
        * https://stackoverflow.com/questions/2661441/matplotlib-write-tex-on-qt-form
        * [matplotlib.backends.backend_qt5agg](http://matplotlib.org/2.0.0b2/api/backend_qt5agg_api.html)
        The easiest way to generate images without having a window appear
        is use a non-interactive backend (see What is a backend?) such as Agg, SVG etc.
        * https://matplotlib.org/faq/usage_faq.html#what-is-a-backend