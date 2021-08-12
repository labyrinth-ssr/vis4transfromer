import json
def attnProcess(py_data):
    

    layerCnt=0
    sumAttn=[]
    for layer in py_data:
        headCnt=0
        for head in layer:
            headAttn=[]
            sourceCnt=0
            for source in head:
                targetCnt=0
                for val in source:
                    headDict={'source':sourceCnt,'target':targetCnt,'val':val}
                    headAttn.append(headDict)
                    targetCnt+=1
                sourceCnt+=1
            sumDict={'layer':layerCnt,'head':headCnt,'attn':headAttn}
            sumAttn.append(sumDict)
            headCnt+=1
        layerCnt+=1
    return sumAttn

