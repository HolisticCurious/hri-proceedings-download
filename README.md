# hri-proceedings-download
Script for downloading HRI Conference Proceedings from ACM library



Based on [this repository](https://github.com/seanywang0408/Crawling-CV-Conference-Papers.git).

Python notebook allows for easy troubleshooting. It will download every available paper for the year chosen. 

Two versions abailable
- retrieve_titles_urls_from_websites.py and HRIProceedingsDownload.ipynb download every file available, regardless of type (abstract, research article, poster, short paper, etc.)
- retrieve_titles_urls_from_websites_df.py and HRIProceedingsDownload_df.ipynb download only reseach articles and create a dataframe that allows for easy consultation of files downloaded and files skipped.

Reasons which may lead to missed downloads:

* The code is prepared to run using KTH VPN. Acdess to papers must be guaranteed by the user, but the display of the pdf button may change and thus the python script may have to be adjusted accordingly. 
* The document may still not be available, even with academic access. 
* Internet too slow. You can adjust the pause time in the script, giving the page time to load the documents in the tab. I would also recommend running the code again, as it tends to fix it.

