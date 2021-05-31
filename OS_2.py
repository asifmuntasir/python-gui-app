from tkinter import*
from tkinter import Menu
import os
import glob

root = Tk()
root.title("Find your files!")
root.geometry("400x300")

#Directory selection
clicked1 = StringVar()
clicked1.set("Directories!")
directories = {'Local Disk: C','Local Disk: D','Local Disk: G'}

popupMenu1 = OptionMenu(root, clicked1, *directories)
popupMenu1.grid(row = 0, column = 0)


#File type selection
clicked2 = StringVar()
clicked2.set("File Type!")
types = {'.c','.cpp','.py','.java','.pdf','.txt','.doc','.PNG','.JPG','.JPEG','.exe'}

popupMenu2 = OptionMenu(root, clicked2, *types)
popupMenu2.grid(row=0, column=2)


fileList = Listbox(root,width=23,height=10)
fileList.grid(row=1,column=2)
scroll = Scrollbar(root,command=fileList.yview)
scroll.grid(row=1, column=3, sticky='ns')



def showfiles():
    value=clicked1.get()
    if value == 'Local Disk: G':
        check=clicked2.get()
        if check == '.pdf':
            g=glob.glob("G:\\*.pdf")
            for f in g:
                fileList.insert(END,f)
        elif check == '.c':
            g=glob.glob("G:\\*.c")
            for f in g:
                fileList.insert(END,f)
        elif check == '.cpp':
            g=glob.glob("G:\\*.cpp")
            for f in g:
                fileList.insert(END,f)
        elif check == '.txt':
            g=glob.glob("G:\\*.txt")
            for f in g:
                fileList.insert(END,f)    
        elif check == '.py':
            g=glob.glob("G:\\*.py")
            for f in g:
                fileList.insert(END,f)
        elif check == '.java':
            g=glob.glob("G:\\*.java")
            for f in g:
                fileList.insert(END,f)
        elif check == '.doc':
            g=glob.glob("G:\\*.doc")
            for f in g:
                fileList.insert(END,f)
        elif check == '.PNG':
            g=glob.glob("G:\\*.PNG")
            for f in g:
                fileList.insert(END,f)
        elif check == '.JPG':
            g=glob.glob("G:\\*.JPG")
            for f in g:
                fileList.insert(END,f)
        elif check == '.JPEG':
            g=glob.glob("G:\\*.JPEG")
            for f in g:
                fileList.insert(END,f)
    if value == 'Local Disk: C':
        check=clicked2.get()
        if check == '.pdf':
            g=glob.glob("C:\\*.pdf")
            for f in g:
                fileList.insert(END,f)
        elif check == '.c':
            g=glob.glob("C:\\*.c")
            for f in g:
                fileList.insert(END,f)
        elif check == '.cpp':
            g=glob.glob("C:\\*.cpp")
            for f in g:
                fileList.insert(END,f)
        elif check == '.txt':
            g=glob.glob("C:\\*.txt")
            for f in g:
                fileList.insert(END,f)    
        elif check == '.py':
            g=glob.glob("C:\\*.py")
            for f in g:
                fileList.insert(END,f)
        elif check == '.java':
            g=glob.glob("C:\\*.java")
            for f in g:
                fileList.insert(END,f)
        elif check == '.doc':
            g=glob.glob("C:\\*.doc")
            for f in g:
                fileList.insert(END,f)
        elif check == '.PNG':
            g=glob.glob("C:\\*.PNG")
            for f in g:
                fileList.insert(END,f)
        elif check == '.JPG':
            g=glob.glob("C:\\*.JPG")
            for f in g:
                fileList.insert(END,f)
        elif check == '.JPEG':
            g=glob.glob("C:\\*.JPEG")
            for f in g:
                fileList.insert(END,f)
    if value == 'Local Disk: D':
        check=clicked2.get()
        if check == '.pdf':
            g=glob.glob("D:\\*.pdf")
            for f in g:
                fileList.insert(END,f)
        elif check == '.c':
            g=glob.glob("D:\\*.c")
            for f in g:
                fileList.insert(END,f)
        elif check == '.cpp':
            g=glob.glob("D:\\*.cpp")
            for f in g:
                fileList.insert(END,f)
        elif check == '.txt':
            g=glob.glob("D:\\*.txt")
            for f in g:
                fileList.insert(END,f)    
        elif check == '.py':
            g=glob.glob("D:\\*.py")
            for f in g:
                fileList.insert(END,f)
        elif check == '.java':
            g=glob.glob("D:\\*.java")
            for f in g:
                fileList.insert(END,f)
        elif check == '.doc':
            g=glob.glob("D:\\*.doc")
            for f in g:
                fileList.insert(END,f)
        elif check == '.PNG':
            g=glob.glob("D:\\*.PNG")
            for f in g:
                fileList.insert(END,f)
        elif check == '.JPG':
            g=glob.glob("D:\\*.JPG")
            for f in g:
                fileList.insert(END,f)
        elif check == '.JPEG':
            g=glob.glob("D:\\*.JPEG")
            for f in g:
                fileList.insert(END,f)
        elif check == '.exe':
            g=glob.glob("D:\\*.exe")
            for f in g:
                fileList.insert(END,f)


btn = Button(root,text="Search", command=showfiles,bg='yellowgreen')
btn.grid(row=0, column=4)


root.mainloop()

