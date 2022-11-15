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

#Do not edit this code

from navigator import Navigator
import traceback

def main():
    magellan = Navigator()
    try:
        magellan.navigate()
        magellan.click_em_all()
        magellan.fill_form()
    except Exception as e:
        magellan.screenshot_error(e)
        print(traceback.format_exc())
        print(e)
        
if __name__ == '__main__':
    main()