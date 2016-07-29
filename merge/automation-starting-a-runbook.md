<properties
   pageTitle="Starting a runbook in Azure Automation | Azure"
   description="Summarizes the different methods that can be used to start a runbook in Azure Automation and provides details on using both the Azure Classic Management Portal and Windows PowerShell."
   services="automation"
   documentationCenter=""
   authors="mgoedtel"
   manager="jwhit"
   editor="tysonn" /><tags
	ms.service="automation"
	ms.date="06/06/2016"
	wacn.date=""/>

# Starting a runbook in Azure Automation

[AZURE.ACOM]{

The following table will help you determine the method to start a runbook in Azure Automation that is most suitable to your particular scenario. This article includes details on starting a runbook with the Azure portal and with Windows PowerShell. Details on the other methods are provided in other documentation that you can access from the links below.

[AZURE.ACOM]}

[AZURE.ACN]{

The following table will help you determine the method to start a runbook in Azure Automation that is most suitable to your particular scenario. This article includes details on starting a runbook with the Azure Classic Management Portal and with Windows PowerShell. Details on the other methods are provided in other documentation that you can access from the links below.

[AZURE.ACN]}

| **METHOD**                                                                    | **CHARACTERISTICS**                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|[AZURE.ACOM]{|
| [Azure Portal](#starting-a-runbook-with-the-azure-portal)                     | <li>Simplest method with interactive user interface.<br> <li>Form to provide simple parameter values.<br> <li>Easily track job state.<br> <li>Access authenticated with Azure logon.                                                                                                                                                                               |
|[AZURE.ACOM]}|
|[AZURE.ACN]{|
| [Azure Classic Management Portal](#starting-a-runbook-with-the-azure-portal)                     | <li>Simplest method with interactive user interface.<br> <li>Form to provide simple parameter values.<br> <li>Easily track job state.<br> <li>Access authenticated with Azure logon.                                                                                                                                                                               |
|[AZURE.ACN]}|
| [Windows PowerShell](https://msdn.microsoft.com/zh-cn/library/dn690259.aspx)        | <li>Call from command line with Windows PowerShell cmdlets.<br> <li>Can be included in automated solution with multiple steps.<br> <li>Request is authenticated with certificate or OAuth user principal / service principal.<br> <li>Provide simple and complex parameter values.<br> <li>Track job state.<br> <li>Client required to support PowerShell cmdlets. |
|[AZURE.ACOM]{|
| [Azure Automation API](https://msdn.microsoft.com/zh-cn/library/azure/mt662285.aspx) | <li>Most flexible method but also most complex.<br> <li>Call from any custom code that can make HTTP requests.<br> <li>Request authenticated with certificate, or Oauth user principal / service principal.<br> <li>Provide simple and complex parameter values.<br> <li>Track job state.                                                                          |
|[AZURE.ACOM]}|
|[AZURE.ACN]{|
| [Azure Automation API](http://msdn.microsoft.com/zh-cn/library/azure/mt163849.aspx) | <li>Most flexible method but also most complex.<br> <li>Call from any custom code that can make HTTP requests.<br> <li>Request authenticated with certificate, or Oauth user principal / service principal.<br> <li>Provide simple and complex parameter values.<br> <li>Track job state.                                                                          |
|[AZURE.ACN]}|
| [Webhooks](/documentation/articles/automation-webhooks/)                                            | <li>Start runbook from single HTTP request.<br> <li>Authenticated with security token in URL.<br> <li>Client cannot override parameter values specified when webhook created. Runbook can define single parameter that is populated with the HTTP request details.<br> <li>No ability to track job state through webhook URL.                                      |
|[AZURE.ACOM]{|
| [Respond to Azure Alert](/documentation/articles/log-analytics-alerts/)               | <li>Start a runbook in response to Azure alert.<br> <li>Configure webhook for runbook and link to alert.<br> <li>Authenticated with security token in URL.<br> <li>Currently supports alert on Metrics only.                                                                                                                                                       |
|[AZURE.ACOM]}|
|[AZURE.ACOM]{|
| [Schedule](/documentation/articles/automation-scheduling-a-runbook/)                                | <li>Automatically start runbook on hourly, daily, or weekly schedule.<br> <li>Manipulate schedule through Azure portal, PowerShell cmdlets, or Azure API.<br> <li>Provide parameter values to be used with schedule.                                                                                                                                               |
|[AZURE.ACOM]}|
|[AZURE.ACN]{|
| [Schedule](/documentation/articles/automation-scheduling-a-runbook/)                                | <li>Automatically start runbook on hourly, daily, or weekly schedule.<br> <li>Manipulate schedule through Azure Classic Management Portal, PowerShell cmdlets, or Azure API.<br> <li>Provide parameter values to be used with schedule.                                                                                                                                               |
|[AZURE.ACN]}|
| [From Another Runbook](/documentation/articles/automation-child-runbooks/)                          | <li>Use a runbook as an activity in another runbook.<br> <li>Useful for functionality used by multiple runbooks.<br> <li>Provide parameter values to child runbook and use output in parent runbook.                                                                                                                                                               |

[AZURE.ACOM]{

The following image illustrates detailed step-by-step process in the life cycle of a runbook. It includes different ways a runbook is started in Azure Automation, components required for Hybrid Runbook Worker to execute Azure Automation runbooks and interactions between different components. To learn about executing Automation runbooks in your datacenter, refer to [hybrid runbook workers](/documentation/articles/automation-hybrid-runbook-worker/)

[AZURE.ACOM]}

[AZURE.ACN]{

The following image illustrates detailed step-by-step process in the life cycle of a runbook. It includes different ways a runbook is started in Azure Automation, components required for an on-premises machine to execute Azure Automation runbooks and interactions between different components.

[AZURE.ACN]}

![Runbook Architecture](./media/automation-starting-runbook/runbooks-architecture.png)

##<a name="starting-a-runbook-with-the-azure-portal"></a> Starting a runbook with the Azure Classic Management Portal

1.	In the Azure Classic Management Portal, select **Automation** and then then click the name of an automation account.
2.	Select the **Runbooks** tab.
3.	Select a runbook, and then click **Start**.
4.	If the runbook has parameters, you will be prompted to provide values with a text box for each parameter. See [Runbook Parameters](#Runbook-parameters) below for further details on parameters.
5.	Either select **View Job** next to the **Starting** runbook message or select the **Jobs** tab for the runbook to view the runbook job's status.

[AZURE.ACOM]{

## Starting a runbook with the Azure portal

1.	From your automation account, click the **Runbooks** part to open the **Runbooks** blade.
2.	Click a runbook to open its **Runbook** blade.
3.	Click **Start**.
4.	If the runbook has no parameters, you will be prompted to confirm whether you want to start it. If the runbook has parameters, the **Start Runbook** blade will be opened so you can provide parameter values. See [Runbook Parameters](#Runbook-parameters) below for further details on parameters.
5.	The **Job** blade is opened so that you can track the job's status.

[AZURE.ACOM]}

##<a name="starting-a-runbook-with-windows-powershell"></a> Starting a runbook with Windows PowerShell

[AZURE.ACOM]{

You can use the [Start-AzureRmAutomationRunbook](https://msdn.microsoft.com/zh-cn/library/mt603661.aspx) to start a runbook with Windows PowerShell. The following sample code starts a runbook called Test-Runbook.

	Start-AzureRmAutomationRunbook -AutomationAccountName "MyAutomationAccount" -Name "Test-Runbook" -ResourceGroupName "ResourceGroup01"

Start-AzureRmAutomationRunbook returns a job object that you can use to track its status once the runbook is started. You can then use this job object with [Get-AzureRmAutomationJob](https://msdn.microsoft.com/zh-cn/library/mt619440.aspx) to determine the status of the job and [Get-AzureRmAutomationJobOutput](https://msdn.microsoft.com/zh-cn/library/mt603476.aspx) to get its output. The following sample code starts a runbook called Test-Runbook, waits until it has completed, and then displays its output.

[AZURE.ACOM]}

[AZURE.ACN]{

You can use the [Start-AzureAutomationRunbook](http://msdn.microsoft.com/zh-cn/library/azure/dn690259.aspx) to start a runbook with Windows PowerShell. The following sample code starts a runbook called Test-Runbook.

	Start-AzureAutomationRunbook –AutomationAccountName "MyAutomationAccount" –Name "Test-Runbook"

Start-AzureAutomationRunbook returns a job object that you can use to track its status once the runbook is started. You can then use this job object with [Get-AzureAutomationJob](http://msdn.microsoft.com/zh-cn/library/azure/dn690263.aspx) to determine the status of the job and [Get-AzureAutomationJobOutput](http://msdn.microsoft.com/zh-cn/library/azure/dn690268.aspx) to get its output. The following sample code starts a runbook called Test-Runbook, waits until it has completed, and then displays its output.

[AZURE.ACN]}

	$runbookName = "Test-Runbook"

	[AZURE.ACOM]{

	$ResourceGroup = "ResourceGroup01"

	[AZURE.ACOM]}

	$AutomationAcct = "MyAutomationAccount"

	[AZURE.ACOM]{

	$job = Start-AzureRmAutomationRunbook -AutomationAccountName $AutomationAcct -Name $runbookName -ResourceGroupName $ResourceGroup

	[AZURE.ACOM]}

	[AZURE.ACN]{

	$job = Start-AzureAutomationRunbook -AutomationAccountName $AutomationAcct -Name $runbookName

	[AZURE.ACN]}

	$doLoop = $true
	While ($doLoop) {

	   [AZURE.ACOM]{

	   $job = Get-AzureRmAutomationJob -AutomationAccountName $AutomationAcct -Id $job.JobId -ResourceGroupName $ResourceGroup

	   [AZURE.ACOM]}

	   [AZURE.ACN]{

	   $job = Get-AzureAutomationJob -AutomationAccountName $AutomationAcct -Id $job.Id

	   [AZURE.ACN]}

	   $status = $job.Status
	   $doLoop = (($status -ne "Completed") -and ($status -ne "Failed") -and ($status -ne "Suspended") -and ($status -ne "Stopped"))
	}

	[AZURE.ACOM]{

	Get-AzureRmAutomationJobOutput -AutomationAccountName $AutomationAcct -Id $job.JobId -ResourceGroupName $ResourceGroup -Stream Output

	[AZURE.ACOM]}

	[AZURE.ACN]{

	Get-AzureAutomationJobOutput -AutomationAccountName $AutomationAcct -Id $job.Id -Stream Output

	[AZURE.ACN]}

If the runbook requires parameters, then you must provide them as a [hashtable](http://technet.microsoft.com/zh-cn/library/hh847780.aspx) where the key of the hashtable matches the parameter name and the value is the parameter value. The following example shows how to start a runbook with two string parameters named FirstName and LastName, an integer named RepeatCount, and a boolean parameter named Show. For additional information on parameters, see [Runbook Parameters](#Runbook-parameters) below.
	$params = @{"FirstName"="Joe";"LastName"="Smith";"RepeatCount"=2;"Show"=$true}

	[AZURE.ACOM]{

	Start-AzureRmAutomationRunbook -AutomationAccountName "MyAutomationAccount" -Name "Test-Runbook" -ResourceGroupName "ResourceGroup01" -Parameters $params

	[AZURE.ACOM]}

	[AZURE.ACN]{

	Start-AzureAutomationRunbook -AutomationAccountName "MyAutomationAccount" -Name "Test-Runbook" -Parameters $params

	[AZURE.ACN]}

##<a name="runbook-parameters"></a> Runbook parameters

[AZURE.ACOM]{

When you start a runbook from the Azure Portal or Windows PowerShell, the instruction is sent through the Azure Automation web service. This service does not support parameters with complex data types. If you need to provide a value for a complex parameter, then you must call it inline from another runbook as described in [Child runbooks in Azure Automation](/documentation/articles/automation-child-runbooks/).

[AZURE.ACOM]}

[AZURE.ACN]{

When you start a runbook from the Azure Classic Management Portal or Windows PowerShell, the instruction is sent through the Azure Automation web service. This service does not support parameters with complex data types. If you need to provide a value for a complex parameter, then you must call it inline from another runbook as described in [Child runbooks in Azure Automation](/documentation/articles/automation-child-runbooks/).

[AZURE.ACN]}

The Azure Automation web service will provide special functionality for parameters using certain data types as described in the following sections.

### Named Values

If the parameter is data type [object], then you can use the following JSON format to send it a list of named values: *{"Name1":Value1, "Name2":Value2, "Name3":Value3}*. These values must be simple types. The runbook will receive the parameter as a [PSCustomObject](https://msdn.microsoft.com/zh-cn/library/system.management.automation.pscustomobject(v=vs.85).aspx) with properties that correspond to each named value.

Consider the following test runbook that accepts a parameter called user.

	Workflow Test-Parameters
	{
	   param ( 
	      [Parameter(Mandatory=$true)][object]$user
	   )
	    if ($user.Show) {
	        foreach ($i in 1..$user.RepeatCount) {
	            $user.FirstName
	            $user.LastName
	        }
	    } 
	}

The following text could be used for the user parameter.

	{"FirstName":"Joe","LastName":"Smith","RepeatCount":2,"Show":true}

This results in the following output.

	Joe
	Smith
	Joe
	Smith

### Arrays

If the parameter is an array such as [array] or [string[]], then you can use the following JSON format to send it a list of values: *[Value1,Value2,Value3]*. These values must be simple types.

Consider the following test runbook that accepts a parameter called *user*.

	Workflow Test-Parameters
	{
	   param ( 
	      [Parameter(Mandatory=$true)][array]$user
	   )
	    if ($user[3]) {
	        foreach ($i in 1..$user[2]) {
	            $ user[0]
	            $ user[1]
	        }
	    } 
	}

The following text could be used for the user parameter.

	["Joe","Smith",2,true]

This results in the following output.

	Joe
	Smith
	Joe
	Smith

### Credentials

If the parameter is data type **PSCredential**, then you can provide the name of an Azure Automation [credential asset](/documentation/articles/automation-credentials/). The runbook will retrieve the credential with the name that you specify.

Consider the following test runbook that accepts a parameter called credential.

	Workflow Test-Parameters
	{
	   param ( 
	      [Parameter(Mandatory=$true)][PSCredential]$credential
	   )
	   $credential.UserName
	}

The following text could be used for the user parameter assuming that there was a credential asset called *My Credential*.

	My Credential

Assuming the username in the credential was *jsmith*, this results in the following output.

	jsmith

## Next Steps

- [AZURE.ACOM]{

-	The runbook architecture in current article provides a high-level description about hybrid runbooks.  To learn more, see [Child runbooks in Azure Automation](/documentation/articles/automation-child-runbooks/)
- [AZURE.ACOM]}

- [AZURE.ACN]{

-	The runbook architecture in current article provides a high-level description about the child runbooks, to know more details, see [Child runbooks in Azure Automation](/documentation/articles/automation-child-runbooks/)
- [AZURE.ACN]}

