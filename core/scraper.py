import core.helpers as helpers

class Scraper:
    def __init__(self, *args, **kwargs):
        # extract arguments 
        self.client = \
            kwargs.get("client", None) 
        self.download_outdir = \
            kwargs.get("download_outdir", None) 
        self.output_filename = \
            kwargs.get("output_filename", lambda p, t: f"{t}.html")

        # set download dir of client 
        self.client.download_outdir = self.download_outdir  

        # get list items to scrape
        self.items = [] 

    def add(self, tail): 
        self.items.append(tail)

    def add_multi(self, tails): 
        self.items += tails

    def scrape(self, verbose=False):
        client = self.client
        for item in self.items: 
            prefix = client.prefix 
            filename = self.output_filename(prefix, item)
            client.download(item, filename)
