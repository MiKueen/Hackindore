#!C:\Python36\python.exe


print("Content-type:text/html")
print("")


import cgi, cgitb, mysql.connector
import datetime,os



now = datetime.datetime.now()
date1=now.strftime("%Y-%m-%d")
cgitb.enable()

obj=cgi.FieldStorage()
id=obj.getvalue('id')

db=mysql.connector.connect(host="localhost",user="root",password="",database="mess")
cursor=db.cursor()
if id==None:
    id=""
query="select menuname from menu where date='"+date1+"' && admin='"+id+"' "
cursor.execute(query)
result=cursor.fetchall()
db.commit()

print("""
<html>
<head>
""")

    


print("""
    <title>Mess Manager</title>
</head>
<body style="text-align: center;">
<br/>
<h2>Hello """+id+"""</h2> &nbsp;&nbsp;&nbsp;&nbsp; <a href="./index.py" onclick="delcookie()">logout</a>
<h3>Responses for todays menus:</h3>
""")
if "HTTP_COOKIE" in os.environ:
    if id!=os.environ["HTTP_COOKIE"]:
        print("""   <script>window.location='http://localhost/pro1/index.py</script>  """)


else:
    print("HTTP_COOKIE not set!")
    print(""" <script>window.location='http://localhost/pro1/index.py';</script> """)


for element in result:
    menun=element[0]    
    query="select * from feedback where date='"+date1+"' "
    cursor.execute(query)
    result=cursor.fetchall()
    
    for x in result:
        tempd=x[2].strftime('%Y-%m-%d')
        print("ID="+x[0]+", Choice="+x[1]+", Date="+tempd+"<br/>")
    db.commit()
print("""<br/>
<h2>ADD A NEW MENU:</h2>
<form method="POST" action='regi1.py?id="""+id+"""'>
<h3>Date: &nbsp;<input type="date" name="date" id="date"> &nbsp;&nbsp; </h3><br/>
<h3>Menu name: &nbsp;<input type="text" name="menuname" id="menuname"></h3><br/>
<h3>Add Menu: </h3><br/>
<textarea id="tarea" name="tarea" rows="15" cols="50">
</textarea><br/>
<input type="submit" style="margin-top:1%;" value="SUBMIT MENU" name="submit" id="submit"/>
</form>
<script>
function delcookie(){

    var cookies = document.cookie.split(";");

    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        var eqPos = cookie.indexOf("=");
        var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
    }
    
    document.location.reload()
    alert("Redirecting.........")
}
</script>



</body>
</html>

""")