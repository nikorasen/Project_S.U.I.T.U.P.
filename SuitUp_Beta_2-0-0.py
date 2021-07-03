#S.U.I.T.U.P. V.2.0.0 BETA
#a RANT Original Script
#D.O.L.E.: 12/22/2020
import datetime as dt
import time
import feedparser
import re
import tkinter as tk
from tkinter import messagebox
import pickle as pk
class Source:
    Src_ID = 0
    def __init__(self, Src_Name, Src_URL):
        self.Src_Name = input('Enter the Name of the source: ')
        self.Src_URL = input('Enter the source URL: ')
        self.Src_ID += 1
    def Src_Save(self):
        try:
           pk.dump(Source,
           open('Sources.pkl', 'a'))
        except FileNotFoundError:
            pk.dump(Source,
            open('Sources.pkl', 'x'))
    def Src_URL_Load(self):
        try:
            pk.load(open('Sources.pkl'), 'r')
            return self.Src_URL
        except FileNotFoundError:
            print('Error Code: #0001, the Sources.pkl file cannot be found. Please create or locate the file and try again.')
    def Src_Name_Load(self):
        try:
            pk.load(open('Sources.pkl'), 'r')
            return self.Src_Name 
        except FileNotFoundError:
            print('Error Code: #0001, the Sources.pkl file cannot be found. Please create or locate the file and try again.')
    def Src_ID_Load(self):
        try:
            pk.load(open('Sources.pkl'), 'r')
            return self.Src_ID 
        except FileNotFoundError:
            print('Error Code: #0001, the Sources.pkl file cannot be found. Please create or locate the file and try again.')
class Article:
    Art_ID = 0
    Art_RTP = "" #Ready to print
    def __init__(self, Art_Title, Art_Auth, Art_URL, Art_PT, Art_Desc):
        self.Art_Title = ''
        self.Art_Auth = ''
        self.Art_URL = ''
        self.Art_PT = ''
        self.Art_Desc = ''
        self.Art_ID += 1
    def Art_Save(self):
        try:
            pk.dump(Article,
            open('Raw_Archive.pkl'), 'a')
        except FileNotFoundError:
            pk.dump(Article,
            open('Raw_Archive.pkl'), 'x')
    def Art_Load(self):
        Art_New = ""
        try:
            with open('Raw_Archive.pkl', 'r') as Archive:
                pk.load(open(Archive), 'r')
                for self in Archive:
                    Art_New += str(self.Art_Title) + str(self.Art_Auth) + str(self.Art_URL) + str(self.Art_PT) + str(self.Art_Desc)
                return str(Art_New)
        except FileNotFoundError:
            print('Error code #0002, the Art_Archive.pkl file cannot be found, Please create or locate the file and try again.')
        except EOFError:
            pass
    def Art_Clean(self):
        try:
            with open('Raw_Archive.pkl', 'a') as Archive:
                pk.load(open(Archive), 'a')
                for self in Archive:
                    self.Art_Title = self.Art_Title.strip('\n', 
                    '</a>', 
                    '</p>', 
                    '<p>', 
                    '</strong>', 
                    '<p><img', 
                    '<p><img ', 
                    ' <img ',
                    '<img width="300"',
                    '<img'
                    ' <img src=',
                    ' align="right"',
                    ' hspace="20" ',
                    ' vspace="20" ',
                    '<td',
                    '</td',
                    '</td>',
                    '<br',
                    ' <br />',
                    ' <br ',
                    'MISC',
                    ' MISC ',
                    '</a')
                    self.Art_Auth = self.Art_Auth.strip('\n', 
                    '</a>', 
                    '</p>', 
                    '<p>', 
                    '</strong>', 
                    '<p><img', 
                    '<p><img ', 
                    ' <img ',
                    '<img width="300"',
                    '<img'
                    ' <img src=',
                    ' align="right"',
                    ' hspace="20" ',
                    ' vspace="20" ',
                    '<td',
                    '</td',
                    '</td>',
                    '<br',
                    ' <br />',
                    ' <br ',
                    'MISC',
                    ' MISC ',
                    '</a')
                    self.Art_Desc = self.Art_Desc.strip('\n', 
                    '</a>', 
                    '</p>', 
                    '<p>', 
                    '</strong>', 
                    '<p><img', 
                    '<p><img ', 
                    ' <img ',
                    '<img width="300"',
                    '<img'
                    ' <img src=',
                    ' align="right"',
                    ' hspace="20" ',
                    ' vspace="20" ',
                    '<td',
                    '</td',
                    '</td>',
                    '<br',
                    ' <br />',
                    ' <br ',
                    'MISC',
                    ' MISC ',
                    '</a')
                    self.Art_URL = str(self.Art_URL)
                    self.Art_PT = time.asctime(self.Art_PT) #converts from unreadable time to human readable
                    self.Art_PT = str(self.Art_PT) #converts to string from time struct
                    with open('Art_Catalogue.txt', 'a') as Catalogue:
                       Art_RTP = ' Title: ' +str(self.Art_Title)+ ' Author: ' +str(self.Art_Auth)+ ' Post Time: ' +str(self.Art_PT)+ ' Summary: ' +str(self.Art_Desc)+ ' '
                       Catalogue.write(Art_RTP+'\n')
        except EOFError:
            pass
