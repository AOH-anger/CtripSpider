# CtripSpider
携程爬虫

1. 使用scrapy框架下Spider的派生类CrawlSpiders, CrawlSpider类定义了一些（rule）来提供跟进link的方便的机制，更适合从爬取的网页中获取link并继续爬取

2. 爬取的是携程北京地区的某一时段的酒店信息（酒店名称、图片地址、描述、价格、分数、用户推荐百分比）

3. 少部分酒店的信息条目是缺失的，使用xpath解析的时候会报错，需要特别处理
![图片](/img/show.png)

4. ctrip.json是爬取下来的酒店信息

