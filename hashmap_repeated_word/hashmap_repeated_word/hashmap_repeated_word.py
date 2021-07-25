from .hashtable import Hashtables


def repeated_word(string):
    string = string.lower()
    hashtable = Hashtables(8192)
    array_of_the_string = string.replace(',', ' ').replace('.', ' ').split()

    for ele in array_of_the_string:
        if hashtable.contains(ele):
            return ele
        hashtable.add(ele)



if __name__ == '__main__':
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..." 
    print(repeated_word(string))