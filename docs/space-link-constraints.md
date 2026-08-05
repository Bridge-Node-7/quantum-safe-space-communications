# Space-Link and Mission Constraints

Post-quantum migration must be evaluated against the exact algorithm, parameter set, implementation, protocol, mission profile, and hardware in scope.

Record at minimum:

- public-key, ciphertext, and signature sizes;
- frame and packet overhead;
- link rate, contact duration, and retransmission behavior;
- authentication and handshake latency;
- firmware and software-signing package impact;
- processor, memory, power, and thermal limits;
- radiation and fault-tolerance requirements;
- on-orbit updateability and rollback;
- key distribution, trust-anchor update, revocation, and recovery;
- store-and-forward, delayed, intermittent, and disconnected operations;
- vendor support, lifecycle, and interoperability.

Do not rely on a generic claim that a post-quantum algorithm is merely larger or slower. Use current official parameter values and measured mission-specific evidence.
