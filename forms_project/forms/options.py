from bs4 import BeautifulSoup
import requests


def get_options(url):
    URL = url
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all(
        class_="freebirdFormviewerComponentsQuestionRadioChoice freebirdFormviewerComponentsQuestionRadioOptionContainer")
    #each_question_op = int(input("please add the number of options each question has: "))
    # print(results)
    each_question_op = 4

    all_option_list = []
    for option in results:
        all_option_list.append(option.text)
    # print(all_option_list)
    # print("the length of the option list is " + str(len(all_option_list)))
    return all_option_list
