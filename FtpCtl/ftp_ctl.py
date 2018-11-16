from ftplib import FTP

"""
    FTP接続クラス
"""
class FtpControll:
    """
        コンストラクタ
        接続オブジェクトを作成
        ip:FTP接続先IP
        user:ユーザ名
        pswd:パスワード
    """
    def __init__(self, ip, user, pswd):
        try:
            self.ftp = FTP(ip)
            self.ftp.login(user, pswd)
            self.cwd = ''
            self.saveDir = ''
        except:
            traceback.print_exc()
            self.ftp.quit()

    '''
        ファイルの保存先を指定する
        dir:保存先のディレクトリ
    '''
    def SetSaveDir(self, dir):
        self.saveDir = dir

    """
        カレントワーキングディレクトリをセットする
        cwd:現在のディレクトリ
    """
    def SetCwd(self, cwd):
        try:
            if len(cwd) <= 0:
                raise ValueError('The value is invalid')
            self.ftp.cwd(cwd)
            self.cwd = cwd
        except:
            traceback.print_exc()
            self.ftp.quit()

    """
        カレントディレクトリ内のリストを取得する
    """
    def GetDirList(self):
        try:
            files = self.ftp.nlst('.')
            return files
        except:
            traceback.print_exc()
            self.ftp.quit()

    """
        カレントディレクトリ配下のディレクトリのフルパスを取得する
        cwd:現在のディレクトリ
    """
    def GetDirPath(self, cwd):
        dirlist = glob.glob(cwd + '/*')
