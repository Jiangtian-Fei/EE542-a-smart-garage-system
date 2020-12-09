#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3
import pandas as pd
from datetime import datetime
import numpy as np

client = boto3.client('iotanalytics')

dataset = "parking_dataset"
dataset_url  = client.get_dataset_content(datasetName = dataset)['entries'][0]['dataURI']

df = pd.read_csv(dataset_url).sort_values(by=['time']).drop(columns=['__dt']).reset_index(drop=True)
df = df.drop([0,1,2,3,4]).reset_index(drop=True)
df
dict = {'7UON934':'+1 5305649132', '8GWM929':'+1 5307606039'};


# Second = df[df['status']=='LEVEL 2'].reset_index(drop=True)
# First = df
# for x in range (0,len(Second.index)-1):
#     First = First[First['plate']!=Second['plate'][x]]

# In[2]:


def send(txt, phone):
	# Create an SNS client
	client = boto3.client(
    		"sns",
    		aws_access_key_id="AKIAXDK47CXK2TIZMMF3",
    		aws_secret_access_key="kleDihHqu1i+GVE0vaJ0OU0GciVMIFAd28bF9bPL",
    		region_name="us-east-1"
	)

	# Send your sms message.
	client.publish(
    		PhoneNumber=phone,
    		Message=txt
	)

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)


# In[3]:


df


# In[4]:


from datetime import datetime
import numpy as np

test = df
eliminate = np.full(len(test.index),True)
for x in range(len(test.index)):
    if test['status'][x]=='Exiting':
        plate = test['plate'][x]
        eliminate = eliminate & (test['plate']!=plate).values
test = test[eliminate]
test


# In[ ]:


import time
index = 31
while True:
    
    client = boto3.client('iotanalytics')

    dataset = "parking_dataset"
    dataset_url  = client.get_dataset_content(datasetName = dataset)['entries'][0]['dataURI']

    df = pd.read_csv(dataset_url).sort_values(by=['time']).drop(columns=['__dt']).reset_index(drop=True)
    df = df.drop([0,1,2,3,4]).reset_index(drop=True)
    new = df[index:].reset_index(drop=True)

    if len(new.index) > 0:
        print ("New data detected")
        index = index + len(new.index)
        test = pd.concat([test,new]).reset_index(drop=True)
        eliminate = np.full(len(test.index),True)
        for x in range(len(new.index)):
            if new['status'][x]=='Entering':
                print(new['plate'][x],'Enter')
            if new['status'][x]=='Exiting':
                print(new['plate'][x],'Exit')
                plate = new['plate'][x]
                if plate in dict:
                    print("plate found")
                    phone = dict[plate]
                    ts = new['time'][x]
                    exit = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    if len(df.loc[df['plate']==plate].loc[df['status']=='Entering']['time']) > 1:
                        meter = convert(ts - df.loc[df['plate']==plate].loc[df['status']=='Entering']['time'].iloc[-1])
                    else:
                        meter = convert(ts - df.loc[df['plate']==plate].loc[df['status']=='Entering']['time'])
                    text = "Your vehicle " + plate + " exited at " + exit+". Total parking time is "+ meter+
                    send(text,phone)
                    send(text,phone)
                    print("Message sent.")
                eliminate = eliminate & (test['plate']!=plate).values
        test = test[eliminate]
    time.sleep(10)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




