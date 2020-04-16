import numpy as np 

from gensim.models import KeyedVectors as kv 

#lambda for extracting words out of list
mwords = lambda nn : [word for word, sim in nn]

#Wikipedia File
#vecFile = r"D:\Project\Thesis\tranined models\enwiki.skip.size300.win10.neg15.sample1e-5.min15.txt"
vecFile = r"D:\Project\Thesis\tranined models\raw-legal\NNP replaced\legalrawtextreplacewithnnp.bin"
#load into gensim Model
model = kv.load_word2vec_format(vecFile, binary=False)

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

#Model 1
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
    print(neighs("valentine's" ))















# def neighs(qry, pos=[None], neg=[None]):
#     #using neighbours('apple')-neighbours('macintosh')+neighours('fruit')
#     nnQry= model.most_similar(qry)
#     nQry = model[mwords(nnQry)].mean(0)

#     nPos = nQry
#     nPos.fill(0)
#     for itm in pos:
#         nnPos= model.most_similar(itm)
#         nPos = nPos + model[mwords(nnPos)].mean(0)

#     nNeg=nQry
#     nNeg.fill(0)
#     for itm in neg:
#         nnNeg= model.most_similar(itm)
#         nNeg = nNeg + model[mwords(nnNeg)].mean(0)

#     #wrdMat = nQry + nPos - nNeg
#     fKeyWds=iter(10,nQry,nPos,nNeg)
#     return print(fKeyWds)

# #iterate for more keywords
# def iter(n,nQry, nPos, nNeg):
#     fKeyWds=[]
#     nQry=nQry + nPos - nNeg
#     for i in range(n):
#         keyWds=model.similar_by_vector(nQry)
#         fKeyWds = list(set(fKeyWds + mwords(keyWds)))
#         nQry=model[fKeyWds].mean(0)
#     return fKeyWds


# # def neighs(qry, pos, neg):
# #     #using neighbours('apple')-neighbours('macintosh')+neighours('fruit')
# #     nnQry=model.most_similar(qry)
# #     nnPos=model.most_similar(pos)
# #     nnNeg=model.most_similar(neg)

# #     #matix of vectors
# #     nQry = model[mwords(nnQry)].mean(0)
# #     nPos = model[mwords(nnPos)].mean(0)
# #     nNeg = model[mwords(nnNeg)].mean(0)

# #     #wrdMat = nQry + nPos - nNeg
# #     fKeyWds=iter(10,nQry,nPos,nNeg)
# #     return print(fKeyWds)


# neighs('apple', pos=['fruits'], neg=['macintosh'])
# neighs('apple', pos=['macintosh'], neg=['fruits'])

