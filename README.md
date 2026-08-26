# 🔥 PyTorch Daily Practice

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?logo=pytorch&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

> Documenting my day-by-day journey through PyTorch — from raw tensors to a trained, saved, and **deployed** deep learning model.

---

## 📖 About This Repository

This repo is a hands-on, learning-in-public log as I go from PyTorch basics to building and deploying a real model. Instead of just watching tutorials, I'm shipping one small, working project per topic and pushing the code daily.

**End goal:** a fully trained model, saved as a checkpoint, and served through a FastAPI `/predict` endpoint.

If you're new to PyTorch too, feel free to follow along, fork this repo, or open an issue if you spot a bug — I'm figuring this out in public, mistakes included.

---

## 🗺️ Learning Roadmap

| # | Topic | What It Covers | Status |
|---|-------|-----------------|--------|
| 1 | Tensors & Core Operations | Creating tensors, shapes, reshaping, broadcasting, core math ops | ✅ Done |
| 2 | Data Pipeline: Dataset & DataLoader | Custom `Dataset` class, `DataLoader`, transforms, batching | ⬜ Upcoming |
| 3 | Building Models with `nn.Module` | Custom models, `nn.Sequential`, common layers | ⬜ Upcoming |
| 4 | Training Loop Essentials | Forward/backward pass, loss functions, optimizers, validation | ⬜ Upcoming |
| 5 | CNNs for Computer Vision | `Conv2d`, pooling, CNN architecture, data augmentation | ⬜ Upcoming |
| 6 | Transfer Learning & Fine-Tuning | Pretrained backbones, freezing layers, fine-tuning strategy | ⬜ Upcoming |
| 7 | GPU Training, Saving & Inference | Device management, `state_dict`, mixed precision, inference | ⬜ Upcoming |
| 8 | Debugging & Best Practices | Common mistakes, reproducibility, performance tuning | ⬜ Upcoming |

*(Flip the ⬜ to ✅ as each topic is completed and pushed.)*

---

## 📂 Repository Structure

```
pytorch-test/
├── day-1/
│   ├── challenge1.py
│   └── challenge2.py
├── 02_data_pipeline_dataset_dataloader/
├── 03_building_models_nn_module/
├── 04_training_loop_essentials/
├── 05_cnn_computer_vision/
├── 06_transfer_learning_finetuning/
├── 07_gpu_training_saving_inference/
├── 08_debugging_best_practices/
├── pyproject.toml
├── uv.lock
└── README.md
```

Each folder contains:
- 📓 A python scripts of that day's mini-project


## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core language |
| PyTorch | Model building & training |
| NumPy / Pandas | Data handling |
| Jupyter Notebook | Experimentation |
| FastAPI | Final model deployment (`/predict` endpoint) |

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/IkkIsuhas/pytorch-test.git
cd pytorch-test

# Set up a virtual environment
uv venv
.venv\Scripts\activate     # on Mac: source venv/bin/activate

# Install dependencies
uv sync

# Launch Jupyter to explore any project folder
uv run jupyter notebook
```

---

## ✅ Progress Tracker

- [x] Day 1 — Tensors & Core Operations
- [x] Day 2 — Data Pipeline: Dataset & DataLoader
- [ ] Day 3 — Building Models with nn.Module
- [ ] Day 4 — Training Loop Essentials
- [ ] Day 5 — CNN Template for Computer Vision
- [ ] Day 6 — Transfer Learning & Fine-Tuning
- [ ] Day 7 — GPU Training, Saving & Inference
- [ ] Day 8 — Debugging & Best Practices
- [ ] Final — Train, save & deploy the model via FastAPI

---

## 🤝 Connect

If you're learning PyTorch too, or want to follow along:

- GitHub: [@IkkIsuhas](https://github.com/IkkIsuhas)
- LinkedIn: [SUHAS](https://linkedin.com/in/suhas-dev)

---

## 📄 License

This project is open-sourced under the [MIT License](LICENSE) — feel free to use it as a template for your own "learning in public" repo.