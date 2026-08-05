# Release Strategy Decision

## Decision

Proceed directly from the historical v0.1.5 release to the corrected documentation-first v0.2.0 release.

## Superseded interim plan

The earlier v0.1.6 containment plan is superseded only because the complete corrected v0.2.0 source and staged release controls are being prepared for immediate execution. If execution is materially delayed or the reviewed baseline changes, the containment plan must be reconsidered.

## Rationale

- The full-engine candidate was withdrawn after adversarial testing identified false-favorable paths.
- The documentation-first v0.2.0 retires the defective public methods without publishing the unsafe engine.
- One controlled pull request preserves history while minimizing public exposure to the known defect.

## Conditions

- Preserve v0.1.5 tag and assets.
- Append, do not replace, the supersession notice.
- Merge only the exact hosted-validated head.
- Complete public read-back and final seal before declaring PASS.
