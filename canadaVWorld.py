import csv
import matplotlib.pyplot as plt
import numpy as np

# arrays

canada = []
usa = []
worldNoU = []
line = '--------------------------------------------------------'
# need a place to put clean data set (categories)
# puts headers here
categories = []

with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1

        elif row[4] == 'CAN':
            # putting an array in an array
            canada.append([int(row[0]), row[5], row[6], row[7]])
        elif row[4] == 'USA':
            usa.append([int(row[0]), row[5], row[6], row[7]])
        else:
            worldNoU.append([int(row[0]), row[5], row[6], row[7]])
        line_count += 1

print(line)
print('total medals for Canada:', len(canada))
print('total medals for USA:', len(usa))
print('total medals for the rest:', len(worldNoU + usa))

print(line)
print(canada[0])  # processing first header title
print('processed', line_count, 'rows of data')

# gold medals per year
gold_1924 = []
gold_1948 = []
gold_1972 = []
gold_2002 = []
gold_2014 = []
# silver medals per year
silver_1924 = []
silver_1948 = []
silver_1972 = []
silver_2002 = []
silver_2014 = []
# bronze medals per year
bronze_1924 = []
bronze_1948 = []
bronze_1972 = []
bronze_2002 = []
bronze_2014 = []


# medal = placeholder, can call it anything
# can replace with row

for medal in canada:
    if medal[0] == 1924 and medal[3] == 'Gold':
        gold_1924.append(medal)
    elif medal[0] == 1948 and medal[3] == 'Gold':
        gold_1948.append(medal)
    elif medal[0] == 1972 and medal[3] == 'Gold':
        gold_1972.append(medal)
    elif medal[0] == 2002 and medal[3] == 'Gold':
        gold_2002.append(medal)
    elif medal[0] == 2014 and medal[3] == 'Gold':
        gold_2014.append(medal)

    elif medal[0] == 1924 and medal[3] == 'Silver':
        silver_1924.append(medal)
    elif medal[0] == 1948 and medal[3] == 'Silver':
        silver_1948.append(medal)
    elif medal[0] == 1972 and medal[3] == 'Silver':
        silver_1972.append(medal)
    elif medal[0] == 2002 and medal[3] == 'Silver':
        silver_2002.append(medal)
    elif medal[0] == 2014 and medal[3] == 'Silver':
        silver_2014.append(medal)

    elif medal[0] == 1924 and medal[3] == 'Bronze':
        bronze_1924.append(medal)
    elif medal[0] == 1948 and medal[3] == 'Bronze':
        bronze_1948.append(medal)
    elif medal[0] == 1972 and medal[3] == 'Bronze':
        bronze_1972.append(medal)
    elif medal[0] == 2002 and medal[3] == 'Bronze':
        bronze_2002.append(medal)
    elif medal[0] == 2014 and medal[3] == 'Bronze':
        bronze_2014.append(medal)

print('Canada won', len(gold_1924), 'gold medals in 1924')
print('Canada won', len(gold_2014), 'gold medals in 2014')

print('Canada won', len(silver_1924), 'silver medals in 1924')
print('Canada won', len(silver_2014), 'silver medals in 2014')

print('Canada won', len(bronze_1924), 'bronze medals in 1924')
print('Canada won', len(bronze_2014), 'bronze medals in 2014')

# bar graph - number of medals total per year
# bar graph - 2014 number of gold, bronze, silver medals

men = (192, 128, 66)
women = (123, 75, 41)

ind = np.arange(len(men))  # the x locations for the groups
width = 0.35  # width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, men, width,
                color='#228B22', label='Men')
rects2 = ax.bar(ind + width/2, women, width,
                color='#4b0082', label='Women')


ax.set_ylabel('# Medals Won')
ax.set_title('Types of Medals Won Between Men and Women')
ax.set_xticks(ind)
ax.set_xticklabels(('Gold', 'Silver', 'Bronze'))
ax.legend()


def autolabel(rects, xpos='center'):
    xpos = xpos.lower()
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()

# filtering Canada 2014 gold medals by gender

gold_2014_men = []
gold_2014_women = []

print(line)
print('pushing data into gender in Canada Gold Medals 2014 array')

for gender in gold_2014:
    if gender[1] == 'Men' and gender[3] == 'Gold':
        gold_2014_men.append(gender)
    if gender[1] == 'Women' and gender[3] == 'Gold':
        gold_2014_women.append(gender)

print('Class challenge:')
print('Male athletes in Canada won', len(gold_2014_men), 'gold medals in 2014')
print('Female athletes in Canada won', len(gold_2014_women), 'gold medals in 2014')

gold_men = []
gold_women = []
silver_men = []
silver_women = []
bronze_men = []
bronze_women = []

# in array (i.e. medal[]), count over from parent array from 0
# i.e. Canada column = 0 --> 4 rows = medals

print(line)
print('pushing data to gender in canada array:')

for gender in canada:
    if gender[1] == 'Men' and gender[3] == 'Gold':
        gold_men.append(gender)
    elif gender[1] == 'Men' and gender[3] == 'Silver':
        silver_men.append(gender)
    elif gender[1] == 'Men' and gender[3] == 'Bronze':
        bronze_men.append(gender)

    elif gender[1] == 'Women' and gender[3] == 'Gold':
        gold_women.append(gender)
    elif gender[1] == 'Women' and gender[3] == 'Silver':
        silver_women.append(gender)
    elif gender[1] == 'Women' and gender[3] == 'Bronze':
        bronze_women.append(gender)

print('processed', line_count, 'rows of data')

print('Male athletes in Canada won', len(gold_men), 'gold medals')
print('Female athletes in Canada won', len(gold_women), 'gold medals')

print('Male athletes in Canada won', len(silver_men), 'silver medals')
print('Female athletes in Canada won', len(silver_women), 'silver medals')

print('Male athletes in Canada won', len(bronze_men), 'bronze medals')
print('Female athletes in Canada won', len(bronze_women), 'bronze medals')

# bar graph men gold, silver, bronze vs women gold, silver, bronze
# percentages of medals per men in canada, medals per women in canada

men = (192, 128, 66)
women = (123, 75, 41)

ind = np.arange(len(men))  # the x locations for the groups
width = 0.35  # width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, men, width,
                color='#228B22', label='Men')
rects2 = ax.bar(ind + width/2, women, width,
                color='#4b0082', label='Women')


ax.set_ylabel('# Medals Won')
ax.set_title('Types of Medals Won Between Men and Women')
ax.set_xticks(ind)
ax.set_xticklabels(('Gold', 'Silver', 'Bronze'))
ax.legend()


def autolabel(rects, xpos='center'):
    xpos = xpos.lower()
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()

# Bar graph canada hockey gold, silver, bronze vs all the world combined bronze silver gold 
# pie chart canada vs usa total medals

hockey = []

gold_canada_hockeyMedals = []
silver_canada_hockeyMedals = []
bronze_canada_hockeyMedals = []

gold_worldNoU_hockeyMedals = []
silver_worldNoU_hockeyMedals = []
bronze_worldNoU_hockeyMedals = []

gold_usa_hockeyMedals = []
silver_usa_hockeyMedals = []
bronze_usa_hockeyMedals = []

print(line)
print('pushing data to Canada ice hockey array:')

for hockey in canada:
    if hockey[2] == 'Ice Hockey' and hockey[3] == 'Gold':
        gold_canada_hockeyMedals.append(hockey)
    elif hockey[2] == 'Ice Hockey' and hockey[3] == 'Silver':
        silver_canada_hockeyMedals.append(hockey)
    elif hockey[2] == 'Ice Hockey' and hockey[3] == 'Bronze':
        bronze_canada_hockeyMedals.append(hockey)

print('Canada has won', len(gold_canada_hockeyMedals), 'gold hockey medals')
print('Canada has won', len(silver_canada_hockeyMedals), 'silver hockey medals')
print('Canada has won', len(bronze_canada_hockeyMedals), 'bronze hockey medals')

print('pushing data to world (excluding CAN and USA) array:')
for hockey in worldNoU:
    if hockey[2] == 'Ice Hockey' and hockey[3] == 'Gold':
        gold_worldNoU_hockeyMedals.append(hockey)
    elif hockey[2] == 'Ice Hockey' and hockey[3] == 'Silver':
        silver_worldNoU_hockeyMedals.append(hockey)
    elif hockey[2] == 'Ice Hockey' and hockey[3] == 'Bronze':
        bronze_worldNoU_hockeyMedals.append(hockey)

print('pushing data to USA ice hockey array:')
for hockey in usa:
    if hockey[2] == 'Ice Hockey' and hockey[3] == 'Gold':
        gold_usa_hockeyMedals.append(hockey)
    elif hockey[2] == 'Ice Hockey' and hockey[3] == 'Silver':
        silver_usa_hockeyMedals.append(hockey)
    elif hockey[2] == 'Ice Hockey' and hockey[3] == 'Bronze':
        bronze_usa_hockeyMedals.append(hockey)

print('World has won', len(gold_worldNoU_hockeyMedals + gold_usa_hockeyMedals), 'gold hockey medals')
print('World has won', len(silver_worldNoU_hockeyMedals + silver_usa_hockeyMedals), 'silver hockey medals')
print('world has won', len(bronze_worldNoU_hockeyMedals + bronze_usa_hockeyMedals), 'bronze hockey medals')

print('USA has won', len(gold_usa_hockeyMedals), 'gold hockey medals')
print('USA has won', len(silver_usa_hockeyMedals), 'silver hockey medals')
print('USA has won', len(bronze_usa_hockeyMedals), 'bronze hockey medals')
