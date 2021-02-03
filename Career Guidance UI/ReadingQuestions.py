import pandas
import numpy as np
travel_df = pandas.read_excel('Questions.xlsx')
content = travel_df.to_dict()
questcareerlist=list(content['Career'].values())
questionlist=list(content['Questions'].values())
optionAlist=list(content['OptionA'].values())
optionBlist=list(content['OptionB'].values())
optionClist=list(content['OptionC'].values())
optionDlist=list(content['OptionD'].values())
currect_ans_list=list(content['Correct Ans'].values())
avbl_careers=np.unique(np.array(questcareerlist))
career_scores=[0]*len(avbl_careers)
print(avbl_careers)
print(career_scores)
res={avbl_careers[i]: career_scores[i] for i in range(len(avbl_careers))}
print(res)
#print(questionlist)
#print(optionAlist)
#print(optionBlist)
#print(optionClist)
#print(optionDlist)
#print(currect_ans_list)
score=0
for i in range(0,len(questionlist)):
    print(questcareerlist[i])
    print(questionlist[i])
    print('A',optionAlist[i])
    print('B',optionBlist[i])
    print('C',optionClist[i])
    print('D',optionDlist[i])
    
    ans=input("Enter Correct Answer(A B C D):")
    if ans==currect_ans_list[i]:
        print("correct ans")
        res[questcareerlist[i]]=res[questcareerlist[i]]+1
    else:
        print("Wrong ans")
    
print(res)