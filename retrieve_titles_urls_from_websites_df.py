import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import pandas as pd

def retrieve_from_hri(driver):
    pdfurllist =  []
    pdfnamelist = []
    df = pd.DataFrame()
    paper_types = []
    paper_names = []
    downloaded = []
    sections = []

    elementllist =  driver.find_elements_by_class_name('toc__section')
    for i, section in enumerate(elementllist):
        try:
          section.find_element_by_partial_link_text('SESSION').click()
          section_name = section.find_element_by_partial_link_text('SESSION').get_attribute('textContent')
          #print(section_name)
          time.sleep(10)
        except NoSuchElementException:  
          section_name = 'None'
          pass
        except ElementClickInterceptedException:
          section_name = 'None'
          pass
          
        
        lists_paper_types = []
        for i, element in enumerate(section.find_elements_by_class_name('issue-item__citation')):
            type_p = element.find_element_by_class_name('issue-heading').get_attribute('innerHTML')
            #print(type_p)
            lists_paper_types.append(type_p)
            
        for j, paper_element in enumerate(section.find_elements_by_class_name('issue-item__content')):
          
          
          try:
            if (lists_paper_types[j] == 'research-article') | (lists_paper_types[j] == 'Article'):
                paper_name = paper_element.find_element_by_xpath('div/h5').get_attribute('textContent')
                #print(paper_name)
                pdf_url = paper_element.find_element_by_class_name("red").get_attribute('href')
                #print(paper_name,pdf_url)
                pdfnamelist.append(paper_name)
                pdfurllist.append(pdf_url)
                paper_types.append(lists_paper_types[j])
                paper_names.append(paper_name)
                downloaded.append(1)
                sections.append(section_name)

            else:
                paper_name = paper_element.find_element_by_xpath('div/h5').get_attribute('textContent')
                paper_types.append(lists_paper_types[j])
                paper_names.append(paper_name)
                downloaded.append(0)
                sections.append(section_name)



          except NoSuchElementException: 
            paper_types.append(lists_paper_types[j])
            paper_name = paper_element.find_element_by_xpath('div/h5').get_attribute('textContent')
            paper_names.append(paper_name)
            downloaded.append(0)
            sections.append(section_name)

            pass

    df['Section'] = sections
    df['Type'] = paper_types
    df['Name'] = paper_names
    df['Downloaded?'] = downloaded

    return pdfurllist, pdfnamelist, df

