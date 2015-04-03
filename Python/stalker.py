import requests
from bs4 import BeautifulSoup


def get_topics():
    ''' (None) -> Array[Str]

    Gets all topics from the first page of SoftUni's forum and
    return array of their topic names and data of the last post.

    '''
    url = 'https://softuni.bg/forum/questions/index/0/10'
    # Test for unanswered questions
    # url = 'https://softuni.bg/Forum/Questions/Unanswered'
    data = []
    try:
        htmlText = requests.get(url).text
    except:
        print(url  + 'can\'t be processed')
    # print(htmlText)
    soup = BeautifulSoup(htmlText)
    allQuestions = soup.find('div', id='forum-questions')
    for question in allQuestions.findAll('div', class_='box-forum'):
        header = question.find('h3').find('a').text
        try:
            date = question.find('span', class_='post-details').text
        except:
            # Post without answer
            date = 'new'
        data.append(header + " " + date)
    return data

# data = get_topics()
# data = ['За обучителната система  - въпроси/предложения/бъгове 02/04/2015 03:30:10', '[Team Building] Следизпитно парти - 05.04 - Желаещи? 01/04/2015 12:20:47', '[Team Building] Танго - безплатен урок - 7ми април 30/03/2015 12:34:51', '[Homework] Digital Marketing & SEO - “Подготовка към проекта” 03/04/2015 15:32:05', 'Места, на които трябва да седим по време на изпита 03/04/2015 15:06:12', '[Homework] Programming Basics - Math for developers - Problem {3} 03/04/2015 14:57:55', '[Technical Issue] Prodvigator.bg 03/04/2015 13:08:16', '[Technical Issue] Системата за определяне на място на изпита 03/04/2015 12:50:52', '[Useful Info] SEO - за начинаещи (книга) - На Български! 03/04/2015 12:13:39', 'Мога ли да ползвам WordPress website за целите на курсов проект? 03/04/2015 11:43:18', 'Нощувка в София 03/04/2015 06:14:16', 'Какво следва след приемния изпит? 03/04/2015 04:44:51', '[Technical Issue] Visual Studio - Преместване 03/04/2015 01:47:58']
# print(data)