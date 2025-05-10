# NMAP-Fusion v0.2 · NeuroMAP-Lab  
[![PROSPERO](https://img.shields.io/badge/PROSPERO-CRD420251044665-blue)](https://www.crd.york.ac.uk/PROSPERO/view/CRD420251044665)  
[![Zenodo](https://zenodo.org/badge/DOI/10.5281/zenodo.15355619.svg)](https://doi.org/10.5281/zenodo.15355619)  
[![OSF](https://img.shields.io/badge/OSF-Pre--reg-green)](https://osf.io/p7cjd/)

> *Disclaimer: “NeuroMap Alignment Pipeline” is unrelated to the Nmap security scanner (nmap.org).*

---

## 🧠 About This Project  
This is the official implementation repository for the **NeuroMAP-Lab** pipeline, formerly known as *NMAP-Fusion*.  
It operationalizes our PROSPERO-registered protocol (CRD420251044665) and integrates:

1. Coordinate-based meta-analysis (ALE via BrainMap-GinerALE)
2. Image-based synthesis (Neurosynth)

The full method rationale and metadata are available in our [Zenodo archive](https://doi.org/10.5281/zenodo.15355619).

---

## 🛠️ Current Repository Contents (`v0.2`)
- ✅ Year-batched coordinate files from BrainMap Sleuth (1985–1999)
- ✅ Unified merging script for `.txt` exports  
- ✅ Initial directory structure (`data/`, `scripts/`)
- ⚠️ ⚠️ Core analysis modules (e.g., ALE integration) in development

```bash
NMAP-Fusion/
├── data/BrainMap/
│   ├── 1985_1999.txt
│   ├── ...
│   ├── fmir_all.txt
│   └── sleuth_guide.png
├── scripts/
│   └── merge_brainmap_coordinates.py
```

---

## 📋 Methodology Overview
1. **Data ingestion** from BrainMap, Neurosynth, NeuroQuery
2. **Text mining** and category classification
3. **Multi-source evidence quantification**
4. **Voxel-/region-level scoring and visualization**
Full design: NMAP-Fusion_v0.2/2_DATA/BrainMap/README.md (available in our [Zenodo archive](https://doi.org/10.5281/zenodo.15355619))

---

## 🔗 Related Records

- 📄 **PROSPERO Protocol**: [CRD420251044665](https://www.crd.york.ac.uk/PROSPERO/view/CRD420251044665)  
- 📦 **Zenodo Archive**: [v0.2 Release](https://doi.org/10.5281/zenodo.15355619)  
- 🧾 **OSF Pre-registration**: [https://osf.io/p7cjd](https://osf.io/p7cjd)

---

## 🧾 Citation

See 3_DISSEMINATION/Citation.cff by the Zenodo DOI: [10.5281/zenodo.15355619](https://doi.org/10.5281/zenodo.15355619)

---

## 📧 Contact

- **Lead author**: Jiale Chen  
- **Email**: [jlchen7080@gmail.com](mailto:jlchen7080@gmail.com)  
- **GitHub**: [NeuroMAP-Lab](https://github.com/NeuroMAP-Lab)  
- **Affiliation**: Chengdu University of Traditional Chinese Medicine / NeuroMAP-Lab
