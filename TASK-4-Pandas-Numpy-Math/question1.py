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
#        .

import pandas as pd
import seaborn as sns


def main():
    df = sns.load_dataset('iris')
    print(df)

if __name__ == '__main__':
    main()
