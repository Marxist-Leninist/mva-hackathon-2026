.PHONY: check test validate privacy

check: test validate privacy

test:
	python -m unittest discover -s tests -v

validate:
	python scripts/validate_submission.py results/MarxistLeninist_bub1b_compound_het.csv

privacy:
	python scripts/privacy_gate.py .

