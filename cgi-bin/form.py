#!C:/Python3.6/python.exe
import os, cgi, cgitb
from datetime import datetime

form = cgi.FieldStorage()
time = datetime.now()

print("content-type: text/html\n\n")
print
print("<html><head><title>Post Message</title></head><body>")
print("<form method='POST' action='http://localhost:80/cgi-bin/form.py'>")
print("Name: <br> <input type='text' size='14' name='name'><br><br>")
print("Massage: <br> <textarea rows ='3' cols=46 name='msn'>--Message--</textarea><br><br>")
print("<input type='submit'></form>")

ler = open('C:/xampp/cgi-bin/message.txt', 'r')
recados = ler.read()
ler.close()
escreve = open('C:/xampp/cgi-bin/message.txt', 'w')
escreve.write("Name: "+form["name"].value + "<br>")
escreve.write("Message: "+form["msn"].value + "<br>")
escreve.write("Time: %sh:%smin<br/>" % (time.hour, time.minute))
escreve.write("Date: %s/%s/%s<br/>" % (time.day, time.month, time.year))
escreve.write(recados)
escreve.close()
antigo = open('C:/xampp/cgi-bin/message.txt', 'r')
imprimir = antigo.read()
antigo.close()
print(imprimir)
print

print("</body></html>")
