import requests
import matplotlib.pyplot as plt





url='https://api.nytimes.com/svc/search/v2/articlesearch.json' 


#params={'query':'Trump','api-key':'tWibIF6HmU4UJUiykZnZCAXsa8jAJfLY'}
params={'query':'Trump','api-key':'tWibIF6HmU4UJUiykZnZCAXsa8jAJfLY','fq':'body.contains("Trump")','fq':'body.contains("campaign")'}

# 'fq':'source=trump',
#fq=subject.contains:("Trump")
trump_response=requests.get(url,params = params)

print("Total Articles for Trump: " + str(trump_response.json()['response']['meta']['hits']))




'''
# Results with Biden in subject

params2={'query':'Biden','fq=subject.contains':'Biden','api-key':'tWibIF6HmU4UJUiykZnZCAXsa8jAJfLY'}

biden_response=requests.get(url,params2)

print("Total Articles with Biden in the headline: " + str(biden_response.json()['response']['meta']['hits']))

# Results with Clinton in subject

params3={"fq=subject.contains":("Clinton"),'api-key':'tWibIF6HmU4UJUiykZnZCAXsa8jAJfLY'}

clinton_response=requests.get(url,params=params3)

print("Total Articles with Clinton in the headline: " + str(clinton_response.json()['response']['meta']['hits']))


'''
