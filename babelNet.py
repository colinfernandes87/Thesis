import requests as rq

# getSynsetIds = 'https://babelnet.io/v5/getSynsetIds'
# getSynset = 'https://babelnet.io/v5/getSynset'
# getEdgs = 'https://babelnet.io/v5/getOutgoingEdges'
getSenses= 'http://babelnet.io/v5/getSenses'

# lemma = 'apple'
lang = 'EN'
keyId  = '22fcb183-8007-44dc-bcdc-acf10ab92516'

def getBabLemmas(word):
        params = {'lemma' : word, 'searchLang' : lang, 'key'  : keyId}
        syns=rq.get(getSenses, params=params)
        syDict = syns.json()
        senses=[]
        for itm in syDict:
                prop=itm.get('properties')
                senses.append(prop['simpleLemma'])
        return list(set(senses))


if __name__=="__main__":
    print(getBabLemmas("oreo"))