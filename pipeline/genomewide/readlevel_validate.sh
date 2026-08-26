#!/usr/bin/env bash
# Independent read-level confirmation of the two BUB1B alleles, straight from the
# raw FASTQs. Streams each file from the Hub (never stored on disk), decompresses
# on the fly, and counts exact 31-mer matches for the REF and ALT haplotypes on
# both strands. This validates the calls without trusting the supplied VCF.
set -uo pipefail
TOKEN="${HF_TOKEN:?need HF_TOKEN}"
BASE="https://huggingface.co/datasets/SageBio/mva-hackathon-2026-data/resolve/main"
OUT=/home/claude/mva/work/readlevel_counts.tsv
: > "$OUT"
PAT=/home/claude/mva/work/all_patterns.txt
: > "$PAT"
while IFS=$'\t' read -r lbl fwd rev; do echo "$fwd"; echo "$rev"; done < /home/claude/mva/work/kmer_L737X.txt >> "$PAT"
while IFS=$'\t' read -r lbl fwd rev; do echo "$fwd"; echo "$rev"; done < /home/claude/mva/work/kmer_N1002K.txt >> "$PAT"
echo "patterns:"; cat "$PAT"

for f in WGS_EX2312012_HGWCNDSX7_S16_L001_R1_001.fastq.gz \
         WGS_EX2312012_HGWCNDSX7_S16_L001_R2_001.fastq.gz \
         WGS_EX2312012_HGWCNDSX7_S16_L002_R1_001.fastq.gz \
         WGS_EX2312012_HGWCNDSX7_S16_L002_R2_001.fastq.gz \
         WGS_EX2312012_HGWCNDSX7_S16_L003_R1_001.fastq.gz \
         WGS_EX2312012_HGWCNDSX7_S16_L003_R2_001.fastq.gz \
         WGS_EX2312012_HGWCNDSX7_S16_L004_R1_001.fastq.gz \
         WGS_EX2312012_HGWCNDSX7_S16_L004_R2_001.fastq.gz ; do
  echo "[$(date -u +%H:%M:%S)] streaming $f" >> /home/claude/mva/work/readlevel.log
  curl -sSL -H "Authorization: Bearer $TOKEN" "$BASE/$f" \
    | zcat 2>/dev/null \
    | awk 'NR%4==2' \
    | grep -o -F -f "$PAT" \
    | sort | uniq -c | awk -v F="$f" '{print F"\t"$2"\t"$1}' >> "$OUT"
  echo "[$(date -u +%H:%M:%S)] done $f" >> /home/claude/mva/work/readlevel.log
done
echo "ALLDONE" >> /home/claude/mva/work/readlevel.log
