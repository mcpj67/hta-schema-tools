# HTA Schema Viewer User Guide

## What Is This?

The **HTA Schema Viewer** is a web-based tool that:
- Displays HTA Schema JSON models in a readable format
- **Computes cost-effectiveness results** automatically
- Shows the decision tree structure
- Displays all model parameters
- Calculates ICER (Incremental Cost-Effectiveness Ratio)

**Key feature:** It works entirely in your browser - no server, no installation, no programming required.

## How to Use It

### Step 1: Open the Viewer
1. Download `hta_viewer.html` to your computer
2. Double-click the file (it opens in your web browser)
3. That's it! No installation needed.

### Step 2: Load a Model
1. Drag and drop a `.json` model file onto the upload area
   - OR click the upload area to browse for a file
2. Try it with `example_stroke_thrombolysis.json` first

### Step 3: View Results
The viewer automatically:
- ✓ Validates the model structure
- ✓ Computes costs and QALYs for each strategy
- ✓ Calculates the ICER
- ✓ Shows parameter values and sources
- ✓ Displays the decision tree nodes

## What You'll See

### 1. Model Information
- Model name and description
- Clinical area (e.g., "Acute Ischemic Stroke")
- Healthcare setting (e.g., "UK NHS")
- Currency and reference year

### 2. Cost-Effectiveness Results
For each strategy:
- **Total Cost** (discounted, over time horizon)
- **Total QALYs** (discounted)

Plus overall results:
- **ICER** - Cost per QALY gained
- **Incremental costs and QALYs** between strategies

### 3. Decision Tree Structure
- Visual representation of nodes
- Node types: Decision, Chance, Terminal
- (Simplified view - full interactive tree in future version)

### 4. Parameter Table
- All model parameters
- Types (probability, cost, utility, etc.)
- Base values
- Data sources

## What Gets Computed

The computation engine performs a **deterministic base case analysis**:

1. **Backward induction** through the decision tree
2. **Expected value calculation** at chance nodes (probability × outcome)
3. **Cost accumulation** with proper discounting
4. **QALY calculation** from utilities over the time horizon
5. **ICER computation** for intervention vs baseline

### Discounting
- Uses the discount rates from `analysis_settings.base_case`
- Applied annually using formula: `discount_factor = (1 + rate)^(-year)`
- Standard rates: 3.5% for both costs and QALYs (UK NHS)

### Time Horizon
- Taken from the model's `analysis_settings` or `time_horizon` parameter
- Used for annual cost/utility calculations

## Testing the Viewer

### Quick Test with Example Model
1. Open `hta_viewer.html`
2. Load `example_stroke_thrombolysis.json`
3. You should see:
   - Two strategies: "IV Thrombolysis" and "Standard Care"
   - ICER around £7,000-8,000 per QALY (will vary based on exact parameters)
   - 31 parameters listed
   - 8 nodes shown in tree structure

### Expected Results for Example Model
Based on the stroke thrombolysis example:
- **IV Thrombolysis**: Higher cost (~£15,000-20,000), Higher QALYs (~6-7)
- **Standard Care**: Lower cost (~£12,000-17,000), Lower QALYs (~5-6)
- **ICER**: Should be cost-effective by NICE standards (< £20,000/QALY)

## Sharing with Colleagues

### For Non-Technical Users
Just send them two files:
1. `hta_viewer.html` (the viewer)
2. `example_stroke_thrombolysis.json` (or any model)

Instructions: "Double-click the HTML file, then drag the JSON file onto it"

### For Demonstrations
- Works great for live demos - just drag and drop
- No internet connection required after initial page load
- Results appear instantly
- Professional-looking output suitable for presentations

### For Peer Review
Reviewers can:
- See all parameters and sources
- Verify the computation logic (it's transparent)
- Check the decision tree structure
- Examine cost and utility calculations

## Current Limitations (v0.1)

**What it DOES do:**
✓ Base case deterministic analysis
✓ Discounting with specified rates
✓ ICER calculation
✓ Display all parameters and metadata

**What it DOESN'T do yet (planned for future):**
✗ Probabilistic sensitivity analysis (PSA)
✗ One-way sensitivity analysis
✗ Tornado diagrams
✗ Cost-effectiveness plane
✗ Interactive tree visualization (drag/zoom)
✗ Export results to Excel/CSV
✗ Model editing

## Troubleshooting

### "Invalid JSON file" error
- Check the JSON file is properly formatted
- Validate using `hta_validator.py` first
- Make sure it's HTA Schema v0.1 format

### Results look wrong
- Check parameter values in the JSON file
- Verify probabilities sum to 1.0 for chance nodes
- Check discount rates are reasonable (typically 0.00-0.10)
- Confirm time horizon is sensible

### Browser compatibility
Works in:
- ✓ Chrome / Edge (recommended)
- ✓ Firefox
- ✓ Safari
- ✗ Internet Explorer (not supported)

### File won't load
- Make sure file extension is `.json`
- Try opening the JSON file in a text editor to check it's valid
- File size should be < 5MB

## Advanced: How It Works

### Technology Stack
- **React** - UI framework (loaded from CDN)
- **Pure JavaScript** - Computation engine
- **HTML/CSS** - Layout and styling
- **No server required** - Everything runs in your browser

### Computation Process
```
1. Load JSON model
2. Parse model structure and parameters
3. Start at root decision node
4. For each decision branch:
   a. Follow chance nodes using probabilities
   b. Calculate expected values
   c. Reach terminal nodes
   d. Sum costs (with discounting)
   e. Sum QALYs (with discounting)
5. Compare strategies
6. Calculate incremental costs and QALYs
7. Compute ICER
8. Display results
```

### Code Structure
The viewer contains:
- `HTAComputationEngine` class - Core calculation logic
- `HTAViewer` React component - UI and file handling
- Helper functions for formatting (currency, numbers)

## Extending the Viewer

The HTML file is self-contained and can be modified:
- Edit CSS styles in the `<style>` section
- Modify computation logic in `HTAComputationEngine` class
- Add new features in the React component
- Everything is in one file for easy distribution

## Next Steps

### For Users
1. Try loading your own models
2. Share with colleagues for feedback
3. Report issues or suggestions

### For Developers
1. Add PSA functionality
2. Implement sensitivity analysis visualizations
3. Create interactive tree diagram
4. Add result export features
5. Build model editing capabilities

## Support

For issues or questions:
- Check the technical specification document
- Validate models with `hta_validator.py` first
- Review parameter values for reasonableness
- Ensure model follows HTA Schema v0.1 structure

## Version History

**v0.1** (December 2024)
- Initial release
- Basic deterministic analysis
- ICER calculation
- Parameter display
- Simple tree visualization

---

**Remember:** This viewer demonstrates the power of standardized HTA models. Once a model is in HTA Schema format, anyone can view it, understand it, and verify the calculations - without needing specialized software.
