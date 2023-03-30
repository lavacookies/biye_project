import codecs
from nltk.tokenize import sent_tokenize
import argparse

import csv

# storypath = 'SentenceSegmentation/story/'+'Cinderella.txt'


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


def main(storypath):
    storypath = "./story/"+storypath+".txt"

    with codecs.open(storypath, 'r', encoding='utf-8') as fp:
        str = fp.read().strip()

    sentence_str = sentence_token_nltk(str) #sent_tokenize
    sentence_str_2 = sentence_split(str) # ? ! .
    
    with open('output.csv', 'w', newline='', encoding='big5') as csvfile:
        writer = csv.writer(csvfile)

        for i in sentence_str:
            print(i,end='\n\n')
            writer.writerow([i])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--story', type=str, default='theGoodBargain', help='the story to split')

    config = parser.parse_args()
    
    print(config)
    if config.story is None:
        raise RuntimeError("Please enter the the story path which want to split.")
    
    main(config.story)

# python NLTK_Split.py --story ./story/LittleRedRidingHood.txt