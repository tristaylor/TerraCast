#set the model parameters

# Setting initial means for the distributions of independent variables
temp_mean = [10.0, 25.0]        # Example range in Celsius
moisture_mean = [0.1, 0.5]      # Example range as a fraction (0 to 1)
co2_mean = [400.0, 800.0]       # Example range in ppm
carbon_mean = [0.5, 2.5]        # Example range in % of soil composition
ph_mean = [5.5, 7.5]            # Example pH range
disturbance_level = [0.0, 1.0]  # Example range for disturbance (0: no disturbance, 1: high disturbance)

# Setting possible personalities or types of AMF agents based on environmental adaptability
personalities = ['Generalist', 'Specialist']

# Dependent Variables - could be initialized randomly based on the environment or set based on data
abundance_rate = [-1.0, 1.0]       # Example range for colonization rate (-1: low, 1: high)
uptake_efficiency = [0.0, 1.0]     # Efficiency (0: no uptake, 1: full efficiency)
biomass_mean = [0.1, 5.0]          # Example range in grams per unit soil
grsp_concentration = [0.01, 0.5]   # Example range in % of soil carbon content


