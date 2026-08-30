.PHONY: check test validate privacy competition

PYTHON ?= python3

check: test validate privacy competition

test:
	$(PYTHON) -m unittest discover -s tests -v

validate:
	$(PYTHON) scripts/validate_submission.py results/MarxistLeninist_bub1b_compound_het.csv

privacy:
	$(PYTHON) scripts/privacy_gate.py .

competition:
	$(PYTHON) scripts/validate_competition_manifest.py
