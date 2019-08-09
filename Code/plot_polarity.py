import pandas as pd
import plotly
list_of_states=["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
cols=['state','polarity']
scl = [[0.2, 'rgb(255,0,0)'],[0.4, 'rgb(255,255,255)']]
# initialize list of lists 
dataForTrump = [['AL','Alabama',0,0],['AK','Alaska',0,0],['AZ','Arizona',0,0],['AR','Arkansas',0,0],['CA','California',0,0],['CO','Colorado',0,0],['CT','Connecticut',0,0],['DE','Delaware',0,0],['FL','Florida',0,0],['GA','Georgia',0,0],['HI','Hawaii',0,0],['ID','Idaho',0,0],['IL','Illinois',0,0],['IN','Indiana',0,0],['IA','Iowa',0,0],['KS','Kansas',0,0],['KY','Kentucky',0,0],['LA','Louisiana',0,0],['ME','Maine',0,0],['MD','Maryland',0,0],['MA','Massachusetts',0,0],['MI','Michigan',0,0],['MN','Minnesota',0,0],['MS','Mississippi',0,0],['MO','Missouri',0,0],['MT','Montana',0,0],['NE','Nebraska',0,0],['NV','Nevada',0,0],['NH','New Hampshire',0,0],['NJ','New Jersey',0,0],['NM','New Mexico',0,0],['NY','New York',0,0],['NC','North Carolina',0,0],['ND','North Dakota',0,0],['OH','Ohio',0,0],['OK','Oklahoma',0,0],['OR','Oregon',0,0],['PA','Pennsylvania',0,0],['RI','Rhode Island',0,0],['SC','South Carolina',0,0],['SD','South Dakota',0,0],['TN','Tennessee',0,0],['TX','Texas',0,0],['UT','Utah',0,0],['VT','Vermont',0,0],['VA','Virginia',0,0],['WA','Washington',0,0],['WV','West Virginia',0,0],['WI','Wisconsin',0,0],['WY','Wyoming',0,0]]
# initialize  DataFrame for trump 
dataframeForTrump = pd.DataFrame(dataForTrump, columns = ['Code', 'State', 'Positive', 'Negative'])

#load tweet data 
tweetDataForTrump = pd.read_csv("tweet_polarity_DonaldTrump.txt", names=cols, header=None,engine="python", sep=',' , error_bad_lines=False)

#iterate tweet data to calculate state wise positive and negative polarity
for ind in tweetDataForTrump.index:
 st=str(tweetDataForTrump['state'][ind])
 pol= str(tweetDataForTrump['polarity'][ind])
 for i in dataframeForTrump.index:
  if( str(dataframeForTrump['State'][i]) == st and (pol == 'positive')):
      dataframeForTrump.at[i,'Positive'] =dataframeForTrump['Positive'][i]+1
  elif (str(dataframeForTrump['State'][i]) == st and pol == 'negative'):
      dataframeForTrump.at[i,'Negative'] =dataframeForTrump['Negative'][i]+1       


#calculate the polarity for each state - (count of postive - count of negative)
dataframeForTrump['Difference'] = dataframeForTrump.apply( lambda row: row.Positive - row.Negative,axis=1)


print(dataframeForTrump)

# initialize list of lists
dataForBernie = [['AL','Alabama',0,0],['AK','Alaska',0,0],['AZ','Arizona',0,0],['AR','Arkansas',0,0],['CA','California',0,0],['CO','Colorado',0,0],['CT','Connecticut',0,0],['DE','Delaware',0,0],['FL','Florida',0,0],['GA','Georgia',0,0],['HI','Hawaii',0,0],['ID','Idaho',0,0],['IL','Illinois',0,0],['IN','Indiana',0,0],['IA','Iowa',0,0],['KS','Kansas',0,0],['KY','Kentucky',0,0],['LA','Louisiana',0,0],['ME','Maine',0,0],['MD','Maryland',0,0],['MA','Massachusetts',0,0],['MI','Michigan',0,0],['MN','Minnesota',0,0],['MS','Mississippi',0,0],['MO','Missouri',0,0],['MT','Montana',0,0],['NE','Nebraska',0,0],['NV','Nevada',0,0],['NH','New Hampshire',0,0],['NJ','New Jersey',0,0],['NM','New Mexico',0,0],['NY','New York',0,0],['NC','North Carolina',0,0],['ND','North Dakota',0,0],['OH','Ohio',0,0],['OK','Oklahoma',0,0],['OR','Oregon',0,0],['PA','Pennsylvania',0,0],['RI','Rhode Island',0,0],['SC','South Carolina',0,0],['SD','South Dakota',0,0],['TN','Tennessee',0,0],['TX','Texas',0,0],['UT','Utah',0,0],['VT','Vermont',0,0],['VA','Virginia',0,0],['WA','Washington',0,0],['WV','West Virginia',0,0],['WI','Wisconsin',0,0],['WY','Wyoming',0,0]]
  
# initialize  DataFrame for Bernie 
dataFrameForBernie = pd.DataFrame(dataForBernie, columns = ['Code', 'State', 'Positive', 'Negative'])

#load tweet data 
tweetDataForBernie = pd.read_csv("tweet_polarity_BernieSanders.txt", names=cols, header=None,engine="python", sep=',' , error_bad_lines=False)

#iterate tweet data to calculate state wise positive and negative polarity
for ind in tweetDataForBernie.index:
 st=str(tweetDataForBernie['state'][ind])
 pol= str(tweetDataForBernie['polarity'][ind])
 for i in dataFrameForBernie.index:
  if( str(dataFrameForBernie['State'][i]) == st and pol == 'positive'):
      dataFrameForBernie.at[i,'Positive'] =dataFrameForBernie['Positive'][i]+1
  elif (str(dataFrameForBernie['State'][i]) == st and pol == 'negative'):
      dataFrameForBernie.at[i,'Negative'] =dataFrameForBernie['Negative'][i]+1       
      
      
#calculate the polarity for each state - (count of postive - count of negative)
dataFrameForBernie['Difference'] = dataFrameForBernie.apply( lambda row: row.Positive - row.Negative,axis=1)

print(dataFrameForBernie)

dataForPlotlyMap = [['AL','Alabama',0],['AK','Alaska',0],['AZ','Arizona',0],['AR','Arkansas',0],['CA','California',0],['CO','Colorado',0],['CT','Connecticut',0],['DE','Delaware',0],['FL','Florida',0],['GA','Georgia',0],['HI','Hawaii',0],['ID','Idaho',0],['IL','Illinois',0],['IN','Indiana',0],['IA','Iowa',0],['KS','Kansas',0],['KY','Kentucky',0],['LA','Louisiana',0],['ME','Maine',0],['MD','Maryland',0],['MA','Massachusetts',0],['MI','Michigan',0],['MN','Minnesota',0],['MS','Mississippi',0],['MO','Missouri',0],['MT','Montana',0],['NE','Nebraska',0],['NV','Nevada',0],['NH','New Hampshire',0],['NJ','New Jersey',0],['NM','New Mexico',0],['NY','New York',0],['NC','North Carolina',0],['ND','North Dakota',0],['OH','Ohio',0],['OK','Oklahoma',0],['OR','Oregon',0],['PA','Pennsylvania',0],['RI','Rhode Island',0],['SC','South Carolina',0],['SD','South Dakota',0],['TN','Tennessee',0],['TX','Texas',0],['UT','Utah',0],['VT','Vermont',0],['VA','Virginia',0],['WA','Washington',0],['WV','West Virginia',0],['WI','Wisconsin',0],['WY','Wyoming',0]]

# initialize  DataFrame for trump 
dataFrameForPlotlyMap = pd.DataFrame(dataForPlotlyMap, columns = ['Code', 'State', 'Color'])

for r in dataFrameForPlotlyMap.index:
    if dataframeForTrump['Difference'][r] < dataFrameForBernie['Difference'][r]:
        dataFrameForPlotlyMap.at[r,'Color'] = -1 
    else:
        dataFrameForPlotlyMap.at[r,'Color']=1
        
    
dataFrameForPlotlyMap['text'] = dataFrameForBernie.apply( lambda row: 'Bernie vs Trump',axis=1)        


        
dataMapForPlotly = [ dict(
        type='choropleth',
        colorscale = scl,
        autocolorscale = False,
        locations = dataFrameForPlotlyMap['Code'],
        z = dataFrameForPlotlyMap['Color'].astype(float),
        locationmode = 'USA-states',
        text = dataFrameForPlotlyMap['text']
        ) ]    	        


layout = dict(
        title = 'Election Prediction',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'),
             )    

plotly.offline.plot({"data":dataMapForPlotly, "layout":layout},filename = 'electionPrediction.html')        






