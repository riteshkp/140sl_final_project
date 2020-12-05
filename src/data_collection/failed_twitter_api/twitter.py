import twint
import datetime
import pandas

since_date = datetime.datetime(2019, 8, 11)
stock = "Intel"
until_date = datetime.datetime(2019, 8, 12)

def jobone():
	print ("Fetching Tweets")
	c = twint.Config()
	# choose search term (optional)
	c.Search = "#intel"
	# choose beginning time (narrow results)
	c.Since = "2020-12-04"
	# set limit on total tweets
	c.Limit = 10
	# no idea, but makes the csv format properly
	c.Store_csv = False
	c.Hide_output = False
	# choose beginning time (narrow results)
	c.Pandas_clean = True
	# set limit on total tweets
	c.Pandas = True
	# no idea, but makes the csv format properly
	c.Store_csv = False
	# format of the csv
	c.Custom = ["date", "time", "tweet", "likes_count", "hashtags"]
	# change the name of the csv file
	c.Output = "filename2.csv"
	twint.run.Search(c)

if __name__ == '__main__':
    jobone()
	# print ("Fetching Tweets")
	# c = twint.Config()
    # c.Hide_output=False
    # c.Pandas_clean = True
    # c.Pandas=True
	# # choose search term (optional)
	# c.Search = "#intel"
	# # choose beginning time (narrow results)
	# c.Since = "2020-12-04"
	# # set limit on total tweets
	# c.Limit = 10
	# # no idea, but makes the csv format properly
	# c.Store_csv = False
	# # format of the csv
	# #c.Custom = ["date", "time", "username", "tweet", "link", "likes", "retweets", "replies", "mentions", "hashtags"]
	# # change the name of the csv file
	# c.Output = "filename.csv"
	# twint.run.Search(c)
