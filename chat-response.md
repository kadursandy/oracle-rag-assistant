# 🤖 Oracle RAG Assistant -- Sample Chat (Q&A)

This document demonstrates example interactions with the Oracle RAG
Assistant.\
The assistant retrieves information from Oracle Cloud Infrastructure
(OCI) documentation using Retrieval-Augmented Generation (RAG).

------------------------------------------------------------------------

## 📌 Question 1: List services in OCI

### 🧑 User:

List services in OCI

### 🤖 Assistant:

Oracle Cloud Infrastructure (OCI) provides a comprehensive set of cloud
services across compute, storage, networking, database, analytics, AI,
security, and developer tools.

### Key Service Categories

**Compute Services** - Virtual Machines (VMs) - Bare Metal Instances -
Container Instances - Oracle Kubernetes Engine (OKE)

**Storage Services** - Block Volumes - Object Storage - File Storage -
Archive Storage

**Networking Services** - Virtual Cloud Network (VCN) - Load Balancing -
FastConnect - VPN Connect

**Database Services** - Oracle Autonomous Database - Oracle Database
Cloud Service - Oracle NoSQL Database - Data Guard & GoldenGate

**Security & IAM** - Identity Cloud Service - Policies and Roles - Web
Application Firewall (WAF) - Key Management - Security Zones

**Analytics & AI** - Oracle Analytics Cloud - Big Data Service - AI
Platform - Data Science Services

------------------------------------------------------------------------

## 📌 Question 2: Basic IAM Policies for Cross-Tenancy

### 🧑 User:

Give me basic IAM policies for cross tenancy

### 🤖 Assistant:

Cross-tenancy IAM policies allow users or groups in one tenancy to
access resources in another tenancy.

### Example Policy (Target Tenancy)

    Allow group CrossTenancyUsers to manage all-resources in compartment TargetCompartment

### Read-Only Access

    Allow group CrossTenancyUsers to inspect all-resources in compartment TargetCompartment

### Granular Resource Access

    Allow group CrossTenancyUsers to manage instances in compartment TargetCompartment

**Best Practices:** - Follow least privilege principle - Be specific
with resource types - Maintain documentation for audit compliance

------------------------------------------------------------------------

## 📌 Question 3: How to Set API Keys

### 🧑 User:

How to set API keys?

### 🤖 Assistant:

To configure API keys in OCI:

1.  Create a User in Identity section.
2.  Navigate to **API Keys** tab.
3.  Generate or upload a public key.
4.  Download the private key securely.
5.  Record:
    -   User OCID
    -   Tenancy OCID
    -   Region
    -   Key fingerprint

### Example Environment Variables

    export OCI_USER_OCID=<your_user_ocid>
    export OCI_TENANCY_OCID=<your_tenancy_ocid>
    export OCI_REGION=<your_region>
    export OCI_API_KEY_PRIVATE_KEY_FILE=<path_to_private_key>
    export OCI_API_KEY_FINGERPRINT=<fingerprint>

------------------------------------------------------------------------

## 📌 Question 4: What is AIDP?

### 🤖 Assistant:

AIDP (Autonomous Identity Database Provisioning) automates provisioning
and management of Oracle Autonomous Database resources, improving
scalability, cost optimization, and operational simplicity.

------------------------------------------------------------------------

## 📌 Question 5: What is an AI Data Platform?

### 🤖 Assistant:

An AI Data Platform (AIDP) is an integrated environment that supports
AI/ML development, deployment, and monitoring.

### Core Components:

-   Data Ingestion
-   Data Storage
-   Data Preparation
-   Model Development
-   Deployment & Monitoring
-   Governance & Security

------------------------------------------------------------------------

## 📌 Question 6: Resource Principal Example in Go

``` go
provider, err := common.NewResourcePrincipalConfiguration()
identityClient, err := identity.NewIdentityClientWithConfigurationProvider(provider)
```

Allows OCI services to authenticate without API keys.

------------------------------------------------------------------------

## 📌 Question 7: Workload Identity in Go

``` go
provider, err := common.NewWorkloadIdentityConfiguration()
identityClient, err := identity.NewIdentityClientWithConfigurationProvider(provider)
```

Used for workloads running in OKE or OCI-managed environments.

------------------------------------------------------------------------

# 🚀 Summary

This sample conversation demonstrates how the Oracle RAG Assistant:

-   Retrieves OCI documentation
-   Performs semantic search via vector embeddings
-   Generates context-aware responses
-   Supports IAM, API authentication, and OCI SDK examples
-   Handles multi-domain cloud architecture queries

------------------------------------------------------------------------

🔗 Built as part of the Oracle RAG Assistant Project
