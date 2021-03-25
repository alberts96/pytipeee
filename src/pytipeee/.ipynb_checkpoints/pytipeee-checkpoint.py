
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
def show_categories(categories = categories):
    """
    Show list of admissible values for category 
    """
    for category in categories.keys():
        print(category)

class Creators:
    
    def __init__(self, lang='en'):
        self.lang = lang
        self.categroies = categories
        self.creators = []
        
    def __iter__(self):
        for elem in self.creators: 
            yield elem['slug']
            
    def __repr__(self):
        return str(self.creators)
        
    def scrape(self, limit=None, category=None, headers=None, lang=None):
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
    
        # TO REQUEST ONE SINGLE PAGE
        def __requesting(url, headers = headers):
            req = urllib.request.Request(url,headers=headers)
            response= urllib.request.urlopen(req)
            data = response.read()
            encoding = response.info().get_content_charset('utf-8')
            data = json.loads(data.decode(encoding))
            return data
        
        def __get_hdr():
            return {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
        
        def __params_setting(category=category, limit=limit, headers = headers, lang=lang):
            if limit != None: assert(type(limit)==int)
            if lang not in ['en','de','fr','es','it']: lang = 'en'
            if headers == None: headers = __get_hdr()
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
            data = __requesting(base_url.format(mode, page, lang, category), headers) 
            creators_list += data['items']
            try: 
                page = data['pager']['next']
            except: 
                break
        if len(creators_list) >  limit : creators_list = creators_list[:limit]
        
        self.creators = creators_list
        return creators_list
    
    
    def to_dataframe(self, lang=None):
        """
        return a pandas dataframe 
        
        PARAMS:
            lang: chose the lenguage for categories.
        
        """
        def __get_creator(item): 
            return {   
                'id' :           item['id'],
                'username' :     item['slug'],
                'lang' :         item['lang'],
                'photo_link' :   item['avatar']['filename'] ,
                'tipperAmount' : item['parameters']['tipperAmount'],
                'tipperNumber' : item['parameters']['tipperNumber'],
                'newsNumber' :   item['parameters']['newsNumber'],
                'categories' :   [category['slug'] for category in item['categories']]
            }
            
        if len(self.creators)==0: return 
        import pandas 
        columns = ['id','username','lang','categories','photo_link','tipperAmount','tipperNumber','newsNumber']
        df = pandas.DataFrame(columns=columns)
        for creator in self.creators:
            df = df.append(__get_creator(creator), ignore_index=True)
            
        df.set_index('id',inplace=True)   
        
        return df
        
    
    