import glob
import re
import os
import time
import datetime
import itertools
import collections
from itertools import groupby

'''
    渡されたディレクトリ配下にある指定の拡張子のファイルを再帰的に取得し、
    リストにして返す
    path:検索ディレクトリのパス
    ext_list:拡張子のリスト
    header_list:行タイトルのリスト
'''
class FileList:
    def __init__(self, path, ext_list):
        # 対象月
        self.path  = path
        # 拡張子のリスト
        self.ext_list = ext_list
        if len(ext_list) <= 0 :
            raise ValueError("拡張子の個数が0です")
    
    # フルパスのリストを返す
    def get_allfile_list(self, rng):
        try:
            # 返すリスト
            p_list = []
            
            # 指定の拡張子ですべて取得
            for ext in self.ext_list :
                for p in glob.iglob(self.path + '/**/*.' + ext, recursive=True) :
                    time = os.stat(p).st_mtime
                    d = datetime.datetime.fromtimestamp(time)
                    print(str(p))
                    for i in rng :
                        # フォルダ別に分ける
                        if i in p :
                            stamp = d.strftime("%Y%m%d")
                            year = d.strftime("%Y")
                            month = d.strftime("%m")
                            p_list.append([p, stamp, i, year, month])
            
            return p_list
        except :
            print("get list error!")

    """
        フルパスとそのファイルが所属するトップフォルダのリストを返す
        rng:検索範囲のフォルダ
        year:検索年の配列
        month:検索月の配列
    """
    def get_filelists_withdate(self, rng, yaers, months):
        try:
            if not rng: 
                print("検索範囲が指定されていません") 
                return None
            if not yaers: 
                print("検索年が指定されていません") 
                return None
            if not months: 
                print("検索月が指定されていません") 
                return None
            # 返すリスト
            p_list = []
            # 指定の拡張子ですべて取得
            result = self.get_allfile_list(rng)

            for year in yaers:
                for month in months:
                    for i in result:
                        # 月は2桁で判定
                        if str(year) in i and str(month).zfill(2) in i:
                            print(i)
                            p_list.append(i)
            print(p_list)
            return p_list
        except :
            print("get lists error!")

    """
        フルパスとそのファイルが所属するトップフォルダのリストを返す
        rng:検索範囲のフォルダ
        year:検索年
        month:検索月
    """
    def get_filelist_withtop(self, rng, yaer, month):
        try:
            if rng == None: return None
            # 返すリスト
            p_list = []
            if len(self.ext_list) <= 0 :  return
            
            for ext in self.ext_list :
                for p in glob.iglob(self.path + '/**/*.' + ext, recursive=True) :
                    time = os.stat(p).st_mtime
                    d = datetime.datetime.fromtimestamp(time)
                    if d.year == yaer and d.month == month :
                        print(str(p))
                        for i in rng :
                            if i in p :
                                stamp = d.strftime("%Y%m%d")
                                p_list.append([p, stamp, i])
            return p_list
        except :
            print("get list error!")