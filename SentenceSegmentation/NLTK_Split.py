import codecs
from nltk.tokenize import sent_tokenize

storypath = 'SentenceSegmentation/story/'+'theGOLDENBIRD.txt'


def sentence_token_nltk(str):
    sent_tokenize_list = sent_tokenize(str)
    return  sent_tokenize_list

def sentence_split(str_centence):
    list_ret = list()
    for s_str in str_centence.split('.'):
        if '?' in s_str:
            list_ret.extend(s_str.split('?'))
        elif '!' in s_str:
            list_ret.extend(s_str.split('!'))
        else:
            list_ret.append(s_str)
    return list_ret

def main():
    with codecs.open(storypath, 'r', encoding='utf-8') as fp:
        str = fp.read().strip()

    sentence_str = sentence_token_nltk(str) #sent_tokenize
    sentence_str_2 = sentence_split(str) # ? ! .
    for i in sentence_str:
        print(i,end='\n\n')


if __name__ == '__main__':
    main()