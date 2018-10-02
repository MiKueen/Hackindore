#!C:\Python36\python.exe


print("Content-type:text/html")
print("")
print("""
<!DOCTYPE html>
<html>
    <style>
        form {
            margin-top:60px;   
        }

        body {
            background-image: url('images/food.jpg');
            background-repeat: no-repeat;
            background-size: 100%;
        }

        a {
            text-decoration: none;
            color: black;
            margin-top:70px;
        }

        button {
            background-color: black;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            width: 100%;
        }

        button:hover {
            opacity: 0.8;
        }


        .btn{
            width: auto;
            padding: 10px 18px;
            background: black;
            color: white;
        }

        .imgcontainer {
            text-align: center;
            margin-top:20px;
        }

        img.avatar {
            width: 25%;
            border-radius: 8px;
            float:left;
        }

        .container {
            padding: 0px;
        }

        #login_id {
            border-radius: 25px;
            width:200px;
            height:20px;
            padding:8px;
        }

        #login_pass {
            border-radius: 25px;
            width:200px;
            height:20px;
            padding:8px;
        }

        h1 {
            color:grey;
            font-size: 40px;
            font-weight: 900;
        }

        .D {
            font-size: 30px;
            font-weight: 900;
        }

        @media screen and (max-width: 300px) {
            span.login_pass {
            display: block;
            float: none;
            }
        }
    </style>

    <body>
        <form method="POST" action="regi.py">
            <h1 id="heading">Welcome Folks!</h1>
            <div class="imgcontainer">
                <img src="images/lo.png" alt="Avatar" class="avatar" height="280" width="320">
            </div>
            <div class="container">
                <table cellpadding="8px" cellspacing="0px">
                    <tr>
                        <td><label class="D"><b>User ID</b></label></td>
                        <td><input type="text" placeholder="Enter User ID" name="login_id" id="login_id" required></td>
                    </tr><br>
                    <tr>
                        <td><label class="D"><b>Password</b></label></td>
                        <td><input type="password" placeholder="Enter Password" name="login_pass" id="login_pass" required></td>
                    </tr>
                </table>
            </div>
            <div class="container">
                <table cellspacing="10px">
                    <tr>
                        <td><button type="submit" class="btn" value="SUBMIT" name="submit">Login</td>
                        <td><button type="submit" class="btn" value="SIGNUP"><a href="signup.py" class="btn">SIGN UP</a></td>
                    </tr>
                </table>
            </div>
        </form>

        <script>
            $(window).on('popstate', function(event) {
                alert("pop");
            });
        </script>
""")

import cgi, cgitb, mysql.connector
cgitb.enable()
obj=cgi.FieldStorage()
submit=obj.getvalue("submit")

role=""
if submit!=None:
    login_id=obj.getvalue("login_id")
    xpass=obj.getvalue("login_pass")
    db=mysql.connector.connect(host="localhost",user="root",password="",database="mess")
    cursor=db.cursor()
    query="select * from login where id='%s'"%login_id
    cursor.execute(query)
    result=cursor.fetchall()
    db.commit()
    resultfine=result[0]
    passw=resultfine[1]
    role=resultfine[2]
    if passw==xpass:
        print("Login successful")
        
    else:
        print("Login not successful")    
    

print('''
</body>
</html>
''')
