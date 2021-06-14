# options = [["option 1","option 2","option 3","option 4"],["option 5","option 6","option 7","option 8"]]

# votes = [[0,2,3,4],[1,4,2,5]]
# questions_list = ['test question 1','test question 2']

# zipped_list = zip(options, votes,questions_list)
# print(zipped_list)


# for option,vote,question in zipped_list:
#     print("the question is " + str(question))
#     for sub_option,sub_vote in zip(option,vote):
#         print(sub_option)
#         print(sub_vote)
    


# ques_ans_dict = {
#     "test question 1": {
#         "option 1": 12,
#         "option 2":13,
#         "option 3":14,
#         "option 4":15
#     },
#     "test question 2": {
#         "option 1":16,
#         "option 2":17,
#         "option 3":18,
#         "option 4":19
#     }
# }

# for question in ques_ans_dict:
#     print("QUESTION : " + question)
#     for option in ques_ans_dict[question]:
#         print(option)
#         print(ques_ans_dict[question][option])



# options = [["option 1","option 2","option 3","option 4"],["option 5","option 6","option 7","option 8"]]
# questions_list = ['test question 1', 'test question 2']
# votes = [[0, 2, 3, 4], [1, 4, 2, 5]]




# ques_ans_dict = {}
# sub_dict = {}
# for question in questions_list:
#     for op,vot in zip(options,votes):
#         for option,vote in zip(op,vot):
#             sub_dict[option] = vote
#         ques_ans_dict[question] = sub_dict
# print(ques_ans_dict)




# option_vote_list = [{"option 1":5,"option 2":6,"option 3":7,"option 4":8},{"option 5":9,"option 6":10,"option 7":11,"option 8":12}]


# for option in option_vote_list:
#     for sub_option in option:
#         print(sub_option)
#         print(ques_ans_dict[])


for question in Questions.objects.filter(room="the_room"):
    questions_list.append(question.question)
    sub_option = []
    sub_votes = []
    for option in Options.objects.filter(question=question.question):
        sub_option.append(option.option)
        sub_votes.append(option.votes)
    options_list.append(sub_option)
    votes_list.append(sub_votes)
