#***************************************************
# Name: Sonam mehra
# Student Number: A00213174
#
#ANA1001 LAB 11
#***************************************************




import urllib.request
import json
import nasdaqdatalink
import matplotlib.pyplot as plt


# url = f'https://data.nasdaq.com/api/v3/datasets/WIKI/FB/data.json?api_key==4p6BzezQxmLisD1qzVzb'

# response = urllib.request.urlopen(url)
# result = json.loads(response.read())

# #empty list to append values from the result
# dates, high,low = [], [], []


# #appending values
# for value in result['dataset']['data']:

#   dates.append(value[0])
#   high.append(value[2])
#   low.append(value[3])

# #prints high low
# print("High and low for for Last five days")
# print(f"On {dates[0]} the high was {high[0]} and low was {low[0]}")
# print(f"On {dates[1]} the high was {high[1]} and low was {low[1]}")
# print(f"On {dates[2]} the high was {high[2]} and low was {low[2]}")
# print(f"On {dates[3]} the high was {high[3]} and low was {low[3]}")
# print(f"On {dates[4]} the high was {high[4]} and low was {low[4]}")

# #plot for last five days 
# plt.plot(dates[0:5],high[0:5])
# #chart labels
# plt.xlabel('Dates')
# plt.ylabel('High')
# plt.title('High for five days')
# plt.grid(True)
# plt.savefig("stock_price_high.png")
# print("Done")


# #plot for last five days 
# plt.plot(dates[0:5],low[0:5])
# #chart labels
# plt.xlabel('Dates')
# plt.ylabel('Low')
# plt.title('Low for five days')
# plt.grid(True)
# plt.savefig("stock_price_low.png")
# print("Done")




