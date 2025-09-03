from flask import Flask, render_template,request,jsonify

import requests

API_Key = 'd3f631f97d2f49718c8bdcab4df61985'
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-07-28&sortBy=publishedAt&apiKey=d3f631f97d2f49718c8bdcab4df61985"
app = Flask(__name__)

@app.route('/api/news' , methods = ['GET'])
def news():
    res = requests.get(url)
    if(res.status_code == 200):
        
        news_data = res.json()
        count = len(news_data['articles'])
        source = news_data['articles'][0]['source']
        author = news_data['articles'][0]['author']
        publishedAt = news_data['articles'][0]['publishedAt']
        content = news_data['articles'][0]['content']
   
        # returning in the json format:
        output_format = {
            'Total number of articles': count,
            'source':source,
            'author':author,
            'publishedAt':publishedAt,
            'content':content
            }
        
        return output_format
    
    else:
        return jsonify({'Error':'Invalid Api Key'})    

if __name__ == "__main__":
    app.run(debug=True)
