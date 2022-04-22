import newspaper
from newspaper import Article
 
url = "https://hk.on.cc/hk/intnews/index.html"
 
# download and parse article
article = Article(url)
article.download()
article.parse()
 
# print article text
print(article.text)