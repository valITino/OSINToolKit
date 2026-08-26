# Frameworks

Tools find facts. Frameworks tell you what to do with them and when you are done.
Pick one to structure the investigation before you start collecting, so findings
map to a shared model instead of a pile of notes.

## The ones worth knowing

**Cyber Kill Chain (Lockheed Martin).** Seven stages from reconnaissance to
actions-on-objectives. Useful for framing *where* an adversary is in an intrusion
and which artifact you are looking at. Weak on post-exploitation nuance - that is
what ATT&CK is for.

**MITRE ATT&CK.** A matrix of adversary tactics (the "why": Reconnaissance,
Initial Access, Exfiltration, ...) and techniques (the "how"). The lingua franca
for describing behaviour. In OSINT and attribution work, ATT&CK's
**Reconnaissance** and **Resource Development** tactics map directly onto what the
tools in this repo detect and to what a subject may have done to prepare.

**NIST SP 800-61 (Computer Security Incident Handling Guide).** The incident
lifecycle: Preparation; Detection and Analysis; Containment, Eradication and
Recovery; Post-Incident Activity. Use it to keep an investigation disciplined and
to know which phase you are in.

**NIST SP 800-86 (Guide to Integrating Forensic Techniques into Incident
Response).** The forensic process: Collection, Examination, Analysis, Reporting -
and the order-of-volatility guidance that says what to capture first. This is the
backbone for handling evidence defensibly.

## How to use them here

- Frame the case with **NIST 800-61** (what phase) and describe adversary
  behaviour with **ATT&CK** (what tactic/technique).
- Handle any evidence with **800-86** discipline - collect before you analyse,
  preserve order of volatility, document everything.
- Map each tool you run to a stage. If a tool does not advance the investigation
  against the model, you are collecting for its own sake.

## Related

- [../documentation/README.md](../documentation/README.md) - recording it defensibly
- [../opsec/README.md](../opsec/README.md) - not becoming part of your own findings
