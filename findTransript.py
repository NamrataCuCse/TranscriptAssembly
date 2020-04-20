from random import sample
import numpy as np  
import collections, sys
import csv
from collections import defaultdict


filename=sys.argv[1]
readfile = open(filename,"r")
filedata = readfile.readlines()
readfile.close()
t_line=[]
for every_line in filedata:
       t_line.append(every_line.split())
size=len(t_line)     
kmer=[]
for i in range(len(t_line)):
    read = t_line[i]
    kmer.append(read[0])
graph={}                           
def find_transcripts(graph, start, end, transcript=[]):
        transcript = transcript + [start]
        if start == end:
            return [transcript]
        if not graph.has_key(start):
            return []
        transcripts = []
        for node in graph[start]:
            if node not in transcript:
                newtranscripts = find_transcripts(graph, node, end, transcript)
                for newtranscript in newtranscripts:
                    transcripts.append(newtranscript)
        return transcripts    
for i in range(len(kmer)):
    substr1 = kmer[i]      
    for j in range(len(kmer)):
        if i!=j :
            substr2 = kmer[j]
            start = 0
            for i in range(len(substr1)-2):
                stop = i   
                if len(substr1) > stop :
                    xx = substr1[0: start:] + substr1[stop + 1::]
                    if (substr2.startswith(xx)):
                        graph.setdefault(substr1, [])
                        graph[substr1].append(substr2)
                        
for i in range(len(kmer)):
    substr1 = kmer[i]      
    for j in range(len(kmer)):
        if i!=j :
            substr2 = kmer[j]
            print(find_transcripts(graph, substr1, substr2))
