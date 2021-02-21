from xml.dom.minidom import Document, parse
dom: Document = parse("Books.xml")
print(help(Document.toprettyxml))
