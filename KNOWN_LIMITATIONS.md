# Known Limitations

Quantum Readiness for Space Communications is a documentation-first planning framework.

It does not:

- implement cryptography;
- validate a cryptographic module or product;
- calculate an authoritative score or decision;
- replace mission engineering, safety, legal, contracting, or authorization processes;
- establish the completeness or accuracy of information supplied by an assessor;
- predict when a cryptographically relevant quantum computer will exist;
- prove interoperability, radiation tolerance, side-channel resistance, recovery, or flight suitability;
- make NIST, CISA, NSA/CNSS, IETF, or CCSDS material applicable to every organization.

Assessment quality depends on scope completeness, evidence currency, reviewer competence, accountable ownership, and explicit handling of unknowns and conflicting information.

A posture such as **Ready for Governed Migration** means only that the documented planning package supports the next governed migration step within the stated scope. It is not operational authorization.

## Validation dependency

The validation environment uses an exact PyYAML version and automated weekly dependency review. It does not include a multi-platform hash-locked wheel set. Release validation must install from `requirements-validation.txt`, verify the expected version, and pass `pip check` in hosted Linux and Windows jobs.
