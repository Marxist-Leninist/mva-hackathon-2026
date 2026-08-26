#!/usr/bin/env python3
"""Report local AlphaFold confidence and predicted contacts around a residue.

The result is hypothesis-generating only. Predicted contacts are not experimental
evidence of folding, binding, or variant pathogenicity.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import dist
from pathlib import Path


def parse_atoms(path: Path):
    atoms = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.startswith("ATOM"):
                continue
            atoms.append(
                {
                    "atom": line[12:16].strip(),
                    "residue": line[17:20].strip(),
                    "number": int(line[22:26]),
                    "xyz": tuple(float(line[a:b]) for a, b in ((30, 38), (38, 46), (46, 54))),
                    "plddt": float(line[60:66]),
                }
            )
    return atoms


def summarize(path: Path, residue_number: int, radius: float):
    atoms = parse_atoms(path)
    target = [atom for atom in atoms if atom["number"] == residue_number]
    if not target:
        raise ValueError(f"residue {residue_number} not found")
    side_chain = [atom for atom in target if atom["atom"] not in {"N", "CA", "C", "O"}]
    contacts = []
    for atom in side_chain:
        for other in atoms:
            if other["number"] == residue_number:
                continue
            distance = dist(atom["xyz"], other["xyz"])
            if distance <= radius:
                contacts.append(
                    {
                        "target_atom": atom["atom"],
                        "other_residue": other["number"],
                        "other_residue_name": other["residue"],
                        "other_atom": other["atom"],
                        "distance_angstrom": round(distance, 3),
                    }
                )
    return {
        "model_file_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "residue_number": residue_number,
        "residue_name": target[0]["residue"],
        "mean_plddt": round(sum(atom["plddt"] for atom in target) / len(target), 2),
        "contact_radius_angstrom": radius,
        "predicted_contacts": sorted(contacts, key=lambda item: item["distance_angstrom"]),
        "interpretation_limit": "AlphaFold geometry is a hypothesis, not functional or clinical evidence.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdb", type=Path)
    parser.add_argument("--residue", type=int, default=1002)
    parser.add_argument("--radius", type=float, default=3.2)
    args = parser.parse_args()
    print(json.dumps(summarize(args.pdb, args.residue, args.radius), indent=2))


if __name__ == "__main__":
    main()

