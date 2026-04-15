# Opentrons Protocols

This repository contains a collection of Opentrons OT-2 protocols developed for automated RT-PCR-based workflows, including miRNA detection, HPV primer testing, and serial dilution experiments.

## Overview

Each folder represents a distinct experimental lineage, and within each folder, a single protocol file is updated across commits to reflect its development over time.

## Protocol Categories

- **miRNA RT-PCR**  
  Multi-sample workflows for miRNA detection and amplification.

- **HPV RT-PCR**  
  Protocols for HPV primer testing and proprietary assay development, including a transition from JSON-based definitions to Python-based Opentrons API scripts.

- **Serial Dilution RT-PCR**  
  Protocols for generating and testing dilution series, including multi-primer configurations.

## Repository Structure

```
Opentrons Programs/
├── miRNA rtPCR Project/
│   └── protocol.json
├── HPV rtPCR Project/
│   ├── protocol.json   (early versions)
│   └── protocol.py     (later versions)
├── Serial Dilution rtPCR Test/
│   └── protocol.json
```
