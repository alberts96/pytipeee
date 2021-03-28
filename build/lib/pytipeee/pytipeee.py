
import urllib.request
import json 

categories = {
    "other":"32",
    "bd-illustration":"33",
    "movies":"34",
    "food":"35",
    "geek":"36",
    "video-game":"38",
    "humour":"37",
    "journalism":"39",
    "books":"40",
    "fashion":"41",
    "music":"42",
    "photography":"43",
    "science-technology":"44",
    "performing-arts":"45",
    "sports":"46",
    "vlog":"47",
    "streaming":"52"
}

superheaders = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}

def show_categories(categories = categories):
    """
    Show list of admissible values for category 
    """
    for category in categories.keys():
        print(category)
        
# TO REQUEST ONE SINGLE JSON WEB PAGE
def requesting(url, headers = superheaders):
    req = urllib.request.Request(url,headers=headers)
    response= urllib.request.urlopen(req)
    data = response.read()
    encoding = response.info().get_content_charset('utf-8')
    data = json.loads(data.decode(encoding))
    return data



class Comment:
    
    def __init__(self,comment):
        self.id = comment['id']
        self.time = comment['created_at']
        self.author = comment['author']['username']
        self.author_id = comment['author']['id']
        def __cleanComment(text):
            import re 
            return re.sub('\n',' ',text)
        self.text = comment['body']
        
    def __repr__(self):
        
        return '\n ' + '\033[1m' + self.author+ '\033[0m' + '\n_____________________________________\n' + self.text + '\n'
   


class Tipper:
    '''
    Subscribed common user of tipeee
    '''
    def __init__(self, username):
        self.username = username
        self.tips = list()
    def __repr__(self):
        return self.username
    
    def get_tips(self):
        '''
        See all tips fro this user
        '''
        self.tips = list()
        data = requesting("https://api.tipeee.com/v2.0/users/{}".format(self.username))
        for subscription in data['activeSubscriptions'].keys:
            self.tips.append(data['activeSubscriptions'][subscription]['slug'])
        return self.tips
            
        
        
        
class Creator:
    
    
    def __init__(self, user):
        
        if type(user) == str: 
            self.username = user
            self.data = requesting("https://api.tipeee.com/v2.0/projects/{}".format(user))
            self.scraped = True
        else: 
            self.data = user
            self.username = user['slug']
            self.scraped = False
            
        self.id = self.data['id']
        self.lang = self.data['lang']
        self.tipperAmount = self.data['parameters']['tipperAmount']
        self.tipperNumber = self.data['parameters']['tipperNumber']
        self.newsNumber =   self.data['parameters']['newsNumber']
        self.subscription =  self.data['parameters']['activateAt']
        self.categories = set(category['slug'] for category in self.data['categories'])
        self.comments = list()
        self.goals = list()
        self.news = list()
        self.tippers = list()
        
        if self.scraped == True:
            self.num_comments = int(self.data['thread']['num_comments'])
            self.num_rewards = len(self.data['rewards'])
            self.num_goals = len(self.data['goals'])
        else :
            self.num_goals = None 
            self.num_rewards = None
            self.num_comments = None
            
    def more_info(self): 
        ''' 
        scrape the creators own web page
        '''
        self = self.__init__(self.username)
        
        
    def visit(self):
        '''
        Open the creator tipeee own web page 
        '''
        import webbrowser
        webbrowser.open_new("https://en.tipeee.com/{}/".format(self.username))
        
    def to_dict(self):
        '''
        Create a dictionary with main information for the creator
        '''
        return {
            "id" : self.id,
            "username" : self.username ,
            "lang" : self.lang,
            #"name" : self.name,
            "tipperAmount": self.tipperAmount,
            "tipperNumber" :self.tipperNumber,
            "newsNumber" : self.newsNumber,
            "subsciption" :   self.subscription,
            "categories" : self.categories,
            "num_comments": self.num_comments,
            "num_goals": self.num_goals,
            "num_rewards": self.num_rewards,
            
        }
    
    
    def get_comments(self):
        ''' 
        Return a list with all comments
        '''
        self.comments = list()
        page = '1'
        while True:
            data = requesting("https://api.tipeee.com/v2.0/threads/project_{}?page={}&perPage=150".format(self.id,page))
            for item in data['items'] : 
                self.comments.append(Comment(item))
            try: page = data['pager']['next']
            except: break
        return self.comments
                
    
    def get_news(self):
        '''
        Return a list with all news/works names updated by an author
        '''
        self.news = list()
        page = '1'
        while True:
            data = requesting("https://api.tipeee.com/v2.0/projects/{}/news?page={}&perPage=150".format(self.username,page))
            for item in data['items'] : 
                self.news.append(item['name'])
            try: page = data['pager']['next']
            except: break
        return self.news
    
    
    def get_tippers(self):
        '''
        Return all subscribed tippers of the creator 
        N.B. A lot of tippers are anonimous, not subscribed to tipeee
        '''
        self.tippers = list()
        page='1'
        while True:
            data = requesting("https://api.tipeee.com/v2.0/projects/{}/top/tippers?page={}&perPage=150".format(self.username,page))
            for item in data['items'] : 
                try: self.tippers.append(Tipper(item['username_canonical']))
                except: continue
            try: page = data['pager']['next']
            except: break
        return self.tippers
            
    
    def __repr__(self): return str(self.to_dict())

     
    def __gt__(self, anotherCreator):
        assert(type(anotherCreator) == type(self))
        if self.tipperNumber > anotherCreator.tipperNumber : return True
        else : return False 
        
    def __lt__(self, anotherCreator):
        assert(type(anotherCreator) == type(self))
        if self.tipperNumber < anotherCreator.tipperNumber : return True
        else : return False 
        
    def __eq__(self, anotherAuthor):
        assert(type(anotherCreator) == type(self))
        if self.username == anotherCreator.username : return True
        else: return False
        
        
        
        
    

class Creators:
    
    def __init__(self, lang='en'):
        self.lang = lang
        self.scraped =   list()
        self.creators = list()
       
        
    def __iter__(self):
        for elem in self.creators: 
            yield elem['slug']
            
    def __len__(self):
        return len(self.creators)
    
    def __repr__(self):
        return str(self.creators)
        
    def scrape(self, limit=None, category=None, headers=superheaders, lang=None):
        '''
        returns creator in a list 

       Parameters
       ----------
           limit : the number of creators to get, if not specified return all authors.
                Authors are crawled in the order giben by the site 
                N.B. if not specified can take some time 

           category : specifying a category will obtain only authors of that category 
               N.B. run pytipeee.show_categories() to see admissible vlaues for category
       '''    
        
        def __params_setting(category=category, limit=limit, headers = headers, lang=lang):
            if limit != None: assert(type(limit)==int)
            if lang not in ['en','de','fr','es','it']: lang = 'en'
            mode = 'default'
            if category != None:
                if category in categories:
                    category = '&category='+str(categories[category])
                    mode = 'category'
                else:
                    print('wrong value for category: will not be considered')
            else:
                category=''
            return limit, mode, category, headers, lang
        
             # PARAMETHERS SETTING
        limit, mode ,category, headers, lang = __params_setting(category,limit,headers,lang)
        page='1'
        base_url = 'https://api.tipeee.com/v2.0/projects?mode={}&page={}&perPage=150&lang={}{}'
        creators_list = list()
        
            #COLLECTING DATA
        while len(creators_list) < limit:
            data = requesting(base_url.format(mode, page, lang, category), headers) 
            creators_list += data['items']
            try: 
                page = data['pager']['next']
            except: 
                break
        if len(creators_list) >  limit : creators_list = creators_list[:limit]
        
        self.scraped = creators_list
        return creators_list
    
    
    def get_creators(self):
        ''' 
        paramether:
        ____________
        Trasform each scraped item in an element of class Crator, so you can call methods on it
        
        '''
        if len(self.scraped) > 0 :
            for item in self.scraped:
                try :
                    self.creators.append(Creator(item))
                except: 
                    print(item)
                    break
                    
   
    
    
    def to_dataframe(self, lang=None):
        """
        return a pandas dataframe 
        
        PARAMS:
            lang: chose the lenguage for categories.
        
        """
            
        if len(self.creators)==0: return 
        import pandas 
        columns = ['id','username','lang','categories','tipperAmount','tipperNumber','newsNumber']
        df = pandas.DataFrame(columns=columns)
        for creator in self.creators:
            df = df.append(creator.to_dict(), ignore_index=True)
        df.set_index('id',inplace=True)   
        
        return df
        
    