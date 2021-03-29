# Pytipeee
``Pytipeee`` is an unofficial scraper for [tipeee.com](https://en.tipeee.com/) using python.
Codes are hosted in this [repository](https://github.com/alberts96/pytipeee),
Thanks to ``Pytipeee`` you are able to:
- Collect large amounts of creators by category
- see infromation for each creator
- read comments
- see news 
- get tipper and tips



## Installation
To install you can use pip by terminal:
```bash

pip install pytipeee
```

## Usage

### Import 


```python
import pytipeee as pt
```

### Categories

Different categories are available.



```python
pt.show_categories()
```

    other
    bd-illustration
    movies
    food
    geek
    video-game
    humour
    journalism
    books
    fashion
    music
    photography
    science-technology
    performing-arts
    sports
    vlog
    streaming
    

### Creators Collection 

You can collect a defined number of creators filtering by category...
by default the class ``Creators`` collect all creator of all categories.




```python
creators = pt.Creators()          #Initialize the class
creators.scrape(100,'vlog')       #scrape the site using a limit of creatros to collect ans a category 
creators.get_creators()           #transform each scraped in a Creator element
df = creators.to_dataframe()      #return a pandas dataframe
df.head()
```




<div>


    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>username</th>
      <th>lang</th>
      <th>categories</th>
      <th>tipperAmount</th>
      <th>tipperNumber</th>
      <th>newsNumber</th>
      <th>num_comments</th>
      <th>num_goals</th>
      <th>num_rewards</th>
      <th>subsciption</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>258359</th>
      <td>theoloji</td>
      <td>en</td>
      <td>{vlog, podcast}</td>
      <td>185</td>
      <td>5</td>
      <td>False</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>2020-09-24 23:13:20</td>
    </tr>
    <tr>
      <th>234038</th>
      <td>mountainsandcoconuts</td>
      <td>en</td>
      <td>{vlog, nature}</td>
      <td>15</td>
      <td>2</td>
      <td>False</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>2020-01-05 19:49:18</td>
    </tr>
    <tr>
      <th>136967</th>
      <td>antoine-le-guen</td>
      <td>en</td>
      <td>{vlog}</td>
      <td>150</td>
      <td>1</td>
      <td>8</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>False</td>
    </tr>
    <tr>
      <th>249220</th>
      <td>1upcrew</td>
      <td>en</td>
      <td>{art-culture, vlog}</td>
      <td>0</td>
      <td>1</td>
      <td>False</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>2020-06-02 11:19:38</td>
    </tr>
    <tr>
      <th>150377</th>
      <td>partager-cest-sympa</td>
      <td>fr</td>
      <td>{vlog, humour}</td>
      <td>10204</td>
      <td>1607</td>
      <td>56</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>2017-10-31 15:00:03</td>
    </tr>
  </tbody>
</table>
</div>



Some attributes are missing in the data collect for the moment... you can fill those field creator by creator...


```python
creator = creators.creators[3]
creator.more_info()
df = creators.to_dataframe()      
df.head()
```




<div>


    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
    
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>username</th>
      <th>lang</th>
      <th>categories</th>
      <th>tipperAmount</th>
      <th>tipperNumber</th>
      <th>newsNumber</th>
      <th>num_comments</th>
      <th>num_goals</th>
      <th>num_rewards</th>
      <th>subsciption</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>258359</th>
      <td>theoloji</td>
      <td>en</td>
      <td>{vlog, podcast}</td>
      <td>185</td>
      <td>5</td>
      <td>False</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>2020-09-24 23:13:20</td>
    </tr>
    <tr>
      <th>234038</th>
      <td>mountainsandcoconuts</td>
      <td>en</td>
      <td>{vlog, nature}</td>
      <td>15</td>
      <td>2</td>
      <td>False</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>2020-01-05 19:49:18</td>
    </tr>
    <tr>
      <th>136967</th>
      <td>antoine-le-guen</td>
      <td>en</td>
      <td>{vlog}</td>
      <td>150</td>
      <td>1</td>
      <td>8</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>False</td>
    </tr>
    <tr>
      <th>249220</th>
      <td>1upcrew</td>
      <td>en</td>
      <td>{art-culture, vlog}</td>
      <td>0</td>
      <td>1</td>
      <td>False</td>
      <td>11</td>
      <td>0</td>
      <td>1</td>
      <td>2020-06-02 11:19:38</td>
    </tr>
    <tr>
      <th>150377</th>
      <td>partager-cest-sympa</td>
      <td>fr</td>
      <td>{vlog, humour}</td>
      <td>10204</td>
      <td>1607</td>
      <td>56</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>2017-10-31 15:00:03</td>
    </tr>
  </tbody>
</table>
</div>



### Comments
You can display in a fancy way comments that a creator received


```python
creator = creators.creators[50]
for comment in creator.get_comments()[:5]: print(comment)

```

    
     [1mvictoria-9[0m
    _____________________________________
    Merci Laeticia!
    
    
     [1mteddy-11[0m
    _____________________________________
    ❤️❤️ merci pour tes vidéos et courage à toi et aux brésiliens pour ces temps difficiles
    
    
     [1mstephanie-henrionn[0m
    _____________________________________
    Merci d'avoir organisé cette collecte et surtout de monter tout en haut de Rocinha pour distribuer de quoi manger à ceux et celles qui en ont le plus besoin. Merci et bravo
    
    
     [1mcyn-3[0m
    _____________________________________
    J’envoie mon aide et tout mon amour au Brésil
    
    
     [1msarah-226[0m
    _____________________________________
    Un petit geste pour moi, qui fait la différence pour ces familles brésiliennes.... Avec beaucoup d`amour
    
    

### News 
Collect the title for all the news / projects updated by a creator 


```python
creator.get_news()
```




    ['Un cadeau un peu Spécial',
     'VIDEO SURPRISE (qui parle de poils et de mounette!)',
     'Une vidéo juste pour vous!',
     'Une Vidéos avant sa Sortie',
     'La Vidéo :)',
     'Vidéo Juste pour Vous',
     'Mille Merci!']






### Tippers 
Access to the users that donate tips to the author... 




```python
creator.get_tippers()
```




    [debris-58cd,
     romane-11,
     g111826957486368441236,
     f-florence-5a9d0c,
     sarah-110,
     f-marion-591595,
     ryalou-ros,
     shany,
     carole-amelin,
     f10153713871571985,
     claire-aline,
     flore-5b70,
     g114412240751960374835,
     steph-gr,
     tropical-piou,
     masset-3]



N.B. Only Signed users appears in the search 



### Scrape a single creator
If you want information about a specific creator you noly need to set up the **Creator class** using the username.


```python
rm = pt.Creator('roberto-mercadini')
rm.visit()  #visit the tipeee page of the creator
rm.to_dict()
```




    {'id': 268882,
     'username': 'roberto-mercadini',
     'lang': 'it',
     'tipperAmount': 0,
     'tipperNumber': '613',
     'newsNumber': '1',
     'subsciption': '2021-02-11 09:52:40',
     'categories': {'art-culture'},
     'num_comments': 129,
     'num_goals': 0,
     'num_rewards': 6}



## LICENSE
Copyright (c) 2021 Carlo Alberto Carrucciu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
