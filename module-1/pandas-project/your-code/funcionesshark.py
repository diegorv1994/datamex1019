# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:33:37 2019

@author: diego
"""
t=["6' to 8' shark",'"a large shark"','"a little shark"',
   '"a pack of 6 sharks"','"a pack of sharks"','"a very large shark"',
   '"shark had a very large girth"',"+3' shark",".5 m shark",
   "0.7 m [2.5'] shark","0.9 m  [3'] shark",
   "0.9 m  to 1.2 m [3' to 4'] shark","0.9 m [3']  shark",
   "0.9 m [3'] shark","0.9 m to 1.2 m [3' to 4'] shark",
   "0.9 m to 1.2 m [3' to 4'] shark; tooth fragment recovered from hand",
   "0.9 m to 1.5 m [3' to 5'] shark","1 m  shark","1 m shark",
   "1' to 2' shark","1' to 4' shark","1,100-lb shark","1.2 m  [4'] shark",
   "1.2 m [4'], possibly  larger shark","remains recovered 5 days later",
   "remains recovered from 3 sharks",
   "remains recovered from shark caught days later",
   "reported as a shark attack, the story was a hoax ","1.5 m [5'] shark",
   "1.2 m to 1.5 m [4' to 5'] shark","1.5 m shark",
   "tooth fragments recovered from hull","two 1.2 m to 1.5 m [4' to 5'] sharks",
   "two 2.1 m [7'] sharks""two shark's teeth recovered from canoe",
   "two sharks seen in vicinity: 2.4 m & 4.25 m  [8' & 14'] tl",
   '"a school of sharks"',"1.5 m to 1.8 m [5' to 6'] shark",
   "1.8 m [6'] shark","1.5 m to 1.8m [5' to 6'] shark",
   "1.5 m to 2 m [5' to 6.75'] shark","1.5 m to 2 m shark",
   "1.5 m to 2.1 m  [5' to 7'] shark","1.5 m, 45-kg shark",
   "1.5 to 1.8 m [5' to 6'] shark","1.5 to 2 m [5' to 6.75'] shark",
   "1.5 to 2 m shark","1.5' to 2' shark","1.6 m shark","1.7 m [5.5'] shark",
   "1.7 m shark","1.8 m [6']  shark","10' shark","1.8 m shark",
   "10' to 12' shark","1.8 m to 2.4 m [6' to 8'] shark",
   "12' shark","12' to 14' shark"]

def clean_species(s):
    if "unknown" in s.lower():
        s="unknown"
    elif "probable" in s.lower():
        s="unknown"
    elif "possibly" in s.lower():
        s="unknown"
    elif "no" in s.lower():
        s="unknown"
    elif s in t:
        s="unknown"
    elif "1.2 m [4'] shark" in s.lower():
        s="unknown"
    elif "small shark" in s.lower():
        s="unknown"
    elif "said" in s.lower():
        s="unknown"
    elif "a small shark" in s.lower():
        s="unknown"
    elif "believe" in s.lower():
        s="unknown"
    elif "invalid" in s.lower():
        s="unknown"
    elif "questionable" in s.lower():
        s="unknown"
    elif "not" in s.lower():
        s="not"
    elif "unidentified" in s.lower():
        s="unknown"
    elif "unconfirmed" in s.lower():
        s="unknown"
    elif "doubtful" in s.lower():
        s="unknown"
    elif "?" in s.lower():
        s="unknown"
    elif "still" in s.lower():
        s="unknown"
    elif "white" in s.lower():
        s="white"
    elif "wobbegong" in s.lower():
        s="wobbegog"
    elif "zambesi" in s.lower():
        s="zambesi"
    elif "zambesi" in s.lower():
        s="zambesi"
    elif "tiger" in s.lower():
        s="tiger"
    elif "bull" in s.lower():
        s="bull"
    elif "lemon" in s.lower():
        s="lemon"
    elif "blue" in s.lower():
        s="blue"
    elif "grey" in s.lower():
        s="grey"
    elif "whaler" in s.lower():
        s="whaler"
    elif "thought" in s.lower():
        s="unknown"
    elif "nurse" in s.lower():
        s="nurse"
    elif "spinner" in s.lower():
        s="spinner"
    elif "thresher" in s.lower():
        s="thresher"
    elif "gray" in s.lower():
        s="gray"
    elif "black" in s.lower():
        s="black tipped"
    elif "cat" in s.lower():
        s="cat"
    elif "sand" in s.lower():
        s="sandbar"
    elif "hammerhead" in s.lower():
        s="hammerhead"
    elif "brown" in s.lower():
        s="brown"
    elif "galapagos" in s.lower():
        s="galapagos"
    elif "silky" in s.lower():
        s="silky"
    elif "silver" in s.lower():
        s="silky"
    elif "shovel" in s.lower():
        s="shovel"
    elif "gummy" in s.lower():
        s="gummy"
    elif "shortfin" in s.lower():
        s="shortfin"
    elif "carpet" in s.lower():
        s="carpet"
    elif "dog" in s.lower():
        s="dog"
    elif "dusky" in s.lower():
        s="dusky"
    elif "ragged" in s.lower():
        s="ragged"
    elif "salmon" in s.lower():
        s="salmon"
    elif "blue" in s.lower():
        s="blue"
    elif "angel" in s.lower():
        s="angel"
    elif "goblin" in s.lower():
        s="goblin"
    elif "baskin" in s.lower():
        s="baskin"
    elif "copper" in s.lower():
        s="copper"
    elif "reef" in s.lower():
        s="reef"
    elif "gill" in s.lower():
        s="sevengill"
    elif "soup" in s.lower():
        s="soupfin"
    elif "cow" in s.lower():
        s="cow"
    elif "beagle" in s.lower():
        s="porbeagle"
    elif "mako" in s.lower():
        s="mako"
    else:
        s="unknown"
    return s

def clean_fatal(s):
    if " N" in s:
        s="N"
    elif "y" in s:
        s="Y"
    elif "UNKNOWN" in s:
        s="unknown"
    elif "M" in s:
        s="N"
    elif "N " in s:
        s="N"
    elif "2017" in s:
        s="unknown"
    return s

def clean_age(s):
    try:
        s=float(s)
        if 0<s<=20:
            return "Between 0 and 20 years"
        elif 20<s<=40:
            return "Between 21 and 40 years"
        elif 40<s<=60:
            return "Between 41 and 60 years"
        elif 60<s<=80:
            return "Between 61 and 80 years"
        elif s>80:
            return "More than 80 years"
    except:
        return "unknown"
def clean_year(s):
    try:
        s=float(s)
        return s
    except:
        return 1000000
    
def clean_year2(s):        
    s=float(s)
    if 1500<s<=1600:
        return "Between 1500 and 1600"
    elif 1600<s<=1700:
        return "Between 1600 and 1700"
    elif 1700<s<=1800:
        return "Between 1700 and 1800"
    elif 1800<s<=1900:
        return "Between 1800 and 1900"
    elif 1900<s<=2000:
        return "Between 1900 and 2000"
    elif 2000<s<2019:
        return "More than 2000"
    else:
        return "unknown"    
t=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
def clean_date(s):        
    if "jan" in s.lower():
        return "jan"
    elif "feb" in s.lower():
        return "feb"
    elif "mar" in s.lower():
        return "mar"
    elif "ap" in s.lower():
        return "apr"
    elif "may" in s.lower():
        return "may"
    elif "jun" in s.lower():
        return "jun"
    elif "jul" in s.lower():
        return "jul"
    elif "aug" in s.lower():
        return "aug"
    elif "sep" in s.lower():
        return "sep"
    elif "oct" in s.lower():
        return "oct"
    elif "nov" in s.lower():
        return "nov"
    elif "dec" in s.lower():
        return "dec"
    else:
        return "unknown"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    























