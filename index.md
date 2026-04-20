# Avantika Banerjee — CS 499 Capstone ePortfolio

**Bachelor of Science, Computer Science**
Southern New Hampshire University

---

## Professional Self-Assessment

### Program Reflection

The CS program gave me a lot of chances to revisit the same concepts from different angles, and by the time I got to the capstone most of them had started to feel automatic. CS 250 covered Agile and Scrum, which changed how I think about scope and planning. CS 320 was about writing code other people can test, which is a different problem than writing code that runs. CS 465 put both together in a full-stack MEAN application where every layer had to integrate correctly and the design decisions compounded on each other. Those courses together cover collaboration, stakeholder communication, and the kind of system thinking that makes software actually maintainable.

The more technical work built up the same way. CS 260 is where data structures stopped being abstract and started being something I could use to evaluate tradeoffs. CS 340 is where I started thinking about the database as part of the architecture rather than just something in the back that stores things. Security ran through a lot of the program in smaller pieces before it became explicit, and by the time I was looking at credentials sitting in a notebook that was about to go on a public GitHub repository, the habit of thinking about it was already there.

### Artifact Summary

This portfolio has two artifacts. The first is the CS-340 Grazioso Salvare animal shelter dashboard, a full-stack Python application with a MongoDB backend and a Dash frontend. It covers software design and engineering and databases. The second is the CS-370 deep Q-learning treasure hunt game, a reinforcement learning project where an agent learns to navigate a maze. It covers algorithms and data structures. Together they cover all three capstone categories across two different problem domains.

The dashboard enhancements are about structure and the data layer. The software design work refactored a single Jupyter notebook into a multi-file Python application with separated concerns, environment variable configuration, and proper error handling. The database work added indexes based on the actual query patterns of the application so the database can look up records directly instead of scanning the whole collection on every filter. The game enhancement is a more focused algorithmic decision: replacing a plain list replay buffer with a deque with a fixed maxlen, which makes oldest-episode removal O(1) instead of O(n) and bounds memory across thousands of training epochs. One artifact is about building a system that holds up. The other is about choosing the right tool for a specific problem.

---

## Code Review

[Watch on YouTube](https://youtu.be/A0Q_wQ_efB0)

---

## Artifact 1 — Software Design & Engineering

**CS-340 Animal Shelter Dashboard**

A full-stack dashboard for Grazioso Salvare pulling animal records from MongoDB. Users filter by rescue type and see a data table, breed pie chart, and location map update live.

**Original**
- [ProjectTwoDashboard.ipynb](CS340_Artifact/ProjectTwoDashboard.ipynb)
- [CRUD_Python_Module.py](CS340_Artifact/CRUD_Python_Module.py)

**Enhanced**
- [app.py](cs340_enhanced/app.py)
- [animal_shelter.py](cs340_enhanced/animal_shelter.py)
- [data.py](cs340_enhanced/data.py)
- [layout.py](cs340_enhanced/layout.py)

**Narrative:** [CS 499 Milestone Two Narrative.docx](CS%20499%20Milestone%20Two%20Narrative.docx)

---

## Artifact 2 — Algorithms & Data Structures

**CS-370 Deep Q-Learning Treasure Hunt**

A reinforcement learning application where an AI agent learns to navigate an 8x8 maze using deep Q-learning and a neural network trained over thousands of epochs.

**Original**
- [TreasureHuntGame.ipynb](CS370_Artifact/TreasureHuntGame.ipynb)
- [GameExperience.py](CS370_Artifact/GameExperience.py)
- [TreasureMaze.py](CS370_Artifact/TreasureMaze.py)

**Enhanced**
- [TreasureHuntGame.ipynb](CS370_Artifact_Enhanced/TreasureHuntGame.ipynb)
- [GameExperience.py](CS370_Artifact_Enhanced/GameExperience.py)
- [TreasureMaze.py](CS370_Artifact_Enhanced/TreasureMaze.py)

**Narrative:** [CS 499 Milestone 3 Narrative.docx](CS%20499%20Milestone%203%20Narrative.docx)

---

## Artifact 3 — Databases

**CS-340 Animal Shelter Dashboard — Database Enhancement**

A second pass on the CS-340 dashboard focused on the MongoDB layer: compound indexes on the fields the dashboard queries most and a setup script to enforce this on any deployment.

**Original**
- [CRUD_Python_Module.py](CS340_Artifact/CRUD_Python_Module.py)

**Enhanced**
- [indexes.py](cs340_enhanced/indexes.py)
- [animal_shelter.py](cs340_enhanced/animal_shelter.py)

**Narrative:** [CS 499 Milestone 4 Narrative.docx](CS%20499%20Milestone%204%20Narrative.docx)
