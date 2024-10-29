import sqlite3
class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db
    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False,log=True):
        if not parameters:
            parameters = ()
        connection = self.connection
        if log:
            connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        
        if commit:
            connection.commit()#Сохраняем изменения
        if fetchall:
            data = cursor.fetchall()#Выбираем всех пользователей
        if fetchone:
            data = cursor.fetchone()# для получения данных по одной строке
        connection.close()#закрываем соединение
        return data
    
    def create_Xodimlar(self):
        sql="""
        CREATE TABLE Xodimlar(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT varchar(255) NOT NULL,
            Lavozim TEXT varchar(255) NOT NULL,
            photo TEXT varchar(1000) NOT NULL,
            Caption TEXT NOT NULL,
            Link TEXT NOT NULL
            )        
        """
        self.execute(sql, commit=True)
      
    def create_Kurslar(self):
        sql="""
        CREATE TABLE Kurslar(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT varchar(255) NOT NULL,
            File TEXT varchar(1000) NOT NULL,
            Caption TEXT NOT NULL,
            Link TEXT NOT NULL
            )        
        """
        self.execute(sql, commit=True)
    def create_main(self):
        sql="""
        CREATE TABLE PHOTO(
            NAME TEXT NOT NULL,
            PHOTO_ID TEXT NOT NULL
            )
        """
        self.execute(sql, commit=True)
        self.execute("INSERT INTO PHOTO(NAME,PHOTO_ID) VALUES(?,?)",("Loby","AgACAgIAAxkBAAIIq2cUt6ee5nV7yAPk4hYxZjul8xr9AAKd2zEbyjipSMPuN2GREPxLAQADAgADeAADNgQ"), commit=True)
        self.execute("INSERT INTO PHOTO(NAME,PHOTO_ID) VALUES(?,?)",("Menu","AgACAgIAAxkBAAIIq2cUt6ee5nV7yAPk4hYxZjul8xr9AAKd2zEbyjipSMPuN2GREPxLAQADAgADeAADNgQ"), commit=True)
        self.execute("INSERT INTO PHOTO(NAME,PHOTO_ID) VALUES(?,?)",("Xodimlar","AgACAgIAAxkBAAIIq2cUt6ee5nV7yAPk4hYxZjul8xr9AAKd2zEbyjipSMPuN2GREPxLAQADAgADeAADNgQ"), commit=True)
        self.execute("INSERT INTO PHOTO(NAME,PHOTO_ID) VALUES(?,?)",("Kurslar","AgACAgIAAxkBAAIIq2cUt6ee5nV7yAPk4hYxZjul8xr9AAKd2zEbyjipSMPuN2GREPxLAQADAgADeAADNgQ"), commit=True)
        self.execute("INSERT INTO PHOTO(NAME,PHOTO_ID) VALUES(?,?)",("About","AgACAgIAAxkBAAIIq2cUt6ee5nV7yAPk4hYxZjul8xr9AAKd2zEbyjipSMPuN2GREPxLAQADAgADeAADNgQ"), commit=True)
    
        
    def Get(self,Name):
        sql = f"SELECT * FROM {Name}"
        return self.execute(sql, fetchall=True)
    def GetLang(self,Lang ,Item):
        sql=f"""SELECT * FROM {Lang} WHERE Item = '{Item}'"""
        try:
            return self.execute(sql, fetchone=True,log=False)[1]
        except:return Item
    def delete(self,Table:str, ID:int):
        sql = f"DELETE FROM {Table} WHERE ID = {ID}"
        self.execute(sql, commit=True)
        
    def getUserLang(self,id):
        sql = f"SELECT Language FROM Users WHERE User_ID = {id}"
        return self.execute(sql, fetchone=True,log=False)[0]
    def Find(self,Name,id):
        sql=f"""SELECT * FROM {Name} WHERE ID = {id}"""
        return self.execute(sql, fetchone=True)
    def SQL_Command(self,SQL:str):
        if SQL.split()[0] not in ['CREATE','INSERT','UPDATE','DROP','DELETE']:
            try:
                b=SQL.__len__()
                for i in self.execute("SELECT name FROM sqlite_master WHERE type='table'",fetchall=True):
                    if i[0].lower() in SQL.lower() and SQL.find(i[0])<b:
                        a=self.execute(f"SELECT name FROM PRAGMA_TABLE_INFO('{i[0]}')",fetchall=True)
                        b=SQL.find(i[0])
                for i in range(len(a)):
                    a[i]=a[i][0]
                a=[tuple(a)]
            except:a=[]

        if SQL.split()[0] in ['CREATE','INSERT','UPDATE','DROP','DELETE']:
            self.execute(SQL, commit=True)
            if SQL.split()[0] in ['DELETE','INSERT']:
                table=SQL.split()[2]
                f=table.find('(')
                if f != -1:
                    table=table[:f]
                print(table)
                try:
                    a=self.execute(f"SELECT NAME FROM {table}", fetchall=True)
                    print(a)  
                    for i in range(len(a)):
                        name=a[i][0]
                        self.execute(f"UPDATE {table} SET ID = {i+1} WHERE Name = '{name}'",commit=True,log=False)
                except:None
            return "UPDATED"
        else:
            return f"<pre><code class=\"language-sql\">{a}\n{self.execute(SQL,fetchall=True)}\n</code></pre>".replace("<br>","").replace("),",")\n")
def logger(statement):
    print(f"""SQL: {statement}""")