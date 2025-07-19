# Appendix F: Algorithmic Bias Technical Deep Dive

## Introduction

Algorithmic bias isn't a bug—it's a feature of how machine learning systems learn from biased data, optimize biased objectives, and operate in biased contexts. This appendix provides technical detail on how bias emerges, amplifies, and resists correction.

## 1. Mathematical Foundations of Bias

### Formal Definition

**Statistical Parity** (Demographic Parity):
```
P(Ŷ = 1 | A = 0) = P(Ŷ = 1 | A = 1)
```
Where Ŷ is the prediction and A is the protected attribute.

**Equalized Odds**:
```
P(Ŷ = 1 | Y = y, A = 0) = P(Ŷ = 1 | Y = y, A = 1) ∀y ∈ {0,1}
```

**Calibration**:
```
P(Y = 1 | Ŷ = p, A = a) = p ∀a,p
```

### The Impossibility Theorem

**Kleinberg et al. (2016)**: Cannot simultaneously satisfy:
1. Calibration
2. Balance for positive class
3. Balance for negative class

Except in trivial cases. This means perfect fairness is mathematically impossible.

### Bias Amplification

**Amplification Factor**:
```
AF = (P(Ŷ = 1 | A = 1) / P(Ŷ = 1 | A = 0)) / (P(Y = 1 | A = 1) / P(Y = 1 | A = 0))
```

Studies show AF > 1.5 is common, meaning ML amplifies existing biases.

## 2. Sources of Algorithmic Bias

### Historical Bias in Training Data

**Example: Hiring Algorithms**

Amazon's 2018 hiring tool:
```python
# Simplified representation
def extract_features(resume):
    features = {
        'years_experience': extract_years(resume),
        'education_level': extract_education(resume),
        'previous_companies': extract_companies(resume),
        'skills': extract_skills(resume),
        # Problem: gendered correlations
        'womens_sports': count_mentions(['womens', 'female']),
        'name_embedding': embed_name(extract_name(resume))
    }
    return features
```

**Data Statistics**:
- Training set: 90% male hires (historical)
- Model learns: male-correlated features → success
- Result: Penalizes "women's chess club" vs "chess club"

### Representation Bias

**Facial Recognition Error Rates**:
```
Dataset Composition:
White Male: 45%
White Female: 35%
Black Male: 10%
Black Female: 5%
Asian Male: 3%
Asian Female: 2%

Error Rates:
White Male: 0.8%
White Female: 7.1%
Black Male: 12.9%
Black Female: 34.7%
```

**Mathematical Relationship**:
```
Error_Rate ∝ 1 / sqrt(Training_Samples)
```

### Measurement Bias

**Healthcare Algorithm (Obermeyer et al., 2019)**:

Algorithm used healthcare costs as proxy for health needs:
```
Health_Need_Proxy = Total_Healthcare_Costs
```

But:
- Black patients: $1,800 less annual healthcare spending
- Same illness severity
- Due to access barriers, not health

Result: Algorithm assigns Black patients 50% lower risk scores.

### Aggregation Bias

**Single Model Problem**:
```python
# One model for all groups
model = train_model(all_data)

# Performance varies by subgroup
for group in demographic_groups:
    subset = data[data.group == group]
    performance[group] = evaluate(model, subset)
    
# Typical result:
# Majority group: 95% accuracy
# Minority group: 75% accuracy
```

### Feedback Loops

**Predictive Policing Example**:
```
1. Historical arrests (biased by over-policing)
   ↓
2. Model predicts high crime areas
   ↓
3. More police deployed to predicted areas
   ↓
4. More arrests in those areas
   ↓
5. Confirms model predictions (self-fulfilling)
   ↓
6. Reinforces bias in next training cycle
```

**Mathematical Model**:
```
Bias(t+1) = Bias(t) × (1 + feedback_strength)
```

Exponential growth without intervention.

## 3. Redundant Encodings

### The Whack-a-Mole Problem

Removing protected attributes doesn't eliminate bias:

**Zip Code → Race Proxy**:
```python
# Correlation analysis
correlation(zip_code, race) = 0.82
correlation(zip_code, income) = 0.74
correlation(income, race) = 0.61

# Even without race variable:
model_without_race still achieves 85% accuracy 
at predicting race from other features
```

### Common Proxies

**Name → Gender/Ethnicity**:
```python
def name_bias_analysis(name):
    # Common patterns
    if name.endswith('sha') or name.endswith('ika'):
        implied_gender = 'female'
        implied_ethnicity_prob = {'african_american': 0.7}
    
    # ML models learn these automatically
    name_embedding = word2vec[name]
    gender_vector = word2vec['man'] - word2vec['woman']
    gender_score = cosine_similarity(name_embedding, gender_vector)
```

**Education → Socioeconomic Status**:
```
P(High_SES | Ivy_League) = 0.73
P(Low_SES | Community_College) = 0.68
```

### Network Effects

**LinkedIn Paradox**:
```python
# Recommendation algorithm
def recommend_candidates(job):
    current_employees = get_employees(job.company)
    networks = get_networks(current_employees)
    
    # Homophily: similar people connect
    # Result: recommends demographically similar candidates
    candidates = rank_by_network_similarity(networks)
    return candidates
```

## 4. Real-World Case Studies

### COMPAS Recidivism Prediction

**Algorithm Claims**: Race-neutral risk assessment

**ProPublica Analysis (2016)**:
```
False Positive Rates (labeled high-risk but didn't reoffend):
Black defendants: 44.9%
White defendants: 23.5%

False Negative Rates (labeled low-risk but did reoffend):
Black defendants: 28.0%
White defendants: 47.7%
```

**Technical Issue**: Optimizing for overall accuracy while groups have different base rates.

### Healthcare Allocation

**Optum Algorithm** (affects 200 million Americans):

```python
# Simplified logic
def assign_care_management(patient):
    # Uses cost as proxy for need
    predicted_cost = model.predict(patient.features)
    
    if predicted_cost > threshold:
        return "extra_care"
    else:
        return "standard_care"

# Result: 
# Black patients need to be sicker to receive same care
# At same risk score:
# Black patients: 26.3% have chronic conditions
# White patients: 17.7% have chronic conditions
```

### Resume Screening

**HireVue's Video Analysis**:
```python
def analyze_candidate_video(video):
    features = {
        'facial_expressions': extract_micro_expressions(video),
        'voice_tone': analyze_prosody(video.audio),
        'word_choice': nlp_analysis(video.transcript),
        'eye_contact': measure_gaze_direction(video)
    }
    
    # Problems:
    # - Cultural differences in expression
    # - Neurodivergent penalization
    # - Lighting bias (darker skin = poor feature extraction)
    
    score = model.predict(features)
    return score
```

## 5. Technical Mitigation Strategies

### Pre-Processing Approaches

**Reweighting**:
```python
def reweight_data(X, y, sensitive_attr):
    # Calculate weights to balance outcomes
    for group in unique(sensitive_attr):
        for outcome in [0, 1]:
            mask = (sensitive_attr == group) & (y == outcome)
            n_group_outcome = sum(mask)
            n_total = len(y)
            
            # Weight inversely proportional to frequency
            weight[mask] = n_total / (n_groups * n_outcomes * n_group_outcome)
    
    return weight
```

**Synthetic Data Generation**:
```python
def generate_fair_synthetic_data(real_data):
    # Learn distribution without protected attributes
    generator = VAE()
    generator.fit(remove_protected_attrs(real_data))
    
    # Generate balanced synthetic data
    synthetic = []
    for group in demographic_groups:
        n_samples = len(real_data) // len(demographic_groups)
        samples = generator.sample(n_samples)
        samples['group'] = group
        synthetic.append(samples)
    
    return concat(synthetic)
```

### In-Processing Approaches

**Fairness Constraints**:
```python
def fair_svm_objective(w, X, y, sensitive_attr, lambda_fairness):
    # Standard SVM loss
    hinge_loss = sum(max(0, 1 - y * (X @ w)))
    
    # Fairness constraint
    group_0_pred = X[sensitive_attr == 0] @ w
    group_1_pred = X[sensitive_attr == 1] @ w
    fairness_loss = (mean(group_0_pred) - mean(group_1_pred))**2
    
    # Combined objective
    return hinge_loss + lambda_fairness * fairness_loss
```

**Adversarial Debiasing**:
```python
class AdversarialDebiasing(nn.Module):
    def __init__(self):
        self.predictor = Predictor()
        self.adversary = Adversary()
    
    def forward(self, X):
        pred = self.predictor(X)
        # Adversary tries to predict protected attribute
        protected_pred = self.adversary(self.predictor.embeddings)
        return pred, protected_pred
    
    def loss(self, pred, y, protected_pred, protected_attr):
        pred_loss = cross_entropy(pred, y)
        # Maximize adversary loss (fool it)
        adv_loss = -cross_entropy(protected_pred, protected_attr)
        return pred_loss + lambda * adv_loss
```

### Post-Processing Approaches

**Threshold Optimization**:
```python
def find_fair_thresholds(scores, labels, groups):
    thresholds = {}
    
    for group in unique(groups):
        group_mask = groups == group
        group_scores = scores[group_mask]
        group_labels = labels[group_mask]
        
        # Find threshold achieving target FPR
        target_fpr = 0.1
        thresholds[group] = find_threshold_for_fpr(
            group_scores, group_labels, target_fpr
        )
    
    return thresholds

def fair_predict(scores, groups, thresholds):
    predictions = zeros_like(scores)
    for group in unique(groups):
        mask = groups == group
        predictions[mask] = scores[mask] > thresholds[group]
    return predictions
```

## 6. Why Debiasing Often Fails

### The Accuracy-Fairness Trade-off

**Pareto Frontier**:
```
Max accuracy achievable = f(fairness_level)

Typical results:
0% fairness constraint → 95% accuracy
50% fairness → 92% accuracy  
90% fairness → 85% accuracy
100% fairness → 75% accuracy (random baseline)
```

### Context Shift

**Training vs. Deployment**:
```python
# Training distribution
P_train(X, Y, A) = Historical data from 2010-2020

# Deployment distribution  
P_deploy(X, Y, A) = Current data from 2024

# Fairness guarantees assume:
P_train = P_deploy

# Reality:
KL_divergence(P_train || P_deploy) > 0.5
```

### Intersectionality

**Multiple Protected Attributes**:
```
Fairness for gender: ✓
Fairness for race: ✓
Fairness for (gender, race) combinations: ✗

Example:
White women: 85% acceptance
Black women: 45% acceptance
Black men: 65% acceptance
White men: 80% acceptance
```

Single-attribute debiasing misses intersectional discrimination.

### Gaming and Adaptation

**Strategic Behavior**:
```python
# Original feature importance
feature_importance = {
    'GPA': 0.4,
    'test_score': 0.3,
    'extracurriculars': 0.2,
    'essay': 0.1
}

# After public disclosure
# Applicants game high-weight features
# Model performance degrades
# Bias returns through new channels
```

## 7. Measurement and Auditing

### Bias Metrics Zoo

```python
def calculate_all_fairness_metrics(y_true, y_pred, sensitive_attr):
    metrics = {}
    
    # Statistical Parity Difference
    metrics['SPD'] = abs(
        mean(y_pred[sensitive_attr == 1]) - 
        mean(y_pred[sensitive_attr == 0])
    )
    
    # Equal Opportunity Difference
    mask_pos = y_true == 1
    metrics['EOD'] = abs(
        mean(y_pred[mask_pos & (sensitive_attr == 1)]) -
        mean(y_pred[mask_pos & (sensitive_attr == 0)])
    )
    
    # Average Odds Difference
    metrics['AOD'] = mean([
        metrics['EOD'],
        abs(mean(y_pred[~mask_pos & (sensitive_attr == 1)]) -
            mean(y_pred[~mask_pos & (sensitive_attr == 0)]))
    ])
    
    # Disparate Impact
    metrics['DI'] = (
        mean(y_pred[sensitive_attr == 1]) /
        mean(y_pred[sensitive_attr == 0])
    )
    
    return metrics
```

### Auditing Framework

```python
class BiasAuditor:
    def __init__(self, model, test_data, sensitive_attrs):
        self.model = model
        self.test_data = test_data
        self.sensitive_attrs = sensitive_attrs
    
    def audit(self):
        results = {}
        
        # Overall performance
        y_pred = self.model.predict(self.test_data.X)
        results['overall_accuracy'] = accuracy(
            self.test_data.y, y_pred
        )
        
        # Per-group performance
        for attr in self.sensitive_attrs:
            results[attr] = {}
            for value in unique(self.test_data[attr]):
                mask = self.test_data[attr] == value
                results[attr][value] = {
                    'accuracy': accuracy(
                        self.test_data.y[mask], 
                        y_pred[mask]
                    ),
                    'n_samples': sum(mask)
                }
        
        # Fairness metrics
        results['fairness'] = calculate_all_fairness_metrics(
            self.test_data.y, y_pred, self.sensitive_attrs
        )
        
        # Intersectional analysis
        results['intersectional'] = self.intersectional_audit()
        
        return results
```

## 8. Legal and Regulatory Landscape

### Disparate Impact Standard

**80% Rule (EEOC)**:
```
Selection_Rate_Minority / Selection_Rate_Majority ≥ 0.8
```

**Technical Challenge**: Which groups to compare?

### GDPR Article 22

**Prohibition on automated decision-making**:
- Right to human intervention
- Right to explanation
- Special protections for sensitive data

**Technical Implications**:
- Must provide meaningful explanations
- Cannot use certain protected attributes
- Must implement human oversight

### Proposed EU AI Act

**High-Risk AI Systems** (includes hiring, credit, justice):
- Mandatory bias testing
- Ongoing monitoring requirements
- Documentation standards
- Human oversight obligations

## 9. Future Directions

### Causal Fairness

**Moving beyond correlation**:
```
Traditional: P(Y|A) = P(Y|A')
Causal: P(Y|do(A)) = P(Y|do(A'))
```

**Causal Graphs**:
```
A → X → Y (indirect discrimination)
A → Y (direct discrimination)
U → A, U → Y (confounding)
```

### Multi-stakeholder Fairness

**Optimization across groups**:
```
maximize Σ_i w_i * utility_i(policy)
subject to fairness_constraints
```

Challenge: Whose weights count?

### Federated Fair Learning

**Training without centralized data**:
```python
def federated_fair_training(clients):
    global_model = initialize_model()
    
    for round in range(n_rounds):
        client_updates = []
        
        for client in clients:
            # Local training with fairness constraints
            local_model = copy(global_model)
            local_model.train(
                client.data, 
                fairness_constraint=client.fairness_requirement
            )
            client_updates.append(local_model - global_model)
        
        # Aggregate with fairness preservation
        global_model += weighted_average(
            client_updates, 
            weights=client_sizes
        )
    
    return global_model
```

## 10. Recommendations

### For Practitioners

1. **Assume Bias Exists**: Test for it, don't hope
2. **Multiple Metrics**: No single fairness metric suffices
3. **Continuous Monitoring**: Bias evolves with data
4. **Stakeholder Involvement**: Include affected communities
5. **Document Everything**: Decisions, trade-offs, limitations

### For Organizations

1. **Bias Impact Assessments**: Before deployment
2. **Red Team Exercises**: Adversarial bias testing
3. **Diverse Teams**: Reduce blind spots
4. **External Audits**: Independent verification
5. **Remediation Processes**: Fix problems found

### For Policymakers

1. **Technical Standards**: Require specific testing
2. **Liability Frameworks**: Clear responsibility
3. **Audit Requirements**: Regular external review
4. **Public Registries**: Transparency in high-stakes AI
5. **Research Funding**: Bias detection and mitigation

## Conclusion

Algorithmic bias is not a simple technical problem with a technical solution. It's a sociotechnical challenge requiring:
- Mathematical innovation
- Social awareness
- Regulatory frameworks
- Continuous vigilance

The tools exist to reduce bias, but perfect fairness is mathematically impossible and socially contested. The goal isn't perfection but continuous improvement and accountability.

## References

1. Barocas, S. et al. (2019). "Fairness and Machine Learning: Limitations and Opportunities"
2. Obermeyer, Z. et al. (2019). "Dissecting racial bias in healthcare algorithm"
3. Kleinberg, J. et al. (2016). "Inherent Trade-Offs in Algorithmic Fairness"
4. Caliskan, A. et al. (2017). "Semantics derived from language corpora contain human-like biases"
5. Mitchell, S. et al. (2021). "Algorithmic Fairness: Choices, Assumptions, and Definitions"