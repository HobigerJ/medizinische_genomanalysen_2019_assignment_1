#!/usr/bin/env python3

import mysql.connector
import pysam
import pybedtools

__author__ = "Johanna Hobiger"

##
## Concept:
## TODO
##
samfile = pysam.AlignmentFile("chr21.bam", "rb") 
# bzw "ex1.sam", "r" für SAM files. rb = readbinary

class Assignment1:
    
    def __init__(self):
        self.gene = "CTSB"
        self.genome_reference = "hg38"
        self.genedict = self.download_gene_coordinates(file_name="test.txt")

    
    def download_gene_coordinates(self, file_name):
        
        print("Connecting to UCSC to fetch data")
        
        ## Open connection
        cnx = mysql.connector.connect(host='genome-mysql.cse.ucsc.edu', user='genomep', passwd='password', db=self.genome_reference)
        
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
        query = 'SELECT DISTINCT %s from refGene' % ','.join(query_fields) + \
        ' WHERE refGene.name2="' + self.gene + '"'
        
        ## Execute query
        cursor.execute(query)
        
        ## Write to file
        genedict = {}
        with open(file_name, "w") as fh:
            for row in cursor:
                fh.write(str(row) + "\n")
                genedict = {
                "name2": row[0],
                "name": row[1],
                "chrom": row[2],
                "txStart": row[3],
                "txEnd": row[4],
                "strand": row[5],
                "exonCount": row[6],
                "exonStarts": row[7],
                "exonEnds": row[8]
                }    
            
        ## Close cursor & connection
        cursor.close()
        cnx.close()
        print("Done fetching data")
        return genedict
        
    def get_coordinates_of_gene(self):
        '''with open(coordinates_file, "r") as fh:
            for line in fh.readlines():
                coord = line.strip("'").strip(" ").strip("'").strip("(").split(",")
                if coord[0] == "'"+genename+"'":
                    coord_string = "chr21:" + coord[3].strip(" ") + "-" + coord[4].strip(" ")
                    coord_list = [coord[3].strip(" "), coord[4].strip(" ")]
                    print("coordstring: ", coord_string, "coordliste: ", coord_list)'''

        print("Coordinates of gene " + self.gene + ": ")
        print("Start:\t", self.genedict["txStart"], "\nEnd:\t", self.genedict["txEnd"])
        
    def get_gene_symbol(self):
        print("Gene Symbol: ")
        print(self.genedict["name"])
        print()
                        
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
        self.get_coordinates_of_gene()
        print("Print all results here")
    
    
def main():
    print("Assignment 1")
    assignment1 = Assignment1()
    assignment1.print_summary()
    #assignment1.download_gene_coordinates("gene_coordinates")
    
    
    print("Done with assignment 1")
    
        
if __name__ == '__main__':
    main()
    
    
