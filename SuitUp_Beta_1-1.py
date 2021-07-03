import tkinter as tk
import feedparser
import datetime
import time
from tkinter import messagebox
import re
def Spyder(): #Crawls the links in the sources file, saves them to a txt file
    All_Articles=''
    CPA_Art='' #Cleaned, Parsed, Added Articles
    try:
        with open('Sources.txt', 'r') as Srcs:
            for line in Srcs:
                Link=line
                Link=Link.strip('\n') #removes any newline characters
                Feed=feedparser.parse(Link)
                for entry in Feed.entries:
                    try:
                        Art_Title=entry.title
                    except AttributeError:
                        Art_Title='n/a'
                    try:
                        Art_Auth=entry.author
                    except AttributeError:
                        try:
                            Art_Auth=entry.media
                        except AttributeError:
                            try:
                                Art_Auth=entry.generator
                            except AttributeError:
                                Art_Auth='n/a'
                    try:
                        Art_URL=entry.link
                    except AttributeError:
                        try:
                            Art_URL=entry.url
                        except AttributeError:
                            Art_URL='n/a'
                    try:
                        Post_Time=entry.pubdate
                    except AttributeError:
                        try:
                            Post_Time=entry.pubDate
                        except AttributeError:
                            try:
                                Post_Time=entry.published_parsed
                            except AttributeError:
                                Post_Time='n/a'
                    try:
                        Desc=entry.summary
                    except AttributeError:
                        try:
                            Desc=entry.description
                        except AttributeError:
                            Desc='n/a'
                    All_Articles+=' Title: '+str(Art_Title)+' Author: '+str(Art_Auth)+' Link: '+str(Art_URL)+' Posted: '+str(Post_Time)+' Summary: '+str(Desc)+'\n'
    except EOFError:
        pass
    try:
        with open('Art_Arch.txt', 'a') as Svd: #Saves the All_Articles string to a text file
            Svd.write(All_Articles+'\n')
    except FileNotFoundError:
        with open('Art_Arch.txt', 'x') as Svd:
            Svd.write(All_Articles+'\n')
    except UnicodeEncodeError:
        CPA_Art=All_Articles.encode('utf-8','ignore').decode('utf-8')
        with open('Art_Arch.txt', 'a', encoding='utf-8') as Svd:
            Svd.write(All_Articles+'\n')
def shif():
    shif.msg = shif.msg[1:] + shif.msg[0]
    svar.set(shif.msg)
    root.after(150, shif)
def Strip_XML1(string): #Removes the XML characters from a passed string using a regex
    XML_Chr=re.compile(r'[\s()-]+')
    return XML_Chr.sub(' ', string)
def Strip_XML2(string): #Removes the XML characters from a passed string using a regex
    XML_Chr=re.compile(r'<.*?>')
    return XML_Chr.sub(' ', string)
def Strip_XML3(): #Finishes removing the XML characters from a passed string using specific instances
    strArticles=''
    try:
        with open('Art_Arch.txt', 'r') as Svd:
            strCurr_Disp=''
            for line in Svd:
                strCurr_Disp=line
                strCurr_Disp=strCurr_Disp.strip('\n')
                strCurr_Disp=strCurr_Disp.strip('</a>')
                strCurr_Disp=strCurr_Disp.strip('<a')
                strCurr_Disp=strCurr_Disp.strip('</p>')
                strCurr_Disp=strCurr_Disp.strip('<p>')
                strCurr_Disp=strCurr_Disp.strip('</strong>')
                strCurr_Disp=strCurr_Disp.strip('<p><img')
                strCurr_Disp=strCurr_Disp.strip(' <p><img ')
                strCurr_Disp=strCurr_Disp.strip(' <img ')
                strCurr_Disp=strCurr_Disp.strip('<img width="300"')
                strCurr_Disp=strCurr_Disp.strip('<img')
                strCurr_Disp=strCurr_Disp.strip(' <img src=')
                strCurr_Disp=strCurr_Disp.strip(' align="right" ')
                strCurr_Disp=strCurr_Disp.strip(' hspace="20" ')
                strCurr_Disp=strCurr_Disp.strip(' vspace="20" ')
                strCurr_Disp=strCurr_Disp.strip('<td')
                strCurr_Disp=strCurr_Disp.strip('</td')
                strCurr_Disp=strCurr_Disp.strip('</td>')
                strCurr_Disp=strCurr_Disp.strip('<br')
                strCurr_Disp=strCurr_Disp.strip(' <br />')
                strCurr_Disp=strCurr_Disp.strip(' <br ')
                strCurr_Disp=strCurr_Disp.strip('MISC')
                strCurr_Disp=strCurr_Disp.strip(' MISC ')
                strCurr_Disp=strCurr_Disp.strip('</a')
                strCurr_Disp=Strip_XML1(strCurr_Disp)
                strCurr_Disp=Strip_XML2(strCurr_Disp)
                strArticles=strArticles + str(strCurr_Disp)
                #shif.msg=(strArticles)
    except EOFError:
        pass
    except UnicodeDecodeError:
        strArticles=strArticles.encode('utf-8','ignore').decode('utf-8')
        #shif.msg=(strArticles)
    return strArticles
Spyder()
#Strip_XML3()
root = tk.Tk()
root.geometry('1900x30')
root.wm_title('S.U.I.T.U.P. Newsdesk BETA Ticker')
svar = tk.StringVar()
labl = tk.Label(root, textvariable=svar, height=25, bg='#003b6f', fg='white')
strArticles=Strip_XML3()
shif.msg=(strArticles)
shif()
labl.pack()
root.mainloop()
