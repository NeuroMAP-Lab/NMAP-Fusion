# NMAP-Fusion v0.1: PROSPERO-Registered Neuroimaging Meta-Analysis Pipeline  
[![PROSPERO](https://img.shields.io/badge/PROSPERO-CRD420251044665-blue)](https://www.crd.york.ac.uk/PROSPERO/view/CRD420251044665) [![OSF](https://img.shields.io/badge/OSF-Pre–reg-brightgreen)](https://osf.io/p7cjd/) [![Zenodo](https://zenodo.org/badge/DOI/10.5281/zenodo.15330614.svg)](https://doi.org/10.5281/zenodo.15330614)

> *Disclaimer: “NeuroMap Alignment Pipeline” is independent of the Nmap security scanner (nmap.org).*

---

## 📜 Study Overview  
This repository hosts the **pre-implementation** for a PROSPERO-registered protocol (CRD420251044665) to develop an integrated meta-analysis pipeline that:  
1. Unifies coordinate-based (ALE) and image-based (Neurosynth) methods  
2. Incorporates predictive modeling (NeuroQuery)  
3. Adheres to PRISMA for transparency and reproducibility  

> 🔒 **Note**: Full code, data, and docs will be released after protocol approval and manuscript submission.

---

## 🛠️ Current Contents (`config/`)  
- **`preset_categories.yaml`**  
  Behavioral-domain classification template  
- **`stopwords_custom.yaml`**  
  Custom keyword-filtering list  

> ⚠️ _Existing files are never overwritten to preserve reproducibility._

---

## 📋 Planned Methodology  
1. **Data ingestion** from BrainMap Sleuth (MNI coordinates) and Neurosynth (association maps)  
2. **Quality control**: outlier detection, coordinate‐space checks  
3. **Meta-analysis**: ALE + image-based synthesis + predictive modeling  
4. **Reporting**: PRISMA flowcharts, result tables, interactive visualizations  

---

## 📦 Expected Data Sources  
- **BrainMap Sleuth** (v3.0.4) – fMRI studies with MNI coordinates  
- **Neurosynth** – whole-brain decoding association maps  

> Detailed acquisition and preprocessing steps are in Section 3.1 of the PROSPERO protocol.

---

## 📅 Release Plan  
| Stage                | Deliverables                              |
|----------------------|-------------------------------------------|
| **Protocol Approval**| PROSPERO & OSF records                    |
| **Preprint**         | bioRxiv manuscript + non-core scripts     |
| **Manuscript**       | Journal submission                        |
| **Public Release**   | Full pipeline code & documentation (GPL-3.0) |

---

## 📧 Contact  
- **Lead author**: Jiale Chen (ORCID: 0009-0008-3902-9675)  
- **Email**: jlchen7080@gmail.com  
- **Affiliation**: Chengdu University of Traditional Chinese Medicine / NeuroMAP Initiative  
- **GitHub**: https://github.com/NeroMAP/NMAP-Fusion  
