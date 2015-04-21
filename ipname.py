#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# read a list of IP and return the Longitute and Langitute


import sys
import pygeoip


def read_ip(filename):
  rawdata = pygeoip.GeoIP('static/GeoLiteCity.dat')
  input_file = open(filename, 'r')
  myarray = []
  for line in input_file:
    words = line.split()
    ip = words[0]
    data = rawdata.record_by_name(ip)
    mydict = {}
    print "IP: " ,ip, "Latitude: ", data['latitude'],"Longitute", data['longitude'] 
    mydict['ip']=ip
    mydict['latitude']=data['latitude']
    mydict['longitude']=data['longitude']
    myarray.append(mydict)
  input_file.close()  # Not strictly required, but good form.
  print "My Array: ", myarray




# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  # if len(sys.argv) != 2:
  #   print 'usage: ./ipname.py ip_file'
  #   sys.exit(1)

  filename = sys.argv[1]
  read_ip(filename)

if __name__ == '__main__':
  main()
