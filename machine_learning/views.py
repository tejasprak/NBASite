# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from os import listdir

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from machine_learning.forms import tform
from machine_learning.forms import pform
from django.views.decorators.csrf import csrf_exempt


import scipy, numpy
#from sklearn import neighbors, datasets
from sklearn.svm import LinearSVC
import pickle
import csv
import warnings
import pandas
import urllib2
from bs4 import BeautifulSoup as bs
import requests
from urllib2 import urlopen

def get_games_for_name(name):
    with open('adv_stats.csv') as csvfile:
            nbalist = csv.reader(csvfile)
            data = []
            target = []
            i = 0
            for row in nbalist:
                #print row
                if i == 0:
                    i = i + 1
                    continue
                namee =  row[1]
                namee = namee.split("""\\""")[0]
                #print name

                #if len(name.split()) == 2:
                #    fr, lr = name.split(" ")
                #elif len(name.split()) == 3:
                #    fr, lr, tr = name.split(" ")
                #else:
                #    fr, lr, tr, br = name.split(" ")
                #print fr, lr
                #print f,
                #if fr == f:
                #    if lr == l:
                if namee == name:
                    return row[5]
def get_player_stats(name):
    thename = name
    print name
    #f, l = name.split(" ")
    #pid = player.get_player(first_name=f,last_name=l)
    #ts = player.PlayerGeneralSplits(player_id=pid,season='2016-17').json
    #print ts['resultSets'][1]['headers']
    #ts = ts['resultSets'][0]['rowSet'][0]
    #return ts
    with open('adv_stats.csv') as csvfile:
            nbalist = csv.reader(csvfile)
            data = []
            target = []
            i = 0
            for row in nbalist:
                #print row
                if i == 0:
                    i = i + 1
                    continue
                namee =  row[1]
                namee = namee.split("""\\""")[0]
                #print name

                #if len(name.split()) == 2:
                #    fr, lr = name.split(" ")
                #elif len(name.split()) == 3:
                #    fr, lr, tr = name.split(" ")
                #else:
                #    fr, lr, tr, br = name.split(" ")
                #print fr, lr
                #print f,
                #if fr == f:
                #    if lr == l:
                if namee == name:
                    per =  row[7]
                    #print per
                    ws48 = row[23]
                    bpm = row[27]
                    return [per,ws48,bpm]
            return [0,0,0]

def get_salary_for_name(name):
    df2 = pandas.DataFrame.from_csv('salary.csv')
    f = 0
    for row in df2.iterrows():
        if f==0:
            f = f + 1
            continue
        #salaries[d[1]['Unnamed: 1']] = d[1]['Salary']
        name2  = row[1]['Unnamed: 1']
        name2 = name2.split("""\\""")[0]
        #print name
        #print name2
        if name2 == name:
            salary = row[1]['Salary']
            salary = salary.replace("$", "")
            salary = int(salary)
            return salary
    return "None"
def scrape_for_url2(url):
    soup = bs(urlopen(url),"html.parser")
    height = soup.find("span",attrs={"itemprop":"height"})
    height = str(height)
    height = height.replace('''<span itemprop="height">''', "")
    height = height.replace('</span>',"")
    height = height.replace('-'," ")
    ft, inc = height.split(" ")
    ft = int(ft)
    inc = int(inc)
    cm = (ft * 12) * 2.54
    cm = cm + (inc * 2.54)
    cm =  int(round(cm))
    print cm
    players = soup.find("tfoot")
    pdata = {}
    for row in players.find_all("td"):
        row = str(row)
        row2 = row.replace('td', "")
        row2 = row2.replace('<', "")
        row2 = row2.replace('class=', "")
        row2 = row2.replace('data-stat=', "")
        row2 = row2.replace(""" "left " """, "")
        row2 = row2.replace(""" "right " """, "")
        row2 = row2.replace("/>", "")
        row2 = row2.replace(">", ":")
        row2 = row2.replace('"', "")
        d1, d2 = row2.split(':')
        #print d1
        #print d2
        #print row2
        pdata[d1] = d2
    #print pdata
    if pdata['fg3_pct'] == '':
        array = [float(pdata['pts_per_g']),float(pdata['trb_per_g']),float(pdata['ast_per_g']),float(pdata['stl_per_g']),float(pdata['blk_per_g']),float(pdata['tov_per_g']),float(pdata['pf_per_g']), float(pdata['ft_pct']),0,float(pdata['fg2_pct']),cm]
    else:
        array = [float(pdata['pts_per_g']),float(pdata['trb_per_g']),float(pdata['ast_per_g']),float(pdata['stl_per_g']),float(pdata['blk_per_g']),float(pdata['tov_per_g']),float(pdata['pf_per_g']), float(pdata['ft_pct']),float(pdata['fg3_pct']),float(pdata['fg2_pct']),cm]


    return array
    #   print players
    #   print players

def scrape_for_url(url):
    soup = bs(urlopen(url),"html.parser")
    height = soup.find("span",attrs={"itemprop":"height"})
    height = str(height)
    height = height.replace('''<span itemprop="height">''', "")
    height = height.replace('</span>',"")
    height = height.replace('-'," ")
    ft, inc = height.split(" ")
    ft = int(ft)
    inc = int(inc)
    cm = (ft * 12) * 2.54
    cm = cm + (inc * 2.54)
    cm =  int(round(cm))
    print cm
    players = soup.find("tfoot")
    pdata = {}
    for row in players.find_all("td"):
        row = str(row)
        row2 = row.replace('td', "")
        row2 = row2.replace('<', "")
        row2 = row2.replace('class=', "")
        row2 = row2.replace('data-stat=', "")
        row2 = row2.replace(""" "left " """, "")
        row2 = row2.replace(""" "right " """, "")
        row2 = row2.replace("/>", "")
        row2 = row2.replace(">", ":")
        row2 = row2.replace('"', "")
        row2 = row2.replace("incomplete", "")
        row2 = row2.replace(''' right ''', "")
        row2 = row2.replace(" ", "")
        d1, d2 = row2.split(':')
        #print d1
        #print d2
        #print row2
        pdata[d1] = d2
    pdata_fixed = {}
    for value in pdata.values():
        if value == "":
            for key, val2 in pdata.iteritems():
                if val2 == value:
                    pdata_fixed[key] = 0
        else:
            for key, val2 in pdata.iteritems():
                if val2 == value:
                    pdata_fixed[key] = value
    #print pdata_fixed
    pdata = pdata_fixed
    array = [float(pdata['pts_per_g']),float(pdata['trb_per_g']),float(pdata['ast_per_g']),float(pdata['stl_per_g']),float(pdata['blk_per_g']),float(pdata['tov_per_g']),float(pdata['pf_per_g']), float(pdata['ft_pct']),float(pdata['fg3_pct']),float(pdata['fg_pct']),cm]


    return array
# Create your views here.
@csrf_exempt
def index(request):
    #print listdir('.')
    firstName = ''
    lastName = ''
    context = RequestContext(request)
    context_dict = {}
    context_dict['LUL'] = "DRAFT"
    cd = {}
    isyes = 0
    if request.method == "POST":
        f = tform(request.POST)
        if f.is_valid():
            cd = f.cleaned_data
            print cd
            firstName = cd['firstName']
            firstName = firstName.lower()
            lastName = cd['lastName']
            lastName = lastName.lower()
    else:
        isyes = 1
        f = tform()
        args = {}

        args['form'] = f
    context_dict['form'] = f

    if isyes == 0:
        bball = {}

        x  = ['superstar','star','starter','role_player','bust']
        x = numpy.array(x)
        bball['target_names'] = x


        with open('college-nba-players-stats.csv') as csvfile:
            nbalist = csv.reader(csvfile)
            data = []
            target = []
            for row in nbalist:
                z = []
                for y in range(1,13):
                    if y != 11:
                        z.append(float(row[y]))

                    #print z
                data.append(z)

                target.append(float(row[13]))

        data = numpy.array(data)
        #print data[0]
        bball['data'] = data
        target = numpy.array(target)
        bball['target'] = target
        bball['DESCR'] = 'blah'

        feature_names = ['points', 'rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'personal fouls', 'FT%', '3P%', 'FG%','height(cm)']
        feature_names = numpy.array(feature_names)
        bball['feature_names'] = feature_names
        x,y = bball['data'], bball['target']

        url2 = 'https://www.sports-reference.com/cbb/players/' + firstName + '-' + lastName + '-1.html'
        print url2
        willie = scrape_for_url(url2)


        with warnings.catch_warnings():
            warnings.filterwarnings("ignore",category=DeprecationWarning)

            #result = linSVC._predict_proba_lr([13.8,5.4,0.8,0.9,1.6,2.0,4.1,.685,.350,.530,206])
            #print "Marquese Chriss - ", result
            #result = linSVC._predict_proba_lr([17.3,3.0,7.0,1.5,0.1,2.0,1.8,.856,.344,.434,175])
            #print "Tyler Ulis - ", result
            #result = linSVC._predict_proba_lr([14.6,5.4,2.0,0.8,0.6,3.1,3.2,.654,.294,.431,201])
            #print "Jaylen Brown - ", result
            def get_prediction(array):
                lonzo_list = []
                for i in range(501):
                    linSVC = LinearSVC()
                    linSVC.fit(x,y)
                    result = linSVC._predict_proba_lr(array)
                    lonzo_list.append(list(result[0]))
                    #print i
                    #print lonzo_list
                avg = [float(sum(col))/len(col) for col in zip(*lonzo_list)]
                return avg
            pred = get_prediction(willie)
            i = 0
            highest_value = 0
            role = 0
            for value in pred:
                if value > highest_value:
                    highest_value = value
                    role = i
                i = i + 1
            #print highest_value
            ##print role
            if role == 0:
                context_dict['PRINT'] = firstName + " "  + lastName + " is a superstar"
            elif role == 1:
                context_dict['PRINT'] = firstName + " "  + lastName + " is a star"
            elif role == 2:
                context_dict['PRINT'] = firstName + " "  + lastName + " is a starter"
            elif role == 3:
                context_dict['PRINT'] = firstName + " "  + lastName + " is a role player"
            elif role == 4:
                context_dict['PRINT'] = firstName + " "  + lastName + " is a bust"
            result = [list(get_prediction(willie))]
            print result
            context_dict['PR']  = result[0][0], "chance of being a superstar,", result[0][1], "chance of being a star,", result[0][2], "chance of being a starter,", result[0][3], "chance of being a role player,", result[0][4], "chance of being a bust"
    #print get_prediction(jkidd)
    #print result[0][0], "chance of being a superstar,", result[0][1], "chance of being a star,", result[0][2], "chance of being a starter,", result[0][3], "chance of being a role player,", result[0][4], "chance of being a bust"
    #result = linSVC._predict_proba_lr(jkidd)
    #sprint result[0][0], "chance of being a superstar,", result[0][1], "chance of being a star,", result[0][2], "chance of being a starter,", result[0][3], "chance of being a role player,", result[0][4], "chance of being a bust"

    #print "jkidd", result



    #array =  get_player_stats("Chris Paul")
    #Print array

    return render_to_response('machine_learning/index.html', context_dict, context)
@csrf_exempt
def value(request):
    daa = []
    context = RequestContext(request)
    context_dict = {}
    isyes = 0
    if request.method == "POST":
        f = pform(request.POST)
        if f.is_valid():
            cd = f.cleaned_data
            print cd
            value = cd['asd']
    else:
        isyes = 1
        f = pform()
        args = {}

        args['form'] = f
    context_dict['form'] = f

    if isyes == 0:
        bball = {}

        x = ['max','high','medium','lowish','low']
        x = numpy.array(x)
        bball['target_names'] = x

        df = pandas.DataFrame.from_csv('salary.csv')
        salaries = {}
        target = []
        data = []
        i = 0
        for d in df.iterrows():
            if i==0:
                i = i + 1
                continue
            #salaries[d[1]['Unnamed: 1']] = d[1]['Salary']
            name  = d[1]['Unnamed: 1']
            name = name.split("""\\""")[0]

            salary = d[1]['Salary']
            salary = salary.replace("$", "")
            salary = int(salary)
            #print name
            if salary < 4000000:
                #print name
                target.append(4)
                data.append(get_player_stats(name))
            elif salary < 12000000:
                #print name
                target.append(3)
                data.append(get_player_stats(name))
            elif salary < 20000000:
                #print name
                target.append(2)
                data.append(get_player_stats(name))
            elif salary < 28000000:
                #print name
                target.append(1)
                data.append(get_player_stats(name))
            else:
                #print name
                target.append(0)
                data.append(get_player_stats(name))


        data = numpy.array(data)
        bball['data'] = data
        #print data
        target = numpy.array(target)
        bball['target'] = target
        #print target
        bball['DESCR'] = 'blah'
        feature_names = ['PER','WS/48','BPM']
        feature_names = numpy.array(feature_names)
        bball['feature_names'] = feature_names
        x,y = bball['data'], bball['target']

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore",category=DeprecationWarning)
            def get_prediction(array):
                lonzo_list = []
                for i in range(25):
                    linSVC = LinearSVC()
                    linSVC.fit(x,y)

                    result = linSVC._predict_proba_lr(array)
                    lonzo_list.append(list(result[0]))
                    #print i
                #print lonzo_list
                avg = [float(sum(col))/len(col) for col in zip(*lonzo_list)]
                return avg

            with open('adv_stats.csv') as csvfile:
                    nbalist = csv.reader(csvfile)
                    i = 0
                    for row in nbalist:
                        if i == 0:
                            i = i + 1
                            continue
                        namee =  row[1]
                        #print row[1]
                        namee = namee.split("""\\""")[0]

                        per =  float(row[7])
                        #print per
                        ws48 = float(row[23])
                        bpm = float(row[27])
                        #print namee
                        pred = get_prediction([per,ws48,bpm])
                        relpred = max(pred)
                        max_index = pred.index(relpred)
                        if max_index == 0:
                            #print namee
                            sal = get_salary_for_name(namee)
                            #print "passed 1"
                            if sal > 10000000:
                                #print "passed 2"
                                if get_games_for_name(namee) > 45:
                                    #print "3"
                                    print namee
                                    daa.append("At only " + str(sal) + " dollars, " + namee + " is getting criminally underpaid!" + str(pred))
    context_dict['daa'] = daa
    return render_to_response('machine_learning/value.html', context_dict, context)
