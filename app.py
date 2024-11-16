from flask import Flask, request, jsonify
from recipe_scrapers import scrape_html
import requests

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')
    if not url:
      return jsonify({'error': 'URL is required'}), 400
    
    print('got ', url)
    html = requests.get(url, headers={"User-Agent": f"MealMind"}).content
    scraper = scrape_html(html, org_url=url)
    data = {
      'title': scraper.title(),
      'total_time': scraper.total_time(),
      'ingredients': scraper.ingredients(),
      'instructions': scraper.instructions(),
      'image': scraper.image(),
      'host': scraper.host(),
      'author': scraper.author()
    }

    return jsonify(data)

if __name__ == '__main__':
  app.run()
