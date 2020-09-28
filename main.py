import pyttsx3
import PyPDF2
from tkinter.filedialog import *
root=Tk()
root.overrideredirect(1)
root.image = PhotoImage(file='logo.gif')
label = Label(image=root.image)
label.pack()
book = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

for num in range(0, pages):
    page = pdfReader.getPage(0)
    text = page.extractText()
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()


