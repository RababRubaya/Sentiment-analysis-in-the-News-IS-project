#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from newspaper import Article
import json
import pandas as pd
from pprint import pprint
import pdb

path_txt_categories = 'C:/new_laptop/Intelligent_Systems/final project/outputs/category.txt'

path_txt_headlines = 'C:/new_laptop/Intelligent_Systems/final project/outputs/headline.txt'

path_txt_contents = 'C:/new_laptop/Intelligent_Systems/final project/outputs/url_content.txt'

news_categories = open(path_txt_categories,'w', encoding="utf-8")

news_headlines = open(path_txt_headlines,'w', encoding="utf-8")

news_contents = open(path_txt_contents,'w', encoding="utf-8")

len = 1000
json_popos = pd.read_json('C:/new_laptop/Intelligent_Systems/final project/inputs/News_Category_Dataset_v2.json', lines=True) 
json_popos = (json_popos).iloc[:,[1,3,4]];

json_popos_Pos = json_popos.loc[json_popos['category'] == 'POLITICS'].sample(n = len);
json_popos_Ned = json_popos.loc[json_popos['category'] != 'POLITICS'].sample(n = len);
all_req_dataframs = pd.concat([json_popos_Pos, json_popos_Ned], axis=0, join='inner')
#pdb.set_trace()
print(all_req_dataframs)

loop_variable = 0  
exception_variable = 0

for index, row in all_req_dataframs.iterrows(): 
    #print (index, row[2])
    loop_variable = loop_variable + 1
    print("loop_variable:" + str(loop_variable) )
    try:
        article = Article(row[2])
        article.download()
        article.html
        article.parse()
        content_of_article = (article.text).replace("\n","")
        news_contents.write(content_of_article)
        news_contents.write("\n" + "\n")
        print(content_of_article)
        print("\n" + "\n")
    except:
        print("\n" + "----oops--------------Connection refused by the server..")
        print (row[2])
        exception_variable = exception_variable + 1
        continue
# now we will write categories        
    news_categories.write(row[0])
    news_categories.write("\n" + "\n")
# now we will write headlines
    news_headlines.write(row[1])
    news_headlines.write("\n" + "\n")
    
    print("loop working-----------------------------------------------------")
    
news_contents.close()
news_categories.close()
news_headlines.close()
print(str(exception_variable)+"--------end--------")


