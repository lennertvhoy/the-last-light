# Appendix D: AI Environmental Impact Calculations

## Introduction

The environmental cost of AI is often invisible—hidden in data centers, water treatment facilities, and electricity grids worldwide. This appendix provides detailed calculations and measurements of AI's environmental footprint.

## 1. Energy Consumption Fundamentals

### Computational Requirements

**FLOPS (Floating-Point Operations Per Second)**:
- GPT-3 training: ~3.14 × 10²³ FLOPS
- GPT-4 training: ~2.15 × 10²⁵ FLOPS (estimated)
- Daily ChatGPT inference: ~3.5 × 10²¹ FLOPS

**Energy per Operation**:
Modern GPUs (H100): ~50 GFLOPS/Watt
Therefore: 1 FLOP ≈ 2 × 10⁻¹¹ Joules

### Training Energy Calculations

**GPT-3 Full Training**:
```
Energy = FLOPS / (Efficiency × Utilization)
Energy = 3.14 × 10²³ / (5 × 10¹⁰ × 0.5)
Energy = 1.26 × 10¹³ Joules
Energy = 3,500 MWh
```

**Carbon Emissions**:
```
Emissions = Energy × Grid_Carbon_Intensity
US Average: 0.42 kg CO₂/kWh
Emissions = 3,500 × 0.42 = 1,470 tons CO₂
```

Equivalent to:
- 320 cars driven for one year
- 180 homes' annual energy use
- 1,700 round-trip flights NYC-LA

### Inference Energy Calculations

**Per Query Energy Cost**:
- Average tokens per query: 100 input + 500 output
- Energy per token: ~0.0003 kWh
- Total per query: 0.18 kWh

**Daily Global Inference** (all LLMs):
```
Queries per day: ~10 billion
Energy: 10⁹ × 0.18 = 1.8 GWh/day
Annual: 657 GWh
CO₂: 276,000 tons/year
```

## 2. Water Consumption Analysis

### Direct Cooling Requirements

Data centers use water for cooling through:
1. Evaporative cooling towers
2. Direct chip cooling
3. Humidity control

**Water Usage Effectiveness (WUE)**:
```
WUE = Annual_Water_Use / IT_Equipment_Energy
```

Typical values:
- Best practice: 0.5 L/kWh
- Average: 1.8 L/kWh
- Worst case: 4.0 L/kWh

### AI-Specific Water Consumption

**Training GPT-3**:
```
Water = Energy × WUE
Water = 3,500,000 kWh × 1.8 L/kWh
Water = 6.3 million liters
```

**Per ChatGPT Conversation**:
```
Energy: 0.18 kWh
Water: 0.18 × 1.8 = 324mL
```

A 20-exchange conversation ≈ 6.5 liters

### Regional Water Stress

**Water Stress Index (WSI)** calculation:
```
WSI = Water_Withdrawal / Available_Renewable_Water
```

Data center locations by WSI:
- Virginia (US-East): WSI = 0.15 (Low stress)
- California: WSI = 0.61 (High stress)
- Singapore: WSI = 0.81 (Extreme stress)
- Ireland: WSI = 0.12 (Low stress)

**Effective Water Impact**:
```
Impact = Consumption × (1 + WSI)²
```

Same consumption has 4× impact in California vs. Virginia.

## 3. Hardware Lifecycle Analysis

### Manufacturing Emissions

**NVIDIA H100 GPU**:
- Manufacturing: 314 kg CO₂
- Transportation: 12 kg CO₂
- Total embodied carbon: 326 kg CO₂

**Typical AI Cluster** (1000 GPUs):
- Embodied carbon: 326 tons CO₂
- Operational life: 3 years
- Annual amortized: 109 tons CO₂

### Obsolescence Rates

**Hardware Generations**:
```
Performance(t) = Performance(0) × 2^(t/1.5)
```

Moore's Law for AI accelerators = 18-month doubling

**Economic Obsolescence**:
When: New_Efficiency > Old_Efficiency × (1 + Energy_Cost_Ratio)

Typically occurs at 2.5-3 years for AI hardware.

### E-Waste Generation

**Per H100 GPU**:
- Weight: 3.5 kg
- Recyclable materials: 65%
- Hazardous materials: 15%
- Landfill: 20%

**Global AI Hardware E-Waste** (2024):
```
GPUs retired: ~2 million units
E-waste: 7,000 tons
Hazardous: 1,050 tons
```

## 4. Complete Carbon Footprint Model

### Comprehensive LCA Formula

```
Total_Carbon = Manufacturing + Operation + Cooling + Transmission + Disposal
```

Where:
- Manufacturing: Embodied carbon amortized
- Operation: Direct energy use × grid intensity
- Cooling: PUE factor × operation
- Transmission: Network infrastructure
- Disposal: E-waste processing

### Power Usage Effectiveness (PUE)

**Industry Standards**:
- Google: PUE = 1.10
- Industry average: PUE = 1.58
- Older facilities: PUE = 2.0+

**Cooling Load Calculation**:
```
Cooling_Power = IT_Power × (PUE - 1)
```

### Real-World Example: GPT-4 Lifecycle

**Training Phase**:
- Compute: 25,000 MWh
- Cooling: 10,000 MWh
- Infrastructure: 2,000 MWh
- Total: 37,000 MWh
- CO₂: 15,540 tons

**Annual Inference** (estimated):
- Compute: 200,000 MWh
- Cooling: 80,000 MWh
- Total: 280,000 MWh
- CO₂: 117,600 tons/year

**3-Year Total**:
- Training: 15,540 tons
- Inference: 352,800 tons
- Hardware: 5,000 tons
- Total: 373,340 tons CO₂

## 5. Comparative Analysis

### AI vs. Other Industries

**Annual Carbon Emissions (2024)**:
```
Cryptocurrency: 110 million tons
AI Industry: 80 million tons
Aviation: 1,000 million tons
Steel Production: 3,600 million tons
```

**Growth Rates**:
```
AI: +35% annually
Crypto: -10% annually
Aviation: +3% annually
```

### Per-Unit Comparisons

**Carbon per Operation**:
- Google Search: 0.2g CO₂
- ChatGPT Query: 4.3g CO₂
- Image Generation: 12.1g CO₂
- 1-hour Video Processing: 3.2kg CO₂

## 6. Regional Grid Analysis

### Carbon Intensity by Region

```
Region          | g CO₂/kWh | Main Sources
----------------|-----------|---------------
Iceland         | 28        | Geothermal, Hydro
Norway          | 35        | Hydro
France          | 56        | Nuclear
California      | 240       | Natural Gas, Solar
Virginia (US)   | 420       | Natural Gas, Coal
China           | 580       | Coal
India           | 720       | Coal
```

### Optimal Data Center Placement

**Carbon-Optimal Locations** (considering latency):
1. Quebec, Canada: 30g CO₂/kWh, good connectivity
2. Iceland: 28g CO₂/kWh, limited capacity
3. Norway: 35g CO₂/kWh, expanding capacity

**Water-Optimal Locations**:
1. Ireland: Abundant rainfall, low stress
2. Nordic countries: Cool climate, water availability
3. Pacific Northwest: Hydro power, water access

## 7. Efficiency Improvements and Trends

### Historical Efficiency Gains

**Compute Efficiency** (FLOPS/Watt):
```
2012: 2 GFLOPS/W (Kepler)
2017: 15 GFLOPS/W (Volta)
2022: 50 GFLOPS/W (Hopper)
2024: 65 GFLOPS/W (Projected)
```

**Koomey's Law**: Energy efficiency doubles every 1.57 years

### Model Efficiency Advances

**Parameter Efficiency**:
```
Performance ∝ Parameters^0.35
Energy ∝ Parameters^1.0
```

Result: Larger models are less efficient per parameter but more capable per joule.

**Sparse Models**:
- Dense GPT-3: 175B parameters
- Sparse equivalent: 1.7T parameters, same compute
- Energy reduction: 40%

## 8. Renewable Energy Integration

### Current Renewable Usage

**Major AI Companies** (2024):
- Google: 64% renewable
- Microsoft: 45% renewable
- Amazon: 42% renewable
- Meta: 59% renewable

### Challenges for 24/7 Renewable AI

**Intermittency Problem**:
- Solar: Available 20-30% of time
- Wind: Available 35-45% of time
- AI Training: Requires 95%+ uptime

**Solutions and Costs**:
1. Battery storage: +$0.05/kWh
2. Geographic distribution: +15% latency
3. Demand response: -20% efficiency

## 9. Future Projections

### Business-as-Usual Scenario

```python
def project_emissions(years):
    base_emissions = 80  # million tons CO₂ (2024)
    growth_rate = 0.35   # 35% annual growth
    efficiency_gain = 0.15  # 15% annual improvement
    
    net_growth = growth_rate - efficiency_gain
    
    for year in range(years):
        emissions = base_emissions * (1 + net_growth)**year
        print(f"Year {2024+year}: {emissions:.1f} million tons")
```

Results:
- 2025: 96 million tons
- 2027: 139 million tons
- 2030: 243 million tons

### Intervention Scenarios

**Aggressive Efficiency** (30% annual improvement):
- 2030: 87 million tons (stable)

**Renewable Transition** (100% by 2030):
- 2030: 48 million tons (80% reduction)

**Combined Approach**:
- 2030: 17 million tons (sustainable)

## 10. Mitigation Strategies

### Technical Solutions

1. **Model Compression**:
   - Quantization: 4× reduction, 5% accuracy loss
   - Pruning: 10× reduction, 10% accuracy loss
   - Distillation: 100× reduction, 20% accuracy loss

2. **Efficient Architectures**:
   - Mixture of Experts: 5× efficiency gain
   - Sparse attention: 10× for long sequences
   - Retrieval-augmented: 50× for knowledge tasks

3. **Hardware Optimization**:
   - Optical computing: 100× efficiency (experimental)
   - Neuromorphic chips: 1000× for specific tasks
   - Quantum computing: Unknown but potentially massive

### Policy Recommendations

1. **Carbon Pricing**: $50-100/ton CO₂ would incentivize efficiency
2. **Renewable Requirements**: Mandate 24/7 clean energy
3. **Efficiency Standards**: FLOPS/Watt minimums
4. **Water Use Limits**: WUE < 1.0 in stressed regions
5. **Right to Repair**: Extend hardware lifespan

## 11. Calculation Tools

### Carbon Calculator Formula

```python
def calculate_carbon_footprint(
    model_parameters,
    training_hours,
    queries_per_day,
    hardware_type,
    location,
    lifetime_years
):
    # Training emissions
    flops = model_parameters * 6 * training_data_size
    energy_kwh = flops / (hardware_efficiency * 3.6e12)
    training_carbon = energy_kwh * grid_carbon_intensity[location]
    
    # Inference emissions
    annual_queries = queries_per_day * 365
    inference_energy = annual_queries * energy_per_query
    annual_carbon = inference_energy * grid_carbon_intensity[location]
    
    # Hardware emissions
    hardware_carbon = (num_gpus * embodied_carbon) / lifetime_years
    
    total_annual = (training_carbon / lifetime_years) + 
                   annual_carbon + hardware_carbon
                   
    return total_annual
```

## 12. Key Findings and Recommendations

### Critical Insights

1. **Inference Dominates**: 90% of lifetime emissions from deployment
2. **Location Matters**: 20× difference based on grid carbon
3. **Water Hidden Cost**: Often in stressed regions
4. **Hardware Turnover**: 30% of carbon from manufacturing
5. **Efficiency Gains Insufficient**: Growth outpaces improvements

### Recommendations

**For Developers**:
- Choose carbon-efficient regions
- Implement aggressive model compression
- Monitor and report environmental metrics

**For Organizations**:
- Set carbon budgets for AI projects
- Invest in renewable energy
- Extend hardware replacement cycles

**For Policymakers**:
- Implement carbon pricing
- Mandate environmental reporting
- Support green AI research

**For Users**:
- Be mindful of AI query volume
- Support companies with green practices
- Advocate for sustainable AI

## Conclusion

AI's environmental impact is significant and growing rapidly. Without intervention, AI could consume 3-4% of global electricity by 2030. However, combining technical innovation, renewable energy, and policy action could enable AI advancement while minimizing environmental harm.

The choice is ours, but the window for action is narrowing.

## References

1. Patterson, D. et al. (2021). "Carbon Emissions and Large Neural Network Training"
2. Strubell, E. et al. (2019). "Energy and Policy Considerations for Deep Learning in NLP"
3. IEA (2024). "Data Centres and Data Transmission Networks"
4. Mytton, D. (2021). "Data centre water consumption"
5. Kaack, L.H. et al. (2022). "Aligning artificial intelligence with climate change mitigation"