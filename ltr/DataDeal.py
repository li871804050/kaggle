# encoding=utf-8
import pandas as pd
from ltr.SolrDeal import *
import fasttext

if __name__ == '__main__':
    org_data = pd.read_csv('data/jm.csv')

    #获取查询关键字
    keywords = org_data['rel_keyword'].drop_duplicates()
    for keyword in keywords:
        print(keyword)
        rel_keyword = org_data[(org_data.rel_keyword == keyword)]
        solrData = getSolrData(keyword)
        # print(rel_keyword.iloc[2])
        if len(solrData) > 0:
            for i in range(len(rel_keyword)):
                pid = rel_keyword.iloc[i]['products_id']
                if pid in solrData['products_id']:
                    s_data = solrData[(solrData.products_id == pid)]
                    rel_keyword.iloc[i]['text_soce'] = s_data['score']
                    rel_keyword.iloc[i]['products_price'] = s_data['products_price']
                    print(rel_keyword[i])
                    break
