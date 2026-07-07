# Tech-Audit AI: Automated Compliance RAG Agent
An autonomous, production-grade Agentic RAG Pipeline designed to audit internal corporate infrastructure logs against strict regulatory data protection frameworks.
Powered entirely by the LlamaIndex Workflow architecture and utilizing the free-tier Gemini 2.5 Flash model, this agent executes autonomous reasoning loops (ReAct) to identify infrastructure compliance failures, unencrypted data risks, and data retention violations without incurring OpenAI API costs.
## Key Features
 * Autonomous ReAct Agent Loop: Rather than executing standard linear text retrieval, the agent dynamically determines which database or regulatory framework tool to query based on contextual auditing requirements.
 * 100% Free Production Stack: Powered by Google's gemini-2.5-flash for advanced functional calling/reasoning and BAAI/bge-small-en-v1.5 for fast, localized data embedding.
 * State-Aware Workflow Architecture: Leverages the latest LlamaIndex Context and asynchronous runtime specifications for tracking conversation sessions during multi-step analysis.
 * Zero Infrastructure Overhead: Reads fragmented text configurations natively using the updated SimpleDirectoryReader engine.
## System Architecture & Data Sources
The agent operates across isolated data environments to preserve compliance objectivity:
 1. company_retention_policy.txt (Internal Environment): Simulates a production profile containing data retention timelines, plain-text developer debugging logs, and standard database encryption specifications.
 2. compliance_requirements.txt (Regulatory Baseline): Serves as the golden legal standard, detailing storage limitation mandates and strict backup encryption thresholds.
> ☕:
Here is a clean, professional README.md template tailored exactly to the project you just built. It highlights the architecture, the free-tier tech stack, and shows recruiters that you understand production-level AI concepts like state management and multi-step reasoning.
# Tech-Audit AI: Automated Compliance RAG Agent
An autonomous, production-grade Agentic RAG Pipeline designed to audit internal corporate infrastructure logs against strict regulatory data protection frameworks.
Powered entirely by the LlamaIndex Workflow architecture and utilizing the free-tier Gemini 2.5 Flash model, this agent executes autonomous reasoning loops (ReAct) to identify infrastructure compliance failures, unencrypted data risks, and data retention violations without incurring OpenAI API costs.
## 🚀 Key Features
 * Autonomous ReAct Agent Loop: Rather than executing standard linear text retrieval, the agent dynamically determines which database or regulatory framework tool to query based on contextual auditing requirements.
 * 100% Free Production Stack: Powered by Google's gemini-2.5-flash for advanced functional calling/reasoning and BAAI/bge-small-en-v1.5 for fast, localized data embedding.
 * State-Aware Workflow Architecture: Leverages the latest LlamaIndex Context and asynchronous runtime specifications for tracking conversation sessions during multi-step analysis.
 * Zero Infrastructure Overhead: Reads fragmented text configurations natively using the updated SimpleDirectoryReader engine.
## 📁 System Architecture & Data Sources
The agent operates across isolated data environments to preserve compliance objectivity:
 1. company_retention_policy.txt (Internal Environment): Simulates a production profile containing data retention timelines, plain-text developer debugging logs, and standard database encryption specifications.
 2. compliance_requirements.txt (Regulatory Baseline): Serves as the golden legal standard, detailing storage limitation mandates and strict backup encryption thresholds.

## Sample Output & Audit Evaluation Summary
When executed, the agent successfully handles multi-step tool navigation and synthesizes the following risks:

1. Indefinite Data Retention: Identifies that customer PII (names, emails, IP addresses) is stored indefinitely, directly violating regulatory storage limitations.
2. Unencrypted Debug Logs: Flags that fallback developer logs are left in plain text format, exposing critical user identifiers and failing standard backup encryption rules.
##  License
Distributed under the MIT License. Feel free to use, modify, and build upon this pipeline for your compliance portfolios!

