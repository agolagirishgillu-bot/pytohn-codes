def m_w(words):
    ctr=0
    list=[]

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr+=1
            list.append(words)

    print('word macht')
    return ctr

l=['101','202','303']
a=m_w(l)
print(a)