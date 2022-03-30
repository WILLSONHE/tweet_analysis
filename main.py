# Name: Yuanhe Zhao
# Student number:
# Assignment 3: Sentiment Analysis


import sentiment_analysis


def main():
    keyword_file_input = str(input("Please enter file name of keywords: "))
    tweets_file_input = str(input("please enter file name of tweets: "))
    result = sentiment_analysis.compute_tweets(tweets_file_input, keyword_file_input)
    if result:
        print("Average happiness of Eastern region is %.4f." % result[0][0])
        print("Average happiness of Central region is %.4f." % result[1][0])
        print("Average happiness of Mountain region is %.4f." % result[2][0])
        print("Average happiness of Pacific region is %.4f." % result[3][0])
        print("In order to calculate average happiness value, data are based from:")
        print("Tweets from Eastern region with keyword at %d." % result[0][1])
        print("There are %d tweets in total from Eastern region to be analyzed." % result[0][2])
        print("Tweets from Central region with keyword at %d." % result[1][1])
        print("There are %d tweets in total from Central region to be analyzed." % result[1][2])
        print("Tweets from Mountain region with keyword at %d." % result[2][1])
        print("There are %d tweets in total from Mountain region to be analyzed." % result[2][2])
        print("Tweets from Pacific region with keyword at %d." % result[3][1])
        print("There are %d tweets in total from Pacific region to be analyzed." % result[3][2])
    else:
        print("File does not exist or is not found.")


if __name__ == '__main__':
    main()
