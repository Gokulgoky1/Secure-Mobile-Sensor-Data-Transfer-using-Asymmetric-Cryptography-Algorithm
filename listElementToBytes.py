import pickle
def ListElementToBytes(list1):
    for i in range(len(list1)):
        k=pickle.dumps(list1[i])
        list1[i]=k
    return list1
def BytesToListElement(list1):
    for i in range(len(list1)):
        k=pickle.loads(list1[i])
        list1[i]=k
    return list1