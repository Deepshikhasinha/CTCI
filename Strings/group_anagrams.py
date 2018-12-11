# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:52:17 2018

@author: dsinha1
"""

def groupAnagrams( strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        d = dict()
        for s in strs:
            tp = ''.join(sorted(s))
            if not tp in d:
                d[tp] = [s]
            else :
                d[tp].append(s)
        output=[]
        for key in d.keys():
            output.append(d[key])
        print(output)

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
