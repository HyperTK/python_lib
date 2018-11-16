import csv
import traceback

'''
    CSVのIOを処理するクラス
    path:CSVファイル保存先フォルダ
    filename:CSVファイル名
'''
class CsvIo:
    # コンストラクタ
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename
    '''
        リストからCSVファイルを作成する
        str_list:CSVに書き出すリスト
        is_split:リストをファイルごとに分割するか
    '''
    def csv_list_writer(self, str_list, is_split):
        try:
            path = self.path + "/" + self.filename
            self.file_writer(str_list, path)
            # if is_split:
            #     for i in str_list:
            #         self.file_writer(i)
            # else:
            #     self.file_writer(li, path)

        except:
            print("error!ファイルを開いていたりしませんか？？")
            traceback.print_exc()
    
    '''
        CSV形式でファイルに書き込む
        li:CSVに書き出すリスト
    '''
    def file_writer(self, li, path):
        try:
            # csv 作成
            with open(path, "w") as f:
                # ファイル名
                writer = csv.writer(f, lineterminator="\n")
                writer.writerows(li)
        except:
            traceback.print_exc()