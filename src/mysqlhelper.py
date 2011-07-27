#-*- coding=utf-8 -*-
'''
Created on 9 лип. 2011

@author: tree
'''
import MySQLdb

class mysqlhelper(object):
    '''
    classdocs
    '''


    def __init__(self, dbhost, dbuser, dbpass, dbscheme):
        '''
        Creating DB connection
        '''
        self.connection = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpass, db=dbscheme)
        self.cursor = self.connection.cursor()
    
    def mhfetchrow(self, dbtablename, dbwhere):
        '''
        Find one string from DB
        '''
        sql = "SELECT * FROM %s WHERE %s" % (dbtablename, dbwhere)
        print sql;
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
    
    def mhsqlrun (self,sql):
        self.cursor.execute(sql)
        self.cursor.close()
        self.commit()
        
    def mhprintresult(self, dbtablename, dbwhere):
        for records in self.mhfetchrow(dbtablename, dbwhere):
            for i in range(0, len(records)):
                print "%s \t" % records[i], "|",
            print "\n"
            print "#" * 80
    def mhinsert(self, dbtable, dbtablerow, dbtablevalues):
        print dbtablerow
        print tuple(dbtablevalues)
        sql = """
        INSERT INTO %s (%s) VALUES %s
        """ % (dbtable, dbtablerow, tuple(dbtablevalues))
        print sql
        self.cursor.execute(sql)
    def commit(self):
        self.connection.commit()
