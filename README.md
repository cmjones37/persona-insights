# Persona Insights: AI-Powered Persona Analysis for Product Management

---

## **Overview**
This project demonstrates how **AI** can analyse persona data to generate actionable insights for product development. While the example uses **RPG roles as a proxy**, the workflow is **industry-agnostic** and can be adapted for clinical trials, SaaS, or any other domain where persona research is critical.

The goal is to showcase how **AI-assisted tools** can scale persona analysis, reduce manual effort, and provide data-driven insights for prioritising features, identifying edge cases, and drafting documents like PRDs.

[![PRD](https://img.shields.io/badge/docs-PRD-3c4f2c)](./docs/PRD_persona-insights.md)

The thinking behind this project is documented in the [PRD](./docs/PRD_persona-insights.md).

---

## **Workflow**
1. **Survey**: Collect persona data (e.g., pain points, goals, wishes others understood).
2. **Dataset**: Store responses in a structured CSV (e.g., `data/rpg_persona_data.csv`).
3. **AI Analysis**: Use Python to cluster roles, generate profiles, and prioritise features.
4. **Outputs**: Persona profiles, feature prioritisation matrix, and visualisations.

---

## **Files and Structure**
```
persona-insights/
├── data/
│   ├── rpg_persona_data.csv          # Example dataset (RPG roles)
│   └── rpg_persona_survey.md         # Mock survey for data collection
├── scripts/
│   └── persona_analysis.py           # Python script for AI analysis
├── outputs/
│   ├── persona_profiles.md           # AI-generated persona profiles
│   ├── persona_profiles.json
│   ├── feature_prioritization.md     # Feature prioritisation matrix
│   └── feature_prioritization.csv
└── README.md                         # This file
```

---

## **How to Run**
### Prerequisites
- Python 3.8+
- Required libraries: `pandas`, `tabulate`

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/persona-insights.git
   cd persona-insights
   ```

2. Install dependencies:
   ```bash
   pip install pandas tabulate
   ```

3. Run the script:
   ```bash
   python scripts/persona_analysis.py
   ```

4. Review the outputs in the `outputs/` folder.

---
## **Real-World Applications**
The workflow demonstrated here can be adapted to **any industry** by replacing the RPG roles with relevant personas. Examples:

| Industry          | Example Roles                          | Use Case                                                                 |
|-------------------|----------------------------------------|--------------------------------------------------------------------------|
| Clinical Trials   | Monitors, CRCs, PIs, Participants       | Prioritise features like "simplified data entry for CRCs" or "better participant communication tools." |
| SaaS              | Admins, End Users, IT Teams            | Identify conflicts like "Admins want security, but End Users want ease of use." |
| Gaming            | Tanks, Healers, DPS, Hybrid             | Use as-is for game design or community management.                   |
| E-commerce        | Shoppers, Sellers, Admins              | Analyse pain points like "checkout friction" or "inventory management." |

---
## **Key Features**
- **Clustering**: Groups personas at granular (e.g., Physical Melee vs. Magical Melee) and high-level (e.g., DPS vs. Tanks vs. Healers) levels.
- **Profile Generation**: Creates detailed persona profiles with pain points, goals, and "wishes others understood."
- **Feature Prioritisation**: Generates a matrix to rank features by role and impact.
- **Contradiction Detection**: Flags conflicts between personas (e.g., "Tanks want high-risk mechanics, but Healers want safety").

---
## **Future Iterations**
- **Automated Agents** for RAG real-time analysis:
  - Monitor for new survey responses (e.g., via file watchers or webhooks).
  - Automatically run the Python script to update outputs.
  - Notify stakeholders (e.g., via Slack or email) with a summary of changes.
- **Dashboard Integration**: Connect outputs to tools like **Notion**, **Tableau**, or **Google Data Studio** for visualisation.
- **Expanded Data Sources**: Pull persona data from **CRMs**, **support tickets**, or **user interviews** for real-world applications.

---
## **How to Adapt This Tool to Your Industry**
1. **Replace the Dataset**:
   - Swap `rpg_persona_data.csv` with your own persona data (e.g., clinical trial roles).
   - Ensure columns match: `Role`, `Pain Points`, `Goals`, `Wishes Others Understood`, etc.

2. **Customise the Script**:
   - Update the `FEATURES` list in `persona_analysis.py` to reflect your domain (e.g., "Patient Recruitment Tools" for clinical trials).
   - Adjust the `HIGH_LEVEL_ROLE_MAPPING` dictionary to group roles appropriately.

3. **Run the Analysis**:
   ```bash
   python scripts/persona_analysis.py
   ```

---
## **License**
This project is open-source and available under the [MIT License](LICENSE).
