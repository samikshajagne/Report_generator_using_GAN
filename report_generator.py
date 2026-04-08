import pandas as pd

def generate_report(df):
    report = ""

    report += "📊 AUTOMATED DATA REPORT\n"
    report += "---------------------------------\n\n"

    # Basic Info
    report += f"Total Rows: {df.shape[0]}\n"
    report += f"Total Columns: {df.shape[1]}\n\n"

    # Column Summary
    report += "📌 Column Summary:\n"
    for col in df.columns:
        report += f"- {col}: {df[col].dtype}\n"

    report += "\n"

    # Numeric Analysis
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    if len(numeric_cols) > 0:
        report += "📈 Numerical Insights:\n"
        for col in numeric_cols:
            report += f"\n🔹 {col}:\n"
            report += f"  Mean: {df[col].mean():.2f}\n"
            report += f"  Max: {df[col].max()}\n"
            report += f"  Min: {df[col].min()}\n"

    # Categorical Analysis
    categorical_cols = df.select_dtypes(include=['object']).columns

    if len(categorical_cols) > 0:
        report += "\n📊 Categorical Insights:\n"
        for col in categorical_cols:
            top_value = df[col].value_counts().idxmax()
            report += f"\n🔹 {col}:\n"
            report += f"  Most Frequent: {top_value}\n"

    report += "\n✨ Summary:\n"
    report += "The dataset shows meaningful patterns. Numerical features indicate trends, while categorical features highlight dominant groups.\n"

    return report