<properties
   pageTitle="Schedules in Azure Automation | Azure"
   description="Automation schedules are used to schedule runbooks in Azure Automation to start automatically.  This article describes how to create schedules."
   services="automation"
   documentationCenter=""
   authors="mgoedtel"
   manager="stevenka"
   editor="tysonn" />
<tags
	ms.service="automation"
	ms.date="03/18/2016"
	wacn.date=""/>

# Schedules in Azure Automation

Automation Schedules are used to schedule runbooks to run automatically.  This could be either a single date and time for the runbook to run once.  Or, it could be a recurring hourly, daily, weekly, or monthly schedule to start the runbook multiple times.  Schedules are typically not accessed from runbooks.

## Windows PowerShell Cmdlets

The cmdlets in the following table are used to create and manage schedules with Windows PowerShell in Azure Automation. They ship as part of the [Azure PowerShell module](/documentation/articles/powershell-install-configure/).

|Cmdlets|Description|
|:---|:---|
|[Get-AzureAutomationSchedule](http://msdn.microsoft.com/zh-cn/library/dn690274.aspx)|Retrieves a schedule.|
|[New-AzureAutomationSchedule](http://msdn.microsoft.com/zh-cn/library/dn690271.aspx)|Creates a new schedule.|
|[Remove-AzureAutomationSchedule](http://msdn.microsoft.com/zh-cn/library/dn690279.aspx)|Removes a schedule.|
|[Set-AzureAutomationSchedule](http://msdn.microsoft.com/zh-cn/library/dn690270.aspx)|Sets the properties for an existing schedule.|
|[Get-AzureAutomationScheduledRunbook](http://msdn.microsoft.com/zh-cn/library/dn913778.aspx)|Retrieves scheduled runbooks.|
|[Register-AzureAutomationScheduledRunbook](http://msdn.microsoft.com/zh-cn/library/dn690265.aspx)|Associates a runbook with a schedule.|
|[Unregister-AzureAutomationScheduledRunbook](http://msdn.microsoft.com/zh-cn/library/dn690273.aspx)|Dissociates a runbook from a schedule.|

## Creating a new Schedule

### To create a new schedule with the Azure Classic Management Portal


1. From your automation account, click **Assets** at the top of the window.
1. At the bottom of the window, click **Add Setting**.
1. Click **Add Schedule**.
1. Complete the wizard and click the checkbox to save the new schedule.

### To create a new schedule with Windows PowerShell

The [New-AzureAutomationSchedule](http://msdn.microsoft.com/zh-cn/library/dn690271.aspx) cmdlet creates a new schedule and sets the value for an existing schedule.  The following sample Windows PowerShell commands create a new schedule called My Daily Schedule that starts on tomorrow at noon and fires every day one year:

	$automationAccountName = "MyAutomationAccount"
	$scheduleName = "My Daily Schedule"
	$startTime = (Get-Date).Date.AddDays(1).AddHours(12)
	$expiryTime = $startTime.AddYears(1)

	New-AzureAutomationSchedule -AutomationAccountName $automationAccountName -Name $scheduleName -StartTime $startTime -ExpiryTime $expiryTime -DayInterval 1


## See Also
- [Scheduling a runbook in Azure Automation](/documentation/articles/automation-scheduling-a-runbook/)
