from loader import db
class html_Table():
    def __init__(self) -> None:
        self.db = db
        self.Html1="""
        <!DOCTYPE html>
            <head>
                <title>Tables</title>
                <style>
                    table {
                        border-collapse: collapse;
                        width: 40%;
                        margin-right: 20px;
                        margin-bottom: 20px;
                        font-size: 10px;
                        float: left;
                    }
                    th, td {
                        border: 1px solid black;
                        padding: 10px;
                    }
                </style>
            </head>
        """
    def HTML(self):
        self.Html1 +=f"""
            <body>
                {self.Tables()}
            </body>
        </html>
        """
        with open("data/index.html","w",encoding="utf8") as f:
            f.write(self.Html1)
    def Tables(self):
        self.html = ""
        for i in self.db.execute("SELECT name FROM sqlite_master WHERE type='table'",fetchall=True,log=False):
        #for i in [('UZ',),('EN',),('RU',)]:
            head=self.db.execute(f"SELECT name FROM PRAGMA_TABLE_INFO('{i[0]}')",fetchall=True,log=False)
            body=self.db.execute(f"SELECT * FROM {i[0]}",fetchall=True,log=False)
            self.html += self.create_table(i[0],head, body)
        return self.html
    def create_table(self,name, head, body):
        table_html = f"<table><thead><tr><th>{name}</th></tr><tr>"
        for i in head:
            table_html += f"<th>{i[0]}</th>"
        table_html += "</tr></thead><tbody>"
        for i in body:
            table_html += "<tr>"
            for h in i:
                table_html += f"<td>{h}</td>"
            table_html += "</tr>"
        table_html += "</tbody></table>"
        return table_html
