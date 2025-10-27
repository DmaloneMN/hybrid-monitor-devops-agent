# 🔧 Hybrid Azure Monitor + DevOps Agent (Copilot Studio + Azure AI Foundry)

This solution implements a hybrid agent that monitors Azure alerts, summarizes issues using a fine-tuned model, and triggers DevOps deployments — combining the orchestration power of **Copilot Studio** with the intelligence of **Azure AI Foundry**.

---

## 📌 Use Case

- **Input**: Azure Monitor alert (e.g., high CPU, failed deployment)
- **Agent Action**:
  1. Summarize the alert using a fine-tuned GPT-4 or SLM model
  2. Recommend remediation (e.g., restart service, scale out)
  3. Trigger a DevOps pipeline or rollback
  4. Log actions to Fabric or tag resources via Purview (optional)

---

## 🧱 Architecture Overview
User → Copilot Studio Agent → Azure Monitor Plugin (GET alert) → Azure Function Plugin (POST to Foundry model) → Azure DevOps Plugin (POST to trigger deployment) → Optional: Fabric Logging / Purview Tagging


- **Copilot Studio**: Handles multi-turn orchestration, plugin routing, and user interaction
- **Azure AI Foundry**: Hosts the summarization/classification model
- **Azure Function**: Bridge layer to normalize payloads and call the model

---

## 📁 Repo Structure
hybrid-monitor-devops-agent/ ├── README.md ├── .github/ │   └── workflows/ │       └── deploy-function.yml         # CI/CD pipeline for Azure Function ├── copilot-studio/ │   ├── plugin-manifests/ │   │   ├── azure-monitor.json │   │   ├── azure-devops.json │   │   └── summarize-alert.json │   └── agent-config.md                 # Agent intents, flows, and logic ├── foundry-model/ │   ├── training-data/ │   │   └── alerts.jsonl                # JSONL file for fine-tuning │   └── model-config.md                 # Model type, endpoint, and usage ├── azure-function/ │   ├── summarize-alert/ │   │   ├── init.py                 # Python function code │   │   ├── function.json               # Azure Function binding config │   │   └── requirements.txt            # Dependencies │   └── local.settings.json             # Local dev config (excluded from prod) ├── docs/ │   ├── architecture-diagram.png        # Visual flow of hybrid agent │   ├── deployment-checklist.md         # Step-by-step rollout guide │   └── telemetry-setup.md              # App Insights + Monitor config

---

## 🚀 Quick Start

### 1. Fine-Tune or Deploy Model
- Format training data in `foundry-model/training-data/alerts.jsonl`
- Use Azure AI Foundry CLI or portal to fine-tune or deploy a model
- Save endpoint and key in Azure Key Vault

### 2. Deploy Azure Function
- Edit `azure-function/summarize-alert/__init__.py` to call your model
- Deploy via `deploy-function.yml` GitHub Actions workflow

### 3. Configure Copilot Studio Agent
- Create orchestration agent
- Upload plugin manifests from `copilot-studio/plugin-manifests/`
- Define intents and flows in `agent-config.md`

---

## 🔐 Security & Access

- Use **Azure Key Vault** for secrets
- Enable **Managed Identity** for Azure Function
- Enforce **RBAC** in Copilot Studio and DevOps

---

## 📊 Monitoring

- Enable **Application Insights** for Azure Function
- Use **Azure Monitor** to track alert volume and agent usage
- Optional: log actions to Fabric or tag resources via Purview

---

## 🧠 Future Enhancements

- Add SLM/Nano model for fast triage
- Integrate with Microsoft Fabric for audit trails
- Build a feedback loop to improve model recommendations

---

## 🤝 Contributing

Feel free to fork, extend, or adapt this solution for your own hybrid agent scenarios. PRs welcome!

---

## 📄 License

MIT License



Would you like me to generate the actual contents of the plugin manifest files or the Azure Function code next? I can also simulate the alerts.jsonl training file or help you build the agent-config.md for Copilot Studio.

---

## 🚀 Quick Start

### 1. Fine-Tune or Deploy Model
- Format training data in `foundry-model/training-data/alerts.jsonl`
- Use Azure AI Foundry CLI or portal to fine-tune or deploy a model
- Save endpoint and key in Azure Key Vault

### 2. Deploy Azure Function
- Edit `azure-function/summarize-alert/__init__.py` to call your model
- Deploy via `deploy-function.yml` GitHub Actions workflow

### 3. Configure Copilot Studio Agent
- Create orchestration agent
- Upload plugin manifests from `copilot-studio/plugin-manifests/`
- Define intents and flows in `agent-config.md`

---

## 🔐 Security & Access

- Use **Azure Key Vault** for secrets
- Enable **Managed Identity** for Azure Function
- Enforce **RBAC** in Copilot Studio and DevOps

---

## 📊 Monitoring

- Enable **Application Insights** for Azure Function
- Use **Azure Monitor** to track alert volume and agent usage
- Optional: log actions to Fabric or tag resources via Purview

---

## 🧠 Future Enhancements

- Add SLM/Nano model for fast triage
- Integrate with Microsoft Fabric for audit trails
- Build a feedback loop to improve model recommendations

---

## 🤝 Contributing

Feel free to fork, extend, or adapt this solution for your own hybrid agent scenarios. PRs welcome!

---

## 📄 License

MIT License
