from babelnetpy.babelnet import BabelNet

def getLemmasbab(word):
    bn = BabelNet("22fcb183-8007-44dc-bcdc-acf10ab92516") # or BabelNet(open("key.txt", "r").read())
    Ids = bn.getSynset_Ids(word, "en")
    lemma=[]
    for itm in Ids:
        synsets = bn.getSynsets(itm.id)
        #print(synsets)
        lemma.extend([j.properties.simpleLemma for i in synsets for j in i.senses])
    return list(set(lemma))

if __name__=="__main__":
    print(getLemmasbab("rip"))
