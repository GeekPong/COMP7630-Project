from langchin.document_loaders import PyPDFLoader
#Creater a instant of PyPDFLoader
loader = PyPDFLoader("/Path/.../Regulation.pdf")
Using the function of PyPDFLoader to load the PDF file
pages = loader.load()

