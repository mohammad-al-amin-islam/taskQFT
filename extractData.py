
import requests;
from bs4 import BeautifulSoup;
import re;


def extractData():
    baseUrl="https://www.dsebd.org/old_news.php?inst=ACI&criteria=3&archive=news";
    response = requests.get(baseUrl);
    soup = BeautifulSoup(response.text, 'html.parser')

    tables = soup.find_all("table", class_="table-news")
    myRegex = 'EPS was Tk. (.*?) for (.*?) (.*?) as against Tk. (.*?) for (.*?) (\d*)'
    finalData = [];
    
    for table in tables:
        td = table.find_all("td");
        for singleTd in td:
            # print(singleTd.string);
            text = singleTd.string;
            epsValue = re.findall(myRegex,text);
            
            if(len(epsValue)!=0):
                finalData.append(epsValue);
    
    # showing the data
    for data in finalData:
        for sData in data:
            print(f"Date: ({sData[1]}){sData[2]} EPS: {sData[0]}\nDate: ({sData[4]}){sData[5]} EPS: {sData[3]}\n");  

extractData()