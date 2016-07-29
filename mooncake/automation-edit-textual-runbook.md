<properties 
	pageTitle="Editing textual runbooks in Azure Automation"
	description="This article provides different procedures for working and PowerShell Workflow runbooks in Azure Automation using the textual editor."
	services="automation"
	documentationCenter=""
	authors="mgoedtel"
	manager="stevenka"
	editor="tysonn" />
<tags
	ms.service="automation"
	ms.date="02/23/2016"
	wacn.date=""/>

# Editing textual runbooks in Azure Automation

The textual editor in Azure Automation can be used to edit PowerShell Workflow runbooks. This has the typical features of other code editors such as intellisense and color coding  with additional special features to assist you in accessing resources common to runbooks.  This article provides detailed steps for performing different functions with this editor.

The textual editor includes a feature to insert code for activities, assets, and child runbooks into a runbook. Rather than typing in the code yourself, you can select from a list of available resources and have the appropriate code inserted into the runbook.

Each runbook in Azure Automation has two versions, Draft and Published. You edit the Draft version of the runbook and then publish it so it can be executed. The Published version cannot be edited. See [Publishing a runbook](/documentation/articles/automation-creating-importing-runbook/#publishing-a-runbook) for more information.


## To edit a runbook with the Azure Classic Management Portal

Use the following procedure to open a runbook for editing in the textual editor.

1. In the Azure Classic Management Portal, select **Automation** and then then click the name of an automation account.
2. Select the **Runbooks** tab.
3. Click the name of the runbook you want to edit and then select the **Author** tab.
5. Click the **Edit** button at the bottom of the screen.
6. Perform the required editing.
7. Click **Save** when your edits are complete.
8. Click **Publish** if you want the latest draft version of the runbook to be published.

### To insert an activity into a Runbook

1. In the Canvas of the textual editor, position the cursor where you want to place the activity.
1. At the bottom of the screen, click **Insert** and then **Activity**.
1. In the **Integration Module** column, select the module that contains the activity.
1. In the **Activity** pane, select an activity.
1. In the **Description** column, note the description of the activity. Optionally, you can click View detailed help to launch help for the activity in the browser.
1. Click the right arrow.  If the activity has parameters, they will be listed for your information.
1. Click the check button.  Code to run the activity will be inserted into the runbook.
1. If the activity requires parameters, provide an appropriate value in place of the data type surrounded by braces <>.

### To insert code for a child runbook into a runbook

1. In the Canvas of the textual editor, position the cursor where you want to place the [child runbook](/documentation/articles/automation-child-runbooks/).
2. At the bottom of the screen, click **Insert** and then **Runbook**.
3. Select the runbook to insert from the center column and click the right arrow.
4. If the runbook has parameters, they will be listed for your information.
5. Click the check button.  Code to run the selected runbook will be inserted into the current runbook.
7. If the runbook requires parameters, provide an appropriate value in place of the data type surrounded by braces <>.

### To insert an asset into a runbook

1. In the Canvas of the textual editor, position the cursor where you want to place the activity to retrieve the asset.
1. At the bottom of the screen, click **Insert** and then **Setting**.
1. In the **Setting Action** column, select the action that you want.
1. Select from the available assets in the center column.
1. Click the check button.  Code to get or set the asset will be inserted into the runbook.



## To edit an Azure Automation runbook using Windows PowerShell

To edit a runbook with Windows PowerShell, you use the editor of your choice and save it to a .ps1 file. You can use the [Get-AzureAutomationRunbookDefinition](https://msdn.microsoft.com/zh-cn/library/dn690269.aspx) cmdlet to retrieve the contents of the runbook and then [Set-AzureAutomationRunbookDefinition](https://msdn.microsoft.com/zh-cn/library/dn690267.aspx) cmdlet to replace the existing draft runbook with the modified one.

### To Retrieve the Contents of a Runbook Using Windows PowerShell

The following sample commands show how to retrieve the script for a runbook and save it to a script file. In this example, the Draft version is retrieved. It is also possible to retrieve the Published version of the runbook although this version cannot be changed.

    $automationAccountName = "MyAutomationAccount"
    $runbookName = "Sample-TestRunbook"
    $scriptPath = "c:\runbooks\Sample-TestRunbook.ps1"
    
    $runbookDefinition = Get-AzureAutomationRunbookDefinition -AutomationAccountName $automationAccountName -Name $runbookName -Slot Draft
    $runbookContent = $runbookDefinition.Content

    Out-File -InputObject $runbookContent -FilePath $scriptPath

### To Change the Contents of a Runbook Using Windows PowerShell

The following sample commands show how to replace the existing contents of a runbook with the contents of a script file. Note that this is the same sample procedure as in [To import a runbook from a script file with Windows PowerShell](/documentation/articles/automation-creating-importing-runbook/#ImportRunbookScriptPS).

    $automationAccountName = "MyAutomationAccount"
    $runbookName = "Sample-TestRunbook"
    $scriptPath = "c:\runbooks\Sample-TestRunbook.ps1"

    Set-AzureAutomationRunbookDefinition -AutomationAccountName $automationAccountName -Name $runbookName -Path $scriptPath -Overwrite
    Publish-AzureAutomationRunbook -AutomationAccountName $automationAccountName -Name $runbookName

## Related articles

- [Creating or importing a runbook in Azure Automation](/documentation/articles/automation-creating-importing-runbook/)
- [Learning PowerShell workflow](/documentation/articles/automation-powershell-workflow/)
- [Certificates](/documentation/articles/automation-certificates/)
- [Connections](/documentation/articles/automation-connections/)
- [Credentials](/documentation/articles/automation-credentials/)
- [Schedules](/documentation/articles/automation-schedules/)
- [Variables](/documentation/articles/automation-variables/)