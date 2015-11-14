# -*- coding: utf-8 -*-
"""
Created on Fri Dec 06 16:54:36 2013

@author: Zengliangwei
"""
import sqlite3
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from addr_book.models import People
def add_people(request):
    global ids
    if request.POST:
        post = request.POST
        new_people = People(
        name = post["name"],
        number = post["number"],
        phone = post["phone"],
        QQ = post["QQ"],
        email = post["email"],
        address = post["address"],
        birth = post["birth"],)
        if post["sex"] == 'M':
            new_people.sex = True
        else:
            new_people.sex = False
        new_people.save()
    people_list = People.objects.all()
    c = Context({"people_list":people_list,})   
    return render_to_response("form.html",c)
def main_page(request):
    output = '''
    <html align='center' >
    <head><title>%s</title></head>
    <body  background="/site_media/02.gif"  >
    <h1>%s</h1><p>%s</p>
    <p><a href='http://127.0.0.1:8000/addpeople/'>添加作者</a>
    <a href='http://127.0.0.1:8000/check/'>查看编辑作者</a></p>
    <img src="/site_media/4.jpg" width=900>
    </body>
    </html>
    ''' % (
    '图书管理',
    'USBOOK',
    '您可以使用以下功能',
    )
    return HttpResponse(output)
def check(request):
    if request.POST:
        post = request.POST
        for people in People.objects.all():
            if post["search"]==people.name:
                c = Context({"people":people,}) 
                return render_to_response("search.html",c)
        return render_to_response("Nonesearch.html")
    people_list = People.objects.all()
    c = Context({"people_list":people_list,}) 
    return render_to_response("check.html",c)
def delete(request):
    con=sqlite3.connect ('db.sqlite3')
    cur = con.cursor ()
    cur.execute ('delete from addr_book_people where id=?',(request.GET['id'],))
    con.commit()
    con.close()
    return render_to_response("delete.html")
def update(request):
    if request.POST:
        con=sqlite3.connect ('db.sqlite3')
        cur = con.cursor ()
        cur.execute ('delete from addr_book_people where id=?',(request.GET['id'],))
        con.commit()
        con.close()
        post = request.POST
        new_people = People(
        name = post["name"],
        number = post["number"],
        phone = post["phone"],
        QQ = post["QQ"],
        email = post["email"],
        address = post["address"],
        birth = post["birth"],)
        if post["sex"] == 'M':
            new_people.sex = True
        else:
            new_people.sex = False
        new_people.save()
        people_list = People.objects.all()
        c = Context({"people_list":people_list,}) 
        return render_to_response("updates.html",c)
    for people in People.objects.all():
        if int(request.GET['id'])==people.id:
            c = Context({"people":people,})
            return render_to_response("update.html",c)
    
    
    