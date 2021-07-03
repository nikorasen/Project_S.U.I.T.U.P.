# Project_S.U.I.T.U.P.
This is a web crawler/scraper which is meant to gather all the news from all of your favorite sources, Clip just the headlines and summaries and dates, then present them to you in news-ticker fashion. News-ticker, as in the text rolls steadily across the screen. 
As of 09/21/2020, the program is only able to crawl RSS feeds. Eventually it will be updated to include the following functions;
  1.Twitter feed parsing
  2.HTTP page parsing
  3.GUI Menu for archive & source management

SuitUp Program Anatomy and Explanation;
the first 6 lines are importing modules needed for the program to function.
The function “Spyder” is what actually crawls the RSS feeds, grabs the data, catalogs and edits it, then saves it to the Article Archive. It visits each line, and for each line in each entry it searches for the data with tags that match the parameters it is looking for- Title, Author, Date, etx. It searches for each parameter in the entries under multiple names (if no author, try media, if no media, try generator, else; assign n/a) At the end of each entry, Spyder reviews what it has collected, converts it to a string, then writes it to Art_Arch.txt.
The function Strip_XML1 removes a group of XML characters from the file using regex
The function Strip_XML2 removes a group of XML characters from the file using regex
Spyder is then called, because the rest of the functions depend upon the creation/updating of Art_Arch.txt
Strip_XML3 removes xml characters based on specifics values.
The window which contains the ticker is then built, and labeled. 
The function shif is my piece de resistance, the hardest one to figure out, the one I’m most proud of, despite being the shortest function. Shif makes the ticker TICK!
Finally, the window is called.
Version Alpha-Kappa has officially become Beta Version 1.0.
Functions exactly as intended, with same residual issue as Linux version; time objects aren’t correctly formatted.
Needs the following;
Update function
Auto Archive function
Menu
Time formatting
Commenting
Ability to add/remove sources
Twitter connectivity
html crawl ability for full web page scrape
To fix the time issue: use a regex to find all instances of time.time_struct, then store (temporarily) in a variable where it is converted into a normal time format and finally it replaces the time.time_struct object with the newly converted string. 

12/22/2020
Gonna try for Articles as a Class object.
Attributes for Class: Article
    1. Art_Tit = Article Title
    2. Art_Auth = Article Author
    3. Art_URL = Article Link
    4. Art_PT = Article Post Time
    5. Art_Desc = Article summary
    6. Art_Src = Article Source Name
Attributes for Class: Source
    1. Src_Name = Source display name (i.e.; Reuters News instead of the url, reuters.com)
    2. Src_URL = Source URL
for the Art_PT, when it gets printed to the ticker, that’s when it needs to be converted from a time string with datetime and strptime. 

The source class prompts the user for input to create the source. The class has a few methods; 
Src_Save – which appends the newly created source to a pickle file.
Src_URL_Load – which will be used by the crawler section to grab the URLs for each source
Src_Name_Load – which will be used by the writer section and appended to the corresponding articles as they get fed to the Ticker. 
Src_ID_Load – is mainly for posterity and troubleshooting purposes. If each source has a corresponding number ID then they can be easier to locate if one happens to be mistyping a source name when trying to pull feeds from just one source. 
Left off; finished the source class and all its methods, now I’m onto the Article class, its init is defined, I just need to give it methods. The question is, should I have the class itself parse the feeds or wait until the feedparser section creates the class instances? Will try both. 
The order of operations for article retrieval is as follows:
    1. Article Source
    2. Article ID
    3. Article Title
    4. Article Author
    5. Article URL
    6. Article Post Time
    7. Article Description
Lines 4-10 are module imports.
Class Source, needs an outside function to create Sources, preferably with windows and buttons. 