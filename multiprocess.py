import numpy as np 
from gensim.models import fasttext as ft
from nltk.corpus import wordnet

def getLemmas(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemma_names():
            synonyms.append(l)
    return list(set(synonyms))


#get set of words
mwords = lambda nn : [word for word, sim in nn]

#Twitter File
binFile = r"D:\Project\Thesis\tranined models\fasttext_twitter_raw_100.bin"

#load into gensim Model
model = ft.load_facebook_vectors(binFile)

w2c = dict()
for item in model.vocab:
    w2c[item]=model.vocab[item].count

w2cSorted=dict(sorted(w2c.items(), key=lambda x: x[1],reverse=True))

stopFile = open("D:\Project\Thesis\stop_words.txt", "r")
stop_words = list(stopFile)

#delete words that are not so common
delete = [key for key in w2cSorted if key.startswith('#') or key.startswith('@') or key in stop_words or w2cSorted[key] > 550000 ]
for key in delete: del w2cSorted[key]

sims={}

def neighs(qry, pos=None, neg=None):
    nnQry= model.most_similar(qry)
    nQry = model[mwords(nnQry)].mean(0)  
    if pos is None:
        pos = []
    if neg is None:
        neg = []
    nPos= np.zeros(nQry.shape[0])
    for itm in pos:
        nnPos= model.most_similar(itm)
        nPos = nPos + model[mwords(nnPos)].mean(0)
    nNeg = np.zeros(nQry.shape[0])
    for itm in neg:
        nnNeg= model.most_similar(itm)
        nNeg = nNeg + model[mwords(nnNeg)].mean(0)
    fKeyWds=iter(10,nQry,nPos,nNeg)
    return fKeyWds



#iterate for more keywords
def iter(n,nQry, nPos, nNeg):
    fKeyWds=[]
    nQry=nQry + nPos - nNeg
    for i in range(n):                
        keyWds=model.similar_by_vector(nQry)
        fKeyWds = list(set(fKeyWds + mwords(keyWds)))
        nQry=model[fKeyWds].mean(0)
    return fKeyWds



#similarity for 1000 words in the vocab
count =1000
wn_lemmas = set(wordnet.all_lemma_names())
for key in w2cSorted:
    if key in wn_lemmas:
        ff_mat=neighs(key)
        wn_mat=getLemmas(key)
        if set(wn_mat).issubset(w2cSorted) and len(wn_mat)!=0:
            sims[key]=model.n_similarity(ff_mat,wn_mat)
            count-=1
            print(key)
        if count ==0:
            break

        
print(sum(sims.values())/len(sims))