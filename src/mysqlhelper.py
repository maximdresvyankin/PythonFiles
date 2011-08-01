#-*- coding=utf-8 -*-
'''
Created on 9 лип. 2011

@author: tree
'''
import MySQLdb
import sys

class mysqlhelper(object):
    '''
    classdocs
    '''


    def __init__(self, dbhost, dbuser, dbpass, dbscheme):
        '''
        Creating DB connection
        '''
        try:
            self.connection = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpass, db=dbscheme)
            self.cursor = self.connection.cursor()
        except MySQLdb.Error, e:
            print('Error {0} : {1}'.format(e.args[0], e.args[1]))
            sys.exit (1)

    
    def mhfetchrow(self, dbtablename, dbwhere):
        '''
        Get string from DB using
        sql = SELECT * FROM {tablename} WHERE {something}
        '''
        try:
            sql = "SELECT * FROM %s WHERE %s" % (dbtablename, dbwhere)
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except MySQLdb.Error, e:
            print('Error {0} : {1}'.format(e.args[0], e.args[1]))
            sys.exit (1)
    
    def mhprintresult(self, dbtablename, dbwhere):
        '''
        Print results of mhfetchrow
        '''
        for records in self.mhfetchrow(dbtablename, dbwhere):
            for i in range(0, len(records)):
                print "%s \t" % records[i], "|",
            print "\n"
            print "#" * 80
    
    def mhsqlrun (self,sql):
        '''
        Run any SQL
        '''
        try:
            self.cursor.execute(sql)
            self.cursor.close()
            self.commit()
        except MySQLdb.Error, e:
            print('Error {0} : {1}'.format(e.args[0], e.args[1]))
            sys.exit (1)
        
            
    def mhinsert(self, dbtable, dbtablerow, dbtablevalues):
        """
        Simple Insert in table
        """
        try:
            sql = "INSERT INTO %s (%s) VALUES %s" % (dbtable, dbtablerow, tuple(dbtablevalues))
            self.cursor.execute(sql)
        except MySQLdb.Error, e:
            print('Error {0} : {1}'.format(e.args[0], e.args[1]))
            sys.exit (1)
        
    def commit(self):
        """
        Commit changes
        """
        try:
            self.connection.commit()
        except MySQLdb.Error, e:
            print('Error {0} : {1}'.format(e.args[0], e.args[1]))
            sys.exit (1)