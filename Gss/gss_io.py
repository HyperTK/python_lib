import gspread
from oauth2client.service_account import ServiceAccountCredentials

"""
    GoogleSpreadSheetの入出力を処理するクラス
"""
class Gss:
    """
        コンストラクタ
        json:GoogleサービスアカウントのJsonファイル(秘密鍵)
    """
    def __init__(self, json):
        if json is None:
            return
        scope = ["https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/drive"]
        self.credential = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
    
    """
        SpreadSheetのオブジェクトを取得する
    """
    def get_gs_object(self):
        return gspread.authorize(self.credential)

    """
        SpreadSheetのSheetをBookとSheetの名前で取得する
    """
    def get_gs_book(self, book_name, sheet_name):
        obj =  gspread.authorize(self.credential)
        book = obj.open(book_name).worksheet(sheet_name)
        return book

        