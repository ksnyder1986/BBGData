# BBGData
Data from BoardGameGeek.com and Python code for retrieval of that data.

This contains code that has been modified from the repository https://github.com/ThaWeatherman/scrapers/tree/master/boardgamegeek
The code in that repository no longer works as coded (or at least did not for me)

In this repository there are two primary python programs for retrieving the data from the website.

Collect_Game_Ids.py is ran against the boardgamegeek.com search page. It will go through each page of the list of board games and retrieve the board game Ids. At the time of this run there were 1099 pages of games. Note that line 15 should be modified to go through the entire list of pages. This will output into a ids.csv a file that contains just the Ids of the games. Note that as written this code will pull down two entries for each game (the href containing the game's id shows up twice per game. Once in the thumbnail and once in the link). 

This file must be deduplicated. I lazily did it using excel, but I am sure a quick code could have been whipped up :-). This was left up to the reader.

The second program get_game_info.py will take the list of game ids and go to each game's page to scrap information. Note that as of this writing there were nearly 110k games in the database. This scraper takes 5 seconds per game to keep from blocked by BBG. Therefore it takes roughly 55 hours of runtime to get data for all 110k games.

There are two other programs that are works in progress in here.
Usertest.py is an attempt to scrape a list of usernames from the reviews left on other games. I am not a skilled html parser so this needs work. The concept is that it will go to the most reviewed games on the website (Catan, Carcassone, etc.) and go through the list of reviews to get the usernames of all the reviews. Then it will deduplicate those usernames and take a sample of them to run through the next code.

Get_user_info.py retrievews the BBG API for each user to get that users collection data. The idea being that if I can get a subset of user collection data and run it against the data on the games I might be able to build a algorithm that can predict which games certain types of players may enjoy. Obvious relationships might be combinations of certain mechanics and themes. Certain play times and player counts. Etc.
