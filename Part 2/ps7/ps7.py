# 6.00.1x Problem Set 7
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 7

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, gid, titl, sub, summ, link):
        self.gid = gid
        self.titl = titl
        self.sub = sub
        self.summ = summ
        self.link = link
    
    def getGuid(self):
        return self.gid
    
    def getTitle(self):
        return self.titl

    def getSubject(self):
        return self.sub
        
    def getSummary(self):
        return self.summ

    def getLink(self):
        return self.link


#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word

    def isWordIn(self, text):
        text = text.replace("'",' ') # to keep word clean of things after the '
        text = text.translate(None, string.punctuation)
        if self.word in text.split():
            return True
        else:
            return False

class TitleTrigger(WordTrigger):   
    def evaluate(self, newsitem): # newsitem is expected to be a NewsStory object
        wTrigger = WordTrigger(self.word.lower())
        if wTrigger.isWordIn(newsitem.getTitle().lower()):
            return True
        else:
            return False

class SubjectTrigger(WordTrigger):
    def evaluate(self, newsitem): # newsitem is expected to be a NewsStory object
        wTrigger = WordTrigger(self.word.lower())
        if wTrigger.isWordIn(newsitem.getSubject().lower()):
            return True
        else:
            return False

class SummaryTrigger(WordTrigger):
    def evaluate(self, newsitem): # newsitem is expected to be a NewsStory object
        wTrigger = WordTrigger(self.word.lower())
        if wTrigger.isWordIn(newsitem.getSummary().lower()):
            return True
        else:
            return False


# Composite Triggers
# Problems 6-8

class NotTrigger(Trigger):
    def __init__(self, trig):
        self.trig = trig
    
    def evaluate(self, newsitem):
        if self.trig.evaluate(newsitem):
            return False
        else:
            return True

class AndTrigger(Trigger):
    def __init__(self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2
        
    def evaluate(self, newsitem):
        trig1_res = self.trig1.evaluate(newsitem)
        trig2_res = self.trig2.evaluate(newsitem)
        if trig1_res and trig2_res:
            return True
        else:
            return False

class OrTrigger(Trigger):
    def __init__(self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2
        
    def evaluate(self, newsitem):
        trig1_res = self.trig1.evaluate(newsitem)
        trig2_res = self.trig2.evaluate(newsitem)
        if trig1_res or trig2_res:
            return True
        else:
            return False


# Phrase Trigger
# Question 9

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    
    def evaluate(self, newsitem):
        for t in ('getTitle', 'getSubject', 'getSummary'):
            if self.phrase in getattr(newsitem, t)(): return True
        return False


#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered = []
    for story in stories:
        for trig in triggerlist:
            if trig.evaluate(story):
                filtered.append(story)
                break
    return filtered


#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    if triggerType == 'TITLE':
        triggerMap[name] = TitleTrigger(' '.join(params))
        return triggerMap[name]
    elif triggerType == 'SUBJECT':
        triggerMap[name] = SubjectTrigger(' '.join(params))
        return triggerMap[name]
    elif triggerType == 'SUMMARY':
        triggerMap[name] = SummaryTrigger(' '.join(params))
        return triggerMap[name]
    elif triggerType == 'PHRASE':
        triggerMap[name] = PhraseTrigger(' '.join(params))
        return triggerMap[name]
    elif triggerType == 'NOT':
        triggerMap[name] = NotTrigger(triggerMap[params[0]])
        return triggerMap[name]
    elif triggerType == 'AND':
        triggerMap[name] = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
        return triggerMap[name]
    elif triggerType == 'OR':
        triggerMap[name] = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
        return triggerMap[name]


def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        #t1 = TitleTrigger("Boston")
        #t2 = SubjectTrigger("Romney")
        #t3 = PhraseTrigger("Election")
        #t4 = OrTrigger(t2, t3)
        #triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        triggerlist = readTriggerConfig("triggers.txt")

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

