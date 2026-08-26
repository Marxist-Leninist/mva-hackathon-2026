#!/usr/bin/env python3
"""Extract BUB1B-region candidate variants from the challenge VCF.

Usage: python3 extract_candidates.py /path/to/WGS.vcf.gz
Requires: bcftools. Outputs candidate table with GT/AD/DP/GQ.
No patient data is embedded in this script.
"""
import subprocess, sys
VCF = sys.argv[1]
REGION = '15:40161068-40221122'  # BUB1B, GRCh38, numeric contigs (no chr prefix in this VCF)
out = subprocess.run(['bcftools','view','-H',VCF,REGION],capture_output=True,text=True).stdout
for line in out.splitlines():
    f = line.split('\t')
    fmt = f[8].split(':'); s = dict(zip(fmt, f[9].split(':')))
    print(f[1], f[3]+'>'+f[4], f[6], 'GT='+s.get('GT','.'), 'AD='+s.get('AD','.'), 'DP='+s.get('DP','.'), 'GQ='+s.get('GQ','.'))
