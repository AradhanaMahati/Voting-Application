import dframe as df
from dframe import *


def showVotes():
    result = df.show_result()
    print("Vote Count")
    print("BJP : ", result['bjp'])
    print("Cong : ",result['cong'])
    print("AAP : ",result['aap'])
    print("Shiv Sena : ",result['ss'])
    print("NOTA : ",result['nota'])

