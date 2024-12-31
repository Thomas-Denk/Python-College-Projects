import requests
import matplotlib.pyplot as plt
import time




url='https://api.nytimes.com/svc/search/v2/articlesearch.json' 


print("Please be patient while the program obtains the graph data. This may take a while since the NY Times API limits the amount of calls...")
# Below are our actions to obtain the trump article values

trump_years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
trump_year_article_count = []
time.sleep(15)
for each in trump_years:
    begin_date = each + '0101'
    if each == '2023':
        end_date = each + '1210'
    else:
        end_date = each + '1231'
    params={'query':'Trump','api-key':'tWibIF6HmU4UJUiykZnZCAXsa8jAJfLY','begin_date':begin_date, 'end_date':end_date,'fq':'body.contains("Trump")','fq':'body.contains("campaign")'}
    response=requests.get(url,params=params)
    time.sleep(15)
    trump_year_article_count.append(response.json()['response']['meta']['hits'])
    

#deprecated....year_article_count.append(response.json()['response']['meta']['hits'])

#deprecated...print("Total Articles about the Trump campaign: " + str(response.json()['response']['meta']['hits']))

# Below are our actions to obtain the Biden article values

biden_years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
biden_year_article_count = []

for each in biden_years:
    begin_date = each + '0101'
    if each == '2023':
        end_date = each + '1210'
    else:
        end_date = each + '1231'
    params={'query':'Biden','api-key':'tWibIF6HmU4UJUiykZnZCAXsa8jAJfLY','begin_date':begin_date, 'end_date':end_date,'fq':'body.contains("Biden")','fq':'body.contains("campaign")'}
    response=requests.get(url,params=params)
    time.sleep(15)
    biden_year_article_count.append(response.json()['response']['meta']['hits'])


# Below are our actions to obtain the Clinton article values

clinton_years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
clinton_year_article_count = []

for each in clinton_years:
    begin_date = each + '0101'
    if each == '2023':
        end_date = each + '1210'
    else:
        end_date = each + '1231'
    params={'query':'Clinton','api-key':'tWibIF6HmU4UJUiykZnZCAXsa8jAJfLY','begin_date':begin_date, 'end_date':end_date,'fq':'body.contains("Clinton")','fq':'body.contains("campaign")'}
    response=requests.get(url,params=params)
    time.sleep(15)
    clinton_year_article_count.append(response.json()['response']['meta']['hits'])




#Transform Data

fig, ax = plt.subplots()

ax.plot(trump_years, trump_year_article_count)
plt.text(trump_years[0],trump_year_article_count[0], 'Trump', fontsize = 10)

ax.plot(biden_years, biden_year_article_count)
plt.text(biden_years[0],biden_year_article_count[0], 'Biden', fontsize = 10)

ax.plot(clinton_years, clinton_year_article_count)
plt.text(clinton_years[0],clinton_year_article_count[0], 'Clinton', fontsize = 10)


plt.title("Number of Articles Published Mentioning Candidates")
plt.xlabel("Year")
plt.ylabel("Number of Relevant Articles")
#Load Data 
plt.savefig('Candidates Relevency Chart.png')

print("The graph has finished exporting")

print("The year-by-year breakdown of article numbers for Trump is")
print(trump_year_article_count)
print("The total article count for Trump is ")
print(sum(trump_year_article_count))
print()
print("The year-by-year breakdown of article numbers for Biden is")
print(biden_year_article_count)
print("The total article count for Biden is ")
print(sum(biden_year_article_count))
print()
print("The year-by-year breakdown of article numbers for Clinton is")
print(clinton_year_article_count)
print("The total article count for Clinton is ")
print(sum(clinton_year_article_count))