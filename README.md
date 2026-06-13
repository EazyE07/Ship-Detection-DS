
# Ship-Detection-DS
Satellite-based ship detection and monitoring tool for military and logistical classification using YOLOv8.

## Project Overview
This repository introduces the Ship-Detection System, an automated pipeline to process and classify maritime vessels from satellite and aerial imagery. The system bridges high-level logistics tracking with strategic security monitoring by automatically ingesting, filtering, and analyzing unstructured image data.

## The Data-Centric Approach
The core milestone of this project was shifting from model tuning to a Data-Centric AI approach:
* **Version 1 (Baseline):** Suffered from extreme over-granularity with more than 20 specific ship classes, leading to massive label noise and high intra-class confusion.
* **Version 2 (Optimized)**: Built upon structural class consolidation into 3 core classes (`civilian`, `logistics`, `military`) combined with rigorous manual dataset cleaning and bounding box refinement. This dataset optimization stabilized the training process and yielded an optimal performance of 73% mAP.

## Core Features
* **Directory Scanning:** The script scans defined target directories and processes input images autonomously.
* **Negative-Filter Logic:** To maximize efficiency, frames containing only empty ocean water are identified and skipped, saving significant computational capacity during batch inference.
* **Standardized Rendering:** Detections exceeding the confidence threshold are exported with precise bounding boxes and confidence scores.