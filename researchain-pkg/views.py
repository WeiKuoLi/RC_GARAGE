from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Profile, MapCityinfo, MapConninfo, TrendCitaDocu, TrendCitaImpact, TrendPublisher, articleinfo, Arxiv, MapCoauthorinfo, Profile_token, scopusmatch1, Profile_check
from django import forms

#Map
from django.core.serializers import serialize
import json

import time
from slugify import slugify
import pandas as pd
import re
###
import operator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q

from django.contrib.staticfiles.storage import staticfiles_storage

from django.contrib.staticfiles.finders import find

import urllib
import urllib.request

import requests

import time

import json
from django.contrib.auth.models import User
from profiles.models import Referral

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import get_object_or_404
from django.http import Http404

from journals.models import *
from django.core.exceptions import ValidationError
from django.db.models import Q


# def profile(request, user_url):

#     user_listing = get_object_or_404(Profile, userurl=user_url)

#     user_url=user_listing.user_url
#     userurl=user_listing.userurl
#     onboard=user_listing.onboard

#     # print(user_url)
#     # print(user_listing)

#     if request.method == 'POST':
#         user_email=request.user.email
#         avatarStyle = request.POST.get('avatarStyle')
#         topType = request.POST.get('topType')
#         accessoriesType = request.POST.get('accessoriesType')
#         hairColor = request.POST.get('hairColor')
#         hatColor = request.POST.get('hatColor')
#         facialHairType = request.POST.get('facialHairType')
#         facialHairColor = request.POST.get('facialHairColor')
#         clotheType = request.POST.get('clotheType')
#         clotheColor = request.POST.get('clotheColor')
#         graphicType = request.POST.get('graphicType')
#         eyeType = request.POST.get('eyeType')
#         eyebrowType = request.POST.get('eyebrowType')
#         mouthType = request.POST.get('mouthType')
#         skinColor = request.POST.get('skinColor')
#         Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

#         URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


#         return redirect('profile', URL)

    

#     csvpath='AA/static/scopus_match1.csv'
#     scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8', engine='python')
#     # print(scopusmatch.columns)
#     # print(scopusmatch['scopus'].values)
#     userurllist=scopusmatch['user_url'].values
#     scopuslist=scopusmatch['scopus'].values
#     dictmatch=dict(zip(userurllist,scopuslist))
    
 
#     #trend
#     # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
#     # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
#     # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
#     # citedata=cite.split('#')
#     # docyear=docu.split('#')

#     #impact
#     # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
#     # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
#     # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
#     # ifdata=impact.split('#')
#     # docyear=docu.split('#')

#     #publisher
#     # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
#     # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
#     # publisher=publisher.split('#') 


#     # cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


#     # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

#     # countorigin=[]
#     # for i in range(len(cityinfo_qs)):
#     #     countorigin.append(int(cityinfo_qs[i].countn))

#     if onboard is True:
#         ######################20210103###################
#         cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
#         #print("幹")
#         #print(cityinfo_qs)
#         #print(len(cityinfo_qs))

#         conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

#         countorigin=[]
#         for i in range(len(cityinfo_qs)):
#             tmpcityinfo=cityinfo_qs[i].asso
#             #print(tmpcityinfo)
#             cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
#             countorigin.append(int(cityinfo_qs[i].countn))
    



#         # start = 5
#         # end = 10
#         # arr=countorigin
#         # if len(arr)>1:
#         #     print(arr)
#         #     print(len(arr))
#         #     width = end - start
#         #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
#         # else:
#         #     res=[arr for x in arr][0]

#         start = 5
#         end = 10
#         arr=countorigin
#         if len(arr)>1:
#             #print(arr)
#             #print(len(arr))
#             width = end - start
#             if int(max(arr)-min(arr))!=0:
#                 res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
#             else:
#                 res=[x for x in arr]
#         else:
#             res=arr

#         for i in range(len(cityinfo_qs)):
#             cityinfo_qs[i].countn=res[i]

#         cityinfo_json = serialize("json", cityinfo_qs)
#         conninfo_json = serialize("json", conninfo_qs)


        
#         f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r') 

#         # f = urllib.request.urlopen('http://127.0.0.1:8000/static/profile/%s/tree.json' %(user_url))
#         tree1_json=f.read()

#         f.close()

#         # GOODDDDD
#         # with urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json') as response:
#         #     tree1_json=response.read()

#             # f.close()



#         #article
#         articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
    

        


#         profile1=[]
#         for i in range(len(articleinfo_qs)):
#             profile1.append(user_url) 
#         journal=list(articleinfo_qs.values_list('journal', flat=True))
#         year=list(articleinfo_qs.values_list('year', flat=True))
#         title=list(articleinfo_qs.values_list('title', flat=True))
#         titleurl=[slugify(x) for x in title]
#         #author=list(articleinfo_qs.values_list('author', flat=True))
#         author=list(articleinfo_qs.values_list('authorabbr', flat=True))

#         author=["; ".join(x.split('#')) for x in author]
#         #print(author)
#         cite=list(articleinfo_qs.values_list('cite', flat=True))
#         # print("cite",cite)
#         cite1=[]
#         for x in cite:
#             try:
#                 cite1.append(int(x))
#             except:
#                 cite1.append(0)
#         abstract=list(articleinfo_qs.values_list('abstract', flat=True))


#         articlein=zip(profile1,journal,year,title,author,cite1,titleurl,abstract)

#         # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)
#         # print(len(profile1))

#         articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=True)[:10]
        
#         connauthorinfo_qs=MapCoauthorinfo.objects.filter(profile=dictmatch[user_url])
#         # print("幹幹幹!")
#         coauthorstr=list(connauthorinfo_qs.values_list('coauthor', flat=True))[0]
#         #print(coauthorstr.split('$')[0])
        
#         coauthorname=[]
#         coauthoraffi=[]
#         coauthoritem=[]
#         coauthorahref=[]
#         #   var tmp=NewArray[i].split("#")[0].split('&')[0];
#         #                     var tmp2=NewArray[i].split("#")[0].split('&')[1];
#         #                     var tmp1=tmp.split(" ").join("7").replace('.','_').replace(',','8');
#         #                     //var tmp1="test";
#         #                     var userurl='{{user_url}}';
#         #                     //console.log(userurl);
#         #                     var ttt='<a href= "http://127.0.0.1:8000/profile/'+userurl+'/network-affliation/'+tmp1+'">';
#         for k in range(len(coauthorstr.split('$'))):
#             coauthorname.append(coauthorstr.split('$')[k].split('#')[0].split('&')[0])
#             coauthoraffi.append(coauthorstr.split('$')[k].split('#')[0].split('&')[1])
#             coauthoritem.append(int(coauthorstr.split('$')[k].split('#')[-1]))
#             tmpname=coauthorstr.split('$')[k].split('#')[0].split('&')[0]
#             # print(tmpname.split(" "))
#             # ['Liao,', 'Y.-M']
#             # Liao87Y_-M
#             tmp1="7".join(tmpname.split(" ")).replace('.','_').replace(',','8')
            
#             coauthorahref.append("/profile/%s/network-coauthor/%s" %(userurl,tmp1))
        
#         coauthorzip=sorted(zip(coauthorname,coauthoraffi,coauthoritem,coauthorahref),key=lambda x: -x[2])[:10]



#         context = {
#                 'user_listing':user_listing,
#                 # 'citedata':citedata,
#                 # 'docyear':docyear,
#                 # 'ifdata':ifdata,
#                 #'publisher':publisher,
#                 'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
#                 'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
#                 'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
#                 'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),
#                 'cityinfo_json':cityinfo_json,
#                 'conninfo_json':conninfo_json,
#                 'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
#                 'tree1_json':tree1_json,
#                 'articlein':articlein,
#                 'user_url':user_url,
#                 'userurl':userurl,
#                 'coauthorzip':coauthorzip,
#             }

#     else: 
#         context = {
#                 'user_listing':user_listing,
#             }

    
#     return render(request, 'profile/profile_listing.html', context)


# def profile0707(request, user_url):

#     zero_time=time.time()

#     #user_listing = get_object_or_404(Profile, userurl=user_url)
#     searchid=int(user_url.split("-")[-1])

#     #user_listing = get_object_or_404(Profile_test, userurl=user_url)
#     #print(len(Profile_test.objects.all()))
#     user_listing= Profile.objects.get(pk=searchid)

#     zero_time1=time.time()
#     #print(zero_time1-zero_time)
#     #print("get_object_or_404(Profile, userurl=user_url)")
#     #print(zero_time1-zero_time)
#     #print("#####################################################")

#     user_url=user_listing.user_url
#     userurl=user_listing.userurl

#     # print(user_url)
#     # print(user_listing)

#     if request.method == 'POST':
#         user_email=request.user.email
#         avatarStyle = request.POST.get('avatarStyle')
#         topType = request.POST.get('topType')
#         accessoriesType = request.POST.get('accessoriesType')
#         hairColor = request.POST.get('hairColor')
#         hatColor = request.POST.get('hatColor')
#         facialHairType = request.POST.get('facialHairType')
#         facialHairColor = request.POST.get('facialHairColor')
#         clotheType = request.POST.get('clotheType')
#         clotheColor = request.POST.get('clotheColor')
#         graphicType = request.POST.get('graphicType')
#         eyeType = request.POST.get('eyeType')
#         eyebrowType = request.POST.get('eyebrowType')
#         mouthType = request.POST.get('mouthType')
#         skinColor = request.POST.get('skinColor')
#         Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

#         URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


#         return redirect('profile', URL)

    

#     csvpath='AA/static/scopus_match1.csv'
#     scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8', engine='python')

#     zero_time2=time.time()
    
#     #print("pd.read_csv(csvpath,sep='\t',encoding='utf-8', engine='python')")
#     #print(zero_time2-zero_time)
#     #print("#####################################################")
#     # print(scopusmatch.columns)
#     # print(scopusmatch['scopus'].values)
#     userurllist=scopusmatch['user_url'].values
#     scopuslist=scopusmatch['scopus'].values
#     dictmatch=dict(zip(userurllist,scopuslist))
    
 
#     #trend
#     # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
#     # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
#     # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
#     # citedata=cite.split('#')
#     # docyear=docu.split('#')

#     #impact
#     # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
#     # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
#     # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
#     # ifdata=impact.split('#')
#     # docyear=docu.split('#')
#     # zero_time3=time.time()
    
#     #print("TrendCitaImpact.objects.filter(profile=dictmatch[user_url])")
#     #print(zero_time3-zero_time)
#     #print("#####################################################")
#     #publisher
#     # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
#     # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
#     # publisher=publisher.split('#') 


#     # cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


#     # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

#     # countorigin=[]
#     # for i in range(len(cityinfo_qs)):
#     #     countorigin.append(int(cityinfo_qs[i].countn))

#     ######################20210103###################
#     cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
#     #print("幹")
#     #print(cityinfo_qs)
#     #print(len(cityinfo_qs))

#     conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

#     countorigin=[]
#     for i in range(len(cityinfo_qs)):
#         tmpcityinfo=cityinfo_qs[i].asso
#         #print(tmpcityinfo)
#         cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
#         countorigin.append(int(cityinfo_qs[i].countn))
#     zero_time4=time.time()
    
#     #print("MapCityinfo.objects.filter(profile=dictmatch[user_url])")
#     #print(zero_time4-zero_time)
#     #print("#####################################################")


#     # start = 5
#     # end = 10
#     # arr=countorigin
#     # if len(arr)>1:
#     #     print(arr)
#     #     print(len(arr))
#     #     width = end - start
#     #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
#     # else:
#     #     res=[arr for x in arr][0]

#     start = 5
#     end = 10
#     arr=countorigin
#     if len(arr)>1:
#         #print(arr)
#         #print(len(arr))
#         width = end - start
#         if int(max(arr)-min(arr))!=0:
#             res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
#         else:
#             res=[x for x in arr]
#     else:
#         res=arr

#     for i in range(len(cityinfo_qs)):
#         cityinfo_qs[i].countn=res[i]

#     cityinfo_json = serialize("json", cityinfo_qs)
#     conninfo_json = serialize("json", conninfo_qs)


    
#     #f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r') 

#     # f=open('AA/static/profile/%s/tree.json' %(user_url),'r') 
#     # tree1_json=f.read()

#     # f.close()
#     # zero_time5=time.time()
    
#     #print("MapCityinfo.objects.filter(profile=dictmatch[user_url])")
#     #print("f=open('AA/static/profile/%s/tree.json' %(user_url),'r') ")
#     #print(zero_time5-zero_time)
#     #print("#####################################################")
#     #article
#     ##############################################################################
#     ##############################################################################
#     #20210607!!!!!!!!!!!!!!!!
#     #必須去判斷id!!!!!!!! id介於甚麼數字下去選擇甚麼models!
#     #print("幹妳娘機掰!")
#     # modelid=int(user_listing.userurl.split('-')[-1])
#     # if modelid<1000:
#     #     articleinfo_qs=articleinfo_0to1000.objects.filter(profile=dictmatch[user_url])
#     # #print(user_listing.user_url)
#     # else:
#     articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url]) 
#     #articleinfo_qs=articleinfo.objects.filter(user_url=user_url)
    
#     #########20210619改!!!!!articleinfo需要加設primary key column
#     #####user_listing= Profile.objects.get(pk=searchid)

    


#     profile1=[]
#     for i in range(len(articleinfo_qs)):
#         profile1.append(user_url) 
#     journal=list(articleinfo_qs.values_list('journal', flat=True))
#     year=list(articleinfo_qs.values_list('year', flat=True))
#     title=list(articleinfo_qs.values_list('title', flat=True))
#     titleurl=[slugify(x) for x in title]
#     #author=list(articleinfo_qs.values_list('author', flat=True))
#     author=list(articleinfo_qs.values_list('authorabbr', flat=True))

#     author=["; ".join(x.split('#')) for x in author]
#     #print(author)
#     cite=list(articleinfo_qs.values_list('cite', flat=True))
#     # print("cite",cite)
#     cite1=[]
#     for x in cite:
#         try:
#             cite1.append(int(x))
#         except:
#             cite1.append(0)
#     abstract=list(articleinfo_qs.values_list('abstract', flat=True))


#     articlein=zip(profile1,journal,year,title,author,cite1,titleurl,abstract)

#     # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)
#     # print(len(profile1))

#     articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=True)[:10]

#     zero_time6=time.time()
    
#     #print("journal=list(articleinfo_qs.values_list('journal', flat=True))")
#     #print("articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url]):")
#     #print(zero_time6-zero_time)
#     #print("#####################################################")



#     connauthorinfo_qs=MapCoauthorinfo.objects.filter(profile=dictmatch[user_url])
#     #print(user_url)
#     #print(dictmatch[user_url])
#     #print(connauthorinfo_qs)
#     #print()
#     # print("幹幹幹!")
#     coauthorstr=list(connauthorinfo_qs.values_list('coauthor', flat=True))[0]
#     #print(coauthorstr.split('$')[0])
    
#     coauthorname=[]
#     coauthoraffi=[]
#     coauthoritem=[]
#     coauthorahref=[]
#     #   var tmp=NewArray[i].split("#")[0].split('&')[0];
#     #                     var tmp2=NewArray[i].split("#")[0].split('&')[1];
#     #                     var tmp1=tmp.split(" ").join("7").replace('.','_').replace(',','8');
#     #                     //var tmp1="test";
#     #                     var userurl='{{user_url}}';
#     #                     //console.log(userurl);
#     #                     var ttt='<a href= "http://127.0.0.1:8000/profile/'+userurl+'/network-affliation/'+tmp1+'">';
#     for k in range(len(coauthorstr.split('$'))):
#         coauthorname.append(coauthorstr.split('$')[k].split('#')[0].split('&')[0])
#         coauthoraffi.append(coauthorstr.split('$')[k].split('#')[0].split('&')[1])
#         coauthoritem.append(int(coauthorstr.split('$')[k].split('#')[-1]))
#         tmpname=coauthorstr.split('$')[k].split('#')[0].split('&')[0]
#         # print(tmpname.split(" "))
#         # ['Liao,', 'Y.-M']
#         # Liao87Y_-M
#         tmp1="7".join(tmpname.split(" ")).replace('.','_').replace(',','8')
        
#         coauthorahref.append("/profile/%s/network-coauthor/%s" %(userurl,tmp1))
    
#     coauthorzip=sorted(zip(coauthorname,coauthoraffi,coauthoritem,coauthorahref),key=lambda x: -x[2])[:10]

#     zero_time7=time.time()
    
#     #print("journal=list(articleinfo_qs.values_list('journal', flat=True))")
#     #print("connauthorinfo_qs=MapCoauthorinfo.objects.filter(profile=dictmatch[user_url])")
#     #print("for k in range(len(coauthorstr.split('$'))):")
#     #print(zero_time7-zero_time)
#     #print("#####################################################")

#     context = {
#             'user_listing':user_listing,
#             # 'citedata':citedata,
#             # 'docyear':docyear,
#             # 'ifdata':ifdata,
#             #'publisher':publisher,
#             'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
#             'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
#             'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
#             'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),
#             'cityinfo_json':cityinfo_json,
#             'conninfo_json':conninfo_json,
#             'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
#             # 'tree1_json':tree1_json,
#             'articlein':articlein,
#             'user_url':user_url,
#             'userurl':userurl,
#             'coauthorzip':coauthorzip,
#         }
    
#     return render(request, 'profile/profile_listing.html', context)


def profile(request, user_url):
    

    #user_listing = get_object_or_404(Profile, userurl=user_url)
    searchid=int(user_url.split("-")[-1])
    #user_listing = get_object_or_404(Profile, userurl=user_url)
    #print(len(Profile_test.objects.all()))
    zero_time=time.time()
    user_listing= Profile.objects.get(pk=searchid)
    
    checkurl=user_listing.user_url
    checkurl=checkurl.replace(checkurl.split('-')[-1],'')
     
    checkurl0=user_url.replace(user_url.split('-')[-1],'')
    if str(checkurl0) != str(checkurl):
        raise Http404("")


    #############20210904
    try:
        tmpcheck_listing=Profile_token.objects.get(userurl=user_url)
        check_token=float(tmpcheck_listing.token)
        check_first_name=tmpcheck_listing.user_first_name
        check_last_name=tmpcheck_listing.user_last_name
        check_institution=tmpcheck_listing.user_institution
        check_department=tmpcheck_listing.user_department
        check_email=tmpcheck_listing.user_email
        check_orcid=tmpcheck_listing.orcid
        check_gspi=tmpcheck_listing.gspi
        check_rcpi=tmpcheck_listing.rcpi
        referral_link=tmpcheck_listing.referral_link
        tmpcheck=1

        token=float(tmpcheck_listing.token)
        tmptoken=float(tmpcheck_listing.tmptoken)
        NFTToken = float(tmpcheck_listing.token) - float(tmpcheck_listing.tmptoken)

    except: 
        tmpcheck=0
        check_token=float(0)
        check_first_name=""
        check_last_name=""
        check_institution=""
        check_department=""
        check_email=""
        check_orcid=""
        check_gspi=""
        check_rcpi=""
        referral_link=""
        tmpcheck_listing=user_listing

        token=float(0)
        tmptoken=float(0)
        NFTToken=float(0)


    zero_time1=time.time()
    print(zero_time1-zero_time)
    print(user_listing.user_url)
    zero_time1=time.time()
    #print(zero_time1-zero_time)
    #print("get_object_or_404(Profile, userurl=user_url)")
    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    
    # ###################################################################################20210811
    # csvpath='static/scopus_match1.csv'
    # scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8', engine='python')

    # #print("pd.read_csv(csvpath,sep='\t',encoding='utf-8', engine='python')")
    # # print(scopusmatch.columns)
    # # print(scopusmatch['scopus'].values)
    # userurllist=scopusmatch['user_url'].values
    # scopuslist=scopusmatch['scopus'].values
    # dictmatch=dict(zip(userurllist,scopuslist))

    # userurllist1=userurllist
    # scopuslist1=scopuslist
    # scopuslist2=[x.replace('-',' ') for x in scopuslist1]
    # collabordict=dict(zip(scopuslist2,userurllist1))
    # ###################################################################################20210811
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')
    #zero_time3=time.time()
    
    #print("TrendCitaImpact.objects.filter(profile=dictmatch[user_url])")
    #print(zero_time3-zero_time)
    #print("#####################################################")
    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    #cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    #conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

    ######################20210103###################
    #ss=time.time()
    #cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    mapcity=user_listing.mapcity
    #newmapcity=country+'@'+lat+'@'+lon+'@'+countn+'@'+asso
    try:
        mapcity_country=mapcity.split('@')[0].split('$')
        mapcity_lat=mapcity.split('@')[1].split('$')
        mapcity_lat=[float(x) for x in mapcity_lat]
        mapcity_lon=mapcity.split('@')[2].split('$')
        mapcity_lon=[float(x) for x in mapcity_lon]
        mapcity_countn=mapcity.split('@')[3].split('$')
        mapcity_countn=[int(x) for x in mapcity_countn]
        mapcity_asso=mapcity.split('@')[4].split('*')
        mapcity_asso=[x.replace('\'','') for x in mapcity_asso]
    except:
        mapcity_country=[]
        mapcity_lat=[]
        mapcity_lon=[]
        mapcity_countn=[]
        mapcity_asso=[]
    # print(mapcity_country)
    # print(mapcity_lat)
    # print(mapcity_lon)
    # print(mapcity_countn)
    # print(mapcity_asso)
    ##########################################################################

    # mapcity
    # mapconn
    # mapcoau
    # coauthors
    #conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])
    #print(time.time()-ss)

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     tmpcityinfo=cityinfo_qs[i].asso
    #     #print(tmpcityinfo)
    #     cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
    #     countorigin.append(int(cityinfo_qs[i].countn))
    
    countorigin=mapcity_countn
    start = 3
    end = 6
    arr=countorigin
    arrnew=[]
    for x in arr:
        if int(x)>100:
            arrnew.append(int(100))
        else:
            arrnew.append(int(x))
    arr=arrnew
    if len(arr)>1:
        width = end - start
        maxarr=max(arr)
        if int(maxarr-min(arr))!=0:
            res=[(x-min(arr))/(maxarr-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        #res=arr
        res=[5] #20210718改

    #for i in range(len(cityinfo_qs)):
    #    cityinfo_qs[i].countn=res[i]
    mapcity_countn_new=res
    #print(mapcity_countn_new)
    #cityinfo_json_new=json.dumps(mapcity_country,mapcity_lat,mapcity_lon,mapcity_countn_new,mapcity_asso)
    #print(cityinfo_json_new)


    #cityinfo_json = serialize("json", cityinfo_qs)
    #conninfo_json = serialize("json", conninfo_qs)
    #等等來做這裡!!!
    newmapcity=[{'country': x1,'lat': x2,'lon': x3,'countn': x4, 'asso': x5} \
    for x1, x2, x3, x4, x5 in zip(mapcity_country, mapcity_lat, mapcity_lon, mapcity_countn_new, mapcity_asso)]
    #cityinfo_json_new=json.dumps([{'country': mapcity_country,'lat':mapcity_lat,'lon':mapcity_lon,'countn':mapcity_countn_new, 'asso': mapcity_asso}])
    cityinfo_json_new=json.dumps(newmapcity)


    

    mapconn=user_listing.mapconn
    #print("幹你娘")
    #print(mapconn)
    try:
        mapconn_long1=mapconn.split('@')[0].split('$')
        mapconn_long1=[float(x) for x in mapconn_long1]
        mapconn_long2=mapconn.split('@')[1].split('$')
        mapconn_long2=[float(x) for x in mapconn_long2]
        mapconn_lat1=mapconn.split('@')[2].split('$')
        mapconn_lat1=[float(x) for x in mapconn_lat1]
        mapconn_lat2=mapconn.split('@')[3].split('$')
        mapconn_lat2=[float(x) for x in mapconn_lat2]
    except:
        mapconn_long1=[]
        mapconn_long2=[]
        mapconn_lat1=[]
        mapconn_lat2=[]

    newmapconn=[{'long1': x1,'long2': x2,'lat1': x3,'lat2': x4} \
    for x1, x2, x3, x4 in zip(mapconn_long1, mapconn_long2, mapconn_lat1, mapconn_lat2)]
    conninfo_json_new=json.dumps(newmapconn)
    
    #f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r') 

    # f=open('AA/static/profile/%s/tree.json' %(user_url),'r') 
    # tree1_json=f.read()

    # f.close()
    #############################################################################################
    profile1=[]
    for i in range(len(user_listing.author.split('$')[0:10])):
        profile1.append(user_listing.user_url) 

    author=user_listing.authorabbr.split('$')[0:10]
    author1=user_listing.authorabbr.split('$')[0:10]
    title=user_listing.title.split('$')[0:10]
    journal=user_listing.journal.split('$')[0:10]
    year=user_listing.year.split('$')[0:10]

    titleurl=[slugify(x) for x in title]
    author=["; ".join(x.split('#')) for x in author]
    cite=user_listing.cite.split('$')[0:10]
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)

    abstract=user_listing.abstract.split('$')[0:10]
    artoropen=user_listing.artoropen.split('$')[0:10]
    volume=user_listing.volume.split('$')[0:10]
    issue=user_listing.issue.split('$')[0:10]
    pages=user_listing.pages.split('$')[0:10]
    languages=user_listing.languages.split('$')[0:10]
    publisher=user_listing.publisher.split('$')[0:10]
    doi=user_listing.doi.split('$')[0:10]
    titleslug=user_listing.titleslug.split('$')[0:10]
    
    articlein=zip(profile1,journal,year,title,author,cite1,titleurl,abstract,author1,artoropen,volume,\
    issue,pages,languages,publisher,doi,titleslug)

    articlein=list(articlein)

    ###################################################################################
    coauthor=user_listing.coauthor
    print("幹你娘機掰coauthor")
    try:
        coauthorname=coauthor.split('@')[0].split('#')
        #print("coauthorname:",coauthorname)
        coauthoraffi=coauthor.split('@')[1].split('#')
        coauthoritem=coauthor.split('@')[2].split('#')
        coauthoritem=[int(x) for x in coauthoritem]
        #coauthorahref=coauthor.split('@')[3].split('#')
        coauthorahref=['#' for x in coauthoritem ]
        coauthorahref1=coauthor.split('@')[4].split('*')
        coauthorahref2=[]
        for x in coauthorahref1:
            if x=="":
                coauthorahref2.append("#")
            else:
                coauthorahref2.append(x)
    except:
        coauthorname=[]
        coauthoraffi=[]
        coauthoritem=[]
        coauthorahref=[]
        coauthorahref2=[]
    # print(coauthor.split('@')[4])
    # print(coauthorahref2)
    # print(coauthor.split('@')[3])
    # print(coauthorahref)
    #coauthorname,coauthoraffi,coauthoritem,coauthorahref,coauthorahref2

    # connauthorinfo_qs=MapCoauthorinfo.objects.filter(profile=dictmatch[user_url])


    # coauthorstr=list(connauthorinfo_qs.values_list('coauthor', flat=True))[0:10]
    # print(coauthorstr)
    # coauthorname=[]
    # coauthoraffi=[]
    # coauthoritem=[]
    # coauthorahref=[]
    # coauthorahref2=[]

    # ####################################################################20210716改
    # for kk in range(len(coauthorstr)):
    #     if str(coauthorstr[kk])!='nan':
    #         for k in range(len(coauthorstr[kk].split('$'))):
    #             coauthorname.append(coauthorstr[kk].split('$')[k].split('#')[0].split('&')[0])
    #             try:
    #                 #user_listing=Profile.objects.get(user_url=dictmatch[coauthorstr[kk].split('$')[k].split('#')[0].split('&')[0]])
    #                 collabordict1=Profile.objects.get(user_url=collabordict[coauthorstr[kk].split('$')[k].split('#')[0].split('&')[0].replace('-',' ')])
    #                 coauthorahref2.append("/profile/%s" % collabordict1.userurl)
    #             except:
    #                 coauthorahref2.append('#')

    #             coauthoraffi.append(coauthorstr[kk].split('$')[k].split('#')[0].split('&')[1])
    #             coauthoritem.append(int(coauthorstr[kk].split('$')[k].split('#')[-1]))
    #             tmpname=coauthorstr[kk].split('$')[k].split('#')[0].split('&')[0]
    #             # print(tmpname.split(" "))
    #             # ['Liao,', 'Y.-M']
    #             # Liao87Y_-M
    #             tmp1="7".join(tmpname.split(" ")).replace('.','_').replace(',','8')
                
    #             coauthorahref.append("/profile/%s/network-coauthor/%s" %(userurl,tmp1))

    coauthorzip=sorted(zip(coauthorname,coauthoraffi,coauthoritem,coauthorahref,coauthorahref2),key=lambda x: -x[2])[:10]
    #print(coauthorzip)
    #zero_time7=time.time()
    ####################################################################20210716改

    #print("journal=list(articleinfo_qs.values_list('journal', flat=True))")
    #print("connauthorinfo_qs=MapCoauthorinfo.objects.filter(profile=dictmatch[user_url])")
    #print("for k in range(len(coauthorstr.split('$'))):")
    #print(zero_time7-zero_time)
    #print("#####################################################")

    if title[0]!='':
        articleinlen=1
    else:
        articleinlen=0

    ###############20210912
    try:
        qsnft=Pdfupload.objects.filter(email_address__icontains=request.user.email)
        if len(qsnft)>0:
            nfttitle=[]
            nfttitleurl=[]
            nfteach=[]
            nftcoll=0
            for x in range(len(qsnft)):
                qsnftemaillist=qsnft[x].nftpeopleemail
                qsnftdistribute=qsnft[x].nftdistribute
                qsnfttitle=qsnft[x].title
                qsnfttitleurl=qsnft[x].titleurl
                
                try:
                    qsindex=qsnftemaillist.index(qsnftemaillist)
                    eachnft=qsnftdistribute[qsindex]
                    nfttitle.append(qsnfttitle)
                    nfttitleurl.append(qsnfttitleurl)
                    nfteach.append(float(eachnft))
                    nftcoll+=1
                except:
                    pass
            
            nftzip=zip(nfttitle,nfteach,nfttitleurl)
            sumnft=sum(nfteach)
            
        else:
            nftzip=""
            sumnft=0
            nftcoll=0
    except:
        nftzip=""
        sumnft=0
        nftcoll=0

    #######################################################################
    #nft
    try:
        qsnftlist=nftlist.objects.filter(email_address=request.user.email)
        if len(qsnftlist)>0:
            nftlisttitle=[]
            nftlisttitleurl=[]
            nftlistq=[]
            nftlistp=[]
            for x in range(len(qsnftlist)):
                qsnftlistq=qsnftlist[x].quantity
                qsnftlisttitle=qsnftlist[x].title
                qsnftlisttitleurl=qsnftlist[x].titleurl
                qsnftlistp=qsnftlist[x].pricepernft
                nftlistq.append(qsnftlistq)
                nftlisttitle.append(qsnftlisttitle)
                nftlisttitleurl.append(qsnftlisttitleurl)
                nftlistp.append(qsnftlistp)

            nftlistzip=zip(nftlisttitle,nftlistq,nftlisttitleurl,nftlistp)
        else:
            nftlistzip=""
    except:
        nftlistzip=""

    try:
        qsnftbid=nftbid.objects.filter(email_address=request.user.email)
        if len(qsnftbid)>0:
            nftbidtitle=[]
            nftbidtitleurl=[]
            nftbidq=[]
            nftbidp=[]
            for x in range(len(qsnftbid)):
                qsnftbidq=qsnftbid[x].quantity
                qsnftbidtitle=qsnftbid[x].title
                qsnftbidtitleurl=qsnftbid[x].titleurl
                qsnftbidp=qsnftbid[x].pricepernft
                nftbidtitle.append(qsnftbidtitle)
                nftbidq.append(qsnftbidq)
                nftbidtitleurl.append(qsnftbidtitleurl)
                nftbidp.append(qsnftbidp)

            nftbidzip=zip(nftbidtitle,nftbidq,nftbidtitleurl,nftbidp)
        else:
            nftbidzip=""
    except:
        nftbidzip=""
    
    try:
        qsnftdonate=nftdonate.objects.filter(email_address=request.user.email)

        if len(qsnftdonate)>0:
            nftdonatetitle=[]
            nftdonatetitleurl=[]
            nftdonateq=[]
            for x in range(len(qsnftdonate)):
                qsnftdonateq=qsnftdonate[x].quantity
                qsnftdonatetitle=qsnftdonate[x].title
                qsnftdonatetitleurl=qsnftdonate[x].titleurl
                nftdonateq.append(qsnftdonateq)
                nftdonatetitle.append(qsnftdonatetitle)
                nftdonatetitleurl.append(qsnftdonatetitleurl)

            nftdonatezip=zip(nftdonatetitle,nftdonateq,nftdonatetitleurl)
        else:
            nftdonatezip=""   
    except:
        nftdonatezip="" 
        
    ####################################################20211015
    try:
        testcloudpath=r'/home/djangoadmin/pyapps/bestjobreviews/static/profile7/%s_cloud.json' %(user_url)
        f=open(testcloudpath)
        f.close()
        cloudpath='https://researchain.net/static/profile7/%s_cloud.json' %(user_url)
        #testresult="幹"
    except:
        cloudpath='https://researchain.net/static/profile/%s_cloud.json' %(user_url)

    try:
        testpath=r'/home/djangoadmin/pyapps/bestjobreviews/static/profile9/%s_publisher.csv' %(user_url)
        f=open(testpath)
        f.close()
        publishpath='https://researchain.net/static/profile9/%s_publisher.csv' %(user_url)
        #testresult="幹"
    except:
        publishpath='https://researchain.net/static/profile/%s_publisher.csv' %(user_url)

        

    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            #'publisher':publisher,
            # 'publish_datapath':'https://nyc3.digitaloceanspaces.com/rc-api/static/profile/%s/publisher.csv' %(user_url),
            # 'bubble_datapath':'https://nyc3.digitaloceanspaces.com/rc-api/static/profile/%s/bubble.json' %(user_url),
            # 'cloud_datapath':'https://nyc3.digitaloceanspaces.com/rc-api/static/profile/%s/cloud.json' %(user_url),
            # 'window_datapath':'https://nyc3.digitaloceanspaces.com/rc-api/static/profile/%s/window.json' %(user_url),
            #'publish_datapath':'https://researchain.net/static/profile/%s_publisher.csv' %(user_url),
            'publish_datapath':publishpath,
            'bubble_datapath':'https://researchain.net/static/profile/%s/bubble.json' %(user_url),
            #'cloud_datapath':'https://researchain.net/static/profile/%s_cloud.json' %(user_url),
            'cloud_datapath':cloudpath,
            'window_datapath':'https://researchain.net/static/profile/%s/window.json' %(user_url),
            #'cityinfo_json':cityinfo_json,
            #'conninfo_json':conninfo_json,
            # 'network_datapath':'https://nyc3.digitaloceanspaces.com/rc-api/static/profile/%s/net.json' %(user_url),
            'network_datapath':'https://researchain.net/static/profile/%s/net.json' %(user_url),
            # 'tree1_json':tree1_json,
            'articlein':articlein,
            'articleinlen':articleinlen,
            'user_url':user_url,
            'userurl':userurl,
            'coauthorzip':coauthorzip,
            'cityinfo_json_new':cityinfo_json_new,
            'conninfo_json_new':conninfo_json_new,
            'tmpcheck':tmpcheck,
            'check_token':check_token,
            'check_first_name':check_first_name,
            'check_last_name':check_last_name,
            'check_institution':check_institution,
            'check_department':check_department,
            'tmpcheck_listing':tmpcheck_listing,
            'check_email':check_email,
            'check_orcid':check_orcid,
            'check_gspi':check_gspi,
            'check_rcpi':check_rcpi,
            'referral_link':referral_link,
            #####
            'token':token,
            'tmptoken':tmptoken,
            'NFTToken':NFTToken,
            'nftzip':nftzip,
            'sumnft':sumnft,
            'nftcoll':nftcoll,
            'nftlistzip':nftlistzip,
            'nftbidzip':nftbidzip,
            'nftdonatezip':nftdonatezip,
                   
        }
    
    return render(request, 'profile/profile_listing.html', context)


def d_archive_listing(request, user_url):
    #user_listing = get_object_or_404(Profile, userurl=user_url)
    searchid=int(user_url.split("-")[-1])
    #user_listing = get_object_or_404(Profile, userurl=user_url)
    #print(len(Profile_test.objects.all()))
    zero_time=time.time()
    user_listing= Profile.objects.get(pk=searchid)
    
    checkurl=user_listing.user_url
    checkurl=checkurl.replace(checkurl.split('-')[-1],'')
     
    checkurl0=user_url.replace(user_url.split('-')[-1],'')
    if str(checkurl0) != str(checkurl):
        raise Http404("")


    #############20210904
    try:
        tmpcheck_listing=Profile_token.objects.get(userurl=user_url)
        check_token=float(tmpcheck_listing.token)
        check_first_name=tmpcheck_listing.user_first_name
        check_last_name=tmpcheck_listing.user_last_name
        check_institution=tmpcheck_listing.user_institution
        check_department=tmpcheck_listing.user_department
        check_email=tmpcheck_listing.user_email
        check_orcid=tmpcheck_listing.orcid
        check_gspi=tmpcheck_listing.gspi
        check_rcpi=tmpcheck_listing.rcpi
        referral_link=tmpcheck_listing.referral_link
        tmpcheck=1

        token=float(tmpcheck_listing.token)
        tmptoken=float(tmpcheck_listing.tmptoken)
        NFTToken = float(tmpcheck_listing.token) - float(tmpcheck_listing.tmptoken)
    except: 
        tmpcheck=0
        check_token=float(0)
        check_first_name=""
        check_last_name=""
        check_institution=""
        check_department=""
        check_email=""
        check_orcid=""
        check_gspi=""
        check_rcpi=""
        referral_link=""
        tmpcheck_listing=user_listing

        token=float(0)
        tmptoken=float(0)
        NFTToken=float(0)

    zero_time1=time.time()
    print(zero_time1-zero_time)
    print(user_listing.user_url)
    zero_time1=time.time()
    #print(zero_time1-zero_time)
    #print("get_object_or_404(Profile, userurl=user_url)")
    #user_url=user_listing.user_url
    #userurl=user_listing.userurl

    try:
        xxx=Profile_token.objects.get(userurl=user_url)
        useremail=xxx.user_email
        #pdfupload=Pdfupload.objects.filter(email_address__icontains=useremail)
        pdfupload=Pdfupload.objects.filter(Q(uploadauthor=useremail) | Q(email_address__icontains=useremail))
        if len(pdfupload)>0:
            title=[]
            titleurl=[]
            abstract=[]
            #first_name=[]
            #last_name=[]
            name=[]

            for x in range(len(pdfupload)):
                title.append(pdfupload[x].title)
                titleurl.append(pdfupload[x].titleurl)
                abstract.append(pdfupload[x].abstract)
                #要改
                zipname=zip(pdfupload[x].first_name.split("#"),pdfupload[x].last_name.split('#'))
                tmpname=[]
                for x1,x2 in zipname:
                    tmpname.append(x1+' '+x2)
                newtmpname="; ".join(tmpname)    
                #name.append(pdfupload[x].first_name+' '+pdfupload.last_name)
                name.append(newtmpname)

                authorzip=zip(title,titleurl,abstract,name)
        else:
            authorzip=zip([],[],[],[])
    except:
        authorzip=zip([],[],[],[])
        

    ###################################################################################################
    ###################################################################################################
    ###############20210912
    try:
        qsnft=Pdfupload.objects.filter(email_address__icontains=request.user.email)
        if len(qsnft)>0:
            nfttitle=[]
            nfttitleurl=[]
            nfteach=[]
            nftcoll=0
            for x in range(len(qsnft)):
                qsnftemaillist=qsnft[x].nftpeopleemail
                qsnftdistribute=qsnft[x].nftdistribute
                qsnfttitle=qsnft[x].title
                qsnfttitleurl=qsnft[x].titleurl
                
                try:
                    qsindex=qsnftemaillist.index(qsnftemaillist)
                    eachnft=qsnftdistribute[qsindex]
                    nfttitle.append(qsnfttitle)
                    nfttitleurl.append(qsnfttitleurl)
                    nfteach.append(float(eachnft))
                    nftcoll+=1
                except:
                    pass
            
            nftzip=zip(nfttitle,nfteach,nfttitleurl)
            sumnft=sum(nfteach)
            
        else:
            nftzip=""
            sumnft=0
            nftcoll=0
    except:
        nftzip=""
        sumnft=0
        nftcoll=0

    #######################################################################
    #nft
    try:
        qsnftlist=nftlist.objects.filter(email_address=request.user.email)
        if len(qsnftlist)>0:
            nftlisttitle=[]
            nftlisttitleurl=[]
            nftlistq=[]
            nftlistp=[]
            for x in range(len(qsnftlist)):
                qsnftlistq=qsnftlist[x].quantity
                qsnftlisttitle=qsnftlist[x].title
                qsnftlisttitleurl=qsnftlist[x].titleurl
                qsnftlistp=qsnftlist[x].pricepernft
                nftlistq.append(qsnftlistq)
                nftlisttitle.append(qsnftlisttitle)
                nftlisttitleurl.append(qsnftlisttitleurl)
                nftlistp.append(qsnftlistp)

            nftlistzip=zip(nftlisttitle,nftlistq,nftlisttitleurl,nftlistp)
        else:
            nftlistzip=""
    except:
        nftlistzip=""

    try:
        qsnftbid=nftbid.objects.filter(email_address=request.user.email)
        if len(qsnftbid)>0:
            nftbidtitle=[]
            nftbidtitleurl=[]
            nftbidq=[]
            nftbidp=[]
            for x in range(len(qsnftbid)):
                qsnftbidq=qsnftbid[x].quantity
                qsnftbidtitle=qsnftbid[x].title
                qsnftbidtitleurl=qsnftbid[x].titleurl
                qsnftbidp=qsnftbid[x].pricepernft
                nftbidtitle.append(qsnftbidtitle)
                nftbidq.append(qsnftbidq)
                nftbidtitleurl.append(qsnftbidtitleurl)
                nftbidp.append(qsnftbidp)

            nftbidzip=zip(nftbidtitle,nftbidq,nftbidtitleurl,nftbidp)
        else:
            nftbidzip=""
    except:
        nftbidzip=""
    
    try:
        qsnftdonate=nftdonate.objects.filter(email_address=request.user.email)

        if len(qsnftdonate)>0:
            nftdonatetitle=[]
            nftdonatetitleurl=[]
            nftdonateq=[]
            for x in range(len(qsnftdonate)):
                qsnftdonateq=qsnftdonate[x].quantity
                qsnftdonatetitle=qsnftdonate[x].title
                qsnftdonatetitleurl=qsnftdonate[x].titleurl
                nftdonateq.append(qsnftdonateq)
                nftdonatetitle.append(qsnftdonatetitle)
                nftdonatetitleurl.append(qsnftdonatetitleurl)

            nftdonatezip=zip(nftdonatetitle,nftdonateq,nftdonatetitleurl)
        else:
            nftdonatezip=""   
    except:
        nftdonatezip=""

    # qsnft=Pdfupload.objects.filter(email_address__icontains=request.user.email)
    # if len(qsnft)>0:
    #     nfttitle=[]
    #     nfttitleurl=[]
    #     nfteach=[]
    #     nftcoll=0
    #     for x in range(len(qsnft)):
    #         qsnftemaillist=qsnft[x].nftpeopleemail
    #         qsnftdistribute=qsnft[x].nftdistribute
    #         qsnfttitle=qsnft[x].title
    #         qsnfttitleurl=qsnft[x].titleurl
            
    #         try:
    #             qsindex=qsnftemaillist.index(qsnftemaillist)
    #             eachnft=qsnftdistribute[qsindex]
    #             nfttitle.append(qsnfttitle)
    #             nfttitleurl.append(qsnfttitleurl)
    #             nfteach.append(float(eachnft))
    #             nftcoll+=1
    #         except:
    #             pass
        
    #     nftzip=zip(nfttitle,nfteach,nfttitleurl)
    #     sumnft=sum(nfteach)
        
    # else:
    #     nftzip=""
    #     sumnft=0
    #     nftcoll=0

    # #######################################################################
    # #nft
    # qsnftlist=nftlist.objects.filter(email_address=request.user.email)
    # if len(qsnftlist)>0:
    #     nftlisttitle=[]
    #     nftlisttitleurl=[]
    #     nftlistq=[]
    #     nftlistp=[]
    #     for x in range(len(qsnftlist)):
    #         qsnftlistq=qsnftlist[x].quantity
    #         qsnftlisttitle=qsnftlist[x].title
    #         qsnftlisttitleurl=qsnftlist[x].titleurl
    #         qsnftlistp=qsnftlist[x].pricepernft
    #         nftlistq.append(qsnftlistq)
    #         nftlisttitle.append(qsnftlisttitle)
    #         nftlisttitleurl.append(qsnftlisttitleurl)
    #         nftlistp.append(qsnftlistp)

    #     nftlistzip=zip(nftlisttitle,nftlistq,nftlisttitleurl,nftlistp)
    # else:
    #     nftlistzip=""

    # qsnftbid=nftbid.objects.filter(email_address=request.user.email)
    # if len(qsnftbid)>0:
    #     nftbidtitle=[]
    #     nftbidtitleurl=[]
    #     nftbidq=[]
    #     nftbidp=[]
    #     for x in range(len(qsnftbid)):
    #         qsnftbidq=qsnftbid[x].quantity
    #         qsnftbidtitle=qsnftbid[x].title
    #         qsnftbidtitleurl=qsnftbid[x].titleurl
    #         qsnftbidp=qsnftbid[x].pricepernft
    #         nftbidtitle.append(qsnftbidtitle)
    #         nftbidq.append(qsnftbidq)
    #         nftbidtitleurl.append(qsnftbidtitleurl)
    #         nftbidp.append(qsnftbidp)

    #     nftbidzip=zip(nftbidtitle,nftbidq,nftbidtitleurl,nftbidp)
    # else:
    #     nftbidzip=""
    
    # qsnftdonate=nftdonate.objects.filter(email_address=request.user.email)

    # if len(qsnftdonate)>0:
    #     nftdonatetitle=[]
    #     nftdonatetitleurl=[]
    #     nftdonateq=[]
    #     for x in range(len(qsnftdonate)):
    #         qsnftdonateq=qsnftdonate[x].quantity
    #         qsnftdonatetitle=qsnftdonate[x].title
    #         qsnftdonatetitleurl=qsnftdonate[x].titleurl
    #         nftdonateq.append(qsnftdonateq)
    #         nftdonatetitle.append(qsnftdonatetitle)
    #         nftdonatetitleurl.append(qsnftdonatetitleurl)

    #     nftdonatezip=zip(nftdonatetitle,nftdonateq,nftdonatetitleurl)
    # else:
    #     nftdonatezip="" 


    context = {
            'authorzip':authorzip,
            'user_listing':user_listing,
            # # 'citedata':citedata,
            # # 'docyear':docyear,
            # # 'ifdata':ifdata,
            # #'publisher':publisher,
            # # 'publish_datapath':'https://nyc3.digitaloceanspaces.com/rc-api/static/profile/%s/publisher.csv' %(user_url),
            # # 'bubble_datapath':'https://nyc3.digitaloceanspaces.com/rc-api/static/profile/%s/bubble.json' %(user_url),
            # # 'cloud_datapath':'https://nyc3.digitaloceanspaces.com/rc-api/static/profile/%s/cloud.json' %(user_url),
            # # 'window_datapath':'https://nyc3.digitaloceanspaces.com/rc-api/static/profile/%s/window.json' %(user_url),
            # 'publish_datapath':'https://researchain.net/static/profile/%s_publisher.csv' %(user_url),
            # 'bubble_datapath':'https://researchain.net/static/profile/%s/bubble.json' %(user_url),
            # 'cloud_datapath':'https://researchain.net/static/profile/%s_cloud.json' %(user_url),
            # 'window_datapath':'https://researchain.net/static/profile/%s/window.json' %(user_url),
            # #'cityinfo_json':cityinfo_json,
            # #'conninfo_json':conninfo_json,
            # # 'network_datapath':'https://nyc3.digitaloceanspaces.com/rc-api/static/profile/%s/net.json' %(user_url),
            # 'network_datapath':'https://researchain.net/static/profile/%s/net.json' %(user_url),
            # # 'tree1_json':tree1_json,
            # 'articlein':articlein,
            # 'articleinlen':articleinlen,
            #'user_url':user_url,
            #'userurl':userurl,
            # 'coauthorzip':coauthorzip,
            # 'cityinfo_json_new':cityinfo_json_new,
            # 'conninfo_json_new':conninfo_json_new,
            'tmpcheck':tmpcheck,
            'check_token':check_token,
            'check_first_name':check_first_name,
            'check_last_name':check_last_name,
            'check_institution':check_institution,
            'check_department':check_department,
            'tmpcheck_listing':tmpcheck_listing,
            'check_email':check_email,
            'check_orcid':check_orcid,
            'check_gspi':check_gspi,
            'check_rcpi':check_rcpi,
            'referral_link':referral_link,
            #####
            'token':token,
            'tmptoken':tmptoken,
            'NFTToken':NFTToken,
            'nftzip':nftzip,
            'sumnft':sumnft,
            'nftcoll':nftcoll,
            'nftlistzip':nftlistzip,
            'nftbidzip':nftbidzip,
            'nftdonatezip':nftdonatezip,
        }
    
    return render(request, 'profile/d_archive_listing.html', context)



def publication_listing(request, user_url):

    zero_time=time.time()

    #user_listing = get_object_or_404(Profile, userurl=user_url)
    searchid=int(user_url.split("-")[-1])

    #user_listing = get_object_or_404(Profile, userurl=user_url)
    #print(len(Profile_test.objects.all()))
    user_listing= Profile.objects.get(pk=searchid)
    #print("e04")
    print(user_listing.user_url)

    zero_time1=time.time()
    #print(zero_time1-zero_time)
    #print("get_object_or_404(Profile, userurl=user_url)")
    #print(zero_time1-zero_time)
    #print("#####################################################")
    try:
        tmpcheck_listing=Profile_token.objects.get(userurl=user_url)
        check_token=float(tmpcheck_listing.token)
        check_first_name=tmpcheck_listing.user_first_name
        check_last_name=tmpcheck_listing.user_last_name
        check_institution=tmpcheck_listing.user_institution
        check_department=tmpcheck_listing.user_department
        check_email=tmpcheck_listing.user_email
        check_orcid=tmpcheck_listing.orcid
        check_gspi=tmpcheck_listing.gspi
        check_rcpi=tmpcheck_listing.rcpi
        referral_link=tmpcheck_listing.referral_link
        tmpcheck=1

        token=float(tmpcheck_listing.token)
        tmptoken=float(tmpcheck_listing.tmptoken)
        NFTToken = float(tmpcheck_listing.token) - float(tmpcheck_listing.tmptoken)
        
    except: 
        tmpcheck=0
        check_token=float(0)
        check_first_name=""
        check_last_name=""
        check_institution=""
        check_department=""
        check_email=""
        check_orcid=""
        check_gspi=""
        check_rcpi=""
        referral_link=""
        tmpcheck_listing=user_listing

        token=float(0)
        tmptoken=float(0)
        NFTToken=float(0)


    user_url=user_listing.user_url
    userurl=user_listing.userurl

    # print(user_url)
    # print(user_listing)

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    

    # csvpath='static/scopus_match1.csv'
    # scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8', engine='python')

    # zero_time2=time.time()

    # userurllist=scopusmatch['user_url'].values
    # scopuslist=scopusmatch['scopus'].values
    # dictmatch=dict(zip(userurllist,scopuslist))
    
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')
    zero_time3=time.time()
    
    #print("TrendCitaImpact.objects.filter(profile=dictmatch[user_url])")
    #print(zero_time3-zero_time)
    #print("#####################################################")
    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    # cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

 


    
    #f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r') 

    # f=open('AA/static/profile/%s/tree.json' %(user_url),'r') 
    # tree1_json=f.read()

    # f.close()
    zero_time5=time.time()
    
    #print("MapCityinfo.objects.filter(profile=dictmatch[user_url])")
    #print("f=open('AA/static/profile/%s/tree.json' %(user_url),'r') ")
    #print(zero_time5-zero_time)

    profile1=[]
    for i in range(len(user_listing.author.split('$'))):
        profile1.append(user_listing.user_url) 

    author=user_listing.authorabbr.split('$')
    author1=user_listing.authorabbr.split('$')
    title=user_listing.title.split('$')
    journal=user_listing.journal.split('$')
    year=user_listing.year.split('$')

    titleurl=[slugify(x) for x in title]
    author=["; ".join(x.split('#')) for x in author]
    cite=user_listing.cite.split('$')
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)

    abstract=user_listing.abstract.split('$')
    artoropen=user_listing.artoropen.split('$')
    volume=user_listing.volume.split('$')
    issue=user_listing.issue.split('$')
    pages=user_listing.pages.split('$')
    languages=user_listing.languages.split('$')
    publisher=user_listing.publisher.split('$')
    doi=user_listing.doi.split('$')
    titleslug=user_listing.titleslug.split('$')
    # citeyear=user_listing.citeyear.split('$')
    # try:
    #     citeyear=[int(x) for x in citeyear.split("#")]
    # except:
    #     citeyear=[0,0,0,0,0]
    # citeyear=list(articleinfo_qs.values_list('citeyear', flat=True))[0]

    articlein=zip(profile1,journal,year,title,author,cite1,titleurl,abstract,author1,artoropen,volume,\
    issue,pages,languages,publisher,doi,titleslug)


    # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)
    # print(len(profile1))

    articlein=list(articlein)

    #print(articlein)
    print(abstract)

    paginator = Paginator(articlein, 10)
    page = request.GET.get('page')
    paged_articlein = paginator.get_page(page)


    ###############20210912
    try:
        qsnft=Pdfupload.objects.filter(email_address__icontains=request.user.email)
        if len(qsnft)>0:
            nfttitle=[]
            nfttitleurl=[]
            nfteach=[]
            nftcoll=0
            for x in range(len(qsnft)):
                qsnftemaillist=qsnft[x].nftpeopleemail
                qsnftdistribute=qsnft[x].nftdistribute
                qsnfttitle=qsnft[x].title
                qsnfttitleurl=qsnft[x].titleurl
                
                try:
                    qsindex=qsnftemaillist.index(qsnftemaillist)
                    eachnft=qsnftdistribute[qsindex]
                    nfttitle.append(qsnfttitle)
                    nfttitleurl.append(qsnfttitleurl)
                    nfteach.append(float(eachnft))
                    nftcoll+=1
                except:
                    pass
            
            nftzip=zip(nfttitle,nfteach,nfttitleurl)
            sumnft=sum(nfteach)
            
        else:
            nftzip=""
            sumnft=0
            nftcoll=0
    except:
        nftzip=""
        sumnft=0
        nftcoll=0

    #######################################################################
    #nft
    try:
        qsnftlist=nftlist.objects.filter(email_address=request.user.email)
        if len(qsnftlist)>0:
            nftlisttitle=[]
            nftlisttitleurl=[]
            nftlistq=[]
            nftlistp=[]
            for x in range(len(qsnftlist)):
                qsnftlistq=qsnftlist[x].quantity
                qsnftlisttitle=qsnftlist[x].title
                qsnftlisttitleurl=qsnftlist[x].titleurl
                qsnftlistp=qsnftlist[x].pricepernft
                nftlistq.append(qsnftlistq)
                nftlisttitle.append(qsnftlisttitle)
                nftlisttitleurl.append(qsnftlisttitleurl)
                nftlistp.append(qsnftlistp)

            nftlistzip=zip(nftlisttitle,nftlistq,nftlisttitleurl,nftlistp)
        else:
            nftlistzip=""
    except:
        nftlistzip=""

    try:
        qsnftbid=nftbid.objects.filter(email_address=request.user.email)
        if len(qsnftbid)>0:
            nftbidtitle=[]
            nftbidtitleurl=[]
            nftbidq=[]
            nftbidp=[]
            for x in range(len(qsnftbid)):
                qsnftbidq=qsnftbid[x].quantity
                qsnftbidtitle=qsnftbid[x].title
                qsnftbidtitleurl=qsnftbid[x].titleurl
                qsnftbidp=qsnftbid[x].pricepernft
                nftbidtitle.append(qsnftbidtitle)
                nftbidq.append(qsnftbidq)
                nftbidtitleurl.append(qsnftbidtitleurl)
                nftbidp.append(qsnftbidp)

            nftbidzip=zip(nftbidtitle,nftbidq,nftbidtitleurl,nftbidp)
        else:
            nftbidzip=""
    except:
        nftbidzip=""
    
    try:
        qsnftdonate=nftdonate.objects.filter(email_address=request.user.email)

        if len(qsnftdonate)>0:
            nftdonatetitle=[]
            nftdonatetitleurl=[]
            nftdonateq=[]
            for x in range(len(qsnftdonate)):
                qsnftdonateq=qsnftdonate[x].quantity
                qsnftdonatetitle=qsnftdonate[x].title
                qsnftdonatetitleurl=qsnftdonate[x].titleurl
                nftdonateq.append(qsnftdonateq)
                nftdonatetitle.append(qsnftdonatetitle)
                nftdonatetitleurl.append(qsnftdonatetitleurl)

            nftdonatezip=zip(nftdonatetitle,nftdonateq,nftdonatetitleurl)
        else:
            nftdonatezip=""   
    except:
        nftdonatezip=""
    # qsnft=Pdfupload.objects.filter(email_address__icontains=request.user.email)
    # if len(qsnft)>0:
    #     nfttitle=[]
    #     nfttitleurl=[]
    #     nfteach=[]
    #     nftcoll=0
    #     for x in range(len(qsnft)):
    #         qsnftemaillist=qsnft[x].nftpeopleemail
    #         qsnftdistribute=qsnft[x].nftdistribute
    #         qsnfttitle=qsnft[x].title
    #         qsnfttitleurl=qsnft[x].titleurl
            
    #         try:
    #             qsindex=qsnftemaillist.index(qsnftemaillist)
    #             eachnft=qsnftdistribute[qsindex]
    #             nfttitle.append(qsnfttitle)
    #             nfttitleurl.append(qsnfttitleurl)
    #             nfteach.append(float(eachnft))
    #             nftcoll+=1
    #         except:
    #             pass
        
    #     nftzip=zip(nfttitle,nfteach,nfttitleurl)
    #     sumnft=sum(nfteach)
        
    # else:
    #     nftzip=""
    #     sumnft=0
    #     nftcoll=0

    # #######################################################################
    # #nft
    # qsnftlist=nftlist.objects.filter(email_address=request.user.email)
    # if len(qsnftlist)>0:
    #     nftlisttitle=[]
    #     nftlisttitleurl=[]
    #     nftlistq=[]
    #     nftlistp=[]
    #     for x in range(len(qsnftlist)):
    #         qsnftlistq=qsnftlist[x].quantity
    #         qsnftlisttitle=qsnftlist[x].title
    #         qsnftlisttitleurl=qsnftlist[x].titleurl
    #         qsnftlistp=qsnftlist[x].pricepernft
    #         nftlistq.append(qsnftlistq)
    #         nftlisttitle.append(qsnftlisttitle)
    #         nftlisttitleurl.append(qsnftlisttitleurl)
    #         nftlistp.append(qsnftlistp)

    #     nftlistzip=zip(nftlisttitle,nftlistq,nftlisttitleurl,nftlistp)
    # else:
    #     nftlistzip=""

    # qsnftbid=nftbid.objects.filter(email_address=request.user.email)
    # if len(qsnftbid)>0:
    #     nftbidtitle=[]
    #     nftbidtitleurl=[]
    #     nftbidq=[]
    #     nftbidp=[]
    #     for x in range(len(qsnftbid)):
    #         qsnftbidq=qsnftbid[x].quantity
    #         qsnftbidtitle=qsnftbid[x].title
    #         qsnftbidtitleurl=qsnftbid[x].titleurl
    #         qsnftbidp=qsnftbid[x].pricepernft
    #         nftbidtitle.append(qsnftbidtitle)
    #         nftbidq.append(qsnftbidq)
    #         nftbidtitleurl.append(qsnftbidtitleurl)
    #         nftbidp.append(qsnftbidp)

    #     nftbidzip=zip(nftbidtitle,nftbidq,nftbidtitleurl,nftbidp)
    # else:
    #     nftbidzip=""
    
    # qsnftdonate=nftdonate.objects.filter(email_address=request.user.email)

    # if len(qsnftdonate)>0:
    #     nftdonatetitle=[]
    #     nftdonatetitleurl=[]
    #     nftdonateq=[]
    #     for x in range(len(qsnftdonate)):
    #         qsnftdonateq=qsnftdonate[x].quantity
    #         qsnftdonatetitle=qsnftdonate[x].title
    #         qsnftdonatetitleurl=qsnftdonate[x].titleurl
    #         nftdonateq.append(qsnftdonateq)
    #         nftdonatetitle.append(qsnftdonatetitle)
    #         nftdonatetitleurl.append(qsnftdonatetitleurl)

    #     nftdonatezip=zip(nftdonatetitle,nftdonateq,nftdonatetitleurl)
    # else:
    #     nftdonatezip=""

    try:
        testpath=r'/home/djangoadmin/pyapps/bestjobreviews/static/profile9/%s_publisher.csv' %(user_url)
        f=open(testpath)
        f.close()
        publishpath='https://researchain.net/static/profile9/%s_publisher.csv' %(user_url)
        #testresult="幹"
    except:
        publishpath='https://researchain.net/static/profile/%s_publisher.csv' %(user_url)
 

    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            #'publisher':publisher,
            # 'publish_datapath':'https://nyc3.digitaloceanspaces.com/rc-api/static/profile/%s/publisher.csv' %(user_url),
            # 'bubble_datapath':'https://nyc3.digitaloceanspaces.com/rc-api/static/profile/%s/bubble.json' %(user_url),
            # 'cloud_datapath':'https://nyc3.digitaloceanspaces.com/rc-api/static/profile/%s/cloud.json' %(user_url),
            # 'window_datapath':'https://nyc3.digitaloceanspaces.com/rc-api/static/profile/%s/window.json' %(user_url),
            #'publish_datapath':'https://researchain.net/static/profile/%s_publisher.csv' %(user_url),
            'publish_datapath':publishpath,
            'bubble_datapath':'https://researchain.net/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'https://researchain.net/static/profile/%s_cloud.json' %(user_url),
            'window_datapath':'https://researchain.net/static/profile/%s/window.json' %(user_url),
            #'cityinfo_json':cityinfo_json,
            #'conninfo_json':conninfo_json,
            # 'network_datapath':'https://nyc3.digitaloceanspaces.com/rc-api/static/profile/%s/net.json' %(user_url),
            'network_datapath':'https://researchain.net/static/profile/%s/net.json' %(user_url),
            # 'tree1_json':tree1_json,
            'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,
            #'coauthorzip':coauthorzip,
            'paged_articlein':paged_articlein,
            'tmpcheck':tmpcheck,
            'check_token':check_token,
            'check_first_name':check_first_name,
            'check_last_name':check_last_name,
            'check_institution':check_institution,
            'check_department':check_department,
            'tmpcheck_listing':tmpcheck_listing,
            'check_email':check_email,
            'check_orcid':check_orcid,
            'check_gspi':check_gspi,
            'check_rcpi':check_rcpi,
            'referral_link':referral_link,
            #####
            'token':token,
            'tmptoken':tmptoken,
            'NFTToken':NFTToken,
            'nftzip':nftzip,
            'sumnft':sumnft,
            'nftcoll':nftcoll,
            'nftlistzip':nftlistzip,
            'nftbidzip':nftbidzip,
            'nftdonatezip':nftdonatezip,
        }
    
    return render(request, 'profile/publication_listings.html', context)

def save_create(request):
    print("幹你娘!!!!!!!!!!!!!!!!")
    if request.method == 'POST':
        #save_create = request.POST.get('save_create',"")
        checkemail= request.POST.get('checkemail',"")
        xx=Profile_token.objects.get(user_email=checkemail)
        xx.create_index=1
        xx.save()
    
    return redirect('onboarding')

def save_orcid(request):
    if request.is_ajax(): 
        titleurl = request.POST.get('titleurl', "")
        orcid= request.POST.get('orcid', "")
        email=request.POST.get('email', "")
        
        xx=Profile_token.objects.get(user_email=email)
        if orcid !='':
            xx.orcid=orcid
            xx.save()
        
        return redirect('profile',title_url=titleurl)

def save_gspi(request):
    #if request.is_ajax(): 
    if request.method == 'POST':
        userurl = request.POST.get('userurl', "")
        gspi= request.POST.get('gspi', "")
        email=request.POST.get('email', "")
        xx=Profile_token.objects.get(user_email=email)
        if gspi !='':
            if 'scholar.google.com' in gspi:
                xx.gspi=gspi
                xx.save()
            else:
                pass
                #raise ValidationError('Only urls from google scholar allowed')
        return redirect('profile',user_url=userurl)

def save_gspi_onboarding(request):
    #if request.is_ajax(): 
    if request.method == 'POST':
        userurl = request.POST.get('userurl', "")
        gspi= request.POST.get('gspi', "")
        email=request.POST.get('email', "")
        xx=Profile_token.objects.get(user_email=email)
        if gspi !='':
            if 'scholar.google.com' in gspi:
                xx.gspi=gspi
                xx.save()
            else:
                pass
                #raise ValidationError('Only urls from google scholar allowed')
        return redirect('onboarding')

def save_gspi_referral(request):
    #if request.is_ajax(): 
    if request.method == 'POST':
        userurl = request.POST.get('userurl', "")
        gspi= request.POST.get('gspi', "")
        email=request.POST.get('email', "")
        xx=Profile_token.objects.get(user_email=email)
        if gspi !='':
            if 'scholar.google.com' in gspi:
                xx.gspi=gspi
                xx.save()
            else:
                pass
                #raise ValidationError('Only urls from google scholar allowed')
        #return redirect('profile',user_url=userurl)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def save_rcpi(request):
    #if request.is_ajax(): 
    if request.method == 'POST':
        userurl = request.POST.get('userurl', "")
        rcpi= request.POST.get('rcpi', "")
        email=request.POST.get('email', "")
        xx=Profile_token.objects.get(user_email=email)
        if rcpi !='':
            if 'https://www.researchgate.net/' in rcpi:
                #   raise ValidationError('Only urls from RG allowed')
                xx.rcpi=rcpi
                xx.save()
            else:
                pass
                #raise ValidationError('Only urls from researchgate allowed')
        return redirect('profile',user_url=userurl)

def save_rcpi_onboarding(request):
    #if request.is_ajax(): 
    if request.method == 'POST':
        userurl = request.POST.get('userurl', "")
        rcpi= request.POST.get('rcpi', "")
        email=request.POST.get('email', "")
        xx=Profile_token.objects.get(user_email=email)
        if rcpi !='':
            if 'https://www.researchgate.net/' in rcpi:
                #   raise ValidationError('Only urls from RG allowed')
                xx.rcpi=rcpi
                xx.save()
            else:
                pass
                #raise ValidationError('Only urls from researchgate allowed')
        return redirect('onboarding')

def save_rcpi_referral(request):
    #if request.is_ajax(): 
    if request.method == 'POST':
        userurl = request.POST.get('userurl', "")
        rcpi= request.POST.get('rcpi', "")
        email=request.POST.get('email', "")
        xx=Profile_token.objects.get(user_email=email)
        if rcpi !='':
            if 'https://www.researchgate.net/' in rcpi:
                #   raise ValidationError('Only urls from RG allowed')
                xx.rcpi=rcpi
                xx.save()
            else:
                pass
                #raise ValidationError('Only urls from researchgate allowed')
        #return redirect('profile',user_url=userurl)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def save_orcid_onboard(request):
    if request.is_ajax(): 

        orcid= request.POST.get('orcid', "")
        email=request.POST.get('email', "")
        
        xx=Profile_token.objects.get(user_email=email)
        if orcid !='':
            xx.orcid=orcid
            xx.save()
        
        return redirect('onboarding')


def save_profile(request):

     if request.method == 'POST':

        user_email = request.POST.get('checkemail')
        user_ahref = request.POST.get('checkahref')
        # user_first_name = request.POST.get('user_first_name')
        # user_last_name = request.POST.get('user_last_name')
        # user_institution = request.POST.get('user_institution')
        # user_department = request.POST.get('user_department')
        xxx=Profile_token.objects.get(user_email=request.user.email)
        xxx.userurl=user_ahref
        
        querylist=scopusmatch1.objects.exclude(ischeck=1).filter(userurl=user_ahref)
        if len(querylist)>0:
            queryxx=querylist[0]
            queryxx.ischeck=1
            queryxx.save()
            ###認領
            xxx.save()

        else:
            redirect('onboarding')
        #return render(request, 'profile/onboarding.html', context)
        return redirect('profile',user_url=user_ahref)

def onboard(request):

    if request.user.is_authenticated:

        Create_Email=Profile_token.objects.filter(user_email=request.user.email)
        ##20210903這裡也要改新model
 
        if len(Create_Email) == 0: 

            if request.method == 'POST':

                user_email = request.POST.get('user_email')
                user_first_name = request.POST.get('user_first_name')
                user_last_name = request.POST.get('user_last_name')
                user_institution = request.POST.get('user_institution')
                user_department = request.POST.get('user_department')

                # user_middle_name = request.POST.get('user_middle_name')
                # user_position = request.POST.get('user_position')
                # google_scholar = request.POST.get('google_scholar')
                # researchgate = request.POST.get('researchgate')
                # other = request.POST.get('other')


                # tmpuserurl='-'.join([x.capitalize() for x in slugify(user_first_name+' '+user_last_name).split('-')])

                # if len(Profile.objects.filter(user_url__startswith=tmpuserurl))==0:
                #     user_url=tmpuserurl
                # elif len(Profile.objects.filter(user_url__startswith=tmpuserurl))==1:
                #     user_url=tmpuserurl+'-'+'1'
                # elif len(Profile.objects.filter(user_url__startswith=tmpuserurl))==2:
                #     user_url=tmpuserurl+'-'+'2'
                # elif len(Profile.objects.filter(user_url__startswith=tmpuserurl))==3:
                #     user_url=tmpuserurl+'-'+'3'
                # #####以此類推
                # else:
                #     pass

                

                ####20210814改
                #user = User.objects.get(email=request.user.email)
                #user_id = user.id
                #print(user_id)
                profile = Referral.objects.get(user__email=request.user.email)
                #Referral.objects.filter(user__email="stu5737@gmail.com")
                profile_code = profile.code
                

                print(profile_code)
                #"https://researchain.net/referal/"
                referral_link=profile_code
                print("#####################################")
                print('####################################')
                print("登入的人的拿到的推薦碼:",request.user.first_name)
                if len(request.user.first_name)>0:

                    other_referral_link=request.user.first_name
                    token=float(11)
                    tmptoken=float(11)
                    #########################
                    try:
                        referralemail=Referral.objects.get(code=other_referral_link).user.email
                        print("rederral email is:",referralemail)
                        xxx=Profile_token.objects.get(user_email=referralemail)
                        print("推薦人",xxx)
                        xxx.tmptoken=float(xxx.tmptoken)+float(4)
                        xxx.token=float(xxx.token)+float(4)
                        xxx.save()
                    except:
                        print("SUCESS")
                else:
                    token=float(10)
                    tmptoken=float(10)

                #token=float(10)
                #tmptoken=float(10)

                

                #Profile_token.objects.get_or_create(referral_link=referral_link, user_email=user_email, user_first_name=user_first_name, user_last_name=user_last_name, user_institution=user_institution, user_department=user_department, onboard="True",token=float(10),tmptoken=float(10))
                Profile_token.objects.get_or_create(user_email=user_email,\
                defaults={'referral_link': referral_link,'user_first_name':user_first_name,\
                'user_last_name':user_last_name,'user_institution':user_institution, 'user_department':user_department,\
                'onboard':"True",'token':token,'tmptoken':tmptoken},)
 
                #profile.save()
                ####20210903 要換model存

                #########加上Profile_token model 20210813

                #Profile_token.objects.get_or_create(user_email=user_email, user_first_name=user_first_name, user_last_name=user_last_name, user_institution=user_institution, user_department=user_department)
                
                return redirect('onboarding')

            return render(request, 'profile/onboard.html')

        return redirect('onboarding')


    else:
        return redirect('account_login')


def onboarding(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            user_email=request.user.email
            avatarStyle = request.POST.get('avatarStyle')
            topType = request.POST.get('topType')
            accessoriesType = request.POST.get('accessoriesType')
            hairColor = request.POST.get('hairColor')
            hatColor = request.POST.get('hatColor')
            facialHairType = request.POST.get('facialHairType')
            facialHairColor = request.POST.get('facialHairColor')
            clotheType = request.POST.get('clotheType')
            clotheColor = request.POST.get('clotheColor')
            graphicType = request.POST.get('graphicType')
            eyeType = request.POST.get('eyeType')
            eyebrowType = request.POST.get('eyebrowType')
            mouthType = request.POST.get('mouthType')
            skinColor = request.POST.get('skinColor')
            Profile_token.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor,)   
            return redirect('onboarding')

        user_listing = get_object_or_404(Profile_token, user_email=request.user.email)
        
        check_orcid=user_listing.orcid
        creat_index=user_listing.create_index

        referral_link=user_listing.referral_link

        tmpcheck_listing=user_listing
        check_token=float(tmpcheck_listing.token)
        check_first_name=tmpcheck_listing.user_first_name
        check_last_name=tmpcheck_listing.user_last_name
        check_institution=tmpcheck_listing.user_institution
        check_department=tmpcheck_listing.user_department
        check_email=tmpcheck_listing.user_email
        check_gspi=tmpcheck_listing.gspi
        check_rcpi=tmpcheck_listing.rcpi
        tmpcheck=1         
        


        if str(user_listing.userurl) !="0":
            return redirect('profile',user_url=user_listing.userurl)

        query_first_name=user_listing.user_first_name
        query_last_name=user_listing.user_last_name
        # print(query_first_name)
        # print(query_last_name)
        queryresult=scopusmatch1.objects.exclude(ischeck=1).filter(scopus__icontains=str(query_first_name)+' '+str(query_last_name))
        #queryresult=scopusmatch1.objects.filter(scopus__iexact=str(query_first_name)+' '+str(query_last_name))
        #queryresult=scopusmatch1.objects.filter(scopus__unaccent__icontains=str(query_first_name)+' '+str(query_last_name))
        #
        #queryresult=scopusmatch1.objects.exclude(userurl=0).filter(scopus__icontains='龍明 徳山')
        #print("幹你娘機掰糙")
        if len(queryresult)==0:
            queryindex=0
        else:
            queryindex=1
        
        try:

            if queryindex==1:
                queryname=[]
                queryinstitue=[]
                queryahref=[]
                #queryzip=[]
                for x in queryresult:
                    queryahref.append(x.userurl)     
                    # tmpprofile=Profile.objects.get(userurl=x.userurl)
                    # queryinstitue.append(tmpprofile.user_institution)
                    # queryname.append(tmpprofile.user_first_name+' '+tmpprofile.user_last_name)
                    # queryzip=zip(queryname,queryinstitue,queryahref)
                    queryname.append(x.user_first_name+' '+x.user_last_name)
                    queryinstitue.append(x.user_institution)
                    queryzip=zip(queryname,queryinstitue,queryahref)

            else:
                queryzip=[]
        except:
            queryzip=[]


        #####################################################################
        #20210910 query nft
        qsnft=Pdfupload.objects.filter(email_address__icontains=request.user.email)
        if len(qsnft)>0:
            nfttitle=[]
            nfttitleurl=[]
            nfteach=[]
            nftcoll=0
            for x in range(len(qsnft)):
                qsnftemaillist=qsnft[x].nftpeopleemail
                qsnftdistribute=qsnft[x].nftdistribute
                qsnfttitle=qsnft[x].title
                qsnfttitleurl=qsnft[x].titleurl
                
                try:
                    qsindex=qsnftemaillist.index(qsnftemaillist)
                    eachnft=qsnftdistribute[qsindex]
                    nfttitle.append(qsnfttitle)
                    nfttitleurl.append(qsnfttitleurl)
                    nfteach.append(float(eachnft))
                    nftcoll+=1
                except:
                    pass
            
            nftzip=zip(nfttitle,nfteach,nfttitleurl)
            sumnft=sum(nfteach)
            
        else:
            nftzip=""
            sumnft=0
            nftcoll=0

        #######################################################################
        #nft
        qsnftlist=nftlist.objects.filter(email_address=request.user.email)
        if len(qsnftlist)>0:
            nftlisttitle=[]
            nftlisttitleurl=[]
            nftlistq=[]
            nftlistp=[]
            for x in range(len(qsnftlist)):
                qsnftlistq=qsnftlist[x].quantity
                qsnftlisttitle=qsnftlist[x].title
                qsnftlisttitleurl=qsnftlist[x].titleurl
                qsnftlistp=qsnftlist[x].pricepernft
                nftlistq.append(qsnftlistq)
                nftlisttitle.append(qsnftlisttitle)
                nftlisttitleurl.append(qsnftlisttitleurl)
                nftlistp.append(qsnftlistp)

            nftlistzip=zip(nftlisttitle,nftlistq,nftlisttitleurl,nftlistp)
        else:
            nftlistzip=""
       
        qsnftbid=nftbid.objects.filter(email_address=request.user.email)
        if len(qsnftbid)>0:
            nftbidtitle=[]
            nftbidtitleurl=[]
            nftbidq=[]
            nftbidp=[]
            for x in range(len(qsnftbid)):
                qsnftbidq=qsnftbid[x].quantity
                qsnftbidtitle=qsnftbid[x].title
                qsnftbidtitleurl=qsnftbid[x].titleurl
                qsnftbidp=qsnftbid[x].pricepernft
                nftbidtitle.append(qsnftbidtitle)
                nftbidq.append(qsnftbidq)
                nftbidtitleurl.append(qsnftbidtitleurl)
                nftbidp.append(qsnftbidp)

            nftbidzip=zip(nftbidtitle,nftbidq,nftbidtitleurl,nftbidp)
        else:
            nftbidzip=""
       
        qsnftdonate=nftdonate.objects.filter(email_address=request.user.email)

        if len(qsnftdonate)>0:
            nftdonatetitle=[]
            nftdonatetitleurl=[]
            nftdonateq=[]
            for x in range(len(qsnftdonate)):
                qsnftdonateq=qsnftdonate[x].quantity
                qsnftdonatetitle=qsnftdonate[x].title
                qsnftdonatetitleurl=qsnftdonate[x].titleurl
                nftdonateq.append(qsnftdonateq)
                nftdonatetitle.append(qsnftdonatetitle)
                nftdonatetitleurl.append(qsnftdonatetitleurl)

            nftdonatezip=zip(nftdonatetitle,nftdonateq,nftdonatetitleurl)
        else:
            nftdonatezip=""

        
        NFTToken = float(user_listing.token) - float(user_listing.tmptoken)
        print("##################################")
        print("##################################")
        print("##################################")
        try:
            #print("幹你娘")
            #xxx=Profile_token.objects.get(userurl=user_url)
            useremail=request.user.email
            print(useremail)
            pdfupload=Pdfupload.objects.filter(Q(uploadauthor=useremail) | Q(email_address__icontains=useremail))
            print(pdfupload)
            print("##################################")
            print("##################################")
            print("##################################")
            print("##################################")
            print("##################################")

            if len(pdfupload)>0:

                authorlen=1
                title=[]
                titleurl=[]
                abstract=[]
                #first_name=[]
                #last_name=[]
                name=[]

                for x in range(len(pdfupload)):
                    title.append(pdfupload[x].title)
                    titleurl.append(pdfupload[x].titleurl)
                    abstract.append(pdfupload[x].abstract)
                    #要改
                    zipname=zip(pdfupload[x].first_name.split("#"),pdfupload[x].last_name.split('#'))
                    tmpname=[]
                    for x1,x2 in zipname:
                        tmpname.append(x1+' '+x2)
                    newtmpname="; ".join(tmpname)    
                    #name.append(pdfupload[x].first_name+' '+pdfupload.last_name)
                    name.append(newtmpname)

                    authorzip=zip(title,titleurl,abstract,name)
            else:
                authorzip=zip([],[],[],[])
                authorlen=0
        except:
            authorzip=zip([],[],[],[])
            authorlen=0


        context = {
                'user_listing':user_listing,
                'queryzip':queryzip,
                'token':float(user_listing.token),
                'check_orcid':check_orcid,
                'creat_index':creat_index,
                'queryindex':queryindex,
                'referral_link':referral_link,
                'tmpcheck':tmpcheck,
                'check_token':check_token,
                'check_first_name':check_first_name,
                'check_last_name':check_last_name,
                'check_institution':check_institution,
                'check_department':check_department,
                'tmpcheck_listing':tmpcheck_listing,
                'check_email':check_email,
                'check_gspi':check_gspi,
                'check_rcpi':check_rcpi,
                'nftzip':nftzip,
                'sumnft':sumnft,
                'nftcoll':nftcoll,
                'nftlistzip':nftlistzip,
                'nftbidzip':nftbidzip,
                'nftdonatezip':nftdonatezip,
                'tmptoken':float(user_listing.tmptoken),
                'NFTToken':NFTToken,
                'authorzip':authorzip,
                'authorlen':authorlen,
            }
        return render(request, 'profile/onboarding.html', context)
    else:
        return redirect('account_login')

def referral(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            user_email=request.user.email
            avatarStyle = request.POST.get('avatarStyle')
            topType = request.POST.get('topType')
            accessoriesType = request.POST.get('accessoriesType')
            hairColor = request.POST.get('hairColor')
            hatColor = request.POST.get('hatColor')
            facialHairType = request.POST.get('facialHairType')
            facialHairColor = request.POST.get('facialHairColor')
            clotheType = request.POST.get('clotheType')
            clotheColor = request.POST.get('clotheColor')
            graphicType = request.POST.get('graphicType')
            eyeType = request.POST.get('eyeType')
            eyebrowType = request.POST.get('eyebrowType')
            mouthType = request.POST.get('mouthType')
            skinColor = request.POST.get('skinColor')

            


            
            Profile_token.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor,)
            
            
            
            return redirect('onboarding')

        try:
            user_listing = get_object_or_404(Profile_token, user_email=request.user.email)
        
            
            check_orcid=user_listing.orcid
            referral_link=user_listing.referral_link
            tmpcheck_listing=user_listing
            check_token=float(tmpcheck_listing.token)
            check_first_name=tmpcheck_listing.user_first_name
            check_last_name=tmpcheck_listing.user_last_name
            check_institution=tmpcheck_listing.user_institution
            check_department=tmpcheck_listing.user_department
            check_email=tmpcheck_listing.user_email
            check_gspi=tmpcheck_listing.gspi
            check_rcpi=tmpcheck_listing.rcpi
            tmpcheck=1         

        except:
            return redirect('onboard')
        





        context = {
                'user_listing':user_listing,
                'token':float(user_listing.token),
                'check_orcid':check_orcid,
                'referral_link':referral_link,
                'tmpcheck':tmpcheck,
                'check_token':check_token,
                'check_first_name':check_first_name,
                'check_last_name':check_last_name,
                'check_institution':check_institution,
                'check_department':check_department,
                'tmpcheck_listing':tmpcheck_listing,
                'check_email':check_email,
                #'check_orcid':check_orcid,#
                'check_gspi':check_gspi,
                'check_rcpi':check_rcpi,
            }
        return render(request, 'profile/referral.html', context)

    else:
        return redirect('account_login')

def sociallink(request):

    user_listing = get_object_or_404(Profile, user_email=request.user.email)

    if request.method == 'POST':
        user_email=request.user.email

        googlescholar = request.POST.get('googlescholar')
        researchgate = request.POST.get('researchgate')
        linkedin = request.POST.get('linkedin')
        github = request.POST.get('github')
        orcid = request.POST.get('orcid')
        twitter = request.POST.get('twitter')
        facebook = request.POST.get('facebook')
        personal = request.POST.get('personal')
        
        Profile.objects.filter(user_email=user_email).update(google_scholar=googlescholar, researchgate=researchgate, linkedin=linkedin, github=github, orcid=orcid, twitter=twitter, facebook=facebook, personal=personal)

        return redirect('onboarding')

def personalinfo(request):
    if request.user.is_authenticated:
        user_listing = get_object_or_404(Profile_token, user_email=request.user.email)

        if request.method == 'POST':

            
            user_email=request.user.email
            user_first_name = request.POST.get('user_first_name')
            user_last_name = request.POST.get('user_last_name')
            user_institution = request.POST.get('user_institution')
            user_department = request.POST.get('user_department')
            
            Profile_token.objects.filter(user_email=user_email).update(user_email=user_email, user_first_name=user_first_name, user_last_name=user_last_name, user_institution=user_institution, user_department=user_department)

            return redirect('onboarding')
    else:
        return redirect('account_login')




# def onboarding(request):


    

#     if request.user.is_authenticated:

#         Create_Email=Profile.objects.filter(user_email=request.user.email)
      
#         if len(Create_Email) == 0: 

#             if request.method == 'POST':

                
#                 user_email = request.POST.get('user_email')
#                 user_first_name = request.POST.get('user_first_name')
#                 # user_middle_name = request.POST.get('user_middle_name')
#                 user_last_name = request.POST.get('user_last_name')
#                 user_institution = request.POST.get('user_institution')
#                 user_department = request.POST.get('user_department')
#                 # user_position = request.POST.get('user_position')
#                 # google_scholar = request.POST.get('google_scholar')
#                 # researchgate = request.POST.get('researchgate')
#                 # other = request.POST.get('other')


#                 tmpuserurl='-'.join([x.capitalize() for x in slugify(user_first_name+' '+user_last_name).split('-')])

#                 if len(Profile.objects.filter(user_url__startswith=tmpuserurl))==0:
#                     user_url=tmpuserurl
#                 elif len(Profile.objects.filter(user_url__startswith=tmpuserurl))==1:
#                     user_url=tmpuserurl+'-'+'1'
#                 elif len(Profile.objects.filter(user_url__startswith=tmpuserurl))==2:
#                     user_url=tmpuserurl+'-'+'2'
#                 elif len(Profile.objects.filter(user_url__startswith=tmpuserurl))==3:
#                     user_url=tmpuserurl+'-'+'3'
#                 #####以此類推
#                 else:
#                     pass


#                 profile = Profile.objects.create(user_email=user_email, user_first_name=user_first_name, user_last_name=user_last_name, user_institution=user_institution, user_department=user_department, user_url=user_url, userurl=user_url, onboard="True")


#                 profile.save()

#                 return render(request, 'profile/onboarding.html')

#             return render(request, 'profile/onboarding.html')

#         URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]
        
#         return redirect('profile', URL)


#     else:
#         return redirect('account_login')




def network_affliation(request, user_url):
    #print("幹你娘機掰network_affiliation!")

    searchid=int(user_url.split("-")[-1])
    #user_listing = get_object_or_404(Profile, userurl=user_url)
    #print(len(Profile_test.objects.all()))
    user_listing= Profile.objects.get(pk=searchid)
    #print("e04")
    print(user_listing.user_url)

    try:
        tmpcheck_listing=Profile_token.objects.get(userurl=user_url)
        check_token=float(tmpcheck_listing.token)
        check_first_name=tmpcheck_listing.user_first_name
        check_last_name=tmpcheck_listing.user_last_name
        check_institution=tmpcheck_listing.user_institution
        check_department=tmpcheck_listing.user_department
        check_email=tmpcheck_listing.user_email
        check_orcid=tmpcheck_listing.orcid
        check_gspi=tmpcheck_listing.gspi
        check_rcpi=tmpcheck_listing.rcpi
        referral_link=tmpcheck_listing.referral_link
        tmpcheck=1

        token=float(tmpcheck_listing.token)
        tmptoken=float(tmpcheck_listing.tmptoken)
        NFTToken = float(tmpcheck_listing.token) - float(tmpcheck_listing.tmptoken)
    except: 
        tmpcheck=0
        check_token=float(0)
        check_first_name=""
        check_last_name=""
        check_institution=""
        check_department=""
        check_email=""
        check_orcid=""
        check_gspi=""
        check_rcpi=""
        referral_link=""
        tmpcheck_listing=user_listing

        token=float(0)
        tmptoken=float(0)
        NFTToken=float(0)


    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    

    # csvpath='static/scopus_match1.csv'
    # scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
    # # print(scopusmatch.columns)
    # # print(scopusmatch['scopus'].values)
    # userurllist=scopusmatch['user_url'].values
    # scopuslist=scopusmatch['scopus'].values
    # dictmatch=dict(zip(userurllist,scopuslist))
    
 
    mapcity=user_listing.mapcity
    #newmapcity=country+'@'+lat+'@'+lon+'@'+countn+'@'+asso
    try:
        mapcity_country=mapcity.split('@')[0].split('$')
        mapcity_lat=mapcity.split('@')[1].split('$')
        mapcity_lat=[float(x) for x in mapcity_lat]
        mapcity_lon=mapcity.split('@')[2].split('$')
        mapcity_lon=[float(x) for x in mapcity_lon]
        mapcity_countn=mapcity.split('@')[3].split('$')
        mapcity_countn=[int(x) for x in mapcity_countn]
        mapcity_asso=mapcity.split('@')[4].split('*')
        mapcity_asso=[x.replace('\'','') for x in mapcity_asso]
    except:
        mapcity_country=[]
        mapcity_lat=[]
        mapcity_lon=[]
        mapcity_countn=[]
        mapcity_asso=[]
    
    countorigin=mapcity_countn
    start = 3
    end = 6
    arr=countorigin
    arrnew=[]
    for x in arr:
        if int(x)>100:
            arrnew.append(int(100))
        else:
            arrnew.append(int(x))
    arr=arrnew
    if len(arr)>1:
        width = end - start
        maxarr=max(arr)
        if int(maxarr-min(arr))!=0:
            res=[(x-min(arr))/(maxarr-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        #res=arr
        res=[5] #20210718改


    mapcity_countn_new=res
    newmapcity=[{'country': x1,'lat': x2,'lon': x3,'countn': x4, 'asso': x5} \
    for x1, x2, x3, x4, x5 in zip(mapcity_country, mapcity_lat, mapcity_lon, mapcity_countn_new, mapcity_asso)]
    #cityinfo_json_new=json.dumps([{'country': mapcity_country,'lat':mapcity_lat,'lon':mapcity_lon,'countn':mapcity_countn_new, 'asso': mapcity_asso}])
    cityinfo_json_new=json.dumps(newmapcity)

    cityinfo_qs=zip(mapcity_country, mapcity_lat, mapcity_lon, mapcity_countn_new, mapcity_asso)
    

    mapconn=user_listing.mapconn
    #print("幹你娘")
    #print(mapconn)
    try:
        mapconn_long1=mapconn.split('@')[0].split('$')
        mapconn_long1=[float(x) for x in mapconn_long1]
        mapconn_long2=mapconn.split('@')[1].split('$')
        mapconn_long2=[float(x) for x in mapconn_long2]
        mapconn_lat1=mapconn.split('@')[2].split('$')
        mapconn_lat1=[float(x) for x in mapconn_lat1]
        mapconn_lat2=mapconn.split('@')[3].split('$')
        mapconn_lat2=[float(x) for x in mapconn_lat2]
    except:
        mapconn_long1=[]
        mapconn_long2=[]
        mapconn_lat1=[]
        mapconn_lat2=[]

    newmapconn=[{'long1': x1,'long2': x2,'lat1': x3,'lat2': x4} \
    for x1, x2, x3, x4 in zip(mapconn_long1, mapconn_long2, mapconn_lat1, mapconn_lat2)]
    conninfo_json_new=json.dumps(newmapconn)

    ###################################################################################################
    ###################################################################################################
    # qsnft=Pdfupload.objects.filter(email_address__icontains=request.user.email)
    # if len(qsnft)>0:
    #     nfttitle=[]
    #     nfttitleurl=[]
    #     nfteach=[]
    #     nftcoll=0
    #     for x in range(len(qsnft)):
    #         qsnftemaillist=qsnft[x].nftpeopleemail
    #         qsnftdistribute=qsnft[x].nftdistribute
    #         qsnfttitle=qsnft[x].title
    #         qsnfttitleurl=qsnft[x].titleurl
            
    #         try:
    #             qsindex=qsnftemaillist.index(qsnftemaillist)
    #             eachnft=qsnftdistribute[qsindex]
    #             nfttitle.append(qsnfttitle)
    #             nfttitleurl.append(qsnfttitleurl)
    #             nfteach.append(float(eachnft))
    #             nftcoll+=1
    #         except:
    #             pass
        
    #     nftzip=zip(nfttitle,nfteach,nfttitleurl)
    #     sumnft=sum(nfteach)
        
    # else:
    #     nftzip=""
    #     sumnft=0
    #     nftcoll=0

    # #######################################################################
    # #nft
    # qsnftlist=nftlist.objects.filter(email_address=request.user.email)
    # if len(qsnftlist)>0:
    #     nftlisttitle=[]
    #     nftlisttitleurl=[]
    #     nftlistq=[]
    #     nftlistp=[]
    #     for x in range(len(qsnftlist)):
    #         qsnftlistq=qsnftlist[x].quantity
    #         qsnftlisttitle=qsnftlist[x].title
    #         qsnftlisttitleurl=qsnftlist[x].titleurl
    #         qsnftlistp=qsnftlist[x].pricepernft
    #         nftlistq.append(qsnftlistq)
    #         nftlisttitle.append(qsnftlisttitle)
    #         nftlisttitleurl.append(qsnftlisttitleurl)
    #         nftlistp.append(qsnftlistp)

    #     nftlistzip=zip(nftlisttitle,nftlistq,nftlisttitleurl,nftlistp)
    # else:
    #     nftlistzip=""

    # qsnftbid=nftbid.objects.filter(email_address=request.user.email)
    # if len(qsnftbid)>0:
    #     nftbidtitle=[]
    #     nftbidtitleurl=[]
    #     nftbidq=[]
    #     nftbidp=[]
    #     for x in range(len(qsnftbid)):
    #         qsnftbidq=qsnftbid[x].quantity
    #         qsnftbidtitle=qsnftbid[x].title
    #         qsnftbidtitleurl=qsnftbid[x].titleurl
    #         qsnftbidp=qsnftbid[x].pricepernft
    #         nftbidtitle.append(qsnftbidtitle)
    #         nftbidq.append(qsnftbidq)
    #         nftbidtitleurl.append(qsnftbidtitleurl)
    #         nftbidp.append(qsnftbidp)

    #     nftbidzip=zip(nftbidtitle,nftbidq,nftbidtitleurl,nftbidp)
    # else:
    #     nftbidzip=""
    
    # qsnftdonate=nftdonate.objects.filter(email_address=request.user.email)

    # if len(qsnftdonate)>0:
    #     nftdonatetitle=[]
    #     nftdonatetitleurl=[]
    #     nftdonateq=[]
    #     for x in range(len(qsnftdonate)):
    #         qsnftdonateq=qsnftdonate[x].quantity
    #         qsnftdonatetitle=qsnftdonate[x].title
    #         qsnftdonatetitleurl=qsnftdonate[x].titleurl
    #         nftdonateq.append(qsnftdonateq)
    #         nftdonatetitle.append(qsnftdonatetitle)
    #         nftdonatetitleurl.append(qsnftdonatetitleurl)

    #     nftdonatezip=zip(nftdonatetitle,nftdonateq,nftdonatetitleurl)
    # else:
    #     nftdonatezip=""
    ###############20210912
    try:
        qsnft=Pdfupload.objects.filter(email_address__icontains=request.user.email)
        if len(qsnft)>0:
            nfttitle=[]
            nfttitleurl=[]
            nfteach=[]
            nftcoll=0
            for x in range(len(qsnft)):
                qsnftemaillist=qsnft[x].nftpeopleemail
                qsnftdistribute=qsnft[x].nftdistribute
                qsnfttitle=qsnft[x].title
                qsnfttitleurl=qsnft[x].titleurl
                
                try:
                    qsindex=qsnftemaillist.index(qsnftemaillist)
                    eachnft=qsnftdistribute[qsindex]
                    nfttitle.append(qsnfttitle)
                    nfttitleurl.append(qsnfttitleurl)
                    nfteach.append(float(eachnft))
                    nftcoll+=1
                except:
                    pass
            
            nftzip=zip(nfttitle,nfteach,nfttitleurl)
            sumnft=sum(nfteach)
            
        else:
            nftzip=""
            sumnft=0
            nftcoll=0
    except:
        nftzip=""
        sumnft=0
        nftcoll=0

    #######################################################################
    #nft
    try:
        qsnftlist=nftlist.objects.filter(email_address=request.user.email)
        if len(qsnftlist)>0:
            nftlisttitle=[]
            nftlisttitleurl=[]
            nftlistq=[]
            nftlistp=[]
            for x in range(len(qsnftlist)):
                qsnftlistq=qsnftlist[x].quantity
                qsnftlisttitle=qsnftlist[x].title
                qsnftlisttitleurl=qsnftlist[x].titleurl
                qsnftlistp=qsnftlist[x].pricepernft
                nftlistq.append(qsnftlistq)
                nftlisttitle.append(qsnftlisttitle)
                nftlisttitleurl.append(qsnftlisttitleurl)
                nftlistp.append(qsnftlistp)

            nftlistzip=zip(nftlisttitle,nftlistq,nftlisttitleurl,nftlistp)
        else:
            nftlistzip=""
    except:
        nftlistzip=""

    try:
        qsnftbid=nftbid.objects.filter(email_address=request.user.email)
        if len(qsnftbid)>0:
            nftbidtitle=[]
            nftbidtitleurl=[]
            nftbidq=[]
            nftbidp=[]
            for x in range(len(qsnftbid)):
                qsnftbidq=qsnftbid[x].quantity
                qsnftbidtitle=qsnftbid[x].title
                qsnftbidtitleurl=qsnftbid[x].titleurl
                qsnftbidp=qsnftbid[x].pricepernft
                nftbidtitle.append(qsnftbidtitle)
                nftbidq.append(qsnftbidq)
                nftbidtitleurl.append(qsnftbidtitleurl)
                nftbidp.append(qsnftbidp)

            nftbidzip=zip(nftbidtitle,nftbidq,nftbidtitleurl,nftbidp)
        else:
            nftbidzip=""
    except:
        nftbidzip=""
    
    try:
        qsnftdonate=nftdonate.objects.filter(email_address=request.user.email)

        if len(qsnftdonate)>0:
            nftdonatetitle=[]
            nftdonatetitleurl=[]
            nftdonateq=[]
            for x in range(len(qsnftdonate)):
                qsnftdonateq=qsnftdonate[x].quantity
                qsnftdonatetitle=qsnftdonate[x].title
                qsnftdonatetitleurl=qsnftdonate[x].titleurl
                nftdonateq.append(qsnftdonateq)
                nftdonatetitle.append(qsnftdonatetitle)
                nftdonatetitleurl.append(qsnftdonatetitleurl)

            nftdonatezip=zip(nftdonatetitle,nftdonateq,nftdonatetitleurl)
        else:
            nftdonatezip=""   
    except:
        nftdonatezip=""



    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
            'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
            'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),

            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            # 'tree1_json':tree1_json,
            #'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,
            'cityinfo_qs':cityinfo_qs,
            #'conninfo_qs':conninfo_qs,
            'cityinfo_json_new':cityinfo_json_new,
            'conninfo_json_new':conninfo_json_new,
            'tmpcheck':tmpcheck,
            'check_token':check_token,
            'check_first_name':check_first_name,
            'check_last_name':check_last_name,
            'check_institution':check_institution,
            'check_department':check_department,
            'tmpcheck_listing':tmpcheck_listing,
            'check_email':check_email,
            'check_orcid':check_orcid,
            'check_gspi':check_gspi,
            'check_rcpi':check_rcpi,
            'referral_link':referral_link,
            #####
            'token':token,
            'tmptoken':tmptoken,
            'NFTToken':NFTToken,
            'nftzip':nftzip,
            'sumnft':sumnft,
            'nftcoll':nftcoll,
            'nftlistzip':nftlistzip,
            'nftbidzip':nftbidzip,
            'nftdonatezip':nftdonatezip,
        }
    
    return render(request, 'profile/network_affliation.html', context)

def network_affliation_query(request,user_url,affi):
    print("幹!!!")
    print("DSafsdgfdghfdghfgjgfjhgfhjfghjgfhj")


    user_listing = get_object_or_404(Profile, userurl=user_url)
    print(user_listing)

    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)


    print("dfgfgdhdgfhjhgjgfhjfdghsdfhfgjsgf")
    print(affi)
    affi=affi.strip()
    affi=affi.replace('-',' ').replace('_','.')
    
    
    csvpath='AA/static/scopus_match1.csv'
    scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')

    userurllist=scopusmatch['user_url'].values
    scopuslist=scopusmatch['scopus'].values
    dictmatch=dict(zip(userurllist,scopuslist))
    
    articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url]).filter(authoraffi__contains=affi)


    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

######################20210103###################
    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    #print("幹")
    #print(cityinfo_qs)
    #print(len(cityinfo_qs))

    conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    countorigin=[]
    for i in range(len(cityinfo_qs)):
        tmpcityinfo=cityinfo_qs[i].asso
        #print(tmpcityinfo)
        cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
        countorigin.append(int(cityinfo_qs[i].countn))
    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    start = 5
    end = 10
    arr=countorigin
    if len(arr)>1:
        #print(arr)
        #print(len(arr))
        width = end - start
        if int(max(arr)-min(arr))!=0:
            res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        res=arr

    for i in range(len(cityinfo_qs)):
        cityinfo_qs[i].countn=res[i]

    cityinfo_json = serialize("json", cityinfo_qs)
    conninfo_json = serialize("json", conninfo_qs)

    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()



    profile1=[]
    for i in range(len(articleinfo_qs)):
        profile1.append(user_url) 

    journal=list(articleinfo_qs.values_list('journal', flat=True))
    year=list(articleinfo_qs.values_list('year', flat=True))
    title=list(articleinfo_qs.values_list('title', flat=True))
    titleurl=[slugify(x) for x in title]
    author=list(articleinfo_qs.values_list('authorabbr', flat=True))

    author=["; ".join(x.split('#')) for x in author]

    cite=list(articleinfo_qs.values_list('cite', flat=True))
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)

    articlein=zip(profile1,journal,year,title,author,cite1,titleurl)
    articlein=sorted(articlein,  key =operator.itemgetter(5,2,1), reverse=True)

    paginator = Paginator(articlein, 10)
    page = request.GET.get('page')
    paged_articlein = paginator.get_page(page)




    context={
        'affi':affi,
        'articlein':articlein,
        'paged_articlein':paged_articlein,
        'user_url':user_url,
        'userurl':userurl,
        'user_listing':user_listing,

        'cityinfo_json':cityinfo_json,
        'conninfo_json':conninfo_json,
    }
    return render(request, 'profile/network_affliation_query.html', context)




def network_coauthor(request, user_url):

    searchid=int(user_url.split("-")[-1])

    #user_listing = get_object_or_404(Profile, userurl=user_url)
    #print(len(Profile_test.objects.all()))
    user_listing= Profile.objects.get(pk=searchid)
    #print("e04")
    print(user_listing.user_url)

    try:
        tmpcheck_listing=Profile_token.objects.get(userurl=user_url)
        check_token=float(tmpcheck_listing.token)
        check_first_name=tmpcheck_listing.user_first_name
        check_last_name=tmpcheck_listing.user_last_name
        check_institution=tmpcheck_listing.user_institution
        check_department=tmpcheck_listing.user_department
        check_email=tmpcheck_listing.user_email
        check_orcid=tmpcheck_listing.orcid
        check_gspi=tmpcheck_listing.gspi
        check_rcpi=tmpcheck_listing.rcpi
        referral_link=tmpcheck_listing.referral_link
        tmpcheck=1

        token=float(tmpcheck_listing.token)
        tmptoken=float(tmpcheck_listing.tmptoken)
        NFTToken = float(tmpcheck_listing.token) - float(tmpcheck_listing.tmptoken)
    except: 
        tmpcheck=0
        check_token=float(0)
        check_first_name=""
        check_last_name=""
        check_institution=""
        check_department=""
        check_email=""
        check_orcid=""
        check_gspi=""
        check_rcpi=""
        referral_link=""
        tmpcheck_listing=user_listing

        token=float(0)
        tmptoken=float(0)
        NFTToken=float(0)


    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)


    mapconn=user_listing.mapconn
    try:
        mapconn_long1=mapconn.split('@')[0].split('$')
        mapconn_long1=[float(x) for x in mapconn_long1]
        mapconn_long2=mapconn.split('@')[1].split('$')
        mapconn_long2=[float(x) for x in mapconn_long2]
        mapconn_lat1=mapconn.split('@')[2].split('$')
        mapconn_lat1=[float(x) for x in mapconn_lat1]
        mapconn_lat2=mapconn.split('@')[3].split('$')
        mapconn_lat2=[float(x) for x in mapconn_lat2]
    except:
        mapconn_long1=[]
        mapconn_long2=[]
        mapconn_lat1=[]
        mapconn_lat2=[]

    newmapconn=[{'long1': x1,'long2': x2,'lat1': x3,'lat2': x4} \
    for x1, x2, x3, x4 in zip(mapconn_long1, mapconn_long2, mapconn_lat1, mapconn_lat2)]
    conninfo_json_new=json.dumps(newmapconn)

    mapcoau=user_listing.mapcoau    

    try:
        mapcoau_country=mapcoau.split('@')[0].split('$')
        mapcoau_lat=mapcoau.split('@')[1].split('$')
        mapcoau_lat=[float(x) for x in mapcoau_lat]
        mapcoau_lon=mapcoau.split('@')[2].split('$')
        mapcoau_lon=[float(x) for x in mapcoau_lon]
        mapcoau_countn=mapcoau.split('@')[3].split('$')
        mapcoau_countn=[int(x) for x in mapcoau_countn]
        mapcoau_coauthor=mapcoau.split('@')[4].split('*')
        mapcoau_coauthor=[x.replace('\'','') for x in mapcoau_coauthor]
    except:
        mapcoau_country=[]
        mapcoau_lat=[]
        mapcoau_lon=[]
        mapcoau_countn=[]
        mapcoau_coauthor=[]

    
    countorigin=mapcoau_countn
    start = 3
    end = 6
    arr=countorigin
    arrnew=[] 
    for x in arr:
        if int(x)>100:
            arrnew.append(int(100))
        else:
            arrnew.append(int(x))
    arr=arrnew
    if len(arr)>1:
        width = end - start
        maxarr=max(arr)
        if int(maxarr-min(arr))!=0:
            res=[(x-min(arr))/(maxarr-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        #res=arr
        res=[5] #20210718改

    #print(arr)
    mapcoau_countn_new=res
    #print("幹你娘!!!")
    #print(mapcoau_countn_new)
    newmapcoau=[{'country': x1,'lat': x2,'lon': x3,'countn': x4, 'coauthor': x5} \
    for x1, x2, x3, x4, x5 in zip(mapcoau_country, mapcoau_lat, mapcoau_lon, mapcoau_countn_new, mapcoau_coauthor)]
    #cityinfo_json_new=json.dumps([{'country': mapcity_country,'lat':mapcity_lat,'lon':mapcity_lon,'countn':mapcity_countn_new, 'asso': mapcity_asso}])
    coauthorinfo_json_new=json.dumps(newmapcoau)

    coauthorinfo_qs=zip(mapcoau_country, mapcoau_lat, mapcoau_lon, mapcoau_countn_new, mapcoau_coauthor)
 
    # qsnft=Pdfupload.objects.filter(email_address__icontains=request.user.email)
    # if len(qsnft)>0:
    #     nfttitle=[]
    #     nfttitleurl=[]
    #     nfteach=[]
    #     nftcoll=0
    #     for x in range(len(qsnft)):
    #         qsnftemaillist=qsnft[x].nftpeopleemail
    #         qsnftdistribute=qsnft[x].nftdistribute
    #         qsnfttitle=qsnft[x].title
    #         qsnfttitleurl=qsnft[x].titleurl
            
    #         try:
    #             qsindex=qsnftemaillist.index(qsnftemaillist)
    #             eachnft=qsnftdistribute[qsindex]
    #             nfttitle.append(qsnfttitle)
    #             nfttitleurl.append(qsnfttitleurl)
    #             nfteach.append(float(eachnft))
    #             nftcoll+=1
    #         except:
    #             pass
        
    #     nftzip=zip(nfttitle,nfteach,nfttitleurl)
    #     sumnft=sum(nfteach)
        
    # else:
    #     nftzip=""
    #     sumnft=0
    #     nftcoll=0

    #######################################################################
    #nft
    # qsnftlist=nftlist.objects.filter(email_address=request.user.email)
    # if len(qsnftlist)>0:
    #     nftlisttitle=[]
    #     nftlisttitleurl=[]
    #     nftlistq=[]
    #     nftlistp=[]
    #     for x in range(len(qsnftlist)):
    #         qsnftlistq=qsnftlist[x].quantity
    #         qsnftlisttitle=qsnftlist[x].title
    #         qsnftlisttitleurl=qsnftlist[x].titleurl
    #         qsnftlistp=qsnftlist[x].pricepernft
    #         nftlistq.append(qsnftlistq)
    #         nftlisttitle.append(qsnftlisttitle)
    #         nftlisttitleurl.append(qsnftlisttitleurl)
    #         nftlistp.append(qsnftlistp)

    #     nftlistzip=zip(nftlisttitle,nftlistq,nftlisttitleurl,nftlistp)
    # else:
    #     nftlistzip=""

    # qsnftbid=nftbid.objects.filter(email_address=request.user.email)
    # if len(qsnftbid)>0:
    #     nftbidtitle=[]
    #     nftbidtitleurl=[]
    #     nftbidq=[]
    #     nftbidp=[]
    #     for x in range(len(qsnftbid)):
    #         qsnftbidq=qsnftbid[x].quantity
    #         qsnftbidtitle=qsnftbid[x].title
    #         qsnftbidtitleurl=qsnftbid[x].titleurl
    #         qsnftbidp=qsnftbid[x].pricepernft
    #         nftbidtitle.append(qsnftbidtitle)
    #         nftbidq.append(qsnftbidq)
    #         nftbidtitleurl.append(qsnftbidtitleurl)
    #         nftbidp.append(qsnftbidp)

    #     nftbidzip=zip(nftbidtitle,nftbidq,nftbidtitleurl,nftbidp)
    # else:
    #     nftbidzip=""
    
    # qsnftdonate=nftdonate.objects.filter(email_address=request.user.email)

    # if len(qsnftdonate)>0:
    #     nftdonatetitle=[]
    #     nftdonatetitleurl=[]
    #     nftdonateq=[]
    #     for x in range(len(qsnftdonate)):
    #         qsnftdonateq=qsnftdonate[x].quantity
    #         qsnftdonatetitle=qsnftdonate[x].title
    #         qsnftdonatetitleurl=qsnftdonate[x].titleurl
    #         nftdonateq.append(qsnftdonateq)
    #         nftdonatetitle.append(qsnftdonatetitle)
    #         nftdonatetitleurl.append(qsnftdonatetitleurl)

    #     nftdonatezip=zip(nftdonatetitle,nftdonateq,nftdonatetitleurl)
    # else:
    #     nftdonatezip=""
    ###############20210912
    try:
        qsnft=Pdfupload.objects.filter(email_address__icontains=request.user.email)
        if len(qsnft)>0:
            nfttitle=[]
            nfttitleurl=[]
            nfteach=[]
            nftcoll=0
            for x in range(len(qsnft)):
                qsnftemaillist=qsnft[x].nftpeopleemail
                qsnftdistribute=qsnft[x].nftdistribute
                qsnfttitle=qsnft[x].title
                qsnfttitleurl=qsnft[x].titleurl
                
                try:
                    qsindex=qsnftemaillist.index(qsnftemaillist)
                    eachnft=qsnftdistribute[qsindex]
                    nfttitle.append(qsnfttitle)
                    nfttitleurl.append(qsnfttitleurl)
                    nfteach.append(float(eachnft))
                    nftcoll+=1
                except:
                    pass
            
            nftzip=zip(nfttitle,nfteach,nfttitleurl)
            sumnft=sum(nfteach)
            
        else:
            nftzip=""
            sumnft=0
            nftcoll=0
    except:
        nftzip=""
        sumnft=0
        nftcoll=0

    #######################################################################
    #nft
    try:
        qsnftlist=nftlist.objects.filter(email_address=request.user.email)
        if len(qsnftlist)>0:
            nftlisttitle=[]
            nftlisttitleurl=[]
            nftlistq=[]
            nftlistp=[]
            for x in range(len(qsnftlist)):
                qsnftlistq=qsnftlist[x].quantity
                qsnftlisttitle=qsnftlist[x].title
                qsnftlisttitleurl=qsnftlist[x].titleurl
                qsnftlistp=qsnftlist[x].pricepernft
                nftlistq.append(qsnftlistq)
                nftlisttitle.append(qsnftlisttitle)
                nftlisttitleurl.append(qsnftlisttitleurl)
                nftlistp.append(qsnftlistp)

            nftlistzip=zip(nftlisttitle,nftlistq,nftlisttitleurl,nftlistp)
        else:
            nftlistzip=""
    except:
        nftlistzip=""

    try:
        qsnftbid=nftbid.objects.filter(email_address=request.user.email)
        if len(qsnftbid)>0:
            nftbidtitle=[]
            nftbidtitleurl=[]
            nftbidq=[]
            nftbidp=[]
            for x in range(len(qsnftbid)):
                qsnftbidq=qsnftbid[x].quantity
                qsnftbidtitle=qsnftbid[x].title
                qsnftbidtitleurl=qsnftbid[x].titleurl
                qsnftbidp=qsnftbid[x].pricepernft
                nftbidtitle.append(qsnftbidtitle)
                nftbidq.append(qsnftbidq)
                nftbidtitleurl.append(qsnftbidtitleurl)
                nftbidp.append(qsnftbidp)

            nftbidzip=zip(nftbidtitle,nftbidq,nftbidtitleurl,nftbidp)
        else:
            nftbidzip=""
    except:
        nftbidzip=""
    
    try:
        qsnftdonate=nftdonate.objects.filter(email_address=request.user.email)

        if len(qsnftdonate)>0:
            nftdonatetitle=[]
            nftdonatetitleurl=[]
            nftdonateq=[]
            for x in range(len(qsnftdonate)):
                qsnftdonateq=qsnftdonate[x].quantity
                qsnftdonatetitle=qsnftdonate[x].title
                qsnftdonatetitleurl=qsnftdonate[x].titleurl
                nftdonateq.append(qsnftdonateq)
                nftdonatetitle.append(qsnftdonatetitle)
                nftdonatetitleurl.append(qsnftdonatetitleurl)

            nftdonatezip=zip(nftdonatetitle,nftdonateq,nftdonatetitleurl)
        else:
            nftdonatezip=""   
    except:
        nftdonatezip=""


    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
            'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
            'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),
            #'cityinfo_json':cityinfo_json,
            #'conninfo_json':conninfo_json,
            #'coauthorinfo_json':coauthorinfo_json,
            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            # 'tree1_json':tree1_json,
            #'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,
            #'cityinfo_qs':cityinfo_qs,
            #'conninfo_qs':conninfo_qs,
            'coauthorinfo_qs':coauthorinfo_qs,
            #'cityinfo_json_new':cityinfo_json_new,
            'conninfo_json_new':conninfo_json_new,
            'coauthorinfo_json_new':coauthorinfo_json_new,
            'tmpcheck':tmpcheck,
            'check_token':check_token,
            'check_first_name':check_first_name,
            'check_last_name':check_last_name,
            'check_institution':check_institution,
            'check_department':check_department,
            'tmpcheck_listing':tmpcheck_listing,
            'check_email':check_email,
            'check_orcid':check_orcid,
            'check_gspi':check_gspi,
            'check_rcpi':check_rcpi,
            'referral_link':referral_link,
            #####
            'token':token,
            'tmptoken':tmptoken,
            'NFTToken':NFTToken,
            'nftzip':nftzip,
            'sumnft':sumnft,
            'nftcoll':nftcoll,
            'nftlistzip':nftlistzip,
            'nftbidzip':nftbidzip,
            'nftdonatezip':nftdonatezip,
            
        }
    
    return render(request, 'profile/network_coauthor.html', context)


def network_coauthor_query(request,user_url,affi):


    #authorabbr

    user_listing = get_object_or_404(Profile, userurl=user_url)

    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)


    print("幹你娘!")
    print(affi)
    affi=affi.strip()
    affi=affi=affi.replace('7',' ').replace('_','.').replace('8',',')

    # affi=affi.replace('-',' ').replace('_','.')
    
    csvpath='AA/static/scopus_match1.csv'
    scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')

    userurllist=scopusmatch['user_url'].values
    scopuslist=scopusmatch['scopus'].values
    dictmatch=dict(zip(userurllist,scopuslist))
    
    affi2=str(affi)+"#"
    articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url]).filter(authorabbr__contains=affi2)
    # affi3="#"+str(affi)
    # articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url]).filter(Q(authorabbr__contains=affi2) | Q(authorabbr__contains=affi3))
    #articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url]).filter(authoraffi__contains=str(affi)+'#')+articleinfo.objects.filter(profile=dictmatch[user_url]).filter(authoraffi__contains=+'#'+str(affi))
    print(articleinfo_qs)

    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])
    coauthorinfo_qs=MapCoauthorinfo.objects.filter(profile=dictmatch[user_url])
    countorigin=[]
    for i in range(len(cityinfo_qs)):
        countorigin.append(int(cityinfo_qs[i].countn))


    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    start = 5
    end = 10
    arr=countorigin
    if len(arr)>1:
        #print(arr)
        #print(len(arr))
        width = end - start
        if int(max(arr)-min(arr))!=0:
            res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        res=arr

    for i in range(len(cityinfo_qs)):
        cityinfo_qs[i].countn=res[i]

    cityinfo_json = serialize("json", cityinfo_qs)
    conninfo_json = serialize("json", conninfo_qs)
    coauthorinfo_json = serialize("json", coauthorinfo_qs)


    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()



    # with urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json') as response:
    #     tree1_json=response.read()



    profile1=[]
    for i in range(len(articleinfo_qs)):
        profile1.append(user_url) 

    journal=list(articleinfo_qs.values_list('journal', flat=True))
    year=list(articleinfo_qs.values_list('year', flat=True))
    title=list(articleinfo_qs.values_list('title', flat=True))
    titleurl=[slugify(x) for x in title]
    author=list(articleinfo_qs.values_list('authorabbr', flat=True))

    author=["; ".join(x.split('#')) for x in author]

    cite=list(articleinfo_qs.values_list('cite', flat=True))
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)

    articlein=zip(profile1,journal,year,title,author,cite1,titleurl)
    articlein=sorted(articlein,  key =operator.itemgetter(5,2,1), reverse=True)

    paginator = Paginator(articlein, 10)
    page = request.GET.get('page')
    paged_articlein = paginator.get_page(page)


    print(affi)

    context={
        'affi':affi,
        'articlein':articlein,
        'paged_articlein':paged_articlein,
        'user_url':user_url,
        'userurl':userurl,
        'user_listing':user_listing,

        'cityinfo_json':cityinfo_json,
        'conninfo_json':conninfo_json,
        'coauthorinfo_json':coauthorinfo_json,
        
    }
    return render(request, 'profile/network_coauthor_query.html', context)


def publication_citation91(request, user_url):

    user_listing = get_object_or_404(Profile, userurl=user_url)

    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    

    csvpath='AA/static/scopus_match1.csv'
    scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
    # print(scopusmatch.columns)
    # print(scopusmatch['scopus'].values)
    userurllist=scopusmatch['user_url'].values
    scopuslist=scopusmatch['scopus'].values
    dictmatch=dict(zip(userurllist,scopuslist))
    
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')

    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

######################20210103###################
    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    #print("幹")
    #print(cityinfo_qs)
    #print(len(cityinfo_qs))

    conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    countorigin=[]
    for i in range(len(cityinfo_qs)):
        tmpcityinfo=cityinfo_qs[i].asso
        #print(tmpcityinfo)
        cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
        countorigin.append(int(cityinfo_qs[i].countn))
    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    start = 5
    end = 10
    arr=countorigin
    if len(arr)>1:
        #print(arr)
        #print(len(arr))
        width = end - start
        if int(max(arr)-min(arr))!=0:
            res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        res=arr

    for i in range(len(cityinfo_qs)):
        cityinfo_qs[i].countn=res[i]

    cityinfo_json = serialize("json", cityinfo_qs)
    conninfo_json = serialize("json", conninfo_qs)

    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()

    # with urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json') as response:
    #     tree1_json=response.read()




    #article
    articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


    profile1=[]
    for i in range(len(articleinfo_qs)):
        profile1.append(user_url) 
    journal=list(articleinfo_qs.values_list('journal', flat=True))
    year=list(articleinfo_qs.values_list('year', flat=True))
    title=list(articleinfo_qs.values_list('title', flat=True))
    titleurl=[slugify(x) for x in title]
    author=list(articleinfo_qs.values_list('authorabbr', flat=True))

    author=["; ".join(x.split('#')) for x in author]
    cite=list(articleinfo_qs.values_list('cite', flat=True))
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)


    articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

    # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)

    articlein=sorted(articlein,  key=operator.itemgetter(5,2), reverse=True)
    print(articlein)

    paginator = Paginator(articlein, 10)
    page = request.GET.get('page')
    paged_articlein = paginator.get_page(page)



    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
            'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
            'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),
            'cityinfo_json':cityinfo_json,
            'conninfo_json':conninfo_json,
            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            # 'tree1_json':tree1_json,
            'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,

            'paged_articlein':paged_articlein,


        }
    
    return render(request, 'profile/publication_citation91.html', context)

def publication_citation19(request, user_url):

    user_listing = get_object_or_404(Profile, userurl=user_url)

    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    

    csvpath='AA/static/scopus_match1.csv'
    scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
    # print(scopusmatch.columns)
    # print(scopusmatch['scopus'].values)
    userurllist=scopusmatch['user_url'].values
    scopuslist=scopusmatch['scopus'].values
    dictmatch=dict(zip(userurllist,scopuslist))
    
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')

    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

######################20210103###################
    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    #print("幹")
    #print(cityinfo_qs)
    #print(len(cityinfo_qs))

    conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    countorigin=[]
    for i in range(len(cityinfo_qs)):
        tmpcityinfo=cityinfo_qs[i].asso
        #print(tmpcityinfo)
        cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
        countorigin.append(int(cityinfo_qs[i].countn))
    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    start = 5
    end = 10
    arr=countorigin
    if len(arr)>1:
        #print(arr)
        #print(len(arr))
        width = end - start
        if int(max(arr)-min(arr))!=0:
            res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        res=arr

    for i in range(len(cityinfo_qs)):
        cityinfo_qs[i].countn=res[i]

    cityinfo_json = serialize("json", cityinfo_qs)
    conninfo_json = serialize("json", conninfo_qs)

    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()

    # with urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json') as response:
    #     tree1_json=response.read()




    #article
    articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


    profile1=[]
    for i in range(len(articleinfo_qs)):
        profile1.append(user_url) 
    journal=list(articleinfo_qs.values_list('journal', flat=True))
    year=list(articleinfo_qs.values_list('year', flat=True))
    title=list(articleinfo_qs.values_list('title', flat=True))
    titleurl=[slugify(x) for x in title]
    author=list(articleinfo_qs.values_list('authorabbr', flat=True))

    author=["; ".join(x.split('#')) for x in author]
    cite=list(articleinfo_qs.values_list('cite', flat=True))
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)


    articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

    # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)

    articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=False)
    print(articlein)

    paginator = Paginator(articlein, 10)
    page = request.GET.get('page')
    paged_articlein = paginator.get_page(page)



    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
            'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
            'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),
            'cityinfo_json':cityinfo_json,
            'conninfo_json':conninfo_json,
            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            # 'tree1_json':tree1_json,
            'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,

            'paged_articlein':paged_articlein,


        }
    
    return render(request, 'profile/publication_citation19.html', context)


def publication_date91(request, user_url):

    user_listing = get_object_or_404(Profile, userurl=user_url)

    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    

    csvpath='AA/static/scopus_match1.csv'
    scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
    # print(scopusmatch.columns)
    # print(scopusmatch['scopus'].values)
    userurllist=scopusmatch['user_url'].values
    scopuslist=scopusmatch['scopus'].values
    dictmatch=dict(zip(userurllist,scopuslist))
    
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')

    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

######################20210103###################
    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    #print("幹")
    #print(cityinfo_qs)
    #print(len(cityinfo_qs))

    conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    countorigin=[]
    for i in range(len(cityinfo_qs)):
        tmpcityinfo=cityinfo_qs[i].asso
        #print(tmpcityinfo)
        cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
        countorigin.append(int(cityinfo_qs[i].countn))
    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    start = 5
    end = 10
    arr=countorigin
    if len(arr)>1:
        #print(arr)
        #print(len(arr))
        width = end - start
        if int(max(arr)-min(arr))!=0:
            res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        res=arr

    for i in range(len(cityinfo_qs)):
        cityinfo_qs[i].countn=res[i]

    cityinfo_json = serialize("json", cityinfo_qs)
    conninfo_json = serialize("json", conninfo_qs)

    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()

    # with urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json') as response:
    #     tree1_json=response.read()




    #article
    articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


    profile1=[]
    for i in range(len(articleinfo_qs)):
        profile1.append(user_url) 
    journal=list(articleinfo_qs.values_list('journal', flat=True))
    year=list(articleinfo_qs.values_list('year', flat=True))
    title=list(articleinfo_qs.values_list('title', flat=True))
    titleurl=[slugify(x) for x in title]
    author=list(articleinfo_qs.values_list('authorabbr', flat=True))

    author=["; ".join(x.split('#')) for x in author]
    cite=list(articleinfo_qs.values_list('cite', flat=True))
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)


    articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

    # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)

    articlein=sorted(articlein,  key=operator.itemgetter(2,5), reverse=True)
    print(articlein)

    paginator = Paginator(articlein, 10)
    page = request.GET.get('page')
    paged_articlein = paginator.get_page(page)



    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
            'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
            'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),
            'cityinfo_json':cityinfo_json,
            'conninfo_json':conninfo_json,
            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            # 'tree1_json':tree1_json,
            'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,

            'paged_articlein':paged_articlein,


        }
    
    return render(request, 'profile/publication_date91.html', context)


def publication_date19(request, user_url):

    user_listing = get_object_or_404(Profile, userurl=user_url)

    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    

    csvpath='AA/static/scopus_match1.csv'
    scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
    # print(scopusmatch.columns)
    # print(scopusmatch['scopus'].values)
    userurllist=scopusmatch['user_url'].values
    scopuslist=scopusmatch['scopus'].values
    dictmatch=dict(zip(userurllist,scopuslist))
    
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')

    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

######################20210103###################
    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    #print("幹")
    #print(cityinfo_qs)
    #print(len(cityinfo_qs))

    conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    countorigin=[]
    for i in range(len(cityinfo_qs)):
        tmpcityinfo=cityinfo_qs[i].asso
        #print(tmpcityinfo)
        cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
        countorigin.append(int(cityinfo_qs[i].countn))
    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    start = 5
    end = 10
    arr=countorigin
    if len(arr)>1:
        #print(arr)
        #print(len(arr))
        width = end - start
        if int(max(arr)-min(arr))!=0:
            res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        res=arr

    for i in range(len(cityinfo_qs)):
        cityinfo_qs[i].countn=res[i]

    cityinfo_json = serialize("json", cityinfo_qs)
    conninfo_json = serialize("json", conninfo_qs)

    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()

    # with urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json') as response:
    #     tree1_json=response.read()




    #article
    articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


    profile1=[]
    for i in range(len(articleinfo_qs)):
        profile1.append(user_url) 
    journal=list(articleinfo_qs.values_list('journal', flat=True))
    year=list(articleinfo_qs.values_list('year', flat=True))
    title=list(articleinfo_qs.values_list('title', flat=True))
    titleurl=[slugify(x) for x in title]
    author=list(articleinfo_qs.values_list('authorabbr', flat=True))

    author=["; ".join(x.split('#')) for x in author]
    cite=list(articleinfo_qs.values_list('cite', flat=True))
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)


    articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

    # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)

    articlein=sorted(articlein,  key=operator.itemgetter(2,1), reverse=False)
    print(articlein)

    paginator = Paginator(articlein, 10)
    page = request.GET.get('page')
    paged_articlein = paginator.get_page(page)



    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
            'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
            'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),
            'cityinfo_json':cityinfo_json,
            'conninfo_json':conninfo_json,
            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            # 'tree1_json':tree1_json,
            'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,

            'paged_articlein':paged_articlein,


        }
    
    return render(request, 'profile/publication_date19.html', context)


def publication_journalZA(request, user_url):

    user_listing = get_object_or_404(Profile, userurl=user_url)

    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    

    csvpath='AA/static/scopus_match1.csv'
    scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
    # print(scopusmatch.columns)
    # print(scopusmatch['scopus'].values)
    userurllist=scopusmatch['user_url'].values
    scopuslist=scopusmatch['scopus'].values
    dictmatch=dict(zip(userurllist,scopuslist))
    
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')

    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

######################20210103###################
    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    #print("幹")
    #print(cityinfo_qs)
    #print(len(cityinfo_qs))

    conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    countorigin=[]
    for i in range(len(cityinfo_qs)):
        tmpcityinfo=cityinfo_qs[i].asso
        #print(tmpcityinfo)
        cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
        countorigin.append(int(cityinfo_qs[i].countn))
    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    start = 5
    end = 10
    arr=countorigin
    if len(arr)>1:
        #print(arr)
        #print(len(arr))
        width = end - start
        if int(max(arr)-min(arr))!=0:
            res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        res=arr

    for i in range(len(cityinfo_qs)):
        cityinfo_qs[i].countn=res[i]

    cityinfo_json = serialize("json", cityinfo_qs)
    conninfo_json = serialize("json", conninfo_qs)

    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()


    # with urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json') as response:
    #     tree1_json=response.read()




    #article
    articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


    profile1=[]
    for i in range(len(articleinfo_qs)):
        profile1.append(user_url) 
    journal=list(articleinfo_qs.values_list('journal', flat=True))
    year=list(articleinfo_qs.values_list('year', flat=True))
    title=list(articleinfo_qs.values_list('title', flat=True))
    titleurl=[slugify(x) for x in title]
    author=list(articleinfo_qs.values_list('authorabbr', flat=True))

    author=["; ".join(x.split('#')) for x in author]
    cite=list(articleinfo_qs.values_list('cite', flat=True))
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)


    articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

    # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)

    articlein=sorted(articlein,  key=operator.itemgetter(1,2,5), reverse=True)
    print(articlein)

    paginator = Paginator(articlein, 10)
    page = request.GET.get('page')
    paged_articlein = paginator.get_page(page)



    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
            'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
            'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),
            'cityinfo_json':cityinfo_json,
            'conninfo_json':conninfo_json,
            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            # 'tree1_json':tree1_json,
            'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,

            'paged_articlein':paged_articlein,


        }
    
    return render(request, 'profile/publication_journalZA.html', context)


def publication_journalAZ(request, user_url):

    user_listing = get_object_or_404(Profile, userurl=user_url)

    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    

    csvpath='AA/static/scopus_match1.csv'
    scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
    # print(scopusmatch.columns)
    # print(scopusmatch['scopus'].values)
    userurllist=scopusmatch['user_url'].values
    scopuslist=scopusmatch['scopus'].values
    dictmatch=dict(zip(userurllist,scopuslist))
    
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')

    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

######################20210103###################
    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    #print("幹")
    #print(cityinfo_qs)
    #print(len(cityinfo_qs))

    conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    countorigin=[]
    for i in range(len(cityinfo_qs)):
        tmpcityinfo=cityinfo_qs[i].asso
        #print(tmpcityinfo)
        cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
        countorigin.append(int(cityinfo_qs[i].countn))
    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    start = 5
    end = 10
    arr=countorigin
    if len(arr)>1:
        #print(arr)
        #print(len(arr))
        width = end - start
        if int(max(arr)-min(arr))!=0:
            res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        res=arr

    for i in range(len(cityinfo_qs)):
        cityinfo_qs[i].countn=res[i]

    cityinfo_json = serialize("json", cityinfo_qs)
    conninfo_json = serialize("json", conninfo_qs)

    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()

    # with urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json') as response:
    #     tree1_json=response.read()




    #article
    articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


    profile1=[]
    for i in range(len(articleinfo_qs)):
        profile1.append(user_url) 
    journal=list(articleinfo_qs.values_list('journal', flat=True))
    year=list(articleinfo_qs.values_list('year', flat=True))
    title=list(articleinfo_qs.values_list('title', flat=True))
    titleurl=[slugify(x) for x in title]
    author=list(articleinfo_qs.values_list('authorabbr', flat=True))

    author=["; ".join(x.split('#')) for x in author]
    cite=list(articleinfo_qs.values_list('cite', flat=True))
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)


    articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

    # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)

    articlein=sorted(articlein,  key=operator.itemgetter(1,2), reverse=False)
    print(articlein)

    paginator = Paginator(articlein, 10)
    page = request.GET.get('page')
    paged_articlein = paginator.get_page(page)



    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
            'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
            'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),
            'cityinfo_json':cityinfo_json,
            'conninfo_json':conninfo_json,
            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            # 'tree1_json':tree1_json,
            'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,

            'paged_articlein':paged_articlein,


        }
    
    return render(request, 'profile/publication_journalAZ.html', context)


def hotspot(request, user_url):
    zero_time=time.time()
    #user_listing = get_object_or_404(Profile, userurl=user_url)
    searchid=int(user_url.split("-")[-1])
    #user_listing = get_object_or_404(Profile, userurl=user_url)
    #print(len(Profile_test.objects.all()))
    user_listing= Profile.objects.get(pk=searchid)
    #print("e04")
    print(user_listing.user_url)

    zero_time1=time.time()
    #print(zero_time1-zero_time)
    #print("get_object_or_404(Profile, userurl=user_url)")
    print(zero_time1-zero_time)

    try:
        tmpcheck_listing=Profile_token.objects.get(userurl=user_url)
        check_token=float(tmpcheck_listing.token)
        check_first_name=tmpcheck_listing.user_first_name
        check_last_name=tmpcheck_listing.user_last_name
        check_institution=tmpcheck_listing.user_institution
        check_department=tmpcheck_listing.user_department
        check_email=tmpcheck_listing.user_email
        check_orcid=tmpcheck_listing.orcid
        check_gspi=tmpcheck_listing.gspi
        check_rcpi=tmpcheck_listing.rcpi
        referral_link=tmpcheck_listing.referral_link
        tmpcheck=1

        token=float(tmpcheck_listing.token)
        tmptoken=float(tmpcheck_listing.tmptoken)
        NFTToken = float(tmpcheck_listing.token) - float(tmpcheck_listing.tmptoken)
    except: 
        tmpcheck=0
        check_token=float(0)
        check_first_name=""
        check_last_name=""
        check_institution=""
        check_department=""
        check_email=""
        check_orcid=""
        check_gspi=""
        check_rcpi=""
        referral_link=""
        tmpcheck_listing=user_listing

        token=float(0)
        tmptoken=float(0)
        NFTToken=float(0)
    

    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    

    # csvpath='static/scopus_match1.csv'
    # scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
    # # print(scopusmatch.columns)
    # # print(scopusmatch['scopus'].values)
    # userurllist=scopusmatch['user_url'].values
    # scopuslist=scopusmatch['scopus'].values
    # dictmatch=dict(zip(userurllist,scopuslist))
    
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')

    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    #cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

    ######################20210103###################
    #cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    #print("幹")
    #print(cityinfo_qs)
    #print(len(cityinfo_qs))

    #conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     tmpcityinfo=cityinfo_qs[i].asso
    #     #print(tmpcityinfo)
    #     cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
    #     countorigin.append(int(cityinfo_qs[i].countn))
    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     #print(arr)
    #     #print(len(arr))
    #     width = end - start
    #     if int(max(arr)-min(arr))!=0:
    #         res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    #     else:
    #         res=[x for x in arr]
    # else:
    #     res=arr

    # for i in range(len(cityinfo_qs)):
    #     cityinfo_qs[i].countn=res[i]

    # cityinfo_json = serialize("json", cityinfo_qs)
    # conninfo_json = serialize("json", conninfo_qs)

    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()

    # with urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json') as response:
    #     tree1_json=response.read()




    profile1=[]
    for i in range(len(user_listing.author.split('$'))):
        profile1.append(user_listing.user_url) 

    author=user_listing.authorabbr.split('$')
    author1=user_listing.authorabbr.split('$')
    title=user_listing.title.split('$')
    journal=user_listing.journal.split('$')
    year=user_listing.year.split('$')

    titleurl=[slugify(x) for x in title]
    author=["; ".join(x.split('#')) for x in author]
    cite=user_listing.cite.split('$')
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)

    abstract=user_listing.abstract.split('$')
    artoropen=user_listing.artoropen.split('$')
    volume=user_listing.volume.split('$')
    issue=user_listing.issue.split('$')
    pages=user_listing.pages.split('$')
    languages=user_listing.languages.split('$')
    publisher=user_listing.publisher.split('$')
    doi=user_listing.doi.split('$')
    titleslug=user_listing.titleslug.split('$')
    # citeyear=user_listing.citeyear.split('$')
    # try:
    #     citeyear=[int(x) for x in citeyear.split("#")]
    # except:
    #     citeyear=[0,0,0,0,0]

    # author=models.CharField(max_length=100000,default='0', blank=True)
    # title=models.CharField(max_length=10000,default='0', blank=True)
    # journal=models.CharField(max_length=5000,default='0', blank=True)
    # year=models.CharField(max_length=100,default='0', blank=True)
    # authorabbr=models.CharField(max_length=100000,default='0', blank=True)
    # artoropen=models.CharField(max_length=200,default='0', blank=True)
    # abstract=models.CharField(max_length=1000000,default='0', blank=True)
    # cite=models.CharField(max_length=100,default='0', blank=True)
    # citeyear=models.CharField(max_length=100,default='0', blank=True)
    # doi=models.CharField(max_length=1000,default='0', blank=True)
    # volume=models.CharField(max_length=500,default='0', blank=True)
    # issue=models.CharField(max_length=500,default='0', blank=True)
    # pages=models.CharField(max_length=500,default='0', blank=True)
    # languages=models.CharField(max_length=500,default='0', blank=True)
    # publisher=models.CharField(max_length=5000,default='0', blank=True)
    # titleslug=models.CharField(max_length=10000,default='0', blank=True)
    # authoraffi=models.CharField(max_length=100000,default='0', blank=True)
    #要新增的zip
    ###################################################################################
    ###################################################################################
    ###################################################################################
    #幹你娘要新增的20210705!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # citeyear=list(articleinfo_qs.values_list('citeyear', flat=True))[0]

    ###################################################################################
    ###################################################################################
    ###################################################################################
    #20210705要用到的從author1開始加!!!
    articlein=zip(profile1,journal,year,title,author,cite1,titleurl,abstract,author1,artoropen,volume,\
    issue,pages,languages,publisher,doi,titleslug)
    #print("幹幹幹1!")
    # #print(articlein)
    # for x in articlein:
    #     print("######################")
    #     print(x)

    ####感覺用form比較好!!!!!20210705
    ####use_django_global_variable
    # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)
    # print(len(profile1))

    #articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=True)[:10]
    articlein=list(articlein)[0:10]


    ###############20210912
    try:
        qsnft=Pdfupload.objects.filter(email_address__icontains=request.user.email)
        if len(qsnft)>0:
            nfttitle=[]
            nfttitleurl=[]
            nfteach=[]
            nftcoll=0
            for x in range(len(qsnft)):
                qsnftemaillist=qsnft[x].nftpeopleemail
                qsnftdistribute=qsnft[x].nftdistribute
                qsnfttitle=qsnft[x].title
                qsnfttitleurl=qsnft[x].titleurl
                
                try:
                    qsindex=qsnftemaillist.index(qsnftemaillist)
                    eachnft=qsnftdistribute[qsindex]
                    nfttitle.append(qsnfttitle)
                    nfttitleurl.append(qsnfttitleurl)
                    nfteach.append(float(eachnft))
                    nftcoll+=1
                except:
                    pass
            
            nftzip=zip(nfttitle,nfteach,nfttitleurl)
            sumnft=sum(nfteach)
            
        else:
            nftzip=""
            sumnft=0
            nftcoll=0
    except:
        nftzip=""
        sumnft=0
        nftcoll=0

    #######################################################################
    #nft
    try:
        qsnftlist=nftlist.objects.filter(email_address=request.user.email)
        if len(qsnftlist)>0:
            nftlisttitle=[]
            nftlisttitleurl=[]
            nftlistq=[]
            nftlistp=[]
            for x in range(len(qsnftlist)):
                qsnftlistq=qsnftlist[x].quantity
                qsnftlisttitle=qsnftlist[x].title
                qsnftlisttitleurl=qsnftlist[x].titleurl
                qsnftlistp=qsnftlist[x].pricepernft
                nftlistq.append(qsnftlistq)
                nftlisttitle.append(qsnftlisttitle)
                nftlisttitleurl.append(qsnftlisttitleurl)
                nftlistp.append(qsnftlistp)

            nftlistzip=zip(nftlisttitle,nftlistq,nftlisttitleurl,nftlistp)
        else:
            nftlistzip=""
    except:
        nftlistzip=""

    try:
        qsnftbid=nftbid.objects.filter(email_address=request.user.email)
        if len(qsnftbid)>0:
            nftbidtitle=[]
            nftbidtitleurl=[]
            nftbidq=[]
            nftbidp=[]
            for x in range(len(qsnftbid)):
                qsnftbidq=qsnftbid[x].quantity
                qsnftbidtitle=qsnftbid[x].title
                qsnftbidtitleurl=qsnftbid[x].titleurl
                qsnftbidp=qsnftbid[x].pricepernft
                nftbidtitle.append(qsnftbidtitle)
                nftbidq.append(qsnftbidq)
                nftbidtitleurl.append(qsnftbidtitleurl)
                nftbidp.append(qsnftbidp)

            nftbidzip=zip(nftbidtitle,nftbidq,nftbidtitleurl,nftbidp)
        else:
            nftbidzip=""
    except:
        nftbidzip=""
    
    try:
        qsnftdonate=nftdonate.objects.filter(email_address=request.user.email)

        if len(qsnftdonate)>0:
            nftdonatetitle=[]
            nftdonatetitleurl=[]
            nftdonateq=[]
            for x in range(len(qsnftdonate)):
                qsnftdonateq=qsnftdonate[x].quantity
                qsnftdonatetitle=qsnftdonate[x].title
                qsnftdonatetitleurl=qsnftdonate[x].titleurl
                nftdonateq.append(qsnftdonateq)
                nftdonatetitle.append(qsnftdonatetitle)
                nftdonatetitleurl.append(qsnftdonatetitleurl)

            nftdonatezip=zip(nftdonatetitle,nftdonateq,nftdonatetitleurl)
        else:
            nftdonatezip=""   
    except:
        nftdonatezip=""

    # qsnft=Pdfupload.objects.filter(email_address__icontains=request.user.email)
    # if len(qsnft)>0:
    #     nfttitle=[]
    #     nfttitleurl=[]
    #     nfteach=[]
    #     nftcoll=0
    #     for x in range(len(qsnft)):
    #         qsnftemaillist=qsnft[x].nftpeopleemail
    #         qsnftdistribute=qsnft[x].nftdistribute
    #         qsnfttitle=qsnft[x].title
    #         qsnfttitleurl=qsnft[x].titleurl
            
    #         try:
    #             qsindex=qsnftemaillist.index(qsnftemaillist)
    #             eachnft=qsnftdistribute[qsindex]
    #             nfttitle.append(qsnfttitle)
    #             nfttitleurl.append(qsnfttitleurl)
    #             nfteach.append(float(eachnft))
    #             nftcoll+=1
    #         except:
    #             pass
        
    #     nftzip=zip(nfttitle,nfteach,nfttitleurl)
    #     sumnft=sum(nfteach)
        
    # else:
    #     nftzip=""
    #     sumnft=0
    #     nftcoll=0


    # qsnftlist=nftlist.objects.filter(email_address=request.user.email)
    # if len(qsnftlist)>0:
    #     nftlisttitle=[]
    #     nftlisttitleurl=[]
    #     nftlistq=[]
    #     nftlistp=[]
    #     for x in range(len(qsnftlist)):
    #         qsnftlistq=qsnftlist[x].quantity
    #         qsnftlisttitle=qsnftlist[x].title
    #         qsnftlisttitleurl=qsnftlist[x].titleurl
    #         qsnftlistp=qsnftlist[x].pricepernft
    #         nftlistq.append(qsnftlistq)
    #         nftlisttitle.append(qsnftlisttitle)
    #         nftlisttitleurl.append(qsnftlisttitleurl)
    #         nftlistp.append(qsnftlistp)

    #     nftlistzip=zip(nftlisttitle,nftlistq,nftlisttitleurl,nftlistp)
    # else:
    #     nftlistzip=""

    # qsnftbid=nftbid.objects.filter(email_address=request.user.email)
    # if len(qsnftbid)>0:
    #     nftbidtitle=[]
    #     nftbidtitleurl=[]
    #     nftbidq=[]
    #     nftbidp=[]
    #     for x in range(len(qsnftbid)):
    #         qsnftbidq=qsnftbid[x].quantity
    #         qsnftbidtitle=qsnftbid[x].title
    #         qsnftbidtitleurl=qsnftbid[x].titleurl
    #         qsnftbidp=qsnftbid[x].pricepernft
    #         nftbidtitle.append(qsnftbidtitle)
    #         nftbidq.append(qsnftbidq)
    #         nftbidtitleurl.append(qsnftbidtitleurl)
    #         nftbidp.append(qsnftbidp)

    #     nftbidzip=zip(nftbidtitle,nftbidq,nftbidtitleurl,nftbidp)
    # else:
    #     nftbidzip=""
    
    # qsnftdonate=nftdonate.objects.filter(email_address=request.user.email)

    # if len(qsnftdonate)>0:
    #     nftdonatetitle=[]
    #     nftdonatetitleurl=[]
    #     nftdonateq=[]
    #     for x in range(len(qsnftdonate)):
    #         qsnftdonateq=qsnftdonate[x].quantity
    #         qsnftdonatetitle=qsnftdonate[x].title
    #         qsnftdonatetitleurl=qsnftdonate[x].titleurl
    #         nftdonateq.append(qsnftdonateq)
    #         nftdonatetitle.append(qsnftdonatetitle)
    #         nftdonatetitleurl.append(qsnftdonatetitleurl)

    #     nftdonatezip=zip(nftdonatetitle,nftdonateq,nftdonatetitleurl)
    # else:
    #     nftdonatezip=""



    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            'publish_datapath':'https://researchain.net/static/profile/%s_publisher.csv' %(user_url),
            'bubble_datapath':'https://researchain.net/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'https://researchain.net/static/profile/%s_cloud.json' %(user_url),
            'window_datapath':'https://researchain.net/static/profile/%s/window.json' %(user_url),
            #'cityinfo_json':cityinfo_json,
            #'conninfo_json':conninfo_json,
            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            # 'tree1_json':tree1_json,
            'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,
            'tmpcheck':tmpcheck,
            'check_token':check_token,
            'check_first_name':check_first_name,
            'check_last_name':check_last_name,
            'check_institution':check_institution,
            'check_department':check_department,
            'tmpcheck_listing':tmpcheck_listing,
            'check_email':check_email,
            'check_orcid':check_orcid,
            'check_gspi':check_gspi,
            'check_rcpi':check_rcpi,
            'referral_link':referral_link,
            #####
            'token':token,
            'tmptoken':tmptoken,
            'NFTToken':NFTToken,
            'nftzip':nftzip,
            'sumnft':sumnft,
            'nftcoll':nftcoll,
            'nftlistzip':nftlistzip,
            'nftbidzip':nftbidzip,
            'nftdonatezip':nftdonatezip,
        }
    
    return render(request, 'profile/hotspot.html', context)

def hotspot_bubble(request, user_url):

    user_listing = get_object_or_404(Profile, userurl=user_url)

    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    

    csvpath='AA/static/scopus_match1.csv'
    scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
    # print(scopusmatch.columns)
    # print(scopusmatch['scopus'].values)
    userurllist=scopusmatch['user_url'].values
    scopuslist=scopusmatch['scopus'].values
    dictmatch=dict(zip(userurllist,scopuslist))
    
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')

    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

######################20210103###################
    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    #print("幹")
    #print(cityinfo_qs)
    #print(len(cityinfo_qs))

    conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    countorigin=[]
    for i in range(len(cityinfo_qs)):
        tmpcityinfo=cityinfo_qs[i].asso
        #print(tmpcityinfo)
        cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
        countorigin.append(int(cityinfo_qs[i].countn))
    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    start = 5
    end = 10
    arr=countorigin
    if len(arr)>1:
        #print(arr)
        #print(len(arr))
        width = end - start
        if int(max(arr)-min(arr))!=0:
            res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        res=arr

    for i in range(len(cityinfo_qs)):
        cityinfo_qs[i].countn=res[i]

    cityinfo_json = serialize("json", cityinfo_qs)
    conninfo_json = serialize("json", conninfo_qs)

    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()


    # with urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json') as response:
    #     tree1_json=response.read()




    #article
    articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


    profile1=[]
    for i in range(len(articleinfo_qs)):
        profile1.append(user_url) 
    journal=list(articleinfo_qs.values_list('journal', flat=True))
    year=list(articleinfo_qs.values_list('year', flat=True))
    title=list(articleinfo_qs.values_list('title', flat=True))
    titleurl=[slugify(x) for x in title]
    author=list(articleinfo_qs.values_list('authorabbr', flat=True))

    author=["; ".join(x.split('#')) for x in author]
    cite=list(articleinfo_qs.values_list('cite', flat=True))
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)


    articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

    # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)

    articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=True)[:10]
    print(articlein)


    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
            'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
            'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),
            'cityinfo_json':cityinfo_json,
            'conninfo_json':conninfo_json,
            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            # 'tree1_json':tree1_json,
            'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,

        }
    
    return render(request, 'profile/hotspot_bubble.html', context)

def hotspot_wordcloud(request, user_url):

    zero_time=time.time()

    #user_listing = get_object_or_404(Profile, userurl=user_url)
    searchid=int(user_url.split("-")[-1])

    #user_listing = get_object_or_404(Profile, userurl=user_url)
    #print(len(Profile_test.objects.all()))
    user_listing= Profile.objects.get(pk=searchid)
    #print("e04")
    print(user_listing.user_url)

    zero_time1=time.time()
    #print(zero_time1-zero_time)
    #print("get_object_or_404(Profile, userurl=user_url)")
    print(zero_time1-zero_time)

    try:
        tmpcheck_listing=Profile_token.objects.get(userurl=user_url)
        check_token=float(tmpcheck_listing.token)
        check_first_name=tmpcheck_listing.user_first_name
        check_last_name=tmpcheck_listing.user_last_name
        check_institution=tmpcheck_listing.user_institution
        check_department=tmpcheck_listing.user_department
        check_email=tmpcheck_listing.user_email
        check_orcid=tmpcheck_listing.orcid
        check_gspi=tmpcheck_listing.gspi
        check_rcpi=tmpcheck_listing.rcpi
        referral_link=tmpcheck_listing.referral_link
        tmpcheck=1

        token=float(tmpcheck_listing.token)
        tmptoken=float(tmpcheck_listing.tmptoken)
        NFTToken = float(tmpcheck_listing.token) - float(tmpcheck_listing.tmptoken)
    except: 
        tmpcheck=0
        check_token=float(0)
        check_first_name=""
        check_last_name=""
        check_institution=""
        check_department=""
        check_email=""
        check_orcid=""
        check_gspi=""
        check_rcpi=""
        referral_link=""
        tmpcheck_listing=user_listing

        token=float(0)
        tmptoken=float(0)
        NFTToken=float(0)

    #print("#####################################################")
    user_url=user_listing.user_url
    userurl=user_listing.userurl

    
    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    

    # csvpath='AA/static/scopus_match1.csv'
    # scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
    # # print(scopusmatch.columns)
    # # print(scopusmatch['scopus'].values)
    # userurllist=scopusmatch['user_url'].values
    # scopuslist=scopusmatch['scopus'].values
    # dictmatch=dict(zip(userurllist,scopuslist))
    
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')

    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    #cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

    ######################20210103###################
    #cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    #print("幹")
    #print(cityinfo_qs)
    #print(len(cityinfo_qs))

    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     tmpcityinfo=cityinfo_qs[i].asso
    #     #print(tmpcityinfo)
    #     cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
    #     countorigin.append(int(cityinfo_qs[i].countn))
    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     #print(arr)
    #     #print(len(arr))
    #     width = end - start
    #     if int(max(arr)-min(arr))!=0:
    #         res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    #     else:
    #         res=[x for x in arr]
    # else:
    #     res=arr

    # for i in range(len(cityinfo_qs)):
    #     cityinfo_qs[i].countn=res[i]

    # cityinfo_json = serialize("json", cityinfo_qs)
    # conninfo_json = serialize("json", conninfo_qs)

    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()

    # with urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json') as response:
    #     tree1_json=response.read()




    profile1=[]
    for i in range(len(user_listing.author.split('$'))):
        profile1.append(user_listing.user_url) 

    author=user_listing.authorabbr.split('$')
    author1=user_listing.authorabbr.split('$')
    title=user_listing.title.split('$')
    journal=user_listing.journal.split('$')
    year=user_listing.year.split('$')

    titleurl=[slugify(x) for x in title]
    author=["; ".join(x.split('#')) for x in author]
    cite=user_listing.cite.split('$')
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)

    abstract=user_listing.abstract.split('$')
    artoropen=user_listing.artoropen.split('$')
    volume=user_listing.volume.split('$')
    issue=user_listing.issue.split('$')
    pages=user_listing.pages.split('$')
    languages=user_listing.languages.split('$')
    publisher=user_listing.publisher.split('$')
    doi=user_listing.doi.split('$')
    titleslug=user_listing.titleslug.split('$')
    # citeyear=user_listing.citeyear.split('$')
    # try:
    #     citeyear=[int(x) for x in citeyear.split("#")]
    # except:
    #     citeyear=[0,0,0,0,0]

    # author=models.CharField(max_length=100000,default='0', blank=True)
    # title=models.CharField(max_length=10000,default='0', blank=True)
    # journal=models.CharField(max_length=5000,default='0', blank=True)
    # year=models.CharField(max_length=100,default='0', blank=True)
    # authorabbr=models.CharField(max_length=100000,default='0', blank=True)
    # artoropen=models.CharField(max_length=200,default='0', blank=True)
    # abstract=models.CharField(max_length=1000000,default='0', blank=True)
    # cite=models.CharField(max_length=100,default='0', blank=True)
    # citeyear=models.CharField(max_length=100,default='0', blank=True)
    # doi=models.CharField(max_length=1000,default='0', blank=True)
    # volume=models.CharField(max_length=500,default='0', blank=True)
    # issue=models.CharField(max_length=500,default='0', blank=True)
    # pages=models.CharField(max_length=500,default='0', blank=True)
    # languages=models.CharField(max_length=500,default='0', blank=True)
    # publisher=models.CharField(max_length=5000,default='0', blank=True)
    # titleslug=models.CharField(max_length=10000,default='0', blank=True)
    # authoraffi=models.CharField(max_length=100000,default='0', blank=True)
    #要新增的zip
    ###################################################################################
    ###################################################################################
    ###################################################################################
    #幹你娘要新增的20210705!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # citeyear=list(articleinfo_qs.values_list('citeyear', flat=True))[0]

    ###################################################################################
    ###################################################################################
    ###################################################################################
    #20210705要用到的從author1開始加!!!
    articlein=zip(profile1,journal,year,title,author,cite1,titleurl,abstract,author1,artoropen,volume,\
    issue,pages,languages,publisher,doi,titleslug)
    #print("幹幹幹1!")
    # #print(articlein)
    # for x in articlein:
    #     print("######################")
    #     print(x)

    ####感覺用form比較好!!!!!20210705
    ####use_django_global_variable
    # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)
    # print(len(profile1))

    #articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=True)[:10]
    articlein=list(articlein)[0:10]

    ###############20210912
    try:
        qsnft=Pdfupload.objects.filter(email_address__icontains=request.user.email)
        if len(qsnft)>0:
            nfttitle=[]
            nfttitleurl=[]
            nfteach=[]
            nftcoll=0
            for x in range(len(qsnft)):
                qsnftemaillist=qsnft[x].nftpeopleemail
                qsnftdistribute=qsnft[x].nftdistribute
                qsnfttitle=qsnft[x].title
                qsnfttitleurl=qsnft[x].titleurl
                
                try:
                    qsindex=qsnftemaillist.index(qsnftemaillist)
                    eachnft=qsnftdistribute[qsindex]
                    nfttitle.append(qsnfttitle)
                    nfttitleurl.append(qsnfttitleurl)
                    nfteach.append(float(eachnft))
                    nftcoll+=1
                except:
                    pass
            
            nftzip=zip(nfttitle,nfteach,nfttitleurl)
            sumnft=sum(nfteach)
            
        else:
            nftzip=""
            sumnft=0
            nftcoll=0
    except:
        nftzip=""
        sumnft=0
        nftcoll=0

    #######################################################################
    #nft
    try:
        qsnftlist=nftlist.objects.filter(email_address=request.user.email)
        if len(qsnftlist)>0:
            nftlisttitle=[]
            nftlisttitleurl=[]
            nftlistq=[]
            nftlistp=[]
            for x in range(len(qsnftlist)):
                qsnftlistq=qsnftlist[x].quantity
                qsnftlisttitle=qsnftlist[x].title
                qsnftlisttitleurl=qsnftlist[x].titleurl
                qsnftlistp=qsnftlist[x].pricepernft
                nftlistq.append(qsnftlistq)
                nftlisttitle.append(qsnftlisttitle)
                nftlisttitleurl.append(qsnftlisttitleurl)
                nftlistp.append(qsnftlistp)

            nftlistzip=zip(nftlisttitle,nftlistq,nftlisttitleurl,nftlistp)
        else:
            nftlistzip=""
    except:
        nftlistzip=""

    try:
        qsnftbid=nftbid.objects.filter(email_address=request.user.email)
        if len(qsnftbid)>0:
            nftbidtitle=[]
            nftbidtitleurl=[]
            nftbidq=[]
            nftbidp=[]
            for x in range(len(qsnftbid)):
                qsnftbidq=qsnftbid[x].quantity
                qsnftbidtitle=qsnftbid[x].title
                qsnftbidtitleurl=qsnftbid[x].titleurl
                qsnftbidp=qsnftbid[x].pricepernft
                nftbidtitle.append(qsnftbidtitle)
                nftbidq.append(qsnftbidq)
                nftbidtitleurl.append(qsnftbidtitleurl)
                nftbidp.append(qsnftbidp)

            nftbidzip=zip(nftbidtitle,nftbidq,nftbidtitleurl,nftbidp)
        else:
            nftbidzip=""
    except:
        nftbidzip=""
    
    try:
        qsnftdonate=nftdonate.objects.filter(email_address=request.user.email)

        if len(qsnftdonate)>0:
            nftdonatetitle=[]
            nftdonatetitleurl=[]
            nftdonateq=[]
            for x in range(len(qsnftdonate)):
                qsnftdonateq=qsnftdonate[x].quantity
                qsnftdonatetitle=qsnftdonate[x].title
                qsnftdonatetitleurl=qsnftdonate[x].titleurl
                nftdonateq.append(qsnftdonateq)
                nftdonatetitle.append(qsnftdonatetitle)
                nftdonatetitleurl.append(qsnftdonatetitleurl)

            nftdonatezip=zip(nftdonatetitle,nftdonateq,nftdonatetitleurl)
        else:
            nftdonatezip=""   
    except:
        nftdonatezip=""

    #####################################################
    #########測試多個file 用try測試該資料夾!!!!
    #
    try:
        testcloudpath=r'/home/djangoadmin/pyapps/bestjobreviews/static/profile7/%s_cloud.json' %(user_url)
        f=open(testcloudpath)
        f.close()
        cloudpath='https://researchain.net/static/profile7/%s_cloud.json' %(user_url)
        #testresult="幹"
    except:
        cloudpath='https://researchain.net/static/profile/%s_cloud.json' %(user_url)
        #testresult="幹1"

    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            ##########改成fn=r"/home/djangoadmin/pyapps/bestjobreviews/static/loadNEW"
            ##############/mnt/volume_sfo2_02/profile_cloud
            ##############/mnt/volume_sfo2_02/profile_publisher
            'publish_datapath':'https://researchain.net/static/profile/%s_publisher.csv' %(user_url),
            'bubble_datapath':'https://researchain.net/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath': cloudpath,
            #'cloud_datapath':'/mnt/volume_sfo2_02/profile_cloud/%s_cloud.json' %(user_url), #20211015
            'window_datapath':'https://researchain.net/static/profile/%s/window.json' %(user_url),
            #'cityinfo_json':cityinfo_json,
            #'conninfo_json':conninfo_json,
            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            # 'tree1_json':tree1_json,
            'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,
            'tmpcheck':tmpcheck,
            'check_token':check_token,
            'check_first_name':check_first_name,
            'check_last_name':check_last_name,
            'check_institution':check_institution,
            'check_department':check_department,
            'tmpcheck_listing':tmpcheck_listing,
            'check_email':check_email,
            'check_orcid':check_orcid,
            'check_gspi':check_gspi,
            'check_rcpi':check_rcpi,
            'referral_link':referral_link,
            #####
            'token':token,
            'tmptoken':tmptoken,
            'NFTToken':NFTToken,
            'nftzip':nftzip,
            'sumnft':sumnft,
            'nftcoll':nftcoll,
            'nftlistzip':nftlistzip,
            'nftbidzip':nftbidzip,
            'nftdonatezip':nftdonatezip,
            #'testresult':testresult,

        }
    
    return render(request, 'profile/hotspot_wordcloud.html', context)

def hotspot_mosaic(request, user_url):

    user_listing = get_object_or_404(Profile, userurl=user_url)

    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    

    csvpath='AA/static/scopus_match1.csv'
    scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
    # print(scopusmatch.columns)
    # print(scopusmatch['scopus'].values)
    userurllist=scopusmatch['user_url'].values
    scopuslist=scopusmatch['scopus'].values
    dictmatch=dict(zip(userurllist,scopuslist))
    
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')

    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

######################20210103###################
    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    #print("幹")
    #print(cityinfo_qs)
    #print(len(cityinfo_qs))

    conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    countorigin=[]
    for i in range(len(cityinfo_qs)):
        tmpcityinfo=cityinfo_qs[i].asso
        #print(tmpcityinfo)
        cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
        countorigin.append(int(cityinfo_qs[i].countn))
    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    start = 5
    end = 10
    arr=countorigin
    if len(arr)>1:
        #print(arr)
        #print(len(arr))
        width = end - start
        if int(max(arr)-min(arr))!=0:
            res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        res=arr

    for i in range(len(cityinfo_qs)):
        cityinfo_qs[i].countn=res[i]

    cityinfo_json = serialize("json", cityinfo_qs)
    conninfo_json = serialize("json", conninfo_qs)

    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()

    # with urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json') as response:
    #     tree1_json=response.read()




    #article
    articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


    profile1=[]
    for i in range(len(articleinfo_qs)):
        profile1.append(user_url) 
    journal=list(articleinfo_qs.values_list('journal', flat=True))
    year=list(articleinfo_qs.values_list('year', flat=True))
    title=list(articleinfo_qs.values_list('title', flat=True))
    titleurl=[slugify(x) for x in title]
    author=list(articleinfo_qs.values_list('authorabbr', flat=True))

    author=["; ".join(x.split('#')) for x in author]
    cite=list(articleinfo_qs.values_list('cite', flat=True))
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)


    articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

    # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)

    articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=True)[:10]
    print(articlein)


    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
            'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
            'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),
            'cityinfo_json':cityinfo_json,
            'conninfo_json':conninfo_json,
            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            # 'tree1_json':tree1_json,
            'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,

        }
    
    return render(request, 'profile/hotspot_mosaic.html', context)

def collaboration(request, user_url):

    zero_time=time.time()

    #user_listing = get_object_or_404(Profile, userurl=user_url)
    searchid=int(user_url.split("-")[-1])

    #user_listing = get_object_or_404(Profile, userurl=user_url)
    #print(len(Profile_test.objects.all()))
    user_listing= Profile.objects.get(pk=searchid)
    #print("e04")
    print(user_listing.user_url)

    zero_time1=time.time()
    #print(zero_time1-zero_time)
    #print("get_object_or_404(Profile, userurl=user_url)")
    print(zero_time1-zero_time)
    #print("#####################################################")
    try:
        tmpcheck_listing=Profile_token.objects.get(userurl=user_url)
        check_token=float(tmpcheck_listing.token)
        check_first_name=tmpcheck_listing.user_first_name
        check_last_name=tmpcheck_listing.user_last_name
        check_institution=tmpcheck_listing.user_institution
        check_department=tmpcheck_listing.user_department
        check_email=tmpcheck_listing.user_email
        check_orcid=tmpcheck_listing.orcid
        check_gspi=tmpcheck_listing.gspi
        check_rcpi=tmpcheck_listing.rcpi
        referral_link=tmpcheck_listing.referral_link
        tmpcheck=1

        token=float(tmpcheck_listing.token)
        tmptoken=float(tmpcheck_listing.tmptoken)
        NFTToken = float(tmpcheck_listing.token) - float(tmpcheck_listing.tmptoken)
    except: 
        tmpcheck=0
        check_token=float(0)
        check_first_name=""
        check_last_name=""
        check_institution=""
        check_department=""
        check_email=""
        check_orcid=""
        check_gspi=""
        check_rcpi=""
        referral_link=""
        tmpcheck_listing=user_listing

        token=float(0)
        tmptoken=float(0)
        NFTToken=float(0)


    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    
    # # ###################################################################################20210811
    # csvpath='static/scopus_match1.csv'
    # #chunk=pd.read_csv(csvpath,sep='\t',encoding='utf-8', engine='python',chunksize=1000000)
    # scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8', engine='python')
    # #scopusmatch = pd.concat(chunk)
    # #print("pd.read_csv(csvpath,sep='\t',encoding='utf-8', engine='python')")
    # # print(scopusmatch.columns)
    # # print(scopusmatch['scopus'].values)
    # userurllist=scopusmatch['user_url'].values
    # scopuslist=scopusmatch['scopus'].values
    # dictmatch=dict(zip(userurllist,scopuslist))

    # userurllist1=userurllist
    # scopuslist1=scopuslist
    # scopuslist2=[x.replace('-',' ') for x in scopuslist1]
    # collabordict=dict(zip(scopuslist2,userurllist1))
    # # ###################################################################################20210811
    
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')

    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    #cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

######################20210103###################
    #cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    #print("幹")
    #print(cityinfo_qs)
    #print(len(cityinfo_qs))

    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     tmpcityinfo=cityinfo_qs[i].asso
    #     #print(tmpcityinfo)
    #     cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
    #     countorigin.append(int(cityinfo_qs[i].countn))
    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     #print(arr)
    #     #print(len(arr))
    #     width = end - start
    #     if int(max(arr)-min(arr))!=0:
    #         res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    #     else:
    #         res=[x for x in arr]
    # else:
    #     res=arr

    # for i in range(len(cityinfo_qs)):
    #     cityinfo_qs[i].countn=res[i]

    # cityinfo_json = serialize("json", cityinfo_qs)
    # conninfo_json = serialize("json", conninfo_qs)

    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()

    # with urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json') as response:
    #     tree1_json=response.read()




    #article
    # articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


    # profile1=[]
    # for i in range(len(articleinfo_qs)):
    #     profile1.append(user_url) 
    # journal=list(articleinfo_qs.values_list('journal', flat=True))
    # year=list(articleinfo_qs.values_list('year', flat=True))
    # title=list(articleinfo_qs.values_list('title', flat=True))
    # titleurl=[slugify(x) for x in title]
    # author=list(articleinfo_qs.values_list('authorabbr', flat=True))

    # author=["; ".join(x.split('#')) for x in author]
    # cite=list(articleinfo_qs.values_list('cite', flat=True))
    # cite1=[]
    # for x in cite:
    #     try:
    #         cite1.append(int(x))
    #     except:
    #         cite1.append(0)


    # articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

    # # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)

    # articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=True)[:10]
    # print(articlein)

    #connauthorinfo_qs=MapCoauthorinfo.objects.filter(profile=dictmatch[user_url])
    coauthor=user_listing.coauthor
    print("幹你娘機掰coauthor")
    try:
        coauthorname=coauthor.split('@')[0].split('#')
        #print("coauthorname:",coauthorname)
        coauthoraffi=coauthor.split('@')[1].split('#')
        coauthoritem=coauthor.split('@')[2].split('#')
        coauthoritem=[int(x) for x in coauthoritem]
        #coauthorahref=coauthor.split('@')[3].split('#')
        coauthorahref=['#' for x in coauthoritem ]
        coauthorahref1=coauthor.split('@')[4].split('*')
        coauthorahref2=[]
        for x in coauthorahref1:
            if x=="":
                coauthorahref2.append("#")
            else:
                coauthorahref2.append(x)
        #coauthorahref2=['#' for x in coauthorahref1 if x=='']
    except:
        coauthorname=[]
        coauthoraffi=[]
        coauthoritem=[]
        coauthorahref=[]
        coauthorahref2=[]

    coauthorzip=sorted(zip(coauthorname,coauthoraffi,coauthoritem,coauthorahref,coauthorahref2),key=lambda x: -x[2])
    #print(coauthorzip)

    paginator = Paginator(coauthorzip, 10)
    page = request.GET.get('page')
    paged_coauthorzip = paginator.get_page(page)

    ###############20210912
    try:
        qsnft=Pdfupload.objects.filter(email_address__icontains=request.user.email)
        if len(qsnft)>0:
            nfttitle=[]
            nfttitleurl=[]
            nfteach=[]
            nftcoll=0
            for x in range(len(qsnft)):
                qsnftemaillist=qsnft[x].nftpeopleemail
                qsnftdistribute=qsnft[x].nftdistribute
                qsnfttitle=qsnft[x].title
                qsnfttitleurl=qsnft[x].titleurl
                
                try:
                    qsindex=qsnftemaillist.index(qsnftemaillist)
                    eachnft=qsnftdistribute[qsindex]
                    nfttitle.append(qsnfttitle)
                    nfttitleurl.append(qsnfttitleurl)
                    nfteach.append(float(eachnft))
                    nftcoll+=1
                except:
                    pass
            
            nftzip=zip(nfttitle,nfteach,nfttitleurl)
            sumnft=sum(nfteach)
            
        else:
            nftzip=""
            sumnft=0
            nftcoll=0
    except:
        nftzip=""
        sumnft=0
        nftcoll=0

    #######################################################################
    #nft
    try:
        qsnftlist=nftlist.objects.filter(email_address=request.user.email)
        if len(qsnftlist)>0:
            nftlisttitle=[]
            nftlisttitleurl=[]
            nftlistq=[]
            nftlistp=[]
            for x in range(len(qsnftlist)):
                qsnftlistq=qsnftlist[x].quantity
                qsnftlisttitle=qsnftlist[x].title
                qsnftlisttitleurl=qsnftlist[x].titleurl
                qsnftlistp=qsnftlist[x].pricepernft
                nftlistq.append(qsnftlistq)
                nftlisttitle.append(qsnftlisttitle)
                nftlisttitleurl.append(qsnftlisttitleurl)
                nftlistp.append(qsnftlistp)

            nftlistzip=zip(nftlisttitle,nftlistq,nftlisttitleurl,nftlistp)
        else:
            nftlistzip=""
    except:
        nftlistzip=""

    try:
        qsnftbid=nftbid.objects.filter(email_address=request.user.email)
        if len(qsnftbid)>0:
            nftbidtitle=[]
            nftbidtitleurl=[]
            nftbidq=[]
            nftbidp=[]
            for x in range(len(qsnftbid)):
                qsnftbidq=qsnftbid[x].quantity
                qsnftbidtitle=qsnftbid[x].title
                qsnftbidtitleurl=qsnftbid[x].titleurl
                qsnftbidp=qsnftbid[x].pricepernft
                nftbidtitle.append(qsnftbidtitle)
                nftbidq.append(qsnftbidq)
                nftbidtitleurl.append(qsnftbidtitleurl)
                nftbidp.append(qsnftbidp)

            nftbidzip=zip(nftbidtitle,nftbidq,nftbidtitleurl,nftbidp)
        else:
            nftbidzip=""
    except:
        nftbidzip=""
    
    try:
        qsnftdonate=nftdonate.objects.filter(email_address=request.user.email)

        if len(qsnftdonate)>0:
            nftdonatetitle=[]
            nftdonatetitleurl=[]
            nftdonateq=[]
            for x in range(len(qsnftdonate)):
                qsnftdonateq=qsnftdonate[x].quantity
                qsnftdonatetitle=qsnftdonate[x].title
                qsnftdonatetitleurl=qsnftdonate[x].titleurl
                nftdonateq.append(qsnftdonateq)
                nftdonatetitle.append(qsnftdonatetitle)
                nftdonatetitleurl.append(qsnftdonatetitleurl)

            nftdonatezip=zip(nftdonatetitle,nftdonateq,nftdonatetitleurl)
        else:
            nftdonatezip=""   
    except:
        nftdonatezip=""

    # qsnft=Pdfupload.objects.filter(email_address__icontains=request.user.email)
    # if len(qsnft)>0:
    #     nfttitle=[]
    #     nfttitleurl=[]
    #     nfteach=[]
    #     nftcoll=0
    #     for x in range(len(qsnft)):
    #         qsnftemaillist=qsnft[x].nftpeopleemail
    #         qsnftdistribute=qsnft[x].nftdistribute
    #         qsnfttitle=qsnft[x].title
    #         qsnfttitleurl=qsnft[x].titleurl
            
    #         try:
    #             qsindex=qsnftemaillist.index(qsnftemaillist)
    #             eachnft=qsnftdistribute[qsindex]
    #             nfttitle.append(qsnfttitle)
    #             nfttitleurl.append(qsnfttitleurl)
    #             nfteach.append(float(eachnft))
    #             nftcoll+=1
    #         except:
    #             pass
        
    #     nftzip=zip(nfttitle,nfteach,nfttitleurl)
    #     sumnft=sum(nfteach)
        
    # else:
    #     nftzip=""
    #     sumnft=0
    #     nftcoll=0

    # #######################################################################
    # #nft
    # qsnftlist=nftlist.objects.filter(email_address=request.user.email)
    # if len(qsnftlist)>0:
    #     nftlisttitle=[]
    #     nftlisttitleurl=[]
    #     nftlistq=[]
    #     nftlistp=[]
    #     for x in range(len(qsnftlist)):
    #         qsnftlistq=qsnftlist[x].quantity
    #         qsnftlisttitle=qsnftlist[x].title
    #         qsnftlisttitleurl=qsnftlist[x].titleurl
    #         qsnftlistp=qsnftlist[x].pricepernft
    #         nftlistq.append(qsnftlistq)
    #         nftlisttitle.append(qsnftlisttitle)
    #         nftlisttitleurl.append(qsnftlisttitleurl)
    #         nftlistp.append(qsnftlistp)

    #     nftlistzip=zip(nftlisttitle,nftlistq,nftlisttitleurl,nftlistp)
    # else:
    #     nftlistzip=""

    # qsnftbid=nftbid.objects.filter(email_address=request.user.email)
    # if len(qsnftbid)>0:
    #     nftbidtitle=[]
    #     nftbidtitleurl=[]
    #     nftbidq=[]
    #     nftbidp=[]
    #     for x in range(len(qsnftbid)):
    #         qsnftbidq=qsnftbid[x].quantity
    #         qsnftbidtitle=qsnftbid[x].title
    #         qsnftbidtitleurl=qsnftbid[x].titleurl
    #         qsnftbidp=qsnftbid[x].pricepernft
    #         nftbidtitle.append(qsnftbidtitle)
    #         nftbidq.append(qsnftbidq)
    #         nftbidtitleurl.append(qsnftbidtitleurl)
    #         nftbidp.append(qsnftbidp)

    #     nftbidzip=zip(nftbidtitle,nftbidq,nftbidtitleurl,nftbidp)
    # else:
    #     nftbidzip=""
    
    # qsnftdonate=nftdonate.objects.filter(email_address=request.user.email)

    # if len(qsnftdonate)>0:
    #     nftdonatetitle=[]
    #     nftdonatetitleurl=[]
    #     nftdonateq=[]
    #     for x in range(len(qsnftdonate)):
    #         qsnftdonateq=qsnftdonate[x].quantity
    #         qsnftdonatetitle=qsnftdonate[x].title
    #         qsnftdonatetitleurl=qsnftdonate[x].titleurl
    #         nftdonateq.append(qsnftdonateq)
    #         nftdonatetitle.append(qsnftdonatetitle)
    #         nftdonatetitleurl.append(qsnftdonatetitleurl)

    #     nftdonatezip=zip(nftdonatetitle,nftdonateq,nftdonatetitleurl)
    # else:
    #     nftdonatezip=""


    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
            'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
            'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),
            #'cityinfo_json':cityinfo_json,
            #'conninfo_json':conninfo_json,
            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            # 'tree1_json':tree1_json,
            #'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,
            'coauthorzip':coauthorzip,
            'paged_coauthorzip':paged_coauthorzip,
            'tmpcheck':tmpcheck,
            'check_token':check_token,
            'check_first_name':check_first_name,
            'check_last_name':check_last_name,
            'check_institution':check_institution,
            'check_department':check_department,
            'tmpcheck_listing':tmpcheck_listing,
            'check_email':check_email,
            'check_orcid':check_orcid,
            'check_gspi':check_gspi,
            'check_rcpi':check_rcpi,
            'referral_link':referral_link,
            #####
            'token':token,
            'tmptoken':tmptoken,
            'NFTToken':NFTToken,
            'nftzip':nftzip,
            'sumnft':sumnft,
            'nftcoll':nftcoll,
            'nftlistzip':nftlistzip,
            'nftbidzip':nftbidzip,
            'nftdonatezip':nftdonatezip,

        }
    
    return render(request, 'profile/collaboration.html', context)

def collaboration_hierarchy(request, user_url):

    user_listing = get_object_or_404(Profile, userurl=user_url)

    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    

    csvpath='AA/static/scopus_match1.csv'
    scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
    # print(scopusmatch.columns)
    # print(scopusmatch['scopus'].values)
    userurllist=scopusmatch['user_url'].values
    scopuslist=scopusmatch['scopus'].values
    dictmatch=dict(zip(userurllist,scopuslist))
    
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')

    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

######################20210103###################
    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    #print("幹")
    #print(cityinfo_qs)
    #print(len(cityinfo_qs))

    conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    countorigin=[]
    for i in range(len(cityinfo_qs)):
        tmpcityinfo=cityinfo_qs[i].asso
        #print(tmpcityinfo)
        cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
        countorigin.append(int(cityinfo_qs[i].countn))
    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    start = 5
    end = 10
    arr=countorigin
    if len(arr)>1:
        #print(arr)
        #print(len(arr))
        width = end - start
        if int(max(arr)-min(arr))!=0:
            res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        res=arr

    for i in range(len(cityinfo_qs)):
        cityinfo_qs[i].countn=res[i]

    cityinfo_json = serialize("json", cityinfo_qs)
    conninfo_json = serialize("json", conninfo_qs)

    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()

    # with urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json') as response:
    #     tree1_json=response.read()


    f=open('AA/static/profile/%s/tree.json' %(user_url),'r') 
    tree1_json=f.read()

    f.close()




    #article
    articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


    profile1=[]
    for i in range(len(articleinfo_qs)):
        profile1.append(user_url) 
    journal=list(articleinfo_qs.values_list('journal', flat=True))
    year=list(articleinfo_qs.values_list('year', flat=True))
    title=list(articleinfo_qs.values_list('title', flat=True))
    titleurl=[slugify(x) for x in title]
    author=list(articleinfo_qs.values_list('authorabbr', flat=True))

    author=["; ".join(x.split('#')) for x in author]
    cite=list(articleinfo_qs.values_list('cite', flat=True))
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)


    articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

    # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)

    articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=True)[:10]
    print(articlein)


    connauthorinfo_qs=MapCoauthorinfo.objects.filter(profile=dictmatch[user_url])
    print("幹幹幹!")
    coauthorstr=list(connauthorinfo_qs.values_list('coauthor', flat=True))[0]
    #print(coauthorstr.split('$')[0])
    
    coauthorname=[]
    coauthoraffi=[]
    coauthoritem=[]
    coauthorahref=[]
    #   var tmp=NewArray[i].split("#")[0].split('&')[0];
    #                     var tmp2=NewArray[i].split("#")[0].split('&')[1];
    #                     var tmp1=tmp.split(" ").join("7").replace('.','_').replace(',','8');
    #                     //var tmp1="test";
    #                     var userurl='{{user_url}}';
    #                     //console.log(userurl);
    #                     var ttt='<a href= "http://127.0.0.1:8000/profile/'+userurl+'/network-affliation/'+tmp1+'">';
    for k in range(len(coauthorstr.split('$'))):
        coauthorname.append(coauthorstr.split('$')[k].split('#')[0].split('&')[0])
        coauthoraffi.append(coauthorstr.split('$')[k].split('#')[0].split('&')[1])
        coauthoritem.append(int(coauthorstr.split('$')[k].split('#')[-1]))
        tmpname=coauthorstr.split('$')[k].split('#')[0].split('&')[0]
        # print(tmpname.split(" "))
        # ['Liao,', 'Y.-M']
        # Liao87Y_-M
        tmp1="7".join(tmpname.split(" ")).replace('.','_').replace(',','8')
        
        coauthorahref.append("/profile/%s/network-coauthor/%s" %(userurl,tmp1))
    
    coauthorzip=sorted(zip(coauthorname,coauthoraffi,coauthoritem,coauthorahref),key=lambda x: -x[2])

    paginator = Paginator(coauthorzip, 10)
    page = request.GET.get('page')
    paged_coauthorzip = paginator.get_page(page)


    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
            'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
            'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),
            'cityinfo_json':cityinfo_json,
            'conninfo_json':conninfo_json,
            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            'tree1_json':tree1_json,
            'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,
            'paged_coauthorzip':paged_coauthorzip,

        }
    
    return render(request, 'profile/collaboration_hierarchy.html', context)

def collaboration_tree(request, user_url):

    user_listing = get_object_or_404(Profile, userurl=user_url)

    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    

    csvpath='AA/static/scopus_match1.csv'
    scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
    # print(scopusmatch.columns)
    # print(scopusmatch['scopus'].values)
    userurllist=scopusmatch['user_url'].values
    scopuslist=scopusmatch['scopus'].values
    dictmatch=dict(zip(userurllist,scopuslist))
    
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')

    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

######################20210103###################
    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    #print("幹")
    #print(cityinfo_qs)
    #print(len(cityinfo_qs))

    conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    countorigin=[]
    for i in range(len(cityinfo_qs)):
        tmpcityinfo=cityinfo_qs[i].asso
        #print(tmpcityinfo)
        cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
        countorigin.append(int(cityinfo_qs[i].countn))
    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    start = 5
    end = 10
    arr=countorigin
    if len(arr)>1:
        #print(arr)
        #print(len(arr))
        width = end - start
        if int(max(arr)-min(arr))!=0:
            res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        res=arr

    for i in range(len(cityinfo_qs)):
        cityinfo_qs[i].countn=res[i]

    cityinfo_json = serialize("json", cityinfo_qs)
    conninfo_json = serialize("json", conninfo_qs)

    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()

    f=open('AA/static/profile/%s/tree.json' %(user_url),'r') 
    tree1_json=f.read()

    f.close()

    # f = urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json')
    # tree1_json=f.read()

    # f.close()

    # link = 'http://127.0.0.1:8000/static/profile/%s/tree.json' %(user_url)



    # with urllib.request.urlopen(link) as response:
    #     tree1_json=response.read().decode('utf-8')

    #     response.close



    # request = urllib.request.urlopen("http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json")
    # data = json.load(request)
    # print(data)

    # r = requests.get('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json')
    # tree1_json = r.json()
    # print("222222222222222222222222222222222222222")
    # print(tree1_json)







    #article
    articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


    profile1=[]
    for i in range(len(articleinfo_qs)):
        profile1.append(user_url) 
    journal=list(articleinfo_qs.values_list('journal', flat=True))
    year=list(articleinfo_qs.values_list('year', flat=True))
    title=list(articleinfo_qs.values_list('title', flat=True))
    titleurl=[slugify(x) for x in title]
    author=list(articleinfo_qs.values_list('authorabbr', flat=True))

    author=["; ".join(x.split('#')) for x in author]
    cite=list(articleinfo_qs.values_list('cite', flat=True))
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)


    articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

    # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)

    articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=True)[:10]
    print(articlein)

    connauthorinfo_qs=MapCoauthorinfo.objects.filter(profile=dictmatch[user_url])
    print("幹幹幹!")
    coauthorstr=list(connauthorinfo_qs.values_list('coauthor', flat=True))[0]
    #print(coauthorstr.split('$')[0])
    
    coauthorname=[]
    coauthoraffi=[]
    coauthoritem=[]
    coauthorahref=[]
    #   var tmp=NewArray[i].split("#")[0].split('&')[0];
    #                     var tmp2=NewArray[i].split("#")[0].split('&')[1];
    #                     var tmp1=tmp.split(" ").join("7").replace('.','_').replace(',','8');
    #                     //var tmp1="test";
    #                     var userurl='{{user_url}}';
    #                     //console.log(userurl);
    #                     var ttt='<a href= "http://127.0.0.1:8000/profile/'+userurl+'/network-affliation/'+tmp1+'">';
    for k in range(len(coauthorstr.split('$'))):
        coauthorname.append(coauthorstr.split('$')[k].split('#')[0].split('&')[0])
        coauthoraffi.append(coauthorstr.split('$')[k].split('#')[0].split('&')[1])
        coauthoritem.append(int(coauthorstr.split('$')[k].split('#')[-1]))
        tmpname=coauthorstr.split('$')[k].split('#')[0].split('&')[0]
        # print(tmpname.split(" "))
        # ['Liao,', 'Y.-M']
        # Liao87Y_-M
        tmp1="7".join(tmpname.split(" ")).replace('.','_').replace(',','8')
        
        coauthorahref.append("/profile/%s/network-coauthor/%s" %(userurl,tmp1))
    
    coauthorzip=sorted(zip(coauthorname,coauthoraffi,coauthoritem,coauthorahref),key=lambda x: -x[2])

    paginator = Paginator(coauthorzip, 10)
    page = request.GET.get('page')
    paged_coauthorzip = paginator.get_page(page)


    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
            'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
            'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),
            'cityinfo_json':cityinfo_json,
            'conninfo_json':conninfo_json,
            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            'tree1_json':tree1_json,
            'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,
            'paged_coauthorzip':paged_coauthorzip,

        }
    
    return render(request, 'profile/collaboration_tree.html', context)

def collaboration_net(request, user_url):

    user_listing = get_object_or_404(Profile, userurl=user_url)

    user_url=user_listing.user_url
    userurl=user_listing.userurl

    if request.method == 'POST':
        user_email=request.user.email
        avatarStyle = request.POST.get('avatarStyle')
        topType = request.POST.get('topType')
        accessoriesType = request.POST.get('accessoriesType')
        hairColor = request.POST.get('hairColor')
        hatColor = request.POST.get('hatColor')
        facialHairType = request.POST.get('facialHairType')
        facialHairColor = request.POST.get('facialHairColor')
        clotheType = request.POST.get('clotheType')
        clotheColor = request.POST.get('clotheColor')
        graphicType = request.POST.get('graphicType')
        eyeType = request.POST.get('eyeType')
        eyebrowType = request.POST.get('eyebrowType')
        mouthType = request.POST.get('mouthType')
        skinColor = request.POST.get('skinColor')
        Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

        URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


        return redirect('profile', URL)

    

    csvpath='AA/static/scopus_match1.csv'
    scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
    # print(scopusmatch.columns)
    # print(scopusmatch['scopus'].values)
    userurllist=scopusmatch['user_url'].values
    scopuslist=scopusmatch['scopus'].values
    dictmatch=dict(zip(userurllist,scopuslist))
    
 
    #trend
    # trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
    # cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
    # docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
    # citedata=cite.split('#')
    # docyear=docu.split('#')

    #impact
    # trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
    # impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
    # docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
    # ifdata=impact.split('#')
    # docyear=docu.split('#')

    #publisher
    # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
    # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
    # publisher=publisher.split('#') 


    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


    # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    # countorigin=[]
    # for i in range(len(cityinfo_qs)):
    #     countorigin.append(int(cityinfo_qs[i].countn))

######################20210103###################
    cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
    #print("幹")
    #print(cityinfo_qs)
    #print(len(cityinfo_qs))

    conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

    countorigin=[]
    for i in range(len(cityinfo_qs)):
        tmpcityinfo=cityinfo_qs[i].asso
        #print(tmpcityinfo)
        cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
        countorigin.append(int(cityinfo_qs[i].countn))
    # start = 5
    # end = 10
    # arr=countorigin
    # if len(arr)>1:
    #     print(arr)
    #     print(len(arr))
    #     width = end - start
    #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
    # else:
    #     res=[arr for x in arr][0]

    start = 5
    end = 10
    arr=countorigin
    if len(arr)>1:
        #print(arr)
        #print(len(arr))
        width = end - start
        if int(max(arr)-min(arr))!=0:
            res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
        else:
            res=[x for x in arr]
    else:
        res=arr

    for i in range(len(cityinfo_qs)):
        cityinfo_qs[i].countn=res[i]

    cityinfo_json = serialize("json", cityinfo_qs)
    conninfo_json = serialize("json", conninfo_qs)

    # f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
    # tree1_json=f.read()

    # f.close()


    f=open('AA/static/profile/%s/tree.json' %(user_url),'r') 
    tree1_json=f.read()

    f.close()

    # with urllib.request.urlopen('http://127.0.0.1:8000/static/profile/Zhi-Ming-Zuo-Teng-2573453050/tree.json') as response:
    #     tree1_json=response.read()




    #article
    articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


    profile1=[]
    for i in range(len(articleinfo_qs)):
        profile1.append(user_url) 
    journal=list(articleinfo_qs.values_list('journal', flat=True))
    year=list(articleinfo_qs.values_list('year', flat=True))
    title=list(articleinfo_qs.values_list('title', flat=True))
    titleurl=[slugify(x) for x in title]
    author=list(articleinfo_qs.values_list('authorabbr', flat=True))

    author=["; ".join(x.split('#')) for x in author]
    cite=list(articleinfo_qs.values_list('cite', flat=True))
    cite1=[]
    for x in cite:
        try:
            cite1.append(int(x))
        except:
            cite1.append(0)


    articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

    # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)

    articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=True)[:10]
    print(articlein)

    connauthorinfo_qs=MapCoauthorinfo.objects.filter(profile=dictmatch[user_url])
    print("幹幹幹!")
    coauthorstr=list(connauthorinfo_qs.values_list('coauthor', flat=True))[0]
    #print(coauthorstr.split('$')[0])
    
    coauthorname=[]
    coauthoraffi=[]
    coauthoritem=[]
    coauthorahref=[]
    #   var tmp=NewArray[i].split("#")[0].split('&')[0];
    #                     var tmp2=NewArray[i].split("#")[0].split('&')[1];
    #                     var tmp1=tmp.split(" ").join("7").replace('.','_').replace(',','8');
    #                     //var tmp1="test";
    #                     var userurl='{{user_url}}';
    #                     //console.log(userurl);
    #                     var ttt='<a href= "http://127.0.0.1:8000/profile/'+userurl+'/network-affliation/'+tmp1+'">';
    for k in range(len(coauthorstr.split('$'))):
        coauthorname.append(coauthorstr.split('$')[k].split('#')[0].split('&')[0])
        coauthoraffi.append(coauthorstr.split('$')[k].split('#')[0].split('&')[1])
        coauthoritem.append(int(coauthorstr.split('$')[k].split('#')[-1]))
        tmpname=coauthorstr.split('$')[k].split('#')[0].split('&')[0]
        # print(tmpname.split(" "))
        # ['Liao,', 'Y.-M']
        # Liao87Y_-M
        tmp1="7".join(tmpname.split(" ")).replace('.','_').replace(',','8')
        
        coauthorahref.append("/profile/%s/network-coauthor/%s" %(userurl,tmp1))
    
    coauthorzip=sorted(zip(coauthorname,coauthoraffi,coauthoritem,coauthorahref),key=lambda x: -x[2])

    paginator = Paginator(coauthorzip, 10)
    page = request.GET.get('page')
    paged_coauthorzip = paginator.get_page(page)


    context = {
            'user_listing':user_listing,
            # 'citedata':citedata,
            # 'docyear':docyear,
            # 'ifdata':ifdata,
            # 'publisher':publisher,
            'publish_datapath':'http://127.0.0.1:8000/static/profile/%s/publisher.csv' %(user_url),
            'bubble_datapath':'http://127.0.0.1:8000/static/profile/%s/bubble.json' %(user_url),
            'cloud_datapath':'http://127.0.0.1:8000/static/profile/%s/cloud.json' %(user_url),
            'window_datapath':'http://127.0.0.1:8000/static/profile/%s/window.json' %(user_url),
            'cityinfo_json':cityinfo_json,
            'conninfo_json':conninfo_json,
            'network_datapath':'http://127.0.0.1:8000/static/profile/%s/net.json' %(user_url),
            'tree1_json':tree1_json,
            'articlein':articlein,
            'user_url':user_url,
            'userurl':userurl,
            'paged_coauthorzip':paged_coauthorzip,

        }
    
    return render(request, 'profile/collaboration_net.html', context)



































# def publication(request, user_url):

#     user_listing = get_object_or_404(Profile, user_url=user_url)

#     context = {
#         'user_listing':user_listing,
#     } 
 
#     return render(request, 'profile/publication.html', context)


# def trend(request):


#     trendcitadocu_qs=TrendCitaDocu.objects.filter(profile='Liao, Yuming')
#     cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
#     docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
#     citedata=cite.split('#')
#     docyear=docu.split('#')
    
#     context = {
            # 'citedata':citedata,
#             'docyear':docyear,
#         } 
 
#     return render(request, 'profile/trend.html', context)

# def impact(request):

#     trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile='Liao, Yuming')
    
#     impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
#     docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
#     ifdata=impact.split('#')
#     docyear=docu.split('#')
    

#     context = {
#             'ifdata':ifdata,
#             'docyear':docyear

#         } 

#     return render(request, 'profile/impact.html', context)


# def publisher(request):
    
#     trendpublisher_qs=TrendPublisher.objects.filter(profile='Liao, Yuming')
#     publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
#     publisher=publisher.split('#') 
#     context = {
            # 'publisher':publisher,
#         } 
#     return render(request, 'profile/publisher.html',context)


# def hotspot(request, user_url):

#     user_listing = get_object_or_404(Profile, user_url=user_url)

#     context = {
#         'user_listing':user_listing,
#     } 


#     return render(request, 'profile/bubble.html', context)




# def bubble(request):



#     context = {
          

#         } 
 
#     return render(request, 'profile/bubble.html',context)



# def cloud(request):


 
#     return render(request, 'profile/cloud.html')


# def window(request):


 
#     return render(request, 'profile/window.html')



# def network(request, user_url):

#     user_listing = get_object_or_404(Profile, user_url=user_url)

#     context = {
#         'user_listing':user_listing,
#     } 



 
#     return render(request, 'profile/map.html', context)



# def map(request):

#     cityinfo_qs=MapCityinfo.objects.filter(profile='Liao, Yuming')

#     print(cityinfo_qs)

#     conninfo_qs=MapConninfo.objects.filter(profile='Liao, Yuming')

#     countorigin=[]
#     for i in range(len(cityinfo_qs)):
#         countorigin.append(int(cityinfo_qs[i].countn))
#         #print(cityinfo_qs[i].countn)

#     start = 5
#     end = 10
#     arr=countorigin
#     width = end - start
#     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
#     #print(res)

#     for i in range(len(cityinfo_qs)):
#         cityinfo_qs[i].countn=res[i]

#     cityinfo_json = serialize("json", cityinfo_qs)
#     conninfo_json = serialize("json", conninfo_qs)
 
#     context = {     
#             'cityinfo_json':cityinfo_json,
#             'conninfo_json':conninfo_json,
#         } 
            
 
#     return render(request, 'profile/map.html', context)



# def net(request):


 
#     return render(request, 'profile/net.html')


# def tree(request):

#     f=open('AA/static/%s/tree.json' %("Liao, Yuming".replace(', ','-')),'r') 
#     tree1_json=f.read()

#     f.close()
   
  
#     context = {            
#             'tree1_json':tree1_json,
#         } 
 
#     return render(request, 'profile/tree.html',context)




# def profile(request, user_url):



#     user_listing = get_object_or_404(Profile, user_url=user_url)

#     if request.method == 'POST':
#         user_email=request.user.email
#         avatarStyle = request.POST.get('avatarStyle')
#         topType = request.POST.get('topType')
#         accessoriesType = request.POST.get('accessoriesType')
#         hairColor = request.POST.get('hairColor')
#         hatColor = request.POST.get('hatColor')
#         facialHairType = request.POST.get('facialHairType')
#         facialHairColor = request.POST.get('facialHairColor')
#         clotheType = request.POST.get('clotheType')
#         clotheColor = request.POST.get('clotheColor')
#         graphicType = request.POST.get('graphicType')
#         eyeType = request.POST.get('eyeType')
#         eyebrowType = request.POST.get('eyebrowType')
#         mouthType = request.POST.get('mouthType')
#         skinColor = request.POST.get('skinColor')
#         Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

#         URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


#         return redirect('profile', URL)
        
      

        





#     context = {
#         'user_listing':user_listing,
#     } 
            
    
    
#     return render(request, 'profile/profile_listing.html', context)


# def onboarding(request):

    

#     if request.user.is_authenticated:


#         Email=Profile.objects.filter(user_email=request.user.email)

#         if len(Email) == 0: 

#             if request.method == 'POST':

#                 user_email = request.POST.get('user_email')
#                 user_first_name = request.POST.get('user_first_name')
#                 user_middle_name = request.POST.get('user_middle_name')
#                 user_last_name = request.POST.get('user_last_name')
#                 user_institution = request.POST.get('user_institution')
#                 user_department = request.POST.get('user_department')
#                 user_position = request.POST.get('user_position')
#                 google_scholar = request.POST.get('google_scholar')
#                 researchgate = request.POST.get('researchgate')
#                 other = request.POST.get('other')

#                 user_url=user_first_name+'-'+user_last_name

#                 profile = Profile.objects.create(user_email=user_email, user_first_name=user_first_name, user_middle_name=user_middle_name, user_last_name=user_last_name, user_institution=user_institution, user_department=user_department, user_position=user_position, google_scholar=google_scholar, researchgate=researchgate, other=other,user_url=user_url)


#                 profile.save()

#                 return redirect('profile', user_url=user_url)

#             return render(request, 'profile/onboarding.html')

#         URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


#         return redirect('profile', URL)


#     else:
#         return redirect('account_login')




# def test(request):
#     arxiv_qs=Arxiv.objects.filter(title='Going_deeper_with_convolutions')
#     #print(arxiv_qs)
#     parag=list(arxiv_qs.values_list('parag', flat=True))[0]
#     reference=list(arxiv_qs.values_list('reference', flat=True))[0]
#     table=list(arxiv_qs.values_list('table', flat=True))[0]

#     #docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
#     #m=re.search('[10]',parag).group()
#     text_to_search = parag
#     pattern=re.compile(r'\[\d{1,2}\]')
#     matches=pattern.finditer(text_to_search)
#     #tmpsection=[]
#     pppnew=text_to_search
#     replist=[]
#     for match in matches:
#         #print(match)
#         #if match:
        
#         a=match.span()[0]
#         b=match.span()[1]
#         #print(text_to_search[a:b])
#         replist.append(text_to_search[a:b])
#         #ppp.replace
#     #print(list(set(replist)))
#     for i in range(len(list(set(replist)))):
        
#         pppnew=pppnew.replace(list(set(replist))[i],'<a href="#%s">%s</a>' %(list(set(replist))[i],list(set(replist))[i]))
#         #tmpsection.append((a,b))
    
    
#     # pppnew=text_to_search

#     # pppnew=pppnew.replace('###','<br><br>')
#     ###############table
#     text_to_search = pppnew
#     pattern=re.compile(r'Table\s{0,1}\d{1,2}')
#     matches=pattern.finditer(text_to_search)
#     pppnew1=text_to_search
#     for match in matches:
#         #print(match)
#         #if match:
#         a=match.span()[0]
#         b=match.span()[1]
#         #print(text_to_search[a:b])
#         #ppp.replace
#         pppnew1=pppnew1.replace(text_to_search[a:b],'<a href="#%s">%s</a>' %(text_to_search[a:b],text_to_search[a:b]))
#     #tmpsection=[]
#     pppnew=pppnew1

#     pppnew=pppnew.replace('###','<br><br>')

#     ###################################################################################################
#     text_to_search = reference
#     pattern=re.compile(r'\[\d{1,2}\]')
#     matches=pattern.finditer(text_to_search)
#     ppp1=text_to_search
#     for match in matches:
#         #print(match)
#         #if match:
#         a=match.span()[0]
#         b=match.span()[1]
#         #print(text_to_search[a:b])
#         #ppp.replace
#         ppp1=ppp1.replace(text_to_search[a:b],'''<span id="%s">%s</span>''' %(text_to_search[a:b],text_to_search[a:b]))

#     ref=ppp1.split('#')
#     ################################################################################################################
#     #print(ref)
#     #print(m)
#     text_to_search = table
#     #pattern=re.compile(r'Table\s{0,1}\d{1,2}:\s[a-zA-Z0-9ﬁ ]+')
#     pattern=re.compile(r'Table\s{0,1}\d{1,2}')
#     matches=pattern.finditer(text_to_search)
#     ppp1=text_to_search
#     for match in matches:
#         #print(match)
#         #if match:
#         a=match.span()[0]
#         b=match.span()[1]
#         print(text_to_search[a:b])
#         #ppp.replace
#         ppp1=ppp1.replace(text_to_search[a:b],'''<h3 id="%s">%s</h3>''' %(text_to_search[a:b],text_to_search[a:b]))

#     ppp1=ppp1.replace('!!','<br>')
#     table=ppp1.split('###')
    
#     #table=ppp1.replace('###','<br><br>')
#     #table=ppp1


#     context={
#         'parag':'''%s''' %(pppnew),
#         'ref':ref,
#         'table':table,
#     }
#     return render(request, 'profile/test.html', context)

# def network_affliation(request, user_url):

#     user_listing = get_object_or_404(Profile, user_url=user_url)

#     if request.method == 'POST':
#         user_email=request.user.email
#         avatarStyle = request.POST.get('avatarStyle')
#         topType = request.POST.get('topType')
#         accessoriesType = request.POST.get('accessoriesType')
#         hairColor = request.POST.get('hairColor')
#         hatColor = request.POST.get('hatColor')
#         facialHairType = request.POST.get('facialHairType')
#         facialHairColor = request.POST.get('facialHairColor')
#         clotheType = request.POST.get('clotheType')
#         clotheColor = request.POST.get('clotheColor')
#         graphicType = request.POST.get('graphicType')
#         eyeType = request.POST.get('eyeType')
#         eyebrowType = request.POST.get('eyebrowType')
#         mouthType = request.POST.get('mouthType')
#         skinColor = request.POST.get('skinColor')
#         Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

#         URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


#         return redirect('profile', URL)

    

#     csvpath='AA/static/scopus_match1.csv'
#     scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
#     # print(scopusmatch.columns)
#     # print(scopusmatch['scopus'].values)
#     userurllist=scopusmatch['user_url'].values
#     scopuslist=scopusmatch['scopus'].values
#     dictmatch=dict(zip(userurllist,scopuslist))
    
 
#     #trend
#     trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
#     cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
#     docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
#     citedata=cite.split('#')
#     docyear=docu.split('#')

#     #impact
#     trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
#     impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
#     docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
#     ifdata=impact.split('#')
#     docyear=docu.split('#')

#     #publisher
#     trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
#     publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
#     publisher=publisher.split('#') 


#     cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


#     conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

#     countorigin=[]
#     for i in range(len(cityinfo_qs)):
#         countorigin.append(int(cityinfo_qs[i].countn))


#     start = 5
#     end = 10
#     arr=countorigin
#     width = end - start
#     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]


#     for i in range(len(cityinfo_qs)):
#         cityinfo_qs[i].countn=res[i]

#     cityinfo_json = serialize("json", cityinfo_qs)
#     conninfo_json = serialize("json", conninfo_qs)

#     f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
#     tree1_json=f.read()

#     f.close()




#     #article
#     articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


#     profile1=[]
#     for i in range(len(articleinfo_qs)):
#         profile1.append(user_url) 
#     journal=list(articleinfo_qs.values_list('journal', flat=True))
#     year=list(articleinfo_qs.values_list('year', flat=True))
#     title=list(articleinfo_qs.values_list('title', flat=True))
#     titleurl=[slugify(x) for x in title]
#     author=list(articleinfo_qs.values_list('author', flat=True))
#     author=[", ".join(x.split('#')) for x in author]
#     cite=list(articleinfo_qs.values_list('cite', flat=True))
#     cite1=[]
#     for x in cite:
#         try:
#             cite1.append(int(x))
#         except:
#             cite1.append(0)


#     articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

#     # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)

#     articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=True)[:10]



#     context = {
#             'user_listing':user_listing,
            # 'citedata':citedata,
#             'docyear':docyear,
#             'ifdata':ifdata,
            # 'publisher':publisher,
#             'publish_datapath':'/static/profile/%s/publisher.csv' %(user_url),
#             'bubble_datapath':'/static/profile/%s/bubble.json' %(user_url),
#             'cloud_datapath':'/static/profile/%s/cloud.json' %(user_url),
#             'window_datapath':'/static/profile/%s/window.json' %(user_url),
#             'cityinfo_json':cityinfo_json,
#             'conninfo_json':conninfo_json,
#             'network_datapath':'/static/profile/%s/net.json' %(user_url),
#             'tree1_json':tree1_json,
#             'articlein':articlein,
#             'user_url':user_url,
#         }
    
#     return render(request, 'profile/network_affliation.html', context)

# def profile(request, user_url):

#     user_listing = get_object_or_404(Profile, user_url=user_url)

#     if request.method == 'POST':
#         user_email=request.user.email
#         avatarStyle = request.POST.get('avatarStyle')
#         topType = request.POST.get('topType')
#         accessoriesType = request.POST.get('accessoriesType')
#         hairColor = request.POST.get('hairColor')
#         hatColor = request.POST.get('hatColor')
#         facialHairType = request.POST.get('facialHairType')
#         facialHairColor = request.POST.get('facialHairColor')
#         clotheType = request.POST.get('clotheType')
#         clotheColor = request.POST.get('clotheColor')
#         graphicType = request.POST.get('graphicType')
#         eyeType = request.POST.get('eyeType')
#         eyebrowType = request.POST.get('eyebrowType')
#         mouthType = request.POST.get('mouthType')
#         skinColor = request.POST.get('skinColor')
#         Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

#         URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


#         return redirect('profile', URL)

    

#     csvpath='AA/static/scopus_match1.csv'
#     scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
#     # print(scopusmatch.columns)
#     # print(scopusmatch['scopus'].values)
#     userurllist=scopusmatch['user_url'].values
#     scopuslist=scopusmatch['scopus'].values
#     dictmatch=dict(zip(userurllist,scopuslist))
    
 
#     #trend
#     trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
#     cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
#     docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
#     citedata=cite.split('#')
#     docyear=docu.split('#')

#     #impact
#     trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
#     impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
#     docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
#     ifdata=impact.split('#')
#     docyear=docu.split('#')

#     #publisher
#     trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
#     publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
#     publisher=publisher.split('#') 


#     cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


#     conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

#     countorigin=[]
#     for i in range(len(cityinfo_qs)):
#         countorigin.append(int(cityinfo_qs[i].countn))


#     start = 5
#     end = 10
#     arr=countorigin
#     width = end - start
#     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]


#     for i in range(len(cityinfo_qs)):
#         cityinfo_qs[i].countn=res[i]

#     cityinfo_json = serialize("json", cityinfo_qs)
#     conninfo_json = serialize("json", conninfo_qs)

#     f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
#     tree1_json=f.read()

#     f.close()




#     #article
#     articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


#     profile1=[]
#     for i in range(len(articleinfo_qs)):
#         profile1.append(user_url) 
#     journal=list(articleinfo_qs.values_list('journal', flat=True))
#     year=list(articleinfo_qs.values_list('year', flat=True))
#     title=list(articleinfo_qs.values_list('title', flat=True))
#     titleurl=[slugify(x) for x in title]
#     author=list(articleinfo_qs.values_list('author', flat=True))
#     author=[", ".join(x.split('#')) for x in author]
#     cite=list(articleinfo_qs.values_list('cite', flat=True))
#     cite1=[]
#     for x in cite:
#         try:
#             cite1.append(int(x))
#         except:
#             cite1.append(0)


#     articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

#     # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)

#     articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=True)[:10]



#     context = {
#             'user_listing':user_listing,
            # 'citedata':citedata,
#             'docyear':docyear,
#             'ifdata':ifdata,
            # 'publisher':publisher,
#             'publish_datapath':'/static/profile/%s/publisher.csv' %(user_url),
#             'bubble_datapath':'/static/profile/%s/bubble.json' %(user_url),
#             'cloud_datapath':'/static/profile/%s/cloud.json' %(user_url),
#             'window_datapath':'/static/profile/%s/window.json' %(user_url),
#             'cityinfo_json':cityinfo_json,
#             'conninfo_json':conninfo_json,
#             'network_datapath':'/static/profile/%s/net.json' %(user_url),
#             'tree1_json':tree1_json,
#             'articlein':articlein,
#             'user_url':user_url,
#         }
    
#     return render(request, 'profile/profile_listing.html', context)



# def profile(request, user_url):

#     user_listing = get_object_or_404(Profile, user_url=user_url)

#     if request.method == 'POST':
#         user_email=request.user.email
#         avatarStyle = request.POST.get('avatarStyle')
#         topType = request.POST.get('topType')
#         accessoriesType = request.POST.get('accessoriesType')
#         hairColor = request.POST.get('hairColor')
#         hatColor = request.POST.get('hatColor')
#         facialHairType = request.POST.get('facialHairType')
#         facialHairColor = request.POST.get('facialHairColor')
#         clotheType = request.POST.get('clotheType')
#         clotheColor = request.POST.get('clotheColor')
#         graphicType = request.POST.get('graphicType')
#         eyeType = request.POST.get('eyeType')
#         eyebrowType = request.POST.get('eyebrowType')
#         mouthType = request.POST.get('mouthType')
#         skinColor = request.POST.get('skinColor')
#         Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

#         URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


#         return redirect('profile', URL)

    

#     csvpath='AA/static/scopus_match1.csv'
#     scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
#     # print(scopusmatch.columns)
#     # print(scopusmatch['scopus'].values)
#     userurllist=scopusmatch['user_url'].values
#     scopuslist=scopusmatch['scopus'].values
#     dictmatch=dict(zip(userurllist,scopuslist))
    
 
#     #trend
#     trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
#     cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
#     docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
#     citedata=cite.split('#')
#     docyear=docu.split('#')

#     #impact
#     trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
#     impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
#     docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
#     ifdata=impact.split('#')
#     docyear=docu.split('#')

#     #publisher
#     trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
#     publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
#     publisher=publisher.split('#') 


#     cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


#     conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

#     countorigin=[]
#     for i in range(len(cityinfo_qs)):
#         countorigin.append(int(cityinfo_qs[i].countn))


#     start = 5
#     end = 10
#     arr=countorigin
#     width = end - start
#     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]


#     for i in range(len(cityinfo_qs)):
#         cityinfo_qs[i].countn=res[i]

#     cityinfo_json = serialize("json", cityinfo_qs)
#     conninfo_json = serialize("json", conninfo_qs)

#     f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
#     tree1_json=f.read()

#     f.close()




#     #article
#     articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


#     profile1=[]
#     for i in range(len(articleinfo_qs)):
#         profile1.append(user_url) 
#     journal=list(articleinfo_qs.values_list('journal', flat=True))
#     year=list(articleinfo_qs.values_list('year', flat=True))
#     title=list(articleinfo_qs.values_list('title', flat=True))
#     titleurl=[slugify(x) for x in title]
#     #author=list(articleinfo_qs.values_list('author', flat=True))
#     author=list(articleinfo_qs.values_list('authorabbr', flat=True))
#     #for x in author:
#     #    print(len(x.split('#')))
#     #    print(x)
#     author=;"， ".join(x.split('#')) for x in author]
#     #print(author)
#     cite=list(articleinfo_qs.values_list('cite', flat=True))
#     cite1=[]
#     for x in cite:
#         try:
#             cite1.append(int(x))
#         except:
#             cite1.append(0)


#     articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

#     # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)
#     print(len(profile1))

#     articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=True)[:10]
    


#     context = {
#             'user_listing':user_listing,
            # 'citedata':citedata,
#             'docyear':docyear,
#             'ifdata':ifdata,
            # 'publisher':publisher,
#             'publish_datapath':'/static/profile/%s/publisher.csv' %(user_url),
#             'bubble_datapath':'/static/profile/%s/bubble.json' %(user_url),
#             'cloud_datapath':'/static/profile/%s/cloud.json' %(user_url),
#             'window_datapath':'/static/profile/%s/window.json' %(user_url),
#             'cityinfo_json':cityinfo_json,
#             'conninfo_json':conninfo_json,
#             'network_datapath':'/static/profile/%s/net.json' %(user_url),
#             'tree1_json':tree1_json,
#             'articlein':articlein,
#             'user_url':user_url,
#         }
    
#     return render(request, 'profile/profile_listing.html', context)

# def profile(request, user_url):

#     user_listing = get_object_or_404(Profile, user_url=user_url)

#     if request.method == 'POST':
#         user_email=request.user.email
#         avatarStyle = request.POST.get('avatarStyle')
#         topType = request.POST.get('topType')
#         accessoriesType = request.POST.get('accessoriesType')
#         hairColor = request.POST.get('hairColor')
#         hatColor = request.POST.get('hatColor')
#         facialHairType = request.POST.get('facialHairType')
#         facialHairColor = request.POST.get('facialHairColor')
#         clotheType = request.POST.get('clotheType')
#         clotheColor = request.POST.get('clotheColor')
#         graphicType = request.POST.get('graphicType')
#         eyeType = request.POST.get('eyeType')
#         eyebrowType = request.POST.get('eyebrowType')
#         mouthType = request.POST.get('mouthType')
#         skinColor = request.POST.get('skinColor')
#         Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

#         URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


#         return redirect('profile', URL)

    

#     csvpath='AA/static/scopus_match1.csv'
#     scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
#     # print(scopusmatch.columns)
#     # print(scopusmatch['scopus'].values)
#     userurllist=scopusmatch['user_url'].values
#     scopuslist=scopusmatch['scopus'].values
#     dictmatch=dict(zip(userurllist,scopuslist))
    
 
#     #trend
#     trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
#     cite=list(trendcitadocu_qs.values_list('cite', flat=True))
#     docu=list(trendcitadocu_qs.values_list('docu', flat=True))
#     citedata=cite.split('#')
#     docyear=docu.split('#')

#     #impact
#     trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
#     impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
#     docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
#     ifdata=impact.split('#')
#     docyear=docu.split('#')

#     #publisher
#     # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
#     # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
#     # publisher=publisher.split('#') 


#     cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


#     conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

#     countorigin=[]
#     for i in range(len(cityinfo_qs)):
#         countorigin.append(int(cityinfo_qs[i].countn))


#     start = 5
#     end = 10
#     arr=countorigin
#     if len(arr)>1:
#         print(arr)
#         print(len(arr))
#         width = end - start
#         res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
#     else:
#         res=[arr for x in arr][0]


#     for i in range(len(cityinfo_qs)):
#         cityinfo_qs[i].countn=res[i]

#     cityinfo_json = serialize("json", cityinfo_qs)
#     conninfo_json = serialize("json", conninfo_qs)

#     f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
#     tree1_json=f.read()

#     f.close()




#     #article
#     articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


#     profile1=[]
#     for i in range(len(articleinfo_qs)):
#         profile1.append(user_url) 
#     journal=list(articleinfo_qs.values_list('journal', flat=True))
#     year=list(articleinfo_qs.values_list('year', flat=True))
#     title=list(articleinfo_qs.values_list('title', flat=True))
#     titleurl=[slugify(x) for x in title]
#     #author=list(articleinfo_qs.values_list('author', flat=True))
#     author=list(articleinfo_qs.values_list('authorabbr', flat=True))
#     #for x in author:
#     #    print(len(x.split('#')))
#     #    print(x)
#     author=;"， ".join(x.split('#')) for x in author]
#     #print(author)
#     cite=list(articleinfo_qs.values_list('cite', flat=True))
#     cite1=[]
#     for x in cite:
#         try:
#             cite1.append(int(x))
#         except:
#             cite1.append(0)


#     articlein=zip(profile1,journal,year,title,author,cite1,titleurl)

#     # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)
#     print(len(profile1))

#     articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=True)[:10]
    
#     connauthorinfo_qs=MapCoauthorinfo.objects.filter(profile=dictmatch[user_url])
#     print("幹幹幹!")
#     coauthorstr=list(connauthorinfo_qs.values_list('coauthor', flat=True))[0]
#     #print(coauthorstr.split('$')[0])
    
#     coauthorname=[]
#     coauthoraffi=[]
#     coauthoritem=[]
#     coauthorahref=[]
#     #   var tmp=NewArray[i].split("#")[0].split('&')[0];
#     #                     var tmp2=NewArray[i].split("#")[0].split('&')[1];
#     #                     var tmp1=tmp.split(" ").join("7").replace('.','_').replace(',','8');
#     #                     //var tmp1="test";
#     #                     var userurl='{{user_url}}';
#     #                     //console.log(userurl);
#     #                     var ttt='<a href= "http://127.0.0.1:8000/profile/'+userurl+'/network-affliation/'+tmp1+'">';
#     for k in range(len(coauthorstr.split('$'))):
#         coauthorname.append(coauthorstr.split('$')[k].split('#')[0].split('&')[0])
#         coauthoraffi.append(coauthorstr.split('$')[k].split('#')[0].split('&')[1])
#         coauthoritem.append(int(coauthorstr.split('$')[k].split('#')[-1]))
#         tmpname=coauthorstr.split('$')[k].split('#')[0].split('&')[0]
#         # print(tmpname.split(" "))
#         # ['Liao,', 'Y.-M']
#         # Liao87Y_-M
#         tmp1="7".join(tmpname.split(" ")).replace('.','_').replace(',','8')
        
#         coauthorahref.append("http://127.0.0.1:8000/profile/%s/network-coauthor/%s" %(user_url,tmp1))
    
#     coauthorzip=sorted(zip(coauthorname,coauthoraffi,coauthoritem,coauthorahref),key=lambda x: -x[2])[:10]

#     context = {
#             'user_listing':user_listing,
            # 'citedata':citedata,
#             'docyear':docyear,
#             'ifdata':ifdata,
            # 'publisher':publisher,
#             'publish_datapath':'/static/profile/%s/publisher.csv' %(user_url),
#             'bubble_datapath':'/static/profile/%s/bubble.json' %(user_url),
#             'cloud_datapath':'/static/profile/%s/cloud.json' %(user_url),
#             'window_datapath':'/static/profile/%s/window.json' %(user_url),
#             'cityinfo_json':cityinfo_json,
#             'conninfo_json':conninfo_json,
#             'network_datapath':'/static/profile/%s/net.json' %(user_url),
#             'tree1_json':tree1_json,
#             'articlein':articlein,
#             'user_url':user_url,
#             'coauthorzip':coauthorzip,
#         }
    
#     return render(request, 'profile/profile_listing.html', context)


# def profile(request, user_url):

#     user_listing = get_object_or_404(Profile, user_url=user_url)
#     print(user_url)
#     print(user_listing)

#     if request.method == 'POST':
#         user_email=request.user.email
#         avatarStyle = request.POST.get('avatarStyle')
#         topType = request.POST.get('topType')
#         accessoriesType = request.POST.get('accessoriesType')
#         hairColor = request.POST.get('hairColor')
#         hatColor = request.POST.get('hatColor')
#         facialHairType = request.POST.get('facialHairType')
#         facialHairColor = request.POST.get('facialHairColor')
#         clotheType = request.POST.get('clotheType')
#         clotheColor = request.POST.get('clotheColor')
#         graphicType = request.POST.get('graphicType')
#         eyeType = request.POST.get('eyeType')
#         eyebrowType = request.POST.get('eyebrowType')
#         mouthType = request.POST.get('mouthType')
#         skinColor = request.POST.get('skinColor')
#         Profile.objects.filter(user_email=user_email).update(avatarStyle=avatarStyle, topType=topType, accessoriesType=accessoriesType, hairColor=hairColor, hatColor=hatColor, facialHairType=facialHairType, facialHairColor=facialHairColor, clotheType=clotheType, clotheColor=clotheColor, graphicType=graphicType, eyeType=eyeType, eyebrowType=eyebrowType, mouthType=mouthType, skinColor=skinColor)

#         URL=Profile.objects.filter(user_email=request.user.email).values_list('user_url', flat=True)[0]


#         return redirect('profile', URL)

    

#     csvpath='AA/static/scopus_match1.csv'
#     scopusmatch=pd.read_csv(csvpath,sep='\t',encoding='utf-8')
#     # print(scopusmatch.columns)
#     # print(scopusmatch['scopus'].values)
#     userurllist=scopusmatch['user_url'].values
#     scopuslist=scopusmatch['scopus'].values
#     dictmatch=dict(zip(userurllist,scopuslist))
    
 
#     #trend
#     trendcitadocu_qs=TrendCitaDocu.objects.filter(profile=dictmatch[user_url])
#     cite=list(trendcitadocu_qs.values_list('cite', flat=True))[0]
#     docu=list(trendcitadocu_qs.values_list('docu', flat=True))[0]
#     citedata=cite.split('#')
#     docyear=docu.split('#')

#     #impact
#     trendcitaimpact_qs=TrendCitaImpact.objects.filter(profile=dictmatch[user_url])
#     impact=list(trendcitaimpact_qs.values_list('impact', flat=True))[0]
#     docu=list(trendcitaimpact_qs.values_list('docu', flat=True))[0]
    
#     ifdata=impact.split('#')
#     docyear=docu.split('#')

#     #publisher
#     # trendpublisher_qs=TrendPublisher.objects.filter(profile=dictmatch[user_url])
#     # publisher=list(trendpublisher_qs.values_list('publisher', flat=True))[0]
#     # publisher=publisher.split('#') 


#     # cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])


#     # conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

#     # countorigin=[]
#     # for i in range(len(cityinfo_qs)):
#     #     countorigin.append(int(cityinfo_qs[i].countn))

# ######################20210103###################
#     cityinfo_qs=MapCityinfo.objects.filter(profile=dictmatch[user_url])
#     #print("幹")
#     #print(cityinfo_qs)
#     #print(len(cityinfo_qs))

#     conninfo_qs=MapConninfo.objects.filter(profile=dictmatch[user_url])

#     countorigin=[]
#     for i in range(len(cityinfo_qs)):
#         tmpcityinfo=cityinfo_qs[i].asso
#         #print(tmpcityinfo)
#         cityinfo_qs[i].asso=tmpcityinfo.replace('\'','')
#         countorigin.append(int(cityinfo_qs[i].countn))



#     # start = 5
#     # end = 10
#     # arr=countorigin
#     # if len(arr)>1:
#     #     print(arr)
#     #     print(len(arr))
#     #     width = end - start
#     #     res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
#     # else:
#     #     res=[arr for x in arr][0]

#     start = 5
#     end = 10
#     arr=countorigin
#     if len(arr)>1:
#         #print(arr)
#         #print(len(arr))
#         width = end - start
#         if int(max(arr)-min(arr))!=0:
#             res=[(x-min(arr))/(max(arr)-min(arr))*end+start for x in arr]
#         else:
#             res=[x for x in arr]
#     else:
#         res=arr

#     for i in range(len(cityinfo_qs)):
#         cityinfo_qs[i].countn=res[i]

#     cityinfo_json = serialize("json", cityinfo_qs)
#     conninfo_json = serialize("json", conninfo_qs)

#     f=staticfiles_storage.open('profile/%s/tree.json' %(user_url),'r')
#     tree1_json=f.read()

#     f.close()




#     #article
#     articleinfo_qs=articleinfo.objects.filter(profile=dictmatch[user_url])
 

    


#     profile1=[]
#     for i in range(len(articleinfo_qs)):
#         profile1.append(user_url) 
#     journal=list(articleinfo_qs.values_list('journal', flat=True))
#     year=list(articleinfo_qs.values_list('year', flat=True))
#     title=list(articleinfo_qs.values_list('title', flat=True))
#     titleurl=[slugify(x) for x in title]
#     #author=list(articleinfo_qs.values_list('author', flat=True))
#     author=list(articleinfo_qs.values_list('authorabbr', flat=True))

#     author=["; ".join(x.split('#')) for x in author]
#     #print(author)
#     cite=list(articleinfo_qs.values_list('cite', flat=True))
#     print("cite",cite)
#     cite1=[]
#     for x in cite:
#         try:
#             cite1.append(int(x))
#         except:
#             cite1.append(0)
#     abstract=list(articleinfo_qs.values_list('abstract', flat=True))


#     articlein=zip(profile1,journal,year,title,author,cite1,titleurl,abstract)

#     # articlein=sorted(articlein,  key=operator.itemgetter(2, 5), reverse=True)
#     print(len(profile1))

#     articlein=sorted(articlein,  key=operator.itemgetter(5), reverse=True)[:10]
    
#     connauthorinfo_qs=MapCoauthorinfo.objects.filter(profile=dictmatch[user_url])
#     print("幹幹幹!")
#     coauthorstr=list(connauthorinfo_qs.values_list('coauthor', flat=True))[0]
#     #print(coauthorstr.split('$')[0])
    
#     coauthorname=[]
#     coauthoraffi=[]
#     coauthoritem=[]
#     coauthorahref=[]
#     #   var tmp=NewArray[i].split("#")[0].split('&')[0];
#     #                     var tmp2=NewArray[i].split("#")[0].split('&')[1];
#     #                     var tmp1=tmp.split(" ").join("7").replace('.','_').replace(',','8');
#     #                     //var tmp1="test";
#     #                     var userurl='{{user_url}}';
#     #                     //console.log(userurl);
#     #                     var ttt='<a href= "http://127.0.0.1:8000/profile/'+userurl+'/network-affliation/'+tmp1+'">';
#     for k in range(len(coauthorstr.split('$'))):
#         coauthorname.append(coauthorstr.split('$')[k].split('#')[0].split('&')[0])
#         coauthoraffi.append(coauthorstr.split('$')[k].split('#')[0].split('&')[1])
#         coauthoritem.append(int(coauthorstr.split('$')[k].split('#')[-1]))
#         tmpname=coauthorstr.split('$')[k].split('#')[0].split('&')[0]
#         # print(tmpname.split(" "))
#         # ['Liao,', 'Y.-M']
#         # Liao87Y_-M
#         tmp1="7".join(tmpname.split(" ")).replace('.','_').replace(',','8')
        
#         coauthorahref.append("https://researchain.net/profile/%s/network-coauthor/%s" %(user_url,tmp1))
    
#     coauthorzip=sorted(zip(coauthorname,coauthoraffi,coauthoritem,coauthorahref),key=lambda x: -x[2])[:10]

#     context = {
#             'user_listing':user_listing,
#             'citedata':citedata,
#             'docyear':docyear,
#             'ifdata':ifdata,
#             #'publisher':publisher,
#             'publish_datapath':'/static/profile/%s/publisher.csv' %(user_url),
#             'bubble_datapath':'/static/profile/%s/bubble.json' %(user_url),
#             'cloud_datapath':'/static/profile/%s/cloud.json' %(user_url),
#             'window_datapath':'/static/profile/%s/window.json' %(user_url),
#             'cityinfo_json':cityinfo_json,
#             'conninfo_json':conninfo_json,
#             'network_datapath':'/static/profile/%s/net.json' %(user_url),
#             'tree1_json':tree1_json,
#             'articlein':articlein,
#             'user_url':user_url,
#             'coauthorzip':coauthorzip,
#         }
    
#     return render(request, 'profile/profile_listing.html', context)
