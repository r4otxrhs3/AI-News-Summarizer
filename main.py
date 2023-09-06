#tkinter module is used to deisgn GUI
import tkinter as tk
#nltk is used as natural language toolkit
import nltk
#simplified text processing
from textblob import TextBlob
#to import news article
from newspaper import Article


'''
Calling a function summarize to get the url of the article
'''

def summarize():
    url= utext.get('1.0', 'end').strip()
    '''
    url= 'https://www.msn.com/en-in/entertainment/bollywood/shraddha-kapoor-becomes-center-of-jokes-as-rain-washes-ipl-2023-finale-actress-can-t-stop-laughing/ar-AA1bPhL3?ocid=winp1taskbar&cvid=2832791dbaaa4cd4beb1a7540d0a62fd&ei=11https://www.msn.com/en-in/entertainment/bollywood/shraddha-kapoor-becomes-center-of-jokes-as-rain-washes-ipl-2023-finale-actress-can-t-stop-laughing/ar-AA1bPhL3?ocid=winp1taskbar&cvid=2832791dbaaa4cd4beb1a7540d0a62fd&ei=11'
    '''
#THIS IS THE ALGORITHM OF THE PROJECT
    #retrieve, download the article and parse it.
    article= Article(url)
    article.download()
    article.parse()
#nlp stands for natural language processing, nltk stands for natural language tool kit
    article.nlp()

    #configure the title, author, publication, summary and sentiment parameters to normal
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    #delete them to get a fresh coloumn to reuse the window

    title.delete('1.0', 'end')
    title.insert('1.0', article.title )

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    #sentiment analysis and polarity analysis


    analysis= TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity:{analysis.polarity},Sentiment:  {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity<0 else "neutral"}')



#back to normal state


    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')




#tkinter, GUI designing



root= tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

tlabel= tk.Label(root, text='Title')
tlabel.pack()

title= tk.Text(root, height= 1,width=140)
title.config(state='disabled', bg= '#dddddd')
title.pack()
alabel= tk.Label(root, text='Author')
alabel.pack()

author= tk.Text(root, height= 1,width=140)
author.config(state='disabled', bg= '#dddddd')
author.pack()

plabel= tk.Label(root, text='Publishing Date')
plabel.pack()

publication= tk.Text(root, height= 1,width=140)
publication.config(state='disabled', bg= '#dddddd')
publication.pack()

slabel= tk.Label(root, text='Summary')
slabel.pack()

summary= tk.Text(root, height= 20,width=140)
summary.config(state='disabled', bg= '#dddddd')
summary.pack()

selabel= tk.Label(root, text= "Sentiment Analysis")
selabel.pack()

sentiment= tk.Text(root, height=1, width= 140)
sentiment.config(state='disabled', bg= '#dddddd')
sentiment.pack()

ulabel= tk.Label(root, text= "URL")
ulabel.pack()

utext= tk.Text(root, height=1, width= 140)
utext.pack()

btn= tk.Button(root, text= "Summarize", command= summarize)
btn.pack()




root.mainloop()



