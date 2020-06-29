from django.http import *
from django.shortcuts import *
import math
from bs4 import BeautifulSoup as bs
import sys
import requests

def performoperation(request):
    return render(request,'performoperation.html')

def base(request):
    return render(request,'base.html')
    
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def error(request):
    return render(request,'error.html')

def performOperationAction(request):
    # get text from the text area
    textcoming = request.POST.get('textAdded','default')
    
    # if textarea was empty
    if len(textcoming)==0:
        return HttpResponseRedirect('/performoperation')

    # get the checkbox values
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize','off')
    newlineremove = request.POST.get('newlineremove','off')
    removespace = request.POST.get('removespace','off')
    charcount = request.POST.get('charcount','off')

    # if everything is off
    if removepunc=='off' and capitalize=='off' and newlineremove=='off' and removespace=='off' and charcount=='off':
        return HttpResponseRedirect('/error')

    counts=0
    if charcount=='on':
        counts=len(textcoming)

    result=""
    # if we have to capitalize the whole text
    if capitalize=='on':
        textcoming = textcoming.upper()
        result=textcoming

    # if punctuations are to be removed
    punctuations = '''()[]{}<>|='"<>:,‒–—―!.-‐?;/\⁄&@*\\_`~#$%^()'''
    if removepunc=='on':
        if result=="":
            for char in textcoming:
                if char not in punctuations and char!='\n':
                    result = result + char
        else:
            prevresult = result
            result=""
            for char in prevresult:
                if char not in punctuations:
                    result = result + char

    #if new line characters are to be removed
    if newlineremove=='on':
        if result=="":
            for char in textcoming:
                if char!="\n" and char!="\r":
                    result = result + char
        else:
            prevresult = result
            result=""
            for char in prevresult:
                if char!="\n" and char!="\r":
                    result = result + char

    # if we have to remove the spaces from the text
    if removespace=='on':
        if result=="":
            for index,char in enumerate(textcoming):
                if index>=len(textcoming):
                    break;

                if index == len(textcoming)-1:
                    if(textcoming[index]==' '):
                        break;
                    else:
                        result=result + char
                        break;

                if not(textcoming[index]==" " and textcoming[index+1]==" "):
                    result = result + char
        else:
            prevresult = result
            result = ""
            for index,char in enumerate(prevresult):
                if index>=len(prevresult):
                    break;

                if index == len(prevresult)-1:
                    if(prevresult[index]==' '):
                        break;
                    else:
                        result=result + char
                        break;

                if not(prevresult[index]==" " and prevresult[index+1]==" "):
                    result = result + char

    if counts==0:
        d = {
            'ans':result
        } 
        return render(request,'analyser.html',d)

    else:
        result=result + " => Count Of Characters in String is " + str(counts);
        d = {
            'ans':result
        } 
        return render(request,'analyser.html',d)

def analysecharacters(request):
    return render(request,'analysecharacters.html')

def eachcharresult(request):
    return render(request,'eachcharresult.html')

def analysecharaction(request):
    textcoming = request.POST.get('textAdded')

    if len(textcoming)==0:
        return HttpResponseRedirect('/analysecharacters')

    type = request.POST.get('charAnalyse')
    if type=="allcount":
        ans = len(textcoming)
        s = "The No Of Characters In The Text Are: "
        ans = s + str(ans)

        d={
            'ans':ans
        }

        return render(request,'analysecharresult.html',d)

    if type=="alphacount":
        s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        count=0
        for char in textcoming:
            if char in s:
                count+=1
        
        ans = "The No Of Alphabets In The Text Are: " + str(count)
        d={
            'ans':ans
        }

        return render(request,'analysecharresult.html',d)

    if type=="eachcount":
        s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        data=[]
        for char in s:
            if char in textcoming:
                count = textcoming.count(char)
                dict={}
                dict['alpha'] = char
                dict['count'] = count  
                data.append(dict)
        context = {
            'data':data
        }

        return render(request,'eachcharresult.html',context)

    return render(request,'analysecharresult.html')

def funtext(request):
    return render (request,'funtext.html')

def textfunaction(request):
    textcoming = request.POST.get('textAdded')

    # if textarea was empty
    if len(textcoming)==0:
        return HttpResponseRedirect('/funtext')
    
    s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result=""
    for char in textcoming:
        if char in s:
            result = result + char 

    # finding the length, floor and ceil values
    l = len(result)
    fvalue = math.floor(math.sqrt(l))
    cvalue = math.ceil(math.sqrt(l))

    row = 0
    col = 0

    # finding the no of rows and cols required
    for i in range(fvalue,cvalue+1):
        flag=0
        for j in range(fvalue,cvalue+1):
            if i*j >= len(result):
                row = i
                col = j
                flag=1
                break
        if(flag==1):
            break

    # making the 2d matrix/grid
    list1=[]
    for i in range(0,row):
        temp=[]
        for j in range(0,col):
            ch=" "
            temp.append(ch)
        list1.append(temp)

    index=0
    for i in range(0,row):
        if index >= len(result):
            break
        for j in range(0,col):
            if index >= len(result):
                break
            list1[i][j] = result[index];
            index+=1;

    # finding the encoded string
    ans=""
    for i in range(0,col):
        for j in range(0,row):
            if list1[j][i]==' ':
                continue
            ans = ans + list1[j][i]
        ans=ans+" "
    
    d={
        'ans':ans 
    }
 
    return render(request,'textfunoutput.html',d)

def textfunoutput(request):
    return render(request,'textfunoutput.html')

def extracturl(request):
    return render(request,'extracturl.html')

def extracturlaction(request):
    textcoming = request.POST.get('textAdded')

    if len(textcoming)==0:
        return HttpResponseRedirect('/extracturl')

    result = textcoming
    result.lower()

    h="https://"
    w="www."

    listURLS=[]
    idx=0
    while(True):
        if(idx>=len(result)):
            break 

        indexhttp = result.find(h,idx,len(result))
        if(indexhttp==-1):
            break
        
        idx=indexhttp+1
        indexwww = result.find(w,indexhttp+4,len(result))
        if(indexwww==-1):
            break

        s=""
        idx=indexwww+1 
        while(indexhttp<len(result) and result[indexhttp]!=' '):
            s=s+result[indexhttp]
            indexhttp+=1

        dict = {}
        dict['url'] = s    
       
        listURLS.append(dict)

    idx=0
    h="http://"
    while(True):
        if(idx>=len(result)):
            break 

        indexhttp = result.find(h,idx,len(result))
        if(indexhttp==-1):
            break
        
        idx=indexhttp+1
        indexwww = result.find(w,indexhttp+4,len(result))
        if(indexwww==-1):
            break

        s=""
        idx=indexwww+1 
        while(indexhttp<len(result) and result[indexhttp]!=' '):
            s=s+result[indexhttp]
            indexhttp+=1

        dict = {}
        dict['url'] = s    
       
        listURLS.append(dict)
    d = {
        'ans':listURLS
    }
    return render(request,'extracturloutput.html',d)

def extracturloutput(request):
    return render(request,'extracturloutput.html')

def worddictionary(request):
    return render(request,'worddictionary.html')

def calc(request):
    word = request.GET['word']
    url = "https://dictionary.cambridge.org/dictionary/english/"
    url+=word
    r = requests.get(url)
    soup = bs(r.content,'lxml')

    header = soup.findAll("span", {"class": "pos"})
    if len(header)==0:
        d={'pos':'' , 'result':''}
        return JsonResponse(d,safe=False)

    header = soup.findAll("span", {"class": "pos"})[0].text
    answer_list = soup.findAll("div",{"class":"def-body"})[0].text

    d={'pos':header,'result':answer_list}
    return JsonResponse(d,safe=False)

def wordlimitchecker(request):
    return render(request,'wordlimitchecker.html')
