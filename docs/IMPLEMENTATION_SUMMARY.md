# HTA Schema v0.1.1 - Expression Language Implementation Summary

## Overview

This document summarizes the implementation of complex formula support in HTA Schema v0.1.1, addressing the critical need for realistic terminal node calculations in health economic models.

## Problem Identified

The v0.1.0 schema only supported simple parameter references:
```json
"value": {"parameter_ref": "annual_cost_mrs_0_1"}
```

Real HTA models (like the McMeekin 2024 lifetime stroke model) require complex calculations:
- Discounted lifetime costs: `acute_cost + Σ(annual_cost × discount_factor^t)` 
- QALYs: `utility × life_expectancy × discount_factor`
- Conditional logic: `if(age >= 65, elderly_cost, adult_cost)`
- Statistical functions: Using distribution parameters for PSA

## Solution: Expression Language

### Key Features

1. **Backward Compatible**: Old models with `parameter_ref` still work
2. **Powerful**: Supports arithmetic, functions, conditions, statistical distributions
3. **Safe**: No arbitrary code execution, validated parameter references
4. **Standard**: Follows conventions from TreeAge, Excel, R

### Expression Capabilities

#### Arithmetic & Logic
- Operators: `+`, `-`, `*`, `/`, `^`, `%`
- Comparisons: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logic: `and`, `or`, `not`, `if(condition, true, false)`

#### Mathematical Functions
- Basic: `abs`, `sqrt`, `exp`, `log`, `min`, `max`
- Rounding: `ceil`, `floor`, `round`

#### Statistical Functions
- `gamma_mean(shape, scale)`, `gamma_sd(shape, scale)`
- `beta_mean(alpha, beta)`, `beta_sd(alpha, beta)`
- `normal_mean`, `lognormal_mean`, etc.

#### Discounting Functions
- `discount(value, rate, time)` - Single future value
- `discount_stream(annual_value, rate, years)` - Annuity

## Files in v0.1.1 Release

### 1. Updated Schema (`hta_schema_v0.1.1.json`)

**Location:** `hta-schema/schema/hta_schema_v0.1.1.json`

**Key Changes:**
- New `ValueReference` definition with `oneOf`:
  - `{"parameter_ref": "param_id"}` (v0.1.0 compatible)
  - `{"expression": "formula", "description": "optional"}` (NEW)
- Applied to: terminal node costs/utilities, branch probabilities, durations
- New parameter types: `count`, `ratio`

### 2. Expression Language Documentation (`EXPRESSION_LANGUAGE.md`)

**Location:** `hta-schema/specification/EXPRESSION_LANGUAGE.md`

**Contents:**
- Complete syntax specification
- 25+ function reference with examples
- Practical examples from stroke modeling
- Validation requirements
- Implementation guidance

### 3. Example Model (`example_stroke_with_expressions.json`)

**Location:** `hta-schema-tools/examples/example_stroke_with_expressions.json`

**Demonstrates:**
- Complex lifetime cost calculations
- Discounted QALY computation
- Conditional institutional care costs
- McMeekin 2024 stroke model parameters

### 4. Python Validator (`expression_validator.py`)

**Location:** `hta-schema-tools/validator/expression_validator.py`

**Features:**
- Syntax validation
- Parameter reference checking
- Function name validation
- Warning generation

## Practical Example

### Terminal Node with Expressions

```json
{
  "node_type": "terminal",
  "outcomes": {
    "costs": [
      {
        "category": "acute",
        "value": {"parameter_ref": "acute_cost"}
      },
      {
        "category": "lifetime_annual",
        "value": {
          "expression": "discount_stream(annual_cost, discount_rate_costs, life_expectancy)",
          "description": "Discounted present value of annual care costs"
        }
      }
    ],
    "utilities": [
      {
        "value": {
          "expression": "utility * discount_stream(1, discount_rate_outcomes, life_expectancy)",
          "description": "Discounted QALYs"
        }
      }
    ]
  }
}
```

## Migration Guide

### For Existing v0.1.0 Models

No changes required! All v0.1.0 models are valid v0.1.1 models.

### To Add Expressions

1. Change schema_version to `"0.1.1"`
2. Replace parameter references with expressions where needed

**Before:**
```json
{"value": {"parameter_ref": "total_cost"}}
```

**After:**
```json
{
  "value": {
    "expression": "acute_cost + discount_stream(annual_cost, 0.035, life_years)",
    "description": "Total lifetime costs"
  }
}
```

## Next Steps

### Immediate Priorities

1. **Validator Enhancement**
   - Full expression parser
   - Comprehensive tests
   - Type checking

2. **Viewer Update**
   - JavaScript expression evaluator
   - Update computation engine
   - Display calculated values

3. **Test Suite**
   - Create test models
   - Edge case coverage
   - Performance testing

### Future Development

4. **PSA Support**
   - Expressions with distributions
   - Sampling and evaluation

5. **Additional Functions**
   - Gompertz/Weibull survival
   - Custom user functions

6. **Real Model Conversion**
   - Convert published models
   - Validate against results

## Benefits

### For Model Authors
✅ Express realistic lifetime calculations
✅ Self-documenting formulas
✅ Standardized approach

### For Tool Developers
✅ Clear specification
✅ Backward compatible
✅ Extensible architecture

### For Reviewers
✅ Transparent calculations
✅ Verifiable formulas
✅ Traceable dependencies

## Conclusion

The v0.1.1 expression language transforms HTA Schema from a data format to a **true computational model specification**, enabling realistic modeling of lifetime costs and outcomes as demonstrated in the McMeekin 2024 stroke model.

---

**Version:** 0.1.1  
**Date:** December 2024  
**Author:** HTA Schema Development Team
