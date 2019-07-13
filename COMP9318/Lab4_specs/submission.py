## import modules here 

################# Question 1 #################
def merge_two(x,y):
    if(x == {}):
        return y
    if(y == {}):
        return x
    l = list(x.keys())+list(y.keys())
    z={}
    for i in l:
        if(i in y and i in x):
            z[i] = x[i]+y[i]
        elif(i in x):
            z[i] = x[i]
        else:
            z[i] = y[i]
    return z

def multinomial_nb(training_data,sms):
    #calculate class probability
    Pham=0
    Pspam=0
    hamList=[]
    spamList=[]
    for i in training_data:
        if(list(i)[1]=='ham'):
            Pham+=1
            hamList.append(list(i)[0])
        else:
            spamList.append(list(i)[0])
            Pspam+=1
    Pham = Pham/(len(training_data))
    Pspam = Pspam/(len(training_data))
    
    ###Probability of each word per class
    result_ham = {}
    result_spam = {}
    #when ham show all words
    for d_1 in hamList:
        result_ham = merge_two(result_ham,d_1)
    #when spam show all words
    for d_2 in spamList:
        result_spam = merge_two(result_spam,d_2)
    #number of  words ham class
    s_ham = sum(result_ham.values())
    #number of  words spam class
    s_spam = sum(result_spam.values())
    #occuency of each word
    result_total = result_ham.copy()
    result_total.update(result_spam)

    total_words = len(result_total)
    #calculate the Probability of each word in spam/ham class
    #ham:
    Prob_word_ham={}
    for word in result_total:
        if(word in result_ham):
            Prob_word_ham[word] = (result_ham[word]+1)/(s_ham+total_words)
        else:
            Prob_word_ham[word] = 1/(s_ham+total_words)
    #spam:
    Prob_word_spam={}
    for word in result_total:
        if(word in result_spam):
            Prob_word_spam[word] = (result_spam[word]+1)/(s_spam+total_words)
        else:
            Prob_word_spam[word] = 1/(s_spam+total_words)     
    #prediction
    #spam probability
    product = 1
    for word in sms:
        if(word in Prob_word_spam):
            product = product*Prob_word_spam[word]
    spam_pro = Pspam*product
    product = 1
    #ham probability
    for word in sms:
        if(word in Prob_word_ham):
            product = product*Prob_word_ham[word]
    ham_pro = Pham*product    
    return spam_pro/ham_pro



    