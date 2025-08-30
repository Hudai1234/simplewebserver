from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<HTML>
    <HEAD>
        <TITLE> </TITLE>
    </HEAD>
    <BODY BGCOLOR=" PINK">
        <TABLE BORDER="1" ALIGN="CENTER" BGCOLOR="PINK" CELLPADDING="10">
            <CAPTION><H1> LIST OF PROTOCOLS </H1></CAPTION>
            <TR><TH>S.NO</TH><TH> NAME OF THE PROTOCOL</TH><TH>EXAMPLE</TH>
            </TR>
        <TR>
            <TD>1</TD><TD>APPLICATION</TD><TD>HTTP,FTP,SSH,SMTP</TD>
        </TR>
        <TR>
            <TD>2</TD><TD>TRANSPORT</TD><TD>TCP & UDP</TD>
        </TR>
        <TR>
            <TD>3</TD><TD>NETWORK</TD><TD>ICMP,IGMP</TD>
        </TR>
        <TR>
            <TD>3</TD><TD>NETWORK ACCESS LAYER</TD><TD>ETHERNET</TD>
        </TR>
        </TABLE>
    </BODY>
</HTML>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
