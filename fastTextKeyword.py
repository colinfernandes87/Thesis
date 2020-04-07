import numpy as np 
from gensim.models import fasttext as ft

#lambda for extracting words out of list
mwords = lambda nn : [word for word, sim in nn]

#Twitter File
binFile = r"D:\Project\Thesis\tranined models\fasttext_twitter_raw_100.bin"

#load into gensim Model
model = ft.load_facebook_vectors(binFile)

#using positive/Negative most_similar
#model.wv.most_similar(positive=['apple','fruit'], negative=['macintosh'])

def neighs(qry, pos=None, neg=None):
    nnQry= model.most_similar(qry)
    nQry = model[mwords(nnQry)].sum(0)  
    if pos is None:
        pos = []
    if neg is None:
        neg = []
    nPos= np.zeros(nQry.shape[0])
    for itm in pos:
        nnPos= model.most_similar(itm)
        nPos = nPos + model[mwords(nnPos)].sum(0)
    nNeg = np.zeros(nQry.shape[0])
    for itm in neg:
        nnNeg= model.most_similar(itm)
        nNeg = nNeg + model[mwords(nnNeg)].sum(0)
    fKeyWds=iter(10,nQry,nPos,nNeg)
    return fKeyWds


def vectors(qry, pos=None, neg=None):
    vecQry= model[qry] 
    if pos is None:
        pos = []
        vecPos= np.zeros(vecQry.shape[0])
    else:
        vecPos=model[pos].sum(0)
    if neg is None:
        neg = []
        vecNeg = np.zeros(vecQry.shape[0])
    else:
        vecNeg=model[neg].sum(0)    
    fKeyWds=epoc(10,vecQry,vecPos,vecNeg)
    return fKeyWds

def epoc(n,vecQry,vecPos,vecNeg):
    fKeyWds=[]
    vecQry=vecQry+vecPos-vecNeg
    for i in range(n):                
        keyWds=model.similar_by_vector(vecQry)
        fKeyWds = list(set(fKeyWds + mwords(keyWds)))
        vecQry=model[fKeyWds].sum(0)
    return fKeyWds


#iterate for more keywords
def iter(n,nQry, nPos, nNeg):
    fKeyWds=[]
    nQry=nQry + nPos - nNeg
    for i in range(n):                
        keyWds=model.similar_by_vector(nQry)
        fKeyWds = list(set(fKeyWds + mwords(keyWds)))
        nQry=model[fKeyWds].sum(0)
    return fKeyWds

if __name__=="__main__":
    print(neighs('computer', pos=['laptop']))


# neighs('server', pos=['computer'], neg=['waiter'])
# neighs('apple', pos=['macintosh'], neg=['fruits'])
# #neighs('apple')
#print(neighs('computer', pos=['laptop']))