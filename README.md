# PyPore
Pypore is a python tool box for fast and accurate quality control, conversion and alignment of nanopore sequencing data, in their raw format (Fast5). We developed PyPore as a command-line tool composed by three modules (`seqstats`, `fastqgen` and `alignment`), each provided with a set of specific options. PyPore comes out with a nice interactive result representation function, based on the plotly library, in order to allow user to zoom and pan the result summary getting information related to a specific experimental point.

## Requirements
- [HDF5](http://www.hdfgroup.org/HDF5/)
- OpenMPI
- python 2.7
  - biopython
  - mpi4py
  - numpy
  - h5py
  - h5py_cache
  - plotly
  - python_dateutil
  - ntpath
  - pysam

#### For Unix/OS X users only 
- [samtools](http://www.htslib.org/download/)  
- [minimap2](https://github.com/lh3/minimap2)
- [BWA](https://sourceforge.net/projects/bio-bwa/files/)
- [ngmlr](https://github.com/philres/ngmlr)

## Installation
#### Dependencies
Before proceeding with PyPore installation, check for HDF5 and OpenMPI dependencies.
1. In order to check if HDF5 library is already present, type:
   ```
   h5cc -showconfig
   ```
1. If you are on **OS X** system equipped with the [HomeBrew](https://brew.sh) package manager, check the available packges list by typing:
    ```
    brew list
    ```
    * If missing, install HDF5 through the HomeBrew Science "tap":
    
       ```
       brew tap homebrew/science
       brew install hdf5
       ```
1. Alternatively, if you use a Python distribution, such as [Anaconda](https://www.anaconda.com) or [Miniconda](https://conda.io/miniconda.html), installation of HDF5 can be done (for all OS) on the command line via:
    ```
    conda install -c anaconda hdf5
    ```
1. For **Linux** or other Unix distributions the HDF5 library can be found in `libhdf5-dev` package. Make sure that you have the development headers, as they are usually not installed by default.
1. For **Windows** users the HDF5 library installer can be downloaded from [here](https://support.hdfgroup.org/HDF5/release/obtain518.html).
1. In order to install the OpenMPI library, refer to the following manuals for [Mac](https://github.com/rsemeraro/PyPore/blob/master/readme_data/MPI_mac.md), [Unix/Unix Like](https://github.com/rsemeraro/PyPore/blob/master/readme_data/OpenMPIUnix.md) and [Windows](https://github.com/rsemeraro/PyPore/blob/master/readme_data/MPI_Win.md) respectively.
#### PyPore
1. Clone the PyPore repository:

    * **Unix** or **OS X**
       ```
       git clone https://github.com/rsemeraro/PyPore
       ```
    * **Windows**
       ```
       git clone --single-branch -b Windows https://github.com/rsemeraro/PyPore.git
       ```
1. Install as root:
    ```
    cd PyPore
    python setup.py install
    ```
 
## Usage
PyPore consists of the following three modules:
- ### seqstats
   `seqstats` provides an interface to explore the information related to a dataset of Fast5 files and to, optionally, convert and gather them in FastQ data. The basic syntax is:
    ```
    python pypore seqstats -i Files/Folder -l sample_label
    ```
    By means of `--fastq/-fq` and `--threads_number/-n` options, it is possible to activate the fastq generation and to use multiple processors to speed up analysis. 
    ```
    python pypore seqstats -i Files/Folder -l sample_label --threads_number 8 --fastq yes
    ```
    To see all options, type:
    ```
    python pypore seqstats -h
    ```
    <p align="center">    
        <b>Interactive Summaries</b>
    </p>
    
    Outputs generated by `seqstats` are:
    ![Alt Text](https://github.com/rsemeraro/PyPore/blob/master/readme_data/Seq_summary.gif)
    _**sequencing_summary.html**_
    ![Alt Text](https://github.com/rsemeraro/PyPore/blob/master/readme_data/pore_map.gif)
    _**pore_activity_map.html**_
- ### fastqgen 
    `fastqgen` is a faster alternative to seqstats, for FastQ generation, allowing user to convert data without wasting time in multiple parsing. The basic syntax is:
    ```
    python pypore fastqgen -i Files/Folder -l sample_label
    ```
    By means of `--threads_number/-n` option, it is possible to use multiple processors to speed up conversion.    
    ```
    python pypore fastqgen -i Files/Folder -l sample_label -n 8
    ```
    To see all options, type:
    ```
    python pypore fastqgen -h
    ```
- ### alignment 
   The last feature of our tool consist of an alignment module based on three state-of-the-art long-read aligners and able to generate an interactive resulting summary. The basic syntax is:
    ```
    python pypore alignment -i input_1.fastq input_2.fastq -r reference.fasta -l sample_label
    ```
    As input you can pass a single or multiple fastq, optionally, it is possible to obtain an HTML summary file, by means of argument `—-alignment_stats/-s`, or/and to customize the aligners list, composed by minimap2(`m`), bwa(`b`) and ngmlr(`n`), removing some of them or editing their execution order `—-aligner/-a`.
    ```
    python pypore alignment -i input_1.fastq -r reference.fasta -l sample_label -a b m n -s yes
    ```
    To see all options, type:
    ```
    python pypore alignment -h
    ```
    <p align="center">    
        <b>Interactive Summary</b>
    </p>
    
    ![Alt Text](https://github.com/rsemeraro/PyPore/blob/master/readme_data/alignment_summary.gif)
    _**alignment_stats.html**_
## Contacts

This program has been developed by Roberto Semeraro, Department of Experimental and Clinical Medicine, University of Florence
