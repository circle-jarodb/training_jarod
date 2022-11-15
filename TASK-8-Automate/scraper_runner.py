#    ___| _)             |          |                   _)        |   _)             
#   |      |   __|  __|  |   _ \    |       _ \    _` |  |   __|  __|  |   __|   __| 
#   |      |  |    (     |   __/    |      (   |  (   |  | \__ \  |    |  (    \__ \ 
#  \____| _| _|   \___| _| \___|   _____| \___/  \__, | _| ____/ \__| _| \___| ____/ 
#                                                |___/                               
#  
#  AUTHOR: 
#  NOTES: 
#         
#         
#     

from scraper import Scraper
import traceback

def main():
    scotty = Scraper()
    try:
        #Call your functions
        pass
    except Exception as e:
        scotty.screenshot_error(e)
        print(traceback.format_exc())
        print(e)
        
if __name__ == '__main__':
    main()