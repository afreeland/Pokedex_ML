# Pokedex_ML
This project aims to allow for a real life pokedex.  I've put it off far too long and decided to pick it back up.



## Crawling images
Nobody wants to manually fetch images for classification training...so this helps automate that

You can simply run the following
```
python crawler.py pikachu
```

This will automatically start to crawl Google images and begin fetching images for `pikachu`.  Additionally, there are some other searches that are automated for `pikachu plush` and `pikachu cards`.  The hope is that you can simply point your pokedex at many different styles of objects and be able to identify the proper Pokemon.

Things still needing to be done:
- Include Bing images (which also means prefixing data sets)
- Automate for *ALL* the different pokemon..but lets start small instead of killing image search at the moment.

