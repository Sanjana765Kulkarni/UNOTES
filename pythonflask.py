from flask import Flask, redirect, url_for, request,render_template
from pythonsqlconn import *

app=Flask(__name__)

@app.route("/")
def home():
        return render_template("unoteshomeclr.html")

@app.route("/contact",methods=["GET","POST"])
def getcontactinfo():

    if request.method=="GET":
        return (render_template("unoteshomeclr.html")) 

    fname=request.form["fname"]
    lname=request.form["lname"]
    phoneno=request.form["phoneno"]
    emailid=request.form["emailid"]

    if(request.form["action_button"]=="Submit"):
        cinmsg=InsertCinfo(fname,lname,phoneno,emailid)
        print("Yay for inserting cinfo")

    return(render_template("unoteshomeclr.html",fn=fname,ln=lname,pn=phoneno,em=emailid,cmsg=cinmsg))

@app.route("/browse")
def browse():
    return(render_template("searchingclr.html"))

@app.route("/retcontact")
def recontact():
    return redirect(url_for('getcontactinfo'))

@app.route("/addn",methods=["GET","POST"])
def addn():

    if request.method=="GET":
        return (render_template("add_notesclr.html"))

    autr=request.form["author"]
    sbjt=request.form["subject"]
    tpc=request.form["topic"]
    cntnt=request.form["body"]

    if(request.form["action_button"]=="Add"):
         msg=InsertNote(autr,sbjt,tpc,cntnt)
         print("Yay for note insertion")

    return(render_template("add_notesclr.html",athr=autr,subj=sbjt,topc=tpc,cont=cntnt,addmsg=msg))

@app.route("/searchn",methods=["GET","POST"])
def searchn():

    if request.method=="GET":
        return (render_template("searchingclr.html"))


    if(request.form["action_button"]=="Search"):
        skword=request.form["search"]
        retval=Searchfor(skword)
        print("Yay for sending search query and receiving return")


    elif(request.form["action_button"]=="All"):
        retval=AllNotes()
        print("Yay for sending search query and receiving return")
        

    return(render_template("searchingclr.html",rtv=retval))

if __name__=="__main__":
    app.run(port=9000) 
