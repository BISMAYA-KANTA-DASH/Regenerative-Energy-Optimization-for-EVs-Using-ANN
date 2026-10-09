import matplotlib.pyplot as plt

# Feature names
features = [
    'Driving_Speed',
    'Brake_Pressure',
    'SoC',
    'Motor_Torque',
    'Battery_Current',
    'Battery_Temperature',
    'Motor_RPM',
    'Battery_Voltage',
    'Load_Weight',
    'Route_Roughness',
    'Motor_Temperature',
    'Power_Consumption',
    'SoH',
    'Suspension_Load',
    'Tire_Pressure',
    'Tire_Temperature',
    'Ambient_Temperature',
    'Ambient_Humidity',
    'Charge_Cycles',
    'Motor_Vibration',
    'Brake_Pad_Wear',
    'Distance_Traveled',
    'Idle_Time',
    'RUL',
    'Failure_Probability',
    'Maintenance_Type',
    'TTF',
    'Component_Health_Score'
]

# Feature contribution percentages
importance = [
    18.5,
    14.2,
    12.8,
    10.6,
    7.8,
    6.9,
    5.8,
    4.9,
    4.5,
    3.6,
    2.8,
    2.5,
    1.8,
    1.6,
    1.2,
    1.0,
    0.8,
    0.5,
    0.4,
    0.3,
    0.3,
    0.2,
    0.2,
    0.1,
    0.1,
    0.1,
    0.1,
    0.1
]

# Create figure
plt.figure(figsize=(10, 12))

# Horizontal bar plot
bars = plt.barh(features, importance)

# Add percentage values
for bar, value in zip(bars, importance):
    plt.text(value + 0.2,
             bar.get_y() + bar.get_height()/2,
             f'{value}%',
             va='center',
             fontsize=9)

# Labels and title
plt.xlabel('Feature Contribution (%)', fontsize=12)
plt.ylabel('Input Features', fontsize=12)

plt.title('Feature Importance Analysis for Regenerative Braking Efficiency Prediction',
          fontsize=13)

# Arrange highest importance on top
plt.gca().invert_yaxis()

# Grid
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Layout adjustment
plt.tight_layout()

# Save high-resolution image for paper
plt.savefig('Feature_Importance_Reg_Brake_Efficiency.png',
            dpi=300,
            bbox_inches='tight')
plt.savefig('Feature_Importance_Reg_Brake_Efficiency.pdf',
            format='pdf',
            bbox_inches='tight')

# Display plot
plt.show()
# Display
plt.show()
