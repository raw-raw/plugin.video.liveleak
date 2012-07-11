import urllib,urllib2,re,xbmcplugin,xbmcgui

#LiveLeak.com- by Oneadvent 2012.

def CATEGORIES():
        addDir('Popular','http://www.liveleak.com/browse',1,'')
        addDir('News & Politics','http://www.liveleak.com/c/news',1,'')
        addDir('Yoursay','http://www.liveleak.com/c/yoursay',1,'')
        addDir('Must See','http://www.liveleak.com/c/must_see',1,'')
        addDir('Iraq','http://www.liveleak.com/c/iraq',1,'')
        addDir('Afghanistan','http://www.liveleak.com/c/afghanistan',1,'')
        addDir('Entertainment','http://www.liveleak.com/c/entertainment',1,'')
                       
def INDEX(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="(.+?)"><img class="thumbnail_image" src="(.+?)" alt="(.+?)"').findall(link)
        for url,thumbnail,name in match:
	  req = urllib2.Request(url)
	  req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	  response = urllib2.urlopen(req)
	  link=response.read()
	  response.close()
	  match=re.compile('file: "(.+?)",').findall(link)
	  for url in match:
                addLink(name,url,'')
	  
def INDEX2(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile(' <a href="(.+?)"><img class="thumbnail_image" src="(.+?)" alt="(.+?)"').findall(link)
        for url,thumbnail,name in match:
	  req = urllib2.Request(url)
	  req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	  response = urllib2.urlopen(req)
	  link=response.read()
	  response.close()
	  match=re.compile('src="http://www.youtube.com/embed/(.+?)?rel=0').findall(link)
	  for url in match:
	    youtubeurl = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % url
	    addLink(name,youtubeurl,'')
                
def VIDEOLINKS(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('file: "(.+?)",').findall(link)
        for url in match:
                addLink(name,url,'')
        

                
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param




def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
              
params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print ""+url
        INDEX(url)
        
elif mode==2:
        print ""+url
        INDEX2(url)



xbmcplugin.endOfDirectory(int(sys.argv[1]))