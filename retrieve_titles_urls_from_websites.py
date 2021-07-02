import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

def retrieve_from_hri(driver):
    pdfurllist =  []
    pdfnamelist = []

    elementllist =  driver.find_elements_by_class_name('toc__section')
    for i, section in enumerate(elementllist):
        try:
          section.find_element_by_partial_link_text('SESSION').click()
          print(section.find_element_by_partial_link_text('SESSION').get_attribute('textContent'))
        except NoSuchElementException:  
          pass
        except ElementClickInterceptedException:
          pass
          
        time.sleep(10)
        for j, paper_element in enumerate(section.find_elements_by_class_name('issue-item__content')):
          
          try:
            paper_name = paper_element.find_element_by_xpath('div/h5').get_attribute('textContent')
            #print(paper_name)
            pdf_url = paper_element.find_element_by_class_name("red").get_attribute('href')
            print(paper_name,pdf_url)
            pdfnamelist.append(paper_name)
            pdfurllist.append(pdf_url)
          except NoSuchElementException: 
            pass


    return pdfurllist, pdfnamelist
