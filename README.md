## GenBank-GFF

### 1. Python script running on terminal
#### 1.1 Build python environment
```bash
conda create -n genbank-gff python=3.9
conda activate genbank-gff

# Pip installation module can effectively reduce the volume of executable files compiled by pyinstaller.
pip install biopython
pip install bcbio-gff
pip install pyinstaller
```
#### 1.2 Run python script
```bash
conda activate genbank-gff

python genbank-gff.py
```
#### 1.3 Program execution process
```bash
python genbank-gff.py
Please input GenBank format file path/filename(.gbff):
./GCF_010614865.1_ASM1061486v1_genomic.gbff.gz 
Please input GFF format file path/filename(.gff/.gff3):
./GCF_010614865.1_ASM1061486v1_genomic.gff    
Confirm Information:
Input GenBank File:./GCF_010614865.1_ASM1061486v1_genomic.gbff.gz;
Output GFF File:./GCF_010614865.1_ASM1061486v1_genomic.gff
Please ENTER to start conversion.

Need to uncompress the .gz file! Please input 'yes' to uncompress.
yes
Uncompressing...
Uncompressed!
Converting...
Converted!
```
#### 1.4 [Input file] GenBank format file content
```txt
LOCUS       NW_023312688          196462 bp    DNA     linear   CON 07-JUL-2020
DEFINITION  Stegodyphus dumicola isolate AA2019 ecotype Namibia, Etosha
            unplaced genomic scaffold, ASM1061486v1 SEQ_00001, whole genome
            shotgun sequence.
ACCESSION   NW_023312688
VERSION     NW_023312688.1
DBLINK      BioProject: PRJNA642917
            BioSample: SAMN13619660
            Assembly: GCF_010614865.1
KEYWORDS    WGS; RefSeq.
SOURCE      Stegodyphus dumicola
  ORGANISM  Stegodyphus dumicola
            Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Chelicerata; Arachnida;
            Araneae; Araneomorphae; Entelegynae; Eresoidea; Eresidae;
            Stegodyphus.
REFERENCE   1  (bases 1 to 196462)
  AUTHORS   Liu,S., Aageaard,A., Bechsgaard,J. and Bilde,T.
  TITLE     DNA Methylation Patterns in the Social Spider, Stegodyphus dumicola
  JOURNAL   Genes (Basel) 10 (2), E137 (2019)
   PUBMED   30759892
  REMARK    Publication Status: Online-Only
COMMENT     REFSEQ INFORMATION: The reference sequence is identical to
            JAADJH010000001.1.
            Assembly name: ASM1061486v1
            The genomic sequence for this RefSeq record is from the
            whole-genome assembly released by the None on 2020/02/14. The
            original whole-genome shotgun project has the accession
            JAADJH000000000.1.

            ##Genome-Assembly-Data-START##
            Assembly Provider      :: None
            Assembly Method        :: DBG2OLC v. Nov 16th, 2017
            Genome Representation  :: Full
            Expected Final Version :: Yes
            Features Annotated          :: Gene; mRNA; CDS; ncRNA
            ##Genome-Annotation-Data-END##
FEATURES             Location/Qualifiers
     source          1..196462
                     /organism="Stegodyphus dumicola"
                     /mol_type="genomic DNA"
                     /isolate="AA2019"
                     /isolation_source="tree"
                     /db_xref="taxon:202533"
                     /chromosome="Unknown"
                     /tissue_type="whole individual"
                     /ecotype="Namibia, Etosha"
                     /country="Namibia"
                     /lat_lon="19.06232 S 17.86362 E"
                     /collection_date="Jan-2017"
     gene            27109..87988
                     /gene="LOC118188962"
                     /note="Derived by automated computational analysis using
                     gene prediction method: Gnomon."
                     /db_xref="GeneID:118188962"
     mRNA            join(27109..27370,36197..36309,36398..36491,48378..48632,
                     64458..64527,64681..64766,74809..74957,77345..77481,
                     87849..87988)
                     /gene="LOC118188962"
                     /product="immunoglobulin-binding protein 1-like"
                     /note="Derived by automated computational analysis using
                     gene prediction method: Gnomon. Supporting evidence
                     includes similarity to: 6 Proteins, and 100% coverage of
                     the annotated genomic feature by RNAseq alignments,
                     including 51 samples with support for all annotated
                     introns"
                     /transcript_id="XM_035362696.1"
                     /db_xref="GeneID:118188962"
     CDS             join(27203..27370,36197..36309,36398..36491,48378..48632,
                     64458..64527,64681..64766,74809..74957,77345..77481,
                     87849..87889)
                     /gene="LOC118188962"
                     /note="Derived by automated computational analysis using
                     gene prediction method: Gnomon."
                     /codon_start=1
                     /product="immunoglobulin-binding protein 1-like"
                     /protein_id="XP_035218587.1"
                     /db_xref="GeneID:118188962"
                     /translation="MTSSELSLVLQSLTPLEEKTVDDKSGSILSKTFDSCCQAYDLIQ
                     DSDLDSSNTEIQGAISQCIKHLELCTHMVNELNLFSSNEAIGEVQTSSLKYLLLPALL
                     GSLNLQVQHKDMSKRLENLHIAEVYFKDFLLRCRNYELCTVELPEDFEEDGLENGDSS
                     VKNSSHAHNVLDAAIVRERKIQQYKRTKELEKREKELKPALVRPDAEEFIREYYMILL
                     EKWIMTVTAELETVKTEKNIVGTMVQMKDKSGNNLNRKESVKAKPLKTIIITKNEIQK
                     KVFGMGYPSLPVMTIDDFYRQRFEKAIQEQKSAVKGMSLQEKALYGDDNTKEEEEIKK
                     EELMEKDDPVELAKARQWNDWKDENPRGSGNRKNKG"
```
#### 1.5 [Output file] GFF format content
```txt
##gff-version 3
##sequence-region NW_023312688.1 1 196462
NW_023312688.1  annotation      remark  1       196462  .       .       .       accessions=NW_023312688;comment=REFSEQ INFORMATION: The reference sequence is identical to%0AJAADJH010000001.1.%0AAssembly name: ASM1061486v1%0AThe genomic sequence for this RefSeq record is from the%0Awhole-genome assembly released by the None on 2020/02/14. The%0Aoriginal whole-genome shotgun project has the accession%0AJAADJH000000000.1.;contig=join%28JAADJH010000001.1:1..196462%29;data_file_division=CON;date=07-JUL-2020;keywords=WGS,RefSeq;molecule_type=DNA;organism=Stegodyphus dumicola;references=location: %5B0:196462%5D%0Aauthors: Liu%2CS.%2C Aageaard%2CA.%2C Bechsgaard%2CJ. and Bilde%2CT.%0Atitle: DNA Methylation Patterns in the Social Spider%2C Stegodyphus dumicola%0Ajournal: Genes %28Basel%29 10 %282%29%2C E137 %282019%29%0Amedline id: %0Apubmed id: 30759892%0Acomment: Publication Status: Online-Only;sequence_version=1;source=Stegodyphus dumicola;structured_comment=OrderedDict%28%5B%28%27Genome-Assembly-Data%27%2C OrderedDict%28%5B%28%27Assembly Provider%27%2C %27None%27%29%2C %28%27Assembly Method%27%2C %27DBG2OLC v. Nov 16th%2C 2017%27%29%2C %28%27Genome Representation%27%2C %27Full%27%29%2C %28%27Expected Final Version%27%2C %27Yes%27%29%2C %28%27Genome Coverage%27%2C %2779.0x%27%29%2C %28%27Sequencing Technology%27%2C %27Illumina HiSeq%3B PacBio%27%29%5D%29%29%2C %28%27Genome-Annotation-Data%27%2C OrderedDict%28%5B%28%27Annotation Provider%27%2C %27NCBI%27%29%2C %28%27Annotation Status%27%2C %27Full annotation%27%29%2C %28%27Annotation Name%27%2C %27Stegodyphus dumicola Annotation Release 100%27%29%2C %28%27Annotation Version%27%2C %27100%27%29%2C %28%27Annotation Pipeline%27%2C %27NCBI eukaryotic genome annotation pipeline%27%29%2C %28%27Annotation Software Version%27%2C %278.4%27%29%2C %28%27Annotation Method%27%2C %27Best-placed RefSeq%3B Gnomon%27%29%2C %28%27Features Annotated%27%2C %27Gene%3B mRNA%3B CDS%3B ncRNA%27%29%5D%29%29%5D%29;taxonomy=Eukaryota,Metazoa,Ecdysozoa,Arthropoda,Chelicerata,Arachnida,Araneae,Araneomorphae,Entelegynae,Eresoidea,Eresidae,Stegodyphus;topology=linear
```
  
### 2. Compile exe file for windows
```bash
conda activate genbank-gff

# The executable program is located in dist directory.
pyinstaller -F genbank-gff.py
```

