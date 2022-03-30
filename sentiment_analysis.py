

def latitude_longitude_comparison(latitude, longitude):
    if 24.660845 <= latitude <= 49.189787:
        latitude_status = True
    else:
        latitude_status = False
    if -87.518395 <= longitude <= -67.444574:
        longitude_status = "E"
    elif -101.998892 <= longitude < -87.518395:
        longitude_status = "C"
    elif -115.236428 <= longitude < -101.998892:
        longitude_status = "M"
    elif -125.242264 <= longitude < -115.236428:
        longitude_status = "P"
    else:
        longitude_status = "F"
    return latitude_status, longitude_status


def average_calculation(total, quantity):
    try:
        average_result = total / quantity
    except ZeroDivisionError:
        average_result = 0
    return average_result


def compute_tweets(tweet_file_open, keyword_file_open):
    # to determine variables
    count_for_tweet_east = 0
    count_for_tweet_central = 0
    count_for_tweet_mountain = 0
    count_for_tweet_pacific = 0
    happiness_total_east = 0
    happiness_total_central = 0
    happiness_total_mountain = 0
    happiness_total_pacific = 0
    keyword_tweet_east = 0
    keyword_tweet_central = 0
    keyword_tweet_mountain = 0
    keyword_tweet_pacific = 0
    keyword_tuple = []
    # to determine exceptions
    try:
        tweet_file = open(tweet_file_open, "r", encoding="utf-8")  # open files
        keyword_file = open(keyword_file_open, "r", encoding="utf-8")
        for keyword_line in keyword_file.readlines():
            keyword_list = keyword_line.strip().split(",")
            keyword_tuple.append(keyword_list)
        for tweet_line in tweet_file.readlines():  # read file lines using loop
            tweet_list = tweet_line.lower().strip().split(" ")  # strip and split a line into list of word, be determined by spaces
            # to make latitude into numbers
            latitude = str(tweet_list[0])
            new_latitude = ""
            for i in range(len(latitude)):
                if i == 0 or i == len(latitude)-1:
                    continue
                else:
                    new_latitude += latitude[i]
            new_latitude = float(new_latitude)
            # to make longitude into numbers
            longitude = str(tweet_list[1])
            new_longitude = ""
            for i in range(len(longitude)):
                if i == len(longitude)-1:
                    continue
                else:
                    new_longitude += longitude[i]
            new_longitude = float(new_longitude)
            # to count and determine region tweets
            location_status = latitude_longitude_comparison(new_latitude, new_longitude)
            # to determine words that people post in tweets
            sentence_word_list = tweet_list[5:]
            # to determine happiness value and keyword tweets
            if location_status[0] and location_status[1] != "F":
                if location_status[1] == "E":
                    count_for_tweet_east += 1
                    # to determine happiness value
                    for m in range(len(sentence_word_list)):  # to loop by each word in list
                        for n in range(len(keyword_tuple)):  # to loop by each keyword in list
                            if sentence_word_list[m] == keyword_tuple[n][0]:  # to check whether word matches keyword
                                happiness_total_east += int(keyword_tuple[n][1])  # if so, add up keyword value
                                keyword_tweet_east += 1  # count for keyword tweets
                elif location_status[1] == "C":
                    count_for_tweet_central += 1
                    # to determine happiness value
                    for m in range(len(sentence_word_list)):
                        for n in range(len(keyword_tuple)):
                            if sentence_word_list[m] == keyword_tuple[n][0]:
                                happiness_total_central += int(keyword_tuple[n][1])
                                keyword_tweet_central += 1
                elif location_status[1] == "M":
                    count_for_tweet_mountain += 1
                    # to determine happiness value
                    for m in range(len(sentence_word_list)):
                        for n in range(len(keyword_tuple)):
                            if sentence_word_list[m] == keyword_tuple[n][0]:
                                happiness_total_mountain += int(keyword_tuple[n][1])
                                keyword_tweet_mountain += 1
                else:
                    count_for_tweet_pacific += 1
                    for m in range(len(sentence_word_list)):
                        for n in range(len(keyword_tuple)):
                            if sentence_word_list[m] == keyword_tuple[n][0]:
                                happiness_total_pacific += int(keyword_tuple[n][1])
                                keyword_tweet_pacific += 1
        # to calculate averages
        average_east = average_calculation(happiness_total_east, keyword_tweet_east)
        average_central = average_calculation(happiness_total_central, keyword_tweet_central)
        average_mountain = average_calculation(happiness_total_mountain, keyword_tweet_mountain)
        average_pacific = average_calculation(happiness_total_pacific, keyword_tweet_pacific)
        # to make up tuples
        east_list = [average_east, keyword_tweet_east, count_for_tweet_east]
        central_list = [average_central, keyword_tweet_central, count_for_tweet_central]
        mountain_list = [average_mountain, keyword_tweet_mountain, count_for_tweet_mountain]
        pacific_list = [average_pacific, keyword_tweet_pacific, count_for_tweet_pacific]
        result_tuple = [east_list, central_list, mountain_list, pacific_list]
        return result_tuple
    except IOError:
        empty_list = []
        return empty_list
