import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

def retrieve_from_hri(driver):
    pdfurllist =  []
    pdfnamelist = []

    elementllist =  driver.find_elements_by_class_name('toc__section')[2:-2]
    for i, section in enumerate(elementllist):
        #print(section.get_attribute('outerHTML'))
        try:
          section.find_element_by_partial_link_text('SESSION').click()
        except NoSuchElementException:  
          pass
        except ElementClickInterceptedException:
          pass
          
        time.sleep(3)
        for j, paper_element in enumerate(section.find_elements_by_class_name('issue-item__content')):
          
          try:
            paper_name = paper_element.find_element_by_xpath('div/h5').text
           
            pdf_url = paper_element.find_element_by_class_name("red").get_attribute('href')
            print(paper_name,pdf_url)
            pdfnamelist.append(paper_name)
            pdfurllist.append(pdf_url)
          except NoSuchElementException: 
            pass


    return pdfurllist, pdfnamelist
