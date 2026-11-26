---
name: computer-vision
description: Build and validate computer vision and image-based estimation pipelines.
---

# computer-vision

1. Define target, camera geometry, capture conditions and ground truth. Distinguish classification, detection, segmentation, tracking and regression.
2. Collect consented representative data with documented labels, provenance and train/validation/test splits by subject or capture group to avoid leakage.
3. Start with simple baselines; use OpenCV, PyTorch or suitable pretrained models only after checking license and constraints.
4. Evaluate task-specific metrics, error by subgroup and uncertainty; for physical measurements compare against calibrated real-world ground truth and report units and error.
5. Test lighting, distance, angles and device variation. Do not claim an unvalidated estimate is an accurate measurement.
