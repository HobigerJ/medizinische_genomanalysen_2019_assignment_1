#!/usr/bin/env python3

import mysql.connector
import pysam

__author__ = "Johanna Hobiger"

##
## Concept:
## TODO
##
samfile = pysam.AlignmentFile("chr21.bam", "rb") 
# bzw "ex1.sam", "r" für SAM files. rb = readbinary

class Assignment1:
    
    def __init__(self):
        ## Your gene of interest
        self.gene = "CTSB"

    
    def download_gene_coordinates(self, genome_reference, file_name):
        #genome_reference = "hg38", filename = "gene_coordinates" file in das hinein geschrieben wird
        ## TODO concept

        
        print("Connecting to UCSC to fetch data")
        
        ## Open connection
        cnx = mysql.connector.connect(host='genome-mysql.cse.ucsc.edu', user='genomep', passwd='password', db=genome_reference)
        
        ## Get cursor
        cursor = cnx.cursor()
        
        ## Build query fields
        query_fields = ["refGene.name2",
                        "refGene.name",
                        "refGene.chrom",
                        "refGene.txStart",
                        "refGene.txEnd",
                        "refGene.strand",
                        "refGene.exonCount",
                        "refGene.exonStarts",
                        "refGene.exonEnds"]
        
        ## Build query
        query = "SELECT DISTINCT %s from refGene" % ",".join(query_fields)
        
        ## Execute query
        cursor.execute(query)
        
        ## Write to file
        ## TODO this may need some work 
        with open(file_name, "w") as fh:
            for row in cursor:
                fh.write(str(row) + "\n")
    
            
        ## Close cursor & connection
        cursor.close()
        cnx.close()
        
        print("Done fetching data")
        
    def get_coordinates_of_gene(self, coordinates_file, genename):
        with open(coordinates_file, "r") as fh:
            for line in fh.readlines():
                coord = line.strip("'").strip(" ").strip("'").strip("(").split(",")
                if coord[0] == "'"+genename+"'":
                    coord_string = "chr21:" + coord[3].strip(" ") + "-" + coord[4].strip(" ")
                    coord_list = [coord[3].strip(" "), coord[4].strip(" ")]
                    print("coordstring: ", coord_string, "coordliste: ", coord_list)
        
        ## Use UCSC file
        print("todo")
        
    def get_gene_symbol(self):
        print("todo")
                        
    def get_sam_header(self):
        print("todo") # pysam verwenden
        
    def get_properly_paired_reads_of_gene(self): # pysam verwenden
        print("todo")
        
    def get_gene_reads_with_indels(self): # pysam verwenden
        print("todo")
        
    def calculate_total_average_coverage(self): # pysam verwenden
        print("todo")
        
    def calculate_gene_average_coverage(self): # pybed tools. Command Line Tools mit subprocess verwenden
        print("todo")
        
    def get_number_mapped_reads(self): # pysam verwenden?
        print("todo")

    def get_region_of_gene(self): # pysam verwenden?
        print("todo")
        
    def get_number_of_exons(self): # pysam verwenden?
        print("ads")
    
    
    def print_summary(self):
        print("Print all results here")
    
    
def main():
    print("Assignment 1")
    assignment1 = Assignment1()
    assignment1.print_summary()
    #assignment1.download_gene_coordinates("hg38", "gene_coordinates")
    assignment1.get_coordinates_of_gene("gene_coordinates", "GSN")
    for line in samfile:
        print(line)
    
    print("Done with assignment 1")
    
        
if __name__ == '__main__':
    main()
    
    
