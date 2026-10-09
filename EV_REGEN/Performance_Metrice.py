import matplotlib.pyplot as plt

# Models
models = ['Conventional', 'LR', 'SVR', 'Random Forest', 'Proposed ANN']

# Performance metrics
MAE = [0.086, 0.054, 0.039, 0.031, 0.018]
MSE = [0.0112, 0.0064, 0.0038, 0.0027, 0.0009]
RMSE = [0.106, 0.080, 0.061, 0.052, 0.030]
R2 = [0.82, 0.89, 0.93, 0.95, 0.98]

# Different colours for models
colors = [
    'blue',
    'orange',
    'green',
    'red',
    'purple'
]

# Function to plot metrics
def plot_metric(values, ylabel, title, filename):
    
    plt.figure(figsize=(7,5))
    
    bars = plt.bar(models, values, color=colors)

    # Add values on bars
    for bar, value in zip(bars, values):
        plt.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height(),
            f'{value:.3f}',
            ha='center',
            va='bottom',
            fontsize=9
        )

    plt.xlabel('Prediction Models', fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=13)

    plt.xticks(rotation=30)
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()

    # Save PDF
    plt.savefig(filename,
                format='pdf',
                dpi=300,
                bbox_inches='tight')

    plt.show()


# Generate four graphs

plot_metric(
    MAE,
    'MAE Value',
    'Mean Absolute Error (MAE) Comparison',
    'MAE_Comparison.pdf'
)

plot_metric(
    MSE,
    'MSE Value',
    'Mean Squared Error (MSE) Comparison',
    'MSE_Comparison.pdf'
)

plot_metric(
    RMSE,
    'RMSE Value',
    'Root Mean Squared Error (RMSE) Comparison',
    'RMSE_Comparison.pdf'
)

plot_metric(
    R2,
    'R² Score',
    'Coefficient of Determination (R²) Comparison',
    'R2_Comparison.pdf'
)
