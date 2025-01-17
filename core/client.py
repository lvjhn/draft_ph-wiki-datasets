import core.helpers as helpers
import requests

class Client:
    def __init__(self, *args, **kwargs):
        # dependency injection 
        self.requests = kwargs.get("inject_requests", requests)
        self.open     = kwargs.get("inject_open", open) 

        # extract arguments 
        self.base_url = \
            kwargs.get("base_url", "https://en.wikipedia.org")
        self.prefix   = \
            kwargs.get("prefix", "wiki") 
        self.download_outdir = \
            kwargs.get("download_outdir", "./data/articles/uncategorized")
    
    def get_output_filename(self, uri, outfile = None, extension="html"):
        if outfile: 
            return outfile  
        else: 
            return uri + "." + extension 

    def get_full_url(self, uri): 
        url = self.base_url + "/" + self.prefix + "/" + uri
        return url

    def data(self, uri): 
        url  = self.get_full_url(uri) 
        data = self.requests.get(url) 
        text = data.text    
        return text

    def download(self, uri, outfile = None, extension="html"): 
        outfile = self.get_output_filename(uri, outfile, extension) 
        text = self.data(uri)
        self.save_to_file(outfile, text)

    def save_to_file(self, outfile, text): 
        file = self.download_outdir + "/" + outfile
        file = file.replace("//", "/")
        outfile = self.open(file, "w") 
        outfile.write(text)
    