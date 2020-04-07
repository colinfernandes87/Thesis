from nltk.corpus import stopwords
import wordnet
import fastTextKeyword
import re

w2c = dict()
for item in model.vocab:
    w2c[item]=model.vocab[item].count

w2cSorted=dict(sorted(w2c.items(), key=lambda x: x[1],reverse=True))

stopFile = open("D:\Project\Thesis\stop_words.txt", "r")
stop_words = list(stopFile)

delete = [key for key in w2cSorted if re.search("^([@#]|(http|https):).+|^[0-9\W]*$", key) or key in stop_words or w2cSorted[key] > 550000 or w2cSorted[key] < 10]
for key in delete: del w2cSorted[key]

sims={}

# w2ccopy= w2cSorted.copy()
# keys=[key for key in w2cSorted]

count =20000
nims={}
wn_lemmas = set(wordnet.all_lemma_names())
for key in w2cSorted:
    if key in wn_lemmas:
        wn_mat=getLemmas(key)
        if len(wn_mat)!=0:
            ff_mat=neighs(key)
            nims[key]=model.n_similarity(ff_mat,wn_mat)
            count-=1
            print(key, nims[key])
            if count==0:
                break



sum(nims.values())/len(nims)

import pickle
f = open('D:\\Project\\Thesis\\vims.pkl',"wb")
pickle.dump(vims,f)
f.close()


count =20000
vims={}
wn_lemmas = set(wordnet.all_lemma_names())
for key in w2cSorted:
    if key in wn_lemmas:
        wn_mat=getLemmas(key)
        if len(wn_mat) !=0:
            ff_mat=vectors(key)
            vims[key]=model.n_similarity(ff_mat,wn_mat)
            count-=1
            print(key,vims[key])
            if count==0:
                break



count =990
bims={}
for key in w2cSorted:
    bn_mat=getBabLemmas(key)
    if len(bn_mat) !=0:
        ff_mat=vectors(key)
        bims[key]=model.n_similarity(ff_mat,bn_mat)
        count-=1
        print(key,bims[key])
        if count==0:
            break



sum(bims.values())/len(bims)

f = open('D:\\Project\\Thesis\\bims.pkl',"wb")
pickle.dump(bims,f)
f.close()


