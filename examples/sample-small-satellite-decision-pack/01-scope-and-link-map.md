# 01. Scope and Link Map

## In scope

- SC-01 fictional spacecraft avionics and secure boot
- LINK-01 primary command uplink
- LINK-02 telemetry and mission-data downlink
- GS-01 fictional ground station and mission network
- UPDATE-01 firmware and software update path
- VENDOR-01 radio supplier
- VENDOR-02 ground-network service

## Excluded

Payload science processing is excluded pending owner approval. The exclusion is recorded as unassessed, not Not Applicable.

## Link summary

| Link ID | Direction | Mission function | Authentication | Confidentiality | Owner |
|---|---|---|---|---|---|
| LINK-01 | Ground to spacecraft | Command | Legacy certificate-based control | Limited | Mission operations |
| LINK-02 | Spacecraft to ground | Telemetry and mission data | Legacy signing | Encrypted | Data operations |
