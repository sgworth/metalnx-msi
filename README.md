![alt text] [1]
[1]: docs/IMAGES/emc_metalnx_logo.png 

Metalnx MSI is a set of microservices designed to work alongside the iRODS ([integrated Rule-Oriented Data System][irods]). It provides tools to enable automatic metadata extraction from a specific file types,
list of all microservices installed in the grid as well as the MSI package version installed in the system.

## Supported file types

* Image files (JPG, JPEG)
* [SAM files][samtools] (SAM, BAM, CRAM)
* Illumina projects (entire Illumina project compressed file)
* [Variant call files][vcf-files] (VCF)

## Documentation

Metalnx has documentation to help with building and using the tool. Please, check the following links for further information.

### Installing Metalnx MSI


The full documentation on how to install Metalnx MSI using `.rpm` and `.deb` packages is available in the [INSTALL](docs/INSTALL.md) document.

### How to build Metalnx MSI packages

Documentation on how to build Metalnx MSI is available in the [BUILD](docs/BUILD.md) file. 

## License

Copyright © 2015-2017 Dell EMC.

This software is provided under the Software license provided in the <a href="LICENSE"> LICENSE </a> file.

[irods]: http://www.irods.org
[samtools]: http://www.htslib.org/
[vcf-files]: http://www.1000genomes.org/wiki/Analysis/vcf4.0
