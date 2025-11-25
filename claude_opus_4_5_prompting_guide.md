# Claude Opus 4.5: Complete Prompting Techniques & Capabilities Guide
## 30+ Techniques with Implementation Details & Sources

**Last Updated:** November 24, 2025  
**Model String:** `claude-opus-4-5-20251101`  
**Pricing:** $5/M input tokens, $25/M output tokens

---

## TABLE OF CONTENTS
1. [Core Instruction Techniques](#1-core-instruction-techniques)
2. [Extended Thinking & Reasoning](#2-extended-thinking--reasoning)
3. [Agentic & Multi-Agent Capabilities](#3-agentic--multi-agent-capabilities)
4. [Tool Use & API Features](#4-tool-use--api-features)
5. [Context Management](#5-context-management)
6. [Output Control & Formatting](#6-output-control--formatting)
7. [Advanced Prompting Frameworks](#7-advanced-prompting-frameworks)
8. [Safety & Alignment](#8-safety--alignment)
9. [Complete Source References](#9-complete-source-references)

---

## 1. CORE INSTRUCTION TECHNIQUES

### TECHNIQUE 1: Explicit Instruction Prompting
Claude 4.5 models are trained for **precise instruction following**. Unlike previous models that exhibited "above and beyond" behavior, Opus 4.5 requires explicit direction.

**Implementation:**
```
❌ "Create a dashboard"
✅ "Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation."
```

**Key Insight:** Add explicit modifiers like "Don't hold back," "Give it your all," "Include thoughtful details like hover states."

📚 Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices

---

### TECHNIQUE 2: Context & Motivation Prompting
Providing **why** behind instructions dramatically improves results.

**Implementation:**
```
"This analytics dashboard will be used by C-level executives to make 
million-dollar decisions. Accuracy and visual clarity are critical because 
errors could lead to significant business losses."
```

📚 Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices

---

### TECHNIQUE 3: XML Tag Structuring
Claude is **specifically fine-tuned** to recognize XML tag structures for organizing complex prompts.

**Implementation:**
```xml
<context>
You are a senior financial analyst reviewing Q3 earnings.
</context>

<task>
Analyze the following report and identify key anomalies.
</task>

<constraints>
- Focus on variance > 10%
- Flag potential fraud indicators
- Output in markdown table format
</constraints>

<input>
{financial_data}
</input>
```

**Best Practices:**
- Use consistent tag names across prompts
- Nest tags for hierarchical content
- Combine with chain-of-thought and few-shot examples

📚 Source: https://simonwillison.net/2025/May/25/claude-4-system-prompt/

---

### TECHNIQUE 4: Role Prompting via System Parameter
Assign specific personas through the system parameter for consistent behavior.

**Implementation:**
```python
client.messages.create(
    model="claude-opus-4-5-20251101",
    system="You are a senior code reviewer with 15 years of experience in 
            security-critical systems. You never approve code that could 
            introduce vulnerabilities.",
    messages=[...]
)
```

📚 Source: https://www.walturn.com/insights/mastering-prompt-engineering-for-claude

---

### TECHNIQUE 5: Few-Shot Example Prompting
Single input-output pairs lock tone and structure better than paragraphs of rules.

**Implementation:**
```
User: "Rewrite: 'Our Q4 profits soared dramatically.'"
Assistant: "We closed Q4 with profits that leapt off the chart."

Now rewrite: "The market experienced significant volatility."
```

📚 Source: https://ai-claude.net/prompts/

---

## 2. EXTENDED THINKING & REASONING

### TECHNIQUE 6: Extended Thinking Mode (API)
Enable deep, step-by-step reasoning for complex tasks.

**Implementation:**
```python
response = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 64000  # Up to 64K thinking tokens
    },
    messages=[{"role": "user", "content": "..."}]
)
```

**Key Parameters:**
- `budget_tokens`: Minimum 1,024; recommended starting point
- Optimal range: 10,000-64,000 for complex reasoning
- Can exceed `max_tokens` when using interleaved thinking with tools

📚 Source: https://docs.claude.com/en/docs/build-with-claude/extended-thinking

---

### TECHNIQUE 7: Interleaved Thinking (Beta)
Think between tool calls for sophisticated multi-step workflows.

**Implementation:**
```python
response = client.beta.messages.create(
    model="claude-opus-4-5-20251101",
    thinking={"type": "enabled", "budget_tokens": 10000},
    tools=[calculator_tool, database_tool],
    betas=["interleaved-thinking-2025-05-14"],
    messages=[...]
)
```

**Capabilities:**
- Reason about tool results before deciding next action
- Chain multiple tool calls with reasoning steps between
- Make nuanced decisions based on intermediate results

📚 Source: https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html

---

### TECHNIQUE 8: Preserved Thinking Blocks (Opus 4.5 Exclusive)
Opus 4.5 introduces **default preservation** of thinking blocks from previous turns.

**Benefits:**
- Cache optimization with tool use
- Token savings in multi-step workflows
- No negative effect on model performance

**Note:** This is default behavior—no code changes required.

📚 Source: https://platform.claude.com/docs/en/build-with-claude/extended-thinking

---

### TECHNIQUE 9: Chain-of-Thought Prompting
Explicitly request step-by-step reasoning within designated tags.

**Implementation:**
```
Solve this problem step by step. 

First, output your reasoning in <thinking></thinking> tags.
Then provide your final answer in <answer></answer> tags.

Problem: [complex problem here]
```

**Results:** Visibility into reasoning slashes logic errors by ~40% (Anthropic internal testing, 2025).

📚 Source: https://ai-claude.net/prompts/

---

### TECHNIQUE 10: Uncertainty Acknowledgment
Add explicit uncertainty handling for improved accuracy.

**Implementation:**
```
"If you are unsure about any calculation or fact, write 'I don't know' 
rather than guessing. This is a high-stakes financial analysis."
```

📚 Source: https://ai-claude.net/prompts/

---

## 3. AGENTIC & MULTI-AGENT CAPABILITIES

### TECHNIQUE 11: Effort Parameter Control (Beta)
Control computational effort across thinking, tool calls, and responses.

**Implementation:**
```python
response = client.messages.create(
    model="claude-opus-4-5-20251101",
    effort="high",  # Options: low, medium, high
    ...
)
```

**Performance Data:**
- Medium effort: Matches Sonnet 4.5 on SWE-bench, uses **76% fewer tokens**
- High effort: Exceeds Sonnet 4.5 by 4.3 percentage points, uses **48% fewer tokens**

📚 Source: https://www.anthropic.com/news/claude-opus-4-5

---

### TECHNIQUE 12: Native Subagent Orchestration
Opus 4.5 recognizes when tasks benefit from subagent delegation **without explicit instruction**.

**Implementation:**
```python
# Ensure well-defined subagent tools are available
subagent_tool = {
    "name": "research_subagent",
    "description": "Delegate research tasks to a specialized agent",
    "input_schema": {...}
}

# Claude will delegate appropriately without explicit prompting
```

**Orchestrator-Worker Pattern:**
- Lead Agent (Opus 4.5): Manages workflow, synthesizes results
- Worker Subagents (typically Sonnet 4.5): Execute specific subtasks
- Each subagent has isolated 200K token context window

📚 Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices

---

### TECHNIQUE 13: Multi-Agent Coordination
Build complex, well-coordinated multi-agent systems.

**Architecture:**
```
┌─────────────────┐
│   Opus 4.5      │  ← Orchestrator
│   Lead Agent    │
└────────┬────────┘
         │
    ┌────┴────┬────────┬────────┐
    ▼         ▼        ▼        ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│Sonnet │ │Sonnet │ │Sonnet │ │Haiku  │
│Worker1│ │Worker2│ │Worker3│ │Worker4│
└───────┘ └───────┘ └───────┘ └───────┘
```

**Best Practices:**
- Use Opus for orchestration (superior reasoning)
- Use Sonnet for workers (cost-efficiency)
- Use Haiku for sub-agents in free-tier products

📚 Source: https://www.cursor-ide.com/blog/claude-subagents

---

### TECHNIQUE 14: Long-Horizon Task Execution
Opus 4.5 can work independently for **hours** while maintaining clarity.

**Prompting for Sustained Work:**
```
"Work on this refactoring task systematically. Make steady advances on 
a few tasks at a time rather than attempting everything at once. 
Provide fact-based progress updates that accurately reflect what has 
been accomplished. You have permission to work for as long as needed."
```

📚 Source: https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-5

---

## 4. TOOL USE & API FEATURES

### TECHNIQUE 15: Parallel Tool Execution
Opus 4.5 fires off multiple tool operations simultaneously.

**Implementation:**
```
"Invoke all relevant tools simultaneously. Execute searches in parallel 
and analyze results as they return."
```

**Steering Aggression:**
```
# For maximum parallelism
"Execute all available tools in parallel without waiting for sequential results."

# For conservative parallelism
"Execute tools one at a time, waiting for each result before proceeding."
```

📚 Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices

---

### TECHNIQUE 16: Tool Search Tool (On-Demand Discovery)
Dynamically discover tools from large libraries without consuming context.

**Implementation:**
```python
{
    "tools": [
        {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
        {
            "name": "github.createPullRequest",
            "description": "Create a pull request",
            "input_schema": {...},
            "defer_loading": True  # Tool discovered on-demand
        }
    ]
}
```

**Performance:**
- Saves ~85% token usage on tool definitions
- Opus 4.5 accuracy improved from 79.5% → 88.1% with Tool Search enabled

📚 Source: https://www.anthropic.com/engineering/advanced-tool-use

---

### TECHNIQUE 17: Memory Tool
Enable persistent storage across conversations.

**Implementation:**
```python
response = client.beta.messages.create(
    model="claude-opus-4-5-20251101",
    tools=[{"type": "memory_20250818", "name": "memory"}],
    betas=["context-management-2025-06-27"],
    messages=[...]
)
```

**Commands:**
- `view`: Read files/directories
- `create`: Create new files
- `update`: Modify existing files
- `delete`: Remove files

📚 Source: https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool

---

### TECHNIQUE 18: Code Execution Tool
Run Python code, create visualizations, analyze data within API calls.

**Use Cases:**
- Data analysis and visualization
- Mathematical computations
- File format conversions
- Statistical analysis

📚 Source: https://claude.com/platform/api

---

### TECHNIQUE 19: Computer Use Enhancement
Opus 4.5 is Anthropic's best model for computer use automation.

**Prompt Injection Resistance:**
- Hardest to trick with prompt injection among frontier models
- Improved significantly over Opus 4.1

📚 Source: https://www.anthropic.com/news/claude-opus-4-5

---

### TECHNIQUE 20: MCP Connector Integration
Connect to remote MCP servers without writing client code.

**Configuration:**
```json
{
    "type": "mcp_toolset",
    "mcp_server_name": "google-drive",
    "default_config": {"defer_loading": true},
    "configs": {
        "search_files": {"defer_loading": false}
    }
}
```

📚 Source: https://www.anthropic.com/engineering/advanced-tool-use

---

## 5. CONTEXT MANAGEMENT

### TECHNIQUE 21: Context Awareness (Token Budget Tracking)
Opus 4.5 receives real-time updates on remaining context window.

**Prompting for Context Management:**
```
"Your context window will be automatically compacted as it approaches 
its limit, allowing you to continue working indefinitely from where 
you left off. Therefore, do not stop tasks early due to token budget 
concerns. As you approach your token budget limit, save your current 
progress and state to memory before the context window refreshes."
```

📚 Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices

---

### TECHNIQUE 22: Context Compaction (Automatic)
Automatically summarize previous messages when approaching limits.

**API Implementation:**
```python
response = client.beta.messages.create(
    model="claude-opus-4-5-20251101",
    betas=["context-management-2025-06-27"],
    context_management={
        "edits": [{
            "type": "clear_tool_uses_20250919",
            "trigger": {"type": "input_tokens", "value": 100000},
            "keep": {"type": "tool_uses", "value": 3}
        }]
    },
    ...
)
```

📚 Source: https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool

---

### TECHNIQUE 23: Fresh Context vs Compaction Strategy
Sometimes starting fresh outperforms compaction.

**Prompting for State Discovery:**
```
"Call pwd; you can only read and write files in this directory."
"Review progress.txt, tests.json, and the git logs."
"Manually run through a fundamental integration test before moving on."
```

**Key Insight:** Opus 4.5 is extremely effective at discovering state from the local filesystem.

📚 Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices

---

### TECHNIQUE 24: Prompt Caching (1-Hour Extended)
Cache prompts for up to one hour (extended from 5 minutes).

**Best For:**
- Extended thinking tasks (often >5 minutes)
- Multi-step workflows
- Repeated similar queries

📚 Source: https://claude.com/platform/api

---

## 6. OUTPUT CONTROL & FORMATTING

### TECHNIQUE 25: Communication Style Adjustment
Opus 4.5 has a more concise, direct communication style by default.

**For More Verbose Output:**
```
"After completing a task that involves tool use, provide a quick summary 
of the work you've done. Explain your reasoning process step by step."
```

**For Maximum Efficiency:**
```
"Skip verbal summaries after tool calls. Jump directly to the next action."
```

📚 Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices

---

### TECHNIQUE 26: Document Creation Excellence
Opus 4.5 produces polished presentations, spreadsheets, and documents.

**Prompting:**
```
"Create a professional presentation on [topic]. Include thoughtful 
design elements, visual hierarchy, and engaging animations where 
appropriate. Apply professional polish and genuine domain awareness."
```

📚 Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices

---

### TECHNIQUE 27: Structured Output Control
Specify exact output formats using format instructions + XML tags.

**Implementation:**
```
"Output your response in the following structure:

<analysis>
[Your detailed analysis here]
</analysis>

<recommendations>
1. [First recommendation]
2. [Second recommendation]
</recommendations>

<confidence>
[Your confidence level: HIGH/MEDIUM/LOW with justification]
</confidence>"
```

📚 Source: https://www.iweaver.ai/blog/claude-4-models-demystified-use-cases-prompt-tricks-and-avoiding-pitfalls/

---

### TECHNIQUE 28: Assistant Prefilling
Pre-fill the assistant response to control output direction.

**API Implementation:**
```python
messages = [
    {"role": "user", "content": "Analyze this code for security issues"},
    {"role": "assistant", "content": "Security Analysis Report:\n\n1."}
]
```

📚 Source: https://www.vellum.ai/blog/prompt-engineering-tips-for-claude

---

## 7. ADVANCED PROMPTING FRAMEWORKS

### TECHNIQUE 29: Agentic Search Optimization
Structure research tasks for maximum effectiveness.

**Implementation:**
```
"Search for this information in a structured way. As you gather data:

1. Develop several competing hypotheses
2. Track confidence levels in progress notes
3. Regularly self-critique your approach and plan
4. Update a hypothesis tree or research notes file
5. Verify information across multiple sources
6. Define clear success criteria for the answer

Break down this complex research task systematically."
```

📚 Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices

---

### TECHNIQUE 30: Prompt Chaining with Self-Review
Chain prompts to have Claude review its own work.

**Implementation Flow:**
```
Step 1: Generate initial output
Step 2: "Review your previous output for accuracy, clarity, and completeness"
Step 3: "Use the feedback to improve the original content"
```

📚 Source: https://www.walturn.com/insights/mastering-prompt-engineering-for-claude

---

### TECHNIQUE 31: ROSES Framework (Opus 4.5 Optimized)
```
Role: "You are a financial advisor bot"
Objective: "Create a retirement plan"
Scenario: "User is 35 with $50K in savings"
Expected Solution: "Savings and investment breakdown"
Steps: "Analyze, calculate, recommend"
```

📚 Source: https://medium.com/@kai.ni/top-12-prompt-engineering-frameworks-you-can-use-with-claude-4-99a3af0e6212

---

### TECHNIQUE 32: Iterative Refinement Protocol
```
Draft → Test on 5 edge cases → Measure tokens/latency/precision → 
Tweak one element → Retest
```

**Result:** Three loops typically lift factual precision from ~80% to 95%.

📚 Source: https://ai-claude.net/prompts/

---

## 8. SAFETY & ALIGNMENT

### TECHNIQUE 33: Prompt Injection Resistance
Opus 4.5 is the most resistant frontier model to prompt injection attacks.

**Best Practices:**
- Model automatically defends against deceptive instructions
- 18.21% success rate on StrongREJECT (vs 31.95% for Sonnet 3.7)
- Computer use scenarios have improved security

📚 Source: https://simonwillison.net/2025/May/25/claude-4-system-prompt/

---

### TECHNIQUE 34: Reduced Misaligned Behaviors
Opus 4.5 shows reduced rates of:
- Sycophancy
- Deception
- Power-seeking
- Encouragement of delusions
- Compliance with harmful system prompts

📚 Source: https://www.anthropic.com/news/claude-sonnet-4-5

---

### TECHNIQUE 35: Reduced Reward Hacking
67% decrease in hard-coding behavior compared to previous models.

**Prompting to Further Reduce:**
```
"Complete this task genuinely. Do not use shortcuts, hard-coded values, 
or loopholes. Show all work and verify each step produces valid results."
```

📚 Source: https://simonwillison.net/2025/May/25/claude-4-system-prompt/

---

## 9. COMPLETE SOURCE REFERENCES

### Official Anthropic Documentation
1. **Claude 4.5 Best Practices:** https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices
2. **Extended Thinking:** https://docs.claude.com/en/docs/build-with-claude/extended-thinking
3. **What's New in Claude 4.5:** https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-5
4. **Memory Tool:** https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool
5. **Subagents:** https://docs.claude.com/en/docs/claude-code/sub-agents
6. **Claude Developer Platform:** https://claude.com/platform/api

### Anthropic Announcements
7. **Introducing Claude Opus 4.5:** https://www.anthropic.com/news/claude-opus-4-5
8. **Introducing Claude Sonnet 4.5:** https://www.anthropic.com/news/claude-sonnet-4-5
9. **Introducing Claude 4:** https://www.anthropic.com/news/claude-4
10. **Advanced Tool Use:** https://www.anthropic.com/engineering/advanced-tool-use
11. **Building Agents with Claude Agent SDK:** https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk
12. **Claude Opus 4.1:** https://www.anthropic.com/claude/opus

### Cloud Provider Documentation
13. **AWS Bedrock Extended Thinking:** https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html
14. **AWS Claude Opus 4.5 Blog:** https://aws.amazon.com/blogs/machine-learning/claude-opus-4-5-now-in-amazon-bedrock/
15. **Microsoft Azure Foundry Opus 4.5:** https://azure.microsoft.com/en-us/blog/introducing-claude-opus-4-5-in-microsoft-foundry/

### Technical Analysis
16. **Simon Willison - Claude 4 System Prompt:** https://simonwillison.net/2025/May/25/claude-4-system-prompt/
17. **PromptHub - Claude 4 System Prompt Analysis:** https://www.prompthub.us/blog/an-analysis-of-the-claude-4-system-prompt
18. **PromptHub - Everything About Claude 4.5:** https://www.prompthub.us/blog/everything-you-need-to-know-about-claude-4-5

### Tutorials & Guides
19. **iWeaver - Claude 4 Mastering Guide:** https://www.iweaver.ai/blog/claude-4-models-demystified-use-cases-prompt-tricks-and-avoiding-pitfalls/
20. **Vellum - 12 Prompt Engineering Tips:** https://www.vellum.ai/blog/prompt-engineering-tips-for-claude
21. **Walturn - Mastering Prompt Engineering:** https://www.walturn.com/insights/mastering-prompt-engineering-for-claude
22. **ai-claude.net - Prompt Engineering for Claude 4:** https://ai-claude.net/prompts/
23. **Medium - Top 12 Frameworks:** https://medium.com/@kai.ni/top-12-prompt-engineering-frameworks-you-can-use-with-claude-4-99a3af0e6212
24. **DataCamp - Claude Agent SDK Tutorial:** https://www.datacamp.com/tutorial/how-to-use-claude-agent-sdk

### Specialized Resources
25. **Skywork - Creative Writing Best Practices:** https://skywork.ai/blog/claude-4-5-best-practices-creative-writing-brainstorming-ideation-2025/
26. **ClaudeLog - Configuration Guide:** https://claudelog.com/configuration/
27. **Cursor IDE - Subagents Guide:** https://www.cursor-ide.com/blog/claude-subagents
28. **Digital Applied - Sonnet 4.5 Complete Guide:** https://www.digitalapplied.com/blog/claude-sonnet-4-5-code-2-agent-sdk-guide
29. **The Neuron - Everything About Claude 4:** https://www.theneuron.ai/explainer-articles/everything-to-know-about-claude-4-sonnet-4-opus-4-from-the-good-to-the-bad-and-the-mid
30. **GitHub - Anthropic Interactive Tutorial:** https://github.com/anthropics/prompt-eng-interactive-tutorial

---

## QUICK REFERENCE: MODEL COMPARISON

| Feature | Opus 4.5 | Sonnet 4.5 | Haiku 4.5 |
|---------|----------|------------|-----------|
| **API String** | claude-opus-4-5-20251101 | claude-sonnet-4-5-20250929 | claude-haiku-4-5-20251001 |
| **Pricing (Input)** | $5/M | $3/M | Lower |
| **Pricing (Output)** | $25/M | $15/M | Lower |
| **Context Window** | 200K | 200K | 200K |
| **Max Output** | 64K | 64K | Variable |
| **Extended Thinking** | ✅ (64K budget) | ✅ (64K budget) | ✅ |
| **Interleaved Thinking** | ✅ | ✅ | ✅ |
| **Preserved Thinking** | ✅ Default | ❌ | ❌ |
| **Effort Parameter** | ✅ | ❌ | ❌ |
| **Best For** | Complex agents, orchestration | Rapid iteration, production | Sub-agents, high volume |

---

## IMPLEMENTATION CHECKLIST

- [ ] Use explicit instructions with modifiers ("go beyond basics", "don't hold back")
- [ ] Structure prompts with XML tags for complex tasks
- [ ] Enable extended thinking for complex reasoning (budget_tokens: 10,000+)
- [ ] Use interleaved thinking beta for tool-heavy workflows
- [ ] Leverage effort parameter for cost/performance optimization
- [ ] Configure context management for long-running tasks
- [ ] Implement Tool Search for large tool libraries
- [ ] Use memory tool for persistent state
- [ ] Apply prompt caching (1-hour extended) for repeated patterns
- [ ] Design subagent tools for delegation-heavy workflows

---

*Generated by Claude Opus 4.5 | Research compiled from 30+ authoritative sources | November 2025*
