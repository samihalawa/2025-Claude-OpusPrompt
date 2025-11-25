#!/usr/bin/env python3
"""
Test script to verify the Opus 4.5 Prompt Expert system prompt
Demonstrates how it transforms various prompt types
"""

# These are example transformations the system should produce
# Use these to verify your implementation is working correctly

TEST_CASES = [
    {
        "name": "Simple Task",
        "input": "Write a function to reverse a string",
        "expected_features": [
            "Explicit error handling instruction",
            "Production-ready code requirement",
            "Test case inclusion",
            "XML structure for clarity",
            "Output format specification"
        ]
    },
    {
        "name": "Research Task",
        "input": "Research AI ethics frameworks",
        "expected_features": [
            "Extended thinking enabled (budget_tokens: 10000+)",
            "Structured research protocol (hypothesis tracking)",
            "Citation requirements",
            "Multi-source verification",
            "Agentic search instructions",
            "Success criteria definition"
        ]
    },
    {
        "name": "Complex Agent Workflow",
        "input": "Build an agent that monitors GitHub, creates PRs, and notifies team",
        "expected_features": [
            "Extended thinking enabled (budget_tokens: 32000+)",
            "Memory tool recommended",
            "Context management instructions",
            "Subagent delegation patterns",
            "Parallel tool execution",
            "Effort parameter (high or medium)",
            "Progress tracking requirements"
        ]
    },
    {
        "name": "Document Creation",
        "input": "Create a quarterly business review presentation",
        "expected_features": [
            "Professional polish instruction",
            "Visual hierarchy requirements",
            "Domain awareness emphasis",
            "Completeness specification",
            "Thoughtful design elements mention"
        ]
    },
    {
        "name": "Data Analysis",
        "input": "Analyze sales data for trends",
        "expected_features": [
            "Extended thinking enabled",
            "Statistical rigor requirements",
            "Visualization recommendations",
            "Actionable insights focus",
            "Confidence levels required",
            "Code execution tool suggested"
        ]
    }
]

def verify_optimization(test_case: dict, optimized_output: str) -> dict:
    """
    Verify that the optimization includes expected features
    
    Returns:
        dict with verification results
    """
    results = {
        "test_name": test_case["name"],
        "passed": [],
        "missing": []
    }
    
    for feature in test_case["expected_features"]:
        # Simple keyword matching - in production you'd parse XML
        if any(keyword.lower() in optimized_output.lower() 
               for keyword in feature.split()):
            results["passed"].append(feature)
        else:
            results["missing"].append(feature)
    
    return results

def print_test_results(results: dict):
    """Pretty print verification results"""
    print(f"\n{'='*80}")
    print(f"TEST: {results['test_name']}")
    print(f"{'='*80}")
    
    print(f"\n✅ PASSED ({len(results['passed'])}):")
    for feature in results['passed']:
        print(f"   • {feature}")
    
    if results['missing']:
        print(f"\n❌ MISSING ({len(results['missing'])}):")
        for feature in results['missing']:
            print(f"   • {feature}")
    
    score = len(results['passed']) / (len(results['passed']) + len(results['missing']))
    print(f"\nScore: {score*100:.1f}%")

# Example usage with mock data
if __name__ == "__main__":
    print("="*80)
    print("OPUS 4.5 PROMPT EXPERT - VERIFICATION TEST SUITE")
    print("="*80)
    print("\nRun this with actual API calls to verify your implementation.")
    print("Expected behavior for each test case:\n")
    
    for test_case in TEST_CASES:
        print(f"\n{'─'*80}")
        print(f"Test: {test_case['name']}")
        print(f"Input: {test_case['input']}")
        print(f"\nExpected features in optimization:")
        for feature in test_case['expected_features']:
            print(f"  ✓ {feature}")
    
    print("\n" + "="*80)
    print("TO RUN ACTUAL VERIFICATION:")
    print("="*80)
    print("""
1. Load the system prompt from opus_4_5_system_prompt.txt
2. For each test case, call the API with:
   - system: [loaded system prompt]
   - user message: test_case['input']
3. Parse XML response
4. Verify expected features are present
5. Report pass/fail results
    """)
    
    print("\nSample implementation:")
    print("""
    from anthropic import Anthropic
    import os
    
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    
    with open("opus_4_5_system_prompt.txt", "r") as f:
        system_prompt = f.read()
    
    for test_case in TEST_CASES:
        response = client.messages.create(
            model="claude-opus-4-5-20251101",
            max_tokens=16000,
            system=system_prompt,
            messages=[{"role": "user", "content": test_case["input"]}]
        )
        
        optimized = response.content[0].text
        results = verify_optimization(test_case, optimized)
        print_test_results(results)
    """)

print("\n" + "="*80)
print("Key Success Indicators:")
print("="*80)
print("""
✓ System prompt never executes tasks, only optimizes prompts
✓ All responses are in XML format with required sections
✓ Simple tasks get moderate enhancement (3-5 techniques)
✓ Complex tasks get full enhancement suite (10+ techniques)
✓ API configuration matches task complexity
✓ Extended thinking enabled for reasoning-heavy tasks
✓ Effort parameter recommended for cost optimization
✓ Tool recommendations match task requirements
✓ Enhanced prompts are production-ready (copy-paste executable)
""")
