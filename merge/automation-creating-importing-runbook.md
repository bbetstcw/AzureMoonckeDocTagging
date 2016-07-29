<properties
	pageTitle="Creating or importing a runbook in Azure Automation"
	description="This article describes how to create a new runbook in Azure Automation or import one from a file."
	services="automation"
	documentationCenter=""
	authors="mgoedtel"
	manager="jwhit"
	editor="tysonn" />
<tags
	ms.service="automation"
	ms.date="05/31/2016"
	wacn.date=""/>

# Creating or importing a runbook in Azure Automation

You can add a runbook to Azure Automation by either [creating a new one](#creating-a-new-runbook) or by importing an existing runbook from a file or from the [Runbook Gallery](/documentation/articles/automation-runbook-gallery/). This article provides information on creating and importing runbooks from a file.  You can get all of the details on accessing community runbooks and modules in [Runbook and module galleries for Azure Automation](/documentation/articles/automation-runbook-gallery/).

## <a name="creating-a-new-runbook"></a> Creating a new runbook

[AZURE.ACOM]{

You can create a new runbook in Azure Automation using one of the Azure portals or Windows PowerShell. Once the runbook has been created, you can edit it using information in [Learning PowerShell Workflow](/documentation/articles/automation-powershell-workflow/) and [Graphical authoring in Azure Automation](/documentation/articles/automation-graphical-authoring-intro/).

[AZURE.ACOM]}

[AZURE.ACN]{

You can create a new runbook in Azure Automation using one of the Azure portals or Windows PowerShell. Once the runbook has been created, you can edit it using information in [Learning PowerShell Workflow](/documentation/articles/automation-powershell-workflow/).

[AZURE.ACN]}

### To create a new Azure Automation runbook with the Azure Classic Management Portal

[AZURE.ACOM]{

You can only work with [PowerShell Workflow runbooks](/documentation/articles/automation-runbook-types/#powershell-workflow-runbooks) in the Azure portal.

[AZURE.ACOM]}

[AZURE.ACN]{

You can only work with PowerShell Workflow runbooks in the Azure Classic Management Portal.

[AZURE.ACN]}

1. In the Azure Classic Management Portal, click, **New**, **App Services**, **Automation**, **Runbook**, **Quick Create**.
2. Enter the required information, and then click **Create**. The runbook name must start with a letter and can have letters, numbers, underscores, and dashes.
3. If you want to edit the runbook now, then click **Edit Runbook**. Otherwise, click **OK**.
4. Your new runbook will appear on the **Runbooks** tab.

[AZURE.ACOM]{

### To create a new Azure Automation runbook with the Azure portal

1. In the Azure portal, open your Automation account.
2. Click on the **Runbooks** tile to open the list of runbooks.
3. Click on the **Add a runbook** button and then **Create a new runbook**.
2. Type a **Name** for the runbook and select its [Type](/documentation/articles/automation-runbook-types/). The runbook name must start with a letter and can have letters, numbers, underscores, and dashes.
3. Click **Create** to create the runbook and open the editor.

[AZURE.ACOM]}

### To create a new Azure Automation runbook with Windows PowerShell

[AZURE.ACOM]{

You can use the [New-AzureRmAutomationRunbook](https://msdn.microsoft.com/zh-cn/library/mt619376.aspx) cmdlet to create an empty [PowerShell Workflow runbook](/documentation/articles/automation-runbook-types/#powershell-workflow-runbooks). You can either specify the **Name** parameter to create an empty runbook that you can later edit, or you can specify the **Path** parameter to import a runbook file. The **Type** parameter should also be included to specify one of the four runbook types.

[AZURE.ACOM]}

[AZURE.ACN]{

You can use the [New-AzureAutomationRunbook](https://msdn.microsoft.com/zh-cn/library/dn690272.aspx) cmdlet to create an empty PowerShell Workflow runbook. You can either specify the **Name** parameter to create an empty runbook that you can later edit, or you can specify the **Path** parameter to import a script file. 

[AZURE.ACN]}

The following sample commands show how to create a new empty runbook.

    [AZURE.ACOM]{

    New-AzureRmAutomationRunbook -AutomationAccountName MyAccount `

    -Name NewRunbook -ResourceGroupName MyResourceGroup -Type PowerShell

    [AZURE.ACOM]}

    [AZURE.ACN]{

    $automationAccountName = "MyAutomationAccount"
    $runbookName = "Sample-TestRunbook"

    New-AzureAutomationRunbook -AutomationAccountName $automationAccountName -Name $runbookName

    [AZURE.ACN]}

## <a name="ImportRunbook"></a> Importing a runbook from a file into Azure Automation

[AZURE.ACOM]{

You can create a new runbook in Azure Automation by importing a PowerShell script or PowerShell Workflow (.ps1 extension) or an exported graphical runbook (.graphrunbook).  You must specify the [type of runbook](/documentation/articles/automation-runbook-types/) that will be created from the import taking into account the following considerations.

[AZURE.ACOM]}

[AZURE.ACN]{

You can create a new runbook in Azure Automation by importing a PowerShell Workflow (.ps1 extension).

If the file contains multiple PowerShell Workflows, then the import will fail. You must save each workflow to its own file and import each separately.

[AZURE.ACN]}

- [AZURE.ACOM]{

- A .graphrunbook file may only be imported into a new [graphical runbook](/documentation/articles/automation-runbook-types/#graphical-runbooks), and graphical runbooks can only be created from a .graphrunbook file.
- A .ps1 file containing a PowerShell Workflow can only be imported into a [PowerShell Workflow runbook](/documentation/articles/automation-runbook-types/#powershell-workflow-runbooks).  If the file contains multiple PowerShell Workflows, then the import will fail. You must save each workflow to its own file and import each separately.
- A .ps1 file that does not contain a workflow can be imported into either a [PowerShell runbook](/documentation/articles/automation-runbook-types/#powershell-runbooks) or a [PowerShell Workflow runbook](/documentation/articles/automation-runbook-types/#powershell-workflow-runbooks).  If it is imported into a PowerShell Workflow runbook, then it will be converted to a workflow, and comments will be included in the runbook specifying the changes that were made.
- [AZURE.ACOM]}

### To import a runbook from a file with the Azure Classic Management Portal

[AZURE.ACOM]{

You can use the following procedure to import a script file into Azure Automation.  Note that you can only import a .ps1 file into a PowerShell Workflow runbook using this portal.  You must use the Azure portal for other types.

[AZURE.ACOM]}

[AZURE.ACN]{

You can use the following procedure to import a script file into Azure Automation.  Note that you can only import a .ps1 file into a PowerShell Workflow runbook using this portal.  

[AZURE.ACN]}

1. In the Azure Classic Management Portal, select **Automation** and then select an Automation Account.
2. Click **Import**.
3. Click **Browse for File** and locate the script file to import.
4. If you want to edit the runbook now, then click **Edit Runbook**. Otherwise, click OK.
5. The new runbook will appear on the **Runbooks** tab for the Automation Account.
6. You must [publish the runbook](#publishing-a-runbook) before you can run it.

[AZURE.ACOM]{

### To import a runbook from a file with the Azure portal
You can use the following procedure to import a script file into Azure Automation.  

>[AZURE.NOTE] Note that you can only import a .ps1 file into a PowerShell Workflow runbook using the portal.

1. In the Azure portal, open your Automation account.
2. Click on the **Runbooks** tile to open the list of runbooks.
3. Click on the **Add a runbook** button and then **Import**.
4. Click **Runbook file** to select the file to import
2. If the **Name** field is enabled, then you have the option to change it.  The runbook name must start with a letter and can have letters, numbers, underscores, and dashes.
3. The [runbook type](/documentation/articles/automation-runbook-types/) will be automatically selected, but you can change the type after taking the applicable restrictions into account. 
3. The new runbook will appear in the list of runbooks for the Automation Account.
4. You must [publish the runbook](#publishing-a-runbook) before you can run it.

>[AZURE.NOTE] After you import a graphical runbook or a graphical PowerShell workflow runbook, you have the option to convert to the other type if wanted. You can't convert to textual.

[AZURE.ACOM]}

### <a name="ImportRunbookScriptPS"></a> To import a runbook from a script file with Windows PowerShell

[AZURE.ACOM]{

You can use the [Import-AzureRMAutomationRunbook](https://msdn.microsoft.com/zh-cn/library/mt603735.aspx) cmdlet to import a script file as a draft PowerShell Workflow runbook. If the runbook already exists, the import will fail unless you use the *-Force* parameter. 

The following sample commands show how to import a script file into a runbook.

    $automationAccountName =  "AutomationAccount"

    $runbookName = "Sample_TestRunbook"

    $scriptPath = "C:\Runbooks\Sample_TestRunbook.ps1"

    $RGName = "ResourceGroup"

    Import-AzureRMAutomationRunbook -Name $runbookName -Path $scriptPath `
    -ResourceGroupName $RGName -AutomationAccountName $automationAccountName `
    -Type PowerShellWorkflow 

[AZURE.ACOM]}

[AZURE.ACN]{

You can use the [Set-AzureAutomationRunbookDefinition](https://msdn.microsoft.com/zh-cn/library/dn690267.aspx) cmdlet to import a script file into the Draft version of an existing runbook. The script file must contain a single Windows PowerShell Workflow. If the runbook already has a Draft version, then the import will fail unless you use the Overwrite parameter. After the runbook has been imported, you can publish it with [Publish-AzureAutomationRunbook](https://msdn.microsoft.com/zh-cn/library/dn690266.aspx).

The following sample commands show how to import a script file into an existing runbook and then publish it.

    $automationAccountName = "AutomationAccount"

    $runbookName = "Sample-TestRunbook"

    $scriptPath = "c:\runbooks\Sample-TestRunbook.ps1"

    Set-AzureAutomationRunbookDefinition -AutomationAccountName $automationAccountName -Name $runbookName -Path $ scriptPath -Overwrite
    Publish-AzureAutomationRunbook -AutomationAccountName $automationAccountName -Name $runbookName

[AZURE.ACN]}

## <a name="publishing-a-runbook"></a> Publishing a runbook

When you create or import a new runbook, you must publish it before you can run it.  Each runbook in Automation has a Draft and a Published version. Only the Published version is available to be run, and only the Draft version can be edited. The Published version is unaffected by any changes to the Draft version. When the Draft version should be made available, then you publish it which overwrites the Published version with the Draft version.

## To publish a runbook using the Azure Classic Management Portal

1. Open the runbook in the Azure Classic Management Portal.
1. At the top of the screen, click **Author**.
1. At the bottom of the screen, click **Publish** and then **Yes** to the verification message.

[AZURE.ACOM]{

## To publish a runbook using the Azure portal

1. Open the runbook in the Azure portal.
1. Click the **Edit** button.
1. Click the **Publish** button and then **Yes** to the verification message.

[AZURE.ACOM]}

## To publish a runbook using Windows PowerShell

[AZURE.ACOM]{

You can use the [Publish-AzureRmAutomationRunbook](https://msdn.microsoft.com/zh-cn/library/mt603705.aspx) cmdlet to publish a runbook with Windows PowerShell. The following sample commands show how to publish a sample runbook.

[AZURE.ACOM]}

[AZURE.ACN]{

You can use the [Publish-AzureAutomationRunbook](https://msdn.microsoft.com/zh-cn/library/dn690266.aspx) cmdlet to publish a runbook with Windows PowerShell. The following sample commands show how to publish a sample runbook.

[AZURE.ACN]}

	$automationAccountName = "AutomationAccount"
	$runbookName = "Sample_TestRunbook"

    [AZURE.ACOM]{

    $RGName = "ResourceGroup"

	Publish-AzureRmAutomationRunbook -AutomationAccountName $automationAccountName `

	-Name $runbookName -ResourceGroupName $RGName

    [AZURE.ACOM]}

    [AZURE.ACN]{

    Publish-AzureAutomationRunbook -AutomationAccountName $automationAccountName -Name $runbookName

    [AZURE.ACN]}

## Next Steps
- To learn about how you can benefit from the Runbook and PowerShell Module Gallery, see  [Runbook and module galleries for Azure Automation](/documentation/articles/automation-runbook-gallery/)
- To learn more about editing PowerShell and PowerShell Workflow runbooks with a textual editor, see [Editing textual runbooks in Azure Automation](/documentation/articles/automation-edit-textual-runbook/)
- [AZURE.ACOM]{

- To learn more about Graphical runbook authoring, see [Graphical authoring in Azure Automation](/documentation/articles/automation-graphical-authoring-intro/)
- [AZURE.ACOM]}

