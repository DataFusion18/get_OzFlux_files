#!/usr/bin/env python

"""
Get OzFlux files from dap server.

The processing levels available are:
L3 - quality controlled, post-processed but not gap filled.
L4 - L3 with gap filled meteorology
L5 - L4 with gap filled fluxes
L6 - L5 data with NEE partitioned into GPP and ER

From Peter Isaac:

Within each processing level, there are nominally 2 sets of data called
"default" and "site_pi".  The "default" data set is produced by the OzFlux
Central Node using a default set of processing options for each site while
the "site_pi" data set is intended to offer data processed by the site PIs
using their knowledge of their sites to produce the best quality gap filling
and partitioning.  At this stage, all sites have the "default" data set but
the "site_pi" versions are a work in progress

That's all folks.
"""

__author__ = "Martin De Kauwe"
__version__ = "1.0 (30.05.2018)"
__email__ = "mdekauwe@gmail.com"

import urllib.request
import os
import sys

def main(url_base, level, processing_level):

    output_dir = "data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    sites = ["AdelaideRiver","Calperum","CapeTribulation","CowBay",\
             "CumberlandPlains","DalyPasture","DalyUncleared",\
             "DryRiver","Emerald","Gingin","GreatWesternWoodlands",\
             "HowardSprings","Otway","RedDirtMelonFarm","RiggsCreek",\
             "Samford","SturtPlains","Tumbarumba","Whroo",\
             "WombatStateForest","Yanco"]

    for site in sites:
        url = "%s/%s/%s/%s/%s_%s.nc" % \
                (url_base, site, level, processing_level, site, level)

        # address is missing the "s"
        if site == "CumberlandPlains":
            url = "%s/%s/%s/%s/%s_%s.nc" % \
                    (url_base, "CumberlandPlain", level, processing_level,
                     site, level)

        ofname = "%s/%s_%s.nc" % (output_dir, site, level)
        urllib.request.urlretrieve(url, ofname)

if __name__ == "__main__":

    url_base = "http://dap.ozflux.org.au/thredds/fileServer/ozflux/sites"
    level = "L6"
    processing_level = "default" # "site_pi"
    main(url_base, level, processing_level)
