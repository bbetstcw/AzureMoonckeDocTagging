<properties
   pageTitle="Azure Automation Security"
   description="This article provides an overview of automation security and the different authentication methods available for Automation Accounts in Azure Automation."
   services="automation"
   documentationCenter=""
   authors="MGoedtel"
   manager="jwhit"
   editor="tysonn"
   keywords="automation security, secure automation" />
<tags
	ms.service="automation"
	ms.date="07/06/2016"
	wacn.date=""/>

# Azure Automation security

[AZURE.ACOM]{

Azure Automation allows you to automate tasks against resources in Azure, on-premises, and with other cloud providers such as Amazon Web Services (AWS).  In order for a runbook to perform its required actions, it must have permissions to securely access the resources with the minimal rights required within the subscription.  

[AZURE.ACOM]}

[AZURE.ACN]{

Azure Automation allows you to automate tasks against resources in Azure and on-premises.  In order for a runbook to perform its required actions, it must have permissions to securely access the resources with the minimal rights required within the subscription.

[AZURE.ACN]}

This article will cover the various authentication scenarios supported by Azure Automation and will show you how to get started based on the environment or environments you need to manage.  

## Automation Account overview
When you start Azure Automation for the first time, you must create at least one Automation account. Automation accounts allow you to isolate your Automation resources (runbooks, assets, configurations) from the resources contained in other Automation accounts. You can use Automation accounts to separate resources into separate logical environments. For example, you might use one account for development, another for production, and another for your on-premises environment.  An Azure Automation account is different from your Azure account or accounts created in your Azure subscription.

The Automation resources for each Automation account are associated with a single Azure region, but Automation accounts can manage resources in any region. The main reason to create Automation accounts in different regions would be if you have policies that require data and resources to be isolated to a specific region.

[AZURE.ACOM]{

>[AZURE.NOTE]Automation accounts, and the resources they contain that are created in the Azure portal, cannot be accessed in the Azure Classic Management Portal. If you want to manage these accounts or their resources with Windows PowerShell, you must use the Azure Resource Manager modules.

[AZURE.ACOM]}

All of the tasks that you perform against resources using Azure Resource Manager (ARM) and the Azure cmdlets in Azure Automation must authenticate to Azure using Azure Active Directory organizational identity credential-based authentication.  Certificate-based  authentication was the original authentication method with Azure Service Management (ASM) mode, but it was complicated to setup.  Authenticating to Azure with Azure AD user was introduced back in 2014 to not only simplify the process to configure an Authentication account, but also support the ability to non-interactively authenticate to Azure with a single user account that worked with both ASM and ARM mode.   

We recently released another update, where we now automatically create an Azure AD service principal object when the Automation account is created. This is referred to as an Azure Run As account and is the default authentication method for runbook automation with Azure Resource Manager.     

Role-based access control is available in ARM mode to grant permitted actions to an Azure AD user account and service principal, and authenticate that service principal.  Please read [Role-based access control in Azure Automation article](/documentation/articles/automation-role-based-access-control/) for further information to help develop your model for managing Automation permissions.  

[AZURE.ACOM]{

Runbooks running on a Hybrid Runbook Worker in your datacenter or against computing services in AWS cannot use the same method that is typically used for runbooks authenticating to Azure resources.  This is because those resources are running outside of Azure and therefore, will require their own security credentials defined in Automation to authenticate to resources that they will access locally.  

[AZURE.ACOM]}

## Authentication methods

The following table summarizes the different authentication methods for each environment supported by Azure Automation and the article describing how to setup authentication for your runbooks.

Method  |  Environment  | Article
----------|----------|----------
Azure AD User Account | Azure Resource Manager and Azure Service Management | [Authenticate Runbooks with Azure AD User account](/documentation/articles/automation-sec-configure-aduser-account/)
|[AZURE.ACN]{|
Azure AD Service Principal object | Azure Resource Manager | Authenticate Runbooks with Azure Run As account
|[AZURE.ACN]}|
|[AZURE.ACOM]{|
Azure AD Service Principal object | Azure Resource Manager | [Authenticate Runbooks with Azure Run As account](/documentation/articles/automation-sec-configure-azure-runas-account/)
|[AZURE.ACOM]}|
|[AZURE.ACOM]{|
Windows Authentication | On-Premises Datacenter | [Authenticate Runbooks for Hybrid Runbook Workers](/documentation/articles/automation-hybrid-runbook-worker/)
|[AZURE.ACOM]}|
|[AZURE.ACOM]{|
AWS Credentials | Amazon Web Services | [Authenticate Runbooks with Amazon Web Services (AWS)](/documentation/articles/automation-sec-configure-aws-account/)
|[AZURE.ACOM]}|

