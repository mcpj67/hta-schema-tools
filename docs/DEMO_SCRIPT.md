# HTA Schema Demo Script

## For Presenting to Health Economists, HTA Agencies, or Funders

### Setup (Before Meeting)
1. Open `hta_viewer.html` in browser
2. Have `example_stroke_thrombolysis.json` ready
3. Have printed copies of technical spec highlights
4. Optional: Have GitHub page open

---

## Part 1: The Problem (2 minutes)

**Opening:**
"How many of you have spent hours recreating someone else's HTA model just to review it? Or struggled to understand an Excel model with hundreds of hidden tabs?"

**Key Pain Points:**
- HTA models are **locked in incompatible tools** (Excel, TreeAge, R)
- **Review burden** is enormous for NICE, CADTH, pharmaceutical companies
- **No reusability** - every model built from scratch
- **Validation is manual** and error-prone
- **Transparency suffers** with proprietary formats

**The Cost:**
- Months wasted on model development
- Weeks spent on peer review
- Errors slip through manual validation
- Knowledge doesn't accumulate across studies

---

## Part 2: The Solution (3 minutes)

**Show the JSON file** (briefly, in text editor):
"This is an HTA model in our standard format - JSON. It's human-readable, machine-validatable, and tool-agnostic."

**Three Core Components:**

### 1. Universal Format (JSON)
- Structured, version-controlled
- Works with any tool
- Human and machine readable

### 2. Validation Tools
**[Open terminal, run validator]**
```bash
python hta_validator.py example_stroke_thrombolysis.json
```
"Instant validation - structural checks, probability constraints, parameter ranges. Takes seconds, not days."

### 3. Computation & Visualization
**[Open hta_viewer.html]**
"But here's the game-changer..."

---

## Part 3: The Demo (5 minutes)

### Step 1: Load the Model
**[Drag JSON file onto viewer]**
"Just drag and drop. No installation, no specialized software."

### Step 2: Show Model Information
**[Scroll through model info section]**
- "Here's the metadata - author, date, clinical area, data sources"
- "All traceable, all documented"
- "This is from the NINDS trial - proper citations included"

### Step 3: Show Results
**[Point to results section]**
- "The engine computes everything automatically"
- "Two strategies: Thrombolysis vs Standard Care"
- "Total costs, total QALYs - properly discounted"
- "ICER calculated: £7,500 per QALY - well below NICE threshold"

**Key Point:** "This isn't just display - it's actually computing. Backward induction through the tree, expected values, discounting, the full analysis."

### Step 4: Show Parameters
**[Scroll through parameter table]**
- "All 31 parameters documented"
- "Sources cited"
- "Types clearly specified"
- "Distributions defined for PSA"

### Step 5: Show Tree Structure
**[Point to node display]**
- "The decision tree structure"
- "Decision nodes, chance nodes, terminal outcomes"
- "All explicitly defined"

---

## Part 4: The Business Case (5 minutes)

### For Academic Researchers
**Benefits:**
- Share models easily with journal submissions
- Reviewers can verify calculations
- Build on others' work
- Version control with Git

**Ask:** "How many models have you built where half the parameters came from a previous study? Imagine just importing that parameter library."

### For HTA Agencies
**Benefits:**
- Standardized submission format
- Automated structural validation
- Easier peer review process
- Transparent, auditable models

**Ask:** "What if NICE submissions came in a standard format? How much review time would that save?"

### For Pharmaceutical Companies
**Benefits:**
- Consistency across therapeutic areas
- Faster model development with component libraries
- Easier collaboration with CROs
- Regulatory confidence

**Ask:** "How many HTA models do you submit per year? What's the cost of development?"

### For Consultancies
**Benefits:**
- Reusable components across projects
- Quality assurance through validation
- Differentiation through standardization
- Faster turnaround times

---

## Part 5: Roadmap & Call to Action (3 minutes)

### What We Have (v0.1)
✓ Schema for decision trees
✓ Validation tools
✓ Computation engine
✓ Web viewer
✓ Example models
✓ Complete documentation

### What's Next (v0.2-1.0)
- **Q1 2025:** Markov models
- **Q2 2025:** Time-to-event, partitioned survival
- **Q3 2025:** Microsimulation
- **Q4 2025:** Value of information (EVPI)

### Alongside:
- R/Python packages for import/export
- Cloud validation API
- Graphical model builder
- Component marketplace

### The Business Model
- **Schema:** Open source (free to implement)
- **Tools:** Freemium SaaS
  - Free: Basic validation, local tools
  - Pro: Cloud execution, collaboration
  - Enterprise: On-premise, custom integrations

---

## Part 6: How to Get Involved (2 minutes)

### For Early Adopters
1. **Try it:** Convert one of your models
2. **Feedback:** What's missing? What would make it useful?
3. **Contribute:** Example models, validation rules, use cases

### For Pilot Partners
- Work with us to test in real projects
- Help shape the roadmap
- Co-author methods paper
- Early access to advanced features

### For Investors/Funders
- Grant applications in progress (Innovate UK, NIHR)
- Seeking seed funding for tool development
- Clear path to revenue through SaaS model
- Growing market: £XXM spent on HTA annually

---

## Handling Common Questions

### Q: "Why would I switch from Excel/TreeAge?"
A: "You don't have to switch completely. We're building import/export tools. But imagine your Excel model being automatically validated, or sharing it with a reviewer who can see it instantly without needing TreeAge."

### Q: "What about proprietary models?"
A: "The schema is just structure. Your parameter values, your clinical assumptions - those remain yours. Think of it like PDF - it's a standard format, but your content is your intellectual property."

### Q: "Who else is using this?"
A: "We're at launch stage. That's why we're talking to you - we want early adopters to shape this. First-mover advantage: you help define the standard."

### Q: "What about existing standards like ADDIS?"
A: "ADDIS focuses on network meta-analysis. We're focused on economic models - decision trees, Markov models, etc. Complementary, not competing."

### Q: "How do you make money if it's open source?"
A: "The schema is open, like HTTP. We make money on the services: cloud validation, graphical builders, component libraries, enterprise support. Like GitHub - Git is free, GitHub services are not."

### Q: "What's your moat?"
A: "Network effects. Once researchers start sharing components and HTA agencies accept submissions in this format, the standard becomes self-reinforcing. Plus first-mover advantage and trademark."

---

## Follow-Up Actions

**Immediately after demo:**
1. Send them the example files
2. Share GitHub link (once created)
3. Get their email for updates
4. Ask: "Would you try converting one model?"

**Within 1 week:**
1. Send technical specification
2. Schedule follow-up call
3. If interested: Propose pilot collaboration
4. Add to mailing list

**Within 1 month:**
1. Send update on any new features/examples
2. Share any academic paper drafts
3. Invite to technical working group

---

## Tailoring the Pitch

### For Technical Audience (Computer Scientists, Programmers)
- Emphasize: JSON Schema validation, API design, computation engine
- Show: Code structure, validation rules, GitHub repo
- Discuss: Tool integrations, SDK development

### For Clinical/Academic Audience (Health Economists)
- Emphasize: Model transparency, parameter documentation, reproducibility
- Show: Example models, parameter tables, citations
- Discuss: Journal submission format, peer review improvements

### For Business Audience (Executives, Funders)
- Emphasize: Market size, efficiency savings, revenue model
- Show: ICER calculations, professional interface
- Discuss: ROI, market adoption strategy, competitive advantages

### For Regulatory Audience (HTA Agencies)
- Emphasize: Standardization, validation, review burden reduction
- Show: Structural validation, parameter checking
- Discuss: Submission requirements, pilot programs

---

## Key Talking Points (Sound Bites)

- "JSON for HTA models - like PDF for documents"
- "Validate in seconds, not days"
- "See the model, verify the math, trust the results"
- "Stop rebuilding, start reusing"
- "Open standard, professional tools"
- "Built by health economists, for health economists"

---

## Success Metrics to Track

After each presentation:
- [ ] Interest level (1-5 scale)
- [ ] Willing to try? (yes/no)
- [ ] Willing to pilot? (yes/no)
- [ ] Key objections raised
- [ ] Suggested features/improvements
- [ ] Follow-up scheduled? (date)

---

**Remember:** The goal isn't to convince everyone immediately. The goal is to find 5-10 early adopters who will test, provide feedback, and help validate the concept. Quality over quantity in the early stage.
