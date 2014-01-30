#! /usr/bin/python
print 'Content-Type: text/html\n\n'
import cgi, cgitb, lf
cgitb.enable()
#<--------------Everything is by Muhamed Rahman---------------->
page='''<html>
<head>
    <title>Search Results</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
</head>

<body>
    <script src="js/bootstrap.min.js"></script>'''

page += lf.makeNavBar()
page +='''
    <h1>
        Here are the Results:
    </h1>
    <table class="table">
        <tr>
            <th>item id</th><th>item name</th><th>owner</th><th>category</th>
            <th>bid</th><th>bidder</th><th>condition</th><th>description</th>
        </tr>'''

field=cgi.FieldStorage()

#<---Returns a table of all the matching results--->
def searchresults():
    field=cgi.FieldStorage()
    ans=''
    categories=['Electronics', 'Home_and_Kitchen', 'Education', 'category']
    if 'search' in field.keys():
        if field['search'].value != '':
            if 'category' in field.keys():
                for i in categories:
                    if field['category'].value==i:
                        f=open('../data/allfile.txt', 'r')
                        items=f.read().split('\n')
                        x=0
                        while x < len(items):
                            result=items[x].split(',')
                            if field['search'].value in result and result[3]==i:
                                ans+='<tr>'
                                for i in result:
                                    ans+='<td>'+i+'</td>'
                                ans+='''<td>
<form action="displayItem.py" method="get">
<input type="hidden" name="itemid" value="'''+result[0]+'''">
<input type="submit" value="Bid Here">
</form></td>'''
                                ans+='</tr>'
                                x+=1
                            elif field['search'].value in result:
                                ans+='<tr>'
                                for i in result:
                                    ans+='<td>'+i+'</td>'
                                ans+='''<td>
<form action="displayItem.py" method="get">
<input type="hidden" name="itemid" value="'''+result[0]+'''">
<input type="submit" value="Bid Here">
</form></td>'''
                                x+=1
                            else:
                                x+=1
                
        else:
            ans+='''<tr><td>No Results</td><tr>'''
    else:
        ans+='''Please enter a search!'''
    return ans




page+=searchresults()
page+='''</table>
</body>
</html>'''

print page
        
