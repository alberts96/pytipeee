
import urllib.request
import json 



class Creators:
    
    def __init__(self, lang='en' ):
        self.lang = lang
        self.categroies = {'art-culture':'31', 'bd-illustration':'33', 'movies':'34', 'music':'42'}
        self.creators = []
        
    def __iter__(self):
        for elem in self.creators: 
            yield elem['slug']
            
    def __repr__(self):
        return self.creators
        
    def scrape(self, limit=None, headers=None, category=None):
        '''
        returns creator in a list 

       Parameters
       ----------
           limit : the number of creators to get, if not specified return all authors.
                Authors are crawled in the order giben by the site 
                N.B. if not specified can take some time 

           category : specifying a category will obtain only authors of that category 
       ''' 
    
        # TO REQUEST ONE SINGLE PAGE
        def requesting(url,headers = None):
            req = urllib.request.Request(url,headers=headers)
            response= urllib.request.urlopen(req)
            data = response.read()
            encoding = response.info().get_content_charset('utf-8')
            data = json.loads(data.decode(encoding))
            return data
        
        def get_hdr():
            return {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
        
        def params_setting(category=category, limit=limit, headers = headers):
            if limit != None: assert(type(limit)==int)
            if headers == None: headers = get_hdr()
            mode = 'default'
            if category != None:
                if category in ['food','health-well-being']:
                    category = 'category='+str(categories[category])
                    mode = 'category'
                else:
                    print('wrong value for category: will not be considered')
            else:
                category=''
            return limit, mode, category, headers
        
        
             # PARAMETHERS SETTING
        limit, mode ,category, headers = params_setting(category,limit,headers)
        page='1'
        base_url = 'https://api.tipeee.com/v2.0/projects?mode={}&page={}&perPage=150&lang=en{}'
        creators_list = list()
        #COLLECTING DATA
        while len(creators_list) < limit:
            data = requesting(base_url.format(mode, page, category), headers) 
            creators_list += data['items']
            try: 
                page = data['pager']['next']
            except: 
                break
        if len(creators_list) >  limit : creators_list = creators_list[:limit]
        
        self.creators = creators_list
        return creators_list
    
    
        