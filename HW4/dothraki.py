import urllib.request
import re
import matplotlib.pyplot as plt

def file_analyzer(link, user_agent):
    req = urllib.request.Request(url, headers={'User-Agent':user_agent})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    return html

def pos_analyzer (file):
    reg_tag = re.compile('<dl><dd><i>[a-z]*?.</i>')
    # число слов каждой части речи = число употреблений каждой глоссы
    text = reg_tag.findall(words)
    reg_gloss = re.compile('>[a-z]+.<')
    dict_gloss = {}
    for item in text:
        if reg_gloss.search(item) is not None:
            index = reg_gloss.search(item).group()
            index = index[1:len(index) - 1]
            if dict_gloss.get(index) is not None:
                dict_gloss[index] += 1
            else:
                dict_gloss[index] = 1
    return dict_gloss

def first_letter (text):
    voc = list()
    fl = {}
    reg_lex = re.compile('<ul><li><b>[a-z]*</b>')
    words = reg_lex.findall(text)
    reg_html = re.compile('<[/]?[a-z]*>')
    for word in words:
        voc.append(reg_html.sub('', word))
    for item in voc:
        if fl.get(item[0]) is not None:
            fl[item[0]] += 1
        else:
            fl[item[0]] = 1
    return fl

def painting(variables, title):
    y = list(variables.values())
    x = [i + 5 for i in range(len(y))]
    labels = list(variables.keys())
    plt.title(title)
    plt.plot(x, y, 'ro')
    plt.xticks(x, labels, rotation='vertical')
    plt.margins(0.2)
    plt.subplots_adjust(bottom=0.15)
    plt.show()
    
def main():
    link = 'http://wiki.dothraki.org/Vocabulary'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    doc = file_analyzer(link, user_agent)
    pos = pos_analyzer(doc)
    abc = first_letter(doc)
    painting(pos, 'Число слов каждой части речи в словаре')
    painting(abc, 'Число слов в словаре, начинающихся на каждую букву')

if __name__ == '__main__':
    main()
