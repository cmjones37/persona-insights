import pandas as pd
import json
from typing import Dict, List, Union

# --- CONFIGURATION ---
# Define features and roles dynamically (easy to update)
FEATURES = [
    "Shield Mechanics",
    "Aggro Meter Visibility",
    "AoE Healing",
    "Mana Regeneration",
    "Mobility Buffs",
    "Crowd Control",
    "Safe Zones"
]

# High-level role mapping (customizable)
HIGH_LEVEL_ROLE_MAPPING = {
    "Physical Melee": "DPS",
    "Magical Melee": "DPS",
    "Physical Ranged": "DPS",
    "Magical Ranged": "DPS",
    "Tank": "Tank",
    "Healer": "Healer",
    "Hybrid": "Hybrid"
}

# --- LOAD DATA ---
def load_data(filepath: str) -> pd.DataFrame:
    """Load the persona dataset from CSV."""
    return pd.read_csv(filepath)

# --- CLUSTERING ---
def cluster_roles(df: pd.DataFrame) -> Dict[str, Dict[str, int]]:
    """
    Cluster roles at granular and high-level.
    Returns:
        - granular_clusters: Count of each granular role (e.g., {"Tank": 10}).
        - high_level_clusters: Count of each high-level role (e.g., {"DPS": 40}).
    """
    granular_clusters = df["Role"].value_counts().to_dict()

    df["High_Level_Role"] = df["Role"].map(HIGH_LEVEL_ROLE_MAPPING)
    high_level_clusters = df["High_Level_Role"].value_counts().to_dict()

    return granular_clusters, high_level_clusters

# --- PROFILE GENERATION ---
def generate_profiles(df: pd.DataFrame) -> Dict[str, Dict[str, Union[str, List[str]]]]:
    """
    Generate persona profiles for each role.
    Returns:
        Dictionary of profiles, e.g.:
        {
            "Tank": {
                "Key Traits": "High survivability",
                "Common Pain Points": ["Needs reliable healers", "Hates squishy DPS"],
                ...
            }
        }
    """
    profiles = {}
    for role in df["Role"].unique():
        role_data = df[df["Role"] == role]
        profiles[role] = {
            "Key Traits": role_data["Playstyle"].mode()[0],
            "Common Pain Points": role_data["Pain Points"].str.split("; ").explode().mode().tolist(),
            "Goals": role_data["Goals"].str.split("; ").explode().mode().tolist(),
            "Wishes Others Understood": role_data["Wishes Others Understood"].mode()[0],
            "Edge Cases": role_data["Quotes"].sample(1).iloc[0],
            "Weapons": role_data["Weapons"].mode()[0],
            "Preferred Games": role_data["Preferred Games"].mode()[0]
        }
    return profiles

# --- FEATURE PRIORITIZATION MATRIX ---
def generate_feature_matrix(
    df: pd.DataFrame,
    features: List[str] = FEATURES,
    custom_logic: Dict[str, Dict[str, str]] = None
) -> pd.DataFrame:
    """
    Generate a feature prioritization matrix.
    Args:
        df: Input DataFrame.
        features: List of features to include (default: FEATURES).
        custom_logic: Optional custom logic for prioritization (e.g., {"Shield Mechanics": {"Tank": "High"}}).
    Returns:
        DataFrame with features as rows and roles as columns.
    """
    roles = df["Role"].unique()
    matrix = pd.DataFrame(index=features, columns=roles, data="Low")  # Default: Low

    # Apply custom logic if provided
    if custom_logic:
        for feature, role_priorities in custom_logic.items():
            for role, priority in role_priorities.items():
                if feature in matrix.index and role in matrix.columns:
                    matrix.loc[feature, role] = priority

    # Default logic (overridden by custom_logic if provided)
    for feature in features:
        if feature == "Shield Mechanics":
            matrix.loc[feature, "Tank"] = "High"
        elif feature == "AoE Healing":
            matrix.loc[feature, "Healer"] = "High"
        elif feature == "Mana Regeneration":
            matrix.loc[feature, ["Magical Melee", "Magical Ranged", "Healer"]] = "High"
        elif feature == "Mobility Buffs":
            matrix.loc[feature, ["Physical Melee", "Physical Ranged"]] = "High"

    return matrix

# --- SAVE OUTPUTS ---
def save_outputs(
    profiles: Dict[str, Dict[str, Union[str, List[str]]]],
    matrix: pd.DataFrame,
    output_dir: str = "outputs"
) -> None:
    """Save profiles and matrix to files."""
    import os
    os.makedirs(output_dir, exist_ok=True)

    # Save profiles as JSON and Markdown
    with open(f"{output_dir}/persona_profiles.json", "w") as f:
        json.dump(profiles, f, indent=4)

    with open(f"{output_dir}/persona_profiles.md", "w") as f:
        for role, profile in profiles.items():
            f.write(f"### {role}\n")
            for key, value in profile.items():
                f.write(f"**{key}**: {value}\n")
            f.write("\n")

    # Save matrix as CSV and Markdown
    matrix.to_csv(f"{output_dir}/feature_prioritization.csv")
    matrix.to_markdown(f"{output_dir}/feature_prioritization.md")

# --- MAIN ---
def main():
    # Load data
    df = load_data("rpg_persona_data.csv")

    # Cluster roles
    granular, high_level = cluster_roles(df)
    print("Granular Clusters:", granular)
    print("High-Level Clusters:", high_level)

    # Generate profiles
    profiles = generate_profiles(df)
    print("Profiles generated for:", list(profiles.keys()))

    # Generate feature matrix (with default logic)
    matrix = generate_feature_matrix(df)
    print("Feature Matrix:\n", matrix)

    # Save outputs
    save_outputs(profiles, matrix)
    print("Outputs saved to 'outputs/' directory.")

if __name__ == "__main__":
    main()