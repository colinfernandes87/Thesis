from nltk.corpus import wordnet

def getLemmas(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemma_names():
            synonyms.append(l)
        for h in syn.hyponyms():
            for l in h.lemma_names():
                synonyms.append(l)
    return list(set(synonyms))

        
#remove duplicates
def remove_dups(arr):
    n=len(arr)
    narr=[]
    mp={i:0 for i in arr}
    for i in range(n):
        if mp[arr[i]]==0:
            narr.append(arr[i])
        mp[arr[i]]+=1
    return narr

if __name__=="__main__":
    print(getLemmas("oreo"))




# from collections import Counter

# res = Counter(votes.values())


# import matplotlib.pyplot as plt
# import seaborn as sns

# plt.hist(res['arr_delay'], color = 'blue', edgecolor = 'black')

