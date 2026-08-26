.PHONY: check test validate privacy

PYTHON ?= python3

check: test validate privacy

test:
	$(PYTHON) -m unittest discover -s tests -v

validate:
	$(PYTHON) scripts/validate_submission.py results/MarxistLeninist_bub1b_compound_het.csv

privacy:
	$(PYTHON) scripts/privacy_gate.py .
