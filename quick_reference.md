# OPUS 4.5 PROMPT TECHNIQUES - QUICK REFERENCE CARD

## 35 Techniques Encoded in the System Prompt

### CORE PATTERNS (Always Apply)
1. **Explicit Instructions** - Use directive language with modifiers like "Don't hold back"
2. **XML Structure** - Wrap in `<context>`, `<task>`, `<constraints>`, `<output_format>`
3. **Role Definition** - "You are a [senior/expert] [role] with [credentials]..."
4. **Context/Motivation** - Explain WHY the task matters
5. **Output Format Spec** - Define exact structure (markdown, JSON, prose, etc.)

### REASONING & THINKING (Medium/Complex Tasks)
6. **Extended Thinking** - Enable with budget_tokens: 10000-64000
7. **Interleaved Thinking** - Beta: Think between tool calls
8. **Preserved Thinking** - Opus 4.5 exclusive: Previous thinking stays in context
9. **Chain-of-Thought** - Request `<thinking>` then `<answer>` tags
10. **Uncertainty Acknowledgment** - "If unsure, say 'I don't know'"

### AGENTIC CAPABILITIES (Complex Workflows)
11. **Effort Parameter** - LOW/MEDIUM (76% savings)/HIGH (48% savings vs Sonnet)
12. **Native Subagent Orchestration** - Auto-delegates without prompting
13. **Multi-Agent Coordination** - Orchestrator + worker pattern
14. **Long-Horizon Execution** - "Work for as long as needed, provide progress updates"

### TOOL USE (API Features)
15. **Parallel Tool Execution** - "Invoke all tools simultaneously"
16. **Tool Search** - On-demand discovery for >10 tools (85% token savings)
17. **Memory Tool** - Persistent storage: `/memories/[task].xml`
18. **Code Execution** - Run Python, create visualizations
19. **Computer Use** - Best prompt injection resistance among frontier models
20. **MCP Connector** - Connect remote servers without client code

### CONTEXT MANAGEMENT (Long Conversations)
21. **Context Awareness** - Model tracks remaining token budget
22. **Context Compaction** - Auto-summarize when approaching limits
23. **Fresh Context Strategy** - Sometimes better than compaction; discover from filesystem
24. **Prompt Caching** - 1-hour extended duration for repeated patterns

### OUTPUT CONTROL (Formatting)
25. **Communication Style** - Default concise; request verbose if needed
26. **Document Creation** - "Professional polish, visual hierarchy, domain awareness"
27. **Structured Output** - XML/JSON schema with validation
28. **Assistant Prefilling** - Pre-start response to control direction

### QUALITY ASSURANCE (High-Stakes)
29. **Agentic Search** - Structured research: hypotheses, confidence tracking, multi-source
30. **Prompt Chaining** - Self-review loops for quality
31. **Citation Requirements** - Source every claim
32. **Verification Steps** - "Review for [accuracy/security/completeness]"
33. **Constraint Enforcement** - Make all limits explicit

### SAFETY & ALIGNMENT
34. **Prompt Injection Resistance** - Built-in (18.21% vs 31.95% Sonnet 3.7)
35. **Reduced Reward Hacking** - 67% decrease vs previous models

---

## DECISION TREE: Which Techniques to Apply?

```
Is task SIMPLE? (single-step, clear output)
├─ YES → Apply: 1, 5, 10 (minimal enhancement)
└─ NO → Continue...

Does task need REASONING? (multi-step, analysis)
├─ YES → Apply: 6, 9 (extended thinking)
└─ MAYBE → Continue...

Does task use TOOLS? (APIs, file access)
├─ MANY (>10) → Apply: 16 (tool search)
├─ FEW → Apply: 15 (parallel execution)
└─ NONE → Continue...

Is task LONG-RUNNING? (>10 minutes)
├─ YES → Apply: 17, 21, 22 (memory + context mgmt)
└─ NO → Continue...

Is task AGENTIC? (autonomous, multi-step)
├─ YES → Apply: 11, 12, 13, 14 (full agentic suite)
└─ NO → Continue...

Is task HIGH-STAKES? (prod, financial, security)
├─ YES → Apply: 29, 30, 31, 32 (quality assurance)
└─ NO → Continue...

DOMAIN-SPECIFIC:
├─ CODING → 6, 15, 18, 32 (thinking, tools, verification)
├─ RESEARCH → 6, 7, 29, 31 (thinking, search, citations)
├─ CREATIVE → 1, 4, 25 (explicit, minimal structure)
├─ DOCUMENT → 26, 27 (polish, structure)
└─ AGENT → 11, 12, 13, 14, 17 (full agentic)
```

---

## API CONFIGURATION CHEATSHEET

### Model & Pricing
```python
model="claude-opus-4-5-20251101"
# $5/M input, $25/M output (3x cheaper than Opus 4.1)
```

### Extended Thinking (Techniques 6-9)
```python
thinking={
    "type": "enabled",
    "budget_tokens": 10000  # Start here, up to 64000
}
```

### Interleaved Thinking (Technique 7)
```python
betas=["interleaved-thinking-2025-05-14"]
```

### Effort Parameter (Technique 11)
```python
effort="medium"  # 76% token savings, Sonnet 4.5-level perf
effort="high"    # +4.3% vs Sonnet, 48% fewer tokens
```

### Memory Tool (Technique 17)
```python
tools=[{"type": "memory_20250818", "name": "memory"}]
betas=["context-management-2025-06-27"]
```

### Tool Search (Technique 16)
```python
tools=[
    {"type": "tool_search_tool_regex_20251119"},
    {"name": "your_tool", "defer_loading": True}
]
```

### Context Management (Techniques 21-22)
```python
betas=["context-management-2025-06-27"]
context_management={
    "edits": [{
        "type": "clear_tool_uses_20250919",
        "trigger": {"type": "input_tokens", "value": 100000},
        "keep": {"type": "tool_uses", "value": 3}
    }]
}
```

---

## PROMPT ENHANCEMENT TEMPLATE

```xml
<context>
[Why this task matters, who will use it, what's at stake]
</context>

<role>
You are [specific expertise] with [credentials/experience].
Your output will be used for [critical purpose].
</role>

<task>
[Clear, explicit instruction with action verbs]
[Add: "Don't hold back", "Go beyond basics" for complex tasks]
</task>

<methodology>
[For complex tasks: Step-by-step approach]
1. [First step]
2. [Second step]
...

[If reasoning needed:]
Think step-by-step in <thinking> tags.
Provide final answer in <answer> tags.
</methodology>

<constraints>
- [Specific limitation 1]
- [Quality threshold: "p < 0.05", "accuracy > 95%"]
- [Format requirement]
- If uncertain, state "I don't know" rather than guessing
</constraints>

<tools>
[If tools available:]
- Use [tool1] for [purpose]
- Execute operations in parallel when possible
- Store state in /memories/[task].xml for long-running tasks
</tools>

<output_format>
[Exact structure:]
1. [Section 1 name]
2. [Section 2 name]
...

[Specify: markdown, JSON, prose, table, etc.]
</output_format>

<verification>
[For critical tasks:]
After generating output, review for:
- [Accuracy criterion]
- [Security criterion]
- [Completeness criterion]
Identify and correct any issues before final output.
</verification>

<input>
{user_data_here}
</input>
```

---

## COST OPTIMIZATION QUICK WINS

1. **Use effort=medium** → 76% token savings for most tasks
2. **Start thinking at 10K** → Increase only if needed (vs 64K max)
3. **Enable Tool Search** → 85% reduction when using >10 tools
4. **Cache system prompts** → 1-hour duration, massive savings
5. **Batch similar tasks** → Reuse optimized templates

---

## WHEN TO USE OPUS 4.5 vs SONNET 4.5

**Use Opus 4.5 when:**
- Complex orchestration (managing subagents)
- Long-running workflows (>30 minutes)
- Maximum reasoning depth needed
- Token efficiency critical (effort=medium beats Sonnet)
- Highest quality/polish required

**Use Sonnet 4.5 when:**
- Sub-agent workers (orchestrated by Opus)
- High-volume, lower-complexity tasks
- Speed > reasoning depth
- Budget constraints (cheaper per token)
- Real-time user-facing responses

**Combined Strategy:**
```
Opus 4.5 (Orchestrator)
    ├─ Sonnet 4.5 (Worker 1)
    ├─ Sonnet 4.5 (Worker 2)
    └─ Haiku 4.5 (Simple worker)
```

---

## TROUBLESHOOTING

**Prompt too verbose?**
→ This is expected for Opus 4.5; model handles complexity well

**Not applying thinking?**
→ Check: Is task truly complex? System prioritizes cost efficiency

**Missing tool recommendations?**
→ Ensure task description implies tool use (e.g., "analyze data" → code execution)

**Effort not recommended?**
→ Default is no effort parameter; only suggested when cost/perf balance matters

---

## VALIDATION CHECKLIST

After running system prompt, verify:
- [ ] Output is valid XML with all required sections
- [ ] `<enhanced_prompt>` is complete and executable
- [ ] API configuration matches task complexity
- [ ] Techniques list explains all enhancements
- [ ] Usage notes provide actionable optimization tips
- [ ] Never executes task, only optimizes prompt

---

*Print this card for quick reference when building with Opus 4.5*
*All 35 techniques are encoded in the system prompt - just send any prompt to activate*

---

Generated: November 2025 | Model: claude-opus-4-5-20251101
Sources: 30+ official Anthropic docs, technical analyses, implementation guides
