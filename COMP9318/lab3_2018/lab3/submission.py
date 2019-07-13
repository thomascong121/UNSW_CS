## import modules here 
################# Question 1 #################
def multinomial_nb(training_data, sms):# do not change the heading of the function
    spam_list = {}
    spam_amount= 0
    ham_list = {}
    ham_amount = 0
    spam_num = 0
    ham_num = 0              
    for x in training_data:
        if x[1] == 'ham':
            ham_num = ham_num + 1
            for y in x[0]:
                if y not in ham_list:
                    ham_list[y]=x[0][y]
                else:
                    ham_list[y] = ham_list[y] + x[0][y]
                ham_amount = ham_amount + x[0][y]
        elif x[1] == 'spam':
             spam_num = spam_num + 1
             for y in x[0]:
                if y not in spam_list:
                    spam_list[y]=x[0][y]
                else:
                    spam_list[y] = spam_list[y] + x[0][y]
                spam_amount = spam_amount + x[0][y]
    p_spam = spam_num/(spam_num + ham_num)
    p_ham = ham_num/(spam_num + ham_num)
    total_list = dict(ham_list,**spam_list)
    smooth = len(total_list)
    for word in sms:
        if word in total_list:
            if word in spam_list:
                p_spam = p_spam*((spam_list[word]+1)/(spam_amount+smooth))
            else:
                p_spam = p_spam*(1/(spam_amount+smooth))
            if word in ham_list:
                p_ham = p_ham*((ham_list[word]+1)/(ham_amount+smooth))
            else:
                p_ham = p_ham*(1/(ham_amount+smooth))
    ratio =  p_spam/p_ham
    return ratio
    
     # **replace** this line with your code