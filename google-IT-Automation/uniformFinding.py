from re import U


def solution(uniformSet, uniformPieces):
    # Please write your code here.
    missing = len(uniformSet)
    productList = {}
    for product in uniformSet:
        #productList = {}
        for uniform in uniformPieces:
                #uniform.split('_',1)= [uniform]
            #productList = 
            #if uniform.split('_')[0] in productList :
            # else:
                #print("remove")
                #print(uniform)
                #productList.remove(uniform.split('_')[0])
                #print(productList)
            if uniform.split('_')[1] == product:
                # if uniform.split('_')[1] == product:
                #print(uniform.split('_'))
                #productList.append(uniform.split('_',1)[0])
                #company = uniform.split('_')[0]
                key = uniform.split('_')[0]
                if key in productList:
                    productList[uniform.split('_')[0]] +=1
                else:
                    productList[uniform.split('_')[0]] = 1
                    #uniform.split('_')[2] = [uniform]
                #print(productList)
            #if uniform.split('_')[0] in productList :
            # else:
            #     productList.remove(uniform.split('_')[0])
            #     print(productList)
    for company, value in productList.items():
        if value < missing:
            return company
    return ("N/A")
    #return productList
    
        
print(solution(["shoe", "shirt"], ["AstroCorp_shoe", "BetaCorp_hat", "CaliCorp_pant", "AstroCorp_shirt", "DeltaCorp_pant", "BetaCorp_shirt", "AstroCorp_belt", "DeltaCorp_shoe", "BetaCorp_belt", "BetaCorp_shoe", "CaliCorp_shirt", "CaliCorp_shoe", "AstroCorp_hat", "CaliCorp_belt", "CaliCorp_jacket", "DeltaCorp_belt", "DeltaCorp_pant", "AstroCorp_pant", "DeltaCorp_lanyard", "DeltaCorp_shirt"]))
# N/A
print(solution(["shoe", "shirt", "belt", "pant"], ["AstroCorp_shoe", "BetaCorp_hat", "CaliCorp_pant", "AstroCorp_shirt", "DeltaCorp_pant", "BetaCorp_shirt", "AstroCorp_belt", "DeltaCorp_shoe", "BetaCorp_belt", "BetaCorp_shoe", "CaliCorp_shirt", "CaliCorp_shoe", "AstroCorp_hat", "CaliCorp_belt", "CaliCorp_jacket", "DeltaCorp_belt", "DeltaCorp_pant", "AstroCorp_pant", "DeltaCorp_lanyard", "DeltaCorp_shirt"]))
# BetaCorp
print(solution(["hat","glasses"],["company1_hat", "company1_glasses","company2_hat"]))
# company2