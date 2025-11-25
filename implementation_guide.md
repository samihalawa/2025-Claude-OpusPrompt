# OPUS 4.5 PROMPT EXPERT - IMPLEMENTATION GUIDE

## Quick Start: How to Use This System Prompt

The system prompt in `opus_4_5_system_prompt.txt` transforms Claude Opus 4.5 into an automatic prompt optimizer. Send ANY prompt to it, and it returns an enhanced, production-ready version.

---

## PYTHON IMPLEMENTATION

```python
import anthropic
import os

# Initialize client
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Load the system prompt
with open("opus_4_5_system_prompt.txt", "r") as f:
    PROMPT_EXPERT_SYSTEM = f.read()

def optimize_prompt(user_prompt: str) -> dict:
    """
    Send any prompt to the Opus 4.5 Prompt Expert.
    Returns XML-formatted optimization with:
    - Analysis
    - API configuration recommendations  
    - Enhanced prompt (ready to use)
    - Techniques applied
    - Usage notes
    """
    
    response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=16000,
        system=PROMPT_EXPERT_SYSTEM,
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )
    
    return response.content[0].text

# Example usage
if __name__ == "__main__":
    # Example 1: Simple prompt
    original_prompt = "Write code to parse JSON files"
    
    optimized = optimize_prompt(original_prompt)
    print("=" * 80)
    print("OPTIMIZED PROMPT:")
    print("=" * 80)
    print(optimized)
    
    # Example 2: Complex agentic workflow
    original_prompt = """
    Build an agent that monitors GitHub repos for security vulnerabilities,
    creates reports, and notifies the team
    """
    
    optimized = optimize_prompt(original_prompt)
    print("\n" + "=" * 80)
    print("OPTIMIZED AGENTIC PROMPT:")
    print("=" * 80)
    print(optimized)
```

---

## CURL IMPLEMENTATION

```bash
#!/bin/bash

# Save system prompt to variable
SYSTEM_PROMPT=$(cat opus_4_5_system_prompt.txt)

# Your prompt to optimize
USER_PROMPT="Research the latest developments in quantum computing and their business applications"

# Call API
curl https://api.anthropic.com/v1/messages \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --header "content-type: application/json" \
  --data @- <<EOF
{
  "model": "claude-opus-4-5-20251101",
  "max_tokens": 16000,
  "system": "$SYSTEM_PROMPT",
  "messages": [
    {
      "role": "user",
      "content": "$USER_PROMPT"
    }
  ]
}
EOF
```

---

## WORKFLOW: USING THE ENHANCED PROMPTS

### Step 1: Get Optimized Prompt
```python
# Send your original prompt to the expert
optimized_output = optimize_prompt("Build a data pipeline for customer analytics")
```

### Step 2: Parse the XML Response
```python
import xml.etree.ElementTree as ET

root = ET.fromstring(optimized_output)

# Extract the enhanced prompt
enhanced_prompt = root.find(".//enhanced_prompt").text

# Extract API configuration
model = root.find(".//model").text
max_tokens = root.find(".//max_tokens").text
thinking_enabled = root.find(".//thinking/enabled").text == "true"
thinking_budget = root.find(".//thinking/budget_tokens").text if thinking_enabled else None
effort = root.find(".//effort").text

# Extract beta features
beta_features = [b.text for b in root.findall(".//beta_features/*")]

# Extract recommended tools
tools = [t.text for t in root.findall(".//recommended_tools/*")]
```

### Step 3: Execute the Enhanced Prompt
```python
# Build API call based on recommendations
api_params = {
    "model": model,
    "max_tokens": int(max_tokens),
    "messages": [{"role": "user", "content": enhanced_prompt}]
}

# Add thinking if recommended
if thinking_enabled:
    api_params["thinking"] = {
        "type": "enabled",
        "budget_tokens": int(thinking_budget)
    }

# Add effort if recommended
if effort and effort != "none":
    api_params["effort"] = effort

# Add beta features
if beta_features:
    api_params["betas"] = beta_features

# Execute with optimized configuration
response = client.messages.create(**api_params)
print(response.content[0].text)
```

---

## COMPLETE END-TO-END EXAMPLE

```python
import anthropic
import os
import xml.etree.ElementTree as ET

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Load the Prompt Expert system
with open("opus_4_5_system_prompt.txt", "r") as f:
    PROMPT_EXPERT = f.read()

def get_optimized_prompt(original_prompt: str):
    """Step 1: Get optimization from the expert"""
    response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=16000,
        system=PROMPT_EXPERT,
        messages=[{"role": "user", "content": original_prompt}]
    )
    return response.content[0].text

def parse_optimization(xml_output: str):
    """Step 2: Parse the XML response"""
    root = ET.fromstring(xml_output)
    
    return {
        "enhanced_prompt": root.find(".//enhanced_prompt").text.strip(),
        "model": root.find(".//model").text,
        "max_tokens": int(root.find(".//max_tokens").text),
        "thinking_enabled": root.find(".//thinking/enabled").text == "true",
        "thinking_budget": int(root.find(".//thinking/budget_tokens").text) if root.find(".//thinking/budget_tokens") is not None else None,
        "effort": root.find(".//effort").text,
        "betas": [b.text for b in root.findall(".//beta_features/*") if b.text],
        "tools": [t.text for t in root.findall(".//recommended_tools/*") if t.text],
        "techniques": [t.text for t in root.findall(".//techniques_applied/*") if t.text],
        "usage_notes": root.find(".//usage_notes").text.strip() if root.find(".//usage_notes") is not None else ""
    }

def execute_optimized(config: dict):
    """Step 3: Execute with optimized configuration"""
    params = {
        "model": config["model"],
        "max_tokens": config["max_tokens"],
        "messages": [{"role": "user", "content": config["enhanced_prompt"]}]
    }
    
    if config["thinking_enabled"]:
        params["thinking"] = {
            "type": "enabled",
            "budget_tokens": config["thinking_budget"]
        }
    
    if config["effort"] and config["effort"] != "none":
        params["effort"] = config["effort"]
    
    if config["betas"]:
        params["betas"] = config["betas"]
    
    response = client.messages.create(**params)
    return response.content[0].text

# USAGE
if __name__ == "__main__":
    # Your original prompt
    my_prompt = """
    Create a Python script that analyzes CSV files for anomalies,
    generates visualizations, and outputs a report
    """
    
    print("🔍 STEP 1: Getting optimization...")
    optimization_xml = get_optimized_prompt(my_prompt)
    
    print("\n📋 STEP 2: Parsing configuration...")
    config = parse_optimization(optimization_xml)
    
    print(f"\n✨ Techniques Applied: {len(config['techniques'])}")
    for t in config['techniques']:
        print(f"   - {t}")
    
    print(f"\n⚙️  Configuration:")
    print(f"   Model: {config['model']}")
    print(f"   Thinking: {config['thinking_enabled']} (Budget: {config['thinking_budget']})")
    print(f"   Effort: {config['effort']}")
    print(f"   Beta Features: {config['betas']}")
    
    print(f"\n📝 Enhanced Prompt Preview:")
    print(config['enhanced_prompt'][:500] + "...")
    
    print("\n🚀 STEP 3: Executing optimized prompt...")
    result = execute_optimized(config)
    
    print("\n✅ RESULT:")
    print("=" * 80)
    print(result)
```

---

## NODEJS/TYPESCRIPT IMPLEMENTATION

```typescript
import Anthropic from '@anthropic-ai/sdk';
import * as fs from 'fs';
import * as xml2js from 'xml2js';

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

// Load system prompt
const PROMPT_EXPERT = fs.readFileSync('opus_4_5_system_prompt.txt', 'utf8');

async function optimizePrompt(userPrompt: string): Promise<string> {
  const response = await client.messages.create({
    model: 'claude-opus-4-5-20251101',
    max_tokens: 16000,
    system: PROMPT_EXPERT,
    messages: [
      { role: 'user', content: userPrompt }
    ]
  });
  
  return response.content[0].text;
}

async function parseOptimization(xmlOutput: string): Promise<any> {
  const parser = new xml2js.Parser();
  const result = await parser.parseStringPromise(xmlOutput);
  
  return {
    enhancedPrompt: result.prompt_optimization.enhanced_prompt[0],
    model: result.prompt_optimization.api_configuration[0].model[0],
    maxTokens: parseInt(result.prompt_optimization.api_configuration[0].max_tokens[0]),
    thinkingEnabled: result.prompt_optimization.api_configuration[0].thinking[0].enabled[0] === 'true',
    thinkingBudget: result.prompt_optimization.api_configuration[0].thinking[0].budget_tokens?.[0],
    effort: result.prompt_optimization.api_configuration[0].effort[0],
    betas: result.prompt_optimization.api_configuration[0].beta_features?.[0] || [],
  };
}

async function executeOptimized(config: any): Promise<string> {
  const params: any = {
    model: config.model,
    max_tokens: config.maxTokens,
    messages: [{ role: 'user', content: config.enhancedPrompt }]
  };
  
  if (config.thinkingEnabled) {
    params.thinking = {
      type: 'enabled',
      budget_tokens: parseInt(config.thinkingBudget)
    };
  }
  
  if (config.effort && config.effort !== 'none') {
    params.effort = config.effort;
  }
  
  if (config.betas && config.betas.length > 0) {
    params.betas = config.betas;
  }
  
  const response = await client.messages.create(params);
  return response.content[0].text;
}

// Usage
(async () => {
  const myPrompt = "Build an API that processes user uploads and stores them in S3";
  
  console.log("🔍 Optimizing prompt...");
  const optimizationXml = await optimizePrompt(myPrompt);
  
  console.log("📋 Parsing configuration...");
  const config = await parseOptimization(optimizationXml);
  
  console.log("🚀 Executing optimized prompt...");
  const result = await executeOptimized(config);
  
  console.log("✅ Result:", result);
})();
```

---

## COST OPTIMIZATION STRATEGIES

### Strategy 1: Use Effort Parameter
```python
# For most tasks, medium effort provides 76% token savings
# while maintaining Sonnet 4.5-level performance

config["effort"] = "medium"  # Recommended default
```

### Strategy 2: Start with Lower Thinking Budgets
```python
# Start at 10K, increase if needed
thinking_budget = 10000  # vs 64000 max

# The expert will recommend budget based on complexity
```

### Strategy 3: Batch Similar Prompts
```python
# Optimize once, reuse for similar tasks
optimized_research_template = optimize_prompt("Research [TOPIC]")
# Replace [TOPIC] with specific queries
```

---

## TROUBLESHOOTING

**Issue:** XML parsing errors
**Solution:** Ensure you're capturing the full response text. The expert always outputs valid XML.

**Issue:** "Thinking not supported" error
**Solution:** Verify you're using `claude-opus-4-5-20251101` (not Sonnet or Haiku).

**Issue:** Expert executes the prompt instead of optimizing
**Solution:** Check system prompt is loaded correctly. The expert should NEVER execute, only optimize.

**Issue:** Enhanced prompts are too verbose
**Solution:** This is intentional for Opus 4.5. The model handles complexity well.

---

## PRODUCTION TIPS

1. **Cache the system prompt**: It's 6K+ tokens. Use 1-hour prompt caching.
2. **Store optimized prompts**: Build a library of enhanced templates.
3. **A/B test configurations**: Compare effort=medium vs effort=high for your use case.
4. **Monitor token usage**: Track savings from the expert's recommendations.
5. **Update regularly**: As Anthropic releases new features, update the system prompt.

---

## EXAMPLE OUTPUT FROM THE EXPERT

When you send: "Analyze customer churn data"

You get back:
```xml
<prompt_optimization>
  <analysis>
    <complexity_level>Medium</complexity_level>
    <task_type>Data Analysis</task_type>
    <estimated_tokens>15000</estimated_tokens>
    <key_challenges>
      - Requires statistical reasoning
      - May need visualization recommendations
      - Should identify actionable insights
    </key_challenges>
  </analysis>

  <api_configuration>
    <model>claude-opus-4-5-20251101</model>
    <max_tokens>8000</max_tokens>
    <thinking>
      <enabled>true</enabled>
      <budget_tokens>10000</budget_tokens>
    </thinking>
    <effort>medium</effort>
    <beta_features></beta_features>
    <recommended_tools>code_execution</recommended_tools>
  </api_configuration>

  <enhanced_prompt>
<context>
You are a senior data scientist specializing in customer analytics and churn prediction.
Your analysis will inform executive decisions on retention strategy.
</context>

<task>
Analyze the provided customer churn dataset to identify patterns, risk factors, 
and actionable insights for reducing churn.
</task>

<methodology>
1. Data exploration and quality assessment
2. Statistical analysis of churn correlates
3. Segment identification (high-risk cohorts)
4. Causal factor analysis
5. Actionable recommendations with expected impact

Think step-by-step in <thinking> tags, then provide final analysis in <answer> tags.
</methodology>

<constraints>
- Focus on statistically significant findings (p < 0.05)
- Prioritize actionable insights over theoretical explanations
- If data quality issues exist, flag them explicitly
- Include confidence levels for each recommendation
</constraints>

<output_format>
Provide analysis in markdown with:
1. Executive Summary (3-5 key findings)
2. Detailed Analysis by Factor
3. Customer Segments at Risk
4. Recommended Actions (prioritized by impact)
5. Expected Outcomes (quantified where possible)
</output_format>

<input>
{customer_churn_data}
</input>
  </enhanced_prompt>

  <techniques_applied>
    1. Explicit instruction enhancement - Added specific analysis steps
    2. XML structure - Organized complex requirements
    3. Role definition - Senior data scientist with domain expertise
    4. Context/motivation - Executive decision context increases quality
    5. Extended thinking - Enabled for statistical reasoning
    6. Output format specification - Structured markdown with sections
    7. Constraint enforcement - Made quality thresholds explicit
    8. Uncertainty handling - Added confidence level requirements
    9. Effort parameter - Recommended medium for 76% token savings
  </techniques_applied>

  <usage_notes>
    - Effort=medium provides optimal cost/performance for this task
    - Extended thinking helps with statistical reasoning and causal analysis
    - Consider adding code_execution tool if you want Claude to generate 
      visualizations directly
    - For very large datasets (>100K rows), consider preprocessing or 
      providing summary statistics
  </usage_notes>
</prompt_optimization>
```

---

## NEXT STEPS

1. **Copy `opus_4_5_system_prompt.txt` to your project**
2. **Run the Python example** to see it in action
3. **Start with simple prompts**, observe enhancements
4. **Build a library** of optimized templates for your common tasks
5. **Share with your team** - Everyone gets Opus 4.5 optimization

---

*Generated for AutoClient.ai optimization workflows | November 2025*
