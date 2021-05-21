import requests     #use this module to get data form newsapi
import json         #use to convert data 

def speak(str):
    '''
    This function take string and read it
    '''
    from win32com.client import Dispatch
    s=Dispatch("SAPI.SpVoice")
    s.Speak(str)
    
    
if __name__=="__main__":
    #take data from newsapi
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=54218257f39b46e8aa62a2f1d7cb98b6"
    r=requests.get(url)
    
    #covert it into text then into python dictionary
    news=r.text
    news_dict=json.loads(news) 
    speak("todays news are")#loads take string()
    
    #iterate each news form aritcle
    for arts in news_dict['articles']:
        if arts==news_dict['articles'][len(news_dict['articles'])-1]:
            print(arts['title'])
            speak(arts['title'])
        else:
            print(arts['title'])
            speak(arts['title'])
            #speak("now moving to our next news....")
    speak("thanx for listening ")
