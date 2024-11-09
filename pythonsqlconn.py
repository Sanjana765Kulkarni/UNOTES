import mysql.connector as msc
import sys
global conn,crsr

def CreateConn():
    global conn, crsr

    try:
        conn = msc.connect(host="localhost", user="root", passwd="pwsd", database="Project")
        crsr=conn.cursor()

        if conn.is_connected():
            print("Connection exists.")
        else:
            print("Connection doesnt exist but will create now.")
            CreateConn()

    except msc.Error as e:
        err="Error connecting to Database. "+str(e)
        sys.exit(1)

def CloseConn():
    global conn, crsr
    try:
        conn.close()
        crsr.close()

    except msc.Error as e:
        err="There was an error closing the connection. "+str(e)

def InsertCinfo(fname,lname,phoneno,emailid):
    global conn, crsr
    CreateConn()
    try:
        searchq="SELECT * FROM cinfo WHERE Pno= %s"
        crsr.execute(searchq,(phoneno,))

        rdbks=crsr.fetchall()
        if rdbks:
            UpdateC(fname,lname,phoneno,emailid)
        else:
            AddC(fname,lname,phoneno,emailid)
        return("Info added successfully.")
        
    except msc.Error as er:
            err="There was an error searching for record. "+str(er)
            return(err)

    finally:
        CloseConn()
    
def UpdateC(fname,lname,phoneno,emailid):
    global conn, crsr
    CreateConn()
    try:
        updq="UPDATE cinfo SET "
        clmns=[]
        if fname:
            updq+="Fname=%s,"
            clmns.append(fname)
        if lname:
            updq+="Lname=%s,"
            clmns.append(lname)
        if emailid:
            updq+="Email=%s,"
            clmns.append(emailid)
        updq.rstrip(',')
        updq+="WHERE Pno=%s"
        clmns.append(phoneno)
        print(clmns)
        crsr.execute(updq,tuple(clmns))

        '''if(fname and lname and emailid):
            updq+="Fname = '{0}', Lname='{1}',Email='{2}' where Pno = {3}".format(fname,lname,emailid,phoneno)
            crsr.execute(updq)
            conn.commit()

        elif (fname and emailid ):
            updq+="Fname = '{0}', Email='{1}'where Pno = {2}".format(fname,emailid,phoneno)
            crsr.execute(updq)
            conn.commit()

        elif (lname and emailid):
            updq+="Lname = '{0}',Email='{1}' where Pno = {2}".format(lname,emailid,phoneno)
            crsr.execute(updq)
            conn.commit()

        elif(fname and lname):
            updq+="Fname='{0}',Lname='{1}' where Pno = {2}".format(fname,lname,phoneno)
            crsr.execute(updq)
            conn.commit()
            
        elif(fname):
            updq+="Fname = '{0}' where Pno = {1}".format(fname,phoneno)
            crsr.execute(updq)
            conn.commit()

        elif(lname):
            updq+="Lname='{0}' where Pno = {1}".format(lname,phoneno)
            crsr.execute(updq)
            conn.commit()

        elif(emailid):
            updq+="Email='{0}' where Pno = {1}".format(emailid,phoneno)
            crsr.execute(updq)
            conn.commit()'''

    except msc.Error as er:
        err="There was an error updating record. "+str(er)

    finally:
        CloseConn()

def AddC(fname,lname,phoneno,emailid):
    global crsr, conn
    CreateConn()
    try:
        addq="INSERT INTO cinfo (Pno, Fname, Lname, Email) VALUES (%s, %s, %s, %s)"
        crsr.execute(addq, (phoneno,fname, lname, emailid))
        conn.commit()

    except msc.Error as er:
        err="There was an error inserting record. "+str(er)

    finally:
        CloseConn()

def InsertNote(atr,sbj,tpc,cnt):
    global crsr, conn
    CreateConn()
    try:
        addq="INSERT INTO nts (Author, Subjct, Topic, Content) VALUES (%s, %s, %s,%s)"
        crsr.execute(addq, (atr,sbj,tpc,cnt))
        conn.commit()
        return("Note added successfully.")

    except msc.Error as er:
        err="There was an error inserting record. "+str(er)
        return(err)

    finally:
        CloseConn()

def Searchfor(skw):
    global crsr, conn
    CreateConn()
    try:
        searchq="SELECT * FROM nts WHERE Subjct LIKE %s OR Topic LIKE %s OR Content like %s "
        crsr.execute(searchq, ('%'+skw+'%', '%'+skw+'%','%'+skw+'%'))
            
        rdnts = crsr.fetchall()
        print("Printing search results.")
        #rdnts in searchFor python",rdnts,"end")
        if rdnts:
            return rdnts
        else:
            return None

    except msc.Error as er:
        err="There was an error searching for record "+str(er)
        return(err)

    finally:
        CloseConn()

def AllNotes():
    global conn, crsr
    CreateConn()

    try:
        dispq="SELECT * FROM nts"
        crsr.execute(dispq)
        dpnts=crsr.fetchall()
        print("Printing all notes")
        if dpnts:
            return dpnts
        else:
            return None

    except msc.Error as er:
        err="There was an error searching for record "+str(er)
        return(err)

    finally:
        CloseConn()
